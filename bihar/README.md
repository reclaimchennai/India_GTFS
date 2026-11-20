# Bihar

Feeds in this folder: 2. Back to the [repository README](../README.md).

## BSRTC (Bihar State Road Transport Corporation)

| | |
|---|---|
| Feed id | `bsrtc` |
| Download | [bsrtc/bus.zip](bsrtc/bus.zip) (0.2 MB), mirror <https://maps.reclaim.city/gtfs/bsrtc.zip> |
| Modes | bus |
| Agencies | Bihar State Road Transport Corporation |
| Routes / stops / trips | 48 / 40 / 323 |
| Trips with a shape | 323 (95 shapes) |
| Service | 2026-11-20 to 2027-05-19 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/bsrtc/> |
| Source | [BSRTC depot timetables (bsrtc.co.in/schedules, one PDF per depot), built into GTFS by reclaim.city (bsrtc_bus)](https://bsrtc.co.in/schedules) |
| Licence | none stated by the source |
| sha256 | `7d5312c4a63df4621c6fb2b8a0dc8f643923d30b8c276d527e1d21148d9f4b1e` |

> Unofficial: origin and destination only, as published; arrival times are estimates (timepoint=0).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 19,070 -> 19,065 shape points

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
| sha256 | `1f9a8da13072d88bbaf65f5cea57f363038a38ba6e1d9871f9cd4745d992b6c3` |
| Routes without a timetable | [patna/bus.routes_without_timetable.csv](patna/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 355 stops served only by those routes moved with them
- 92 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 500 of 577 trips that had none: the map's road-snapped line for the route (45 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 6,251 -> 5,439 shape points
