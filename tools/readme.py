#!/usr/bin/env python3
"""README.md (the whole repository) and <state>/README.md (each state's feeds in full) from feeds.json."""
import collections, json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
cat = json.load(open(os.path.join(ROOT, 'feeds.json')))
feeds = cat['feeds']
MB = lambda b: f'{b / 1048576:.1f} MB' if b else ''
D = lambda s: f'{s[:4]}-{s[4:6]}-{s[6:]}' if s and len(s) == 8 else (s or '')
num = lambda n: f'{n:,}' if isinstance(n, int) else ''


def dl(e):
    if e.get('path'):
        return f'[{os.path.basename(e["path"])}]({e["path"]})'
    if e.get('download'):
        return f'[gtfs.zip]({e["download"]})'
    return '—'


def state_dir(e):
    p = e.get('path') or e.get('routes_without_timetable')
    return p.split('/')[0] if p else e['state'].lower().replace(' ', '-')


by_state = collections.defaultdict(list)
for e in feeds:
    by_state[e['state']].append(e)
live = [e for e in feeds if e.get('realtime')]
tot = lambda k: sum(e.get(k) or 0 for e in feeds)

# ── per-state READMEs ──
for st, es in by_state.items():
    sd = state_dir(es[0]); os.makedirs(os.path.join(ROOT, sd), exist_ok=True)
    L = [f'# {st}', '', f'Feeds in this folder: {len(es)}. Back to the [repository README](../README.md).', '']
    for e in es:
        L += [f'## {e["name"]}', '']
        rel = lambda p: os.path.relpath(p, sd) if p else None
        rows = [('Feed id', f'`{e["id"]}`'),
                ('Download', f'[{rel(e["path"])}]({rel(e["path"])}) ({MB(e.get("bytes"))}), mirror <{e["mirror"]}>' if e.get('path') else
                 (f'<{e["download"]}>' if e.get('download') else 'no GTFS (no timetable)')),
                ('Modes', ', '.join(e.get('modes') or [])), ('Agencies', ', '.join(a for a in e.get('agencies') or [] if a)),
                ('Routes / stops / trips', ' / '.join(num(e.get(k)) for k in ('routes', 'stops', 'trips')) if e.get('routes') is not None else ''),
                ('Trips with a shape', f'{num(e.get("trips_with_shape"))} ({num(e.get("shapes"))} shapes)' if e.get('trips') else ''),
                ('Service', f'{D(e.get("service_start"))} to {D(e.get("service_end"))}' if e.get('service_start') else ''),
                ('Files', ', '.join(f'`{f}`' for f in e.get('files') or [])),
                ('Map', f'<{e["map"]}>' if e.get('map') else ''),
                ('Source', (f'[{e["source"]["name"]}]({e["source"]["url"]})' if e.get('source') and e['source'].get('url') else (e.get('source') or {}).get('name', ''))),
                ('Licence', (e.get('source') or {}).get('licence') or 'none stated by the source'),
                ('sha256', f'`{e["sha256"]}`' if e.get('sha256') else '')]
        if e.get('realtime'):
            rt = e['realtime']
            rows.append(('GTFS-Realtime', f'[VehiclePositions]({rt["vehicle_positions"]}), [TripUpdates]({rt["trip_updates"]}), [status]({rt["status"]})'))
        if e.get('routes_without_timetable'):
            rows.append(('Routes without a timetable', f'[{rel(e["routes_without_timetable"])}]({rel(e["routes_without_timetable"])}) (route, stops in order; not in the GTFS)'))
        L += ['| | |', '|---|---|'] + [f'| {k} | {v} |' for k, v in rows if v] + ['']
        if e.get('note'):
            L += [f'> {e["note"]}', '']
        if e.get('changes'):
            L += ['Changes from the source (see [what we change](../README.md#what-we-change-and-why)):', ''] + [f'- {c}' for c in e['changes']] + ['']
    open(os.path.join(ROOT, sd, 'README.md'), 'w').write('\n'.join(L))

# ── the repository README ──
cov = ['| State | Feed | Modes | Routes | Stops | Trips | Service | Live | Download |', '|---|---|---|--:|--:|--:|---|:-:|---|']
for st in sorted(by_state):
    for e in sorted(by_state[st], key=lambda e: e['name']):
        cov.append(f'| [{st}]({state_dir(e)}/README.md) | {e["name"]} | {", ".join(e.get("modes") or [])} | {num(e.get("routes"))} | {num(e.get("stops"))} | '
                   f'{num(e.get("trips"))} | {D(e.get("service_start"))} – {D(e.get("service_end"))} | {"✓" if e.get("realtime") else ""} | {dl(e)} |'
                   if e.get('service_start') else
                   f'| [{st}]({state_dir(e)}/README.md) | {e["name"]} | {", ".join(e.get("modes") or [])} | {num(e.get("routes"))} | {num(e.get("stops"))} | '
                   f'{num(e.get("trips"))} | | {"✓" if e.get("realtime") else ""} | {dl(e)} |')
rt_rows = ['| Network | VehiclePositions | TripUpdates | Static GTFS (ids match) |', '|---|---|---|---|']
for e in live:
    r = e['realtime']
    rt_rows.append(f'| {e["name"]} | `{r["vehicle_positions"]}` | `{r["trip_updates"]}` | `{e["id"]}`: {dl(e)} |')

README = f'''# India_GTFS

Public transit for India in [GTFS](https://gtfs.org/): **{len([e for e in feeds if e.get("path") or e.get("download")])} feeds** covering
**{len(by_state)} states and union territories**: city buses, state transport corporations, suburban rail, MRTS, metro, RRTS and
ferries. Together they hold {num(tot("routes"))} routes, {num(tot("stops"))} stops and {num(tot("trips"))} trips, with shapes on almost every trip.
**{len(live)} networks also have live GTFS-Realtime feeds** (vehicle positions and trip updates).

Every feed is the timetable behind a map on [maps.reclaim.city](https://maps.reclaim.city/), so the ids in the
static feeds are the ids the maps and the live feeds use. The full API reference, including the live feeds, is at
**[api.reclaim.city/docs](https://api.reclaim.city/docs/#buses)**.

- [Coverage](#coverage)
- [Using the feeds](#using-the-feeds)
- [The catalog: feeds.json](#the-catalog-feedsjson)
- [Live feeds (GTFS-Realtime)](#live-feeds-gtfs-realtime)
- [Standards and validation](#standards-and-validation)
- [What we change, and why](#what-we-change-and-why)
- [Limitations](#limitations)
- [Sources and licences](#sources-and-licences)
- [Rebuilding](#rebuilding)

## Coverage

Folders are `<state>/<city>/<feed>.zip`. A feed that covers a whole state, such as APSRTC, TGSRTC or Goa's KTCL, sits in
the state's folder. Each state's README lists every feed in full: its source, licence, counts, files, checksum and the
changes we made.

{chr(10).join(cov)}

## Using the feeds

Each `.zip` is a standard GTFS Schedule feed. Any GTFS tool reads it: OpenTripPlanner, r5, gtfs-kit, partridge,
Google Transit, or a spreadsheet.

```bash
# one feed, straight from GitHub
curl -LO https://raw.githubusercontent.com/reclaimchennai/India_GTFS/main/tamil-nadu/chennai/mtc-bus.zip
# the same file from our mirror (served with CORS, for browsers)
curl -LO https://maps.reclaim.city/gtfs/mtc.zip
# every feed
git clone https://github.com/reclaimchennai/India_GTFS
```

```python
import zipfile, csv, io
z = zipfile.ZipFile("tamil-nadu/chennai/mtc-bus.zip")
routes = list(csv.DictReader(io.TextIOWrapper(z.open("routes.txt"), encoding="utf-8-sig")))
print(len(routes), routes[0]["route_short_name"])
```

All times are in `Asia/Kolkata`. Times after midnight run past `24:00:00`, as the specification says.

## The catalog: feeds.json

[`feeds.json`](feeds.json) lists every feed, and the same file is served at `https://maps.reclaim.city/gtfs/feeds.json`.

| Field | Meaning |
|---|---|
| `id` | Stable feed id, also used in the mirror URL `https://maps.reclaim.city/gtfs/<id>.zip` |
| `name`, `state` | What the feed covers |
| `path`, `download`, `mirror` | Path in this repository, the raw GitHub URL, and our mirror |
| `modes` | GTFS `route_type`s present, by name (bus, metro, rail, tram, ferry, …) |
| `agencies` | `agency_name`s in `agency.txt` |
| `routes`, `stops`, `trips`, `shapes`, `trips_with_shape` | Counts |
| `service_start`, `service_end` | The calendar's window, `YYYYMMDD` |
| `files` | The GTFS files in the zip |
| `source` | `name`, `url` and `licence` of where the data comes from |
| `changes` | Every change we made to the source data (see below) |
| `routes_without_timetable` | A CSV of routes the source lists without any times, kept out of the GTFS |
| `realtime` | For live networks: the `vehicle_positions`, `trip_updates` and `status` URLs |
| `bytes`, `sha256` | Size and checksum of the zip |

## Live feeds (GTFS-Realtime)

[GTFS-Realtime 2.0](https://gtfs.org/documentation/realtime/reference/) protocol buffers, rewritten within about 15 s of
their source changing. The full reference is at [api.reclaim.city/docs](https://api.reclaim.city/docs/#buses).

{chr(10).join(rt_rows)}

```
GET https://maps.reclaim.city/<network>/rt/vehicle_positions.pb   application/x-protobuf
GET https://maps.reclaim.city/<network>/rt/trip_updates.pb        application/x-protobuf
GET https://maps.reclaim.city/<network>/rt/vehicle_positions.json the same feed as JSON (protobuf JSON mapping)
GET https://maps.reclaim.city/<network>/rt/trip_updates.json
GET https://maps.reclaim.city/<network>/rt/status.json            freshness and match rates
```

`<network>` is one of: {", ".join(f"`{e['realtime']['status'].split('/')[3]}`" for e in live)}.

**Parameters.** There are none. Each response is the full dataset (`incrementality: FULL_DATASET`). There are no keys and
no sign-up. Responses carry `Cache-Control: public, max-age=10` and `Access-Control-Allow-Origin: *`.

**Polling.** Poll every 15–30 s; polling faster gains nothing. The header `timestamp` is the time of the newest bus
position in the feed, not the time the file was written. If a source stops, the last good feed stays up and its
timestamp stops moving, so check it before treating the data as current.

**status.json**

```json
{{"network": "delhi", "feed_time": 1794563646, "written": 1794563743, "vehicles": 3687,
 "on_trip": 2746, "on_route": 2746, "trip_updates": 2746}}
```

**How buses are matched to trips.** A `TripDescriptor` is set only when the bus is matched to a trip in the static feed.
Under the specification, a descriptor without a `trip_id` must carry `route_id`, `direction_id`, `start_date` and
`start_time` together, which an unmatched bus cannot give, so an unmatched bus has a position but no trip.

| Network | `trip_id` | Arrival times ahead |
|---|---|---|
| APSRTC | Exact: the live bus id carries the service key | The timetable plus the bus's current delay |
| TGSRTC | District services exact (`tgc-<serviceId>`); city routes the trip nearest in time (within 3 min) | Our nowcast model |
| Delhi, Chennai MTC, Mumbai | The timetabled trip whose times at the bus's next stops are nearest its predicted arrivals (within 30 min) | The map's predicted arrivals (Chennai: MTC's own), with the delay against that trip |
| Gurugram | Positions only (the source gives no arrivals to match on) | — |
| OSRTC | Exact: OSRTC's route id is the trip | OSRTC's expected times, no delay (its timetable is indicative) |

```python
# pip install gtfs-realtime-bindings
import urllib.request
from google.transit import gtfs_realtime_pb2
m = gtfs_realtime_pb2.FeedMessage()
m.ParseFromString(urllib.request.urlopen("https://maps.reclaim.city/mumbai/rt/vehicle_positions.pb").read())
for e in m.entity[:5]:
    v = e.vehicle
    print(v.vehicle.label, v.trip.trip_id, v.position.latitude, v.position.longitude)
```

## Standards and validation

- Every zip follows the [GTFS Schedule reference](https://gtfs.org/documentation/schedule/reference/). The files sit at
  the root of the zip, only files named in the reference are included, the text is UTF-8, and `feed_info.txt` is always present.
- Every live feed follows the [GTFS-Realtime reference](https://gtfs.org/documentation/realtime/reference/), including
  the TripDescriptor rule above, stop time updates in `stop_sequence` order, and times that never run backwards.
- `tools/check.py` runs a quick structural check on every build: required files and fields, references between files,
  time formats and order, and calendars.
- `tools/validate.sh` runs the canonical [MobilityData GTFS validator](https://github.com/MobilityData/gtfs-validator)
  on every feed. It writes one report per feed and a summary.

## What we change, and why

We republish each source unchanged except for the fixes below. Every fix applied to a feed is listed under `changes` in
`feeds.json` and in its state's README.

1. **Packaging.** The files go at the root of the zip, and only files named in the reference are kept (build notes are left out).
2. **Placeholder trips out.** Where Chalo's scheduler holds a route but no timetable, the source has one trip at
   midnight. That would read as a real 00:00 departure, so it is removed. The route and its stops, in order, go to
   `<feed>.routes_without_timetable.csv`. Trams in Kolkata are handled the same way, since their times are
   placeholders and most routes are suspended.
3. **Times.**
   - A stop time more than 12 h before the previous stop's has crossed midnight, so it is written past `24:00:00`.
   - An intermediate time that still runs backwards is cleared and marked `timepoint=0`.
   - A departure before its own arrival is set to the arrival.
4. **Trips that never run.** A `service_id` in no calendar is left out with its trips.
5. **Calendar.** A feed built without one gets its sibling feeds' calendar (Noida).
6. **Route types.** A wrong `route_type` is corrected. Namo Bharat RRTS was published as bus (3); it is rail (2).
7. **Shapes.** A trip with no shape gets the map's road-snapped line for its route, but only when the trip's first and
   last stops lie within 300 m of the line's ends. Its shape id starts with `map-`.
8. **`feed_info.txt`** is added where the source has none.

## Limitations

- **Unofficial feeds.** Most operators in India publish no GTFS. About 40 feeds here are built from **Chalo's public
  scheduler**: every route and stop, with the day's trips sampled every 30 minutes over one Monday. Their times are
  what Chalo shows, the same every day of the week. Routes Chalo holds no times for are listed without a timetable.
- **Expired calendars, republished as they are.** Goa's official KTCL feed ended on 1 Aug 2025. The DMRC (Delhi Metro)
  feed ended on 31 Dec 2025, though its times still match the current timetable pattern.
- **Indicative timetables:**
  - **OSRTC** is built live from Odisha's bus tracker. Its stop order is exact, but its times are the first ones seen.
  - **Kolkata Metro** times at later stations are estimated from distance.
  - **Indian Railways** has one trip per train number.
- **Suburban rail:**
  - **Mumbai** comes from the railways' working timetables, as collected by Rush Hour (Western Railway Feb 2026,
    Harbour Oct 2024, Trans-Harbour Jan 2024, Port line Dec 2025).
  - **Delhi** and **Kolkata** are cut from the national Indian Railways GTFS.
  - **Chennai**, including the MRTS, is from the Chennai One / CUMTA feed.
  - **Mumbai Metro and Monorail** have no GTFS yet.
- **Live matching.** Trip matching is by time, so where buses run every few minutes, a late bus can be matched to the
  next trip. Buses that cannot be matched have positions but no trip.
- **No fares** except where the source has them (CMRL, some community feeds). No accessibility data, and
  no `pathways.txt` except Chennai's stations.

## Sources and licences

Each feed keeps its source's licence. Where a source states none, the data is shared here for public-interest use as it
is. Check each source before commercial use.

| Feed | Source | Licence |
|---|---|---|
{chr(10).join(f'| {e["name"]} | ' + (f'[{e["source"]["name"]}]({e["source"]["url"]})' if e.get('source') and e['source'].get('url') else (e.get('source') or {}).get('name', '')) + f' | {(e.get("source") or {}).get("licence") or "none stated"} |' for e in sorted(feeds, key=lambda e: (e["state"], e["name"])))}

Shapes marked `map-` and all the changes listed above are © reclaim.city, under the same terms as the feed they are in.
Base map data © OpenStreetMap contributors (ODbL).

## Rebuilding

```bash
tools/build.sh                # every feed from its sources, then feeds.json, the READMEs and tools/check.py
tools/build.sh --only mumbai  # one feed
tools/validate.sh             # the MobilityData validator on every feed (Java 17+)
```

The tools read the source checkouts named in `tools/gtfs_publish.py` and `tools/feeds_extra.json`.

Corrections and new feeds are welcome as [issues](https://github.com/reclaimchennai/India_GTFS/issues).
'''
open(os.path.join(ROOT, 'README.md'), 'w').write(README)
print('README.md +', len(by_state), 'state READMEs')
