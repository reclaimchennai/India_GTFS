# Maharashtra

Feeds in this folder: 4. Back to the [repository README](../README.md).

## Mumbai region bus (BEST, TMT, KDMT, VVMT)

| | |
|---|---|
| Feed id | `mumbai` |
| Download | [mumbai/bus.zip](mumbai/bus.zip) (16.5 MB), mirror <https://maps.reclaim.city/gtfs/mumbai.zip> |
| Modes | bus |
| Agencies | Kalyan Dombivali Municipal Transport, Thane Municipal Transport, Brihanmumbai Electric Supply and Transport, Vasai-Virar Municipal Transport |
| Routes / stops / trips | 1,609 / 10,279 / 99,080 |
| Trips with a shape | 98,878 (1,115 shapes) |
| Service | 2026-08-19 to 2027-02-15 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/mumbai/> |
| Source | [croyla/mumbai-gtfs (BLRTransit)](https://github.com/croyla/mumbai-gtfs) |
| Licence | MIT-0 |
| sha256 | `76d82ea119b5cf869e44857fa9431618887934d3166cb16f7a5d205c9379fa69` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/mumbai/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/mumbai/rt/trip_updates.pb), [status](https://maps.reclaim.city/mumbai/rt/status.json) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes for 98878 of 99080 trips that had none: the map's road-snapped line for the route (1115 shapes)

## Mumbai suburban rail (Western, Central, Harbour, Trans-Harbour, Uran)

| | |
|---|---|
| Feed id | `mumbai-suburban` |
| Download | [mumbai/suburban-rail.zip](mumbai/suburban-rail.zip) (0.9 MB), mirror <https://maps.reclaim.city/gtfs/mumbai-suburban.zip> |
| Modes | rail |
| Agencies | Western Railway and Central Railway (Mumbai Suburban) |
| Routes / stops / trips | 9 / 123 / 3,721 |
| Trips with a shape | 3,721 (1,926 shapes) |
| Service | 2026-11-13 to 2027-11-13 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `translations.txt`, `trips.txt` |
| Source | [Rush Hour's Mumbai timetable (railway working timetables: WR Feb 2026, Harbour Oct 2024, Trans-Harbour Jan 2024, Port line Dec 2025), via India Metro's suburban map; built by tools/suburban_gtfs.py](https://git.sr.ht/~sphericalkat/rush-hour) |
| Licence | MIT |
| sha256 | `9e7d4d64b245698e2d560d61ae02fc3e8b1337e43c83aae13d37ffba626ca272` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- feed_info.txt added (none in the source)

## Nagpur

| | |
|---|---|
| Feed id | `nagpur` |
| Download | [nagpur/bus.zip](nagpur/bus.zip) (3.0 MB), mirror <https://maps.reclaim.city/gtfs/nagpur.zip> |
| Modes | bus |
| Agencies | NMPL |
| Routes / stops / trips | 900 / 3,896 / 8,619 |
| Trips with a shape | 8,618 (899 shapes) |
| Service | 2026-11-03 to 2027-11-03 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/nagpur/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `c723694f137ec1915f5837f83e710fb4a23b508e0e4fb72f07fe9a8f0217ddbf` |
| Routes without a timetable | [nagpur/bus.routes_without_timetable.csv](nagpur/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 124 stops served only by those routes moved with them
- 115 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 8618 of 8619 trips that had none: the map's road-snapped line for the route (899 shapes)

## Pune (PMPML)

| | |
|---|---|
| Feed id | `pune` |
| Download | [pune/bus.zip](pune/bus.zip) (4.7 MB), mirror <https://maps.reclaim.city/gtfs/pune.zip> |
| Modes | bus |
| Agencies | Pune Mahanagar Parivahan Mahamandal Limited |
| Routes / stops / trips | 628 / 6,745 / 10,128 |
| Trips with a shape | 10,128 (628 shapes) |
| Service | 2026-10-07 to 2027-04-05 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/pune/> |
| Licence | none stated by the source |
| sha256 | `ec7a8ec794aac7633e34bcada1ab4de56d1cf45098369f27e7a02245526d0d7d` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
