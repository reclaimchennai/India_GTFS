# Tamil Nadu

Feeds in this folder: 3. Back to the [repository README](../README.md).

## Chennai Metro (CMRL)

| | |
|---|---|
| Feed id | `chennai-metro` |
| Download | [chennai/metro-cmrl.zip](chennai/metro-cmrl.zip) (0.1 MB), mirror <https://maps.reclaim.city/gtfs/chennai-metro.zip> |
| Modes | metro |
| Agencies | Chennai Metro Rail Limited |
| Routes / stops / trips | 3 / 294 / 749 |
| Trips with a shape | 749 (34 shapes) |
| Service | 2026-01-01 to 2027-12-31 |
| Files | `agency.txt`, `calendar.txt`, `fare_attributes.txt`, `fare_rules.txt`, `feed_info.txt`, `pathways.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Source | [reclaimchennai/ChennaiGTFS, Chennai One CMRL feed](https://github.com/reclaimchennai/ChennaiGTFS/tree/chennai-one-feeds) |
| Licence | ODbL |
| sha256 | `66670912e1e42533485993795e6504bd849618e60ec05132e5ee4cb6bcd97805` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 4,787 -> 2,621 shape points

## Chennai MTC

| | |
|---|---|
| Feed id | `mtc` |
| Download | [chennai/mtc-bus.zip](chennai/mtc-bus.zip) (13.8 MB), mirror <https://maps.reclaim.city/gtfs/mtc.zip> |
| Modes | bus |
| Agencies | Metropolitan Transport Corporation (Chennai) |
| Routes / stops / trips | 1,092 / 3,768 / 51,763 |
| Trips with a shape | 51,763 (4,287 shapes) |
| Service | 2026-01-01 to 2027-12-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/mapsv2/> |
| Source | [reclaimchennai/ChennaiGTFS, Chennai One MTC feed](https://github.com/reclaimchennai/ChennaiGTFS/tree/chennai-one-feeds) |
| Licence | none stated by the source |
| sha256 | `a51070f41a46ef34600bb2cc7f6a8afc6c5828e04b6b12dbc2c71c1fe16d95a9` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/mapsv2/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/mapsv2/rt/trip_updates.pb), [status](https://maps.reclaim.city/mapsv2/rt/status.json) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 1,005,155 -> 554,923 shape points

## Chennai suburban rail and MRTS (Southern Railway)

| | |
|---|---|
| Feed id | `chennai-suburban` |
| Download | [chennai/suburban-rail-mrts.zip](chennai/suburban-rail-mrts.zip) (0.2 MB), mirror <https://maps.reclaim.city/gtfs/chennai-suburban.zip> |
| Modes | rail |
| Agencies | Southern Railway (Chennai Suburban) |
| Routes / stops / trips | 753 / 388 / 756 |
| Trips with a shape | 756 (107 shapes) |
| Service | 2026-01-01 to 2027-12-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `pathways.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Source | [reclaimchennai/ChennaiGTFS, Chennai One suburban feed (stations from CUMTA, Government Open Data Licence - India)](https://github.com/reclaimchennai/ChennaiGTFS/tree/chennai-one-feeds) |
| Licence | ODbL |
| sha256 | `9cbc5e6687a4c6f183631ea582df425c957b1432f06227cdeb59a56edbdd6e47` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 160,847 -> 13,748 shape points
