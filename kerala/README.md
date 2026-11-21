# Kerala

Feeds in this folder: 9. Back to the [repository README](../README.md).

## Kannur

| | |
|---|---|
| Feed id | `kannur` |
| Download | [kannur/bus.zip](kannur/bus.zip) (1.4 MB), mirror <https://maps.reclaim.city/gtfs/kannur.zip> |
| Modes | bus |
| Agencies | KANNUR PVT BUS, KSRTC |
| Routes / stops / trips | 510 / 1,808 / 2,995 |
| Trips with a shape | 2,995 (487 shapes) |
| Service | 2026-11-03 to 2027-11-03 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/kannur/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `e61ca8ea6ac5312a3de97c575f37ea96b2ae43418a769a4d990fa6dda458b2b8` |
| Routes without a timetable | [kannur/bus.routes_without_timetable.csv](kannur/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 33 stops served only by those routes moved with them
- 13 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 2995 of 2995 trips that had none: the map's road-snapped line for the route (510 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 126,278 -> 103,146 shape points

## Kasaragod

| | |
|---|---|
| Feed id | `kasaragod` |
| Download | [kasaragod/bus.zip](kasaragod/bus.zip) (1.3 MB), mirror <https://maps.reclaim.city/gtfs/kasaragod.zip> |
| Modes | bus |
| Agencies | KSRTC, PVT BUS KASARAGOD |
| Routes / stops / trips | 302 / 1,920 / 1,760 |
| Trips with a shape | 1,760 (299 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/kasaragod/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `1da1abf33d0528f8ddfae9c28b0e89a46c2dc36194bfaadc9f708db02cfd2fb5` |
| Routes without a timetable | [kasaragod/bus.routes_without_timetable.csv](kasaragod/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 80 stops served only by those routes moved with them
- 8 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 1760 of 1760 trips that had none: the map's road-snapped line for the route (302 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 123,256 -> 106,552 shape points

## Kochi

| | |
|---|---|
| Feed id | `kochi` |
| Download | [kochi/bus.zip](kochi/bus.zip) (1.0 MB), mirror <https://maps.reclaim.city/gtfs/kochi.zip> |
| Modes | bus |
| Agencies | DIGITAL BUS, KANJOOR CENTER, KMRL, KSRTC |
| Routes / stops / trips | 1,005 / 548 / 3,528 |
| Trips with a shape | 3,528 (699 shapes) |
| Service | 2026-11-03 to 2027-11-03 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/kochi/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `46a134b4384bfd517d5f86be0850ee3c9082654bec4eaebc8061688a3d111bfe` |
| Routes without a timetable | [kochi/bus.routes_without_timetable.csv](kochi/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 59 stops served only by those routes moved with them
- 370 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 3528 of 3528 trips that had none: the map's road-snapped line for the route (1005 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 99,377 -> 63,309 shape points

## Kottayam

| | |
|---|---|
| Feed id | `kottayam` |
| Download | [kottayam/bus.zip](kottayam/bus.zip) (3.4 MB), mirror <https://maps.reclaim.city/gtfs/kottayam.zip> |
| Modes | bus |
| Agencies | KBA, KSRTC |
| Routes / stops / trips | 1,380 / 2,063 / 9,512 |
| Trips with a shape | 9,497 (1,287 shapes) |
| Service | 2026-11-03 to 2027-11-03 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/kottayam/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `4a09562e54adde2799d0c0cd0354590d1047f3d5f6de3520464acc2d148694f7` |
| Routes without a timetable | [kottayam/bus.routes_without_timetable.csv](kottayam/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 12 stops served only by those routes moved with them
- 27 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 9497 of 9512 trips that had none: the map's road-snapped line for the route (1379 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 339,787 -> 269,909 shape points

## Kozhikode

| | |
|---|---|
| Feed id | `kozhikode` |
| Download | [kozhikode/bus.zip](kozhikode/bus.zip) (2.8 MB), mirror <https://maps.reclaim.city/gtfs/kozhikode.zip> |
| Modes | bus |
| Agencies | KOZHIKODE PVT BUS, KSRTC |
| Routes / stops / trips | 1,103 / 2,144 / 7,331 |
| Trips with a shape | 7,331 (1,054 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/kozhikode/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `8652e3b7df1c8673bd770bc074d1688f7fe5620ee12c9a047e818f01d0ae4db5` |
| Routes without a timetable | [kozhikode/bus.routes_without_timetable.csv](kozhikode/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 52 stops served only by those routes moved with them
- 27 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 7331 of 7331 trips that had none: the map's road-snapped line for the route (1103 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 270,018 -> 220,275 shape points

## Kerala KSRTC (intercity and mofussil)

| | |
|---|---|
| Feed id | `kerala-ksrtc` |
| Download | [ksrtc/bus.zip](ksrtc/bus.zip) (31.4 MB), mirror <https://maps.reclaim.city/gtfs/kerala-ksrtc.zip> |
| Modes | bus |
| Agencies | Kerala State Road Transport Corporation |
| Routes / stops / trips | 6,784 / 56,325 / 20,533 |
| Trips with a shape | 20,533 (6,696 shapes) |
| Service | 2026-11-21 to 2027-12-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/kerala/> |
| Source | [busz, the Kerala state journey planner (klotp2.busz.in OTP GTFS, kl.busz.in), KSRTC services only, built into GTFS by reclaim.city (kerala_bus)](https://www.keralartc.com/) |
| Licence | none stated by the source |
| sha256 | `1ba3f2e56ea8247eadf4743fac21064d419beff9fd53af5f14dbdea0ddcc4483` |

> Unofficial: KSRTC services from the busz journey planner; private operators excluded; daily calendar.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- stop times in 6672 trips: 0 past-midnight times written past 24:00, 0 intermediate times that ran backwards cleared (timepoint=0), 363177 departures before their own arrival set to the arrival
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 2,246,563 -> 2,232,030 shape points

## Thiruvananthapuram

| | |
|---|---|
| Feed id | `thiruvananthapuram` |
| Download | [thiruvananthapuram/bus.zip](thiruvananthapuram/bus.zip) (5.5 MB), mirror <https://maps.reclaim.city/gtfs/thiruvananthapuram.zip> |
| Modes | bus |
| Agencies | KSRTC |
| Routes / stops / trips | 3,247 / 2,579 / 26,519 |
| Trips with a shape | 26,519 (2,909 shapes) |
| Service | 2026-11-03 to 2027-11-03 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/thiruvananthapuram/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `297425638c67b609c1cd253eee7d7f17a9b56e3516f95b9955e2044612568702` |
| Routes without a timetable | [thiruvananthapuram/bus.routes_without_timetable.csv](thiruvananthapuram/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 239 stops served only by those routes moved with them
- 135 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 26519 of 26519 trips that had none: the map's road-snapped line for the route (3247 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 346,989 -> 276,615 shape points

## Thrissur

| | |
|---|---|
| Feed id | `thrissur` |
| Download | [thrissur/bus.zip](thrissur/bus.zip) (3.3 MB), mirror <https://maps.reclaim.city/gtfs/thrissur.zip> |
| Modes | bus |
| Agencies | KSRTC, MALAPPURAM PVT BUS |
| Routes / stops / trips | 1,571 / 2,122 / 11,209 |
| Trips with a shape | 11,209 (1,399 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/thrissur/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `ff2b79d95c43f9b48c7abc78c37ac5ab389c8e7c7f2b40f03ef2f91298d13558` |
| Routes without a timetable | [thrissur/bus.routes_without_timetable.csv](thrissur/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 50 stops served only by those routes moved with them
- 26 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 11209 of 11209 trips that had none: the map's road-snapped line for the route (1571 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 348,350 -> 270,278 shape points

## Wayanad

| | |
|---|---|
| Feed id | `wayanad` |
| Download | [wayanad/bus.zip](wayanad/bus.zip) (5.6 MB), mirror <https://maps.reclaim.city/gtfs/wayanad.zip> |
| Modes | bus |
| Agencies | KOZHIKODE PVT BUS, KSRTC |
| Routes / stops / trips | 969 / 4,483 / 6,895 |
| Trips with a shape | 6,895 (947 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/wayanad/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `00eaf85dc2fc43a75318d63e4a5fee560aa73c06420f670b7788812bb0bb3c2e` |
| Routes without a timetable | [wayanad/bus.routes_without_timetable.csv](wayanad/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 88 stops served only by those routes moved with them
- 30 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 6895 of 6895 trips that had none: the map's road-snapped line for the route (969 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 558,656 -> 479,706 shape points
