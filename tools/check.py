"""Structural checks against the GTFS Schedule reference (required files and fields, references, times): a quick
first pass, not a replacement for the MobilityData validator (tools/validate.sh).
    tools/check.py FEED.zip ...
"""
import csv,io,zipfile,sys,os,re,collections
REQ={'agency.txt':['agency_name','agency_url','agency_timezone'],'stops.txt':['stop_id'],'routes.txt':['route_id','route_type'],
     'trips.txt':['route_id','service_id','trip_id'],'stop_times.txt':['trip_id','stop_id','stop_sequence']}
T=re.compile(r'^\d{1,3}:[0-5]\d:[0-5]\d$')
for zp in sorted(sys.argv[1:]):
    z=zipfile.ZipFile(zp); f=os.path.relpath(zp)[:-4]; E=collections.Counter()
    names=set(z.namelist())
    rd=lambda n: list(csv.DictReader(io.TextIOWrapper(z.open(n),encoding='utf-8-sig'))) if n in names else []
    for n,cols in REQ.items():
        if n not in names: E['missing '+n]+=1; continue
        hdr=next(csv.reader(io.TextIOWrapper(z.open(n),encoding='utf-8-sig')))
        for c in cols:
            if c not in hdr: E[f'{n} lacks {c}']+=1
    if 'calendar.txt' not in names and 'calendar_dates.txt' not in names: E['no calendar.txt or calendar_dates.txt']+=1
    ag=rd('agency.txt'); st=rd('stops.txt'); ro=rd('routes.txt'); tr=rd('trips.txt')
    if len(ag)>1 and any(not a.get('agency_id') for a in ag): E['agency_id missing with several agencies']+=1
    tz={a.get('agency_timezone') for a in ag}
    if len(tz)>1: E['agencies in different timezones']+=1
    sid={s['stop_id'] for s in st}; rid={r['route_id'] for r in ro}
    svc={r['service_id'] for r in rd('calendar.txt')}|{r['service_id'] for r in rd('calendar_dates.txt')}
    for s in st:
        lt=s.get('location_type') or '0'
        if lt in ('0','1','2'):
            try:
                la,lo=float(s['stop_lat']),float(s['stop_lon'])
                if not (-90<=la<=90 and -180<=lo<=180) or (la==0 and lo==0): E['stop lat/lon invalid']+=1
            except: E['stop lat/lon missing']+=1
        if not s.get('stop_name') and lt in ('0','1','2'): E['stop_name missing']+=1
    for r in ro:
        if not (r.get('route_short_name') or r.get('route_long_name')): E['route has no name']+=1
        if r.get('agency_id') and len(ag)>1 and r['agency_id'] not in {a.get('agency_id') for a in ag}: E['route agency_id unknown']+=1
        if len(ag)>1 and not r.get('agency_id'): E['route agency_id missing (several agencies)']+=1
    tid=set()
    for t in tr:
        if t['route_id'] not in rid: E['trip route_id unknown']+=1
        if t['service_id'] not in svc: E['trip service_id unknown']+=1
        if t['trip_id'] in tid: E['duplicate trip_id']+=1
        tid.add(t['trip_id'])
    by=collections.defaultdict(list)
    for r in csv.DictReader(io.TextIOWrapper(z.open('stop_times.txt'),encoding='utf-8-sig')):
        if r['stop_id'] not in sid: E['stop_times stop_id unknown']+=1
        if r['trip_id'] not in tid: E['stop_times trip_id unknown']+=1
        a=r.get('arrival_time') or ''; d=r.get('departure_time') or ''
        for x in (a,d):
            if x and not T.match(x.strip()): E['bad time format']+=1
        by[r['trip_id']].append((int(r['stop_sequence']),a.strip(),d.strip()))
    def sec(x): h,m,s=x.split(':'); return int(h)*3600+int(m)*60+int(s)
    for t,l in by.items():
        l.sort()
        if len({q for q,_,_ in l})<len(l): E['duplicate stop_sequence in trip']+=1
        if len(l)<2: E['trip with <2 stops']+=1
        if not (l[0][1] or l[0][2]) or not (l[-1][1] or l[-1][2]): E['first/last stop without time']+=1
        prev=-1
        for q,a,d in l:
            for x in (a,d):
                if x and T.match(x):
                    v=sec(x)
                    if v<prev: E['times go backwards in trip']+=1; break
                    prev=v
    E['trips without stop_times']+=len(tid-set(by)) if len(tid-set(by)) else 0
    if E['trips without stop_times']==0: del E['trips without stop_times']
    print(f'{f:45s}', 'OK' if not E else '; '.join(f'{k} x{v}' for k,v in E.most_common()))
