# Assam

Feeds in this folder: 2. Back to the [repository README](../README.md).

## ASTC (Assam State Transport Corporation)

| | |
|---|---|
| Feed id | `astc` |
| Download | [astc/bus.zip](astc/bus.zip) (0.5 MB), mirror <https://maps.reclaim.city/gtfs/astc.zip> |
| Modes | bus |
| Agencies | Assam State Transport Corporation |
| Routes / stops / trips | 135 / 224 / 304 |
| Trips with a shape | 304 (258 shapes) |
| Service | 2026-11-20 to 2027-05-19 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/astc/> |
| Source | [ASTC division timetables (astcbus.in/schedules, one PDF per division), built into GTFS by reclaim.city (astc_bus)](https://astcbus.in/schedules) |
| Licence | none stated by the source |
| sha256 | `74da1983f0e6048fe1edaf3e82f2e0a7d5389500e3b9beb98265b8be55440b1d` |

> Unofficial: the PDFs' own times; stop positions are town or stand level (some villages approximate, on the road at their timetable km).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 77,858 -> 70,013 shape points

## Guwahati

| | |
|---|---|
| Feed id | `guwahati` |
| Download | [guwahati/bus.zip](guwahati/bus.zip) (1.3 MB), mirror <https://maps.reclaim.city/gtfs/guwahati.zip> |
| Modes | bus |
| Agencies | ASTC, GTA, POB |
| Routes / stops / trips | 522 / 2,283 / 4,272 |
| Trips with a shape | 2,628 (322 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/guwahati/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `789a16a79c52cf3eba56f10520336b62cd609cab8b4f3b7d017afe4e76e38c87` |
| Routes without a timetable | [guwahati/bus.routes_without_timetable.csv](guwahati/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 275 stops served only by those routes moved with them
- 168 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 2628 of 4272 trips that had none: the map's road-snapped line for the route (326 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 81,773 -> 70,329 shape points
