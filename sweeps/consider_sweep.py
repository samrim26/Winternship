"""Sweep Consider-powered VC job boards: GET page for csrf+cookie, then page through /api-boards/search-jobs, filter titles locally."""
import http.cookiejar, json, os, re, ssl, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem" if os.path.exists("/etc/ssl/cert.pem") else None)
BOARDS = {"jobs.sequoiacap.com": "sequoia-capital", "jobs.kleinerperkins.com": "kleiner-perkins", "jobs.lsvp.com": "lightspeed",
          "jobs.bvp.com": "bessemer-ventures", "jobs.felicis.com": "felicis", "jobs.forerunnerventures.com": "forerunner-ventures",
          "jobs.usv.com": "union-square-ventures", "jobs.battery.com": "battery-ventures", "jobs.baincapitalventures.com": "bain-ventures",
          "jobs.gv.com": "gv", "jobs.firstround.com": "first-round-capital", "jobs.crv.com": "crv", "jobs.costanoa.vc": "costanoa-ventures"}
INT = re.compile(r"\bintern(ship)?s?\b|co-?op\b|spring 2027|winter 2027|apprentice|student|part.?time|fellow", re.I)
ENG = re.compile(r"engineer|software|developer|scientist|design|machine learning|\bml\b|hardware|mechanical|electrical|firmware|security|devops|ios|android|phd|mba|legal|counsel|nurse|clinical|robot|propulsion|manufactur|technician|law", re.I)
LOC = re.compile(r"new york|nyc|brooklyn|manhattan|austin|remote|united states|san francisco|bay area|palo alto|oakland|berkeley|mountain view|menlo|redwood|san mateo|san carlos|south san|tokyo|japan|australia|sydney|melbourne|madrid|barcelona", re.I)

def sweep(item):
    host, board = item
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()), urllib.request.HTTPSHandler(context=ctx))
    op.addheaders = [("User-Agent", "Mozilla/5.0")]
    try:
        tok = re.search(r'"csrfToken":"([^"]+)', op.open(f"https://{host}/jobs", timeout=30).read().decode("utf-8", "ignore")).group(1)
    except Exception as e:
        return host, [], f"ERR {e}"
    out, seq, n = [], None, 0
    for _ in range(150):  # ponytail: 15k-job cap per board
        meta = {"size": 100}
        if seq: meta["sequence"] = seq
        req = urllib.request.Request(f"https://{host}/api-boards/search-jobs", method="POST",
              data=json.dumps({"meta": meta, "board": {"id": board, "isParent": True}, "query": {}}).encode(),
              headers={"Content-Type": "application/json", "x-csrf-token": tok})
        try: d = json.loads(op.open(req, timeout=30).read())
        except Exception as e: return host, out, f"{n} then ERR {e}"
        jobs = d.get("jobs", []); n += len(jobs)
        for j in jobs:
            locs = " / ".join(j.get("locations") or []) + (" remote" if j.get("remote") else "")
            if INT.search(j["title"]) and not ENG.search(j["title"]) and (LOC.search(locs) or not locs.strip()):
                out.append((board, j["companyName"], j["title"], locs[:50], (j.get("timeStamp") or "")[:10], j["url"]))
        seq = (d.get("meta") or {}).get("sequence")
        if not jobs or not seq: break
    return host, out, f"{n}/{d.get('total')}"

seen = set()
with ThreadPoolExecutor(4) as ex:
    for host, rows, stat in ex.map(sweep, BOARDS.items()):
        print(f"# {host} {stat} -> {len(rows)}", file=sys.stderr)
        for r in rows:
            k = (r[1].lower(), r[2].lower())
            if k not in seen: seen.add(k); print("\t".join(r))
