"""Sweep jobs.a16z.com internships. Data embedded in Next.js HTML; 25 results/query, so fan out over title keywords."""
import json, os, re, ssl, sys, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor
ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem" if os.path.exists("/etc/ssl/cert.pem") else None)
KW = """marketing operations business strategy sales growth finance analyst data commercial partnerships community content
social brand events people recruiting talent customer success account product research policy communications investment
venture spring winter january co-op music media creator revenue supply logistics estate accounting fp&a bizops gtm analytics
economics ambassador fellow part-time associate development program project coordinator assistant intern internship
austin new york nyc remote tokyo sydney madrid barcelona san francisco""".split()
ENG = re.compile(r"engineer|software|developer|scientist|design|machine learning|\bml\b|hardware|mechanical|electrical|firmware|security|devops|ios|android|phd|mba|legal|counsel|nurse|clinical|robot|structures|propulsion|avionics|manufactur|technician|gnc|fpga|thermal|naval|rf\b|antenna", re.I)
LOC = re.compile(r"new york|nyc|brooklyn|manhattan|austin|remote|united states|san francisco|bay area|palo alto|oakland|berkeley|mountain view|menlo|redwood|san mateo|san carlos|south san|tokyo|japan|australia|sydney|melbourne|madrid|barcelona", re.I)

def query(q):
    url = "https://jobs.a16z.com/jobs?internships=1&q=" + urllib.parse.quote(q)
    s = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30, context=ctx).read().decode("utf-8", "ignore").replace('\\"', '"')
    tot = re.search(r'"total":(\d+)', s)
    return q, int(tot.group(1)) if tot else 0, [json.loads(m) for m in re.findall(r'(\{"id":"ats:.*?"company_band":(?:"[^"]*"|null)\})', s)]

jobs = {}
with ThreadPoolExecutor(8) as ex:
    for q, tot, js in ex.map(query, KW):
        if tot > len(js): print(f"# truncated: {q} {len(js)}/{tot}", file=sys.stderr)
        for j in js: jobs[j["id"]] = j
print(f"# {len(jobs)} unique internships", file=sys.stderr)
for j in sorted(jobs.values(), key=lambda j: j.get("posted_at") or "", reverse=True):
    locs = " / ".join(j.get("locations") or []) + (" remote" if j.get("remote") else "")
    if ENG.search(j["title"]) or not (LOC.search(locs) or not locs.strip()):
        continue
    print("\t".join([j["company_name"], j["title"], locs[:50], (j.get("posted_at") or "")[:10], j["apply_url"]]))
