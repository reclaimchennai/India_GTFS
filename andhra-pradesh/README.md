# Andhra Pradesh

Feeds in this folder: 2. Back to the [repository README](../README.md).

## APSRTC (Andhra Pradesh, statewide)

| | |
|---|---|
| Feed id | `apsrtc` |
| Download | [apsrtc.zip](apsrtc.zip) (21.4 MB), mirror <https://maps.reclaim.city/gtfs/apsrtc.zip> |
| Modes | bus |
| Agencies | Andhra Pradesh State Road Transport Corporation |
| Routes / stops / trips | 5,095 / 11,156 / 54,812 |
| Trips with a shape | 54,350 (11,609 shapes) |
| Service | 2026-11-01 to 2027-10-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/apsrtc/> |
| Source | [reclaimchennai/apsrtc](https://github.com/reclaimchennai/apsrtc) |
| Licence | none stated by the source |
| sha256 | `be2e1a3286de819ef9229a1615543d4c431556122b80bbe69497e054a1ed87c2` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/apsrtc/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/apsrtc/rt/trip_updates.pb), [status](https://maps.reclaim.city/apsrtc/rt/status.json) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- stop times in 806 trips: 91 past-midnight times written past 24:00, 1728 intermediate times that ran backwards cleared (timepoint=0), 201 departures before their own arrival set to the arrival
- 22 shapes no trip uses left out

## Vijayawada

| | |
|---|---|
| Feed id | `vijayawada` |
| Download | [vijayawada/bus.zip](vijayawada/bus.zip) (1.3 MB), mirror <https://maps.reclaim.city/gtfs/vijayawada.zip> |
| Modes | bus |
| Agencies | APSRTC |
| Routes / stops / trips | 331 / 1,525 / 3,171 |
| Trips with a shape | 3,171 (331 shapes) |
| Service | 2026-11-03 to 2027-11-03 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/vijayawada/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `3e88994861f8e7cf5ac486a9d36cd0351f146a3352d83cd4b42adaec021983ce` |
| Routes without a timetable | [vijayawada/bus.routes_without_timetable.csv](vijayawada/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 223 stops served only by those routes moved with them
- 299 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes for 3061 of 3061 trips that had none: the map's road-snapped line for the route (329 shapes)
