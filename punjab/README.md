# Punjab

Feeds in this folder: 1. Back to the [repository README](../README.md).

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
