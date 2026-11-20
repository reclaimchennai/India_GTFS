# Punjab

Feeds in this folder: 3. Back to the [repository README](../README.md).

## PRTC (PEPSU Road Transport Corporation)

| | |
|---|---|
| Feed id | `pepsu` |
| Download | [pepsu/bus.zip](pepsu/bus.zip) (0.0 MB), mirror <https://maps.reclaim.city/gtfs/pepsu.zip> |
| Modes | bus |
| Agencies | PEPSU Road Transport Corporation |
| Routes / stops / trips | 8 / 12 / 26 |
| Trips with a shape | 26 (15 shapes) |
| Service | 2026-11-21 to 2027-05-20 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/pepsu/> |
| Source | [PRTC online booking timetable (pepsuonline.com), built into GTFS by reclaim.city (pepsu_bus)](https://www.pepsuonline.com/) |
| Licence | none stated by the source |
| sha256 | `a668b175d72e2a05cf884d8ae115b6bde633ca3137ab84634b4bab1873651f2b` |

> Unofficial: online-sold trips only (mostly AC / Volvo), times as published at each town; ordinary buses absent.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only

## PUNBUS / Punjab Roadways

| | |
|---|---|
| Feed id | `punbus` |
| Download | [punbus/bus.zip](punbus/bus.zip) (0.1 MB), mirror <https://maps.reclaim.city/gtfs/punbus.zip> |
| Modes | bus |
| Agencies | PUNBUS / Punjab Roadways |
| Routes / stops / trips | 19 / 32 / 63 |
| Trips with a shape | 63 (36 shapes) |
| Service | 2026-11-21 to 2027-05-20 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/pepsu/> |
| Source | [PUNBUS online booking timetable (punbusonline.com), built into GTFS by reclaim.city (pepsu_bus)](https://www.punbusonline.com/) |
| Licence | none stated by the source |
| sha256 | `28e8edb0050548f97420521c891170bb4a4a07d8b87ed0cadef4c85f046012a6` |

> Unofficial: online-sold trips only (mostly AC / Volvo), times as published at each town; ordinary buses absent.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 6,617 -> 6,615 shape points

## Amritsar

| | |
|---|---|
| Feed id | `amritsar` |
| Download | no GTFS (no timetable) |
| Modes | bus |
| Map | <https://maps.reclaim.city/amritsar/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| Routes without a timetable | [amritsar/bus.routes_without_timetable.csv](amritsar/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

> No timetable: the source holds routes and stops only, so there is no GTFS feed; the routes and their stops are in the CSV.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 75 stops served only by those routes moved with them
- 6 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
