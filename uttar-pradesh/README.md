# Uttar Pradesh

Feeds in this folder: 14. Back to the [repository README](../README.md).

## Agra

| | |
|---|---|
| Feed id | `agra` |
| Download | [agra/bus.zip](agra/bus.zip) (0.1 MB), mirror <https://maps.reclaim.city/gtfs/agra.zip> |
| Modes | bus |
| Agencies | AMCTSL |
| Routes / stops / trips | 44 / 384 / 451 |
| Trips with a shape | 451 (44 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/agra/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `33d829c33e7cc29e9ee1b3cbe4e8e91a028478f23f031376990a58cb6fe45b97` |
| Routes without a timetable | [agra/bus.routes_without_timetable.csv](agra/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 115 stops served only by those routes moved with them
- 12 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 451 of 451 trips that had none: the map's road-snapped line for the route (44 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 19,498 -> 5,502 shape points

## Ayodhya

| | |
|---|---|
| Feed id | `ayodhya` |
| Download | [ayodhya/bus.zip](ayodhya/bus.zip) (0.0 MB), mirror <https://maps.reclaim.city/gtfs/ayodhya.zip> |
| Modes | bus |
| Agencies | CITY BUS AYODHYA |
| Routes / stops / trips | 10 / 123 / 150 |
| Trips with a shape | 150 (10 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/ayodhya/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `f70dcdc6ec55c9b966d82941a0081f990cfe1820199a7f3e6c960dff6dd9fd69` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes.txt left out (header only, no rows)
- shapes for 150 of 150 trips that had none: the map's road-snapped line for the route (10 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 6,527 -> 1,642 shape points

## Bareilly

| | |
|---|---|
| Feed id | `bareilly` |
| Download | [bareilly/bus.zip](bareilly/bus.zip) (0.0 MB), mirror <https://maps.reclaim.city/gtfs/bareilly.zip> |
| Modes | bus |
| Agencies | BCTSL |
| Routes / stops / trips | 6 / 125 / 70 |
| Trips with a shape | 70 (6 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/bareilly/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `238041e9995f8ee89b99a75a516429ac2c19fcc85d2a0bec1be1da287c86dc20` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes.txt left out (header only, no rows)
- shapes for 70 of 70 trips that had none: the map's road-snapped line for the route (6 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 1,833 -> 613 shape points

## Ghaziabad

| | |
|---|---|
| Feed id | `ghaziabad` |
| Download | [ghaziabad/bus.zip](ghaziabad/bus.zip) (0.1 MB), mirror <https://maps.reclaim.city/gtfs/ghaziabad.zip> |
| Modes | bus |
| Agencies | Ghaziabad City Transport Services Ltd |
| Routes / stops / trips | 32 / 224 / 471 |
| Trips with a shape | 0 (0 shapes) |
| Service | 2026-10-01 to 2027-10-01 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `c152a2badba4a07c0b830c492bbdbfb23e898ea7da359f25a049a59857e8e80a` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- feed_info.txt added (none in the source)

## Gorakhpur

| | |
|---|---|
| Feed id | `gorakhpur` |
| Download | [gorakhpur/bus.zip](gorakhpur/bus.zip) (0.0 MB), mirror <https://maps.reclaim.city/gtfs/gorakhpur.zip> |
| Modes | bus |
| Agencies | GCTSL |
| Routes / stops / trips | 8 / 155 / 60 |
| Trips with a shape | 60 (8 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/gorakhpur/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `12054859a7bb42ca4da95c049700b970de8d7d210237b91c65adbb48345e49ef` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes.txt left out (header only, no rows)
- shapes for 60 of 60 trips that had none: the map's road-snapped line for the route (8 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 4,514 -> 1,287 shape points

## Jhansi

| | |
|---|---|
| Feed id | `jhansi` |
| Download | [jhansi/bus.zip](jhansi/bus.zip) (0.0 MB), mirror <https://maps.reclaim.city/gtfs/jhansi.zip> |
| Modes | bus |
| Agencies | JCTSL |
| Routes / stops / trips | 21 / 82 / 260 |
| Trips with a shape | 260 (20 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/jhansi/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `1de01adfd4f36a597e882528c8e43f138f38eb2d9d7c4612815a6c50bd8e3485` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes.txt left out (header only, no rows)
- shapes for 260 of 260 trips that had none: the map's road-snapped line for the route (21 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 8,968 -> 2,168 shape points

## Kanpur

| | |
|---|---|
| Feed id | `kanpur` |
| Download | [kanpur/bus.zip](kanpur/bus.zip) (0.2 MB), mirror <https://maps.reclaim.city/gtfs/kanpur.zip> |
| Modes | bus |
| Agencies | KCTSL |
| Routes / stops / trips | 30 / 752 / 328 |
| Trips with a shape | 151 (15 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/kanpur/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `da91c5dec9dce243225be1c34f52dbf6355be03fc1a6be573fd1707135199b60` |
| Routes without a timetable | [kanpur/bus.routes_without_timetable.csv](kanpur/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 397 stops served only by those routes moved with them
- 81 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 151 of 328 trips that had none: the map's road-snapped line for the route (15 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 3,141 -> 2,747 shape points

## Lucknow

| | |
|---|---|
| Feed id | `lucknow` |
| Download | [lucknow/bus.zip](lucknow/bus.zip) (0.2 MB), mirror <https://maps.reclaim.city/gtfs/lucknow.zip> |
| Modes | bus |
| Agencies | DIGITAL BUS, LCTSL |
| Routes / stops / trips | 32 / 707 / 444 |
| Trips with a shape | 250 (28 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/lucknow/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `f74c0d8082f9ef0207002ccc2dbeae29fcf686d859b7b8c7bcf315978eb2336c` |
| Routes without a timetable | [lucknow/bus.routes_without_timetable.csv](lucknow/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 129 stops served only by those routes moved with them
- 32 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 250 of 444 trips that had none: the map's road-snapped line for the route (28 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 6,482 -> 5,650 shape points

## Mathura

| | |
|---|---|
| Feed id | `mathura` |
| Download | [mathura/bus.zip](mathura/bus.zip) (0.1 MB), mirror <https://maps.reclaim.city/gtfs/mathura.zip> |
| Modes | bus |
| Agencies | AMCTSL |
| Routes / stops / trips | 24 / 220 / 302 |
| Trips with a shape | 302 (24 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/mathura/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `f233acfe7728941437591034508ee89990ddd01ec2e5e2dfca6336f26e10b62d` |
| Routes without a timetable | [mathura/bus.routes_without_timetable.csv](mathura/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 192 stops served only by those routes moved with them
- 18 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 302 of 302 trips that had none: the map's road-snapped line for the route (24 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 17,170 -> 4,594 shape points

## Meerut

| | |
|---|---|
| Feed id | `meerut` |
| Download | [meerut/bus.zip](meerut/bus.zip) (0.0 MB), mirror <https://maps.reclaim.city/gtfs/meerut.zip> |
| Modes | bus |
| Agencies | Meerut City Transport Services Ltd |
| Routes / stops / trips | 28 / 260 / 293 |
| Trips with a shape | 0 (0 shapes) |
| Service | 2026-10-01 to 2027-10-01 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `86b103945485631ec63591b86cdab8b1cd4ffea3320e15fa53252c19b75e0091` |
| Routes without a timetable | [meerut/bus.routes_without_timetable.csv](meerut/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 192 stops served only by those routes moved with them
- 51 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- feed_info.txt added (none in the source)

## Noida

| | |
|---|---|
| Feed id | `noida` |
| Download | [noida/bus.zip](noida/bus.zip) (0.0 MB), mirror <https://maps.reclaim.city/gtfs/noida.zip> |
| Modes | bus |
| Agencies | Noida e-bus (Noida Authority / UPSRTC, reported), NMRC feeder bus, UPSRTC Noida region |
| Routes / stops / trips | 24 / 34 / 330 |
| Trips with a shape | 0 (0 shapes) |
| Service | 2026-10-01 to 2027-10-01 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `39642bad503891cfe2d24455eab8e650f0b9d7b815241f9d5bc26e18bed2df8c` |
| Routes without a timetable | [noida/bus.routes_without_timetable.csv](noida/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 24 stops served only by those routes moved with them
- 5 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- calendar.txt added (the build wrote none): the daily service of its sibling NCR feeds
- feed_info.txt added (none in the source)

## Prayagraj

| | |
|---|---|
| Feed id | `prayagraj` |
| Download | [prayagraj/bus.zip](prayagraj/bus.zip) (0.1 MB), mirror <https://maps.reclaim.city/gtfs/prayagraj.zip> |
| Modes | bus |
| Agencies | ACTSL |
| Routes / stops / trips | 15 / 238 / 115 |
| Trips with a shape | 115 (15 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/prayagraj/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `1a7e0a901fca8c4d68e2e34705601bb8b4330751cbd0c7f84bc1463729b013c2` |
| Routes without a timetable | [prayagraj/bus.routes_without_timetable.csv](prayagraj/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 672 stops served only by those routes moved with them
- 95 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 115 of 115 trips that had none: the map's road-snapped line for the route (15 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 3,407 -> 2,946 shape points

## UPSRTC (Uttar Pradesh State Road Transport Corporation, intercity)

| | |
|---|---|
| Feed id | `upsrtc` |
| Download | [upsrtc/bus.zip](upsrtc/bus.zip) (13.5 MB), mirror <https://maps.reclaim.city/gtfs/upsrtc.zip> |
| Modes | bus |
| Agencies | Uttar Pradesh State Road Transport Corporation |
| Routes / stops / trips | 7,230 / 7,936 / 50,789 |
| Trips with a shape | 50,789 (6,926 shapes) |
| Service | 2026-11-21 to 2027-12-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/upsrtc/> |
| Source | [UPSRTC's Margdarshi tracking backend (margdarshi.upsrtcvlt.com): its line list and route timetables, built into GTFS by reclaim.city (up_bus)](https://www.upsrtc.com/) |
| Licence | none stated by the source |
| sha256 | `858ab1da769734a7f40a19a1c13790a163940edbd87288754383482ebbfa0f00` |

> Unofficial: UPSRTC's own Margdarshi route timetables; daily calendar.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- stop times in 18431 trips: 7 past-midnight times written past 24:00, 99 intermediate times that ran backwards cleared (timepoint=0), 211984 departures before their own arrival set to the arrival
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 839,321 -> 819,084 shape points

## Varanasi

| | |
|---|---|
| Feed id | `varanasi` |
| Download | [varanasi/bus.zip](varanasi/bus.zip) (0.2 MB), mirror <https://maps.reclaim.city/gtfs/varanasi.zip> |
| Modes | bus |
| Agencies | VCTL |
| Routes / stops / trips | 123 / 358 / 688 |
| Trips with a shape | 688 (113 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/varanasi/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `0926d4979d99f87360ec1a06e1e5340dde15e038e255d9b541929e74374b451d` |
| Routes without a timetable | [varanasi/bus.routes_without_timetable.csv](varanasi/bus.routes_without_timetable.csv) (route, stops in order; not in the GTFS) |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 58 stops served only by those routes moved with them
- 26 routes with no timetable (one placeholder trip at midnight each) moved to routes_without_timetable.csv
- shapes.txt left out (header only, no rows)
- shapes for 688 of 688 trips that had none: the map's road-snapped line for the route (123 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 15,728 -> 12,741 shape points
