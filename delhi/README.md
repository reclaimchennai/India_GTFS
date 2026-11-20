# Delhi

Feeds in this folder: 4. Back to the [repository README](../README.md).

## Delhi (DTC and cluster buses)

| | |
|---|---|
| Feed id | `delhi` |
| Download | [bus.zip](bus.zip) (19.8 MB), mirror <https://maps.reclaim.city/gtfs/delhi.zip> |
| Modes | bus |
| Agencies | Delhi Transport Corporation, Department of Transport |
| Routes / stops / trips | 2,554 / 6,812 / 65,322 |
| Trips with a shape | 65,322 (2,525 shapes) |
| Service | 2025-01-01 to 2040-01-01 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/delhi/> |
| Source | [Delhi Transport Department / DTC, Delhi bus static GTFS v1 (Open Transit Data Delhi)](https://otd.delhi.gov.in/) |
| Licence | OTD Delhi terms |
| sha256 | `32ce0d8465b479e8454ed2060ca3289519fdf39365b660eaf5baeca425ace988` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/delhi/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/delhi/rt/trip_updates.pb), [status](https://maps.reclaim.city/delhi/rt/status.json) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 765,633 -> 319,888 shape points

## Delhi Metro (DMRC, incl. Airport Express and Rapid Metro Gurugram)

| | |
|---|---|
| Feed id | `delhi-metro` |
| Download | [metro-dmrc.zip](metro-dmrc.zip) (1.0 MB), mirror <https://maps.reclaim.city/gtfs/delhi-metro.zip> |
| Modes | metro |
| Agencies | Delhi Metro Rail Corporation |
| Routes / stops / trips | 36 / 262 / 5,438 |
| Trips with a shape | 5,438 (36 shapes) |
| Service | 2019-01-01 to 2025-12-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Source | [DMRC static GTFS v1 (Open Transit Data Delhi)](https://otd.delhi.gov.in/) |
| Licence | OTD Delhi terms |
| sha256 | `e39010572ee86ace785d43cb4fd1b74b7115101c63a9e36f124139af73b7e544` |

> The official feed's calendar ended on 31 Dec 2025; republished as it is (the times are the current timetable pattern).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 6,643 -> 3,493 shape points
- feed_info.txt added (none in the source)

## Namo Bharat RRTS (NCRTC, Delhi-Meerut)

| | |
|---|---|
| Feed id | `delhi-rrts` |
| Download | [rrts-namo-bharat.zip](rrts-namo-bharat.zip) (0.0 MB), mirror <https://maps.reclaim.city/gtfs/delhi-rrts.zip> |
| Modes | rail |
| Agencies | National Capital Region Transport Corporation (NCRTC) |
| Routes / stops / trips | 2 / 16 / 130 |
| Trips with a shape | 130 (2 shapes) |
| Service | 2024-01-01 to 2029-01-01 |
| Files | `agency.txt`, `attributions.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Source | [NCRTC static GTFS v1 (Open Transit Data Delhi)](https://otd.delhi.gov.in/) |
| Licence | OTD Delhi terms |
| sha256 | `3ebe3435a7fb1a52e0c2d8c109226de7e4e237acd0509cb0d7339726e0f22e61` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route_type corrected on 2 routes (rail)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 419 -> 160 shape points
- feed_info.txt added (none in the source)

## Delhi NCR suburban rail (Northern Railway EMU/MEMU)

| | |
|---|---|
| Feed id | `delhi-suburban` |
| Download | [suburban-rail.zip](suburban-rail.zip) (0.0 MB), mirror <https://maps.reclaim.city/gtfs/delhi-suburban.zip> |
| Modes | rail |
| Agencies | Northern Railway (Delhi suburban EMU/MEMU) |
| Routes / stops / trips | 14 / 140 / 400 |
| Trips with a shape | 400 (67 shapes) |
| Service | 2026-11-16 to 2027-11-16 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `translations.txt`, `trips.txt` |
| Source | [National Indian Railways GTFS (github.com/Neo2308), cut to the Delhi suburban lines by India Metro's suburban map; built by tools/suburban_gtfs.py](https://github.com/Neo2308) |
| Licence | none stated by the source |
| sha256 | `151a306a977a1e671b56e34636f3e8ea280a4b6f374e4241d93ed8819f4a1c9a` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 11,105 -> 2,288 shape points
- feed_info.txt added (none in the source)
