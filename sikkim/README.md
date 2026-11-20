# Sikkim

Feeds in this folder: 1. Back to the [repository README](../README.md).

## SNT (Sikkim Nationalised Transport)

| | |
|---|---|
| Feed id | `snt` |
| Download | [snt/bus.zip](snt/bus.zip) (0.0 MB), mirror <https://maps.reclaim.city/gtfs/snt.zip> |
| Modes | bus |
| Agencies | Sikkim Nationalised Transport (Transport Department, Government of Sikkim) |
| Routes / stops / trips | 10 / 9 / 23 |
| Trips with a shape | 23 (8 shapes) |
| Service | 2026-11-20 to 2027-05-19 |
| Files | `agency.txt`, `calendar.txt`, `fare_attributes.txt`, `fare_rules.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/sikkim/> |
| Source | [Sikkim Transport Department's published bus schedule and SNT's fare notification (Sikkim Government Gazette No. 325, 24 Jun 2024), built into GTFS by reclaim.city (sikkim_bus)](https://transportdepartment.sikkim.gov.in/visitors/busschedules) |
| Licence | none stated by the source |
| sha256 | `9efb44be353a8e55c4043c62325ae28590e4e0ec9cc2d6dcbb8a43fdce19e9fe` |

> Unofficial: inter-state services to and from Siliguri only; Namchi, Jorethang and Pelling services are ends only, as published; times past the first stop are estimates (timepoint=0).

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 3,148 -> 2,436 shape points
