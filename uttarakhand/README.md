# Uttarakhand

Feeds in this folder: 1. Back to the [repository README](../README.md).

## UTC (Uttarakhand Transport Corporation)

| | |
|---|---|
| Feed id | `utc` |
| Download | [utc/bus.zip](utc/bus.zip) (1.8 MB), mirror <https://maps.reclaim.city/gtfs/utc.zip> |
| Modes | bus |
| Agencies | Uttarakhand Transport Corporation |
| Routes / stops / trips | 135 / 860 / 730 |
| Trips with a shape | 730 (285 shapes) |
| Service | 2026-11-27 to 2027-05-26 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/utc/> |
| Source | [UTC's public online timetable (utconline.uk.gov.in/timetable.aspx), built into GTFS by reclaim.city (utc_bus)](https://utconline.uk.gov.in/timetable.aspx) |
| Licence | none stated by the source |
| sha256 | `cc4c550efe72a3bebb6066caa02404ea70e8185dd849f7fc38691f1c704aca8d` |

> Unofficial: services between the timetable's 83 stations only; stops between the ends are placed by name and timed by distance (timepoint=0).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 283,884 -> 200,257 shape points
