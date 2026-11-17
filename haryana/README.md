# Haryana

Feeds in this folder: 2. Back to the [repository README](../README.md).

## Gurugram (GMCBL)

| | |
|---|---|
| Feed id | `gurugram` |
| Download | [gurugram/bus.zip](gurugram/bus.zip) (0.8 MB), mirror <https://maps.reclaim.city/gtfs/gurugram.zip> |
| Modes | bus |
| Agencies | Gurugram Metropolitan City Bus Ltd |
| Routes / stops / trips | 148 / 1,117 / 3,124 |
| Trips with a shape | 3,124 (148 shapes) |
| Service | 2026-11-01 to 2027-11-01 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Source | [Chalo's public scheduler (production.zophop.com, the backend of GMCBL's Gurugaman app): every route's details (stops in order, its line, every trip on a Monday and a Sunday, frequency windows expanded), Nov 2026, built into GTFS by reclaim.city (ncr_bus pipeline/routedetails_gtfs.py; times between the ends spread by distance, timepoint=0)](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `9b7309ccee40e1d0d6182d0a6218335094ba75225ede84d0269ff1d9ab8830ac` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/gurugram/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/gurugram/rt/trip_updates.pb), [status](https://maps.reclaim.city/gurugram/rt/status.json) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
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
| sha256 | `2d07b233b75e27ab45eca98490b8752082c97eeb034e86a1c33cbd39dd7261ee` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/hr/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/hr/rt/trip_updates.pb), [status](https://maps.reclaim.city/hr/rt/status.json) |

> Unofficial: built from Haryana Roadways' depot timetables and live tracking; stops are towns and bus stands, times after the first are estimates (timepoint=0).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
