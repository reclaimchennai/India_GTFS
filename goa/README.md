# Goa

Feeds in this folder: 1. Back to the [repository README](../README.md).

## Goa (Kadamba Transport Corporation)

| | |
|---|---|
| Feed id | `goa` |
| Download | [ktcl-bus.zip](ktcl-bus.zip) (5.8 MB), mirror <https://maps.reclaim.city/gtfs/goa.zip> |
| Modes | bus |
| Agencies | Kadamba |
| Routes / stops / trips | 476 / 3,255 / 3,130 |
| Trips with a shape | 1,927 (457 shapes) |
| Service | 2023-09-01 to 2025-08-01 |
| Files | `agency.txt`, `calendar.txt`, `fare_attributes.txt`, `fare_rules.txt`, `feed_info.txt`, `frequencies.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/goa/> |
| Source | [Goa Transport Department: KTCL GTFS](https://goatransport.gov.in/GTFS) |
| Licence | none stated by the source |
| sha256 | `76317c750c2d375733297f8d70a6193e475f8eb7ce102fd17937ef9c425080d4` |

> The official feed's calendar ended on 1 Aug 2025; republished as it is.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- calendar_dates.txt left out (header only, no rows)
- feed_info.txt left out (header only, no rows)
- shapes.txt left out (header only, no rows)
- transfers.txt left out (header only, no rows)
- shapes for 1927 of 3130 trips that had none: the map's road-snapped line for the route (464 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 337,241 -> 292,540 shape points
- feed_info.txt added (none in the source)
