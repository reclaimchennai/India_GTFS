#!/usr/bin/env python3
"""Measure how far a simplified GTFS zip's shapes deviate from the original.

Usage: python3 -I measure_deviation.py ORIG.zip SIMPLIFIED.zip [--sample N]

Reports (metres):
- line deviation: distance from every removed original point to the simplified line
  (max / mean / p99 / p99.9, and the worst shape)
- stop offset: distance from stops (one trip per shape, sample of N shapes) to the
  original line vs the simplified line
"""
import argparse, csv, io, math, random, zipfile

R = 6371008.8


def rows(z, name):
    with io.TextIOWrapper(z.open(name), encoding="utf-8-sig", newline="") as f:
        yield from csv.DictReader(f)


def load_shapes(z):
    d = {}
    for r in rows(z, "shapes.txt"):
        d.setdefault(r["shape_id"], []).append(
            (int(r["shape_pt_sequence"]), float(r["shape_pt_lat"]), float(r["shape_pt_lon"])))
    return {k: [(la, lo) for _, la, lo in sorted(v)] for k, v in d.items()}


def seg_dist(px, py, ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    if L2 == 0:
        return math.hypot(px - ax, py - ay)
    t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / L2))
    return math.hypot(px - ax - t * dx, py - ay - t * dy)


def project(pts, lat0):
    kx = R * math.cos(math.radians(lat0)) * math.pi / 180
    ky = R * math.pi / 180
    return [(lo * kx, la * ky) for la, lo in pts], kx, ky


def line_dev(orig, simp):
    """Max/each deviation of original points from simplified chords (simp is a subsequence of orig)."""
    lat0 = orig[len(orig) // 2][0]
    o, _, _ = project(orig, lat0)
    s_ll = {}
    for i, p in enumerate(simp):
        s_ll[i] = p
    # locate simplified vertices in original, moving forward
    idx, j = [], 0
    for p in simp:
        while j < len(orig) and orig[j] != p:
            j += 1
        if j == len(orig):
            return None  # not a subsequence
        idx.append(j)
    devs = []
    for a, b in zip(idx, idx[1:]):
        for i in range(a + 1, b):
            devs.append(seg_dist(*o[i], *o[a], *o[b]))
    return devs


def poly_dist(pt, poly):
    return min(seg_dist(pt[0], pt[1], *poly[i], *poly[i + 1]) for i in range(len(poly) - 1))


def pct(v, q):
    v = sorted(v)
    return v[min(len(v) - 1, int(q * len(v)))] if v else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("orig")
    ap.add_argument("simp")
    ap.add_argument("--sample", type=int, default=400)
    a = ap.parse_args()
    zo, zs = zipfile.ZipFile(a.orig), zipfile.ZipFile(a.simp)

    so, ss = load_shapes(zo), load_shapes(zs)
    # old shape_id -> new shape_id, and one representative trip per old shape
    new_of = {r["trip_id"]: r["shape_id"] for r in rows(zs, "trips.txt") if r.get("shape_id")}
    rep, remap = {}, {}
    for r in rows(zo, "trips.txt"):
        sid = r.get("shape_id")
        if sid and r["trip_id"] in new_of:
            remap.setdefault(sid, new_of[r["trip_id"]])
            rep.setdefault(sid, r["trip_id"])

    alld, worst = [], (0, None)
    bad = 0
    for sid, orig in so.items():
        simp = ss.get(remap.get(sid))
        devs = line_dev(orig, simp) if simp else None
        if devs is None:
            bad += 1
            continue
        alld += devs
        if devs and max(devs) > worst[0]:
            worst = (max(devs), sid)
    print(f"shapes compared: {len(so) - bad}/{len(so)}  removed points measured: {len(alld)}")
    print(f"line deviation (m): max {max(alld):.2f}  mean {sum(alld)/len(alld):.2f}  "
          f"p99 {pct(alld, .99):.2f}  p99.9 {pct(alld, .999):.2f}  worst shape {worst[1]}")

    # stops vs line
    random.seed(1)
    pick = set(random.sample(sorted(rep), min(a.sample, len(rep))))
    trip_shape = {rep[s]: s for s in pick}
    xy = {r["stop_id"]: (float(r["stop_lat"]), float(r["stop_lon"])) for r in rows(zo, "stops.txt")
          if r["stop_lat"]}
    stops = {}
    for r in rows(zo, "stop_times.txt"):
        t = r["trip_id"]
        if t in trip_shape and r["stop_id"] in xy:
            stops.setdefault(trip_shape[t], set()).add(r["stop_id"])
    do, ds = [], []
    for sid, ids in stops.items():
        orig, simp = so[sid], ss[remap[sid]]
        lat0 = orig[len(orig) // 2][0]
        po, kx, ky = project(orig, lat0)
        ps, _, _ = project(simp, lat0)
        for st in ids:
            la, lo = xy[st]
            pt = (lo * kx, la * ky)
            do.append(poly_dist(pt, po))
            ds.append(poly_dist(pt, ps))
    diff = [b - a_ for a_, b in zip(do, ds)]
    print(f"stops measured: {len(do)} (from {len(stops)} shapes)")
    print(f"stop->line (m) original:   mean {sum(do)/len(do):.2f}  p95 {pct(do, .95):.2f}  max {max(do):.2f}")
    print(f"stop->line (m) simplified: mean {sum(ds)/len(ds):.2f}  p95 {pct(ds, .95):.2f}  max {max(ds):.2f}")
    print(f"added by simplification:   mean {sum(diff)/len(diff):.2f}  p99 {pct(diff, .99):.2f}  max {max(diff):.2f}")


if __name__ == "__main__":
    main()
