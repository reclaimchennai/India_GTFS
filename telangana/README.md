# Telangana

Feeds in this folder: 2. Back to the [repository README](../README.md).

## Hyderabad (TGSRTC city, official open data)

| | |
|---|---|
| Feed id | `hyderabad` |
| Download | [hyderabad/bus.zip](hyderabad/bus.zip) (11.7 MB), mirror <https://maps.reclaim.city/gtfs/hyderabad.zip> |
| Modes | bus |
| Agencies | Telangana State Road Transport Corporation |
| Routes / stops / trips | 1,031 / 5,028 / 44,892 |
| Trips with a shape | 16,691 (1,008 shapes) |
| Service | 2026-02-01 to 2031-02-01 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/hyderabad/> |
| Source | [TGSRTC buses GTFS, Open Data Telangana (via OpenCity)](https://data.opencity.in/dataset/hyderabad-bus-stops) |
| Licence | none stated by the source |
| sha256 | `ca38b2b684435556601766cefb6dbedcece85da87eb05262d43cd8bdd4309d33` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes for 16691 of 44892 trips that had none: the map's road-snapped line for the route (1008 shapes)

## TGSRTC (Telangana, statewide)

| | |
|---|---|
| Feed id | `tgsrtc` |
| Download | [tgsrtc.zip](tgsrtc.zip) (57.2 MB), mirror <https://maps.reclaim.city/gtfs/tgsrtc.zip> |
| Modes | bus |
| Agencies | Telangana State Road Transport Corporation |
| Routes / stops / trips | 7,881 / 14,811 / 56,977 |
| Trips with a shape | 56,975 (9,122 shapes) |
| Service | 2026-09-01 to 2031-09-01 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/tgsrtc/> |
| Source | [reclaimchennai/tgsrtc](https://github.com/reclaimchennai/tgsrtc) |
| Licence | none stated by the source |
| sha256 | `57697086976177a02ab494d3ab8526a28d44e437f8e4744b7715c6995ddae5c4` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/tgsrtc/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/tgsrtc/rt/trip_updates.pb), [status](https://maps.reclaim.city/tgsrtc/rt/status.json) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- stop times in 20 trips: 0 past-midnight times written past 24:00, 12 intermediate times that ran backwards cleared (timepoint=0), 13 departures before their own arrival set to the arrival
