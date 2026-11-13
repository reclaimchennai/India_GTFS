# Goa

Feeds in this folder: 1. Back to the [repository README](../README.md).

## Goa (Kadamba Transport Corporation)

| | |
|---|---|
| Feed id | `goa` |
| Download | [ktcl-bus.zip](ktcl-bus.zip) (6.1 MB), mirror <https://maps.reclaim.city/gtfs/goa.zip> |
| Modes | bus |
| Agencies | Kadamba |
| Routes / stops / trips | 476 / 3,255 / 3,130 |
| Trips with a shape | 1,927 (464 shapes) |
| Service | 2023-09-01 to 2025-08-01 |
| Files | `agency.txt`, `calendar.txt`, `fare_attributes.txt`, `fare_rules.txt`, `feed_info.txt`, `frequencies.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/goa/> |
| Source | [Goa Transport Department: KTCL GTFS](https://goatransport.gov.in/GTFS) |
| Licence | none stated by the source |
| sha256 | `5ca8f9d8752544102d1f85a7c4d436b802d7fef6fc09a1b9e40bb995eea7eb6f` |

> The official feed's calendar ended on 1 Aug 2025; republished as it is.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- calendar_dates.txt left out (header only, no rows)
- feed_info.txt left out (header only, no rows)
- shapes.txt left out (header only, no rows)
- transfers.txt left out (header only, no rows)
- shapes for 1927 of 3130 trips that had none: the map's road-snapped line for the route (464 shapes)
- feed_info.txt added (none in the source)
