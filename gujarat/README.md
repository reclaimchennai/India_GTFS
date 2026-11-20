# Gujarat

Feeds in this folder: 3. Back to the [repository README](../README.md).

## Ahmedabad (AMTS, Janmarg BRTS, Gandhinagar GTSL)

| | |
|---|---|
| Feed id | `ahmedabad` |
| Download | [ahmedabad/bus.zip](ahmedabad/bus.zip) (5.9 MB), mirror <https://maps.reclaim.city/gtfs/ahmedabad.zip> |
| Modes | bus |
| Agencies | Ahmedabad Municipal Transport Services, Ahmedabad Janmarg Limited, Gandhinagar Transport Services Limited |
| Routes / stops / trips | 978 / 3,235 / 14,323 |
| Trips with a shape | 14,316 (944 shapes) |
| Service | 2026-09-30 to 2027-03-29 |
| Files | `agency.txt`, `areas.txt`, `calendar.txt`, `fare_leg_rules.txt`, `fare_products.txt`, `feed_info.txt`, `rider_categories.txt`, `routes.txt`, `shapes.txt`, `stop_areas.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/ahmedabad/> |
| Source | [croyla/amd-gtfs](https://github.com/croyla/amd-gtfs) |
| Licence | MIT |
| sha256 | `2ab7ff9586231f8302304224281abfb31104d8e54e9a8ef0b2ea0a07fdcd5154` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes for 14316 of 14323 trips that had none: the map's road-snapped line for the route (972 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 283,752 -> 247,111 shape points

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
