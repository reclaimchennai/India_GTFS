# West Bengal

Feeds in this folder: 4. Back to the [repository README](../README.md).

## Kolkata (bus, metro, suburban rail, ferry)

| | |
|---|---|
| Feed id | `kolkata` |
| Download | [kolkata/all-modes.zip](kolkata/all-modes.zip) (8.4 MB), mirror <https://maps.reclaim.city/gtfs/kolkata.zip> |
| Modes | bus, ferry, metro, rail |
| Agencies | West Bengal Transport Corporation, Private route buses (Kolkata), Private minibuses (Kolkata), Other bus operators (as named in the Chalo app), West Bengal Transport Corporation (Calcutta Tramways), State transport routes (WBTC / SBSTC / NBSTC, community list), Hooghly river ferries, Indian Railways suburban services (Eastern and South Eastern Railway), Metro Railway, Kolkata |
| Routes / stops / trips | 2,449 / 9,208 / 6,646 |
| Trips with a shape | 6,558 (4,055 shapes) |
| Service | 2026-11-01 to 2027-10-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `frequencies.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/kolkata/> |
| Licence | none stated by the source |
| sha256 | `cb71ee51aca31b394357be461ea13b29402101b1824ece3c29ad431b09d11114` |
| Routes without a timetable | [kolkata/all-modes.routes_without_timetable.csv](kolkata/all-modes.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

> Unofficial (no Kolkata operator publishes GTFS). Trams: the timetables are placeholders and most routes are suspended, so they are listed without times.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 71 stops served only by those routes moved with them
- 21 routes with no timetable (placeholder times, tram routes) moved to routes_without_timetable.csv
- shapes for 1064 of 1152 trips that had none: the map's road-snapped line for the route (1064 shapes)
- 43 shapes no trip uses left out
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
| sha256 | `8343c1545de878b28c60104e5866b03d63dad6be72975e2c73984495e51d9efc` |

> Unofficial: mostly headway-based services (frequencies.txt).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only

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
| sha256 | `cf1a445c86ec451bb4c3db359ed5280d74f2cfc5e12fe963519a8a235ab77a05` |

> Unofficial: real first and last trains and headways; times at later stations estimated from distance.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- frequencies.txt left out (header only, no rows)
- 1 shapes no trip uses left out

## Kolkata suburban rail (Eastern and South Eastern Railway)

| | |
|---|---|
| Feed id | `kolkata-suburban` |
| Download | [kolkata/suburban-rail.zip](kolkata/suburban-rail.zip) (0.7 MB), mirror <https://maps.reclaim.city/gtfs/kolkata-suburban.zip> |
| Modes | rail |
| Agencies | Indian Railways suburban services (Eastern and South Eastern Railway) |
| Routes / stops / trips | 25 / 406 / 2,460 |
| Trips with a shape | 2,460 (1,652 shapes) |
| Service | 2026-11-01 to 2027-10-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Licence | none stated by the source |
| sha256 | `ce8b14335b03c91fe8e887c927b9306e56ccc08b6f9f1e2ef33befd5a819535c` |

> Unofficial: built from the national Indian Railways GTFS.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- frequencies.txt left out (header only, no rows)
