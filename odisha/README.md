# Odisha

Feeds in this folder: 2. Back to the [repository README](../README.md).

## Rourkela

| | |
|---|---|
| Feed id | `rourkela` |
| Download | [rourkela/bus.zip](rourkela/bus.zip) (0.5 MB), mirror <https://maps.reclaim.city/gtfs/rourkela.zip> |
| Modes | bus |
| Agencies | CRUT |
| Routes / stops / trips | 160 / 1,081 / 1,042 |
| Trips with a shape | 966 (113 shapes) |
| Service | 2026-11-02 to 2027-11-02 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Map | <https://maps.reclaim.city/rourkela/> |
| Source | [Chalo's public scheduler (production.zophop.com), every route and stop, trips from 48 half-hourly sweeps of one Monday (Nov 2026), built into GTFS by reclaim.city](https://chalo.com/) |
| Licence | none stated by the source |
| sha256 | `d6655d310656a26f13db28dee91b3740387c341a322efc9dbe565475dc7a450a` |

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- shapes.txt left out (header only, no rows)
- shapes for 966 of 1042 trips that had none: the map's road-snapped line for the route (142 shapes)
- route lines thinned to within 4 m (scripts/simplify_shapes.py): 22,508 -> 15,043 shape points

## OSRTC (Odisha, statewide)

| | |
|---|---|
| Feed id | `osrtc` |
| Download | <https://maps.reclaim.city/osrtc/rt/gtfs.zip> |
| Modes | bus |
| Map | <https://maps.reclaim.city/osrtc/> |
| Source | [OSRTC Track a Bus, as seen by the reclaim.city live poller](https://osrtc.org/) |
| Licence | none stated by the source |
| GTFS-Realtime | [VehiclePositions](https://maps.reclaim.city/osrtc/rt/vehicle_positions.pb), [TripUpdates](https://maps.reclaim.city/osrtc/rt/trip_updates.pb), [status](https://maps.reclaim.city/osrtc/rt/status.json) |

> Built live, rebuilt hourly from the services the tracker has shown (OSRTC publishes no GTFS); stop order exact, times indicative.
