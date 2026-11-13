# Rajasthan

Feeds in this folder: 2. Back to the [repository README](../README.md).

## Jaipur

| | |
|---|---|
| Feed id | `jaipur` |
| Download | [jaipur/bus.zip](jaipur/bus.zip) (0.5 MB), mirror <https://maps.reclaim.city/gtfs/jaipur.zip> |
| Modes | bus |
| Agencies | Jctsl |
| Routes / stops / trips | 60 / 903 / 1,421 |
| Trips with a shape | 1,421 (60 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/jaipur/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `055528cd7a5162aa46441d141d3a6ab63048c272d870f5f001eafef6f7d0fb0c` |
| Routes without a timetable | [jaipur/bus.routes_without_timetable.csv](jaipur/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 97 stops served only by those routes moved with them
- 14 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes for 1307 of 1307 trips that had none: the map's road-snapped line for the route (53 shapes)
- 1 shapes no trip uses left out

## Udaipur

| | |
|---|---|
| Feed id | `udaipur` |
| Download | [udaipur/bus.zip](udaipur/bus.zip) (0.2 MB), mirror <https://maps.reclaim.city/gtfs/udaipur.zip> |
| Modes | bus |
| Agencies | UCTSL |
| Routes / stops / trips | 28 / 243 / 303 |
| Trips with a shape | 303 (28 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/udaipur/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `413d5dd90ab635c82e448c56c37249ff283227aa1fa016fe72b6ac1a3fe66803` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes.txt left out (header only, no rows)
- shapes for 303 of 303 trips that had none: the map's road-snapped line for the route (28 shapes)
