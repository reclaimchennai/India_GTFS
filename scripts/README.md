# scripts

Helpers for shrinking GTFS zips. Pure Python 3 standard library, no installs.

Run with `-I` and pass paths as arguments. Write output to a new file, never over the input.

## simplify_shapes.py

Simplifies `shapes.txt` inside a GTFS zip (Douglas-Peucker) and writes a new zip. Other files are copied unchanged, except `trips.txt`, which is rewritten when duplicate shapes are merged.

```
python3 -I scripts/simplify_shapes.py IN.zip OUT.zip [--tol METRES] [--turn-deg DEG] [--no-stops] [--drop-dist]
```

| Option | Default | Meaning |
|---|---|---|
| `--tol` | 4 | Max distance (m) a removed point may be from the simplified line |
| `--turn-deg` | 0 (off) | Also keep vertices where the heading changes by more than this many degrees. 30 is a good value |
| `--no-stops` | off | Don't force-keep the vertex nearest each stop |
| `--drop-dist` | off | Drop the `shape_dist_traveled` column from `shapes.txt` |

What it does:

- Keeps the first and last point of every shape.
- Keeps the vertex nearest each stop, using the stops of one trip per shape, matched in order along the line.
- Keeps the original `shape_dist_traveled` values on the points it retains. They aren't recomputed.
- Merges shapes whose simplified geometry is identical, and points `trips.txt` at one `shape_id` for each.

Used for `karnataka/bengaluru/bus.zip`: `--tol 4 --turn-deg 30`. The zip went from 93.5 MB to 59.5 MB and the points from 4.27M to 1.63M.

## measure_deviation.py

Compares a simplified zip with the original.

```
python3 -I scripts/measure_deviation.py ORIG.zip SIMPLIFIED.zip [--sample N]
```

Reports, in metres:

- **Line deviation:** the distance from every removed point to the simplified line (max, mean, p99, p99.9).
- **Stop offset:** the distance from stops to the original line and to the simplified line, for a random sample of N shapes (default 400).

It assumes the simplified shapes are a subset of the original points, which is true for output from `simplify_shapes.py`.

## Results on Bengaluru BMTC (all with `--turn-deg 30`)

| Tol | Points kept | Zip | Max deviation | Mean deviation |
|---|---|---|---|---|
| 2 | 54% | 67.9 MB | 2 m | 0.83 m |
| 4 | 38% | 59.5 MB | 4 m | 1.58 m |
| 8 | 28% | 53.9 MB | 8 m | 2.72 m |

The remaining size is mostly `stop_times.txt` and `fare_rules.txt`. Neither can be reduced without changing what the feed means.
