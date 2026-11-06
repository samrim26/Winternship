import json, re, ssl, sys, html, urllib.request
ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
def get(u):
    return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=30, context=ctx).read())
def text(h): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(html.unescape(h or ""))))
PAT = re.compile(r"[^.]*(?:january|february|march|april|may|june|spring|winter|semester|weeks|months|start date|duration|hours per week|part[- ]time|full[- ]time|\$\s?\d|per hour|/hr|enrolled|graduat|class of|year|sql|python|technical|experience)[^.]*\.", re.I)
def show(title, body):
    print("==", title); t = text(body)
    for s in PAT.findall(t)[:10]: print("  -", s.strip()[:220])
kind, tok, ids = sys.argv[1], sys.argv[2], sys.argv[3:]
if kind == "gh":
    for i in ids:
        try: j = get(f"https://boards-api.greenhouse.io/v1/boards/{tok}/jobs/{i}"); show(j["title"], j["content"])
        except Exception as e: print("== GONE", i, e)
elif kind == "ashby":
    jobs = {j["id"]: j for j in get(f"https://api.ashbyhq.com/posting-api/job-board/{tok}?includeCompensation=true")["jobs"]}
    for i in ids: j = jobs.get(i); j and show(j["title"] + " | " + str((j.get("compensation") or {}).get("compensationTierSummary")), j["descriptionHtml"]) or (not j and print("== MISSING", i))
elif kind == "lever":
    for i in ids: j = get(f"https://api.lever.co/v0/postings/{tok}/{i}"); show(j["text"], j.get("description","") + " ".join(l["content"] for l in j.get("lists", [])) + j.get("additional",""))
