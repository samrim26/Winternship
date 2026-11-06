import json, re, ssl, sys, urllib.request
ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
F = json.load(open("wd_found.json"))
LOC = re.compile(r"new york|nyc|brooklyn|manhattan|austin|remote|san francisco|burbank|santa monica|los angeles|bay area|palo alto|tokyo|sydney|madrid|barcelona|locations", re.I)
TECH = re.compile(r"engineer|software|developer|scientist|machine learning|hardware|security|devops|cyber|cloud|infrastructure|phd|mba|legal|law|counsel", re.I)
def post(t, s, wd, body):
    u = f"https://{t}.{wd}.myworkdayjobs.com/wday/cxs/{t}/{s}/jobs"
    r = urllib.request.urlopen(urllib.request.Request(u, data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "Accept": "application/json", "User-Agent": "Mozilla/5.0"}), timeout=20, context=ctx)
    return json.loads(r.read())
for t, (t_, s, wd) in F.items():
    allj, off = [], 0
    for q in ("intern", "internship", "spring", "co-op"):
        off = 0
        while off < 400:
            try: d = post(t, s, wd, {"limit": 20, "offset": off, "searchText": q, "appliedFacets": {}})
            except Exception as e: break
            js = d.get("jobPostings", []); allj += js; off += 20
            if len(js) < 20: break
    seen = {}
    for j in allj: seen[j.get("externalPath")] = j
    for p, j in seen.items():
        ti, lo = j["title"], j.get("locationsText", "")
        if re.search(r"intern|co-?op", ti, re.I) and not TECH.search(ti) and LOC.search(lo) and not re.search(r"summer|fall", ti, re.I):
            print(f"{t}\t{ti}\t{lo}\t{j.get('postedOn','')}\thttps://{t}.{wd}.myworkdayjobs.com/{s}{p}")
