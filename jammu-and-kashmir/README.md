# Jammu and Kashmir

Feeds in this folder: 2. Back to the [repository README](../README.md).

## Jammu

| | |
|---|---|
| Feed id | `jammu` |
| Download | [jammu/bus.zip](jammu/bus.zip) (0.7 MB), mirror <https://maps.reclaim.city/gtfs/jammu.zip> |
| Modes | bus |
| Agencies | CITY BUS JAMMU |
| Routes / stops / trips | 248 / 850 / 1,880 |
| Trips with a shape | 1,804 (240 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/jammu/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `e358ec63c57dafc7fd4f6e610199567e56d8eb7f3872d0885632088b90b49f11` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes.txt left out (header only, no rows)
- shapes for 1804 of 1880 trips that had none: the map's road-snapped line for the route (240 shapes)

## Srinagar

| | |
|---|---|
| Feed id | `srinagar` |
| Download | [srinagar/bus.zip](srinagar/bus.zip) (0.8 MB), mirror <https://maps.reclaim.city/gtfs/srinagar.zip> |
| Modes | bus |
| Agencies | CITY BUS SRINAGAR |
| Routes / stops / trips | 168 / 1,065 / 2,404 |
| Trips with a shape | 2,404 (168 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/srinagar/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `a49d4d51a4d9c96fcd636142eb74b273c9c6ef71da19d0e8cbcc286d5a68df7d` |
| Routes without a timetable | [srinagar/bus.routes_without_timetable.csv](srinagar/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 1 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 2404 of 2404 trips that had none: the map's road-snapped line for the route (168 shapes)
