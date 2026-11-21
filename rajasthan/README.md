# Rajasthan

Feeds in this folder: 7. Back to the [repository README](../README.md).

## Jaipur

| | |
|---|---|
| Feed id | `jaipur` |
| Download | [jaipur/bus.zip](jaipur/bus.zip) (0.4 MB), mirror <https://maps.reclaim.city/gtfs/jaipur.zip> |
| Modes | bus |
| Agencies | Jctsl |
| Routes / stops / trips | 60 / 903 / 1,421 |
| Trips with a shape | 1,421 (59 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/jaipur/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `249c8350dc23d43fcb279d345eadb867101039f033ae6660d49d5d7f2478ea55` |
| Routes without a timetable | [jaipur/bus.routes_without_timetable.csv](jaipur/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 97 stops served only by those routes moved with them
- 14 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes for 1307 of 1307 trips that had none: the map's road-snapped line for the route (53 shapes)
- 1 shapes no trip uses left out
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 13,698 -> 8,850 shape points

## RSRTC (Rajasthan State Road Transport Corporation, intercity)

| | |
|---|---|
| Feed id | `rjrtc` |
| Download | [rsrtc/bus.zip](rsrtc/bus.zip) (0.4 MB), mirror <https://maps.reclaim.city/gtfs/rjrtc.zip> |
| Modes | bus |
| Agencies | Rajasthan State Road Transport Corporation |
| Routes / stops / trips | 1,964 / 2,000 / 96 |
| Trips with a shape | 94 (79 shapes) |
| Service | 2026-11-21 to 2027-12-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/rjrtc/> |
| Source | [RSRTC's Intalia VTS tracker (vts.intaliatech.com): its route catalogue and the schedule tuples its buses carry, built into GTFS by reclaim.city (rajasthan_bus)](https://rsrtc.rajasthan.gov.in/) |
| Licence | none stated by the source |
| sha256 | `bdfde72fdc2d050a994463feb42145d038f7da6c466f136ab8578658c16b585f` |

> Unofficial and partial: the routes are RSRTC's whole intercity catalogue, but trips are only the scheduled runs observed on the live tracker so far (origin to destination, with start and end times).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- stop times in 13 trips: 2 past-midnight times written past 24:00, 0 intermediate times that ran backwards cleared (timepoint=0), 11 departures before their own arrival set to the arrival
- 1864 shapes no trip uses left out
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 47,563 -> 39,251 shape points

## Udaipur

| | |
|---|---|
| Feed id | `udaipur` |
| Download | [udaipur/bus.zip](udaipur/bus.zip) (0.1 MB), mirror <https://maps.reclaim.city/gtfs/udaipur.zip> |
| Modes | bus |
| Agencies | UCTSL |
| Routes / stops / trips | 28 / 243 / 303 |
| Trips with a shape | 303 (28 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/udaipur/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `4bb0a13a1fd6c325185c1e0a12299750fbcb3ca926b407a19a43dabdacd5ebf7` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes.txt left out (header only, no rows)
- shapes for 303 of 303 trips that had none: the map's road-snapped line for the route (28 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 17,899 -> 6,610 shape points

## Bhilwara (city e-buses, PM e-Bus Sewa)

| | |
|---|---|
| Feed id | `bhilwara` |
| Download | no GTFS (no timetable) |
| Modes | bus |
| Map | <https://maps.reclaim.city/rjrtc/> |
| Source | [Katch city bus tracking (katchapp.in/bus_tracking): the cities' published route maps (KML) and live GPS, built into GTFS by reclaim.city](https://katchapp.in/bus_tracking) |
| Licence | none stated by the source |
| Routes without a timetable | [bhilwara/bus.routes_without_timetable.csv](bhilwara/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

> No timetable: the source holds routes and stops only, so there is no GTFS feed; the routes and their stops are in the CSV.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 145 stops served only by those routes moved with them
- 11 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- 11 shapes no trip uses left out
- feed_info.txt added (none in the source)

## Bikaner (BCTSL city e-buses, PM e-Bus Sewa)

| | |
|---|---|
| Feed id | `bikaner` |
| Download | no GTFS (no timetable) |
| Modes | bus |
| Map | <https://maps.reclaim.city/rjrtc/> |
| Source | [Katch city bus tracking (katchapp.in/bus_tracking): the cities' published route maps (KML) and live GPS, built into GTFS by reclaim.city](https://katchapp.in/bus_tracking) |
| Licence | none stated by the source |
| Routes without a timetable | [bikaner/bus.routes_without_timetable.csv](bikaner/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

> No timetable: the source holds routes and stops only, so there is no GTFS feed; the routes and their stops are in the CSV.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 70 stops served only by those routes moved with them
- 7 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- 7 shapes no trip uses left out
- feed_info.txt added (none in the source)

## Jodhpur (JBSL city e-buses, PM e-Bus Sewa)

| | |
|---|---|
| Feed id | `jodhpur` |
| Download | no GTFS (no timetable) |
| Modes | bus |
| Map | <https://maps.reclaim.city/rjrtc/> |
| Source | [Katch city bus tracking (katchapp.in/bus_tracking): the cities' published route maps (KML) and live GPS, built into GTFS by reclaim.city](https://katchapp.in/bus_tracking) |
| Licence | none stated by the source |
| Routes without a timetable | [jodhpur/bus.routes_without_timetable.csv](jodhpur/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

> No timetable: the source holds routes and stops only, so there is no GTFS feed; the routes and their stops are in the CSV.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 108 stops served only by those routes moved with them
- 5 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- 5 shapes no trip uses left out
- feed_info.txt added (none in the source)

## Kota (KBSL city e-buses, PM e-Bus Sewa)

| | |
|---|---|
| Feed id | `kota` |
| Download | no GTFS (no timetable) |
| Modes | bus |
| Map | <https://maps.reclaim.city/rjrtc/> |
| Source | [Katch city bus tracking (katchapp.in/bus_tracking): the cities' published route maps (KML) and live GPS, built into GTFS by reclaim.city](https://katchapp.in/bus_tracking) |
| Licence | none stated by the source |
| Routes without a timetable | [kota/bus.routes_without_timetable.csv](kota/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

> No timetable: the source holds routes and stops only, so there is no GTFS feed; the routes and their stops are in the CSV.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 166 stops served only by those routes moved with them
- 8 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- 8 shapes no trip uses left out
- feed_info.txt added (none in the source)
