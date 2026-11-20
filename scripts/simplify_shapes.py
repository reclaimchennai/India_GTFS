#!/usr/bin/env python3
"""Simplify shapes.txt in a GTFS zip (Douglas-Peucker) and write a new zip.

Usage: python3 -I simplify_shapes.py IN.zip OUT.zip [--tol METRES] [--drop-dist] [--no-stops] [--turn-deg DEG]

- Keeps first/last point of every shape and the vertex nearest each stop
  (stops of one representative trip per shape, matched in order); original shape_dist_traveled values are
  kept on retained points (still valid, since they're cumulative along the original line).
- Duplicate shapes (identical simplified geometry) are merged and trips.txt is
  rewritten to point at one canonical shape_id.
- All other files are copied unchanged. Pure stdlib.
"""
import argparse, csv, io, math, zipfile

R = 6371008.8


def simplify(pts, tol, forced=()):
    """pts: list of (x, y) metres. Returns sorted indices to keep (iterative DP).
    Indices in `forced` are always kept."""
    n = len(pts)
    if n <= 2:
        return list(range(n))
    keep = [False] * n
    keep[0] = keep[-1] = True
    for i in forced:
        keep[i] = True
    marks = [i for i, k in enumerate(keep) if k]
    stack = list(zip(marks, marks[1:]))
    tol2 = tol * tol
    while stack:
        a, b = stack.pop()
        if b <= a + 1:
            continue
        ax, ay = pts[a]
        dx, dy = pts[b][0] - ax, pts[b][1] - ay
        L2 = dx * dx + dy * dy
        best, bi = -1.0, -1
        for i in range(a + 1, b):
            px, py = pts[i][0] - ax, pts[i][1] - ay
            if L2 == 0:
                d2 = px * px + py * py
            else:
                t = max(0.0, min(1.0, (px * dx + py * dy) / L2))
                ex, ey = px - t * dx, py - t * dy
                d2 = ex * ex + ey * ey
            if d2 > best:
                best, bi = d2, i
        if best > tol2:
            keep[bi] = True
            stack.append((a, bi))
            stack.append((bi, b))
    return [i for i, k in enumerate(keep) if k]


def sharp_indices(pts, turn_deg, span=15.0):
    """Vertices where the heading changes by > turn_deg. Headings are measured
    to the nearest neighbours at least `span` metres away, so GPS jitter between
    close points isn't mistaken for a turn."""
    n = len(pts)
    out = []
    lim = math.radians(turn_deg)
    for i in range(1, n - 1):
        x, y = pts[i]
        j = i - 1
        while j > 0 and (pts[j][0] - x) ** 2 + (pts[j][1] - y) ** 2 < span * span:
            j -= 1
        k = i + 1
        while k < n - 1 and (pts[k][0] - x) ** 2 + (pts[k][1] - y) ** 2 < span * span:
            k += 1
        a1 = math.atan2(y - pts[j][1], x - pts[j][0])
        a2 = math.atan2(pts[k][1] - y, pts[k][0] - x)
        d = abs(a2 - a1)
        if d > math.pi:
            d = 2 * math.pi - d
        if d > lim:
            out.append(i)
    return out


def stop_indices(pts, stops_xy):
    """Nearest vertex index for each stop, moving forward along the shape
    (so loops/overlaps don't snap a stop to the wrong pass)."""
    out, prev = [], 0
    for sx, sy in stops_xy:
        best, bi = float("inf"), prev
        for i in range(prev, len(pts)):
            dx, dy = pts[i][0] - sx, pts[i][1] - sy
            d = dx * dx + dy * dy
            if d < best:
                best, bi = d, i
        out.append(bi)
        prev = bi
    return out


def load_stop_sequences(zin, names):
    """shape_id -> ordered [(lat, lon)] of stops of one representative trip."""
    if not {"trips.txt", "stop_times.txt", "stops.txt"} <= set(names):
        return {}
    rep = {}  # trip_id -> shape_id (first trip per shape)
    seen = set()
    with io.TextIOWrapper(zin.open("trips.txt"), encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            sid = r.get("shape_id")
            if sid and sid not in seen:
                seen.add(sid)
                rep[r["trip_id"]] = sid
    xy = {}
    with io.TextIOWrapper(zin.open("stops.txt"), encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            try:
                xy[r["stop_id"]] = (float(r["stop_lat"]), float(r["stop_lon"]))
            except (ValueError, KeyError):
                pass
    tmp = {}
    with io.TextIOWrapper(zin.open("stop_times.txt"), encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            t = r["trip_id"]
            if t in rep and r["stop_id"] in xy:
                tmp.setdefault(t, []).append((int(r["stop_sequence"]), xy[r["stop_id"]]))
    return {rep[t]: [p for _, p in sorted(v)] for t, v in tmp.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--tol", type=float, default=4.0, help="tolerance in metres (default 4)")
    ap.add_argument("--turn-deg", type=float, default=0,
                    help="also keep vertices whose heading change exceeds this many degrees (0=off; try 30)")
    ap.add_argument("--no-stops", action="store_true", help="don't force-keep points nearest stops")
    ap.add_argument("--drop-dist", action="store_true", help="drop shape_dist_traveled column")
    a = ap.parse_args()

    zin = zipfile.ZipFile(a.src)
    names = zin.namelist()
    if "shapes.txt" not in names:
        raise SystemExit("no shapes.txt in zip")

    # group shape points (kept in file order, sorted by sequence per shape)
    shapes = {}
    with io.TextIOWrapper(zin.open("shapes.txt"), encoding="utf-8-sig", newline="") as f:
        rd = csv.DictReader(f)
        fields = rd.fieldnames
        for r in rd:
            shapes.setdefault(r["shape_id"], []).append(r)
    has_dist = "shape_dist_traveled" in fields
    out_fields = [c for c in fields if not (a.drop_dist and c == "shape_dist_traveled")]

    stops_by_shape = {} if a.no_stops else load_stop_sequences(zin, names)
    n_in = n_out = 0
    canon = {}      # geometry key -> canonical shape_id
    remap = {}      # old shape_id -> canonical shape_id
    out_rows = []
    for sid, rows in shapes.items():
        rows.sort(key=lambda r: int(r["shape_pt_sequence"]))
        lat0 = math.radians(float(rows[len(rows) // 2]["shape_pt_lat"]))
        kx = R * math.cos(lat0) * math.pi / 180
        ky = R * math.pi / 180
        pts = [(float(r["shape_pt_lon"]) * kx, float(r["shape_pt_lat"]) * ky) for r in rows]
        forced = ()
        if sid in stops_by_shape:
            forced = stop_indices(pts, [(lo * kx, la * ky) for la, lo in stops_by_shape[sid]])
        if a.turn_deg > 0:
            forced = set(forced) | set(sharp_indices(pts, a.turn_deg))
        idx = simplify(pts, a.tol, forced)
        kept = [rows[i] for i in idx]
        n_in += len(rows)
        key = tuple((r["shape_pt_lat"], r["shape_pt_lon"]) for r in kept)
        if key in canon:
            remap[sid] = canon[key]
            continue
        canon[key] = sid
        remap[sid] = sid
        n_out += len(kept)
        for seq, r in enumerate(kept):
            r = dict(r)
            r["shape_pt_sequence"] = seq
            out_rows.append(r)

    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=out_fields, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(out_rows)
    shapes_txt = buf.getvalue()

    trips_txt = None
    if "trips.txt" in names:
        with io.TextIOWrapper(zin.open("trips.txt"), encoding="utf-8-sig", newline="") as f:
            rd = csv.DictReader(f)
            tf = rd.fieldnames
            rows = []
            for r in rd:
                if r.get("shape_id"):
                    r["shape_id"] = remap.get(r["shape_id"], r["shape_id"])
                rows.append(r)
        b = io.StringIO(newline="")
        w = csv.DictWriter(b, fieldnames=tf, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
        trips_txt = b.getvalue()

    with zipfile.ZipFile(a.dst, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zout:
        for n in names:
            if n == "shapes.txt":
                zout.writestr(n, shapes_txt)
            elif n == "trips.txt" and trips_txt is not None:
                zout.writestr(n, trips_txt)
            else:
                with zin.open(n) as s, zout.open(n, "w") as d:
                    while chunk := s.read(1 << 20):
                        d.write(chunk)

    print(f"shapes: {len(shapes)} -> {len(canon)}; points: {n_in} -> {n_out} "
          f"({100 * n_out / n_in:.1f}%); tol {a.tol} m")


if __name__ == "__main__":
    main()
