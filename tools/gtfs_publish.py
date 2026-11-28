#!/usr/bin/env python3
"""India_GTFS: every transit feed behind the reclaim.city maps, one GTFS Schedule zip each, nested by state and city.

    tools/gtfs_publish.py [REPO_DIR] [--only id,id]    write <state>/[<city>/]<feed>.zip and feeds.json (run tools/build.sh)

Each feed is the GTFS a map was built from (or an official / community feed for rail), so its route_id / stop_id are
the map's and the live GTFS-Realtime feeds use them too. Contents are republished with only these changes, each one
listed per feed in feeds.json ("changes") and in the folder's README:
  - packaging: the files at the root of the zip, only files named in the GTFS Schedule reference
  - placeholder trips dropped: a route Chalo held no timetable for was written with one trip at midnight; that trip is
    removed (it would read as a real 00:00 departure) and the route with its stops goes to routes_without_timetable.csv
  - stop times: a time more than 12 h before the previous stop's is past midnight (+24 h); an intermediate time that
    still runs backwards is cleared and marked timepoint=0; a last stop that runs backwards takes the previous time
  - calendar: a feed with no calendar gets the one its sibling feeds from the same build use
  - shapes: a trip with no shape gets the map's road-snapped line for its route (mtc_routes.geojson), when the trip's
    first and last stops lie within 300 m of the line's ends
  - feed_info.txt added when missing (publisher reclaim.city, the validity window from the calendar)
"""
import collections, csv, datetime as dt, hashlib, io, json, math, os, re, shutil, subprocess, sys, tempfile, zipfile

HOME = os.path.expanduser(os.environ.get('SOURCES', '~/Desktop/projects'))           # the project checkouts the feeds come from
SITE = os.path.expanduser(os.environ.get('MAPS_SITE', '~/Desktop/projects/maps-site'))  # the maps (route lines for shapes)
BUILD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'build')        # feeds made by tools/ (suburban rail)
REPO_URL = 'https://github.com/reclaimchennai/India_GTFS'
RAW = 'https://raw.githubusercontent.com/reclaimchennai/India_GTFS/main/'
RT = 'https://maps.reclaim.city/{}/rt/'
SPEC = {'agency.txt', 'stops.txt', 'routes.txt', 'trips.txt', 'stop_times.txt', 'calendar.txt', 'calendar_dates.txt',
        'fare_attributes.txt', 'fare_rules.txt', 'timeframes.txt', 'rider_categories.txt', 'fare_media.txt', 'fare_products.txt',
        'fare_leg_rules.txt', 'fare_leg_join_rules.txt', 'fare_transfer_rules.txt', 'areas.txt', 'stop_areas.txt', 'networks.txt',
        'route_networks.txt', 'shapes.txt', 'frequencies.txt', 'transfers.txt', 'pathways.txt', 'levels.txt', 'location_groups.txt',
        'location_group_stops.txt', 'locations.geojson', 'booking_rules.txt', 'translations.txt', 'feed_info.txt', 'attributions.txt'}
MODES = {'0': 'tram', '1': 'metro', '2': 'rail', '3': 'bus', '4': 'ferry', '5': 'cable tram', '6': 'aerial lift', '7': 'funicular',
         '11': 'trolleybus', '12': 'monorail'}
CHALO_SRC = {'name': "Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday "
                     "(Nov 2026), built into GTFS by reclaim.city", 'url': 'https://chalo.com/', 'licence': None}
CHALO_RD_SRC = {'name': "Chalo's public scheduler (production.zophop.com, the backend of GMCBL's Gurugaman app): every route's details "
                        "(stops in order, its line, every trip on a Monday and a Sunday, frequency windows expanded), Nov 2026, built into "
                        "GTFS by reclaim.city (ncr_bus pipeline/routedetails_gtfs.py; times between the ends spread by distance, timepoint=0)",
                'url': 'https://chalo.com/', 'licence': None}

# ── the catalog: id, folder in the repo, display name, state, source, map folder, realtime, extra ──
def F(fid, path, name, state, src, mapdir=None, rt=None, source=None, modes=None, note=None, kind='bus', route_type=None, drop_types=None,
      sidecar=None):
    """route_type: {route_id or '*': correct GTFS route_type}; drop_types: route_types whose trips are placeholders (moved out);
    sidecar: a CSV the source pipeline writes of routes it lists with no timetable at all (the routes_without_timetable.csv
    columns), published beside the feed"""
    return {'id': fid, 'path': path, 'name': name, 'state': state, 'src': src, 'map': mapdir, 'rt': rt, 'source': source,
            'note': note, 'kind': kind, 'route_type': route_type, 'drop_types': drop_types, 'sidecar': sidecar}

CHALO = {'agra': ('uttar-pradesh/agra', 'Agra', 'Uttar Pradesh'), 'amritsar': ('punjab/amritsar', 'Amritsar', 'Punjab'),
         'ayodhya': ('uttar-pradesh/ayodhya', 'Ayodhya', 'Uttar Pradesh'), 'bareilly': ('uttar-pradesh/bareilly', 'Bareilly', 'Uttar Pradesh'),
         'belgaum': ('karnataka/belagavi', 'Belagavi', 'Karnataka'), 'bhopal': ('madhya-pradesh/bhopal', 'Bhopal', 'Madhya Pradesh'),
         'gorakhpur': ('uttar-pradesh/gorakhpur', 'Gorakhpur', 'Uttar Pradesh'), 'guwahati': ('assam/guwahati', 'Guwahati', 'Assam'),
         'indore': ('madhya-pradesh/indore', 'Indore', 'Madhya Pradesh'), 'jabalpur': ('madhya-pradesh/jabalpur', 'Jabalpur', 'Madhya Pradesh'),
         'jaipur': ('rajasthan/jaipur', 'Jaipur', 'Rajasthan'), 'jammu': ('jammu-and-kashmir/jammu', 'Jammu', 'Jammu and Kashmir'),
         'jhansi': ('uttar-pradesh/jhansi', 'Jhansi', 'Uttar Pradesh'), 'kannur': ('kerala/kannur', 'Kannur', 'Kerala'),
         'kanpur': ('uttar-pradesh/kanpur', 'Kanpur', 'Uttar Pradesh'), 'kasaragod': ('kerala/kasaragod', 'Kasaragod', 'Kerala'),
         'kochi': ('kerala/kochi', 'Kochi', 'Kerala'), 'kottayam': ('kerala/kottayam', 'Kottayam', 'Kerala'),
         'kozhikode': ('kerala/kozhikode', 'Kozhikode', 'Kerala'), 'lucknow': ('uttar-pradesh/lucknow', 'Lucknow', 'Uttar Pradesh'),
         'mangaluru': ('karnataka/mangaluru', 'Mangaluru', 'Karnataka'), 'mathura': ('uttar-pradesh/mathura', 'Mathura', 'Uttar Pradesh'),
         'nagpur': ('maharashtra/nagpur', 'Nagpur', 'Maharashtra'), 'patna': ('bihar/patna', 'Patna', 'Bihar'),
         'prayagraj': ('uttar-pradesh/prayagraj', 'Prayagraj', 'Uttar Pradesh'), 'rourkela': ('odisha/rourkela', 'Rourkela', 'Odisha'),
         'srinagar': ('jammu-and-kashmir/srinagar', 'Srinagar', 'Jammu and Kashmir'),
         'thiruvananthapuram': ('kerala/thiruvananthapuram', 'Thiruvananthapuram', 'Kerala'),
         'thrissur': ('kerala/thrissur', 'Thrissur', 'Kerala'), 'udaipur': ('rajasthan/udaipur', 'Udaipur', 'Rajasthan'),
         'udupi': ('karnataka/udupi', 'Udupi', 'Karnataka'), 'ujjain': ('madhya-pradesh/ujjain', 'Ujjain', 'Madhya Pradesh'),
         'varanasi': ('uttar-pradesh/varanasi', 'Varanasi', 'Uttar Pradesh'), 'vijayawada': ('andhra-pradesh/vijayawada', 'Vijayawada', 'Andhra Pradesh'),
         'wayanad': ('kerala/wayanad', 'Wayanad', 'Kerala')}
FEEDS = [F(c, f'{p}/bus', n, s, f'{HOME}/chalo_cities/gtfs/{c}', c, source=CHALO_SRC) for c, (p, n, s) in CHALO.items()]
FEEDS += [
    F('ahmedabad', 'gujarat/ahmedabad/bus', 'Ahmedabad (AMTS, Janmarg BRTS, Gandhinagar GTSL)', 'Gujarat', f'{HOME}/ahmedabad_bus/gtfs/amts_gtfs.zip', 'amts', rt='amts',
      source={'name': "AMTS and Janmarg's own timetables and tracker (Amdavad ONE, amcitms.in), built into GTFS by reclaim.city; "
                      "Gandhinagar GTSL from croyla/amd-gtfs", 'url': 'https://amdavadone.in/amts/bus-tracking', 'licence': None,
              'detail': "Unofficial: AMTS and Ahmedabad Janmarg publish no GTFS. Everything for AMTS and Janmarg comes from the "
                        "operators' own backend behind the Amdavad ONE app (Amnex ITMS, mobileapi.amcitms.in): the route list "
                        "(a route id is one direction), each route's stations in order and their places, every trip of the "
                        "timetable and each stop's scheduled time on it (GetScheduelByRoute, GetScheduelDetail), and the "
                        "route's road line for shapes (GetRoutePathData, cut from the first stop to the last; no shape where "
                        "the stops do not fit a line). A stop of the route a trip passes without a time of its own is timed by "
                        "distance between its timed neighbours (timepoint=0). Ids are the live map's (route_id = the tracker's "
                        "route id, stop_id s<station id>), so the GTFS-Realtime feed and maps.reclaim.city/amts use them too. "
                        "Gandhinagar GTSL's 16 routes, not on this backend, are croyla/amd-gtfs's (MIT), as before "
                        "(ahmedabad_bus/server/timetable.py, gtfs_build.py)."},
      note="Unofficial: built from AMTS and Janmarg's own timetable and tracker (Amdavad ONE). Service is every day; the timetable has no calendar."),
    F('bengaluru', 'karnataka/bengaluru/bus', 'Bengaluru (BMTC)', 'Karnataka', f'{HOME}/bengaluru_bus/raw/bmtc_plus.zip', 'bengaluru', rt='bengaluru',
      source={'name': 'Vonter/bmtc-gtfs, plus the routes only BMTC\'s own app has (reclaim.city)', 'url': 'https://github.com/Vonter/bmtc-gtfs', 'licence': 'ODbL',
              'detail': "Unofficial GTFS for BMTC built from the official Namma BMTC app (Vonter/bmtc-gtfs, feed version 9 Nov 2026, Mobility "
                        "Database mdb-2595, ODbL; only routes with working live tracking in the app, whose timetables are known to be "
                        "inaccurate), with 296 route parents it lacks added by reclaim.city from BMTC's own route data (Namma BMTC API, "
                        "read 17 Nov 2026): route_id BMTC-API:<parent>, trip_id <working>:<HHMM>, BMTC's stations, path and one weekday's "
                        "timetable (18 Nov 2026, stops between first and last timed by distance, timepoint=0), service bmtc-api. "
                        "The five Namma Metro Pink Line feeders (MF-18J, MF-18JT, MF-18JP, MF-22HS, MF-18T, from 14 Nov 2026) run on "
                        "BMTC's notice. Directions with no BMTC timetable, and KSRTC intercity services BMTC's API lists with "
                        "placeholder run times, are left out (bengaluru_bus/pipeline/gtfs_plus.py)."}),
    F('tricity', 'chandigarh/tricity/bus', 'Chandigarh tricity (CTU: Chandigarh, Mohali, Panchkula)', 'Chandigarh', f'{HOME}/chandigarh_bus/gtfs/ctu_gtfs.zip', 'tricity', rt='tricity',
      source={'name': "CTU's published timetables and its trycityBUS tracker, built into GTFS by reclaim.city", 'url': 'https://ctucitybus.com/', 'licence': None,
              'detail': "Unofficial: CTU publishes no GTFS. Routes and stops from CTU's trycityBUS backend (Amnex): its route list and "
                        "route lines, stops in order from the trips its buses run, stop places from the GPS of buses standing at them "
                        "and CTU's station list (chandigarh_bus/network.py). Trips from CTU's timetable of local and tricity routes "
                        "as on 25 Jul 2026 (each direction's first and last bus and frequency; departures between are spread evenly) and "
                        "the airport shuttles 38 AS (timetable board at ISBT-17) and 36 AS (May 2024 timetable). Only the first stop's "
                        "time is published: later stops are estimated from CTU's running time for the route or the city speed for the "
                        "hour (timepoint=0). Route directions CTU gives no times for, and its inter-state buses, are left out "
                        "(chandigarh_bus/gtfs_build.py)."},
      note='Unofficial: built from CTU\'s timetable PDF and live tracker; times after the first stop are estimates (timepoint=0).'),
    F('davangere', 'karnataka/davangere/bus', 'Davangere (KSRTC city)', 'Karnataka', f'{HOME}/davangere_bus/raw/dvg_gtfs.zip', 'davangere'),
    F('hubballi', 'karnataka/hubballi-dharwad/bus', 'Hubballi-Dharwad (HDBRTS + city)', 'Karnataka', f'{HOME}/hubli_bus/raw/hdbrts-gtfs/gtfs.zip', 'hubballi',
      source={'name': 'croyla/hdbrts-gtfs', 'url': 'https://github.com/croyla/hdbrts-gtfs', 'licence': 'MIT-0'}),
    F('goa', 'goa/ktcl-bus', 'Goa (Kadamba Transport Corporation)', 'Goa', f'{HOME}/goa_bus/raw/goa_gtfs.zip', 'goa',
      note='The official feed\'s calendar ended on 1 Aug 2025; republished as it is.'),
    F('hyderabad', 'telangana/hyderabad/bus', 'Hyderabad (TGSRTC city, official open data)', 'Telangana', f'{HOME}/hyderabad_bus/raw/tgsrtc_gtfs_2026-02-08.zip', 'hyderabad'),
    F('vapi', 'gujarat/vapi/bus', 'Vapi (VCBS)', 'Gujarat', f'{HOME}/vapi_bus/raw/Vapi_GTFS.zip', 'vapi'),
    F('pune', 'maharashtra/pune/bus', 'Pune (PMPML)', 'Maharashtra', f'{HOME}/pune_bus/src/gtfs', 'pune',   # the build the map is drawn from (pune_bus/build.sh GTFS_REF)
      source={'name': 'croyla/pmpml-gtfs', 'url': 'https://github.com/croyla/pmpml-gtfs', 'licence': 'MIT-0'}),
    F('rajkot', 'gujarat/rajkot/bus', 'Rajkot (RRL BRTS + city)', 'Gujarat', f'{HOME}/rajkot_bus/raw/rrl-gtfs/gtfs.zip', 'rajkot',
      source={'name': 'croyla/rrl-gtfs', 'url': 'https://github.com/croyla/rrl-gtfs', 'licence': 'MIT-0'}),
    F('mumbai', 'maharashtra/mumbai/bus', 'Mumbai region bus (BEST, TMT, KDMT, VVMT)', 'Maharashtra', f'{HOME}/mumbai_bus/raw/mumbai-gtfs/gtfs.zip', 'mumbai', rt='mumbai',
      source={'name': 'croyla/mumbai-gtfs (BLRTransit)', 'url': 'https://github.com/croyla/mumbai-gtfs', 'licence': 'MIT-0'}),
    F('kolkata', 'west-bengal/kolkata/all-modes', 'Kolkata (bus, metro, suburban rail, ferry)', 'West Bengal', f'{HOME}/kolkata_bus/gtfs/all', 'kolkata', kind='multi',
      drop_types=['0'], note='Unofficial (no Kolkata operator publishes GTFS). Trams: the timetables are placeholders and most routes are suspended, so they are listed without times.'),
    F('delhi', 'delhi/bus', 'Delhi (DTC and cluster buses)', 'Delhi', os.path.expanduser('~/Downloads/delhi_buses_static_gtfs_v1.zip'), 'delhi', rt='delhi',
      source={'name': 'Delhi Transport Department / DTC, Delhi bus static GTFS v1 (Open Transit Data Delhi)', 'url': 'https://otd.delhi.gov.in/', 'licence': 'OTD Delhi terms'}),
    F('mtc', 'tamil-nadu/chennai/mtc-bus', 'Chennai MTC', 'Tamil Nadu', f'{HOME}/ChennaiGTFS/data/chennai-one-mtc-gtfs.zip', 'mapsv2', rt='mapsv2',
      source={'name': 'reclaimchennai/ChennaiGTFS, Chennai One MTC feed', 'url': 'https://github.com/reclaimchennai/ChennaiGTFS/tree/chennai-one-feeds', 'licence': None}),
    F('apsrtc', 'andhra-pradesh/apsrtc', 'APSRTC (Andhra Pradesh, statewide)', 'Andhra Pradesh', f'{HOME}/rtc-open-data/gh-apsrtc/data/apsrtc-gtfs.zip', 'apsrtc', rt='apsrtc',
      source={'name': 'reclaimchennai/apsrtc', 'url': 'https://github.com/reclaimchennai/apsrtc', 'licence': None}),
    F('tgsrtc', 'telangana/tgsrtc', 'TGSRTC (Telangana, statewide)', 'Telangana', f'{HOME}/rtc-open-data/gh-tgsrtc/data/tgsrtc-gtfs.zip', 'tgsrtc', rt='tgsrtc',
      source={'name': 'reclaimchennai/tgsrtc', 'url': 'https://github.com/reclaimchennai/tgsrtc', 'licence': None}),
    F('gurugram', 'haryana/gurugram/bus', 'Gurugram (GMCBL)', 'Haryana', f'{HOME}/ncr_bus/gtfs/gurugram', None, rt='gurugram', source=CHALO_RD_SRC),
    F('hr', 'haryana/haryana-roadways', 'Haryana Roadways (Haryana, statewide)', 'Haryana', f'{HOME}/haryana_bus/gtfs/hr_gtfs.zip', 'hr', rt='hr',
      source={'name': "Haryana Roadways' depot timetables (hartrans.gov.in) and its live tracking, built into GTFS by reclaim.city",
              'url': 'https://hartrans.gov.in/bus-time-table-depot-wise/', 'licence': None,
              'detail': "Unofficial: Haryana Roadways publishes no GTFS, no stops and no route lines. Routes and stops from the route "
                        "labels its buses carry on its live tracking (the official Haryana app's backend): each label read into its towns "
                        "in order, placed by bus-stand aliases and OpenStreetMap place names, joined by OSRM's road (haryana_bus/places.py, "
                        "network.py). Trips from the 25 official depot timetables (last updated 2 Dec 2024): every departure whose From and "
                        "To are a route's two ends. Only the departure time is published: later towns are estimated from OSRM's driving "
                        "time x 1.25 plus 3 min at each town (timepoint=0). Corridors with no timetabled departure, and private "
                        "(kilometre scheme) and other states' departures with no live Haryana Roadways route, are left out "
                        "(haryana_bus/gtfs_build.py)."},
      note="Unofficial: built from Haryana Roadways' depot timetables and live tracking; stops are towns and bus stands, times after the first are estimates (timepoint=0)."),
    F('noida', 'uttar-pradesh/noida/bus', 'Noida', 'Uttar Pradesh', f'{HOME}/ncr_bus/gtfs/noida', None, source=CHALO_SRC),
    F('ghaziabad', 'uttar-pradesh/ghaziabad/bus', 'Ghaziabad', 'Uttar Pradesh', f'{HOME}/ncr_bus/gtfs/ghaziabad', None, source=CHALO_SRC),
    F('meerut', 'uttar-pradesh/meerut/bus', 'Meerut', 'Uttar Pradesh', f'{HOME}/ncr_bus/gtfs/meerut', None, source=CHALO_SRC),
]
EXTRA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'feeds_extra.json')     # rail, metro, ferry feeds
for x in json.load(open(EXTRA)):
    x['src'] = os.path.abspath(os.path.expanduser(x['src'].replace('{build}', BUILD))); FEEDS.append(F(**x))
SIBLING_CAL = {'noida': f'{HOME}/ncr_bus/gtfs/ghaziabad/calendar.txt'}   # one all-week WK row (Gurugram's now has MS/SU too)


def read(src):
    out = {}
    if os.path.isdir(src):
        for n in os.listdir(src):
            if n in SPEC: out[n] = open(os.path.join(src, n), 'rb').read()
    else:
        z = zipfile.ZipFile(src)
        for n in z.namelist():
            b = os.path.basename(n)
            if b in SPEC and not n.startswith('__MACOSX'): out[b] = z.read(n)
    return out


def table(data, name):
    if name not in data: return [], []
    r = csv.reader(io.StringIO(data[name].decode('utf-8-sig')))
    hdr = [h.strip() for h in next(r, [])]
    return hdr, [dict(zip(hdr, row)) for row in r if row]


def put(data, name, hdr, rows):
    b = io.StringIO(); w = csv.writer(b, lineterminator='\n'); w.writerow(hdr)
    for r in rows: w.writerow([r.get(h, '') for h in hdr])
    data[name] = b.getvalue().encode()


def sec(t):
    t = (t or '').strip()
    if not t: return None
    h, m, s = t.split(':'); return int(h) * 3600 + int(m) * 60 + int(s)


def hms(x):
    return f'{x // 3600:02d}:{x % 3600 // 60:02d}:{x % 60:02d}'


def hav(a, b):
    return math.hypot((a[0] - b[0]) * 111320 * math.cos(math.radians(a[1])), (a[1] - b[1]) * 111320)


def drop_placeholders(f, data, changes, sidecar):
    nt = os.path.join(f['src'], 'notime.json') if os.path.isdir(f['src']) else None
    gone = set(json.load(open(nt))) if nt and os.path.exists(nt) else set()
    rh, routes = table(data, 'routes.txt')
    if f.get('drop_types'):
        gone |= {r['route_id'] for r in routes if r.get('route_type') in f['drop_types']}
    if not gone: return
    th, trips = table(data, 'trips.txt'); sh, sts = table(data, 'stop_times.txt')
    _, stops = table(data, 'stops.txt'); name = {s['stop_id']: s.get('stop_name', '') for s in stops}
    dead = {t['trip_id'] for t in trips if t['route_id'] in gone}
    pat = collections.defaultdict(list)
    for r in sts:
        if r['trip_id'] in dead: pat[r['trip_id']].append((int(r['stop_sequence']), r['stop_id']))
    t2r = {t['trip_id']: t['route_id'] for t in trips if t['trip_id'] in dead}
    for t, ss in pat.items():
        r = next((x for x in routes if x['route_id'] == t2r[t]), {})
        for q, s in sorted(ss):
            sidecar.append([t2r[t], r.get('route_short_name', ''), r.get('route_long_name', ''), q, s, name.get(s, '')])
    keep_st = [r for r in sts if r['trip_id'] not in dead]
    usedst = {r['stop_id'] for r in keep_st}
    sth, stops_all = table(data, 'stops.txt')
    parents = {s.get('parent_station') for s in stops_all if s['stop_id'] in usedst}
    kept_stops = [s for s in stops_all if s['stop_id'] in usedst or s['stop_id'] in parents or (s.get('location_type') or '0') not in ('0', '')]
    if len(kept_stops) < len(stops_all):
        put(data, 'stops.txt', sth, kept_stops)
        changes.append(f'{len(stops_all) - len(kept_stops)} stops served only by those routes moved with them')
    put(data, 'trips.txt', th, [t for t in trips if t['trip_id'] not in dead])
    put(data, 'routes.txt', rh, [r for r in routes if r['route_id'] not in gone])
    put(data, 'stop_times.txt', sh, keep_st)
    why = ('one placeholder trip at midnight each' if not f.get('drop_types') else
           'placeholder times, ' + ', '.join(MODES.get(t, t) for t in f['drop_types']) + ' routes')
    changes.append(f'{len(gone)} routes with no timetable ({why}) moved to routes_without_timetable.csv')
    for name_ in ('frequencies.txt',):
        if name_ in data:
            fh, fr = table(data, name_); put(data, name_, fh, [x for x in fr if x['trip_id'] not in dead])


def fix_times(data, changes):
    sh, sts = table(data, 'stop_times.txt')
    by = collections.defaultdict(list)
    for i, r in enumerate(sts): by[r['trip_id']].append(i)
    wrap = cleared = 0; touched = set(); fixed_dep = [0]
    for t, ix in by.items():
        ix.sort(key=lambda i: int(sts[i]['stop_sequence']))
        add, prev = 0, None
        for k, i in enumerate(ix):
            r = sts[i]
            a, d = sec(r.get('arrival_time')), sec(r.get('departure_time'))
            if a is None and d is None: continue
            if prev is not None and (a if a is not None else d) + add < prev - 43200:
                add += 86400; wrap += 1; touched.add(t)
            a = a + add if a is not None else None; d = d + add if d is not None else None
            if a is not None and d is not None and d < a: d = a
            v = a if a is not None else d
            if prev is not None and v < prev:
                if k == len(ix) - 1:
                    a = d = prev
                else:
                    r['arrival_time'] = r['departure_time'] = ''; r['timepoint'] = '0'; cleared += 1; touched.add(t); continue
            na, nd = hms(a) if a is not None else '', hms(d) if d is not None else ''
            if na != (r.get('arrival_time') or '').strip() or nd != (r.get('departure_time') or '').strip():
                if (r.get('arrival_time') or r.get('departure_time')) and nd != (r.get('departure_time') or '').strip() and not add: fixed_dep[0] += 1
                r['arrival_time'], r['departure_time'] = na, nd; touched.add(t)
            prev = max(prev or 0, d if d is not None else v)
    if wrap or cleared or fixed_dep[0]:
        if 'timepoint' not in sh: sh = sh + ['timepoint']
        for r in sts:
            if r.get('timepoint', '') == '': r['timepoint'] = '0' if not r.get('arrival_time') else '1'
        put(data, 'stop_times.txt', sh, sts)
        changes.append(f'stop times in {len(touched)} trips: {wrap} past-midnight times written past 24:00, '
                       f'{cleared} intermediate times that ran backwards cleared (timepoint=0), '
                       f'{fixed_dep[0]} departures before their own arrival set to the arrival')


def drop_unscheduled(data, changes):
    """trips whose service_id is in neither calendar.txt nor calendar_dates.txt never run: left out"""
    _, cal = table(data, 'calendar.txt'); _, cd = table(data, 'calendar_dates.txt')
    svc = {r['service_id'] for r in cal} | {r['service_id'] for r in cd}
    th, trips = table(data, 'trips.txt')
    dead = {t['trip_id'] for t in trips if t['service_id'] not in svc}
    if not dead: return
    put(data, 'trips.txt', th, [t for t in trips if t['trip_id'] not in dead])
    sh, sts = table(data, 'stop_times.txt'); put(data, 'stop_times.txt', sh, [r for r in sts if r['trip_id'] not in dead])
    for n in ('frequencies.txt',):
        if n in data:
            fh, fr = table(data, n); put(data, n, fh, [x for x in fr if x['trip_id'] not in dead])
    _, trips = table(data, 'trips.txt'); live = {t['route_id'] for t in trips}
    rh, routes = table(data, 'routes.txt'); put(data, 'routes.txt', rh, [r for r in routes if r['route_id'] in live])
    changes.append(f'{len(dead)} trips with a service_id in no calendar (they never run) left out')


def add_calendar(f, data, changes):
    if 'calendar.txt' in data or 'calendar_dates.txt' in data: return
    p = SIBLING_CAL.get(f['id'])
    if p and os.path.exists(p):
        data['calendar.txt'] = open(p, 'rb').read()
        changes.append('calendar.txt added (the build wrote none): the daily service of its sibling NCR feeds')


def add_shapes(f, data, changes):
    if not f['map']: return
    gp = os.path.join(SITE, f['map'], 'data', 'mtc_routes.geojson')
    if not os.path.exists(gp): return
    lines = {}
    for ft in json.load(open(gp))['features']:
        c = ft['properties'].get('code'); g = ft['geometry']
        if c and g and g['type'] == 'LineString' and len(g['coordinates']) >= 2 and c not in lines:
            lines[c] = g['coordinates']
    th, trips = table(data, 'trips.txt')
    need = [t for t in trips if not t.get('shape_id')]
    if not need: return
    _, stops = table(data, 'stops.txt'); xy = {s['stop_id']: (float(s['stop_lon']), float(s['stop_lat'])) for s in stops if s.get('stop_lat')}
    _, sts = table(data, 'stop_times.txt')
    ends = {}
    for r in sts:
        q = int(r['stop_sequence']); e = ends.setdefault(r['trip_id'], [q, r['stop_id'], q, r['stop_id']])
        if q < e[0]: e[0], e[1] = q, r['stop_id']
        if q > e[2]: e[2], e[3] = q, r['stop_id']
    sh_h, shp = table(data, 'shapes.txt')
    if not sh_h: sh_h = ['shape_id', 'shape_pt_lat', 'shape_pt_lon', 'shape_pt_sequence']
    have = {r['shape_id'] for r in shp}
    used, n = set(), 0
    for t in need:
        ln = lines.get(t['route_id']); e = ends.get(t['trip_id'])
        if not ln or not e or e[1] not in xy or e[3] not in xy: continue
        if hav(xy[e[1]], ln[0]) > 300 or hav(xy[e[3]], ln[-1]) > 300: continue
        sid = 'map-' + t['route_id']
        t['shape_id'] = sid; n += 1
        if sid not in used and sid not in have:
            used.add(sid)
            for i, (lo, la) in enumerate(ln):
                shp.append({'shape_id': sid, 'shape_pt_lat': f'{la:.6f}', 'shape_pt_lon': f'{lo:.6f}', 'shape_pt_sequence': str(i + 1)})
    if n:
        if 'shape_id' not in th: th = th + ['shape_id']
        put(data, 'trips.txt', th, trips); put(data, 'shapes.txt', sh_h, shp)
        changes.append(f'shapes for {n} of {len(need)} trips that had none: the map\'s road-snapped line for the route ({len(used)} shapes)')


def prune_shapes(data, changes):
    th, trips = table(data, 'trips.txt'); sh, shp = table(data, 'shapes.txt')
    if not shp: return
    used = {t.get('shape_id') for t in trips}
    keep = [r for r in shp if r['shape_id'] in used]
    gone = len({r['shape_id'] for r in shp}) - len({r['shape_id'] for r in keep})
    if gone:
        if keep: put(data, 'shapes.txt', sh, keep)
        else: del data['shapes.txt']
        changes.append(f'{gone} shapes no trip uses left out')


SIMPLIFY = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts', 'simplify_shapes.py')
SIMPLIFY_ARGS = ['--tol', '4', '--turn-deg', '30']   # what av-j's PR #2 used for Bengaluru: line within 4 m, sharp turns kept


# stop names as riders read them (chennai_one dataset/stop_names.py: title case keeping acronyms, certain abbreviations
# spelt out, 'X or Y' -> X), for the feeds whose source names are in capitals or carry 'or' alternatives
READABLE_NAMES = {'mtc'}


def readable_names(f, data, changes):
    if f['id'] not in READABLE_NAMES or 'stops.txt' not in data: return
    sys.path.insert(0, os.path.join(HOME, 'chennai_one', 'dataset'))
    import stop_names
    hdr, rows = table(data, 'stops.txt')
    N = stop_names.Names([r.get('stop_name', '') for r in rows]); n = 0
    for r in rows:
        new = N.display(r.get('stop_name', ''))
        n += new != r.get('stop_name'); r['stop_name'] = new
    if n:
        put(data, 'stops.txt', hdr, rows)
        changes.append(f'stop names made readable on {n:,} stops (title case, abbreviations spelt out, "X or Y" -> X)')


def simplify_shapes(data, changes):
    """Route lines thinned (scripts/simplify_shapes.py: Douglas-Peucker at 4 m, turns over 30 deg and the vertex nearest
    each stop kept, identical results merged and trips repointed). Bengaluru: 4.27M -> 1.63M points, 93.5 -> 59.8 MB."""
    if 'shapes.txt' not in data: return
    need = [n for n in ('shapes.txt', 'trips.txt', 'stops.txt', 'stop_times.txt') if n in data]
    with tempfile.TemporaryDirectory() as td:
        a, b = os.path.join(td, 'in.zip'), os.path.join(td, 'out.zip')
        with zipfile.ZipFile(a, 'w', zipfile.ZIP_STORED) as z:
            for n in need: z.writestr(n, data[n])
        r = subprocess.run([sys.executable, '-I', SIMPLIFY, a, b, *SIMPLIFY_ARGS], capture_output=True, text=True)
        if r.returncode:
            raise RuntimeError('simplify_shapes.py failed: ' + (r.stderr or r.stdout)[-400:])
        z = zipfile.ZipFile(b)
        before = len(table(data, 'shapes.txt')[1])
        data['shapes.txt'] = z.read('shapes.txt')
        if 'trips.txt' in z.namelist(): data['trips.txt'] = z.read('trips.txt')
    after = len(table(data, 'shapes.txt')[1])
    if after < before:
        changes.append(f'route lines thinned to within 4 m (scripts/simplify_shapes.py): {before:,} -> {after:,} shape points')


def window(data):
    _, cal = table(data, 'calendar.txt'); _, cd = table(data, 'calendar_dates.txt')
    ds = [r[k] for r in cal for k in ('start_date', 'end_date') if r.get(k)] + [r['date'] for r in cd if r.get('exception_type') == '1']
    return (min(ds), max(ds)) if ds else (None, None)


def add_feed_info(f, data, changes):
    if 'feed_info.txt' in data: return
    a, b = window(data)
    put(data, 'feed_info.txt', ['feed_publisher_name', 'feed_publisher_url', 'feed_lang', 'feed_start_date', 'feed_end_date', 'feed_version', 'feed_contact_url'],
        [{'feed_publisher_name': 'reclaim.city (India_GTFS)', 'feed_publisher_url': REPO_URL, 'feed_lang': 'en', 'feed_start_date': a or '',
          'feed_end_date': b or '', 'feed_version': dt.date.today().strftime('%Y%m%d'), 'feed_contact_url': REPO_URL + '/issues'}])
    changes.append('feed_info.txt added (none in the source)')


def source_of(f):
    if f['source']: return f['source']
    p = os.path.join(SITE, f['map'] or '-', 'data', 'sources.json')
    if os.path.exists(p):
        s = json.load(open(p))[0]; txt = s[2] if len(s) > 2 else ''
        lic = next((l for l in ('MIT-0', 'MIT', 'ODbL', 'CC BY 4.0', 'CC-BY', 'Apache') if re.search(r'\b' + re.escape(l) + r'\b', txt)), None)
        return {'name': s[0], 'url': s[1], 'licence': lic, 'detail': txt}
    return None


def build(f, repo):
    data = read(f['src'])
    miss = {'agency.txt', 'stops.txt', 'routes.txt', 'trips.txt', 'stop_times.txt'} - set(data)
    if miss: raise ValueError('not a GTFS feed, missing ' + ', '.join(sorted(miss)))
    changes, sidecar = ['packaging: files at the zip root, GTFS reference files only'], []
    if f.get('route_type'):
        rh, routes = table(data, 'routes.txt'); n = 0
        for r in routes:
            t = f['route_type'].get(r['route_id'], f['route_type'].get('*'))
            if t and r.get('route_type') != t: r['route_type'] = t; n += 1
        if n:
            put(data, 'routes.txt', rh, routes)
            changes.append(f'route_type corrected on {n} routes (' + ', '.join(sorted({MODES.get(v, v) for v in f['route_type'].values()})) + ')')
    drop_placeholders(f, data, changes, sidecar)
    if f.get('sidecar'):
        with open(os.path.expanduser(f['sidecar']), newline='') as fh:
            extra = [r for r in csv.reader(fh)][1:]
        sidecar += extra
        changes.append(f'{len({r[0] for r in extra})} routes the source lists with no timetable (no bus scheduled) listed in routes_without_timetable.csv')
    for n_ in [n for n in data if n not in ('agency.txt', 'stops.txt', 'routes.txt', 'trips.txt', 'stop_times.txt')]:
        if not table(data, n_)[1]:
            del data[n_]; changes.append(f'{n_} left out (header only, no rows)')
    add_calendar(f, data, changes)
    drop_unscheduled(data, changes)
    fix_times(data, changes)
    add_shapes(f, data, changes)
    prune_shapes(data, changes)
    readable_names(f, data, changes)
    simplify_shapes(data, changes)
    add_feed_info(f, data, changes)
    d = os.path.join(repo, os.path.dirname(f['path'])); os.makedirs(d, exist_ok=True)
    if not table(data, 'routes.txt')[1]:
        if sidecar:
            side = f['path'] + '.routes_without_timetable.csv'
            with open(os.path.join(repo, side), 'w', newline='') as fh:
                w = csv.writer(fh); w.writerow(['route_id', 'route_short_name', 'route_long_name', 'stop_sequence', 'stop_id', 'stop_name']); w.writerows(sidecar)
            return {'id': f['id'], 'name': f['name'], 'state': f['state'], 'path': None, 'download': None, 'mirror': None,
                    'map': f'https://maps.reclaim.city/{f["map"]}/' if f['map'] else None, 'modes': ['bus'], 'source': source_of(f),
                    'note': 'No timetable: the source holds routes and stops only, so there is no GTFS feed; the routes and their stops are in the CSV.',
                    'routes_without_timetable': side, 'changes': changes}
        raise ValueError('no routes')
    p = os.path.join(repo, f['path'] + '.zip'); tmp = p + '.tmp'
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for n in sorted(data):
            zi = zipfile.ZipInfo(n, date_time=(2026, 1, 1, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(zi, data[n])
    os.replace(tmp, p)
    side = None
    if sidecar:
        side = f['path'] + '.routes_without_timetable.csv'
        with open(os.path.join(repo, side), 'w', newline='') as fh:
            w = csv.writer(fh); w.writerow(['route_id', 'route_short_name', 'route_long_name', 'stop_sequence', 'stop_id', 'stop_name']); w.writerows(sidecar)
    _, routes = table(data, 'routes.txt'); _, ag = table(data, 'agency.txt'); _, trips = table(data, 'trips.txt')
    a, b = window(data)
    e = {'id': f['id'], 'name': f['name'], 'state': f['state'], 'path': f['path'] + '.zip',
         'download': RAW + f['path'] + '.zip', 'mirror': f'https://maps.reclaim.city/gtfs/{f["id"]}.zip',
         'map': f'https://maps.reclaim.city/{f["map"]}/' if f['map'] else None,
         'modes': sorted({MODES.get(r.get('route_type', ''), r.get('route_type', '')) for r in routes}),
         'agencies': [x.get('agency_name') for x in ag], 'routes': len(routes), 'stops': len(table(data, 'stops.txt')[1]), 'trips': len(trips),
         'shapes': len({t.get('shape_id') for t in trips if t.get('shape_id')}),
         'trips_with_shape': sum(1 for t in trips if t.get('shape_id')),
         'files': sorted(data), 'service_start': a, 'service_end': b, 'source': source_of(f), 'note': f['note'], 'changes': changes,
         'routes_without_timetable': side, 'bytes': os.path.getsize(p), 'sha256': hashlib.sha256(open(p, 'rb').read()).hexdigest()}
    if f['rt']:
        r = RT.format(f['rt'])
        e['realtime'] = {'vehicle_positions': r + 'vehicle_positions.pb', 'trip_updates': r + 'trip_updates.pb', 'status': r + 'status.json'}
    return e


def main():
    repo = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    only = set(sys.argv[sys.argv.index('--only') + 1].split(',')) if '--only' in sys.argv else None
    os.makedirs(repo, exist_ok=True)
    catp = os.path.join(repo, 'feeds.json')
    old = {e['id']: e for e in json.load(open(catp))['feeds']} if os.path.exists(catp) else {}
    cat = dict(old)
    for f in FEEDS:
        if only and f['id'] not in only: continue
        if not os.path.exists(f['src']):
            print(f'{f["id"]}: source missing ({f["src"]}), skipped'); continue
        try:
            e = build(f, repo)
        except Exception as ex:
            print(f'{f["id"]}: FAILED {type(ex).__name__} {ex}'); continue
        cat[f['id']] = e
        if not e.get('path'):
            print(f'{f["id"]:20s} no timetable: routes and stops only -> {e["routes_without_timetable"]}'); continue
        print(f'{f["id"]:20s} {e["routes"]:6d} routes {e["stops"]:6d} stops {e["trips"]:7d} trips {e["trips_with_shape"]:7d} shaped  '
              f'{e["service_start"]}..{e["service_end"]}  {e["bytes"] // 1024} KB  | ' + '; '.join(e['changes'][1:]))
    cat['osrtc'] = {'id': 'osrtc', 'name': 'OSRTC (Odisha, statewide)', 'state': 'Odisha', 'path': None,
                    'download': 'https://maps.reclaim.city/osrtc/rt/gtfs.zip', 'mirror': 'https://maps.reclaim.city/osrtc/rt/gtfs.zip',
                    'map': 'https://maps.reclaim.city/osrtc/', 'modes': ['bus'],
                    'source': {'name': 'OSRTC Track a Bus, as seen by the reclaim.city live poller', 'url': 'https://osrtc.org/', 'licence': None},
                    'note': 'Built live, rebuilt hourly from the services the tracker has shown (OSRTC publishes no GTFS); stop order exact, times indicative.',
                    'realtime': {k: RT.format('osrtc') + v for k, v in (('vehicle_positions', 'vehicle_positions.pb'),
                                 ('trip_updates', 'trip_updates.pb'), ('status', 'status.json'))}}
    feeds = sorted(cat.values(), key=lambda e: (e['state'], e['path'] or 'zz', e['id']))
    json.dump({'generated': dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'repository': REPO_URL,
               'spec': {'schedule': 'https://gtfs.org/documentation/schedule/reference/', 'realtime': 'https://gtfs.org/documentation/realtime/reference/'},
               'feeds': feeds}, open(catp, 'w'), indent=1, ensure_ascii=False)
    print(len(feeds), 'feeds ->', catp)


if __name__ == '__main__':
    main()
