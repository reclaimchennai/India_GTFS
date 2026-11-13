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
| sha256 | `1a02aee7997626c8992b993d03108964f08a0ca64eee18583b8f7e993633248c` |
| Routes without a timetable | [belagavi/bus.routes_without_timetable.csv](belagavi/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 121 stops served only by those routes moved with them
- 30 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 331 of 331 trips that had none: the map's road-snapped line for the route (33 shapes)

## Bengaluru (BMTC)

| | |
|---|---|
| Feed id | `bengaluru` |
| Download | [bengaluru/bus.zip](bengaluru/bus.zip) (88.7 MB), mirror <https://maps.reclaim.city/gtfs/bengaluru.zip> |
| Modes | bus |
| Agencies | BMTC |
| Routes / stops / trips | 5,063 / 10,128 / 69,642 |
| Trips with a shape | 69,642 (8,983 shapes) |
| Service | 2026-11-09 to 2027-11-09 |
| Files | `agency.txt`, `attributions.txt`, `calendar.txt`, `fare_attributes.txt`, `fare_rules.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `translations.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/bengaluru/> |
| Source | [Vonter/bmtc-gtfs](https://github.com/Vonter/bmtc-gtfs) |
| Licence | ODbL |
| sha256 | `2eba4a144e08a59106dcc3ffd6633ab8174fbed8ba2e359e5a60b69c29658c5f` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only

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
| sha256 | `ef0bdc2a397d0c252c59cde44b704fca7fddd88c705791a8733c543e984e9800` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- stop times in 120 trips: 0 past-midnight times written past 24:00, 417 intermediate times that ran backwards cleared (timepoint=0), 0 departures before their own arrival set to the arrival
- shapes for 586 of 586 trips that had none: the map's road-snapped line for the route (14 shapes)

## Hubballi-Dharwad (HDBRTS + city)

| | |
|---|---|
| Feed id | `hubballi` |
| Download | [hubballi-dharwad/bus.zip](hubballi-dharwad/bus.zip) (2.5 MB), mirror <https://maps.reclaim.city/gtfs/hubballi.zip> |
| Modes | bus |
| Agencies | Hubli-Dharwad Bus Rapid Transit System Company Limited |
| Routes / stops / trips | 632 / 2,332 / 8,669 |
| Trips with a shape | 8,669 (630 shapes) |
| Service | 2026-08-24 to 2027-02-20 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/hubballi/> |
| Licence | none stated by the source |
| sha256 | `fb0ff87a4805d348bc3221cd7ccaf09055791c4e41df2f031248ecb92bb5642f` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes for 8669 of 8669 trips that had none: the map's road-snapped line for the route (630 shapes)

## Mangaluru

| | |
|---|---|
| Feed id | `mangaluru` |
| Download | [mangaluru/bus.zip](mangaluru/bus.zip) (1.0 MB), mirror <https://maps.reclaim.city/gtfs/mangaluru.zip> |
| Modes | bus |
| Agencies | CCM, COASTAL ZONE, DKBOA, KCT, KSRTC, MLORE SERVICE BUSES, ROUTE 42-44, SBCR, SERVICE POLALI |
| Routes / stops / trips | 208 / 1,394 / 2,079 |
| Trips with a shape | 2,026 (198 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/mangaluru/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `5c9bae2a15fd62a06ef6e601f85eb13bcdbf3d69f0cd6d470b81f1c0ad0e925e` |
| Routes without a timetable | [mangaluru/bus.routes_without_timetable.csv](mangaluru/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 1355 stops served only by those routes moved with them
- 514 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 2026 of 2079 trips that had none: the map's road-snapped line for the route (198 shapes)

## Udupi

| | |
|---|---|
| Feed id | `udupi` |
| Download | [udupi/bus.zip](udupi/bus.zip) (1.1 MB), mirror <https://maps.reclaim.city/gtfs/udupi.zip> |
| Modes | bus |
| Agencies | CITYBUS, DIGITAL BUS, SAACHI TRAVELS, SRI LAKSHMI EXPRESS, USB |
| Routes / stops / trips | 191 / 1,392 / 2,561 |
| Trips with a shape | 2,318 (174 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/udupi/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `e2bcbfa7638525050343f38a68200c9d273e7c3fce3eb629ae82cec06860c1f1` |
| Routes without a timetable | [udupi/bus.routes_without_timetable.csv](udupi/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 459 stops served only by those routes moved with them
- 114 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 2318 of 2561 trips that had none: the map's road-snapped line for the route (174 shapes)
