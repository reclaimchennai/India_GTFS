# Karnataka

Feeds in this folder: 6. Back to the [repository README](../README.md).

## Belagavi

| | |
|---|---|
| Feed id | `belgaum` |
| Download | [belagavi/bus.zip](belagavi/bus.zip) (0.1 MB), mirror <https://maps.reclaim.city/gtfs/belgaum.zip> |
| Modes | bus |
| Agencies | NWKRTC |
| Routes / stops / trips | 33 / 242 / 331 |
| Trips with a shape | 331 (33 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/belgaum/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `9c8eb921939209e3f30d4428b67ac32dd508f19a7625043cde7074ddf9d97864` |
| Routes without a timetable | [belagavi/bus.routes_without_timetable.csv](belagavi/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 121 stops served only by those routes moved with them
- 30 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 331 of 331 trips that had none: the map's road-snapped line for the route (33 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 6,832 -> 2,613 shape points

## Bengaluru (BMTC)

| | |
|---|---|
| Feed id | `bengaluru` |
| Download | [bengaluru/bus.zip](bengaluru/bus.zip) (57.1 MB), mirror <https://maps.reclaim.city/gtfs/bengaluru.zip> |
| Modes | bus |
| Agencies | BMTC |
| Routes / stops / trips | 5,359 / 10,165 / 76,675 |
| Trips with a shape | 76,675 (9,242 shapes) |
| Service | 2026-11-09 to 2027-11-09 |
| Files | `agency.txt`, `attributions.txt`, `calendar.txt`, `fare_attributes.txt`, `fare_rules.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `translations.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/bengaluru/> |
| Source | [Vonter/bmtc-gtfs, plus the routes only BMTC's own app has (reclaim.city)](https://github.com/Vonter/bmtc-gtfs) |
| Licence | ODbL |
| sha256 | `dbd654f2307d3cb3c246a6115a936bae11086fb6466b0f280051e170027f279c` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/bengaluru/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/bengaluru/rt/trip_updates.pb), [status](https://maps.reclaim.city/bengaluru/rt/status.json) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 4,270,317 -> 1,626,526 shape points

## Davangere (KSRTC city)

| | |
|---|---|
| Feed id | `davangere` |
| Download | [davangere/bus.zip](davangere/bus.zip) (0.1 MB), mirror <https://maps.reclaim.city/gtfs/davangere.zip> |
| Modes | bus |
| Agencies | Karnataka State Road Transport Corporation |
| Routes / stops / trips | 93 / 146 / 586 |
| Trips with a shape | 586 (14 shapes) |
| Service | 2026-06-02 to 2026-11-29 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/davangere/> |
| Source | [croyla/dvg-gtfs](https://github.com/croyla/dvg-gtfs) |
| Licence | MIT-0 |
| sha256 | `8d11df1cbedcfdb16914aebb43612acf7d8e4c3d4066454820684fd0d4739c14` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- stop times in 120 trips: 0 past-midnight times written past 24:00, 417 intermediate times that ran backwards cleared (timepoint=0), 0 departures before their own arrival set to the arrival
- shapes for 586 of 586 trips that had none: the map's road-snapped line for the route (14 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 1,315 -> 1,203 shape points

## Hubballi-Dharwad (HDBRTS + city)

| | |
|---|---|
| Feed id | `hubballi` |
| Download | [hubballi-dharwad/bus.zip](hubballi-dharwad/bus.zip) (1.7 MB), mirror <https://maps.reclaim.city/gtfs/hubballi.zip> |
| Modes | bus |
| Agencies | Hubli-Dharwad Bus Rapid Transit System Company Limited |
| Routes / stops / trips | 632 / 2,332 / 8,669 |
| Trips with a shape | 8,669 (626 shapes) |
| Service | 2026-08-24 to 2027-02-20 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/hubballi/> |
| Source | [croyla/hdbrts-gtfs](https://github.com/croyla/hdbrts-gtfs) |
| Licence | MIT-0 |
| sha256 | `f8727682894c454845dce9eefa92e08933b85df4e82470f4b78c61e0fa653790` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes for 8669 of 8669 trips that had none: the map's road-snapped line for the route (630 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 171,203 -> 63,584 shape points

## Mangaluru

| | |
|---|---|
| Feed id | `mangaluru` |
| Download | [mangaluru/bus.zip](mangaluru/bus.zip) (0.9 MB), mirror <https://maps.reclaim.city/gtfs/mangaluru.zip> |
| Modes | bus |
| Agencies | CCM, COASTAL ZONE, DKBOA, KCT, KSRTC, MLORE SERVICE BUSES, ROUTE 42-44, SBCR, SERVICE POLALI |
| Routes / stops / trips | 208 / 1,394 / 2,079 |
| Trips with a shape | 2,026 (198 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/mangaluru/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `1c04e32e3600c8df92af771bfb72b23456af67b77902c08c124e5fe878619f41` |
| Routes without a timetable | [mangaluru/bus.routes_without_timetable.csv](mangaluru/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 1355 stops served only by those routes moved with them
- 514 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 2026 of 2079 trips that had none: the map's road-snapped line for the route (198 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 88,770 -> 76,633 shape points

## Udupi

| | |
|---|---|
| Feed id | `udupi` |
| Download | [udupi/bus.zip](udupi/bus.zip) (0.9 MB), mirror <https://maps.reclaim.city/gtfs/udupi.zip> |
| Modes | bus |
| Agencies | CITYBUS, DIGITAL BUS, SAACHI TRAVELS, SRI LAKSHMI EXPRESS, USB |
| Routes / stops / trips | 191 / 1,392 / 2,561 |
| Trips with a shape | 2,318 (172 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/udupi/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `d43093bff5182178e89ef40538e864641060af82a9e905e41cde5544df37389c` |
| Routes without a timetable | [udupi/bus.routes_without_timetable.csv](udupi/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 459 stops served only by those routes moved with them
- 114 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 2318 of 2561 trips that had none: the map's road-snapped line for the route (174 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 84,291 -> 69,870 shape points
