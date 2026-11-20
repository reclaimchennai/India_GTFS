# Maharashtra

Feeds in this folder: 4. Back to the [repository README](../README.md).

## Mumbai region bus (BEST, TMT, KDMT, VVMT)

| | |
|---|---|
| Feed id | `mumbai` |
| Download | [mumbai/bus.zip](mumbai/bus.zip) (14.2 MB), mirror <https://maps.reclaim.city/gtfs/mumbai.zip> |
| Modes | bus |
| Agencies | Kalyan Dombivali Municipal Transport, Thane Municipal Transport, Brihanmumbai Electric Supply and Transport, Vasai-Virar Municipal Transport |
| Routes / stops / trips | 1,609 / 10,279 / 99,080 |
| Trips with a shape | 98,878 (1,110 shapes) |
| Service | 2026-08-19 to 2027-02-15 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/mumbai/> |
| Source | [croyla/mumbai-gtfs (BLRTransit)](https://github.com/croyla/mumbai-gtfs) |
| Licence | MIT-0 |
| sha256 | `d5b4a7df54a773fa2c42709dd69153286ab326304ff26ea8e0aab8341fe6cd02` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/mumbai/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/mumbai/rt/trip_updates.pb), [status](https://maps.reclaim.city/mumbai/rt/status.json) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes for 98878 of 99080 trips that had none: the map's road-snapped line for the route (1115 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 488,755 -> 172,645 shape points

## Mumbai suburban rail (Western, Central, Harbour, Trans-Harbour, Uran)

| | |
|---|---|
| Feed id | `mumbai-suburban` |
| Download | [mumbai/suburban-rail.zip](mumbai/suburban-rail.zip) (0.4 MB), mirror <https://maps.reclaim.city/gtfs/mumbai-suburban.zip> |
| Modes | rail |
| Agencies | Western Railway and Central Railway (Mumbai Suburban) |
| Routes / stops / trips | 9 / 123 / 3,721 |
| Trips with a shape | 3,721 (208 shapes) |
| Service | 2026-11-16 to 2027-11-16 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `translations.txt`, `trips.txt` |
| Source | [Rush Hour's Mumbai timetable (railway working timetables: WR Feb 2026, Harbour Oct 2024, Trans-Harbour Jan 2024, Port line Dec 2025), via India Metro's suburban map; built by tools/suburban_gtfs.py](https://git.sr.ht/~sphericalkat/rush-hour) |
| Licence | MIT |
| sha256 | `e311e42deefefca0d45aff10a9b596576dfe5726af2b44561064b3687fceaac1` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 138,760 -> 14,409 shape points
- feed_info.txt added (none in the source)

## Nagpur

| | |
|---|---|
| Feed id | `nagpur` |
| Download | [nagpur/bus.zip](nagpur/bus.zip) (2.9 MB), mirror <https://maps.reclaim.city/gtfs/nagpur.zip> |
| Modes | bus |
| Agencies | NMPL |
| Routes / stops / trips | 900 / 3,896 / 8,619 |
| Trips with a shape | 8,618 (895 shapes) |
| Service | 2026-11-03 to 2027-11-03 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/nagpur/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `935d26dddbb637551eb368c81ffbbb7e54650f39102c0ca7cc61f41beb526b3d` |
| Routes without a timetable | [nagpur/bus.routes_without_timetable.csv](nagpur/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 124 stops served only by those routes moved with them
- 115 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 8618 of 8619 trips that had none: the map's road-snapped line for the route (899 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 107,909 -> 94,895 shape points

## Pune (PMPML)

| | |
|---|---|
| Feed id | `pune` |
| Download | [pune/bus.zip](pune/bus.zip) (3.7 MB), mirror <https://maps.reclaim.city/gtfs/pune.zip> |
| Modes | bus |
| Agencies | Pune Mahanagar Parivahan Mahamandal Limited |
| Routes / stops / trips | 628 / 6,745 / 10,128 |
| Trips with a shape | 10,128 (628 shapes) |
| Service | 2026-10-07 to 2027-04-05 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/pune/> |
| Source | [croyla/pmpml-gtfs](https://github.com/croyla/pmpml-gtfs) |
| Licence | MIT-0 |
| sha256 | `c32d515fd87786d8129f082816624d0a7bbf3a4f81d1a4885ece2095a9aaf4f3` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 256,823 -> 106,052 shape points
