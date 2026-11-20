# Telangana

Feeds in this folder: 2. Back to the [repository README](../README.md).

## Hyderabad (TGSRTC city, official open data)

| | |
|---|---|
| Feed id | `hyderabad` |
| Download | [hyderabad/bus.zip](hyderabad/bus.zip) (11.5 MB), mirror <https://maps.reclaim.city/gtfs/hyderabad.zip> |
| Modes | bus |
| Agencies | Telangana State Road Transport Corporation |
| Routes / stops / trips | 1,031 / 5,028 / 44,892 |
| Trips with a shape | 16,691 (981 shapes) |
| Service | 2026-02-01 to 2031-02-01 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/hyderabad/> |
| Source | [TGSRTC buses GTFS, Open Data Telangana (via OpenCity)](https://data.opencity.in/dataset/hyderabad-bus-stops) |
| Licence | none stated by the source |
| sha256 | `136ce91d0e114f60c2b39d36f6c77d80a37c15f1a85a65eb7d788db0b112e914` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes for 16691 of 44892 trips that had none: the map's road-snapped line for the route (1008 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 222,016 -> 188,338 shape points

## TGSRTC (Telangana, statewide)

| | |
|---|---|
| Feed id | `tgsrtc` |
| Download | [tgsrtc.zip](tgsrtc.zip) (24.6 MB), mirror <https://maps.reclaim.city/gtfs/tgsrtc.zip> |
| Modes | bus |
| Agencies | Telangana State Road Transport Corporation |
| Routes / stops / trips | 7,881 / 14,811 / 56,977 |
| Trips with a shape | 56,975 (6,589 shapes) |
| Service | 2026-09-01 to 2031-09-01 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/tgsrtc/> |
| Source | [reclaimchennai/tgsrtc](https://github.com/reclaimchennai/tgsrtc) |
| Licence | none stated by the source |
| sha256 | `11b1164914ad1d6480df7911d68a04f05e9e16788ab048547feb38343edc0c9c` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/tgsrtc/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/tgsrtc/rt/trip_updates.pb), [status](https://maps.reclaim.city/tgsrtc/rt/status.json) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- stop times in 20 trips: 0 past-midnight times written past 24:00, 12 intermediate times that ran backwards cleared (timepoint=0), 13 departures before their own arrival set to the arrival
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 5,568,409 -> 1,534,112 shape points
