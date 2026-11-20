# West Bengal

Feeds in this folder: 5. Back to the [repository README](../README.md).

## Kolkata (bus, metro, suburban rail, ferry)

| | |
|---|---|
| Feed id | `kolkata` |
| Download | [kolkata/all-modes.zip](kolkata/all-modes.zip) (5.3 MB), mirror <https://maps.reclaim.city/gtfs/kolkata.zip> |
| Modes | bus, ferry, metro, rail |
| Agencies | West Bengal Transport Corporation, Private route buses (Kolkata), Private minibuses (Kolkata), Other bus operators (as named in the Chalo app), West Bengal Transport Corporation (Calcutta Tramways), State transport routes (WBTC / SBSTC / NBSTC, community list), Hooghly river ferries, Indian Railways suburban services (Eastern and South Eastern Railway), Metro Railway, Kolkata |
| Routes / stops / trips | 2,449 / 9,208 / 6,646 |
| Trips with a shape | 6,558 (2,577 shapes) |
| Service | 2026-11-01 to 2027-10-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `frequencies.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/kolkata/> |
| Licence | none stated by the source |
| sha256 | `c4f14ab0a6da671a1ffb2cf8d26790d8e457b68b7b843af5a4bf276da5215e76` |
| Routes without a timetable | [kolkata/all-modes.routes_without_timetable.csv](kolkata/all-modes.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

> Unofficial (no Kolkata operator publishes GTFS). Trams: the timetables are placeholders and most routes are suspended, so they are listed without times.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 71 stops served only by those routes moved with them
- 21 routes with no timetable (placeholder times, tram routes) moved to routes_without_timetable.csv
- shapes for 1064 of 1152 trips that had none: the map's road-snapped line for the route (1064 shapes)
- 43 shapes no trip uses left out
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 935,796 -> 498,125 shape points
- feed_info.txt added (none in the source)

## Kolkata Hooghly ferries

| | |
|---|---|
| Feed id | `kolkata-ferry` |
| Download | [kolkata/ferry.zip](kolkata/ferry.zip) (0.0 MB), mirror <https://maps.reclaim.city/gtfs/kolkata-ferry.zip> |
| Modes | ferry |
| Agencies | Hooghly river ferries |
| Routes / stops / trips | 20 / 30 / 40 |
| Trips with a shape | 40 (40 shapes) |
| Service | 2026-11-01 to 2027-10-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `frequencies.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Licence | none stated by the source |
| sha256 | `c999ada44b63c4abbce57997af8e040183979d172a2dbb48a3514db6116a8b5d` |

> Unofficial: mostly headway-based services (frequencies.txt).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 460 -> 450 shape points

## Kolkata Metro

| | |
|---|---|
| Feed id | `kolkata-metro` |
| Download | [kolkata/metro.zip](kolkata/metro.zip) (0.2 MB), mirror <https://maps.reclaim.city/gtfs/kolkata-metro.zip> |
| Modes | metro |
| Agencies | Metro Railway, Kolkata |
| Routes / stops / trips | 5 / 55 / 1,704 |
| Trips with a shape | 1,704 (9 shapes) |
| Service | 2026-11-01 to 2027-10-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Licence | none stated by the source |
| sha256 | `d0abac6bbe080dae1bd02a1b0de8ba5655b67f85379f60a23d44eeb294fc4d30` |

> Unofficial: real first and last trains and headways; times at later stations estimated from distance.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- frequencies.txt left out (header only, no rows)
- 1 shapes no trip uses left out

## Kolkata suburban rail (Eastern and South Eastern Railway)

| | |
|---|---|
| Feed id | `kolkata-suburban` |
| Download | [kolkata/suburban-rail.zip](kolkata/suburban-rail.zip) (0.4 MB), mirror <https://maps.reclaim.city/gtfs/kolkata-suburban.zip> |
| Modes | rail |
| Agencies | Indian Railways suburban services (Eastern and South Eastern Railway) |
| Routes / stops / trips | 25 / 406 / 2,460 |
| Trips with a shape | 2,460 (355 shapes) |
| Service | 2026-11-01 to 2027-10-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Licence | none stated by the source |
| sha256 | `a66c0b1958e40da551a82976231551535e7f6fc1f66f7cb213e15598fb4152e6` |

> Unofficial: built from the national Indian Railways GTFS.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- frequencies.txt left out (header only, no rows)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 97,523 -> 20,134 shape points

## WBTC (West Bengal Transport Corporation)

| | |
|---|---|
| Feed id | `wbtc` |
| Download | [wbtc/bus.zip](wbtc/bus.zip) (0.1 MB), mirror <https://maps.reclaim.city/gtfs/wbtc.zip> |
| Modes | bus |
| Agencies | West Bengal Transport Corporation |
| Routes / stops / trips | 50 / 51 / 242 |
| Trips with a shape | 242 (83 shapes) |
| Service | 2026-11-21 to 2027-05-20 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/wbtc/> |
| Source | [WBTC online booking site (wbtconline.in: route list and the departures sold from each boarding point), built into GTFS by reclaim.city (wbtc_bus)](https://wbtconline.in/) |
| Licence | none stated by the source |
| sha256 | `3922e7b3035520184330eee138e3e468706cf95de8ba051c3f657c1fc6bc75ea` |

> Unofficial: departures by boarding point as sold on wbtconline.in; arrivals and unsold points are estimates (timepoint=0). Long-distance only; city routes are in west-bengal/kolkata.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 20,832 -> 17,277 shape points
