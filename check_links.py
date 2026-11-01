#!/usr/bin/env python3
"""Liveness pass over every open List 1 (posted) row in dashboard.html.

Prints one line per row: REF  VERDICT  reason  url
  DEAD    — strong closed signal (404/410, ATS API says gone/canApply false, "no longer accepting")
  SUSPECT — weak signal (redirected away from the job, deadline in note has passed)
  OK      — page/API answered and showed no closed signal
  UNKNOWN — couldn't tell (blocked, JS shell, timeout)

The sweep agent confirms every DEAD/SUSPECT by hand before marking a row closed.
Run: python3 check_links.py            (stdlib only)
"""
import html, json, re, sys, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
from datetime import date

OPEN = {"live", "unverified", "conflict", "applied", "drafting", "interviewing", "monitor"}
DEAD_PHRASES = re.compile(
    r"no longer accepting|no longer available|position has been filled|job (?:is|has been) closed"
    r"|this job (?:has )?expired|posting (?:has )?(?:closed|expired)"
    r"|isn&#39;t available|is no longer open|applications (?:are )?closed", re.I)
# Many SPAs (interninsider, Next.js) ship "Page not found" in every page's boilerplate, so
# not-found wording only counts when it is the page <title>.
DEAD_TITLE = re.compile(r"<title>[^<]*(?:not found|404|closed:|expired|no longer)[^<]*</title>", re.I)
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 Safari/605.1.15"}
MONTHS = {m: i for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}


def get(url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, headers={**UA, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status, r.geturl(), r.read(4_000_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, url, ""
    except Exception as e:
        return 0, url, str(e)


def ats(url):
    """Ask the ATS's public API directly where one exists. Returns (verdict, reason) or None."""
    if m := re.search(r"jobs\.lever\.co/([^/]+)/([0-9a-f-]{36})", url):
        s, _, _ = get(f"https://api.lever.co/v0/postings/{m[1]}/{m[2]}")
        return ("DEAD", "lever api 404") if s == 404 else ("OK", "lever api 200") if s == 200 else None
    if m := (re.search(r"greenhouse\.io/([^/]+)/jobs/(\d+)", url)
             or re.search(r"greenhouse\.io/embed/job_app\?for=([^&]+).*?gh_jid=(\d+)", url)):
        s, _, _ = get(f"https://boards-api.greenhouse.io/v1/boards/{m[1]}/jobs/{m[2]}")
        return ("DEAD", "greenhouse api 404") if s == 404 else ("OK", "greenhouse api 200") if s == 200 else None
    if m := re.search(r"jobs\.ashbyhq\.com/([^/]+)/([0-9a-f-]{36})", url):
        s, _, body = get(f"https://api.ashbyhq.com/posting-api/job-board/{m[1]}")
        if s == 200:
            return ("OK", "ashby board lists id") if m[2] in body else ("DEAD", "ashby board no longer lists id")
    if m := re.search(r"https://([^/]+\.myworkdayjobs\.com)/(?:[a-z]{2}-[A-Z]{2}/)?([^/]+)(/job/.+)", url):
        host, site, path = m[1], m[2], m[3]
        s, _, body = get(f"https://{host}/wday/cxs/{host.split('.')[0]}/{site}{path}",
                         headers={"Accept": "application/json"})
        if s == 404:
            return "DEAD", "workday cxs 404"
        if s == 200:
            try:
                ok = json.loads(body)["jobPostingInfo"].get("canApply")
                return ("OK", "workday canApply") if ok else ("DEAD", "workday canApply false")
            except Exception:
                pass
    return None


def passed_deadline(note):
    """Latest 'Deadline <Mon> <d> <yyyy>' / 'closes <Mon> <d> <yyyy>' in the note, if it is in the past."""
    hits = re.findall(r"(?:deadline|closes|closing)[^.]{0,20}?\b([A-Z][a-z]{2})[a-z]*\.? (\d{1,2}),? (20\d\d)", note, re.I)
    ds = [date(int(y), MONTHS[mo.lower()], int(d)) for mo, d, y in hits if mo.lower() in MONTHS]
    return max(ds) if ds and max(ds) < date.today() else None


def check(row):
    ref, url, note = row[0], html.unescape(row[16]), row[17]
    verdict = ats(url)
    if not verdict:
        s, final, body = get(url)
        if s in (404, 410):
            verdict = ("DEAD", f"http {s}")
        elif s == 200 and (m := DEAD_TITLE.search(body) or DEAD_PHRASES.search(body)):
            verdict = ("DEAD", f"page says '{m[0][:80]}'")
        elif s == 200 and re.search(r"\d{4,}", url) and not any(t in final for t in re.findall(r"\d{4,}", url)):
            verdict = ("SUSPECT", f"redirected off the job to {final[:80]}")
        elif s == 200:
            verdict = ("OK", "http 200")
        else:
            verdict = ("UNKNOWN", f"http {s or 'error'}")
    if verdict[0] in ("OK", "UNKNOWN") and (d := passed_deadline(note)):
        verdict = ("SUSPECT", f"{verdict[1]}; note deadline {d} has passed")
    return ref, *verdict, url


def rows():
    src = open("dashboard.html", encoding="utf-8").read()
    raw = re.search(r"const RAW = \[(.*?)\n\];", src, re.S)[1]
    out = []
    for line in raw.splitlines():
        line = line.strip().rstrip(",")
        if line.startswith('["'):
            r = json.loads(line)
            if r[1] == "P" and r[15] in OPEN:  # List 1 only; List 2 (E) has no posting to check
                out.append(r)
    return out


if __name__ == "__main__":
    assert passed_deadline("Deadline Oct 12 2026.") == date(2026, 10, 12) or date.today() <= date(2026, 10, 12)
    assert passed_deadline("Deadline Dec 1 2099") is None
    with ThreadPoolExecutor(12) as ex:
        res = sorted(ex.map(check, rows()), key=lambda r: ("DEAD", "SUSPECT", "UNKNOWN", "OK").index(r[1]))
    for r in res:
        print("\t".join(r))
    print(f"# {len(res)} checked: " + ", ".join(f"{v} {sum(r[1] == v for r in res)}"
          for v in ("DEAD", "SUSPECT", "UNKNOWN", "OK")), file=sys.stderr)
