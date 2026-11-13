# Haryana

Feeds in this folder: 1. Back to the [repository README](../README.md).

## Gurugram (GMCBL)

| | |
|---|---|
| Feed id | `gurugram` |
| Download | [gurugram/bus.zip](gurugram/bus.zip) (0.4 MB), mirror <https://maps.reclaim.city/gtfs/gurugram.zip> |
| Modes | bus |
| Agencies | Gurugram Metropolitan City Bus Ltd |
| Routes / stops / trips | 137 / 1,086 / 1,807 |
| Trips with a shape | 0 (0 shapes) |
| Service | 2026-10-01 to 2027-10-01 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `056ca67434a8cbf8a4f8a2e90c5cb2a8924ea62e54ccf15a69a01d84f49fbad2` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/gurugram/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/gurugram/rt/trip_updates.pb), [status](https://maps.reclaim.city/gurugram/rt/status.json) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- feed_info.txt added (none in the source)
