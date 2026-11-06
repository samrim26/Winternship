import json, re, ssl, urllib.request, sys
from concurrent.futures import ThreadPoolExecutor
ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
NETS = {45303:"FirstMark",257:"Khosla",103:"Lux",340:"Craft",318:"M13",247:"Uncork"}
QUERIES = ["intern", "internship", "part-time", "spring 2027", "winter 2027", "co-op", "fellow", "student"]
ENG = re.compile(r"engineer|software|developer|scientist|design|machine learning|\bml\b|hardware|mechanical|electrical|firmware|security|devops|ios|android|phd|mba|legal|counsel|nurse|clinical|research scientist", re.I)
INT = re.compile(r"intern|co-?op|fellow|student|part.?time|apprentice", re.I)
LOC = re.compile(r"new york|nyc|brooklyn|manhattan|austin|remote|united states|^us$|usa|jersey city", re.I)

def search(net, q, page=0):
    body = json.dumps({"hitsPerPage": 100, "page": page, "query": q, "filters": {}}).encode()
    req = urllib.request.Request(f"https://api.getro.com/api/v2/collections/{net}/search/jobs", data=body,
                                 headers={"Content-Type": "application/json", "Accept": "application/json", "User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            return json.loads(r.read())["results"]["jobs"]
    except Exception:
        return []

def run(args):
    net, q = args
    out = []
    for j in search(net, q):
        t = j.get("title", "")
        locs = " / ".join(j.get("searchable_locations") or [])
        org = (j.get("organization") or {}).get("name", "")
        if INT.search(t) and not ENG.search(t) and (LOC.search(locs) or not locs):
            out.append((NETS[net], org, t, locs[:60], j.get("work_mode") or "", j.get("url", ""), j.get("created_at") or 0))
    return out

seen, rows = set(), []
with ThreadPoolExecutor(16) as ex:
    for res in ex.map(run, [(n, q) for n in NETS for q in QUERIES]):
        for r in res:
            k = (r[1].lower(), r[2].lower())
            if k not in seen:
                seen.add(k); rows.append(r)
rows.sort(key=lambda r: -r[6])
for r in rows:
    print("\t".join(map(str, r[:6])))
print(f"# {len(rows)} unique non-eng intern/part-time roles", file=sys.stderr)
