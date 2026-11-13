#!/usr/bin/env bash
# Rebuild every feed in this repository from its sources, then the catalog, the READMEs and the checks.
#   tools/build.sh                 everything
#   tools/build.sh --only mumbai   one or more feed ids (comma-separated)
# Sources are read from SOURCES (default ~/Desktop/projects: the project checkouts named in tools/gtfs_publish.py and
# tools/feeds_extra.json), the maps from MAPS_SITE (default ~/Desktop/projects/maps-site), the India Metro app from
# METRO2 (default ~/Desktop/projects/metro2.0).
set -euo pipefail
cd "$(dirname "$0")/.."
METRO2=${METRO2:-$HOME/Desktop/projects/metro2.0}
for c in mumbai delhi; do python3 tools/suburban_gtfs.py $c "$METRO2" build/suburban/$c; done
python3 tools/gtfs_publish.py . "$@"
python3 tools/readme.py
find . -path ./build -prune -o -name '*.zip' -print | sort | xargs python3 tools/check.py
