# India_GTFS

Public transit for India in [GTFS](https://gtfs.org/): **64 feeds** covering
**20 states and union territories**: city buses, state transport corporations, suburban rail, MRTS, metro, RRTS and
ferries. Together they hold 54,655 routes, 137,170 stops and 618,252 trips, with shapes on almost every trip.
**7 networks also have live GTFS-Realtime feeds** (vehicle positions and trip updates).

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

| State | Feed | Modes | Routes | Stops | Trips | Service | Live | Download |
|---|---|---|--:|--:|--:|---|:-:|---|
| [Andhra Pradesh](andhra-pradesh/README.md) | APSRTC (Andhra Pradesh, statewide) | bus | 5,095 | 11,156 | 54,812 | 2026-11-01 – 2027-10-31 | ✓ | [apsrtc.zip](andhra-pradesh/apsrtc.zip) |
| [Andhra Pradesh](andhra-pradesh/README.md) | Vijayawada | bus | 331 | 1,525 | 3,171 | 2026-11-03 – 2027-11-03 |  | [bus.zip](andhra-pradesh/vijayawada/bus.zip) |
| [Assam](assam/README.md) | Guwahati | bus | 522 | 2,283 | 4,272 | 2026-11-02 – 2027-11-02 |  | [bus.zip](assam/guwahati/bus.zip) |
| [Bihar](bihar/README.md) | Patna | bus | 54 | 356 | 577 | 2026-11-02 – 2027-11-02 |  | [bus.zip](bihar/patna/bus.zip) |
| [Delhi](delhi/README.md) | Delhi (DTC and cluster buses) | bus | 2,554 | 6,812 | 65,322 | 2025-01-01 – 2040-01-01 | ✓ | [bus.zip](delhi/bus.zip) |
| [Delhi](delhi/README.md) | Delhi Metro (DMRC, incl. Airport Express and Rapid Metro Gurugram) | metro | 36 | 262 | 5,438 | 2019-01-01 – 2025-12-31 |  | [metro-dmrc.zip](delhi/metro-dmrc.zip) |
| [Delhi](delhi/README.md) | Delhi NCR suburban rail (Northern Railway EMU/MEMU) | rail | 14 | 140 | 400 | 2026-11-13 – 2027-11-13 |  | [suburban-rail.zip](delhi/suburban-rail.zip) |
| [Delhi](delhi/README.md) | Namo Bharat RRTS (NCRTC, Delhi-Meerut) | rail | 2 | 16 | 130 | 2024-01-01 – 2029-01-01 |  | [rrts-namo-bharat.zip](delhi/rrts-namo-bharat.zip) |
| [Goa](goa/README.md) | Goa (Kadamba Transport Corporation) | bus | 476 | 3,255 | 3,130 | 2023-09-01 – 2025-08-01 |  | [ktcl-bus.zip](goa/ktcl-bus.zip) |
| [Gujarat](gujarat/README.md) | Ahmedabad (AMTS, Janmarg BRTS, Gandhinagar GTSL) | bus | 978 | 3,235 | 14,323 | 2026-09-30 – 2027-03-29 |  | [bus.zip](gujarat/ahmedabad/bus.zip) |
| [Gujarat](gujarat/README.md) | Rajkot (RRL BRTS + city) | bus | 271 | 760 | 3,168 | 2026-10-16 – 2027-04-14 |  | [bus.zip](gujarat/rajkot/bus.zip) |
| [Gujarat](gujarat/README.md) | Vapi (VCBS) | bus | 22 | 91 | 461 | 2026-01-01 – 2027-12-31 |  | [bus.zip](gujarat/vapi/bus.zip) |
| [Haryana](haryana/README.md) | Gurugram (GMCBL) | bus | 137 | 1,086 | 1,807 | 2026-10-01 – 2027-10-01 | ✓ | [bus.zip](haryana/gurugram/bus.zip) |
| [India](india/README.md) | Indian Railways (all-India trains, incl. EMU/MEMU) | rail | 10,389 | 8,550 | 10,389 | 2025-01-01 – 2099-12-31 |  | [indian-railways.zip](india/indian-railways.zip) |
| [Jammu and Kashmir](jammu-and-kashmir/README.md) | Jammu | bus | 248 | 850 | 1,880 | 2026-11-02 – 2027-11-02 |  | [bus.zip](jammu-and-kashmir/jammu/bus.zip) |
| [Jammu and Kashmir](jammu-and-kashmir/README.md) | Srinagar | bus | 168 | 1,065 | 2,404 | 2026-11-02 – 2027-11-02 |  | [bus.zip](jammu-and-kashmir/srinagar/bus.zip) |
| [Karnataka](karnataka/README.md) | Belagavi | bus | 33 | 242 | 331 | 2026-11-02 – 2027-11-02 |  | [bus.zip](karnataka/belagavi/bus.zip) |
| [Karnataka](karnataka/README.md) | Bengaluru (BMTC) | bus | 5,063 | 10,128 | 69,642 | 2026-11-09 – 2027-11-09 |  | [bus.zip](karnataka/bengaluru/bus.zip) |
| [Karnataka](karnataka/README.md) | Davangere (KSRTC city) | bus | 93 | 146 | 586 | 2026-06-02 – 2026-11-29 |  | [bus.zip](karnataka/davangere/bus.zip) |
| [Karnataka](karnataka/README.md) | Hubballi-Dharwad (HDBRTS + city) | bus | 632 | 2,332 | 8,669 | 2026-08-24 – 2027-02-20 |  | [bus.zip](karnataka/hubballi-dharwad/bus.zip) |
| [Karnataka](karnataka/README.md) | Mangaluru | bus | 208 | 1,394 | 2,079 | 2026-11-02 – 2027-11-02 |  | [bus.zip](karnataka/mangaluru/bus.zip) |
| [Karnataka](karnataka/README.md) | Udupi | bus | 191 | 1,392 | 2,561 | 2026-11-02 – 2027-11-02 |  | [bus.zip](karnataka/udupi/bus.zip) |
| [Kerala](kerala/README.md) | Kannur | bus | 510 | 1,808 | 2,995 | 2026-11-03 – 2027-11-03 |  | [bus.zip](kerala/kannur/bus.zip) |
| [Kerala](kerala/README.md) | Kasaragod | bus | 302 | 1,920 | 1,760 | 2026-11-02 – 2027-11-02 |  | [bus.zip](kerala/kasaragod/bus.zip) |
| [Kerala](kerala/README.md) | Kochi | bus | 1,005 | 548 | 3,528 | 2026-11-03 – 2027-11-03 |  | [bus.zip](kerala/kochi/bus.zip) |
| [Kerala](kerala/README.md) | Kottayam | bus | 1,380 | 2,063 | 9,512 | 2026-11-03 – 2027-11-03 |  | [bus.zip](kerala/kottayam/bus.zip) |
| [Kerala](kerala/README.md) | Kozhikode | bus | 1,103 | 2,144 | 7,331 | 2026-11-02 – 2027-11-02 |  | [bus.zip](kerala/kozhikode/bus.zip) |
| [Kerala](kerala/README.md) | Thiruvananthapuram | bus | 3,247 | 2,579 | 26,519 | 2026-11-03 – 2027-11-03 |  | [bus.zip](kerala/thiruvananthapuram/bus.zip) |
| [Kerala](kerala/README.md) | Thrissur | bus | 1,571 | 2,122 | 11,209 | 2026-11-02 – 2027-11-02 |  | [bus.zip](kerala/thrissur/bus.zip) |
| [Kerala](kerala/README.md) | Wayanad | bus | 969 | 4,483 | 6,895 | 2026-11-02 – 2027-11-02 |  | [bus.zip](kerala/wayanad/bus.zip) |
| [Madhya Pradesh](madhya-pradesh/README.md) | Bhopal | bus | 32 | 492 | 598 | 2026-11-02 – 2027-11-02 |  | [bus.zip](madhya-pradesh/bhopal/bus.zip) |
| [Madhya Pradesh](madhya-pradesh/README.md) | Indore | bus | 45 | 919 | 796 | 2026-11-02 – 2027-11-02 |  | [bus.zip](madhya-pradesh/indore/bus.zip) |
| [Madhya Pradesh](madhya-pradesh/README.md) | Jabalpur | bus | 43 | 445 | 880 | 2026-11-02 – 2027-11-02 |  | [bus.zip](madhya-pradesh/jabalpur/bus.zip) |
| [Madhya Pradesh](madhya-pradesh/README.md) | Ujjain | bus | 3 | 26 | 45 | 2026-11-02 – 2027-11-02 |  | [bus.zip](madhya-pradesh/ujjain/bus.zip) |
| [Maharashtra](maharashtra/README.md) | Mumbai region bus (BEST, TMT, KDMT, VVMT) | bus | 1,609 | 10,279 | 99,080 | 2026-08-19 – 2027-02-15 | ✓ | [bus.zip](maharashtra/mumbai/bus.zip) |
| [Maharashtra](maharashtra/README.md) | Mumbai suburban rail (Western, Central, Harbour, Trans-Harbour, Uran) | rail | 9 | 123 | 3,721 | 2026-11-13 – 2027-11-13 |  | [suburban-rail.zip](maharashtra/mumbai/suburban-rail.zip) |
| [Maharashtra](maharashtra/README.md) | Nagpur | bus | 900 | 3,896 | 8,619 | 2026-11-03 – 2027-11-03 |  | [bus.zip](maharashtra/nagpur/bus.zip) |
| [Maharashtra](maharashtra/README.md) | Pune (PMPML) | bus | 628 | 6,745 | 10,128 | 2026-10-07 – 2027-04-05 |  | [bus.zip](maharashtra/pune/bus.zip) |
| [Odisha](odisha/README.md) | OSRTC (Odisha, statewide) | bus |  |  |  | | ✓ | [gtfs.zip](https://maps.reclaim.city/osrtc/rt/gtfs.zip) |
| [Odisha](odisha/README.md) | Rourkela | bus | 160 | 1,081 | 1,042 | 2026-11-02 – 2027-11-02 |  | [bus.zip](odisha/rourkela/bus.zip) |
| [Punjab](punjab/README.md) | Amritsar | bus |  |  |  | |  | — |
| [Rajasthan](rajasthan/README.md) | Jaipur | bus | 60 | 903 | 1,421 | 2026-11-02 – 2027-11-02 |  | [bus.zip](rajasthan/jaipur/bus.zip) |
| [Rajasthan](rajasthan/README.md) | Udaipur | bus | 28 | 243 | 303 | 2026-11-02 – 2027-11-02 |  | [bus.zip](rajasthan/udaipur/bus.zip) |
| [Tamil Nadu](tamil-nadu/README.md) | Chennai MTC | bus | 970 | 3,393 | 48,132 | 2026-01-01 – 2027-12-31 | ✓ | [mtc-bus.zip](tamil-nadu/chennai/mtc-bus.zip) |
| [Tamil Nadu](tamil-nadu/README.md) | Chennai Metro (CMRL) | metro | 3 | 294 | 749 | 2026-01-01 – 2027-12-31 |  | [metro-cmrl.zip](tamil-nadu/chennai/metro-cmrl.zip) |
| [Tamil Nadu](tamil-nadu/README.md) | Chennai suburban rail and MRTS (Southern Railway) | rail | 753 | 388 | 756 | 2026-01-01 – 2027-12-31 |  | [suburban-rail-mrts.zip](tamil-nadu/chennai/suburban-rail-mrts.zip) |
| [Telangana](telangana/README.md) | Hyderabad (TGSRTC city, official open data) | bus | 1,031 | 5,028 | 44,892 | 2026-02-01 – 2031-02-01 |  | [bus.zip](telangana/hyderabad/bus.zip) |
| [Telangana](telangana/README.md) | TGSRTC (Telangana, statewide) | bus | 7,881 | 14,811 | 56,977 | 2026-09-01 – 2031-09-01 | ✓ | [tgsrtc.zip](telangana/tgsrtc.zip) |
| [Uttar Pradesh](uttar-pradesh/README.md) | Agra | bus | 44 | 384 | 451 | 2026-11-02 – 2027-11-02 |  | [bus.zip](uttar-pradesh/agra/bus.zip) |
| [Uttar Pradesh](uttar-pradesh/README.md) | Ayodhya | bus | 10 | 123 | 150 | 2026-11-02 – 2027-11-02 |  | [bus.zip](uttar-pradesh/ayodhya/bus.zip) |
| [Uttar Pradesh](uttar-pradesh/README.md) | Bareilly | bus | 6 | 125 | 70 | 2026-11-02 – 2027-11-02 |  | [bus.zip](uttar-pradesh/bareilly/bus.zip) |
| [Uttar Pradesh](uttar-pradesh/README.md) | Ghaziabad | bus | 32 | 224 | 471 | 2026-10-01 – 2027-10-01 |  | [bus.zip](uttar-pradesh/ghaziabad/bus.zip) |
| [Uttar Pradesh](uttar-pradesh/README.md) | Gorakhpur | bus | 8 | 155 | 60 | 2026-11-02 – 2027-11-02 |  | [bus.zip](uttar-pradesh/gorakhpur/bus.zip) |
| [Uttar Pradesh](uttar-pradesh/README.md) | Jhansi | bus | 21 | 82 | 260 | 2026-11-02 – 2027-11-02 |  | [bus.zip](uttar-pradesh/jhansi/bus.zip) |
| [Uttar Pradesh](uttar-pradesh/README.md) | Kanpur | bus | 30 | 752 | 328 | 2026-11-02 – 2027-11-02 |  | [bus.zip](uttar-pradesh/kanpur/bus.zip) |
| [Uttar Pradesh](uttar-pradesh/README.md) | Lucknow | bus | 32 | 707 | 444 | 2026-11-02 – 2027-11-02 |  | [bus.zip](uttar-pradesh/lucknow/bus.zip) |
| [Uttar Pradesh](uttar-pradesh/README.md) | Mathura | bus | 24 | 220 | 302 | 2026-11-02 – 2027-11-02 |  | [bus.zip](uttar-pradesh/mathura/bus.zip) |
| [Uttar Pradesh](uttar-pradesh/README.md) | Meerut | bus | 28 | 260 | 293 | 2026-10-01 – 2027-10-01 |  | [bus.zip](uttar-pradesh/meerut/bus.zip) |
| [Uttar Pradesh](uttar-pradesh/README.md) | Noida | bus | 24 | 34 | 330 | 2026-10-01 – 2027-10-01 |  | [bus.zip](uttar-pradesh/noida/bus.zip) |
| [Uttar Pradesh](uttar-pradesh/README.md) | Prayagraj | bus | 15 | 238 | 115 | 2026-11-02 – 2027-11-02 |  | [bus.zip](uttar-pradesh/prayagraj/bus.zip) |
| [Uttar Pradesh](uttar-pradesh/README.md) | Varanasi | bus | 123 | 358 | 688 | 2026-11-02 – 2027-11-02 |  | [bus.zip](uttar-pradesh/varanasi/bus.zip) |
| [West Bengal](west-bengal/README.md) | Kolkata (bus, metro, suburban rail, ferry) | bus, ferry, metro, rail | 2,449 | 9,208 | 6,646 | 2026-11-01 – 2027-10-31 |  | [all-modes.zip](west-bengal/kolkata/all-modes.zip) |
| [West Bengal](west-bengal/README.md) | Kolkata Hooghly ferries | ferry | 20 | 30 | 40 | 2026-11-01 – 2027-10-31 |  | [ferry.zip](west-bengal/kolkata/ferry.zip) |
| [West Bengal](west-bengal/README.md) | Kolkata Metro | metro | 5 | 55 | 1,704 | 2026-11-01 – 2027-10-31 |  | [metro.zip](west-bengal/kolkata/metro.zip) |
| [West Bengal](west-bengal/README.md) | Kolkata suburban rail (Eastern and South Eastern Railway) | rail | 25 | 406 | 2,460 | 2026-11-01 – 2027-10-31 |  | [suburban-rail.zip](west-bengal/kolkata/suburban-rail.zip) |

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

| Network | VehiclePositions | TripUpdates | Static GTFS (ids match) |
|---|---|---|---|
| APSRTC (Andhra Pradesh, statewide) | `https://maps.reclaim.city/apsrtc/rt/vehicle_positions.pb` | `https://maps.reclaim.city/apsrtc/rt/trip_updates.pb` | `apsrtc`: [apsrtc.zip](andhra-pradesh/apsrtc.zip) |
| Delhi (DTC and cluster buses) | `https://maps.reclaim.city/delhi/rt/vehicle_positions.pb` | `https://maps.reclaim.city/delhi/rt/trip_updates.pb` | `delhi`: [bus.zip](delhi/bus.zip) |
| Gurugram (GMCBL) | `https://maps.reclaim.city/gurugram/rt/vehicle_positions.pb` | `https://maps.reclaim.city/gurugram/rt/trip_updates.pb` | `gurugram`: [bus.zip](haryana/gurugram/bus.zip) |
| Mumbai region bus (BEST, TMT, KDMT, VVMT) | `https://maps.reclaim.city/mumbai/rt/vehicle_positions.pb` | `https://maps.reclaim.city/mumbai/rt/trip_updates.pb` | `mumbai`: [bus.zip](maharashtra/mumbai/bus.zip) |
| OSRTC (Odisha, statewide) | `https://maps.reclaim.city/osrtc/rt/vehicle_positions.pb` | `https://maps.reclaim.city/osrtc/rt/trip_updates.pb` | `osrtc`: [gtfs.zip](https://maps.reclaim.city/osrtc/rt/gtfs.zip) |
| Chennai MTC | `https://maps.reclaim.city/mapsv2/rt/vehicle_positions.pb` | `https://maps.reclaim.city/mapsv2/rt/trip_updates.pb` | `mtc`: [mtc-bus.zip](tamil-nadu/chennai/mtc-bus.zip) |
| TGSRTC (Telangana, statewide) | `https://maps.reclaim.city/tgsrtc/rt/vehicle_positions.pb` | `https://maps.reclaim.city/tgsrtc/rt/trip_updates.pb` | `tgsrtc`: [tgsrtc.zip](telangana/tgsrtc.zip) |

```
GET https://maps.reclaim.city/<network>/rt/vehicle_positions.pb   application/x-protobuf
GET https://maps.reclaim.city/<network>/rt/trip_updates.pb        application/x-protobuf
GET https://maps.reclaim.city/<network>/rt/vehicle_positions.json the same feed as JSON (protobuf JSON mapping)
GET https://maps.reclaim.city/<network>/rt/trip_updates.json
GET https://maps.reclaim.city/<network>/rt/status.json            freshness and match rates
```

`<network>` is one of: `apsrtc`, `delhi`, `gurugram`, `mumbai`, `osrtc`, `mapsv2`, `tgsrtc`.

**Parameters.** There are none. Each response is the full dataset (`incrementality: FULL_DATASET`). There are no keys and
no sign-up. Responses carry `Cache-Control: public, max-age=10` and `Access-Control-Allow-Origin: *`.

**Polling.** Poll every 15–30 s; polling faster gains nothing. The header `timestamp` is the time of the newest bus
position in the feed, not the time the file was written. If a source stops, the last good feed stays up and its
timestamp stops moving, so check it before treating the data as current.

**status.json**

```json
{"network": "delhi", "feed_time": 1794563646, "written": 1794563743, "vehicles": 3687,
 "on_trip": 2746, "on_route": 2746, "trip_updates": 2746}
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
| APSRTC (Andhra Pradesh, statewide) | [reclaimchennai/apsrtc](https://github.com/reclaimchennai/apsrtc) | none stated |
| Vijayawada | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Guwahati | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Patna | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Delhi (DTC and cluster buses) | [Delhi Transport Department / DTC, Delhi bus static GTFS v1 (Open Transit Data Delhi)](https://otd.delhi.gov.in/) | OTD Delhi terms |
| Delhi Metro (DMRC, incl. Airport Express and Rapid Metro Gurugram) | [DMRC static GTFS v1 (Open Transit Data Delhi)](https://otd.delhi.gov.in/) | OTD Delhi terms |
| Delhi NCR suburban rail (Northern Railway EMU/MEMU) | [National Indian Railways GTFS (github.com/Neo2308), cut to the Delhi suburban lines by India Metro's suburban map; built by tools/suburban_gtfs.py](https://github.com/Neo2308) | none stated |
| Namo Bharat RRTS (NCRTC, Delhi-Meerut) | [NCRTC static GTFS v1 (Open Transit Data Delhi)](https://otd.delhi.gov.in/) | OTD Delhi terms |
| Goa (Kadamba Transport Corporation) | [Goa Transport Department: KTCL GTFS](https://goatransport.gov.in/GTFS) | none stated |
| Ahmedabad (AMTS, Janmarg BRTS, Gandhinagar GTSL) | [croyla/amd-gtfs](https://github.com/croyla/amd-gtfs) | MIT |
| Rajkot (RRL BRTS + city) |  | none stated |
| Vapi (VCBS) | [shubhamvelani/VapiGTFS](https://github.com/shubhamvelani/VapiGTFS) | none stated |
| Gurugram (GMCBL) | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Indian Railways (all-India trains, incl. EMU/MEMU) | [Community GTFS of Indian Railways by P. Radha Krishna (github.com/Neo2308)](https://github.com/Neo2308) | none stated |
| Jammu | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Srinagar | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Belagavi | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Bengaluru (BMTC) | [Vonter/bmtc-gtfs](https://github.com/Vonter/bmtc-gtfs) | ODbL |
| Davangere (KSRTC city) | [croyla/dvg-gtfs](https://github.com/croyla/dvg-gtfs) | MIT-0 |
| Hubballi-Dharwad (HDBRTS + city) |  | none stated |
| Mangaluru | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Udupi | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Kannur | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Kasaragod | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Kochi | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Kottayam | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Kozhikode | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Thiruvananthapuram | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Thrissur | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Wayanad | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Bhopal | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Indore | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Jabalpur | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Ujjain | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Mumbai region bus (BEST, TMT, KDMT, VVMT) | [croyla/mumbai-gtfs (BLRTransit)](https://github.com/croyla/mumbai-gtfs) | MIT-0 |
| Mumbai suburban rail (Western, Central, Harbour, Trans-Harbour, Uran) | [Rush Hour's Mumbai timetable (railway working timetables: WR Feb 2026, Harbour Oct 2024, Trans-Harbour Jan 2024, Port line Dec 2025), via India Metro's suburban map; built by tools/suburban_gtfs.py](https://git.sr.ht/~sphericalkat/rush-hour) | MIT |
| Nagpur | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Pune (PMPML) |  | none stated |
| OSRTC (Odisha, statewide) | [OSRTC Track a Bus, as seen by the reclaim.city live poller](https://osrtc.org/) | none stated |
| Rourkela | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Amritsar | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Jaipur | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Udaipur | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Chennai MTC | [reclaimchennai/ChennaiGTFS, Chennai One MTC feed](https://github.com/reclaimchennai/ChennaiGTFS/tree/chennai-one-feeds) | none stated |
| Chennai Metro (CMRL) | [reclaimchennai/ChennaiGTFS, Chennai One CMRL feed](https://github.com/reclaimchennai/ChennaiGTFS/tree/chennai-one-feeds) | ODbL |
| Chennai suburban rail and MRTS (Southern Railway) | [reclaimchennai/ChennaiGTFS, Chennai One suburban feed (stations from CUMTA, Government Open Data Licence - India)](https://github.com/reclaimchennai/ChennaiGTFS/tree/chennai-one-feeds) | ODbL |
| Hyderabad (TGSRTC city, official open data) | [TGSRTC buses GTFS, Open Data Telangana (via OpenCity)](https://data.opencity.in/dataset/hyderabad-bus-stops) | none stated |
| TGSRTC (Telangana, statewide) | [reclaimchennai/tgsrtc](https://github.com/reclaimchennai/tgsrtc) | none stated |
| Agra | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Ayodhya | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Bareilly | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Ghaziabad | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Gorakhpur | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Jhansi | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Kanpur | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Lucknow | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Mathura | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Meerut | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Noida | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Prayagraj | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Varanasi | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) | none stated |
| Kolkata (bus, metro, suburban rail, ferry) |  | none stated |
| Kolkata Hooghly ferries |  | none stated |
| Kolkata Metro |  | none stated |
| Kolkata suburban rail (Eastern and South Eastern Railway) |  | none stated |

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
