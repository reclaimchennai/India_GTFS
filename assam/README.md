# Assam

Feeds in this folder: 1. Back to the [repository README](../README.md).

## Guwahati

| | |
|---|---|
| Feed id | `guwahati` |
| Download | [guwahati/bus.zip](guwahati/bus.zip) (1.4 MB), mirror <https://maps.reclaim.city/gtfs/guwahati.zip> |
| Modes | bus |
| Agencies | ASTC, GTA, POB |
| Routes / stops / trips | 522 / 2,283 / 4,272 |
| Trips with a shape | 2,628 (326 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/guwahati/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `dc35ae786efc043f6686ccaae739053c913728d8c97ef96d82930541ba827a36` |
| Routes without a timetable | [guwahati/bus.routes_without_timetable.csv](guwahati/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 275 stops served only by those routes moved with them
- 168 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 2628 of 4272 trips that had none: the map's road-snapped line for the route (326 shapes)
