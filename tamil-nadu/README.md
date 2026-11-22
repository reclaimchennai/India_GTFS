# Tamil Nadu

Feeds in this folder: 4. Back to the [repository README](../README.md).

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
| Download | [chennai/mtc-bus.zip](chennai/mtc-bus.zip) (13.7 MB), mirror <https://maps.reclaim.city/gtfs/mtc.zip> |
| Modes | bus |
| Agencies | Metropolitan Transport Corporation (Chennai) |
| Routes / stops / trips | 1,103 / 3,829 / 52,148 |
| Trips with a shape | 52,148 (4,311 shapes) |
| Service | 2026-01-01 to 2027-12-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/mapsv2/> |
| Source | [reclaimchennai/ChennaiGTFS, Chennai One MTC feed](https://github.com/reclaimchennai/ChennaiGTFS/tree/chennai-one-feeds) |
| Licence | none stated by the source |
| sha256 | `e9b390fa9fdb9d568d83659cb0a9de7801da61c851be393a0ee082bca2035bfa` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/mapsv2/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/mapsv2/rt/trip_updates.pb), [status](https://maps.reclaim.city/mapsv2/rt/status.json) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 1,004,270 -> 552,489 shape points

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

## TNSTC + SETC intercity (Tamil Nadu state transport)

| | |
|---|---|
| Feed id | `tnstc` |
| Download | [tnstc/bus.zip](tnstc/bus.zip) (4.1 MB), mirror <https://maps.reclaim.city/gtfs/tnstc.zip> |
| Modes | bus |
| Agencies | State Express Transport Corporation Tamil Nadu Ltd, Tamil Nadu State Transport Corporation (Coimbatore) Ltd, Tamil Nadu State Transport Corporation (Kumbakonam) Ltd, Tamil Nadu State Transport Corporation (Madurai) Ltd, Tamil Nadu State Transport Corporation (Salem) Ltd, Tamil Nadu State Transport Corporation (Tirunelveli) Ltd, Tamil Nadu State Transport Corporation (Villupuram) Ltd |
| Routes / stops / trips | 940 / 171 / 3,424 |
| Trips with a shape | 3,424 (1,095 shapes) |
| Service | 2026-11-21 to 2027-05-20 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/tnstc/> |
| Source | [TNSTC / SETC public booking timetables (tnstc.in OTRSOnline), built into GTFS by reclaim.city (tnstc_bus)](https://www.tnstc.in/) |
| Licence | none stated by the source |
| sha256 | `7365f06a469ae813b43563eff2aec6ad1aeaa475e67a3f555f7981707511885b` |

> Unofficial: built from the TNSTC/SETC public booking timetables; stops are towns and bus stands, times between the searched hub towns are estimates (timepoint=0).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 472,333 -> 453,666 shape points
