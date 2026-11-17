# Chandigarh

Feeds in this folder: 1. Back to the [repository README](../README.md).

## Chandigarh tricity (CTU: Chandigarh, Mohali, Panchkula)

| | |
|---|---|
| Feed id | `tricity` |
| Download | [tricity/bus.zip](tricity/bus.zip) (0.8 MB), mirror <https://maps.reclaim.city/gtfs/tricity.zip> |
| Modes | bus |
| Agencies | Chandigarh Transport Undertaking |
| Routes / stops / trips | 69 / 558 / 3,938 |
| Trips with a shape | 3,938 (118 shapes) |
| Service | 2026-11-17 to 2027-11-17 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/tricity/> |
| Source | [CTU's published timetables and its trycityBUS tracker, built into GTFS by reclaim.city](https://ctucitybus.com/) |
| Licence | none stated by the source |
| sha256 | `a9c14c4d1f31463e01668d9f7658d05562f7ac80c7e0df40aed4dfb9731a4886` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/tricity/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/tricity/rt/trip_updates.pb), [status](https://maps.reclaim.city/tricity/rt/status.json) |

> Unofficial: built from CTU's timetable PDF and live tracker; times after the first stop are estimates (timepoint=0).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
