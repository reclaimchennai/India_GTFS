# Jammu and Kashmir

Feeds in this folder: 3. Back to the [repository README](../README.md).

## Jammu

| | |
|---|---|
| Feed id | `jammu` |
| Download | [jammu/bus.zip](jammu/bus.zip) (0.6 MB), mirror <https://maps.reclaim.city/gtfs/jammu.zip> |
| Modes | bus |
| Agencies | CITY BUS JAMMU |
| Routes / stops / trips | 248 / 850 / 1,880 |
| Trips with a shape | 1,804 (221 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/jammu/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `b0bd401f5e3da26d3d01fdd192b26759373f4b2536c7f9ca784235a37df8c9ff` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes.txt left out (header only, no rows)
- shapes for 1804 of 1880 trips that had none: the map's road-snapped line for the route (240 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 43,442 -> 37,214 shape points

## Srinagar

| | |
|---|---|
| Feed id | `srinagar` |
| Download | [srinagar/bus.zip](srinagar/bus.zip) (0.7 MB), mirror <https://maps.reclaim.city/gtfs/srinagar.zip> |
| Modes | bus |
| Agencies | CITY BUS SRINAGAR |
| Routes / stops / trips | 168 / 1,065 / 2,404 |
| Trips with a shape | 2,404 (165 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/srinagar/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `a1d54a66f548b3a755a1902fe7e38c4eb74420b7b617602ff736124169b8f4c6` |
| Routes without a timetable | [srinagar/bus.routes_without_timetable.csv](srinagar/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 1 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 2404 of 2404 trips that had none: the map's road-snapped line for the route (168 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 27,538 -> 23,459 shape points

## JKRTC (Jammu & Kashmir Road Transport Corporation)

| | |
|---|---|
| Feed id | `jksrtc` |
| Download | [jksrtc/bus.zip](jksrtc/bus.zip) (0.7 MB), mirror <https://maps.reclaim.city/gtfs/jksrtc.zip> |
| Modes | bus |
| Agencies | Jammu & Kashmir Road Transport Corporation |
| Routes / stops / trips | 112 / 111 / 442 |
| Trips with a shape | 442 (210 shapes) |
| Service | 2026-11-21 to 2027-05-20 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/jkrtc/> |
| Source | [JKRTC division timetables (jksrtc.co.in, the Jammu and Kashmir division PDFs, Dec 2021), built into GTFS by reclaim.city (ne_states_bus)](https://jksrtc.co.in/timetable.php) |
| Licence | none stated by the source |
| sha256 | `e8ee8ee867d7264113ed6ea13aa6a5f3b135f6897bef04c2e70ae5a190794bf9` |

> Unofficial: JKRTC's Dec 2021 timetables (times may have changed); stops are bus stands and town or locality points.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 59,026 -> 59,017 shape points
