#!/usr/bin/env bash
# The canonical check: MobilityData's GTFS Schedule validator (https://github.com/MobilityData/gtfs-validator) on
# every feed, one report per feed in build/validation/<path>/ (report.html, report.json), and a summary of notices
# by severity in build/validation/summary.txt. Needs Java 17+. Downloads the validator jar once, into build/.
set -euo pipefail
cd "$(dirname "$0")/.."
V=8.0.1; JAR=build/gtfs-validator-$V-cli.jar
mkdir -p build/validation
[ -f $JAR ] || curl -sSL -o $JAR https://github.com/MobilityData/gtfs-validator/releases/download/v$V/gtfs-validator-$V-cli.jar
: > build/validation/summary.txt
for z in $(find . -path ./build -prune -o -name '*.zip' -print | sort); do
  o=build/validation/${z#./}; o=${o%.zip}; mkdir -p "$o"
  java -Xmx4g -jar $JAR -i "$z" -o "$o" -c in >/dev/null 2>"$o/stderr.txt" || true
  python3 - "$z" "$o/report.json" >> build/validation/summary.txt <<'PY'
import json, sys, collections
try:
    r = json.load(open(sys.argv[2]))
except Exception as e:
    print(f'{sys.argv[1]:50s} NO REPORT ({e})'); sys.exit()
c = collections.Counter(); codes = collections.Counter()
for n in r.get('notices', []):
    c[n['severity']] += n.get('totalNotices', 1)
    if n['severity'] == 'ERROR': codes[n['code']] += n.get('totalNotices', 1)
print(f'{sys.argv[1]:50s} errors {c["ERROR"]:6d}  warnings {c["WARNING"]:7d}  info {c["INFO"]:6d}  ' + ', '.join(f'{k} x{v}' for k, v in codes.most_common(4)))
PY
done
cat build/validation/summary.txt
