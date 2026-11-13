# Delhi

Feeds in this folder: 4. Back to the [repository README](../README.md).

## Delhi (DTC and cluster buses)

| | |
|---|---|
| Feed id | `delhi` |
| Download | [bus.zip](bus.zip) (24.9 MB), mirror <https://maps.reclaim.city/gtfs/delhi.zip> |
| Modes | bus |
| Agencies | Delhi Transport Corporation, Department of Transport |
| Routes / stops / trips | 2,554 / 6,812 / 65,322 |
| Trips with a shape | 65,322 (2,554 shapes) |
| Service | 2025-01-01 to 2040-01-01 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/delhi/> |
| Source | [Delhi Transport Department / DTC, Delhi bus static GTFS v1 (Open Transit Data Delhi)](https://otd.delhi.gov.in/) |
| Licence | OTD Delhi terms |
| sha256 | `25030b23d46ea430af2f4e31ff90daabd97224a53fce79df6583ff2a7336fabc` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/delhi/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/delhi/rt/trip_updates.pb), [status](https://maps.reclaim.city/delhi/rt/status.json) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only

## Delhi Metro (DMRC, incl. Airport Express and Rapid Metro Gurugram)

| | |
|---|---|
| Feed id | `delhi-metro` |
| Download | [metro-dmrc.zip](metro-dmrc.zip) (1.1 MB), mirror <https://maps.reclaim.city/gtfs/delhi-metro.zip> |
| Modes | metro |
| Agencies | Delhi Metro Rail Corporation |
| Routes / stops / trips | 36 / 262 / 5,438 |
| Trips with a shape | 5,438 (36 shapes) |
| Service | 2019-01-01 to 2025-12-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Source | [DMRC static GTFS v1 (Open Transit Data Delhi)](https://otd.delhi.gov.in/) |
| Licence | OTD Delhi terms |
| sha256 | `ede43926bcf2e5937d7f50c899373cf2d777a739565b5e15b088674b6270acb8` |

> The official feed's calendar ended on 31 Dec 2025; republished as it is (the times are the current timetable pattern).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
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
| sha256 | `b768c743e12913c33db32b97c149a9f73320355ac84d7dc81488ebb3e8efafca` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route_type corrected on 2 routes (rail)
- feed_info.txt added (none in the source)

## Delhi NCR suburban rail (Northern Railway EMU/MEMU)

| | |
|---|---|
| Feed id | `delhi-suburban` |
| Download | [suburban-rail.zip](suburban-rail.zip) (0.1 MB), mirror <https://maps.reclaim.city/gtfs/delhi-suburban.zip> |
| Modes | rail |
| Agencies | Northern Railway (Delhi suburban EMU/MEMU) |
| Routes / stops / trips | 14 / 140 / 400 |
| Trips with a shape | 400 (337 shapes) |
| Service | 2026-11-13 to 2027-11-13 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `translations.txt`, `trips.txt` |
| Source | [National Indian Railways GTFS (github.com/Neo2308), cut to the Delhi suburban lines by India Metro's suburban map; built by tools/suburban_gtfs.py](https://github.com/Neo2308) |
| Licence | none stated by the source |
| sha256 | `ef7c69ba9de4e155735ccc629ec05b3038496621d70b908a5b63710b9f1b8803` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- feed_info.txt added (none in the source)
