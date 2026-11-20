# Haryana

Feeds in this folder: 2. Back to the [repository README](../README.md).

## Gurugram (GMCBL)

| | |
|---|---|
| Feed id | `gurugram` |
| Download | [gurugram/bus.zip](gurugram/bus.zip) (0.7 MB), mirror <https://maps.reclaim.city/gtfs/gurugram.zip> |
| Modes | bus |
| Agencies | Gurugram Metropolitan City Bus Ltd |
| Routes / stops / trips | 148 / 1,117 / 3,124 |
| Trips with a shape | 3,124 (147 shapes) |
| Service | 2026-11-01 to 2027-11-01 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Source | [Chalo's public scheduler (production.zophop.com, the backend of GMCBL's Gurugaman app): every route's details (stops in order, its line, every trip on a Monday and a Sunday, frequency windows expanded), Nov 2026, built into GTFS by reclaim.city (ncr_bus pipeline/routedetails_gtfs.py; times between the ends spread by distance, timepoint=0)](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `beba4d26f0e73fa86421bca70295de0c5c5b11c851b919769bd604a61e68fc16` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/gurugram/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/gurugram/rt/trip_updates.pb), [status](https://maps.reclaim.city/gurugram/rt/status.json) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 29,012 -> 13,507 shape points
- feed_info.txt added (none in the source)

## Haryana Roadways (Haryana, statewide)

| | |
|---|---|
| Feed id | `hr` |
| Download | [haryana-roadways.zip](haryana-roadways.zip) (0.8 MB), mirror <https://maps.reclaim.city/gtfs/hr.zip> |
| Modes | bus |
| Agencies | Haryana Roadways |
| Routes / stops / trips | 420 / 238 / 10,447 |
| Trips with a shape | 10,447 (548 shapes) |
| Service | 2026-11-17 to 2027-11-17 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/hr/> |
| Source | [Haryana Roadways' depot timetables (hartrans.gov.in) and its live tracking, built into GTFS by reclaim.city](https://hartrans.gov.in/bus-time-table-depot-wise/) |
| Licence | none stated by the source |
| sha256 | `1a96dc3d07eb53ebd4a81861788da0dffca19e7ff91d5cd75368aae1b051edb2` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/hr/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/hr/rt/trip_updates.pb), [status](https://maps.reclaim.city/hr/rt/status.json) |

> Unofficial: built from Haryana Roadways' depot timetables and live tracking; stops are towns and bus stands, times after the first are estimates (timepoint=0).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 69,408 -> 69,402 shape points
