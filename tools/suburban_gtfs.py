#!/usr/bin/env python3
"""Suburban rail GTFS from the India Metro suburban map's data (metro2.0 src/suburban/<city>.data.ts + <city>.ts).

    suburban_gtfs.py CITY METRO2_DIR OUT_DIR

Every train of the map's timetable becomes a GTFS trip: its line is the route, its stopping pattern gives the stop
times (minutes after the first stop: departure at each stop, arrival at the last), the days it runs give its service,
its train number is trip_short_name. Shapes follow the real track between stations (RAIL_TRACKS) where the map has it,
straight lines between stations otherwise. Stations without a position are left out of the stops (and so of the trips).
Sources, per the data files' own headers: Mumbai from Rush Hour's timetables (railway working timetables, MIT);
Delhi and Kolkata from the national Indian Railways GTFS; Chennai from the Chennai One (CUMTA) suburban GTFS.
"""
import csv, datetime as dt, io, json, os, re, sys

AGENCY = {'mumbai': ('WR-CR', 'Western Railway and Central Railway (Mumbai Suburban)', 'https://indianrailways.gov.in/'),
          'delhi': ('NR', 'Northern Railway (Delhi suburban EMU/MEMU)', 'https://nr.indianrailways.gov.in/'),
          'kolkata': ('ER-SER', 'Eastern Railway and South Eastern Railway (Kolkata Suburban)', 'https://er.indianrailways.gov.in/'),
          'chennai': ('SR', 'Southern Railway (Chennai Suburban and MRTS)', 'https://sr.indianrailways.gov.in/')}


def exports(path):
    out = {}
    for ln in open(path, encoding='utf-8'):
        m = re.match(r'export const (\w+)\s*:[^=]*=\s*(.*);\s*$', ln)
        if m:
            out[m.group(1)] = json.loads(m.group(2))
    return out


def line_meta(path):
    """line id -> (English name, colour) from <city>.ts (colours may come through a spread const such as ...CR)."""
    src = open(path, encoding='utf-8').read()
    consts = {k: v for k, v in re.findall(r"(\w+)\s*=\s*\{[^}]*?color:\s*'(#[0-9a-fA-F]{6})'", src)}
    meta = {}
    keys = list(re.finditer(r"^  ([a-z0-9_]+):\s*\{", src, re.M))
    for j, m in enumerate(keys):
        body = src[m.end(): keys[j + 1].start() if j + 1 < len(keys) else m.end() + 600]
        nm = re.search(r"name:\s*\{\s*en:\s*'([^']+)'", body)
        col = re.search(r"color:\s*'(#[0-9a-fA-F]{6})'", body)
        sp = re.search(r"\.\.\.(\w+)", body)
        if nm:
            meta[m.group(1)] = (nm.group(1), (col.group(1) if col else consts.get(sp.group(1)) if sp else None))
    # array form (delhi.ts): key: ['GZ', '#b8432c', '#e57a60', { en: 'Ghaziabad Line (...)', ... }]
    for k, sh, col, nm in re.findall(r"^  ([a-z0-9_]+):\s*\['([^']*)',\s*'(#[0-9a-fA-F]{6})',[^{]*\{\s*en:\s*'([^']+)'", src, re.M):
        meta.setdefault(k, (nm, col, sh))
    return meta


def main():
    city, root, out = sys.argv[1], sys.argv[2], sys.argv[3]
    d = exports(os.path.join(root, 'src', 'suburban', f'{city}.data.ts'))
    meta = line_meta(os.path.join(root, 'src', 'suburban', f'{city}.ts'))
    lines, trips, tracks = d['SUBURBAN_LINES'], d['SUBURBAN_TRIPS'], d.get('RAIL_TRACKS', {})
    st = {s['id']: s for s in d['SUBURBAN_STATIONS'] if s.get('geo')}
    ag = AGENCY[city]
    os.makedirs(out, exist_ok=True)
    W = lambda n, h, rows: (lambda f: (csv.writer(f, lineterminator='\n').writerow(h), csv.writer(f, lineterminator='\n').writerows(rows), f.close()))(open(os.path.join(out, n), 'w', newline='', encoding='utf-8'))
    today = dt.date.today()
    hms = lambda m: f'{m // 60:02d}:{m % 60:02d}:00'
    routes, trows, strows, shapes, svcs, used = [], [], [], {}, {}, set()

    def seg(a, b):
        """track points from station a to b (ends excluded), or []"""
        k = '|'.join(sorted((a, b)))
        p = tracks.get(k)
        if not p: return []
        pts = [(p[i], p[i + 1]) for i in range(0, len(p) - 1, 2)]
        return pts if k.split('|')[0] == a else pts[::-1]

    for lid, sts in lines.items():
        tt = trips.get(lid)
        if not tt or not tt.get('trips'): continue
        m_ = meta.get(lid, (lid.replace('_', ' ').title(), None))
        name, colour = m_[0], m_[1]
        short = m_[2] if len(m_) > 2 else (lid.split('_')[0].upper() if city == 'mumbai' else '')
        routes.append([lid, ag[0], short, name, 2, (colour or '').lstrip('#'), 'FFFFFF' if colour else ''])
        for pi, pat in enumerate(tt['patterns']):
            ids = [sts[i] for i in pat['stops']]
            # the shape: every station of the line between consecutive stops (fast trains skip some), with the track
            full = []
            for a, b in zip(pat['stops'], pat['stops'][1:]):
                step = 1 if b > a else -1
                full += [sts[i] for i in range(a, b, step)]
            full.append(sts[pat['stops'][-1]])
            pts = []
            for k, s in enumerate(full):
                if s in st: pts.append(tuple(st[s]['geo']))
                if k + 1 < len(full): pts += seg(s, full[k + 1])
            if len(pts) >= 2: shapes[f'{lid}-p{pi}'] = pts
        for ti, t in enumerate(tt['trips']):
            pi, start, days, num = t[0], t[1], t[2], t[3]
            pat = tt['patterns'][pi]
            if not days & 127: continue                                  # runs on no day
            sid = 'D' + ''.join('1' if days >> b & 1 else '0' for b in range(7))
            svcs[sid] = days
            ids = [(sts[i], m) for i, m in zip(pat['stops'], pat['at'])]
            ids = [(s, m) for s, m in ids if s in st]
            if len(ids) < 2: continue
            tid = f'{lid}-{num or ti}-{start}'
            last = st[ids[-1][0]]['name']['en']
            direction = 0 if pat['stops'][-1] > pat['stops'][0] else 1
            trows.append([lid, sid, tid, last, num, direction, f'{lid}-p{pi}' if f'{lid}-p{pi}' in shapes else ''])
            for q, (s, m) in enumerate(ids):
                strows.append([tid, hms(start + m), hms(start + m), s, q + 1]); used.add(s)
    W('agency.txt', ['agency_id', 'agency_name', 'agency_url', 'agency_timezone', 'agency_lang'], [[ag[0], ag[1], ag[2], 'Asia/Kolkata', 'en']])
    W('routes.txt', ['route_id', 'agency_id', 'route_short_name', 'route_long_name', 'route_type', 'route_color', 'route_text_color'], routes)
    W('stops.txt', ['stop_id', 'stop_name', 'stop_lat', 'stop_lon', 'location_type'],
      [[s, st[s]['name']['en'], st[s]['geo'][0], st[s]['geo'][1], 0] for s in sorted(used)])
    W('trips.txt', ['route_id', 'service_id', 'trip_id', 'trip_headsign', 'trip_short_name', 'direction_id', 'shape_id'], trows)
    W('stop_times.txt', ['trip_id', 'arrival_time', 'departure_time', 'stop_id', 'stop_sequence'], strows)
    W('calendar.txt', ['service_id', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'start_date', 'end_date'],
      [[s] + [b >> i & 1 for i in range(7)] + [today.strftime('%Y%m%d'), (today + dt.timedelta(days=365)).strftime('%Y%m%d')] for s, b in sorted(svcs.items())])
    usedsh = {t[6] for t in trows if t[6]}
    W('shapes.txt', ['shape_id', 'shape_pt_lat', 'shape_pt_lon', 'shape_pt_sequence'],
      [[k, f'{la:.6f}', f'{lo:.6f}', i + 1] for k, pts in shapes.items() if k in usedsh for i, (la, lo) in enumerate(pts)])
    # translations: the stations' other-language names (Marathi, Hindi, Bengali, Tamil, Urdu)
    tr = [['stops', 'stop_name', lang, nm, s] for s in sorted(used) for lang, nm in st[s]['name'].items() if lang != 'en' and nm]
    if tr:
        W('translations.txt', ['table_name', 'field_name', 'language', 'translation', 'record_id'], tr)
    print(f'{city}: {len(routes)} lines, {len(used)} stations, {len(trows)} trains, {len(usedsh)} shapes -> {out}')


if __name__ == '__main__':
    main()
