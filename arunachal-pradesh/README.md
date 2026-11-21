# Arunachal Pradesh

Feeds in this folder: 1. Back to the [repository README](../README.md).

## APSTS (Arunachal Pradesh State Transport Services)

| | |
|---|---|
| Feed id | `apsts` |
| Download | [apsts/bus.zip](apsts/bus.zip) (1.2 MB), mirror <https://maps.reclaim.city/gtfs/apsts.zip> |
| Modes | bus |
| Agencies | Arunachal Pradesh State Transport Services |
| Routes / stops / trips | 63 / 173 / 178 |
| Trips with a shape | 178 (136 shapes) |
| Service | 2026-11-21 to 2027-05-20 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/apsts/> |
| Source | [APSTS online timetable (apsts.arunachal.gov.in, NIC StarBus), built into GTFS by reclaim.city (ne_states_bus)](https://apsts.arunachal.gov.in/timetable.aspx) |
| Licence | none stated by the source |
| sha256 | `81e73f3ada4e06d8519be15461132a4b4eb48fc703d9f9a213898ad22e5b84dd` |

> Unofficial: the site's approximate stop times; weekday-numbered services merged into daily trips; small villages missing.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 105,960 -> 105,925 shape points
