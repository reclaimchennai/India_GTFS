# Uttarakhand

Feeds in this folder: 1. Back to the [repository README](../README.md).

## UTC (Uttarakhand Transport Corporation)

| | |
|---|---|
| Feed id | `utc` |
| Download | [utc/bus.zip](utc/bus.zip) (1.9 MB), mirror <https://maps.reclaim.city/gtfs/utc.zip> |
| Modes | bus |
| Agencies | Uttarakhand Transport Corporation |
| Routes / stops / trips | 135 / 860 / 730 |
| Trips with a shape | 730 (285 shapes) |
| Service | 2026-11-21 to 2027-05-20 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/utc/> |
| Source | [UTC's public online timetable (utconline.uk.gov.in/timetable.aspx), built into GTFS by reclaim.city (utc_bus)](https://utconline.uk.gov.in/timetable.aspx) |
| Licence | none stated by the source |
| sha256 | `e869780f0aa37894f0c0397f93d67fb47a1979fb1bce6e7ae5bb227f9f7f93b3` |

> Unofficial: services between the timetable's 83 stations only; stops between the ends are placed by name and timed by distance (timepoint=0).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 307,194 -> 213,803 shape points
