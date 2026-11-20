# Madhya Pradesh

Feeds in this folder: 4. Back to the [repository README](../README.md).

## Bhopal

| | |
|---|---|
| Feed id | `bhopal` |
| Download | [bhopal/bus.zip](bhopal/bus.zip) (0.2 MB), mirror <https://maps.reclaim.city/gtfs/bhopal.zip> |
| Modes | bus |
| Agencies | BCLL, DIGITAL BUS, INTERCITY, MAA ASSOCIATES |
| Routes / stops / trips | 32 / 492 / 598 |
| Trips with a shape | 502 (27 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/bhopal/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `aa3edfad5b2aa714a21eb210d2d98b0605d67d6b044ba6b9e17a16bd6982a96e` |
| Routes without a timetable | [bhopal/bus.routes_without_timetable.csv](bhopal/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 386 stops served only by those routes moved with them
- 37 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 502 of 598 trips that had none: the map's road-snapped line for the route (28 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 16,067 -> 13,677 shape points

## Indore

| | |
|---|---|
| Feed id | `indore` |
| Download | [indore/bus.zip](indore/bus.zip) (0.3 MB), mirror <https://maps.reclaim.city/gtfs/indore.zip> |
| Modes | bus |
| Agencies | Aictsl |
| Routes / stops / trips | 45 / 919 / 796 |
| Trips with a shape | 796 (45 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/indore/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `ea944f7d12c5bc93f6f5282b98aafef7c615909149e709c14c34afe7d6dae8ed` |
| Routes without a timetable | [indore/bus.routes_without_timetable.csv](indore/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 175 stops served only by those routes moved with them
- 18 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 796 of 796 trips that had none: the map's road-snapped line for the route (45 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 8,132 -> 7,106 shape points

## Jabalpur

| | |
|---|---|
| Feed id | `jabalpur` |
| Download | [jabalpur/bus.zip](jabalpur/bus.zip) (0.2 MB), mirror <https://maps.reclaim.city/gtfs/jabalpur.zip> |
| Modes | bus |
| Agencies | JCTSL, JCTSL INTERCITY, PVT MARKET JABALPUR |
| Routes / stops / trips | 43 / 445 / 880 |
| Trips with a shape | 850 (41 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/jabalpur/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `68a84ed122de6101e0648b7bc6c4eeac7559a7b4c83913318412e0b6cff0fa46` |
| Routes without a timetable | [jabalpur/bus.routes_without_timetable.csv](jabalpur/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 446 stops served only by those routes moved with them
- 79 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 850 of 880 trips that had none: the map's road-snapped line for the route (41 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 7,820 -> 6,705 shape points

## Ujjain

| | |
|---|---|
| Feed id | `ujjain` |
| Download | [ujjain/bus.zip](ujjain/bus.zip) (0.0 MB), mirror <https://maps.reclaim.city/gtfs/ujjain.zip> |
| Modes | bus |
| Agencies | UCTSL |
| Routes / stops / trips | 3 / 26 / 45 |
| Trips with a shape | 45 (3 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/ujjain/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `eb0c40dbc315a29b77ad58d46386a605adc3a00fb6c0c2be3f5a1f9b9c9781de` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes.txt left out (header only, no rows)
- shapes for 45 of 45 trips that had none: the map's road-snapped line for the route (3 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 2,128 -> 769 shape points
