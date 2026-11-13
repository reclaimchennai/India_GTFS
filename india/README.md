# India

Feeds in this folder: 1. Back to the [repository README](../README.md).

## Indian Railways (all-India trains, incl. EMU/MEMU)

| | |
|---|---|
| Feed id | `indian-railways` |
| Download | [indian-railways.zip](indian-railways.zip) (3.7 MB), mirror <https://maps.reclaim.city/gtfs/indian-railways.zip> |
| Modes | rail |
| Agencies | Indian Railways |
| Routes / stops / trips | 10,389 / 8,550 / 10,389 |
| Trips with a shape | 10,389 (10,389 shapes) |
| Service | 2025-01-01 to 2099-12-31 |
| Files | `agency.txt`, `calendar.txt`, `feed_info.txt`, `routes.txt`, `shapes.txt`, `stop_times.txt`, `stops.txt`, `trips.txt` |
| Source | [Community GTFS of Indian Railways by P. Radha Krishna (github.com/Neo2308)](https://github.com/Neo2308) |
| Licence | none stated by the source |
| sha256 | `495b23034426edb985c2bab73343ef44c1af68df2a4e3f0f6868d8ef1daf00c6` |

> One trip per train number; covers long-distance and some EMU/MEMU, not the Mumbai or Chennai local timetables.

Changes from the source (see [what we change](../README.md#what-we-change-and-why)):

- packaging: files at the zip root, GTFS reference files only
- 205 trips with a service_id in no calendar (they never run) left out
- 205 shapes no trip uses left out
