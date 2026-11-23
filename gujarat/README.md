# Gujarat

Feeds in this folder: 4. Back to the [repository README](../README.md).

## Ahmedabad (AMTS, Janmarg BRTS, Gandhinagar GTSL)

| | |
|---|---|
| Feed id | `ahmedabad` |
| Download | [ahmedabad/bus.zip](ahmedabad/bus.zip) (5.2 MB), mirror <https://maps.reclaim.city/gtfs/ahmedabad.zip> |
| Modes | bus |
| Agencies | Ahmedabad Municipal Transport Services, Ahmedabad Janmarg Limited, Gandhinagar Transport Services Limited |
| Routes / stops / trips | 975 / 6,638 / 14,459 |
| Trips with a shape | 12,998 (679 shapes) |
| Service | 2026-09-30 to 2027-11-23 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/amts/> |
| Source | [AMTS and Janmarg's own timetables and tracker (Amdavad ONE, amcitms.in), built into GTFS by reclaim.city; Gandhinagar GTSL from croyla/amd-gtfs](https://amdavadone.in/amts/bus-tracking) |
| Licence | none stated by the source |
| sha256 | `962a8f86fe6357809e85ad4ab2cb40953158f2cba4e85bce49c53c65bb4bcb89` |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/amts/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/amts/rt/trip_updates.pb), [status](https://maps.reclaim.city/amts/rt/status.json) |

> Unofficial: built from AMTS and Janmarg's own timetable and tracker (Amdavad ONE). Service is every day; the timetable has no calendar.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 592,379 -> 159,273 shape points

## GSRTC intercity (Gujarat State Road Transport Corporation)

| | |
|---|---|
| Feed id | `gsrtc` |
| Download | [gsrtc/bus.zip](gsrtc/bus.zip) (4.3 MB), mirror <https://maps.reclaim.city/gtfs/gsrtc.zip> |
| Modes | bus |
| Agencies | Gujarat State Road Transport Corporation |
| Routes / stops / trips | 2,258 / 218 / 5,788 |
| Trips with a shape | 5,788 (2,249 shapes) |
| Service | 2026-11-20 to 2027-05-19 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Source | [GSRTC public booking timetables (gsrtc.in OPRS), built into GTFS by reclaim.city (gsrtc_bus)](https://gsrtc.in/) |
| Licence | none stated by the source |
| sha256 | `a363138a79aa83f7dbdb625f1448db29f56aee64871123cbc015dc18415382d4` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 613,113 -> 611,889 shape points

## Rajkot (RRL BRTS + city)

| | |
|---|---|
| Feed id | `rajkot` |
| Download | [rajkot/bus.zip](rajkot/bus.zip) (0.8 MB), mirror <https://maps.reclaim.city/gtfs/rajkot.zip> |
| Modes | bus |
| Agencies | Rajkot Rajpath Limited |
| Routes / stops / trips | 271 / 760 / 3,168 |
| Trips with a shape | 3,168 (257 shapes) |
| Service | 2026-10-16 to 2027-04-14 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/rajkot/> |
| Source | [croyla/rrl-gtfs](https://github.com/croyla/rrl-gtfs) |
| Licence | MIT-0 |
| sha256 | `620a94c9e5f45c012299169a2c2ec5bd709f2dce25c51697bdeb14264f5bf269` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes for 3168 of 3168 trips that had none: the map's road-snapped line for the route (265 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 136,419 -> 43,097 shape points

## Vapi (VCBS)

| | |
|---|---|
| Feed id | `vapi` |
| Download | [vapi/bus.zip](vapi/bus.zip) (0.0 MB), mirror <https://maps.reclaim.city/gtfs/vapi.zip> |
| Modes | bus |
| Agencies | Vapi City Bus Service |
| Routes / stops / trips | 22 / 91 / 461 |
| Trips with a shape | 461 (22 shapes) |
| Service | 2026-01-01 to 2027-12-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/vapi/> |
| Source | [shubhamvelani/VapiGTFS](https://github.com/shubhamvelani/VapiGTFS) |
| Licence | none stated by the source |
| sha256 | `8b88c3ed69979a6a7f1a3c927c6bca90b6670e72f229e709aba8d3639d6b535a` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 2,336 -> 1,052 shape points
