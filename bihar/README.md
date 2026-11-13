# Bihar

Feeds in this folder: 1. Back to the [repository README](../README.md).

## Patna

| | |
|---|---|
| Feed id | `patna` |
| Download | [patna/bus.zip](patna/bus.zip) (0.1 MB), mirror <https://maps.reclaim.city/gtfs/patna.zip> |
| Modes | bus |
| Agencies | BSRTC, KMRL, PVT BUS PATNA |
| Routes / stops / trips | 54 / 356 / 577 |
| Trips with a shape | 500 (45 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/patna/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `ff2ec09816611681d15d3788b736e0a4898f5e7d32974de79f930303deb0f058` |
| Routes without a timetable | [patna/bus.routes_without_timetable.csv](patna/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 355 stops served only by those routes moved with them
- 92 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 500 of 577 trips that had none: the map's road-snapped line for the route (45 shapes)
