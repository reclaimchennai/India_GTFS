# Himachal Pradesh

Feeds in this folder: 1. Back to the [repository README](../README.md).

## HRTC (Himachal Road Transport Corporation)

| | |
|---|---|
| Feed id | `hrtc` |
| Download | [hrtc/bus.zip](hrtc/bus.zip) (6.5 MB), mirror <https://maps.reclaim.city/gtfs/hrtc.zip> |
| Modes | bus |
| Agencies | Himachal Road Transport Corporation |
| Routes / stops / trips | 313 / 8,294 / 614 |
| Trips with a shape | 614 (611 shapes) |
| Service | 2026-11-21 to 2027-05-20 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/hrtc/> |
| Source | [HRTC's public booking site (online.hrtchp.com, OPRS guest search and Service Route Details), built into GTFS by reclaim.city (hrtc_bus)](https://online.hrtchp.com/oprs-web/guest/home.do) |
| Licence | none stated by the source |
| sha256 | `58be90cb58f8c17517f2ee9a689953268df75a706d18e6a6a6705f8eca3a9147` |

> Unofficial: HRTC's own stop times for the services sold online; local village services are not on the booking site. Some stop positions are approximate (on the road between neighbours).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 735,508 -> 733,178 shape points
