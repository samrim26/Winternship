# Job Tracker — Off-Cycle Spring 2027

> Source of truth for `dashboard.html`. Edit the `Status` column by hand as you apply.
>
> **Reference numbers:** the `RAW` array in `dashboard.html` is authoritative. Tier C numbering in
> this file diverged from it during the 2026-08-02 rebuild, so when allocating a ref for a new role,
> continue from the highest ref in that array — not from this file.
>
> **Sweep 2026-10-30 (full, 13:45 UTC): 1 new row (A182, live), 2 closures.** `check_links.py` — 0
> `DEAD`, 1 `SUSPECT`, 7 `UNKNOWN`, 84 `OK`. **A95** (Parkdepot) re-flagged `SUSPECT` on the same
> standing passed-deadline signal; re-opened directly — unchanged, still "Actively hiring." 7 standing
> `UNKNOWN` Tesla 403s (A68, A122, A124–A126, A139, A172) re-tried via WebFetch, still 403 — no change.
> FULL-run substance re-check (13 live Tier A/B rows not recently sampled: A82, A83, A93, A96, A120,
> A129, A131, A132, A133, A151, A157, A158, A171) surfaced two closures the checker missed (same
> false-negative-`OK` pattern as A153 on 2026-10-29): **A131** (Base Power Company, Financial Planning
> Intern, Austin) — direct fetch shows "Sorry, this job was removed at 11:42 a.m. (CST) on Monday, Oct
> 26, 2026." Was `live`. **A132** (Base Power Company, Marketing Intern, Austin) — direct fetch shows
> "Sorry, this job was removed at 05:38 p.m. (CST) on Friday, Oct 23, 2026." Was `live`. Base Power's
> two remaining open reqs in this cluster (A129 Finance–Analytics, A133 Deployments Operations) still
> show "Be an Early Applicant," no removal notice — unchanged. The other 9 sampled rows (A82, A83, A93,
> A96, A120, A151, A157, A158, A171) matched the tracker on dates/location/mode/pay where stated — no
> corrections. One git-state note (not a jobs.md issue): local `main` had fallen 9 commits behind a
> detached-HEAD checkout from prior runs (Oct 26–29 work was present but the branch pointer hadn't
> moved); fast-forwarded `main` to catch up — no data was lost, origin already had the commits.
> Board sweep: added **A182** (PatientPoint, Client Sales Intern, New York NY, Hybrid, $20–23/hr,
> Sales) via a direct Built In NYC company-page scan — same company as A181 (BD Intern), same mode
> ambiguity (listing header "In-Office" vs. body text "Hybrid Schedule"), three near-identical listing
> IDs tracked as one row. workatastartup.com and wellfound.com root/jobs pages again returned no
> browsable listings to a direct fetch (JS-rendered; W2027 YC batch still not landed — standing issue).
> Economic consulting direct (analysisgroup.com, cornerstone.com, crai.com, compasslexecon.com,
> brattle.com) checked again — none of the five careers pages lists specific internship openings or
> dates on the page itself (all point to Analyst/Associate summer-cycle application funnels or a
> Workday portal); no off-cycle req surfaced. DoorDash careers page returned 403 to direct fetch;
> Flexport's lists no internships at all, only full-time strategy/ops and rotational roles. tokyodev.com
> 403 (standing); coralcap.co/jobs 404 (link form changed — flagging for a future check at a corrected
> URL); japan-dev.com surfaced only HENNGE's "Full-Stack Pathway" internship (engineering, out of
> scope). SimplifyJobs Off-Season README (raw, Winter-2027 and Spring-2027 term pages via
> interninsider.me) and Built In Austin/SF — nothing in target functions/cities cleared the bar; IDeaS
> "Marketing Analytics Intern" resurfaced under both Austin and SF Bay Area searches (remote/hybrid,
> no real target-city presence) — excluded again as the same already-tracked-exclusion class. Built In
> NYC also surfaced Tapestry MBA-level Strategy/E-Commerce intern postings — excluded, MBA-level, not
> a junior-undergrad fit. au.gradconnection.com Sydney — TikTok rows already tracked (A112/A114),
> confirmed current, both closing within hours of this check per the page. Nothing else cleared the
> bar for addition this run.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> **Liveness check 2026-10-29 22:00 UTC: closed A107 (Zipline), A177 (Snowflake).** `check_links.py`
> flagged both `DEAD`; confirmed directly via fetch — both pages now show title "Closed: …" and status
> text "This internship has closed" / "Applications closed on October 28, 2026." A107 was `conflict`,
> A177 was `live`. A95 (Parkdepot) re-flagged `SUSPECT` on the same standing passed-deadline signal;
> re-opened directly — still "Actively hiring," paid, rolling start, no change. 7 standing `UNKNOWN`
> Tesla 403s (A68, A122, A124–A126, A139, A172) unchanged. Access check: all five sanity-check domains
> reachable.
>
> **Sweep 2026-10-29 (full, 13:29 UTC): 0 new rows, 1 closure.** `check_links.py` — 0 `DEAD`,
> 1 `SUSPECT`, 7 `UNKNOWN`, 87 `OK`. Closed **A153** (Contoro Robotics, Business Development Intern,
> Austin) — checker returned `OK` (http 200, false negative), but a direct fetch of the posting now
> reads "Sorry, this job was removed at 06:52 p.m. (UTC) on Monday, Oct 19, 2026." Was `live`. **A95**
> (Parkdepot) re-flagged `SUSPECT` on the same standing passed-deadline signal; re-opened directly —
> unchanged, still "Actively hiring," paid, rolling start. 7 standing `UNKNOWN` Tesla 403s (A68, A122,
> A124–A126, A139, A172) re-tried via WebFetch, still 403 — no change. FULL-run substance re-check:
> sampled 7 `live` Tier A/B rows not sampled in recent runs (A70, A114, A128, A153, A161, A169, A181)
> by opening each posting directly — all matched the tracker (dates, location, mode, pay where
> stated) except A153 above; **A114** (TikTok AI PM Intern, Sydney) confirmed still open, closing
> **30 Oct 2026, 1:59pm Sydney time — inside 24 hours**, flagging for urgency. Board sweep: YC
> (workatastartup.com) and Wellfound root/search pages again returned no listings to a direct fetch
> (JS-rendered; Winter 2027 YC batch still not landed) — standing issue. Economic consulting direct
> (analysisgroup.com, brattle.com, crai.com, compasslexecon.com, cornerstone.com, nera.com) checked
> again — all still summer-cycle only (NERA's own FAQ explicitly limits its internship program to
> final-year undergrads and grad students — Sam doesn't qualify as a junior regardless of cycle).
> DoorDash and Flexport careers pages surfaced no 2027 internship postings. Built In NYC/Austin/SF
> surfaced two candidates that were investigated and excluded as **already-excluded repeats**: IDeaS
> "Marketing Analytics Intern" (Bloomington, MN HQ, no target-city corroboration — same exclusion as
> prior runs) and Emerson "Business Operations Intern" (Austin, hybrid, but no term stated and company
> runs fixed-season programs — same exclusion class as the already-tracked Emerson S&amp;OP intern
> exclusion). Citadel "Operations Analyst – Intern (US)" (NYC, $2,200–2,300/wk) investigated —
> Citadel's own careers pages return 403 to direct fetch; the only cached listing (Built In) shows the
> role removed Dec 17 2025 and the pay band/11-week structure match Citadel's standard **summer**
> analyst-intern program, not an off-cycle cohort — excluded on strong summer-cycle likelihood rather
> than added speculatively. Metis Strategy "Strategy &amp; Management Consultant Intern" surfaced again
> on a different source (Built In via Walnut Creek, CA search) — already tracked as **A180**;
> metisstrategy.com's own careers page lists no open roles directly (boutique firm, third-party-board
> only, consistent with using Simplify exclusively), but `check_links.py` confirms A180's actual
> Simplify.jobs listing still returns `OK` — no change. GradConnection Sydney — TikTok rows already tracked
> (A112/A114), confirmed current. Nothing else cleared the bar for addition this run.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> **Liveness check 2026-10-28 13:00 UTC:** closed **A18** (Datadog, Product Management Intern —
> Winter session) — checker returned `UNKNOWN` (HTTP 429, transient rate-limit), but a direct fetch
> showed "Sorry, this job was removed at 04:18 p.m. (EST) on Tuesday, Oct 27, 2026." Was `conflict`
> (dates ran past the hard stop anyway). `check_links.py` otherwise — 0 `DEAD`, 1 `SUSPECT`, 8
> `UNKNOWN`, 86 `OK`. **A95** (Parkdepot) re-flagged `SUSPECT` on the same standing passed-deadline signal;
> re-opened directly — still "Actively hiring," full-time, on-site SF, rolling start; page now
> explicitly states "Paid internship" — **Pay corrected Unconfirmed → Paid (amount unconfirmed)**
> in both files. 7 standing `UNKNOWN` Tesla 403s (A68, A122, A124–A126, A139, A172) re-tried, still
> 403 — no change. FULL-run substance re-check: sampled 15 other `live` Tier A/B rows (A5, A13, A22,
> A65, A75, A92, A96, A112, A120, A121, A130, A145, A151, A173, A177) by opening each posting directly
> — all matched the tracker exactly (dates, location, mode, hours, pay where stated); several
> workatastartup.com/YC listings only returned a bare title via fetch (JS-rendered, as usual) and
> could not be re-verified this way, consistent with prior runs. No corrections beyond A95's Pay
> field. Remaining live rows not sampled this run are due for a future pass.
>
> **Sweep 2026-10-28 (full, 13:13 UTC): 0 new rows.** Economic consulting direct (analysisgroup.com,
> cornerstone.com, crai.com, compasslexecon.com, brattle.com, nera.com) checked again — all still
> summer-analyst/associate-cycle only, no off-cycle reqs. Palantir Deployment Strategist (Lever)
> checked and excluded — role explicitly requires the application be "your final internship before
> graduating"; Sam graduates 2028, doesn't qualify. DoorDash and Flexport careers pages surfaced no
> 2027 internship postings, only full-time Strategy &amp; Ops reqs. SimplifyJobs Off-Season README
> (raw) partially re-read (~200K of ~1.5M chars) — nothing new in target functions/cities in the
> portion covered. Intern Insider winter-2027/spring-2027 term pages — no new matches. Built In
> Austin/SF — nothing with confirmed Jan–Mar 2027 dates in target functions (mostly Summer-2027
> cycle or wrong location). GradConnection Sydney — TikTok Client Solution Intern and AI PM Intern
> postings found, both already tracked as **A112**/**A114**, status and deadlines confirmed current.
> Energy and Environmental Economics (E3) 2027 Consulting Internship found again — already tracked,
> **twice**, as **A145** and **A164** — flagging this existing duplicate for cleanup on a future
> pass, not acted on here. coralcap.co and tokyodev.com — 403/404 this run (standing, no access
> change). workatastartup.com and wellfound.com root/search pages still return no listings to a
> direct fetch (JS-rendered; `site:` search operators aren't honored by the search engine for either
> domain) — standing issue, full YC sweep still pending the Winter 2027 batch landing in November.
> Nothing cleared the bar for addition this run.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> **Liveness check 2026-10-27 22:00 UTC:** closed **A167** (Dell Technologies, Corporate Strategy
> Undergraduate Intern) — checker returned `DEAD`, confirmed directly: page title now reads "Closed:
> Corporate Strategy Undergraduate Intern at Dell…", status text "This internship has closed" /
> "Applications closed on October 26, 2026." Was `unverified`. **A95** (Parkdepot) re-flagged
> `SUSPECT` on the same standing passed-deadline signal; re-opened directly — still "Actively hiring,"
> rolling start, no change. 6 standing `UNKNOWN` Tesla 403s (A68, A122, A124–A126, A139, A172)
> re-tried via WebFetch, still 403 — no change.
>
> **Sweep 2026-10-27 (full, 13:33 UTC):** Liveness check (`check_links.py`): 0 `DEAD`, 2 `SUSPECT`
> (A95 Parkdepot, A167 Dell — both re-opened directly via WebFetch, still "Actively hiring," no
> closed/filled signal, same standing rolling-deadline pattern as every prior run; dated lines added
> to both notes), 8 `UNKNOWN` (standing Tesla 403s — A68, A122, A124–A126, A139, A172 — plus A149/A155
> Built In NYC, which hit a transient HTTP 429 on this run's automated pass; both re-opened directly
> via WebFetch immediately after and returned 200 with no closed/filled signal — treated as rate-limit
> noise, not a real signal, no status change).
>
> **Board sweep: 1 new row.** Economic consulting direct (analysisgroup.com, cornerstone.com,
> crai.com, compasslexecon.com's own Workday board, brattle.com) checked again — all remain
> summer-analyst/associate-only, no internship or off-cycle reqs surfaced; NERA's careers URL now
> redirects to a dead marketing page (noted, not acted on — no application function lost since no
> internship req existed there anyway). workatastartup.com and wellfound.com still JS/login-gated to
> a direct fetch (standing, full YC sweep still pending the Winter 2027 batch landing in November).
> simplify.jobs' Top Winter/Spring list re-checked — still titled "Winter &amp; Spring 2026," only
> function match is Metis Strategy (already tracked, A180). SimplifyJobs Off-Season README
> (Software Engineering table, Product Management/Data Science sections not reachable in this pass
> due to file size) and Intern Insider winter-2027/spring-2027 term pages surfaced nothing new in
> target functions/cities. **Built In NYC direct company-page scan surfaced A181 (PatientPoint,
> Business Development Intern, NYC, unverified→live, $20–23/hr)** — see note on the row; mode is
> flagged as a possible onsite-that's-really-remote case. Built In Austin surfaced only
> already-excluded Summer-2027 rows (Cox PM intern, Emerson S&OP intern) and borderline non-matches
> (Four Hands, White Cap). GradConnection Sydney surfaced three new postings (ANZ 2027/28 Summer
> Intern EOI — Nov 2027 start, wrong cycle; Grant Thornton 2027/2028 Vacation Program EOI — wrong
> cycle, Australian summer not Jan–Mar; Premium Graduate Placements — no 2027 date stated) — all
> evaluated and excluded, not padded in. coralcap.co's portfolio board remains a warm-intro service
> with no browsable postings (standing); tokyodev.com 403 (standing).
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Last swept: **2026-10-30** (full sweep — **1 new row (A182, live), 2 closures (A131/A132 Base
> Power), 0 `DEAD` on the liveness pass (both closures found via substance re-check, not the
> checker)**.)
>
> Prior — Last swept: **2026-10-29** (full sweep — **0 new rows, 1 closure (A153 Contoro Robotics), 0 `DEAD`
> on the liveness pass (closure found via substance re-check, not the checker)**.)
>
> Prior — Last swept: **2026-10-28** (full sweep — **0 new rows, 1 closure (A18 Datadog), 0 `DEAD` on the
> liveness pass**.)
>
> Prior — Last swept: **2026-10-27** (full sweep — **1 new row (A181, live), 0 closures, 0 `DEAD` on the
> liveness pass**.)
>
> Prior — **Liveness check 2026-10-26 22:00 UTC:** `check_links.py` flagged 1 `DEAD` — **A178 (1Password)**,
> confirmed directly (1Password's own Ashby job-board API no longer lists job id 412c1aac...; direct
> posting URL now returns HTTP 404) — closed, was `conflict`. Also 2 `SUSPECT` (A95 Parkdepot, A167
> Dell — both re-opened directly, still "Actively hiring," same standing rolling-deadline pattern, no
> change) and 7 `UNKNOWN` (standing Tesla 403s — A68, A122, A124–A126, A139, A172; sampled A172 via
> WebFetch, still 403, unchanged). Access check: all five sanity-check domains reachable
> (workatastartup.com 301, wellfound.com 200, simplify.jobs 200, job-boards.greenhouse.io 302,
> www.builtinnyc.com 200) — no regression.
>
> **Sweep 2026-10-26 (full, 13:06 UTC):** Liveness check (`check_links.py`): 0 `DEAD`, 2 `SUSPECT`
> (A95 Parkdepot, A167 Dell — both re-verified directly, still "Actively hiring," same standing
> rolling-deadline pattern as every prior run, no change), 7 `UNKNOWN` (standing Tesla 403s — A68,
> A122, A124–A126, A139, A172, sampled A172 directly via WebFetch, still 403, unchanged). Substance
> re-checks: A5 (Dalus, workatastartup.com — title unchanged; board is login/JS-gated to a direct
> fetch, standing), A13 (DeepAware AI, workatastartup.com — same), A18 (Datadog, Built In NYC —
> unchanged: hybrid NYC, Jan 4–Apr 23 2027, $100–110K, still `conflict`). **A16 (Zipline)** — attempted
> re-verification on the Techstars/Getro portfolio board; the board is JS-rendered with no static job
> data, and Getro's own search API now blocks scraping requests outright ("contact us for API
> access"). Could not confirm the listing is still live — same class of access limitation as the
> Tesla 403s. Left status (`conflict`) unchanged rather than guessing.
>
> **Board sweep: 0 new rows.** Economic consulting (Analysis Group, Cornerstone, CRA, Compass
> Lexecon, Brattle, NERA) checked directly at source again — all remain summer-analyst-only / full-time-
> 2027-grad only (CRA's own board: 91 live postings, zero internships; confirmed directly). YC
> (workatastartup.com) and wellfound.com both JS/login-gated to a direct fetch this pass (standing,
> unchanged — full exhaustive YC sweep still pending the Winter 2027 batch landing in November per the
> playbook). simplify.jobs' Top Winter/Spring list unchanged — still titled "Winter &amp; Spring 2026,"
> only function match is Metis Strategy (already tracked as A180). SimplifyJobs Off-Season README
> re-parsed (Software Engineering + partial Data Science/PM sections): every Data/PM match in target
> cities was already tracked (Gemini A146/A176, Clearwater A148/A155) except **Emerson Electric**'s
> "Software Product Management Intern" (Austin, TX, Oracle Cloud ATS, aggregator-tagged "Winter 2026")
> — evaluated and excluded rather than added: the posting page is JS-rendered and gave no term, mode,
> or pay beyond the aggregator tag, and PM sits near the bottom of the function priority list, so an
> unverified add here didn't clear the quality bar. Intern Insider spring-2027 term page: no Data/
> Strategy/Growth/BD/Partnerships/PM/Sales match in target cities (closest hits — E3's consulting
> internship, Electric Power Engineers R&amp;D — are wrong function). Built In Austin/SF internship
> pages: every Data/Strategy/PM/Sales match found is tagged Summer 2027 — wrong cycle, excluded.
> GradConnection Sydney business/commerce: TikTok rows already tracked, nothing else new (Capgemini
> generalist program, wrong function). Tokyo (coralcap.co, japan-dev.com, tokyodev.com): coralcap.co's
> "Coral Careers" page no longer lists individual portfolio postings (site redesign — now a
> warm-intro service, not a browsable board); japan-dev.com showed one Tokyo internship (HENNGE Global
> Internship Program) but it's an engineering track, not a function match; tokyodev.com 403 (standing).
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Last swept: **2026-10-26** (full sweep — **0 new rows, 0 closures, 0 `DEAD` on the liveness pass**.)
>
> Prior — **Sweep 2026-10-25 (full, 13:00 UTC):** Liveness check (`check_links.py`): 0 `DEAD`, 2 `SUSPECT`
> (A95 Parkdepot, A167 Dell — both re-verified directly, titles unchanged, no closed/filled signal,
> same standing rolling-deadline pattern as prior runs), 7 `UNKNOWN` (standing Tesla 403s — A68, A122,
> A124–A126, A139, A172, sampled A172 directly, still 403, unchanged). Substance re-checks: A22 CertiK
> (Lever API — unchanged, still open, NY), A145 E3 (Lever API — unchanged, still open, SF), A151 Kroll
> (200 OK, unchanged), A161 &amp; A169 MTA (Jobvite — unchanged, titles match tracker). No closures,
> no corrections this run.
>
> **Board sweep: 1 new row.** Economic consulting firms (Analysis Group, Cornerstone, CRA, Compass
> Lexecon, Brattle, NERA) checked directly at source again — all remain summer-analyst-only, zero
> internship reqs (CRA's own 91-posting board confirmed full-time-2027-grad only). workatastartup.com
> still login/JS-gated to a direct fetch (standing, unchanged since yesterday); wellfound.com showed no
> internship postings this pass. SimplifyJobs Off-Season README re-parsed — no new Data/Strategy/
> Growth/BD/PM matches beyond what's already tracked. Intern Insider winter/spring-2027 term pages,
> Built In (Austin/NYC/SF) internships pages, and Tokyo sources (coralcap.co, japan-dev.com — one
> listing but engineering; tokyodev.com 403) all surfaced nothing new. GradConnection Sydney
> business/commerce: TikTok rows already tracked; everything else is Australian-citizenship-gated
> (Treasury), next-cycle (Summer 2027/28), or wrong function (Capgemini Melbourne, mechanical/CAD).
>
> **New: A180 (Metis Strategy)** — "Strategy & Management Consultant Intern," found via
> simplify.jobs' Top Winter/Spring Internships list. Boutique C-level/executive advisory consulting —
> genuine Strategy-function fit, closest thing on the board to the named economic-consulting lane
> outside the five named firms. Walnut Creek, CA (East Bay, adjacent to SF). Could not confirm term,
> dates, hours, or a company-ATS link — metisstrategy.com/careers is JS-rendered and didn't surface
> its own ATS posting; kept the Simplify aggregator link as the real application URL per the
> never-drop rule. **Genuine risk flag:** the aggregator list page itself is titled "Winter & Spring
> 2026," raising a real possibility this is a stale prior-cycle listing rather than 2027 — added
> `unverified` with that risk stated explicitly rather than assumed either way.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Last swept: **2026-10-25** (full sweep — **1 new row (A180, unverified), 0 closures, 0 `DEAD` on the
> liveness pass**.)
>
> Prior — **Sweep 2026-10-24 (full, 13:00 UTC):** Liveness check (`check_links.py`): 1 `DEAD` (**A144 Rundoo —
> closed**: Ashby's job-board API for `rundoo` no longer lists this posting id at all, confirmed
> directly against the live API response, which now shows a different, unrelated set of open roles;
> was `conflict`), 2 `SUSPECT` (A95 Parkdepot, A167 Dell — both re-opened directly, still "Actively
> hiring," no change, same standing rolling-deadline pattern as prior runs), 7 `UNKNOWN` (standing
> Tesla 403s — A68, A122, A124–A126, A139, A172, sampled one directly via WebFetch, still 403,
> unchanged). Substance re-checks: A96 (Crowe Global, Built In Austin — unchanged, still "Apply Now"),
> A120 (MTA, Jobvite — unchanged, 200 OK), A121 (Ankura, Workday CXS API — unchanged: canApply true,
> $34/hr), A130 (Kodiak, Greenhouse API — unchanged, updated_at 2026-10-20, still open), A143 (CBIZ,
> Oracle Cloud ATS — unchanged, 200 OK).
>
> **Board sweep: 0 new rows.** Economic consulting (Analysis Group, Cornerstone, CRA, Brattle, NERA)
> checked directly at source again — all remain summer-analyst-only, no winter/spring or rolling
> track; CRA's own board shows only full-time 2027-grad reqs, no internships. SimplifyJobs Off-Season
> README (Data Science + PM sections) parsed in full — every Winter/Spring 2027 + target-city match
> was already tracked or excluded on verification: Google's "Data Analytics Apprenticeship" (18-month
> DOL program, no-bachelor's-required, application window already closed — wrong shape entirely),
> Cloudflare's "People Analytics Data Engineer Intern" (Austin) confirmed gone via Cloudflare's own
> Greenhouse API — Simplify's entry was stale, and Stand Together's "KIP Policy Data Analyst Intern"
> (Lever API) turned out to be **Albany, NY**, not NYC as tagged — a location-tagging error — plus a
> mandatory June Arlington, VA summit past the Japan departure — conflict, excluded. workatastartup.com
> login-gated this pass (no public listing reachable); wellfound.com and Built In (Austin/NYC/SF) spot
> checks surfaced only already-tracked or summer-cycle roles (Citadel's Operations Analyst intern
> looked promising on duration but citadel.com blocked fetch and no third party confirmed an
> off-cycle cohort — left unverified rather than added on an unconfirmed guess). GradConnection Sydney:
> Australian Treasury program requires Australian citizenship (hard exclude); nothing else new. Tokyo
> (coralcap.co, tokyodev.com, japan-dev.com): no non-engineering internship matches. Named priority
> companies checked directly: Uber/DoorDash don't run on Greenhouse; Uber's actual 2027 Strategic
> Finance/Ops cohort is Amsterdam/Berlin/London, 6 months from February — wrong city and length;
> DoorDash's 2027 cycle is summer-only. Flexport's Greenhouse board (190 live reqs) has no "intern"
> title right now. Palantir's Deployment Strategist internship postings target 2026-grads with a
> security-clearance-gated government track — no 2027-cohort posting found. **Worth a direct cold
> email, not a tracked row:** Clera (SF, pre-seed, Founders Associate Intern, $38–53/hr, in-person,
> runs recurring short cohorts) — its most recent posting was Fall 2026 and is now inactive, no live
> Spring 2027 req to link, but the back-to-back-cohort pattern makes it a good outreach target per the
> cold-email playbook.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Last swept: **2026-10-24** (full sweep — **0 new rows, 1 closure (A144 Rundoo), 1 `DEAD` on the
> liveness pass**.)
>
> Prior — **Sweep 2026-10-23 (full):** 2 new rows, 0 closures. Liveness check (`check_links.py`): 0 `DEAD`,
> 2 `SUSPECT` (A95 Parkdepot, A167 Dell — both re-opened directly, still "Actively hiring," no
> change, same standing text as prior runs), 7 `UNKNOWN` (standing Tesla 403s — A68, A122, A124–A126,
> A139, A172, sampled one directly via WebFetch, still 403, unchanged). Substance re-checks: A145 (E3,
> Lever — unchanged: hybrid ≥3 days/wk, flexible 8–12wk term), A151 (Kroll — unchanged: rolling, no
> stated term), A157 (Scout — unchanged), A158 (Utilyze — unchanged), A177 (Snowflake — **its "Apply
> by Oct 23" deadline is today**; still "Actively hiring," on-site Menlo Park confirmed, apply now if
> pursuing).
>
> **New: A178 (1Password)** — "Data Intern – Product Analytics" (Winter 2027), found via the
> SimplifyJobs off-season README, confirmed live directly on 1Password's own Ashby posting-api.
> Genuinely analytical Data-squad role (SQL/Looker/Amplitude/Hex), strong brand, but fully remote
> (US/Canada) and an explicit "4 months — January to April 2027" window — added `conflict`, not
> dropped, per the never-drop rule. **A179 (Four Hands)** — "Business Operations Analyst Intern"
> (Spring 2027), found via a direct Built In Austin scan, confirmed on the posting itself. In-person
> Austin (home market), Strategy/BizOps-adjacent, but explicitly "through the entire Spring 2027
> term, ending in April 2027" — added `conflict`. A sibling Four Hands posting ("Sales Enablement
> Intern," same Jan–Apr window, more admin/coordination-heavy) was left out as weaker on function fit
> per the quality bar.
>
> **Sweep (full depth):** workatastartup.com/jobs re-confirmed auth-gated for listing detail
> (standing, unchanged); wellfound.com/jobs sampled — no intern-level matches in target functions.
> simplify.jobs top list: only already-tracked Base Power rows and a BlackRock "Quantitative Masters"
> program (graduate-level, excluded) matched target cities. SimplifyJobs Off-Season README parsed
> programmatically (Product Management + Data Science/AI/ML tables, filtered to Winter/Spring 2027 +
> target cities) — surfaced A178 (new, above) and a Cloudflare "People Analytics Data Engineer Intern"
> (Austin, Winter/Spring 2027) that could not be verified: no application link in the README (🔒,
> Simplify-Pro-gated) and the role does not appear on Cloudflare's own public Greenhouse board at all
> (448 reqs pulled via API, zero analytics/people-analytics intern titles) — left out rather than
> added with no real URL to give Sam, per the quality-bar guidance to prefer leaving out an
> unverifiable marginal find over an `unverified` row with nothing to click. Everything else in both
> tables was already tracked or out of scope (engineering, Canada-based, or wrong term). **Economic
> consulting:** Analysis Group's own careers page re-checked directly — summer-analyst/full-time only,
> unchanged (RISE at AG externship has no stated eligibility window, not enough to add); NERA's
> careers URL now redirects, not chased further given the standing no-public-board history; Brattle's
> Greenhouse board (59 reqs, via API) and CRA's Greenhouse board (90 reqs, via API, corrected token
> `charlesriverassociates`) both re-checked — all Research/Analyst Intern titles remain Summer 2027,
> the one Winter/Spring 2027 CRA req (Labor & Employment) remains College Station/Tallahassee-only —
> unchanged. **Built In Austin/NYC** direct scans: Austin surfaced A179 (new, above) plus White Cap
> "Corporate Intern - Inside Sales" (no dates found, weak Sales-function fit, left out) and Expedia
> Applied Science Intern (PhD/Masters only, ineligible); NYC surfaced only already-tracked/excluded
> rows (Circle — prior-cycle "Summer Intern 2026," Gusto — Summer 2027, IDeaS Marketing Analytics
> Intern — remote, no dates/pay, Bloomington MN HQ, same exclusion as the Oct-19/20 sweeps' NYC-tagged
> listing of the same company). **GradConnection Sydney:** nothing beyond already-tracked TikTok reqs
> (A112/A114, now closing in 7 days) and notify-me/EOI placeholders. **Tokyo:** coralcap.co/jobs 404
> (was 503 last run), tokyodev.com still Cloudflare-blocked (403, standing); japan-dev.com's board
> checked — the only "apply from abroad" non-engineering hits (Qubitcore PM, Polymer Capital
> analytics) are full-time ¥8M+ roles, not internships — no match.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Last swept: **2026-10-23** (full sweep — **2 new rows (A178, A179, both `conflict`), 0 closures,
> 0 `DEAD` on the liveness pass**.)
>
> Prior — **Sweep 2026-10-22 (full):** 0 new rows, 0 closures. Liveness check (`check_links.py`): 0 `DEAD`,
> 2 `SUSPECT` (A95 Parkdepot, A167 Dell — both re-opened directly, still "Actively hiring," no
> change; A167's "Apply by Nov 1" reconfirmed as the same rolling aggregator deadline seen since
> Oct 19, not a fixed date), 7 `UNKNOWN` (standing Tesla 403s — A68, A122, A124–A126, A139, A172,
> sampled one directly via WebFetch, still 403, unchanged). Substance re-checks: A92 (TraceRoot,
> YC listing page — unchanged: Developer Marketing Intern, $4–6K/mo, hybrid ≥3 days/wk onsite),
> A128 (Base Power, Built In Austin — unchanged: in-office Austin, no pay/dates stated), A5/A82
> (Dalus, Soren — workatastartup.com detail pages still require login; titles/status reconfirmed
> live via the page shell, substance not independently re-verifiable beyond what's already
> recorded, unchanged).
>
> Last swept: **2026-10-22** (full sweep — **0 new rows, 0 closures, 0 `DEAD` on the liveness
> pass**.)
>
> **Sweep (full depth):** workatastartup.com/jobs re-confirmed auth-gated for listing detail
> (standing, unchanged); wellfound.com/jobs sampled — no intern-level matches in target functions.
> SimplifyJobs Off-Season README re-parsed — nothing beyond already-tracked/excluded rows; two new
> candidates surfaced (Bombardier "Intern, Business Strategy," Pointe-Claire, Quebec; MLSE
> "Business Strategy & Product Management (AI) Intern," Toronto) both excluded on location — not
> target metros. **Economic consulting:** Analysis Group, CRA, and NERA public careers pages link
> only to internal application portals with no visible open-req list (not a change — same gap as
> prior sweeps); Brattle's Greenhouse board (59 reqs, pulled via API) — all Research
> Analyst/Associate Intern titles remain Summer 2027 or (new req, "2026/27 Research Analyst —
> International Arbitration — Madrid") a full-time entry-level hire, not an internship — excluded;
> Compass Lexecon's Workday CXS board unchanged (A154 only). **Palantir's** Lever board (304 reqs,
> via API) — only the already-tracked Paris and Honolulu "Deployment Strategist, Internship" reqs
> exist, unchanged. **DoorDash's** Greenhouse board (458 reqs, via API, correct token
> `doordashusa` found this run) — zero Strategy & Operations internship titles (all S&amp;O titles
> are full-time Associate/Manager), unchanged. **Flexport's** Greenhouse board (194 reqs, via API)
> — zero intern titles, unchanged. **Uber's** career site still returns HTTP 406 on direct fetch —
> standing access gap, unchanged. Built In NYC/Austin/SF direct scans: NYC surfaced only
> already-summer-cycle rows (Gusto, PwC, Citadel, Circle, MetLife); Austin and SF returned zero
> internship results. Intern Insider Winter/Spring 2027 term pages: nothing new in scope (E3
> Consulting Internship, SF, already tracked as A145; TikTok Sydney rows already tracked as
> A112/A114). **GradConnection Sydney:** nothing beyond already-tracked TikTok reqs and
> pay-to-play placement brokerages. **Tokyo:** coralcap.co/jobs 404, tokyodev.com/jobs 403
> (both standing), japan-dev.com's board (282 listings) — no English-friendly, non-Japanese-
> required, entry-level non-engineering match.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com
> 200, simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior — Liveness check 2026-10-21 22:05 UTC: 1 closure — **A76 (Novaflow, Growth Intern)**, confirmed
> `DEAD` by `check_links.py` and WebFetch alike (workatastartup.com/jobs/92868 now 404); was
> `conflict`, now `closed`. 2 `SUSPECT` (A95 Parkdepot, A167 Dell) re-opened directly — both still
> "Actively hiring," no change. 7 `UNKNOWN` (standing Tesla 403s: A68, A122, A124–A126, A139, A172)
> confirmed still blocked via WebFetch — unchanged for months, left `unverified`.
>
> Last swept: **2026-10-21** (full sweep — **1 closure (A14 Celonis, Business Development
> Representative Sales Intern — Built In NYC confirms "this job was removed at 08:09 a.m. (EST) on
> Monday, Oct 19, 2026"), 0 new rows, 0 `DEAD` on the liveness pass.**
>
> **Liveness check (`check_links.py`): 0 `DEAD`, 2 `SUSPECT`, 7 `UNKNOWN`, 97 `OK`.** A95 (Parkdepot)
> and A167 (Dell) both re-flagged SUSPECT (passed-deadline text); both re-opened directly — still
> "Actively hiring," no change. The 7 `UNKNOWN` are the standing Tesla 403s (A68, A122, A124–A126,
> A139, A172) — confirmed still blocked via WebFetch and a browser-UA curl alike; left `unverified`.
>
> **Substance spot-checks this run:** A121 (Ankura, Workday CXS API — unchanged, canApply:true),
> A130 (Kodiak, Greenhouse — unchanged, Jan 2027 start/12–16 wks confirmed), A176 (Gemini, Greenhouse
> — unchanged, Jan–Apr 2027 conflict confirmed), A154 (Compass Lexecon Madrid, Workday CXS API —
> unchanged, still open, apps close 26 Feb 2027), A96 (Crowe Global, Built In Austin — unchanged,
> rolling), A112/A114 (TikTok GBS AU, GradConnection — unchanged, **deadline 30 Oct 2026 1:59pm
> Sydney, now inside three weeks**). A14 (Celonis) closed per above.
>
> **Sweep (full depth):** SimplifyJobs Off-Season README parsed programmatically (Product Management
> + Data Science/AI/ML tables) for target-city/2027 hits — all either already tracked (Tesla A172,
> MTA, Gemini A176, Fenwick A163, NBCUniversal C70) or out of scope (Stand Together "Policy Data
> Analyst Intern," NYC-tagged but the posting's own text gives the office as **Albany, NY** — not a
> target metro — states the role is **full-time**, and references a June 3–4 in-person summit in
> Arlington, VA that implies a cohort running well past Mar 12; excluded on the combination rather
> than added weak). Built In NYC/Austin/SF direct scans: Austin and SF returned zero results this
> run; NYC surfaced IDeaS "Marketing Analytics Intern" (NY-tagged) but IDeaS is Bloomington,
> MN–headquartered with no corroborating direct listing found — left out, not enough to verify.
> **Economic consulting** — Compass Lexecon's own Workday board opened directly: "2027 Analyst
> Interns - US" confirmed **Summer 2027 only** (10 weeks, June–Aug, via the Workday CXS API) —
> excluded; the Madrid Competition-practice intern req is the already-tracked A154, reconfirmed
> unchanged. Brattle's full Greenhouse board pulled directly (56 reqs): every Research
> Analyst/Associate Intern title is **Summer 2027**; "Research Associate Intern" (SF) is explicitly
> for candidates "who have advanced beyond the Research Analyst level" — too senior, not an
> undergrad entry point. CRA's Greenhouse board (89 reqs) has a new "Analyst Intern (Labor &amp;
> Employment practice) - Winter/Spring 2027" req, but it's located College Station, TX / Tallahassee,
> FL only (campus-specific, not a target metro) and reads as a semester-long pipeline-to-full-time
> program — excluded on location. Analysis Group and NERA: summer-analyst/full-time-only, unchanged.
> **Palantir's** Lever board re-checked directly (306 reqs): the only "Deployment Strategist,
> Internship" titles remain the already-tracked Paris and Honolulu reqs — no NYC/SF opening.
> **DoorDash's** Greenhouse board (458 reqs, finally reachable directly) has zero Strategy &amp;
> Operations internship — only a full-time Senior Associate role and Summer-2027 SWE/ML/design
> internships. **Flexport's** Greenhouse board (204 reqs): zero intern titles, unchanged. **Uber's**
> career site still would not render for either a direct fetch or a headless-browser fetch (30s
> timeout on networkidle) — standing access gap, unchanged. **workatastartup.com**: the `/jobs`
> listing page itself now renders (200, with a browser UA + Accept header), but the job board is a
> client-side React app that requires a logged-in session to populate — confirmed via a headless
> Chromium render (page loads, "Log in" present, no job data in the DOM or any embedded JSON); not a
> simple JS-shell problem as previously assumed, but an auth gate. **wellfound.com**: similarly
> renders without login for its generic `/jobs` feed (49 real listings extracted), but none were
> intern-level in that sample, and the role-specific landing pages (`/role/&lt;slug&gt;`) are SEO/signup
> pages with no listings in the page source. Both remain effectively unswept pending the November YC
> batch and/or an authenticated approach. **Tokyo**: tokyodev.com is behind a Cloudflare bot check
> (unreachable); japan-dev.com's full 278-listing board pulled directly — two non-engineering hits
> (Product Manager and Sales Engineer at Mujin/Axelspace) are both full-time, Japanese-required,
> ¥6–10M roles, not internships — no match. coralcap.co returned 503 (Retry-After 3600) both times
> checked this run. GradConnection Sydney: Capgemini/Jemena/Treasury hits are all outside the Dec
> 2026–Feb 2027 intake or already excluded (TikTok rows already tracked as A112/A114).
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior — Liveness check 2026-10-20 22:03 UTC: closed A134 Acxiom (Intern Insider title "Closed:
> Intern - Agency Partnerships at Acxiom," banner "This internship has closed," applications
> closed Oct 19 2026). A95 (Parkdepot) and A167 (Dell) re-flagged SUSPECT on passed deadline
> text, both confirmed still "Actively hiring" directly — no change. 7 standing Tesla UNKNOWNs
> (A68, A122, A124–A126, A139, A172) still 403 on direct fetch — left unverified.
> Last swept: **2026-10-20** (full sweep — **0 new rows, 0 closures, 0 `DEAD` on the liveness pass**.
> Liveness check (`check_links.py`): 0 `DEAD`, 2 `SUSPECT`, 7 `UNKNOWN`, 89 `OK`. The 2 `SUSPECT`
> rows — **A95 (Parkdepot)** and **A167 (Dell)** — both re-opened directly: still "Actively hiring,"
> deadline text unchanged ("Apply by Nov 1" on A167, no year stated on A95), no status change. The
> 7 `UNKNOWN` remain the standing Tesla 403s (A68, A122, A124–A126, A139, A172) — confirmed still
> blocked on direct fetch and WebFetch alike this run too; left `unverified`.
>
> **Substance spot-checks this run:** A13 DeepAware AI, A22 CertiK, A65 Peakflo, A83 Relling, A93
> NewsBreak, A131/A133 Base Power (Financial Planning / Deployments Operations), A169/A171 MTA
> (Data Analysis–Supplier Relations / Operations Support), A173 Pennant — all confirmed unchanged
> against the tracker's claims where the posting was readable. **A13, A65, A83, A173**
> (workatastartup.com) returned only the bare listing title via WebFetch — same standing JS-shell
> limitation as A75 (Surface Labs); inconclusive this run, no change made.
>
> **Sweep (full depth, pre-November — YC W27 batch has not yet landed):** SimplifyJobs Off-Season
> README (Software Engineering, PM, Data Science/AI/ML, and mixed/quant-finance tables) —
> everything in-market was either pure engineering, out-of-window (Summer 2027 or an already-past
> "Winter 2026"), Canada-based, or already tracked (GE Aerospace, Stripe, Figma, Zipline, MTA,
> Tesla variants). Economic consulting direct pages (Analysis Group, Cornerstone, CRA, Compass
> Lexecon, Brattle, NERA) re-checked again — still summer-analyst/full-time-only; CRA's own board
> lists only "2027 graduate" Analyst/Associate full-time hires. simplify.jobs top list: one marginal
> hit (Copart Technology Product Analyst Intern, Dallas) excluded on location. BuiltIn NYC/Austin/SF:
> a few borderline strategy/ops/PM internships (PwC Strategy&amp;, Atlantic PM intern, Four Hands Biz
> Ops Austin) found, all **Summer 2027**, out of window. GradConnection Sydney: 20 listings, all
> either Australian Summer 2027/28 (Nov 2027 start — wrong hemisphere cycle) or notify-me/virtual-
> experience placeholders with no real posting. Palantir's Lever board filtered to Deployment
> Strategy: zero postings. Flexport: no internships listed. workatastartup.com and wellfound.com:
> same standing JS-shell/widget limitation as prior runs (WebFetch and curl both return only a bare
> page title or an empty static list) — no dedicated sweep possible from this environment pending a
> scripted-browser approach; due for a fresh pass once the November YC batch lands regardless.
> **Access problems this run:** DoorDash careers (403), tokyodev.com/jobs (403 via WebFetch and
> curl), coralcap.co (no browsable openings list at /careers/ or /coral-careers/), Uber careers page
> (JS job list never renders for WebFetch), japan-dev.com's one Tokyo hit (HENNGE Full-Stack GIP) is
> engineering, excluded on function.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior — Last swept: **2026-10-19** (full sweep — **3 new Tier A rows (A175 GE Aerospace Data Science Co-op,
> unverified; A176 Gemini Product Management Intern, conflict; A177 Snowflake Product
> Marketing/GTM Intern, live — function ambiguity flagged), 0 closures, 0 `DEAD` on the liveness pass,
> 2 SUSPECT rows (A95 Parkdepot, A167 Dell) re-opened and confirmed unchanged.**
>
> **Liveness check (`check_links.py`): 0 `DEAD`, 2 `SUSPECT`, 7 `UNKNOWN`, 87 `OK`.** A95 (Parkdepot)
> and A167 (Dell) both flagged SUSPECT on their passed deadline text; both re-opened directly — still
> "Actively hiring." A167's deadline text has itself rolled forward on the page, from "Apply by Oct 17"
> to **"Apply by Nov 1"** — confirms a rolling aggregator deadline that keeps advancing, not a stale
> page; no status change. The 7 `UNKNOWN` are the standing Tesla 403s (A68, A122, A124–A126, A139,
> A172) — still blocked on direct fetch and WebFetch alike, unchanged for months; left `unverified`.
>
> **Substance spot-checks this run:** A98 Cresta, A120 MTA (EAM Analyst), A121 Ankura, A151 Kroll,
> A129 Base Power (Finance–Analytics), A153 Contoro Robotics, A161 MTA (EAM Value Realization) — all
> confirmed unchanged against the tracker's claims (location, mode, pay where stated). **A121 (Ankura)**
> specifically re-verified live via Workday's own CXS API (`canApply: true`, `posted: true`), bypassing
> the JS-shell that blocks a plain fetch. **A75 (Surface Labs)** — WebFetch returned only the page
> title, not the full posting; inconclusive this run, no change made pending a fuller re-check.
>
> **Liveness check 2026-10-19 22:00 UTC: 1 `DEAD` → closed (A98 Cresta, Greenhouse API 404 and
> job page redirects to `/cresta?error=true`), 2 `SUSPECT` re-opened and confirmed unchanged (A95
> Parkdepot, A167 Dell — both still "Actively hiring"), 7 `UNKNOWN` unchanged (standing Tesla 403s).
> 89 `OK`. No new rows this run (liveness-only pass).**
>
> **New: A175 (GE Aerospace) — "SaaS – Flight Analytics Platform" Data Science Co-op, Austin, TX.**
> Found via the SimplifyJobs off-season README's Data Science section, confirmed directly on GE's own
> Workday CXS API (`canApply: true`). Clean Data-function, home-market match — but no term length,
> dates, pay, or mode stated anywhere on the posting; added `unverified` per the A165 Figma/A166
> Stripe convention, not for failure to open it. Flagged in the note: GE co-ops have historically run
> full-semester (~6-month) blocks, so the "Spring 2027" title tag is not read as confirming a Jan–Mar
> fit.
> **New: A176 (Gemini) — Product Management Intern (Winter 2027), New York, NY.** Found via the same
> README's Product Management section, confirmed directly on Gemini's own Greenhouse board (job
> 8214332, not SimplifyJobs' embed link). Genuinely data-driven PM work (Databricks, PRDs, release
> planning) — strong PM-function fit — $45/hr, hybrid (3 days/wk in-person stated). Real conflict: the
> posting states explicitly "semester long... from January to April 2027," ~3 weeks past the Mar 12
> hard stop. Added `conflict` per the never-drop rule rather than excluded — strong brand and pay,
> worth an early application disclosing the Jan 4–Mar 12 window up front.
> **New: A177 (Snowflake) — "Product Marketing, AI-Powered Data Engineering Intern" (Winter 2027),
> Menlo Park, CA.** Found via Intern Insider's winter/spring-2027 terms pages; the title is misleading
> — the actual role (customer-story sourcing, launch planning, sales-enablement assets) reads as
> GTM/product marketing, not data engineering. Kept per the ambiguity rule (substance is unclear
> against the content-marketing exclusion, not a clean exclude) — scored Growth, Fit marked down
> accordingly. 12 weeks, on-site, $40–47/hr, strong brand; no direct Snowflake ATS link found (JS-
> rendered site), kept the Intern Insider link per the A93/A95/A167 pattern.
>
> **Also checked, nothing added:** Economic consulting direct careers pages (Analysis Group, Brattle,
> NERA) re-checked — still summer/associate-only, no winter/spring internship cycle found; consistent
> with prior runs' findings for the full six-firm set. Intern Insider's winter-2027 and spring-2027
> terms pages scanned beyond Snowflake — remaining hits were out-of-market (Canada, Midwest) or
> already tracked (MTA Ops Support = A171, E3 = A164). SimplifyJobs README Data Science/PM sections:
> several 🎓-tagged roles (Together AI, Genentech, Block) excluded as advanced-degree/PhD-targeted;
> Rivian/Brain Co./Composio excluded as core software/ML engineering, not an analytics fit; KQED
> "Audience Intelligence Intern" (SF, clean Data substance, $19.61/hr) excluded rather than flagged
> `conflict` — its stated term is Jan 19–Jun 25 2027 (~22 weeks), more than double the 10-week target
> with no flexibility signal from a structured nonprofit program, and pay/prestige are both low — judged
> marginal rather than "strong but date-conflicted." workatastartup.com, Wellfound, BuiltIn
> NYC/Austin/SF, GradConnection Sydney, and the Tokyo boards (Coral Capital/Japan Dev/TokyoDev) were
> not re-swept this run (all checked within the last 1–2 full runs with nothing beyond already-tracked
> rows, and YC's W27 batch has not yet landed) — due for a fresh pass once the November YC batch lands.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior — Last swept: **2026-10-18** (full sweep — **3 new Tier A rows (A172 Tesla Data Analyst Intern/People
> Products, unverified; A173 Pennant Founder Fellow, live; A174 Zipline Change Management Intern,
> conflict), 1 closure (A9 Lambda Robotics), 0 `DEAD` on the liveness pass, 2 SUSPECT rows resolved
> with no status change.**
>
> **Closure: A9 (Lambda Robotics) — Founding GTM, San Francisco.** Its workatastartup.com job id now
> resolves to a different company's listing ("Runtime.si, Founding GTM") — the original posting is
> gone, the id was reassigned/reused. Closed per the liveness/substance pass.
>
> **Liveness check (`check_links.py`): 0 `DEAD`, 2 `SUSPECT`, 6 `UNKNOWN`, 86 `OK`.** The 2 `SUSPECT`
> rows — **A95 (Parkdepot)** and **A167 (Dell)**, both flagged on a passed "Oct 17" deadline — were
> both re-opened directly: still "Actively hiring," rolling/no-year-stated deadline, Apply button
> live. No closure, no status change; dated note added to each. The 6 `UNKNOWN` are the standing
> Tesla 403s (A68, A122, A124–A126, A139) — still blocked on direct fetch and via WebFetch,
> unchanged for months; left `unverified` per the standing pattern.
>
> **Substance spot-checks this run:** A5 Dalus, A14 Celonis, A70 Base Power, A82 Soren, A92
> TraceRoot, A96 Crowe, A112/A114 TikTok Sydney, A128 Base Power, A130 Kodiak, A134 Acxiom, A145 E3,
> A154 Compass Lexecon Madrid, A157 Scout, A158 Utilyze — all confirmed unchanged against the
> tracker's claims (pay, location, mode, dates), except **A112 (TikTok, Client Solution Intern,
> Sydney)** which now shows a firm closing date, **30 Oct 2026** — inside the three-week deadline
> window, flagged below.
>
> **New: A172 (Tesla) — Data Analyst Intern, People Products, Palo Alto, CA / Austin, TX.** New
> distinct Tesla req (286085), found via the SimplifyJobs off-season README's Data Science section —
> not a duplicate of A68/A122/A124–126/A139. Same standing 403-on-direct-fetch pattern as every other
> Tesla row; added `unverified` on that basis.
> **New: A173 (Pennant, YC S26) — Founder Fellow – GTM, Growth & Strategy, New York, NY.** Found via
> a direct workatastartup.com sweep. In-person required ("IRL is a must"), seasonal/rolling with no
> fixed dates (startup sets the term) — substance is market research, competitor analysis,
> growth-metric tracking, and GTM experiments, squarely Strategy/Growth and clear of the
> content-marketing exclusion. No pay listed on this posting; other Pennant FTE roles show
> $150–250K, so this may be an unpaid/stipend seasonal-fellow structure — flagged Unconfirmed.
> **New: A174 (Zipline) — Change Management Intern (Spring 2027), South San Francisco, CA.** Fourth
> distinct Zipline Spring 2027 req (sibling to A4/A16/A64/A123), found via the same SimplifyJobs
> README; confirmed directly on Zipline's own Greenhouse-backed careers page (job 7990677003, board
> token `flyzipline`). On the New Product Introduction team — builds internal tools for hardware
> change management (Python/SQL/dashboards) rather than pure growth or ops. Posting states plainly
> "we will host our Spring 2027 interns from January to April" — the same Jan–Apr conflict pattern
> as every other Zipline Spring row. Eligibility lists ME/CS/info-systems/data-science majors;
> flagged as a genuine ambiguity (the Stats &amp; DS minor plausibly qualifies) rather than assumed.
>
> **Also checked, nothing added:** three other workatastartup.com candidates (Growth & Operations
> Intern @ Juno, GTM & Content Marketing Intern @ Lance, GTM Intern @ Revyl) excluded on the
> substance test — all three are centrally about recruiting/managing creators, producing short-form
> video, and running a social posting calendar, not analysis. Dalus's GTM Intern (job 99648) is the
> same posting already tracked as A5 — confirmed unchanged, not re-added. Economic consulting direct
> careers pages (Analysis Group, Cornerstone, CRA, Compass Lexecon, Brattle, NERA) — all six still
> summer-only or general "Students & Graduates" pages with no off-cycle reqs; CRA's own board lists
> only full-time "2027 graduate" Analyst/Associate hires, not internships. Compass Lexecon's Madrid
> intern req (A154) independently re-verified live via its own Workday CXS API — unchanged, still
> `blocked*` pending the UT Austin convenio question. Palantir's Lever board, Uber/DoorDash/Flexport,
> BuiltIn NYC/Austin/SF, Coral Capital/TokyoDev/Japan Dev, and GradConnection Sydney all re-checked —
> nothing beyond already-tracked rows or out-of-window (Summer 2027) postings.
>
> **Lane coverage note:** wellfound.com's job-title search is a React-select widget that would not
> drive via direct URL params or scripted clicks within this run's time budget — no dedicated
> Wellfound sweep this run beyond the general jobs page; flagging for a future run to script the
> widget properly or use manual category URLs.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior — Last swept: **2026-10-17** (full sweep — **3 new Tier A rows (A169 MTA Data Analysis/Supplier
> Relations, live; A170 FOX News Media Data Analytics, conflict; A171 MTA Operations Support, live),
> 2 closures from the liveness pass below (A135, A142 Acxiom), 1 Tier B correction (B1 Charles Schwab
> `monitor` → `closed` — its 2027 program is summer-only, no spring/winter cycle exists).**
>
> **New: A169 (MTA) — Data Analysis (Supplier Relations), Emerging Talent Intern (Spring), New York,
> NY.** Sibling req to A120/A160/A161, found via the SimplifyJobs off-season README's Data Science
> section and confirmed directly on MTA's own Jobvite ATS (`jobs.jobvite.com/.../oOvWAfwz`).
> Undergraduate-eligible at $19/hr, same onsite/20-hrs-min pattern as the rest of the MTA cluster.
> **New: A170 (FOX News Media) — Spring 2027 Internship Program, Data Analytics, New York, NY.**
> Found via the same SimplifyJobs README parse, confirmed directly on FOX's own Workday CXS API
> (req R50033950). In-person, part-time (16–24 hrs/wk), $20.00/hr (employer-stated pay-disclosure
> footer), sophomore+ eligible. Added `conflict` rather than excluded: the posting's own "SPRING 2027
> SCHEDULE" block states explicit dates of Monday, February 8, 2027 – Friday, April 16, 2027
> (deadline Nov 22, 2026) — about 5 weeks past the Mar 12 hard stop — worth asking directly whether a
> shortened block is possible given the real brand-name/Data-function fit.
> **New: A171 (MTA) — Operations Support, Emerging Talent Intern (Spring), Brooklyn, NY.** Fourth
> MTA "Emerging Talent" sibling, found via a direct Intern Insider winter-2027-term crawl and
> confirmed on MTA's own Jobvite ATS. Based at 130 Livingston Street (Department of Subways
> Operations Support), distinct team/office from the Manhattan HQ rows. Undergraduate-eligible at
> $19/hr, same onsite pattern as A120/A161/A169.
>
> **Correction: B1 (Charles Schwab) closed.** The row's own "opens" window (Sept–Nov 2026) was active
> as of this sweep, so checked directly on Schwab's Intern Academy page rather than waiting further.
> Schwab's entire 2027 program is a single summer cohort, June 7–August 6, 2027 — "we are not able to
> make exceptions" on those dates, no spring/winter cycle exists. Closed per the hard exclusion on
> anything that can't finish by Mar 12.
>
> **Substance spot-checks this run (A5 Dalus, A98 Cresta, A120 MTA EAM Analyst, A121 Ankura, A145
> E3): all confirmed unchanged** — no corrections to report. **A167 (Dell) and A95 (Parkdepot)** both
> carry an "Apply by Oct 17" badge landing today — re-opened directly, both still "Actively hiring"
> with active Apply buttons, no "Closed" signal, consistent with the already-documented pattern that
> these Intern Insider badges are soft/rolling. No status change on either.
>
> **Economic consulting firms checked again this run** (per standing instruction): analysisgroup.com,
> cornerstone.com, crai.com, compasslexecon.com, brattle.com, plus peers Bates White, Berkeley
> Research Group, Edgeworth Economics, and NERA. All confirmed summer-cycle-only or JS-gated with no
> listings reachable; Compass Lexecon's own recruiting post explicitly targets students entering
> their **final year in fall 2027** (disqualifying for Sam's junior-year timeline). No off-cycle
> econ-consulting opening found anywhere in this family, same as every prior sweep.
>
> **Also checked and confirmed empty this run:** YC (workatastartup.com — Winter 2027 batch still
> hasn't landed, as expected before November), Wellfound, Simplify.jobs's Top internships list,
> GradConnection Sydney, Coral Capital / Japan Dev / TokyoDev (Tokyo — no internships for
> non-Japanese-speaking undergrads found), Plaid/Segment/Deel/Rippling ATS boards (resolving last
> run's flagged gap — genuinely empty of non-engineering intern postings right now, not a
> slug/access problem), and Uber/DoorDash/Flexport/Palantir Deployment Strategist (Palantir's own NY
> Deployment Strategist internship requires graduating in 2026 as one's final internship — a hard
> eligibility mismatch for Sam's Class-of-2028 timeline, not just a date conflict; no Uber/DoorDash/
> Flexport internship-length Strategy & Ops opening found for 2027). One false lead ruled out:
> aggregator copies of a "SpaceX Spring 2027 Business Operations Internship/Co-op" resolve to the
> same Greenhouse requisition as A168 (xAI) — mislabeled by the aggregator, not a second company.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Liveness check **2026-10-17 13:05 UTC** (`check_links.py`, 94 open rows before adding A169–A171):
> **2 closed** — A135, A142 (both Acxiom, Intern Insider "Closed:" page title, same pattern as the
> A136/A137 closures on 2026-10-15). 7 `UNKNOWN`: 6 Tesla 403s (standing, unchanged for months), 1
> LinkedIn 429 on A1 (standing, transient). 0 `SUSPECT`.
>
> Prior: **2026-10-16** (full sweep — **1 new Tier A row (A168 xAI Business Operations
> Internship/Co-op, conflict), no closures beyond the liveness pass below, no corrections.**
>
> **New: A168 (xAI) — Business Operations Internship/Co-op, Palo Alto, CA.** Found via a direct
> Greenhouse fetch (`job-boards.greenhouse.io/xai/jobs/5255113007`), confirmed on xAI's own ATS, not
> an aggregator. Strategy & Operations generalist role at a frontier-AI company — no major gate
> (Econ not excluded; 3+ months of corporate/business-function experience required, which the
> posting explicitly lists as satisfiable by data analysis, finance, HR, IT, gov affairs, legal,
> advertising, or sales), $24.50–26/hr depending on class standing plus relocation stipend.
> **Dates don't cleanly fit**: the posting requires "full time, onsite for a minimum of 12
> consecutive weeks beginning in January or March 2027" — a Jan 4 start plus the 12-week floor runs
> to roughly Mar 29, ~2.5 weeks past the Mar 12 hard stop; a March start is worse. Added as
> `conflict` per the never-drop rule rather than excluded — worth an early direct application with
> explicit up-front disclosure of the Jan 4–Mar 12 window (per `PROFILE.md`'s disclosure protocol),
> in case they'll flex the floor for the right candidate. Substance spot-checks this run (A96 Crowe,
> A128 Base Power, A151 Kroll, A82 Soren, A92 TraceRoot) all confirmed unchanged. Delegated board
> sweep (YC, Wellfound, Simplify, Intern Insider, BuiltIn, GradConnection, Tokyo, Palantir, Uber,
> DoorDash, all six named economic-consulting firms, plus a deeper pass on Instacart/Faire/Stripe/
> Twilio/Ramp/Brex/Mercury/Plaid/Segment/Deel/Rippling ATS boards) found nothing else that clears
> the quality bar — YC/Wellfound still empty ahead of the Winter 2027 batch, economic consulting
> firms still summer-only/full-time-only, no new target-metro hits elsewhere. Plaid/Segment/Deel/
> Rippling boards 404'd on standard ATS slugs this pass — not confirmed empty, worth retrying with
> correct slugs next sweep, not a new access gap.
>
> Liveness check **2026-10-16 13:20 UTC** (`check_links.py`, 94 open rows after adding A168): **0
> closed**, 0 `SUSPECT`, 9 `UNKNOWN` — all standing known gaps: 6 Tesla 403s (unchanged for months)
> and 3 BuiltIn NYC 429s (A18, A72, A149 — a Cloudflare challenge page, not a real rate limit),
> all three resolved directly with a spaced-out browser-UA retry — 200, normal non-"Closed" titles,
> confirmed still live, no status change.
>
> Liveness check **2026-10-15 22:08 UTC** (`check_links.py`, 95 open rows): **2 closed** —
> A136, A137 (both Acxiom, Intern Insider "Closed:" page title). 11 `UNKNOWN`: 6 Tesla 403s
> (standing, unchanged); 5 BuiltIn NYC 429s (new this pass — a Cloudflare challenge page, not a
> real rate limit) resolved directly with a spaced-out browser-UA retry: 4 of 5 (A18, A148, A149,
> A155) returned 200 with normal, non-"Closed" titles — confirmed still live, no status change;
> A14 stayed challenge-walled after a second retry, left `unverified`/unchanged per protocol.
> 0 `SUSPECT`.
> Liveness check **2026-10-14 22:25 UTC** (`check_links.py`, 107 open rows): **12 closed** —
> A6, A84, A85, A87 (WAAS 404), A78, A88, A90 (Wellfound 410), A80 (Notion Ashby board dropped
> the req), A81 (Intern Insider 404), A111 (Greenhouse API 404), A109, A140 (Intern Insider
> "Closed:"). The daily sweep had missed all twelve: it only re-opened a handful of rows per run.
>
> Last swept: **2026-10-15** (full sweep — **1 checker-bug correction (false `DEAD` on A138
> Heron Power, caused by `check_links.py` truncating ATS API reads at 400KB — fixed, see below),
> no new Tier A rows, no closures.**
>
> **Correction: A138 (Heron Power) — false `DEAD` from a checker bug, not a real closure.**
> `check_links.py`'s liveness pass flagged A138 as `DEAD` ("ashby board no longer lists id"). Before
> closing it per the liveness protocol, confirmed directly: fetched Heron Power's Ashby job-board API
> payload in full (580KB) and found the job id present (`isListed: true`), and fetched the posting
> page itself directly — 200, correct `<title>`, live Apply button, no closed signal anywhere. Root
> cause: the checker's `get()` helper only reads the first 400,000 bytes of any response, and this
> particular job id happens to sit at byte offset ~409,934 in Heron Power's (unusually large) board
> JSON — past the cutoff, so the id-presence check always missed it. Fixed by raising the read cap to
> 4MB; re-ran the full checker clean afterward (0 `DEAD`, 0 `SUSPECT`). A138 stays `unverified`,
> unchanged — it was never actually dead.
>
> **Liveness check (`check_links.py`, post-fix): 95 open rows, 0 `DEAD`, 0 `SUSPECT`, 7 `UNKNOWN`.**
> All 7 `UNKNOWN` are standing, already-understood access gaps, not new signals: six are Tesla's
> careers site (`www.tesla.com/careers/search/job/…`, HTTP 403 on every attempt for months — A68,
> A122, A124–A126, A139), one is a LinkedIn 429 rate-limit on A1 (Brilliant Infotech, already
> `conflict` status, transient). No status changes from this pass.
>
> **Substance spot-checks (live rows not recently re-touched).** **A167 (Dell Technologies, Corporate
> Strategy Undergrad Intern)** — re-opened directly on Intern Insider: unchanged, still "Apply by Oct
> 17" (now **2 days out**), no term/duration/start date still stated anywhere. **A95 (Parkdepot,
> Marketing Analyst Intern)** — re-opened directly: still "Actively hiring," deadline unchanged ("Apply
> by Oct 17," also **2 days out**). **A161 (MTA, EAM Value Realization)** — Jobvite posting re-opened
> directly, title/page unchanged, no closed signal. **A153 (Contoro Robotics, BD Intern)** — Built In
> posting re-opened directly, unchanged, no closed signal. All four confirmed live and substantively
> unchanged from their tracked details.
>
> **Full re-sweep of every standing source (delegated sub-pass) found nothing that clears the quality
> bar for addition.** **YC/Wellfound** — workatastartup.com reachable (200) but still an empty
> client-rendered shell (no listings extracted, even on an internship-filtered query) — Winter 2027
> batch not live yet, as expected ahead of ~November 2026; wellfound.com reachable, zero internship
> postings on the sampled page. **Economic consulting** — all six named firms (Analysis Group,
> Cornerstone, Charles River Associates, Compass Lexecon, Brattle, NERA) reachable and re-checked
> directly; CRA's own board (91 open reqs) is entirely full-time Bachelor's/Master's-2027 Analyst/
> Associate hiring or PhD Senior Associate roles, no internships, no Jan–Mar dates; the rest remain
> summer-only or render empty, unchanged. **SimplifyJobs off-season README** downloaded fresh (41,258
> lines, +176 since 2026-10-14) and parsed programmatically end-to-end for every target-city/function/
> term hit — every match (MTA ×4, Tesla Data Analyst Intern, FOX Data Analytics Intern, GE Aerospace
> Flight Analytics Co-op, Zipline, Disney Insights/Marketplace ×2, Cloudflare People Analytics Data
> Engineer Intern, J&amp;J AI/ML/DS Intern) is already a tracked row or an already-logged exclusion —
> no net-new hit. **Intern Insider's** Winter/Spring 2027 term pages re-sampled — only flagged hit is
> E3 (already tracked as A145/A164 — confirmed these are genuine duplicate rows for the same posting,
> worth merging on a future pass, not done this run to avoid losing either row's distinct note
> history). **BuiltIn NYC/Austin/SF** — no new Winter/Spring-2027-tagged hit, only Summer 2027/2028
> postings (PwC Strategy&amp; NYC, CrowdStrike/Cox/Optiver/Itron Austin). **GradConnection Sydney** —
> nothing beyond already-tracked TikTok reqs and already-excluded employers (Capgemini, Nestlé YEP, DT
> Infrastructure, ANZ, EY, Treasury, CommBank). **Tokyo** — coralcap.co/jobs still 404s (standing gap);
> coralcap.co/careers loaded (4 postings, all requiring business Japanese or VC experience, none
> match); tokyodev.com/jobs 403'd again (two sweeps running, isolated, not a sanity-check domain);
> japan-dev.com loaded, no non-engineering English-first match. **Palantir's** Lever board re-checked
> unfiltered — still only the Paris/Honolulu Deployment Strategist Internship reqs; a new "Meritocracy
> Fellowship (Business Development)" req, NYC, was found and rejected — it's explicitly a recent-
> high-school-graduate program (not current-college-student eligible), not added. **Uber** — remains a
> client-rendered shell even on an intern-query URL, no listings extracted. **DoorDash**
> (job-boards.greenhouse.io/doordashusa, 458 reqs) — no internship titles found. **Flexport** — no
> internship postings site-wide.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-10-14** (daily sweep — **1 note-only correction (A112/A114 TikTok Sydney:
> subclass-462 work-rights confirmation re-done at the per-req level rather than the page-wide
> list, resolving the recurring truncation ambiguity for good — see below), no new Tier A rows,
> no closures.**
>
> **Correction: A112/A114 (TikTok, Sydney).** Past sweeps resolved the "...show more" work-rights
> truncation by grepping the rendered page for "Australian Working Visa," but that page also lists
> several unrelated TikTok Sydney reqs sharing an identical generic work-rights taxonomy, so a
> bare page-wide match was always at risk of confirming the wrong job's block. This pass isolated
> each req's own `work_rights` JSON array directly and confirmed "Australian Working Visa" is
> listed specifically for A112 and for A114, not just inferred from a sibling req. Subclass 462
> eligibility is now confirmed at the correct scope. No status or date change — both stay `live`,
> closing 30 Oct 2026, 1:59pm Sydney, unchanged.
>
> **Re-verification pass.** **A93 (NewsBreak)** — unchanged, still "Actively hiring," still reads
> "Apply by Oct 12" verbatim two days past that date with no closure — confirms the soft-deadline
> reading. **A95 (Parkdepot)** — unchanged, "Apply by Oct 17," 3 days out. **A159 (Wonder)** — the
> Workday posting is still an empty JS shell on every attempt; no headless-render path available in
> this environment; stays `unverified`, unchanged. **A167 (Dell)** — Intern Insider listing
> unchanged (still "Apply by Oct 17," no term/duration/start date stated). Dell's own primary site
> (jobs.dell.com) now confirmed systemically unreachable rather than an intermittent fetch issue:
> every URL pattern tried (a known-valid job-detail URL, the search endpoint, a keyword search)
> returns an HTML page literally titled "Page not found," by raw curl, not just WebFetch — the 4th
> consecutive sweep with this exact result. A secondary lead (a Bentley University CareerEdge mirror
> of a similarly-titled "Strategy & Operations Undergraduate Intern" req) returned HTTP 410 behind a
> student login wall and carries a different title than the tracked req — not usable as independent
> confirmation, not pursued. Stays `unverified`, unchanged. Spot-checked three `live` rows not
> recently re-touched — **A22 (CertiK)**, **A65 (Peakflo)**, **A92 (TraceRoot.AI)** — all confirmed
> unchanged.
>
> Full re-sweep of every standing source found nothing that clears the quality bar for addition.
> **YC/Wellfound** — workatastartup.com returned `406` on this pass rather than the usual `301`;
> consistent with the bot-challenge quirk noted on 2026-10-11 (a bare request without a browser
> `Accept` header gets a different status than one with it) rather than a genuine access regression
> — WebFetch still renders an empty client-side shell either way, expected ahead of the ~November
> 2026 YC Winter 2027 batch. wellfound.com rendered but surfaced zero internship listings on the
> sampled page. **Economic consulting** — Analysis Group, Cornerstone Research, Charles River
> Associates (including its jobs-board subpage, not just the landing page), Compass Lexecon, Brattle
> (including its Current-Openings subpage, a client-rendered shell), and NERA all re-fetched directly
> — all still summer-only or inconclusive, unchanged. **SimplifyJobs off-season README** downloaded
> fresh (41,082 lines) and parsed programmatically across all five sections for every target-city +
> function + 2027-term hit: two new-looking candidates surfaced (Kodiak Robotics "Data Engineering
> Intern," Mountain View, and Bayer "Data Science Co-Op," Berkeley) but neither cleared the quality
> bar — Kodiak's posting states a 12–16 week term from a January start, which at the 12-week floor
> still overruns 12 Mar by ~2.5 weeks, and the role reads as genuinely technical data-engineering
> work rather than the analytics/commercial-adjacent lane this profile targets, with a garbled
> $10,000–$10,000 pay field; Bayer's posting is simultaneously tagged "Winter 2027" and "Summer
> 2027" with no explicit dates (reads as an evergreen multi-cycle req, not a dated Jan–Mar slot) and
> its eligibility language leans PhD-preferred with an ambiguous "or an undergraduate degree" clause
> echoing the MTA A160 grad-only precedent. Both excluded as marginal rather than added at Priority
> Low, per the tightened quality bar. Confirmed zero rows in the README mention Sydney, Madrid, or
> (non-Melbourne-FL) Melbourne, and no distinct Strategy/Growth/BD/Partnerships/Sales category exists
> in this repo at all. **Intern Insider's** Winter/Spring 2027 term pages — only the already-excluded
> Bayer lead, no other target-function/city hit. **BuiltIn NYC/Austin/SF** — nothing new; all
> target-function-adjacent hits remain Summer 2027. **GradConnection Sydney** — nothing beyond the
> already-tracked TikTok reqs and pay-to-play brokerages. **Tokyo** — coralcap.co/jobs still 404s
> (standing gap); coralcap.co/careers loaded (4 postings, all already-excluded); japan-dev.com's
> non-engineering hits all explicitly require Japanese, ruling them out per the English-first
> positioning; tokyodev.com/jobs returned a new `403` on direct fetch (not one of the five
> sanity-check domains, isolated, not treated as a broader regression). **Palantir's** Lever board
> re-checked unfiltered (44 "Internship" reqs) — still only the Paris and Honolulu Deployment
> Strategist Internship reqs. **Uber** — careers site remains a client-rendered shell, no internship
> confirmed either way. **DoorDash** — found its Greenhouse board moved to the slug `doordashusa`
> (the old `doordash` slug now 404s, useful for future sweeps); no internship postings visible.
> **Flexport** — no internship postings site-wide.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 406 — see bot-challenge
> note above, not a regression; wellfound.com 200, simplify.jobs 200, job-boards.greenhouse.io 200,
> www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-10-13** (daily sweep — **1 note-only correction (A93 NewsBreak: stated
> deadline passed without the listing closing, resolving last sweep's "hard cutoff" framing —
> see below), no new Tier A rows, no closures.**
>
> **Correction: A93 (NewsBreak, Growth Engineer Intern, Mountain View).** The 2026-10-12 sweep
> flagged Oct 12 as "the hard cutoff." Re-opened directly today (Oct 13, one day past that date):
> the listing is unchanged — still tagged "Actively hiring," still reads "Apply by Oct 12" / "Best
> applied by Oct 12." The identical "Apply by X" / "Best applied by X" phrasing also appears on
> A95 (Parkdepot)'s Oct 17 deadline, which that posting's own "rolling" term tag frames as a
> recommendation, not a hard cutoff. Since A93's stated deadline has now passed with no closure,
> that reading is confirmed for A93 too: softened "hard cutoff" language from the prior note.
> Status unchanged (`live`, Priority Low).
>
> **Re-verification pass.** Re-verified the remaining at-risk/near-term rows via direct fetch:
> **A95 (Parkdepot)** — still "Actively hiring," deadline unchanged (Oct 17 2026, 4 days out).
> **A112/A114 (TikTok Sydney)** — both still open, closing date unchanged (30 Oct 2026, 1:59pm
> Sydney, 17 days out — inside the 3-week window); work-rights list still truncated behind "...show
> more" on this pass, but both reqs confirmed "Australian Working Visa" explicitly on the prior
> (2026-10-06) sweep and nothing suggests a narrower policy this time. **A159 (Wonder)** — direct
> Workday fetch still an empty JS shell, same as every prior attempt; no new mirror evidence found
> this pass — stays `unverified`, unchanged. **A167 (Dell)** — Intern Insider listing unchanged:
> still "Apply by Oct 17," no term/duration/start date stated; stays `unverified`, unchanged.
>
> Full re-sweep of every standing source found nothing new that clears the bar. **YC/Wellfound** —
> workatastartup.com still a client-rendered empty shell on direct fetch; wellfound.com rendered
> but surfaced only full-time/non-internship roles outside target functions — expected, the YC
> Winter 2027 batch isn't due until ~November 2026. **Economic consulting** — Charles River
> Associates' Greenhouse board re-queried directly: still only the same EU-only (London/Brussels/
> Munich) reqs plus a US Forensic Services Billing Analyst (not internship-relevant), Summer 2027
> or ungated-by-year, unchanged. Analysis Group's careers page confirms summer-only language
> directly ("seeking full-time and summer internship opportunities"), unchanged. Compass Lexecon's
> main careers page states no timing detail and no current openings list (its Workday openings
> board isn't directly fetchable); not confirmed-empty, consistent with prior inconclusive passes.
> Brattle's careers page again gives no program-timing detail on direct fetch; its own
> Current-Openings subpage wasn't reachable this pass either — inconclusive, unchanged. **Palantir's**
> Lever board re-checked — still only the Paris and Honolulu Deployment Strategist Internship reqs,
> neither term-dated. **SimplifyJobs off-season README** spot-checked (Software Engineering section
> only, given yesterday's full 40,778-line programmatic parse already covered every category) — no
> new target-function hit in the section sampled. **BuiltIn Austin** — re-fetched directly: Cox
> Enterprises PM Intern and Itron Data Science Intern are both Summer 2027 (excluded); CrowdStrike's
> Sales Excellence/Global Programs interns are Summer 2027 and borderline-function at best. **BuiltIn
> NYC** — all visible postings are PwC/Citadel Summer 2027 reqs, wrong term. **GradConnection
> Sydney** — 17 non-TikTok postings checked; all are Australian summer-vacationer/EOI programs (EY,
> ANZ, Treasury, Allens, Jemena-Zinfra) aimed at Australian-enrolled students or starting outside
> the window (ANZ's starts Nov 2027), plus the same pay-to-play brokerages as before — none add.
> **Tokyo** — coralcap.co/jobs still 404s, the same standing access gap as every prior sweep.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-10-12** (daily sweep — **1 correction (A147 Tesla Service Program &amp;
> Project Management Intern downgraded `unverified` → `blocked`), 1 new Tier A row (A167 Dell
> Technologies Corporate Strategy Undergraduate Intern, unverified), no closures.**
>
> **Correction: A147 (Tesla, Service Program &amp; Project Management Intern, Austin).** A fresh
> programmatic parse of the SimplifyJobs off-season README (40,778 lines, downloaded and grepped
> directly, not summarized by search) found this exact req (job 283443 — the same URL already
> tracked) tagged with Simplify's standard 🎓 marker, which that platform uses to flag roles
> requiring a current Master's/advanced-degree enrollment rather than an undergrad. Tesla's own
> careers site returned `403 Forbidden` on every direct-fetch attempt this run, as it has on every
> prior attempt — the grad-only language could not be independently re-confirmed on the primary
> source itself, only inferred from the platform's tagging convention plus an exact req-ID match.
> Downgraded `unverified` → `blocked` on that basis rather than left unchanged, since the signal is
> specific (an exact req match, not a guess) even though the primary source stayed unreachable;
> kept per the never-delete rule rather than removed. Re-open this one if a direct view of the
> posting ever becomes possible and contradicts it.
>
> **New row: A167, Dell Technologies, "Corporate Strategy Undergraduate Intern," Austin, TX.**
> Found via a fresh BuiltIn/Intern Insider sweep pass, confirmed directly on Intern Insider's own
> listing page (not a search snippet): $27.10–$31.80/hr, deadline Oct 17 2026 (still open, 5 days
> out), eligibility explicitly welcomes Economics majors by name alongside Finance/CS/Engineering/
> Information Systems — a clean Strategy-function, home-market (Austin) match with an unusually
> direct econ-major callout. Added `unverified` rather than `live`: no term length, duration, or
> start date is stated anywhere on the aggregator page, and three separate attempts to locate Dell's
> own primary posting (jobs.dell.com and its enterpriseplatform.dell.com redirect target) returned
> only "page not found" — Dell's applicant site appears to be JS-rendered and not directly
> fetchable, the same access pattern seen on Tesla's and GE's career sites. Kept per the never-drop
> rule with the real Intern Insider application URL; worth confirming term structure directly
> before applying, and worth trying a browser-rendered fetch of Dell's own site on a future sweep.
>
> **Re-verification pass.** Re-verified the nearest-term-deadline/at-risk rows via direct fetch: **A93
> (NewsBreak)** — still "Actively hiring"; deadline reads "Apply by Oct 12" — **today, the hard
> cutoff** (pay range $40–60/hr not visible on this pass, could not independently confirm or refute,
> same aggregator-reliability caveat as always). Treat as closing today if not already applied. **A95
> (Parkdepot)** — still "Actively hiring," deadline unchanged (Oct 17 2026, 5 days out). **A112/A114
> (TikTok Sydney)** — both still open, closing date unchanged (30 Oct 2026, 1:59pm, 18 days out —
> inside the 3-week window), work-rights list still truncated behind "...show more" exactly as before
> — Working Holiday/subclass 462 still neither confirmed nor refuted on the rendered page. **A159
> (Wonder)** — direct Workday fetch still an empty JS shell and the CXS API guess still returns
> `403`, same as every prior attempt. New this pass: a WebSearch surfaced a likely-matching listing on
> Wonder's VC-hosted mirror (jobs.accel.com, req 92073413 — title/team/location match but not
> confirmed to be the same requisition as the tracked JR101323) showing the same $36/hr rate already
> tracked, posted Sep 3 2026, listed oddly as "full-time" employment type, and currently marked **"No
> longer accepting applications."** Still no term/cohort date anywhere on that mirror either. Kept
> `unverified` rather than flipped to `closed`: the mirror match to the exact tracked req isn't
> confirmed, so this is elevated risk, not a confirmed closure — worth a priority browser-rendered
> check of the canonical Workday link next sweep.
>
> Full re-sweep of every standing source. **YC/Wellfound** — workatastartup.com and wellfound.com
> remain client-rendered shells with zero indexed postings surfaced via direct fetch or targeted
> WebSearch (expected — the YC Winter 2027 batch isn't due until ~November 2026). **Economic
> consulting** — Analysis Group's own FAQ explicitly states no off-cycle internships (summer-only,
> June–Aug); Cornerstone Research confirmed 2027 program applications don't open until March 1, 2027
> (summer cycle only); Charles River Associates' Greenhouse board re-queried directly — still only
> three EU-only (Brussels/Munich/London) Antitrust & Competition reqs, Summer 2027, unchanged;
> Compass Lexecon, Brattle, NERA — no new postings beyond already-known Summer 2027 cycles. **Palantir's**
> Lever board re-checked — still only the Paris/Honolulu Deployment Strategist Internship reqs.
> **Uber/DoorDash/Flexport** — no Strategy & Operations or Business Operations internship at any of
> the three (Uber's University page lists only full-time Strategy/Ops roles, no term dates; DoorDash
> and Flexport searches surfaced only full-time Associate-level Strategy & Ops roles; Flexport's and
> DoorDash's own careers pages both 403'd directly, relied on Greenhouse search instead). **SimplifyJobs
> off-season README** downloaded fresh and grepped programmatically end-to-end (40,778 lines) for
> every target-city/function/term hit — this is also the source of the A147 correction above. Other
> hits, all already-tracked or excluded: GE Aerospace Data Science Co-op (already A152, same req
> R5040450); VaynerMedia Data Analytics Resident NYC Winter 2027 variant (same req as already-tracked
> A162); MTA "EAM Analyst Intern" (same Emerging Talent family as A120/A160/A161, no distinct live
> posting locatable); FOX News Media NYC Data Analytics Intern (confirmed directly: Feb 8–Apr 16 2027,
> overruns by 5 weeks, excluded); Disney "Insights and Analytics Intern" (ABC News) and "Marketplace &
> Portfolio Insights Intern" NYC (both confirmed Jan–June 2027, 6-month overrun, same pattern as
> A110's family, excluded); Tesla "Data Analyst Intern – People Products" (Palo Alto/Austin, min.
> 12-week commitment from a ~Jan start likely overruns, deadline on the Intern Insider mirror already
> read Oct 10 — passed — excluded rather than added); Domino Data Lab "Forward Deployed Engineer
> Intern" NYC (good functional fit in principle — dev-tool FDE — but the only locatable posting is
> tagged Spring **2028**, targeting Spring 2028 graduates, not the 2027 cycle; no live 2027-specific
> req found, not added); Zipline Data Analytics Intern Spring 2027 (same already-excluded Jan–Apr
> cohort as the rest of Zipline's family). **BuiltIn NYC/Austin/SF** — re-fetched directly; the only
> new find was **A167 above (Dell)**; everything else Winter/Spring-2027-tagged is Summer 2027,
> already-tracked, or wrong function (Notion/Cloudflare SWE, engineering, out of scope).
> **GradConnection Sydney** — nothing beyond already-tracked TikTok reqs and pay-to-play placement
> brokerages (Premium Graduate Placements). **Tokyo** — coralcap.co/jobs still 404s, but coralcap.co/careers
> loaded this time: 4 openings, none internships (Content Producer is content-marketing, excluded by
> function; the rest require business Japanese). japan-dev.com and tokyodev.com — the only
> non-engineering internship found (HENNGE Full-Stack Pathway) is itself engineering; no new lead.
> Madrid/Barcelona — no results on any source this pass.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-10-11** (daily sweep — **no status corrections, no new Tier A rows, no
> closures.** Re-verified the nearest-term-deadline/at-risk rows via direct fetch: **A93
> (NewsBreak)** — still "Actively hiring," deadline unchanged (Oct 12 2026, **1 day out — nearest
> deadline in the tracker**). **A95 (Parkdepot)** — still "Actively hiring," deadline unchanged (Oct
> 17 2026, 6 days out). **A112/A114 (TikTok Sydney)** — both still open, closing date unchanged (30
> Oct 2026, 1:59pm Sydney, 19 days out — inside the 3-week window), work-rights list still truncated
> behind "...show more" exactly as before. **A159 (Wonder)** — re-tried a direct fetch of the Workday
> posting; still an empty JS shell, same as every prior attempt — stays `unverified`, genuinely
> unresolved rather than untried.
>
> Full re-sweep of every standing source found nothing new that clears the bar. **YC/Wellfound** —
> workatastartup.com remains a client-rendered shell with zero visible postings on direct fetch
> (expected — the YC Winter 2027 batch isn't due until ~November 2026; note the bare domain now
> returns a `406` without an `Accept` header and `200` with one — a bot-challenge quirk, not an
> access regression, since the curl sanity check always sends one). **Economic consulting** —
> Cornerstone Research's own page was reachable this run, resolving the 2026-10-10 DNS-failure
> access gap: confirmed summer-only (Analyst/Associate categories for undergrad/grad/PhD, no
> winter/spring req). Charles River Associates' Greenhouse board re-queried directly — still only the
> three EU-only (Brussels/Munich/London) Antitrust & Competition intern/analyst reqs, Summer 2027 or
> Master's/PhD-gated, unchanged. Compass Lexecon and Brattle's own careers pages remain inconclusive
> on direct fetch (no reqs rendered in the fetched content; their Workday/current-openings subpages
> weren't reachable this pass) — not confirmed-empty, worth another look. NERA's own page confirms
> summer-only-by-policy, unchanged. **SimplifyJobs off-season README** downloaded and parsed
> programmatically end-to-end (3,131 rows across all categories) for every target-city/function/term
> hit: 16 rows matched on location+function+Winter-or-Spring-2027 tag, and all 16 are either
> already-tracked (Gemini A146, GE Aerospace A152, Zipline A123, MTA A120/A161, NBCUniversal C70) or
> already-excluded on a hard criterion (FOX NYC Data Analytics Intern and Mastercard AI & Data Co-op,
> both excluded in a prior sweep; Audax Group Data Engineer Co-op, Boston-not-NYC and overruns, same
> as before; Royal Bank of Canada's two NYC reqs are investment-banking/capital-markets analyst roles,
> wrong function; ITT's Orchard Park/Boston-NY co-op and Moog's Buffalo co-op are outside target
> metros). One genuinely new-looking lead, **Crusoe Energy's "Product Manager Intern," San
> Francisco** (Simplify tag: Winter 2026/Spring 2027/Summer 2027) — chased across three sources
> (a WorkInGreen mirror marked the listing **"Expired"** with a garbled eligibility line
> ["graduating between December 2026 Spring 2027"], an MCJ/Dragonfly mirror link 404'd, and Crusoe's
> own Ashby board showed zero open internships) — no live primary source could be found despite
> trying; excluded as stale/expired rather than added `unverified`, consistent with the quality bar
> favoring primary-source confirmation over aggregator mirrors. **Intern Insider's** Winter/Spring
> 2027 term pages spot-checked (too large to enumerate fully — 5,100 Winter + 405 Spring rows) — no
> new target-function/target-city hit found in the sampled pages; closest misses (Key Capture Energy
> Albany ops intern, wrong metro) don't clear location. **BuiltIn NYC/Austin/SF** — no new
> Winter/Spring-2027-tagged hit beyond the already-excluded VelocityEHS remote CX intern and
> Cloudflare SWE intern (both noted 2026-10-10). **GradConnection Sydney** — nothing beyond
> already-tracked TikTok reqs and pay-to-play placement brokerages (Premium Graduate Placements,
> Nestlé YEP) — not recommended as genuine leads. **Tokyo** — coralcap.co's `/jobs` path still 404s
> (standing access gap, unchanged for months); tokyodev.com returned a 403 this run (new, isolated —
> not one of the five sanity-check domains, no broader access issue indicated); japan-dev.com's
> non-engineering hits (Polymer Capital trading-systems support, Qubitcore R&D PM) are both
> technical/senior, not internships.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 200 with a browser
> `Accept` header — see note above; wellfound.com 200, simplify.jobs 200, job-boards.greenhouse.io
> 302, www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-10-10** (daily sweep — **no status corrections, no new Tier A rows, no
> closures.** Re-verified all four at-risk/near-term-deadline rows via direct fetch: **A93
> (NewsBreak)** — still "Actively hiring," deadline unchanged (Oct 12 2026, **2 days out** — nearest
> deadline in the tracker). **A95 (Parkdepot)** — still "Actively hiring," deadline unchanged (Oct 17
> 2026, 7 days out). **A112/A114 (TikTok Sydney)** — both still open, closing date unchanged (30 Oct
> 2026, 1:59pm Sydney, 20 days out — inside the 3-week window).
>
> Full re-sweep of every standing source, via three parallel passes, found nothing new that clears
> the bar. **YC/Wellfound/Simplify** — workatastartup.com and wellfound.com remain client-rendered
> shells/empty of internship listings on direct fetch (expected — the YC Winter 2027 batch isn't due
> until ~November 2026); simplify.jobs' Top-Winter-and-Spring list rendered 30 live postings, none in
> target function or location. **Economic consulting &amp; strategy** — Analysis Group, Brattle, and
> NERA direct careers pages unchanged/summer-only; Charles River Associates' Greenhouse board (92
> reqs) has three new intern reqs but all EU-only antitrust/competition (London/Brussels/Munich,
> Summer 2027) — wrong metro and cycle, not added; Compass Lexecon's own page surfaced nothing new;
> Palantir's Lever board still shows only the already-tracked Paris/Honolulu Deployment Strategist
> Internship reqs; Flexport has zero intern titles, Uber/DoorDash's Greenhouse boards remain
> unreachable at their standard tokens. **Cornerstone Research's own site was unreachable this run
> (DNS failure)** — a genuine access gap, not confirmed-empty; retry next sweep. **SimplifyJobs
> off-season README** parsed programmatically for every target hit: the only new candidate worth
> naming is **Zipline's Spring 2027 cohort** (Data Analytics Intern, Commercial Strategy &amp;
> Operations Intern, and others, South SF/Austin) — excluded on a confirmed hard fact: Zipline's own
> posting states the Spring 2027 cohort runs "January to April," overrunning the Mar 12 hard stop by
> roughly 3 weeks. Other new-looking hits (Faire Applied AI/ML Scientist Intern, American Heart
> Association Data Science Intern, Together AI Systems Research Engineer Intern, Composio Forward
> Deployed Engineering Internship) all excluded on function (ML/engineering, not analytics/
> commercial) or location. **BuiltIn NYC/Austin/SF** — the only new Winter/Spring-2027-tagged hits
> (Cloudflare SWE Intern, VelocityEHS remote CX Intern) are wrong function or overrun (Jan–Apr, 14–16
> weeks). **GradConnection Sydney** — nothing beyond already-tracked TikTok reqs. **Tokyo**
> (coralcap.co, japan-dev.com, tokyodev.com) — coralcap.co's jobs path still 404s (standing access
> gap, unchanged for months); two plausible-looking japan-dev/tokyodev hits (Omakase Robotics,
> Polymer Capital) both confirmed full-time/senior, not internships.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-10-09** (daily sweep — **no status corrections, no new Tier A rows, no
> closures.** Re-verified every near-term-deadline and at-risk row via direct fetch: **A93
> (NewsBreak)** — still "Actively hiring," deadline unchanged (Oct 12 2026, **3 days out** — inside
> the 3-week window, the nearest deadline in the tracker). **A95 (Parkdepot)** — still live, deadline
> unchanged (Oct 17 2026, 8 days out — inside the 3-week window). **A112/A114 (TikTok Sydney)** —
> both re-opened directly, closing date unchanged (30 Oct 2026, 1:59pm Sydney — 21 days out, right at
> the edge of the 3-week window). **A159 (Wonder)** — tried a fresh WebFetch-rendered pass at the
> Workday posting in addition to a direct fetch; still returns an empty JS shell, same as every prior
> attempt this cycle — stays `unverified`, genuinely unresolved rather than untried. Spot-checked a
> sample of plain `live` rows not directly re-touched in recent sweeps: **A22 (CertiK)**, **A98
> (Cresta)**, **A153 (Contoro Robotics)** — all confirmed unchanged (pay, location, mode, open status
> all match the tracker).
>
> Full re-sweep of every standing source found nothing new that clears the bar. **YC/Wellfound**
> remain client-rendered shells on direct fetch (expected — the YC Winter 2027 batch isn't due until
> ~November 2026); targeted search surfaced nothing new in scope. **Economic consulting** — Analysis
> Group, NERA, and Brattle searched directly: every current posting found is Summer 2027 only
> (Analysis Group Boston/Montreal Summer Analyst reqs, NERA London Summer Intern 2027); Cornerstone
> Research and Compass Lexecon returned no new hits at all this run. **SimplifyJobs off-season
> README** downloaded and parsed programmatically end-to-end (251 PM + 2,007 Data Science rows) for
> every target-city/function/cycle hit: besides rows already tracked, the only candidates surfaced
> were excluded on hard criteria — a Stripe **"PhD Data Scientist, Intern"** sibling to already-
> tracked A166 (explicitly PhD-program-only, excludes an undergrad, not added); an MTA "Technology
> Support, Emerging Talent Intern" tagged Spring 2027 on Simplify, but the only confirmable posting
> under that exact title is tagged **Fall**, not Spring, and no verifiable Spring-dated posting could
> be found at all — didn't clear the bar for even an `unverified` row given no real link exists, not
> added; and two Disney "Insights and Analytics" variants (Marketplace & Portfolio Insights Intern,
> and an ABC News variant), both independently confirmed via search to run **January–June 2027**, the
> same 6-month overrun that already excludes A110's family — not added. **Palantir's** Lever board
> re-checked — still only the Paris/Honolulu/2026-grad-only Deployment Strategist Internship reqs, no
> new target-metro req. **Uber** — only a 2026-cycle "Operations & Logistics Intern" surfaced (wrong
> year, wrong metros, July/Dec 2027 grad-only eligibility); **DoorDash** — only a full-time Strategy &
> Operations Associate role, not an internship; **Flexport** — nothing. **BuiltIn NYC/Austin/SF** —
> the one explicit "Winter 2027" hit (Friedom Partners "AI Systems Analyst," remote, investment-firm
> analyst role) is outside target functions, not added. **GradConnection Sydney** — nothing beyond
> already-tracked TikTok reqs and citizen/PR-gated graduate programs. **Tokyo** (coralcap.co,
> japan-dev.com, tokyodev.com) — coralcap.co's `/jobs` path still 404s (standing access gap, unchanged
> from every prior sweep); the one promising-looking lead, a TikTok Tokyo GBS "Business
> Intelligence/Analysis Project Intern," explicitly requires business-level Japanese — excluded on
> language grounds, consistent with every prior Tokyo GBS finding.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-10-08** (daily sweep — **no status corrections; two rows re-verified with notes
> strengthened (A152 GE Aerospace, A163 Fenwick &amp; West — both stay `unverified`), 3 new Tier A
> rows (A164 Energy and Environmental Economics "E3" Consulting Internship, conflict; A165 Figma
> Data Science Intern, unverified; A166 Stripe Data Analyst Intern, unverified), no closures.**
>
> **Re-verification pass.** **A112/A114 (TikTok Sydney)** — both tracked GradConnection URLs
> re-opened directly: closing date unchanged at 30 Oct 2026, 1:59pm Sydney on both, no drift (22
> days out — inside the 3-week deadline window). **A152 (GE Aerospace)** — the Workday page renders
> as an empty JS shell on direct fetch, but its CXS JSON API confirmed directly: `timeType: "Full
> time"` — the full-time classification is now *confirmed*, not merely suspected as in the
> 2026-09-23 entry. Still no explicit term length or start/end date anywhere in the posting itself
> (the `jobPostingEndDateAsText` field is the application-posting expiry, not the internship term —
> not conflated). Kept `unverified` rather than downgraded to `conflict`: full-time hours during a
> short co-op don't by themselves overrun 12 Mar, and no date confirms an overrun; the real open
> question (exact term length, and whether it tolerates concurrent light enrollment) stays
> unresolved — worth asking directly. **A163 (Fenwick &amp; West)** — same JS-shell-on-page /
> working-CXS-API pattern; the API confirmed verbatim: "This is a part-time, non-exempt role
> expected to run through fall of 2026 and into winter of 2027." No other cohort-timing language
> exists anywhere in the source — the mid-cohort-vs-fresh-January-start question is genuinely
> unanswerable from the posting itself, not just missed on a prior pass. Also confirmed unchanged:
> still open (`canApply: true`), part-time min. 16 hrs/wk, $21–25/hr. Kept `unverified`. **A159
> (Wonder)** — the human-readable page is still an empty JS shell, and this sweep additionally tried
> the same Workday-CXS-API route that worked for A152/A163 — this tenant returns `HTTP 403 {errorCode:
> "S22", message: "permission denied"}` on every attempt (varied UA/referer/cookies), unlike GE's and
> Fenwick's tenants. The Winter-2026-vs-Jan-2027-cycle question remains fully unresolved; a
> browser-rendering fetch is still the only path left untried. No change — stays `unverified`. **A93
> (NewsBreak)** and **A95 (Parkdepot)** — neither row carries a direct URL precise enough to
> re-locate the exact tracked listing via search this pass (multiple NewsBreak/Nearby.ai and
> Parkdepot-adjacent postings turned up, none matching the tracked req); both Oct-2026 deadlines
> (NewsBreak Oct 12, now 4 days out; Parkdepot Oct 17, now 9 days out) stay unconfirmed either way —
> not treated as lapsed, not treated as reconfirmed. Resolve with a browser-rendered fetch of the
> tracked URLs directly next run.
>
> **New row: A164, Energy and Environmental Economics, Inc. ("E3") "2027 Consulting Internship."**
> Boutique energy/climate-policy economics consulting firm — a peer, if narrower-niche, addition to
> the named econ-consulting lane. Found via general search after an InternInsider snippet 404'd;
> confirmed directly on E3's own Lever board (jobs.lever.co/ethree), not a snippet. 8–12 week
> consulting internship on electricity-market topics (renewables, rate design, transmission, climate
> policy) supporting consultants' live client work; economics is explicitly named as a welcome major
> alongside science/engineering/business/public policy. Added `conflict` rather than `live`: E3's own
> posting states its hiring cycle runs "September through early 2027, with interviews in January and
> decisions in February" — if an offer doesn't land until February, an 8–12-week term starting then
> overruns 12 Mar by weeks; the posting's "flexible dates" language describes which of Spring/Summer/
> Fall cohort a student joins, not a guaranteed Jan start. Kept per the never-drop rule — the posting
> explicitly invites candidates to propose their own dates, so a direct early application disclosing
> Jan 4 availability is still worth trying. No pay rate stated beyond "full time hourly." Calgary
> office would need separate Canadian work authorization — stick to the three US offices.
>
> **New row: A165, Figma "Data Science Intern (2027)."** Found via a fresh SimplifyJobs off-season
> README parse (Data Science section), confirmed directly on Figma's own Greenhouse board. SQL/
> Python/R-based quantitative analysis connecting data findings to product decisions — a clean Data-
> function fit with skills-based (not major-gated) eligibility. Pay confirmed directly: $46/hr plus a
> housing stipend and travel reimbursement — a real relocation-supported internship, not local-only.
> Added `unverified`: the posting states no season, term length, or start/end date anywhere, only an
> "expected graduation date" field on the application form, so a Jan–Mar 2027 fit is not confirmed
> either way — not on inability to open the posting, which opened cleanly. Mode assumed in-person
> (relocation support implies onsite) rather than confirmed.
>
> **New row: A166, Stripe "Data Analyst, Intern."** Found via the same README parse, confirmed
> directly on Stripe's own careers board — the clearest API/dev-tool-company Data-function match in
> PROFILE.md's named-ideal-company category. Eligibility explicitly targets expected graduation
> December 2027 or spring/summer 2028 — matches Sam's Class-of-2028 track precisely; qualifying
> skills (SQL, cross-functional collaboration, AI-tool proficiency) are a clean fit. Two real,
> unresolved caveats kept this `unverified` rather than `live`: (1) the posting states a single
> $117,000/yr figure in its base-salary field — an annual-salary framing unusual for a fixed-term
> internship, suggesting this may be an evergreen/year-round req rather than a dated Jan–Mar 2027
> cohort slot; (2) no term length or start/end date is stated anywhere on the posting. Kept per the
> never-drop rule — worth a direct question about term structure before applying.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-10-07** (daily sweep — **1 real correction (A160 MTA Ridership downgraded
> `unverified` → `blocked` on confirmed grad-only eligibility), 3 new Tier A rows (A161 MTA EAM
> Value Realization, live; A162 VaynerMedia Resident - Data Analytics, conflict; A163 Fenwick &amp;
> West Forward Deployed Operations Intern, unverified), no closures.**
>
> Re-verified every at-risk Tier A row via direct fetch: **A93 (NewsBreak)** — still "Actively
> hiring," deadline unchanged (**Oct 12 2026, 5 days out — inside the 3-week window**); the posting
> also describes a "rolling term structure," so the Oct 12 date may function as a soft cutoff rather
> than a hard one — treat the 5-day window with some caution. **A95 (Parkdepot)** — still live,
> deadline text unchanged (**Oct 17 2026, 10 days out — inside the 3-week window**); caveat: the
> page shows "Posted 170 days ago," long enough that the Oct 17 deadline string could be a
> stale/evergreen template value rather than a true hard date — couldn't independently resolve this
> run, flagging for awareness rather than treating as a correction. **A96 (Crowe Global)** — still
> live, no deadline, pay/location/mode unchanged ($27–42/hr, Austin, In-Office). **A121 (Ankura)** —
> the Workday CXS API (req R104943) queried directly again: `canApply: true`, same $34/hr, same Dec
> 2027–June 2028 grad-window eligibility, rolling, unchanged. **A112/A114 (TikTok Sydney)** — both
> re-confirmed open directly, closing date unchanged (30 Oct 2026, 1:59pm Sydney — 23 days out, just
> outside the 3-week window but close enough to keep watching). **A159 (Wonder)** — stays
> **unverified**: the Workday CXS API endpoint now returns a 403 (bot-protected, unlike Ankura's
> equivalent endpoint) and the human-readable page is a JS shell on direct fetch — could not resolve
> whether this req targets the Jan–Mar 2027 cycle or an older "Winter 2026" cycle; needs a
> browser-rendering fetch to settle.
>
> **Correction: A160 (MTA, Ridership Analysis and Modeling) downgraded `unverified` → `blocked`.**
> A second, independent direct fetch (not browser-rendered this time) reproduced the exact same
> result as the 2026-10-06 finding: only a $21/hr grad pay tier appears on the page, with the
> eligibility line reading "matriculated in a graduate program in good standing with at least a 2.8
> GPA" — no undergrad tier or alternate GPA line anywhere on the page. This sweep also turned up a
> genuine sibling req (A161, below) that explicitly carries both a $19/hr undergrad and $21/hr grad
> tier on its own primary source — confirming A160's single-tier eligibility language is a real,
> distinguishing feature of this specific req rather than a fetch/rendering artifact. Fit lowered
> ~3 → ~1; kept per the never-delete rule.
>
> **New row: A161, MTA "EAM Value Realization, Emerging Talent Intern (Spring)"** — a third,
> distinct req in the same "Emerging Talent" program family as A120 (EAM Analyst) and A160 (Ridership
> Analysis). This resolves the 2026-10-04 sweep's open item, which had flagged a similarly-named MTA
> req as "near-certainly the same program as A120... couldn't independently confirm as distinct, not
> added" — confirmed via direct fetch to be a real, separate Jobvite posting (job/orDQAfwe). Both pay
> tiers confirmed on the primary source ($19/hr Undergrad, 2.5 GPA / $21/hr Grad, 2.8 GPA) — unlike
> A160. Added `live`, matching A120's own bar (primary source confirmed real/open/in-person/NYC;
> exact start/end dates still unstated on the posting itself, same "Confirm ≤ Mar 12" treatment as
> A120).
>
> **New row: A162, VaynerMedia "Resident - Data Analytics"** — found via the SimplifyJobs off-season
> README, opened directly on VaynerMedia's own Greenhouse board (gh_jid=8126062). NYC HQ, hybrid
> (3–4 days/wk onsite), $20/hr ($30/hr OT), strong growth/marketing-analytics function fit. Added
> `conflict` rather than live: the posting describes a fixed three-month "residency" program with
> "the next residency class" starting January 2027 — a literal 3 months from an early-Jan start runs
> into early April, past the Mar 12 hard stop by roughly 2–3 weeks, and an agency's own named cohort
> program reads as less negotiable than a startup's rolling hire. Real application URL kept; disclose
> the Jan 4–Mar 12 window immediately in case they'd consider a shorter slice.
>
> **New row: A163, Fenwick &amp; West "Forward Deployed Operations Intern"** — found via the
> SimplifyJobs off-season README, opened directly on Fenwick's own Workday board (req R2964).
> AI-native workflow tooling for BD/competitive-intelligence/legal-ops strategy at an AmLaw 100 firm;
> candidate's choice of office including New York and Silicon Valley/SF (also Boston/Seattle/Santa
> Monica/DC); part-time, in-office "on occasion" (commuting distance required, not daily onsite);
> $21–25/hr confirmed directly. Eligibility language explicitly welcomes "quantitative social science
> such as economics" alongside CS/data science/industrial engineering — an unusually direct fit for
> the econ+stats profile, and a notable brand name. Added `unverified` rather than dropped: the
> posting states the role is "expected to run through fall of 2026 and into winter of 2027," which
> reads like one continuing cohort rather than a fresh January intake, and it's unclear whether a
> Jan-2027 starter would join mid-cohort or a new cohort begins then — confirm the actual start/end
> structure directly before applying.
>
> Full re-sweep of every standing source, two parallel passes. **YC/Wellfound** remain
> client-rendered shells on direct fetch; targeted search surfaced nothing new in scope (expected —
> the YC Winter 2027 batch isn't due until ~November 2026). **Economic consulting** — Charles River
> Associates' Greenhouse board re-queried directly: still only the already-excluded College Station
> TX / Tallahassee FL Labor &amp; Employment analyst req (JR 8243522); Analysis Group, Cornerstone,
> Compass Lexecon, Brattle, NERA direct careers pages unchanged/inconclusive on direct fetch, same as
> every prior sweep. **SimplifyJobs off-season README** parsed programmatically end-to-end (253 PM +
> 2,001 Data Science rows) for every target-city/function/cycle hit — besides A161–A163 above,
> several plausible-looking leads were opened directly and excluded on hard criteria: KQED SF
> Audience Intelligence Intern (Jan 19–Jun 25 2027, overruns), FOX News Media Data Analytics Intern
> NYC (Feb 8–Apr 16 2027, overruns), Mastercard "AI &amp; Data Co-Op" (Northeastern-University-
> restricted, plus runs to May 2027 — double exclusion), Vialto Partners Client Technology Services
> Intern (mid-Jan–mid-Apr 2027, overruns), Audax Group Data Engineer Co-op (Boston not NYC as
> mislabeled on Simplify, Jan 4–Jun 25 2027, overruns — already excluded in a prior sweep,
> re-confirmed). **Intern Insider's** Winter/Spring 2027 term pages re-fetched, zero
> target-function/target-city hits on this pass. **BuiltIn NYC/Austin/SF** `/jobs/internships` — no
> new Winter/Spring-2027-tagged postings beyond what's tracked. **GradConnection Sydney** — only
> pay-to-play placement brokerages and a full-time (not internship) Accenture program surfaced;
> nothing new. **Tokyo** (coralcap.co, japan-dev.com, tokyodev.com) — coralcap.co's jobs path still
> 404s (standing access gap, not confirmed-empty); japan-dev/tokyodev nothing new
> non-engineering/English-accessible. **Palantir's** Lever board re-queried directly (74 reqs) —
> still only the Paris and Honolulu Deployment Strategist **Internship** reqs; the Madrid/NYC/
> Chicago/Tokyo "Deployment Strategist" reqs on the same board are full-time, not internships.
> **Uber/DoorDash** still return zero postings at their Greenhouse tokens; **Flexport** (198 reqs)
> has zero "intern" titles.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-10-06** (daily sweep — **no status corrections, 1 note-only correction, 1 new
> Tier A row (A160 MTA, unverified), no closures.** Re-verified every at-risk Tier A row via direct
> fetch: **A93 (NewsBreak)** — still "Actively hiring," deadline unchanged (Oct 12 2026, 6 days out),
> requirements unchanged (3+ yrs growth-engineering experience, BS/MS/PhD CS — the senior-level bar
> already reflected in its low Fit score). **A95 (Parkdepot)** — still live, deadline unchanged (Oct
> 17 2026). **A96 (Crowe Global)** — still live, no deadline, pay/location/mode unchanged ($27–42/hr,
> Austin, In-Office). **A121 (Ankura)** — the Workday CXS API (req R104943) queried directly again:
> `canApply: true`, still no deadline field, same eligibility window (Dec 2027–June 2028 grads); the
> page-render issue flagged 2026-10-05 doesn't affect the API route. **A112/A114 (TikTok Sydney)** —
> both re-opened directly via curl+browser-UA; closing date reconfirmed unchanged (30 Oct 2026, 1:59pm
> Sydney) via both the static "Closing Date:" text and the campaign's embedded JSON `interval` field.
> **Note-only correction:** the work-rights truncation caveat standing since 2026-10-04/05 is now
> resolved — the full list is not actually cut off at the data layer, and both reqs explicitly name
> "Australian Working Visa," confirming subclass-462 eligibility as previously inferred rather than
> directly observed. Both dashboard notes updated to record this; no status change (both stay `live`).
>
> **New row: A160, MTA "Ridership Analysis and Modeling, Emerging Talent Intern (Spring)"** — found
> via the SimplifyJobs off-season README's Data Science section, same "Emerging Talent" program
> family as already-tracked A120 but a distinct req (transportation ridership data analysis/modeling,
> NYC, In-person). Added `unverified` rather than `live`: the Jobvite posting is a client-rendered
> shell on direct curl, so a browser-rendering fetch was used instead, and it reported a "matriculated
> in a graduate program, 2.8 GPA" eligibility line with only a $21/hr grad pay tier (no undergrad tier
> shown, unlike A120's sibling req) — if accurate, this would exclude Sam on class-standing grounds;
> flagged explicitly rather than dropped, confirm directly before applying.
>
> Full re-sweep of every standing source: `workatastartup.com`/`wellfound.com` WebSearched directly
> (targeted queries for spring/winter 2027 growth/BD/strategy/founder's-associate roles) — all hits
> either already tracked or Summer 2027. Economic consulting — Charles River Associates' Greenhouse
> board re-queried via its public API (90 live reqs): the only Winter/Spring 2027 req remains the
> already-excluded College Station TX/Tallahassee FL Labor & Employment analyst intern (Summer/Fall
> 2027-grad requirement, non-target metro), unchanged since 2026-09-30. Compass Lexecon, Analysis
> Group, Cornerstone, Brattle, NERA direct careers pages re-checked (Analysis Group's and Cornerstone's
> own pages fetched directly this run) — all still summer-only/no distinct off-cycle posting. Palantir's
> Lever board queried directly (316 reqs) — still only the Paris and Honolulu (US-gov) Deployment
> Strategist Internship reqs, no target-metro req. Uber and DoorDash's Greenhouse boards both return
> zero postings at those tokens (consistent with them not running a public Greenhouse board there);
> Flexport's board (197 reqs) has zero "intern" titles. SimplifyJobs off-season README parsed
> programmatically end-to-end (251 PM + 1,985 DS rows) for every target-city/Winter-or-Spring-2027 hit:
> besides A160 above, the only other plausible-looking leads were a Cloudflare "People Analytics Data
> Engineering Intern (Winter/Spring 2027)," Austin — opened directly on Greenhouse and excluded on
> **two** independent grounds (requires "currently enrolled in a graduate program," and its own "12
> week internship, January - May" term runs seven weeks past the Mar 12 hard stop) — and a Google "Data
> Analytics Apprenticeship, February 2027 Start" — excluded on its own stated terms ("not currently
> enrolled in... a Bachelor's... degree program," plus an application deadline of Sept 21 2026 already
> passed). Intern Insider's Winter-2027 and Spring-2027 term pages fully re-enumerated — no new
> non-engineering, target-function, in-window hit beyond what's already tracked or excluded (E3
> Consulting's graduating-this-year requirement, same as prior sweeps). BuiltIn NYC/Austin/SF's
> `/jobs/internships` pages checked directly — all Winter/Spring-2027-labeled hits are either already
> tracked (Crowe) or wrong function/cycle; the Cloudflare DE role surfaced here too, same exclusion.
> GradConnection's Sydney business-and-commerce listing re-enumerated — no new non-TikTok/EY/DT
> Infrastructure candidate; EY's Vacationer Program reqs remain AU-citizenship/PR-gated (excluded,
> unchanged). Tokyo boards (coralcap.co, japan-dev.com, tokyodev.com) — no new non-engineering,
> English-accessible lead surfaced this run.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-10-05** (daily sweep — **no corrections, 1 new Tier A row (A159 Wonder,
> unverified), no closures.** Re-verified the two nearest-term deadlines via direct fetch: **A93
> (NewsBreak)** and **A95 (Parkdepot)** — both still live, deadlines unchanged (Oct 12 / Oct 17 2026),
> no drift. Also re-confirmed **A96 (Crowe Global)** still live/open (no deadline), and both reopened
> **A112/A114 (TikTok Sydney)** rows still live, closing 30 Oct 2026 1:59pm Sydney unchanged — the
> work-rights "...show more" truncation listing subclass 462 explicitly still could not be resolved on
> a static fetch (only Australian PR/Bridging visa visible before the cut); treated as unconfirmed,
> not a new risk, same caveat as 2026-10-04. **A121 (Ankura)** — the Workday posting returned blank
> on this run (JS-rendered, no bot-block message); could not independently verify, left unchanged
> pending a better access method.
>
> **New row: A159, Wonder** — Growth & Marketing Analytics Intern, New York NY, hybrid (3 days/wk,
> up to 5), $36/hr, found via Simplify's off-season list and opened directly on Wonder's own Workday
> board. Role, pay, location, and mode confirmed; the posting itself states no explicit start/end
> date (only generic "first 30/60 days" onboarding language) and Simplify's own tag reads "Winter
> 2026," which may mean this exact req predates the 2027 cycle — added as `unverified` rather than
> `live` on that ambiguity, real application URL kept, Fit provisional given strong function match
> (growth/marketing analytics is a top-priority fit for the econ+stats profile). Flag the Jan 4–Mar 12
> 2027 window explicitly in the first conversation per the disclosure rule.
>
> Full re-sweep of every standing source, two parallel passes. **Pass 1 (YC/Wellfound/economic
> consulting/Simplify):** workatastartup.com and wellfound.com remain client-rendered shells for
> direct fetch — no non-engineering target-function hit beyond what's already tracked. Compass
> Lexecon's Workday re-confirmed its only req ("2027 Analyst Interns – US") is Summer 2027 (June–Aug),
> unchanged. Analysis Group, Cornerstone, Brattle, NERA direct careers pages remain
> summer-only/inconclusive on direct fetch, unchanged. Charles River Associates' Greenhouse board has
> a new posting, **"Analyst Intern (Labor & Employment) – Winter/Spring 2027"** (JR 8243522, posted
> 2026-09-30) — College Station TX / Tallahassee FL (not a target metro), runs into early May 2027
> (past the Mar 12 hard stop), and requires Summer/Fall 2027 graduates (current seniors) — excluded on
> all three counts, not added. A Gemini "Product Management Intern (Winter 2027)" lead resurfaced from
> Simplify but is already tracked as **A146** (same Greenhouse req, same Jan–Apr 2027 overrun, already
> `conflict`) — not re-added.
>
> **Pass 2 (BuiltIn/Intern Insider/GradConnection/Tokyo):** BuiltIn NYC/Austin/SF — the one
> Winter-2027-labeled hit found (Capital One's "Intern, Data Analytics Engineering – Winter 2027") is
> based in Toronto, Canada, requiring Canadian work rights — excluded. Intern Insider's Winter/Spring
> 2027 term pages fully re-enumerated; one plausible hit, **Energy and Environmental Economics (E3)
> Consulting Internship**, requires candidates graduating within the year (already excluded, same
> eligibility pattern as already-tracked A145's sibling) — not added. GradConnection Sydney — two new
> **Gradability** "internship" listings found are pay-to-play placement brokerages ($450 upfront +
> $500/mo for 3 months to be placed with a host company, not a direct paid role); not recommended as
> genuine leads, left out. Tokyo boards (coralcap.co, japan-dev.com, tokyodev.com) — coralcap.co's
> jobs path still 404s; japan-dev/tokyodev non-engineering postings remain either
> Japanese-fluency-required or full-time experienced-hire — no change.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-10-04** (daily sweep — **2 corrections (both reopenings), no new rows, no
> closures.** **A112 (TikTok, Client Solution Intern) and A114 (TikTok, AI Product Manager Intern)**
> — both Sydney reqs, previously marked `closed` after lapsing 30 Sep 2026, were found reopened under
> new GradConnection URLs (`-3`/`-4` suffix for A112, `-2` for A114), new closing date confirmed
> directly: **30 Oct 2026, 1:59pm Sydney**. Both flipped `closed` → `live`, links updated to the new
> reqs. One caveat: the new reqs' work-rights list is truncated on the page (shows "ACCEPTS
> INTERNATIONAL: Yes" but the full visa list is behind a "...show more" that didn't resolve) — the
> same employer/campaign named the Australian Working Visa (subclass 462) explicitly on the prior
> (now-superseded) reqs, so this isn't flagged as a new risk, but worth a direct re-check next sweep.
>
> Re-verified the two nearest-term deadlines via direct fetch: **A93 (NewsBreak)** and **A95
> (Parkdepot)** — both still open, deadlines unchanged (Oct 12 / Oct 17 2026), locations/pay/mode
> match the tracker. No drift.
>
> Full re-sweep of every standing source found nothing new that clears the bar, run via two parallel
> passes. **Pass 1 (YC/Wellfound/economic consulting/Simplify):** `workatastartup.com` and
> `wellfound.com/jobs` remain client-rendered shells for direct fetch — targeted searches against both
> surfaced only already-tracked or out-of-window hits. Economic consulting firms (Analysis Group,
> Cornerstone, Charles River Associates' Greenhouse board, Compass Lexecon, Brattle, NERA) unchanged
> from the 2026-10-03 findings; Brattle's careers page and NERA's students page were inconclusive
> (bot-gated / 404) rather than confirmed-empty — worth another direct look. `simplify.jobs` and the
> SimplifyJobs off-season README (parsed programmatically end-to-end, 251 PM + 1,971 Data Science/AI/ML
> rows filtered to target cities) turned up nothing new: a Disney NYC "Marketplace & Portfolio
> Insights Intern" confirmed Jan–Jun 2027 (same overrun pattern as A110's family, not added), an MTA
> "EAM Value Realization" req that's near-certainly the same program as already-tracked A120 under a
> reworded title (careers.mta.org 403'd, couldn't independently confirm as distinct — not added), and
> a Wurl Data Science Intern that's Winter 2026 (wrong cycle) and PhD/MSc-only. Palantir's Lever board
> returned zero Deployment Strategist Internship results this run (previously showed Paris/Honolulu) —
> no target-metro req either way. Uber/DoorDash/Flexport: only Summer 2026 postings found; their
> 2027–2028 cycle isn't posted yet in off-cycle form.
>
> **Pass 2 (BuiltIn/Intern Insider/GradConnection/Tokyo):** BuiltIn NYC/Austin/SF candidate roles are
> all Summer 2027 cohort or wrong-function. Intern Insider's Winter-2027 and Spring-2027 term pages
> fully enumerated — Figure's Supply Chain Analytics Intern (Jan–Apr 2027, rising-senior-only, double
> exclusion) and Gemini's Prediction Markets Operations Intern (Jan–Apr 2027, same overrun as A146)
> both checked and excluded; Dispatch's Mission Operations Intern is real but pure aerospace-ops
> engineering, wrong function. GradConnection Sydney re-confirmed DT Infrastructure and SW Australia
> both explicitly require AU citizenship/PR/graduate-visa (excluded) — no change. Tokyo boards
> (japan-dev.com, tokyodev.com) remain engineering-first; the non-engineering hits found (Channel BD,
> Treasure Data/AI Solutions Architect/PM roles, PayPay/Mercari/Kraken data analyst roles) are all
> full-time, experienced-hire, and/or business-Japanese-required — not internship candidates.
> coralcap.co's jobs-board path 404'd this run — a genuine access gap, not a confirmed-empty result,
> worth retrying next sweep.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-10-03** (daily sweep — **no corrections, no new rows, no closures.** Re-verified
> all six rows with the nearest-term risk via direct fetch: **A93 (NewsBreak)** and **A95
> (Parkdepot)** — both still open, deadlines unchanged (Oct 12 / Oct 17 2026 respectively; both now
> sit inside the 3-week window from today and are the nearest deadlines in the tracker — **A95 is the
> only one not already queued/applied**). **A96 (Crowe Global)**, **A151 (Kroll)**, **A153 (Contoro
> Robotics)**, **A98 (Cresta)** — all confirmed still live, no field drift (location, mode, pay, dates
> all match).
>
> Full re-sweep of every standing source found nothing new that clears the bar. **Economic
> consulting** — Analysis Group and Cornerstone Research still summer-only/final-year-only; Charles
> River Associates' Greenhouse board (queried directly, correct slug `charlesriverassociates`, 89 live
> reqs) resolves the standing watch-item from the 2026-10-02 note: its **"Analyst Intern (Labor &
> Employment practice) – Winter/Spring 2027"** req (College Station, TX / Tallahassee, FL,
> Jan–May 2027, 20–25 hrs/wk) is real and timing-compatible, but explicitly requires candidates
> **"graduating Summer/Fall 2027"** (i.e. a current senior, not a rising junior) and neither location
> is a target metro — disqualified on eligibility, not added. Compass Lexecon's Workday board (28
> live reqs) re-confirmed the already-tracked Madrid req (A154) unchanged, plus a new **"2027 Analyst
> Interns – US"** req (JR261385, Chicago/NYC/Boston/LA/DC, $50/hr, eligible at Sam's class year) —
> but it's explicitly Summer 2027 (June–Aug), out of window. Brattle (51 reqs) and NERA (board
> currently empty; NERA's own page states summer/final-year-only by policy) unchanged. **Palantir's**
> Lever board (319 reqs, queried directly) still shows only the Paris and Honolulu (US-gov,
> clearance-required) Deployment Strategist Internship reqs — no NY/SF/Austin req. Uber, DoorDash,
> and Flexport checked directly — no Strategy & Ops or general internship reqs in the target window
> (DoorDash's board is Cloudflare-protected and could only be checked via search, lower confidence).
>
> `workatastartup.com` and `wellfound.com` swept via targeted WebSearch plus direct fetch of
> individual postings (both sites' browse/search UIs remain client-rendered shells) — all leads found
> were either already tracked or excluded on a hard criterion: FOX News Media and Disney NYC data
> internships both confirmed via direct fetch to run into April/June, past the cutoff; Weekday (YC)
> Account Manager Intern requires senior class standing; Wardstone (YC) is LA-based with a
> military-background preference; Axo Longevity (Barcelona) is majority content/creative production,
> landing on the excluded side of the social-media line. `simplify.jobs` and the SimplifyJobs
> off-season README re-checked, no new non-engineering listings. **BuiltIn NYC/Austin/SF** — all
> candidate roles are Summer 2027 cohorts (PwC, CrowdStrike, Atlassian, Capital One, etc.) or already
> tracked (A149 MetLife). **GradConnection Sydney** — the two non-TikTok/EY/Treasury candidates found
> (SW Australia, DT Infrastructure) both explicitly require Australian citizenship/PR/graduate-visa,
> excluding a subclass 462 holder. **Tokyo** (coralcap.co, japan-dev.com, tokyodev.com) — confirmed
> again these remain engineering-first; the one non-technical-adjacent English-friendly listing found
> (japan-dev BD role) requires Japanese fluency and residency.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-10-02** (daily sweep — **3 status corrections, no new rows, no closures.**
> Corrections: **A93 (NewsBreak)** and **A95 (Parkdepot)** — both re-opened and confirmed directly
> (not just a search snippet) via Intern Insider: postings, deadlines (Oct 12 / Oct 17 2026), pay, and
> requirements all still match the tracker exactly; upgraded `unverified` → `live` now that both are
> independently confirmed. **A121 (Ankura)** — re-queried the Workday CXS API directly (req R104943)
> for the second time running; still open (`canApply: true`), still no deadline field, same $34/hr and
> Dec 2027–June 2028 graduation-window eligibility as previously recorded. No change, but resolves the
> prior sweep's "flagged for a direct CXS-API recheck" note.
>
> Also checked and ruled out: a general-purpose research pass flagged **A112/A114 (TikTok Sydney)** as
> possibly reopened, based on a gradconnection search snippet reading "Accepts International." Opened
> both postings directly — both still show "Closed · Closed 2 days ago," closing date 30 Sep 2026 1:59pm
> unchanged; the snippet was stale search-index data, not a reopening. Not re-flipped. Also surfaced an
> **EY 2026/27 Vacationer Program (Economics)**, Sydney/Brisbane/Canberra/Melbourne/Perth, hybrid,
> closing 16 Oct 2026 — opened the posting directly and it requires **Australian/NZ citizenship or PR**,
> which a US citizen on a subclass 462 visa does not hold; excluded on work-authorization grounds, not
> added.
>
> Full re-sweep of standing sources (workatastartup.com, wellfound.com, the five economic consulting
> firms' own careers pages plus Charles River Associates' Greenhouse board, simplify.jobs, the
> SimplifyJobs off-season README, interninsider.me winter/spring term pages, BuiltIn NYC/Austin/SF,
> GradConnection Sydney, and the Tokyo boards) found nothing new that clears the bar: economic
> consulting firms show only Summer Analyst/Associate programs for 2027 (CRA's Greenhouse board
> confirmed it does sometimes run winter/spring off-cycle slots in other practices — e.g. a past
> Winter/Spring 2026 Labor & Employment analyst intern in College Station TX/Tallahassee FL — worth
> re-checking that board periodically for a 2027 equivalent, but nothing posted yet); YC/Wellfound/
> BuiltIn/Simplify remain dominated by Summer 2027 and engineering postings; Tokyo boards (japan-dev,
> tokyodev) have no non-technical roles open to non-resident/non-Japanese-fluent candidates. **No
> application deadlines inside three weeks** (nearest are A93 Oct 12 and A95 Oct 17, both >3 weeks out).
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-10-01** (daily sweep — 5 corrections [A5 Dalus, A75 Surface Labs, A88 FairwAI, A120
> MTA, A145 E3], 2 new Tier A rows added, both live: **A157 Scout** (Growth & Operations Intern, SF,
> $20/hr) and **A158 Utilyze** (Partnerships Intern, Austin/Boston/NYC/San Antonio/SF, unpaid).)
>
> Prior: **2026-09-30** (daily sweep — **3 corrections, all closures.** Yesterday's sweep flagged
> A112, A114 (TikTok Sydney) and A156 (Workiva Data Analytics, req R12319) as closing "today" (30 Sep
> 2026) and re-confirmed all three still open at time of check. Re-verified again today, later in the
> day: **all three have now closed.**
> - **A112/A114 (TikTok):** GradConnection's own closing-date text reads "Closing Date: 30th Sep 2026,
>   1:59 pm"; current Sydney time at re-check was 23:07 — ~9 hours past that deadline. (The page's
>   "closing in an hour" countdown widget is a stale/cached fragment and was ignored in favor of the
>   static closing-date text plus actual clock time.)
> - **A156 (Workiva):** queried Workiva's own Workday CXS search API directly by req number (R12319)
>   and by title text — both now return zero results, matching the pattern of sibling reqs
>   A115/A117/A118 which closed the same way on 2026-09-27.
>
> All three moved `live` → `closed` in both `jobs.md` and `dashboard.html`. Kept per the never-delete
> rule. No open imminent deadlines remain in the tracker as of this sweep.
>
> **No new Tier A rows this sweep.** Full re-run of every standing source, nothing cleared the bar:
> `workatastartup.com` (301, reachable) and `wellfound.com/jobs` still render engineering/full-time
> listings only — YC Winter 2027 batch not expected until ~November 2026, confirmed again this run.
> Economic consulting checked at source via each firm's own ATS API rather than just their careers
> pages: Analysis Group and Brattle's public careers pages don't expose postings without a live
> browser session; **Charles River Associates' Greenhouse board (86 jobs, queried directly via the
> public Greenhouse API)** has only Summer 2027 internship reqs (Accounting/Finance, Cyber & Forensic,
> Economics Consulting, Management Advisory) plus full-time "2027 Bachelor's graduates" Analyst/Associate
> reqs that require a completed degree — none fit an enrolled junior on the Jan–Mar window. Compass
> Lexecon (A154, Madrid) re-verified, no drift. Palantir's Lever board (queried directly, 318 postings)
> still shows only the two already-tracked Deployment Strategist Internship reqs (Paris, Honolulu US
> Government) — no new target-metro req. Uber and DoorDash's Greenhouse board tokens both 404 (these
> companies don't run public Greenhouse boards at those slugs — not treated as a finding either way,
> consistent with prior sweeps). Flexport's Greenhouse board (207 jobs, queried directly) has zero
> postings with "intern" in the title. A general web search surfaced a possible MiningStore "Product
> Management Intern, Winter 2027, NYC" lead on Wellfound, but the company's Wellfound page 403'd on
> every fetch attempt and no direct job-posting URL could be found via search — with no verifiable link
> and no confirmable details, this didn't clear the quality bar for even an `unverified` row and was
> left out rather than recorded on a guess.
>
> Access check: all five sanity-check domains reachable (workatastartup.com 301, wellfound.com 200,
> simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200) — no regression.
>
> Prior: **2026-09-29** (daily sweep — urgent re-verification of A156/A112/A114 on their stated Sept 30
> deadline day; all three still open at time of check, no status change yet. No corrections, no new
> Tier A rows.)
>
> Prior: **2026-09-28** (daily sweep — 1 correction, A115/A117/A118 Workiva live → closed on schedule;
> 1 new Tier A row, A156 Workiva Spring 2027 Intern – Data Analytics, live. See below.)

## 🔴 Scope: Jan 4 – Mar 12, 2027 only

**Hard stop: study abroad in Japan begins 1 April 2027.** Anything that cannot finish by mid-March
is out of scope, however good it looks. Target window is **Mon 4 Jan → Fri 12 Mar 2027** (10 weeks,
19 days of buffer).

**Removed from every table below** (2026-08-02 revision) for running past mid-March or falling outside the target
markets — recorded so they aren't re-added by a future sweep:

| Removed | Why |
|---|---|
| Delta Air Lines co-ops (HR Analytics; Crew Resources) | Spring co-op runs past March, forbids concurrent enrollment, requires 3 alternating semesters, Atlanta |
| Medpace Feasibility Informatics | Spring co-op ends after March; Cincinnati |
| Allied Global Marketing | Chicago, outside target markets |
| Deloitte Audit & Assurance (Winter 2027) | Jan–Apr, ends after the deadline |
| Wayfair Data Science Co-op | Jan 5 – Jun 19, ends three months late |
| Birthright Israel Excel | Summer only |
| Masa / Career Israel | 4–6 month minimum |
| Atlassian & Canva ANZ 2027/28 | Wrong year entirely |
| TAU International | Summer program |

**Added:** Tokyo as a target market — see the Japan section of `PROFILE.md`. Sam relocates to Japan
1 April regardless, which makes a Jan–Mar Tokyo stint uniquely low-friction, at the cost of being
realistically unpaid on Temporary Visitor status.

---

## ⚠️ Read this first — the timing reality

It is **August 2026**. You are searching ~5 months ahead of a January 2027 start.
That produces a specific, important problem:

**Most Spring/off-cycle 2027 tech and startup roles have not been posted yet.**

Confirmed from the sweep:

- Startups typically post off-cycle roles **January–March 2027** — i.e. *at or after* your
  intended start date. Their process is fast (2–4 weeks), so this is workable, but it
  means the pipeline fills late and you cannot rely on waiting for postings.
- Large corporate programs post **September–November 2026** for spring cycles
  (e.g. Schwab's 2027 roles post Sept–Nov 2026).
- What *is* posted right now for "Spring 2027" is overwhelmingly **accounting/audit busy-season**
  internships (Jan–Apr). Real off-cycle roles, but not your functions.
- The Bessemer Fellowship — the obvious VC-portfolio route — is **paused and being reimagined**.

**Consequence:** this tracker is deliberately split into three tiers. Tier A is what you can
act on today. Tier B is dated — monitor and apply when it opens. Tier C is the target list
for **direct outreach**, which for a January start at a startup is not the fallback plan,
it is the primary plan. Cold outreach to a founder in October beats a job board in February.

### 🇦🇺 Australia — timing correction

Australian summer internships run **Nov/Dec → Feb**, which overlaps your window well. But
the cycle is offset from the US by a full year in naming:

- **"Summer 2026/27"** = Dec 2026 – Feb 2027 ← *this is your window*. Applications largely
  **closed around May 2026**. Canva's 2026/27 program (early Dec 2026 – late Feb 2027) closed
  1 May 2026.
- **"Summer 2027/28"** = Nov 2027 – Feb 2028. Atlassian's applications open **late Aug–early
  Sept 2026** — i.e. right now — but that's for *next* year.

So the big branded ANZ programs have closed for your window. Australia is still live via
**startups and smaller firms recruiting on rolling cycles**, plus the banks' Sydney summer
analyst programs. Don't write it off — but don't expect Canva or Atlassian for Jan 2027.

---

## Legend

| Symbol | Meaning |
|---|---|
| ✅ | **Live** — verified posting, apply now |
| 🕐 | **Opens later** — dated window, monitor |
| 🎯 | **Target** — no posting; direct outreach / careers-page watch. Link goes to careers page. |

**Difficulty** 1–5, higher = harder to get in.
**Fit** 1–5, higher = better match. **`~` = provisional**, estimated from `PROFILE.md` only —
recomputed once the resume is uploaded.
**Mode**: `In-person` / `Hybrid` / `Remote`. In-person scores up per your stated preference.

---

## Tier A — Live now

| # | Company | Role | Function | Location | Mode | Stage | Window | Deadline | Pay | Diff | Fit | Priority | Status | Link |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | Brilliant Infotech (Brilliant Agency) | Business Development Intern (Winter/Spring 2027) | BD | New York, NY (title) / Council Bluffs, IA (JD) | **Remote** | Small | Jan 11 2027 – May/June 2027 ⚠ | Rolling | $250/mo equipment stipend | 2 | ~2 | Low | conflict | [LinkedIn](https://www.linkedin.com/jobs/view/business-development-internship-winter-spring-2027-at-brilliant-infotech-inc-4445733458) |
| A2 | Magnet Media | Social Media Intern (Spring 2027) | Growth/Marketing | New York, NY | In-person | Small | Spring 2027 | Rolling | Verify | 2 | ~2 | Low | closed | [Magnet Media careers](https://magnetmediafilms.com/careers?gh_jid=8036360) |
| A3 | Glovo | Marketing/Finance & Controlling Internship Program | Growth/Data | Barcelona | In-person | Unicorn | 6-mo min ⚠ | Rolling | Paid | 3 | ~4 | Low | conflict | [Glovo careers](https://jobs.glovoapp.com/) |
| A4 | Zipline | Community Engagement Intern (Spring 2027) | Growth/Community | Austin, TX | In-person | Series C | Jan–Apr 2027 ⚠ | Rolling | $30/hr | 3 | ~4 | Low | closed | [Techstars board](https://jobs.techstars.com/companies/zipline/jobs/63567774-community-engagement-intern-summer-2026) |
| A5 | Dalus (YC W25) | GTM Intern | GTM | SF / Melbourne, AU / Munich / Remote | In-person (SF/Munich/Melbourne) or Remote | YC W25 | Rolling, part-time | Rolling | $18–25/hr | 2 | ~4 | **High** | live | [Work at a Startup](https://www.workatastartup.com/jobs/99648) |
| A6 | Uplane (YC F25) | Business Development Intern | BD | San Francisco (or Berlin/Remote) | In-person | YC F25 | Rolling, 3-mo min ⚠ | Rolling | $4K/mo | 2 | ~5 | Med | closed | [Work at a Startup](https://www.workatastartup.com/jobs/97366) |
| A7 | Uplane (YC F25) | AI Marketing Strategist Intern | Growth | San Francisco | In-person | YC F25 | Rolling, 4-mo min ⚠ | Rolling | $4K/mo | 2 | ~4 | Low | conflict | [Work at a Startup](https://www.workatastartup.com/jobs/93708) |
| A8 | GutGutGoose (YC S26) | Growth Intern (founding team) | Growth | San Francisco | In-person | YC S26 | "Beginning whenever you can" | Rolling | $19–25/hr | 1 | ~4 | Low | closed | [Work at a Startup](https://www.workatastartup.com/jobs/102677) |
| A9 | Lambda Robotics (YC F26) | Founding GTM | Growth | San Francisco | In-person | YC F26 | Rolling | Rolling | $6–9K/mo | 3 | ~4 | Med | closed | [Work at a Startup](https://www.workatastartup.com/jobs/104228) |
| A10 | Naive (YC P25) | Growth Engineer Intern | Growth | SF / Remote | In-person or Remote (candidate's choice, not blended) | YC P25 | Rolling | N/A — posting 404'd | $20–40/hr | 2 | ~4 | Med | closed | [Work at a Startup](https://www.workatastartup.com/jobs/94648) |
| A11 | Claim Health (YC P25) | Content Marketing Intern | Growth | New York, NY | In-person | YC P25 | 10–12 wks, rolling | Rolling | Stipend | 2 | ~3 | Med | closed | [Work at a Startup](https://www.workatastartup.com/jobs/94958) |
| A12 | Mosaic (YC W25) | Growth Intern | Growth | San Francisco | In-person | YC W25 | Rolling | Rolling | $5–10K/mo | 3 | ~4 | Med | closed | [Work at a Startup](https://www.workatastartup.com/jobs/74610) |
| A13 | DeepAware AI (YC S25) | Business Development Intern | BD | San Francisco | In-person | YC S25 | Rolling | Rolling | Not listed | 2 | ~4 | Med | live | [Work at a Startup](https://www.workatastartup.com/jobs/100904) |
| A14 | Celonis | Business Development Representative Sales Intern (Part-Time) | BD | New York, NY | Hybrid | Public | Unconfirmed | Unconfirmed | $58,240 (FTE-annualized, PT title) | 3 | ~4 | Med | closed | [Built In NYC](https://www.builtinnyc.com/job/business-development-representative-sales-intern-part-time/10648137) |
| A15 | UT Austin Athletics | Video and Analytics Intern — Baseball | Data | Austin, TX | In-person | On-campus | Winter/Spring 2027 (tagged) | TBC | Unconfirmed | 1 | ~2 | Low | unverified | [UT Workday](https://utaustin.wd1.myworkdayjobs.com/utstudent/job/UT-MAIN-CAMPUS/Video-and-Analytics-Intern--Baseball_R_00047706) |
| A16 | Zipline | Strategic Engagements & Events Intern (Spring 2027) | Partnerships | South San Francisco, CA | In-person | Series C | Jan–Apr 2027 ⚠ | Rolling | $34/hr | 3 | ~4 | Med | conflict | [Techstars board](https://jobs.techstars.com/companies/zipline) |
| A17 | Axo Longevity | Intern (Growth & Creative) | Growth | Barcelona | **Remote** | Early | Unconfirmed | Unconfirmed | Likely unpaid | 1 | ~3 | Low | closed | [Wellfound](https://wellfound.com/jobs/3628609-intern-growth-creative) |
| A18 | Datadog | Product Management Intern (Winter session) | PM | New York, NY | Hybrid | Public | Jan 4 – Apr 23 2027 ⚠ | Unconfirmed | $100K–110K (annualized) | 4 | ~4 | Low | closed | [Built In NYC](https://www.builtinnyc.com/job/product-management-intern/10710775) |
| A19 | IBM | Technology Sales Engineer Intern, Entry-Level Sales Program 2027 | Sales/Solutions Engineer | Austin, TX (+ SF, NYC, RTP, and others) | Hybrid | Enterprise | Unconfirmed | Expired Sept 1 2026 | $71,100–$130,350/yr | 3 | ~4 | Med | closed | [Mirror via Clemson](https://career.clemson.edu/jobs/ibm-technology-sales-engineer-intern-entry-level-sales-program-2027-2/) |
| A64 | Zipline | Supply Chain Business Operations Intern (Spring 2027) | Data/Ops | South San Francisco, CA | In-person | Series C | Jan–Apr/May 2027 ⚠ | Rolling | Unconfirmed | 3 | ~4 | Low | conflict | [Built In SF](https://www.builtinsf.com/job/supply-chain-business-operations-intern-spring-2027/10751227) |
| A65 | Peakflo | Product Manager Intern (Paid) | PM | India | Remote | YC W22 | Rolling | Rolling | ₹360–480K/yr (~$4.3–5.8K) | 2 | ~2 | Low | live | [Work at a Startup](https://www.workatastartup.com/jobs/95821) |
| A66 | Peakflo | Sales Development Representative (SDR) Intern (Paid) | Sales | India | Remote | YC W22 | 6-mo min ⚠ | Rolling | ₹240–300K/yr | 1 | ~1 | Low | conflict | [Work at a Startup](https://www.workatastartup.com/jobs/82428) |
| A67 | Closure | Product Manager Summer 2027 Intern | PM | San Francisco, CA | In-person | YC W25 | Summer 2027 ⚠ | Unconfirmed | $4–8K/mo | 2 | ~4 | Low | closed | [YC](https://www.ycombinator.com/companies/closure) |
| A68 | Tesla | Data Engineer Intern, Cell Engineering | Data | Palo Alto, CA | Unconfirmed | Public | Winter/Spring 2027 (tagged) | Unconfirmed | Unconfirmed | 4 | ~3 | Low | unverified | [Tesla Careers](https://www.tesla.com/careers/search/job/278622) |
| A20 | Agentio | Creator Partnerships Intern | Partnerships | New York, NY | In-person | Early | Unconfirmed | Unconfirmed | $20/hr | 2 | ~3 | Low | closed | [Built In NYC](https://www.builtinnyc.com/job/creator-partnerships-intern/8048359) |
| A21 | Crustdata (YC F24) | AI Solutions Engineering Intern | Solutions Engineer | Brooklyn, NY | In-person | YC F24 | Rolling | ~Aug 26 2026 (confirm) | $4–6K/mo | 3 | ~5 | **High** | closed | [YC](https://www.ycombinator.com/companies/crustdata/jobs/0W1EW1X-ai-solutions-engineering-intern) |
| A22 | CertiK | Business Development Intern / Ambassador | BD | New York, NY | Hybrid | Public/late-stage | Rolling | Rolling | $1K/mo (5 hrs/wk) | 2 | ~3 | Low | live | [Lever](https://jobs.lever.co/certik/241dde9b-95d6-4eda-a207-a149934b16e1) |
| A23 | Chubb | Data Analyst Intern | Data | New York, NY (2 locations) | In-person | Enterprise | Unconfirmed | Unconfirmed | $20–34/hr | 3 | ~4 | Med | closed | [Built In](https://builtin.com/job/data-analyst-intern/8731657) |
| A24 | Lieberman Research Worldwide | Market Research Intern — Quantitative Team | Data | Great Neck, NY | **Remote** | Established | Rolling, year-round | Rolling | $20/hr (~28 hrs/wk) | 2 | ~4 | Low | closed | [Built In](https://builtin.com/job/market-research-intern-year-round-quantitative-team/10317459) |
| A25 | SOUKMEDIA | B2B Growth & Demand Generation Intern | Growth | Remote (US) | Remote | Unconfirmed | 3 months, start TBC | Unconfirmed | Unconfirmed | 2 | ~4 | Low | unverified | [Built In](https://builtin.com/job/b2b-growth-demand-generation-intern/10474143) |
| A26 | Treasure | Go-To-Market Intern | Growth | San Francisco (2 locations) | Hybrid | Unconfirmed | Unconfirmed | Unconfirmed | $25–30/hr | 2 | ~3 | Low | unverified | [Built In](https://builtin.com/job/go-market-intern/10651661) |
| A27 | Anthelion Capital | Quant Developer / Quant Research Intern | Data | New York, NY | In-person | Unconfirmed | Dec 2026 – Feb 2027 (TBC) ⚠ | Unconfirmed | $1.8–2K/wk | 4 | ~3 | Low | conflict | [Built In](https://builtin.com/job/quant-developer-quant-research-intern-2026-2027/10359304) |
| A28 | Unify | GTM Engineering Intern | Growth | San Francisco | In-person | Unconfirmed | Unconfirmed | Unconfirmed | Unconfirmed | 2 | ~3 | Low | unverified | [Built In](https://builtin.com/job/gtm-engineering-intern/10691914) |
| A29 | Rocket Internet SE | Founders' Associate Intern | BD | San Francisco | In-person | Global | Unconfirmed | Unconfirmed | Unpaid | 3 | ~4 | Med | unverified | [Built In](https://builtin.com/job/founders-associate-intern/6196290) |
| A30 | Guidepoint | Business Development Intern | BD | New York, NY | In-person | Public | Unconfirmed | Unconfirmed | ~$25K (program stipend) | 3 | ~3 | Low | unverified | [Built In](https://builtin.com/job/business-development-intern-class-2028/10728729) |
| A31 | Global Pathways AI | Product & Go-to-Market Internship | PM | San Francisco | Remote | Early | Rolling | Rolling | Unpaid (may become paid) | 1 | ~2 | Low | unverified | [Wellfound](https://wellfound.com/jobs/4570560-product-go-to-market-internship-opportunities) |
| A70 | Base Power Company | Sales Intern (was: Growth Intern) | Sales | Austin, TX | In-person | Startup | Unconfirmed | Rolling | Unconfirmed | 2 | ~3 | Low/Med | live | [Built In Austin](https://www.builtinaustin.com/job/growth-intern/10000211) |
| A71 | Zettabyte Inc | Growth Operations Intern | Growth | Bay Area, CA | Flexible | Startup | 3–6 mo, flexible | Rolling | Unconfirmed | 2 | ~4 | Med | unverified | [Built In SF](https://www.builtinsf.com/job/growth-operations-intern/8794820) |
| A72 | Jean Martin Inc | Market Research and Business Development Intern | BD/Data | New York, NY | In-person | Unconfirmed | Unconfirmed | Unconfirmed | Unconfirmed | 2 | ~4 | Med | unverified | [Built In NYC](https://www.builtinnyc.com/job/market-research-and-business-development-intern/10732902) |
| A73 | DEUNA | Data Science Intern | Data | San Francisco, CA | Hybrid | Startup | Unconfirmed | Unconfirmed | Unpaid | 2 | ~3 | Low | unverified | [Built In SF](https://www.builtinsf.com/job/data-science-intern/9973177) |
| A74 | Workato | Intern, AI Engineering | Data (ML-eng skew) | San Francisco, CA | In-person | Growth-stage | Winter 2026 & Spring 2027 (stated) | Unconfirmed | Unconfirmed | 3 | ~2 | Low | unverified | [Built In SF](https://www.builtinsf.com/job/intern-ai-engineering/9010182) |
| A75 | Surface Labs | AI GTM Engineer Intern | Growth/Sales (technical-adjacent) | San Francisco, CA / India | Remote (SF preferred; India also accepted) | YC-backed | Rolling, 3-mo | Confirm ≤ Mar 12 | Commission-only for first 3mo, then FT + base ⚠ (OTE ~$10–20K/mo; equity 0.01–1.00%) | 2 | ~3 | Low | live | [Work at a Startup](https://www.workatastartup.com/jobs/93375) |
| A76 | Novaflow | Growth Intern | Growth | San Francisco, CA | Remote or in-person | YC-backed | Summer 2026 (as posted) ⚠ | Summer 2026 (as posted) ⚠ | $25–30/hr | 2 | ~4 | Low | closed | [Work at a Startup](https://www.workatastartup.com/jobs/92868) |
| A77 | hoop.shop | Performance Marketing & Social Creative Intern | Growth (ambiguous) | New York, NY (listed) / Remote | Remote | Early | Unconfirmed | Unconfirmed | Unconfirmed | 2 | ~3 | Low | unverified | [Wellfound](https://wellfound.com/jobs/4589449-performance-marketing-social-creative-freelance-clone) |
| A78 | FairwAI | Data Analyst Intern, Policy + Ethics | Data | Remote (Boston/NYC/SF/Europe) | Remote | Early | Spring 2026 stated; 2027 TBC ⚠ | Unconfirmed | Unpaid | 2 | ~3 | Low | closed | [Wellfound](https://wellfound.com/jobs/3257803-data-analyst-intern-policy-ethics) |
| A79 | Zeminent | Business Development & Lead Generation Intern | BD | Remote (Gurgaon, India hrs) | Remote | Small | Unconfirmed | Unconfirmed | Unconfirmed | 1 | ~2 | Low | unverified | [Wellfound](https://wellfound.com/jobs/4436924-business-development-lead-generation-intern) |
| A80 | Notion | Data Science Intern (Winter 2027) | Data | San Francisco, CA / New York, NY | In-person | Late-stage | **Jan 25 2027** | **Apr 16 2027 ⚠** | $55/hr (Bachelor's) / $59/hr (Master's) | 5 | ~5 | Med | closed | [Ashby](https://jobs.ashbyhq.com/notion/a67d6f2b-7c13-41d0-b36b-b2f662c9873e/application) |
| A81 | LinkedIn | Global Sales Organization Intern | Sales | San Francisco, CA | In-person | Public | Rolling, unconfirmed | Unconfirmed | Paid (amount unconfirmed) | 4 | ~3 | Med | closed | [Intern Insider](https://interninsider.me/internships/linkedin/global-sales-organization-intern-5793c9fa-ccc5-4abd-b1f5-b57f77f18a37) |
| A82 | Soren | Growth Intern | Growth | San Francisco, CA | In-person | Startup | Rolling | Unconfirmed | $6–11K/mo | 2 | ~4 | **High** | live | [Work at a Startup](https://www.workatastartup.com/jobs/102000) |
| A83 | Relling | Business Operations Intern | Data/Ops | San Francisco, CA | In-person | Startup (hardware, ex-SpaceX/NASA) | Rolling | Unconfirmed | $20–100/hr | 2 | ~3 | Med | live | [Work at a Startup](https://www.workatastartup.com/jobs/97830) |
| A84 | Dedalus Labs | Growth Intern (posted as Summer 2027) | Growth/DevRel | San Francisco, CA | In-person | Early-stage AI infra | Summer 2027 ⚠ | Unconfirmed | $4–8K/mo | 2 | ~4 | Low | closed | [Work at a Startup](https://www.workatastartup.com/jobs/98002) |
| A85 | Dedalus Labs | Product Manager Intern (posted as Summer 2027) | PM | San Francisco, CA | In-person | Early-stage AI infra | Summer 2027 ⚠ | Unconfirmed | $4–8K/mo | 2 | ~4 | Low | closed | [Work at a Startup](https://www.workatastartup.com/jobs/98000) |
| A86 | Sixtyfour | Growth Intern (posted as Fall 2026) | Growth | San Francisco, CA | In-person | Startup (compliance-data AI) | Fall 2026 ⚠ | Unconfirmed | $30–50/hr | 2 | ~3 | Low | conflict | [Work at a Startup](https://www.workatastartup.com/jobs/105487) |
| A87 | GutGutGoose | Growth (founding team) — new posting | Growth | San Francisco, CA | In-person | YC S26 | Trial + FT decision Sept 20 2026 ⚠ | Unconfirmed | $19–22/hr trial → $120K+ FT | 1 | ~3 | Low | closed | [Work at a Startup](https://www.workatastartup.com/jobs/105105) |
| A88 | FairwAI | Project Management Fellow | PM/Partnerships | Remote (NYC/SF/Boston + other hubs; no Austin) | **Remote** | Early | 3–6 mo, flexible start | Rolling | Unpaid (10–20 hrs/wk) | 2 | ~3 | Low | closed | [Wellfound](https://wellfound.com/jobs/3251810-project-management-fellow) |
| A89 | Peggy | Growth & PR Intern (Part-Time) | Growth (ambiguous — PR/comms) | Remote (ET preferred) | **Remote** | Early | Unconfirmed | Unconfirmed | Unconfirmed | 1 | ~2 | Low | unverified | [Wellfound](https://wellfound.com/jobs/4589467-growth-pr-intern-part-time-help-launch-an-ai-app-for-parents) |
| A127 | The Boring Company | Operations Internships (Part-Time) — Business/Project Development track (Winter/Spring 2027) | BD/Strategy & Ops | Bastrop, TX (also Las Vegas, NV) | In-person | Private (Musk-founded infra) | Winter/Spring 2027 (tagged) | Confirm ≤ Mar 12 | Unconfirmed | 4 | ~3 | Med | unverified | [Boring Company careers → application](https://jobs.gem.com/the-boring-company/am9icG9zdDqxHfxcQ--wXDcxkn-GcrPC) |
| A90 | AxentraOS | Market Research Intern | Data/BD | Remote (US) | **Remote** | Early | 2–3 months | Unconfirmed | Unpaid | 1 | ~2 | Low | closed | [Wellfound](https://wellfound.com/jobs/3647210-market-research-intern) |
| A91 | Trellis AI | Business Operations Intern | BD/Ops (founder's-associate generalist) | San Francisco, CA | In-person | Early (AI healthcare) | Rolling | N/A | Unconfirmed | 2 | ~4 | Med | closed | [Intern Insider](https://interninsider.me/internships/trellis-ai/business-operations-intern-3d9acb03-f6b8-41ae-bca8-829c31255e4c) |
| A92 | TraceRoot.AI (YC S25) | Developer Marketing Intern (was: GTM Engineer Intern) | Growth (technical-adjacent) | San Francisco, CA | Hybrid (≥3 days onsite) | YC S25 | Rolling | Unconfirmed (see note) | $4–6K/mo | 2 | ~5 | **High** | live | [YC / Work at a Startup](https://www.ycombinator.com/companies/traceroot-ai/jobs/dk1ep2K-gtm-engineer-intern) |
| A93 | NewsBreak | Growth Engineer Intern | Growth | Mountain View, CA | In-person | Growth-stage | Rolling | Jan 10 2027 | $40–60/hr | 4 | ~1 | Low | live | [Intern Insider](https://interninsider.me/internships/newsbreak/growth-engineer-intern-b3921cc9-7d80-45ae-acd0-e6397c0506e3) |
| A94 | NewForm | Business Development Intern | BD | New York, NY | Hybrid | Startup | Rolling admission | Closed Aug 26 2026 | Unconfirmed | 2 | ~4 | Med | closed | [Intern Insider](https://interninsider.me/internships/newform/business-development-intern-b44b60d3-aa91-4d74-8bf7-b9d00d044884) |
| A95 | Parkdepot | Marketing Analyst Intern | Growth/Data (quantitative) | San Francisco, CA | In-person | Startup | Rolling, "full-time commitment" ⚠ | Oct 17 2026 | Paid (amount unconfirmed) | 2 | ~3 | Low | live | [Intern Insider](https://interninsider.me/internships/parkdepot/marketing-analyst-intern-fceac396-5267-4c7b-af85-dfba02481761) |
| A96 | Crowe Global | AI Functional Intern (Winter 2027) | Data/Strategy (technical-adjacent) | Austin, TX | In-office | Enterprise | **Winter 2027 (explicit)** | Ongoing | $27–42/hr | 3 | ~4 | **High** | live | [Built In Austin](https://www.builtinaustin.com/job/ai-functional-intern-winter-2027/10769798) |
| A97 | Cadence Design Systems | AI & Strategic Marketing Intern | Data/Strategy | Austin, TX | In-office | Public | Unconfirmed | Removed Aug 31 2026 | Unconfirmed | 3 | ~3 | Low | closed | [Built In Austin](https://www.builtinaustin.com/job/ai-strategic-marketing-intern/10787551) |
| A98 | Cresta | Data Science Intern (Customer Success) | Data | Remote (US) | **Remote** | Growth-stage | Rolling | Closed Oct 19 2026 | Unconfirmed | 3 | ~4 | Med | closed | [Greenhouse](https://job-boards.greenhouse.io/cresta/jobs/5213417008) |
| A99 | Scale AI | AI Builder Intern | Growth/Strategy (technical-adjacent) | San Francisco or New York | In-person | Late-stage | Summer 2027 ⚠ | Closed Aug 27 2026 | Unconfirmed | 4 | ~4 | Low | closed | [Intern Insider](https://interninsider.me/internships/scale-ai/ai-builder-intern-b83435b3-da10-4b18-87f4-3bebcf6d72e2) |
| A100 | APX (now Aster) | Developer Relations Intern | DevRel | United States (city unconfirmed) | In-person | Crypto/dev platform | Rolling | Expired (Nov 24 2025) | Unconfirmed | 2 | ~4 | Low | closed | [Intern Insider](https://interninsider.me/internships/apx-now-aster/developer-relations-intern-ab244e84-2b9d-40db-8cf3-3f27f1e048e0) |
| A101 | Advancy Partners | Strategy Consulting Intern (2026 Intake) | Data/Strategy | Sydney, AU | In-person | Boutique consulting | 2–6 months, flexible | Rolling | Paid (amount unconfirmed) | 3 | ~4 | Med | closed | [Advancy](https://advancy.recruitee.com/o/sydney-strategy-consulting-intern-2026-intake) |
| A104 | Direct Agents | AI Business Strategy & Operations Intern | Strategy | Culver City, CA | In-person | Established (2003) | Rolling, no stated minimum | Rolling | Unconfirmed | 2 | ~2 | Low | closed | [Intern Insider](https://interninsider.me/internships/direct-agents/ai-business-strategy-operations-intern-115edaa5-1508-48e8-a5b2-84ba5a0a7cb2) |
| A105 | Zipline | Sales Operations Analyst Intern | Data | South San Francisco, CA | In-person | Series C | Winter 2027 (Jan–Apr 2027) ⚠ | Rolling | $40/hr | 3 | ~4 | Low | conflict | [Intern Insider](https://interninsider.me/internships/zipline/sales-operations-analyst-intern-a2453a3e-deb9-4b6c-85be-2ee8537a8374) |
| A106 | Zipline | Marketing Intern (Spring 2027) | Growth | South San Francisco, CA | In-person | Series C | Jan–Apr 2027 ⚠ | Rolling | $34/hr | 2 | ~3 | Low | conflict | [Intern Insider](https://interninsider.me/internships/zipline/marketing-intern-spring-2027-7ac4e305-f77d-4616-b338-8bd9297b29a7) |
| A107 | Zipline | Operations Experience Intern (Spring 2027) | Strategy | South San Francisco, CA | In-person | Series C | Winter 2027 (Jan–Apr 2027) ⚠ | Rolling | Unconfirmed | 3 | ~4 | Low | closed | [Intern Insider](https://interninsider.me/internships/zipline/operations-experience-intern-spring-2027-404887f1-5384-4506-a2a2-6500b67f8fd6) |
| A108 | Ekimetrics | 6-Month Internship in Strategy & Data Science | Strategy | New York, NY | In-person | Boutique consultancy | Rolling start, 6-month commitment ⚠ | Rolling | Paid (amount unconfirmed) | 3 | ~5 | Med | conflict | [Intern Insider](https://interninsider.me/internships/ekimetrics/6-months-internship-in-strategy-data-science-049dcc50-7033-4fa0-a0a4-e1e74bc773af) |
| A109 | Qureos | Business Development Intern | BD | New York, NY | In-person | Unconfirmed | Rolling | Unconfirmed | Unconfirmed | 1 | ~3 | Low | closed | [Intern Insider](https://interninsider.me/internships/qureos/business-development-intern-d9aec99e-36ef-43d6-8692-aacf913d8029) |
| A110 | The Walt Disney Company | ABC News Insights and Analytics Intern (Spring 2027) | Data | New York, NY | In-person | Enterprise | Jan–Jun 2027 ⚠ | Rolling | $23/hr | 4 | ~4 | Low | conflict | [Disney Workday](https://disney.wd5.myworkdayjobs.com/disneycareer/job/New-York-NY-USA/ABC-News-Insights-and-Analytics-Intern--Spring-2027_10158500) |
| A111 | Motive | Sales Development Intern | Sales | Austin, TX | Hybrid | Startup | Summer 2027 ⚠ (as posted) | Unconfirmed | Unconfirmed | 2 | ~3 | Low | closed | [Greenhouse](https://job-boards.greenhouse.io/gomotive/jobs/8431778002) |
| A112 | TikTok | Client Solution Intern (GBS AU) — 2027 Start | Sales/BD (analytics-adjacent) | Sydney, AU | In-person (assumed; not explicitly stated) | Enterprise | Candidate states own start/end dates; posting shows ~Dec 2026 (approx) | **Reopened — closing 30 Oct 2026, 1:59pm Sydney** | Unconfirmed | 4 | ~4 | High | live | [GradConnection](https://au.gradconnection.com/employers/tiktok/jobs/tiktok-client-solution-intern-gbs-au-2027-start-3/) |
| A113 | TikTok | Revenue Product Operations Intern (TikTok LIVE-Revenue) — 2027 Start | PM/Product Ops | Sydney, AU | Unconfirmed | Enterprise | Rolling; explicit 6-month commitment required ⚠ | Closing 19 Oct 2026 | Unconfirmed | 4 | ~3 | Low | conflict | [GradConnection](https://au.gradconnection.com/employers/tiktok/jobs/tiktok-revenue-product-operations-intern-tiktok-live-revenue-2027-start/) |
| A114 | TikTok | AI Product Manager Intern (TikTok Live-Revenue) — 2027 Start | PM | Sydney, AU | Hybrid | Enterprise | Dec 2026 (approx); candidate states own start/end dates | **Reopened — closing 30 Oct 2026, 1:59pm Sydney** | Unconfirmed | 4 | ~3 | Med | live | [GradConnection](https://au.gradconnection.com/employers/tiktok/jobs/tiktok-ai-product-manager-intern-tiktok-live-revenue-2027-start-2/) |
| A115 | Workiva | Commercial Strategy Intern (Workiva's own site labels this intake "Spring 2027") | Strategy | Remote (US); NYC/SF/Austin office hubs available for hybrid | Remote | Public (NASDAQ: WK) | **Confirmed: term starts Jan 4, 2027**, 15–20 hrs/wk | **Closed Sept 27 2026 (confirmed — req returns 0 results)** | $22.00/hr (confirmed directly, req R12317) | 2 | ~2 | Low | closed | [Workiva Workday, req R12317](https://workiva.wd503.myworkdayjobs.com/careers) |
| A117 | Workiva | Product Management Intern (Workiva's own site: "Spring & Summer 2027 Intern - Product Management") | PM | Remote (US); hybrid near a Workiva office hub | Remote | Public (NASDAQ: WK) | Confirmed: Spring option starts **Jan 4, 2027**, 15–20 hrs/wk (a Summer option starting May 17 2027 also exists on the same req, not relevant here) | **Closed Sept 27 2026 (confirmed — req returns 0 results)** | $40/hr (confirmed, req R12355) | 2 | ~2 | Low | closed | [Workiva Workday, req R12355](https://workiva.wd503.myworkdayjobs.com/careers) |
| A118 | Workiva | Intern – Partnerships (Workiva's own site labels this intake "Spring 2027") | Partnerships | New York, NY (hybrid near NYC hub) or Remote (US) | Remote | Public (NASDAQ: WK) | Confirmed: term starts **Jan 4, 2027**, 15–20 hrs/wk. Two separate live reqs share this exact title (R12268, R12269) | **Closed Sept 27 2026 (confirmed — reqs return 0 results)** | $21.00/hr (confirmed directly) | 2 | ~2 | Low | closed | [Workiva Workday, reqs R12268/R12269](https://workiva.wd503.myworkdayjobs.com/careers) |
| A119 | Zipline | Commercial Strategy & Operations Intern (Winter 2027 term) | Strategy | Austin, TX (+ Houston/Phoenix/San Antonio/Dallas/LA) | In-person | Series C | "Winter 2027" term offered (sibling reqs A105/A107 confirm Zipline's Winter 2027 label = Jan–Apr) ⚠ | Rolling | Paid (amount unconfirmed) | 2 | ~4 | Med | conflict | [Intern Insider](https://interninsider.me/internships/zipline/commercial-strategy-operations-intern-d75db0e8-2047-4484-b916-c7909405d22d) |
| A120 | Metropolitan Transportation Authority (MTA) | EAM Analyst Intern, Emerging Talent (Spring) | Data | New York, NY (Manhattan) | In-person | Public agency | **Spring (title confirms)** | Confirm ≤ Mar 12 | $19/hr (Undergrad) / $21/hr (Grad) | 2 | ~4 | Med | live | [MTA/Jobvite](https://jobs.jobvite.com/metropolitantransportationauthority/job/oZuEAfwr) |
| A121 | Ankura | University Intern, Forensic Data & Analytics | Data/Strategy (forensic/litigation consulting) | New York, NY | In-person | Established (global advisory) | Rolling, no stated term ⚠ | Rolling (no deadline set — see note) | $34/hr | 3 | ~4 | Med | live | [Ankura Workday, req R104943](https://ankura.wd5.myworkdayjobs.com/Ankura/job/New-York-NY/University-Intern--Forensic-Data---Analytics_R104943) |
| A122 | Tesla | Data Engineer Intern, Fleet Analytics | Data | Palo Alto, CA | Unconfirmed | Public | Winter/Spring 2027 (tagged) | Unconfirmed | Unconfirmed | 4 | ~3 | Low | unverified | [Tesla Careers](https://www.tesla.com/careers/search/job/283138) |
| A123 | Zipline | Data Analytics Intern (Spring 2027) | Data | South San Francisco, CA | In-person | Series C | Jan 2027 (inferred); Spring 2027 tag | Apr 2027 ⚠ (inferred from sibling reqs) | Unconfirmed | 3 | ~4 | Low | conflict | [Zipline careers](https://www.zipline.com/open-roles/7990420003) |
| A124 | Tesla | Commercial Charging Product Management Intern, Energy Engineering | PM | Palo Alto, CA | Unconfirmed | Public | Winter/Spring 2027 (tagged) | Unconfirmed | Unconfirmed (sibling reqs ~$20–50/hr) | 4 | ~4 | Low | unverified | [Tesla Careers](https://www.tesla.com/careers/search/job/283156) |
| A125 | Tesla | Data Engineer Intern, Fleet Data – Self-Driving | Data | Palo Alto, CA | Unconfirmed | Public | Spring 2027 (tagged) | Unconfirmed | Unconfirmed | 4 | ~3 | Low | unverified | [Tesla Careers](https://www.tesla.com/careers/search/job/281612) |
| A126 | Tesla | Machine Learning Engineer Intern, Charging Data Modeling | Data (ML-eng skew) | Palo Alto, CA | Unconfirmed | Public | Winter/Spring 2027 (tagged) | Unconfirmed | Unconfirmed | 4 | ~3 | Low | unverified | [Tesla Careers](https://www.tesla.com/careers/search/job/281940) |
| A128 | Base Power Company | Business Operations Intern, Commercial Partnerships | Strategy/Partnerships | Austin, TX | In-person | Startup | Unconfirmed | Confirm ≤ Mar 12 | Unconfirmed | 3 | ~4 | High | live | [Built In Austin](https://www.builtinaustin.com/job/business-operations-intern-commercial-partnerships/11174864) |
| A129 | Base Power Company | Finance – Analytics Intern | Data/Finance | Austin, TX | In-person | Startup | Unconfirmed | Confirm ≤ Mar 12 | Unconfirmed | 3 | ~3 | Med | live | [Built In Austin](https://www.builtinaustin.com/job/finance-analytics-intern/11174862) |
| A130 | Kodiak Robotics | Winter 2027 Intern, Data Engineering | Data | Mountain View, CA | In-person | Late-stage (autonomous trucking) | **Start Jan 2027, 12–16 wks, end date flexible** | Confirm ≤ Mar 12 | $10,000 (range unclear — flat figure) | 3 | ~3 | Med | live | [Greenhouse](https://job-boards.greenhouse.io/kodiak/jobs/4396622009) |
| A131 | Base Power Company | Financial Planning Intern | Data/Finance | Austin, TX | In-person | Startup | Unconfirmed | Confirm ≤ Mar 12 | Unconfirmed | 3 | ~3 | Med | closed | [Built In Austin](https://www.builtinaustin.com/job/finance-planning-intern/11174868) |
| A132 | Base Power Company | Marketing Intern | Growth | Austin, TX | In-person | Startup | Unconfirmed | Confirm ≤ Mar 12 | Unconfirmed | 2 | ~3 | Med | closed | [Built In Austin](https://www.builtinaustin.com/job/marketing-intern/11184090) |
| A133 | Base Power Company | Deployments Operations Intern | Strategy (field ops) | Austin, TX | In-person | Startup | Unconfirmed | Confirm ≤ Mar 12 | Unconfirmed | 2 | ~2 | Low | live | [Built In Austin](https://www.builtinaustin.com/job/deployments-operations-intern/11184062) |
| A134 | Acxiom | Intern, Agency Partnerships | Partnerships | New York, NY | In-person | Enterprise (IPG subsidiary) | **Winter 2027, starts Jan 11 2027** | Confirm ≤ Mar 12 | Paid (amount unconfirmed) | 2 | ~4 | Med | closed | [Intern Insider](https://interninsider.me/internships/acxiom/intern-agency-partnerships-042301fe-a2b3-4883-81c4-1b56a2cc4c38) |
| A135 | Acxiom | Intern, Product Management | PM | Remote (US) | Remote | Enterprise (IPG subsidiary) | **Winter 2027, starts Jan 11 2027** | Confirm ≤ Mar 12 | Paid (amount unconfirmed) | 2 | ~2 | Low | closed | [Intern Insider](https://interninsider.me/internships/acxiom/intern-product-management-30a0e8ee-b65a-43d1-acbd-2d6f995e3beb) |
| A136 | Acxiom | Enterprise Solutions Consulting Intern (aka "Intern - Solution Consultant" on Acxiom's own ATS) | Strategy | Remote/Homebased (resolved — see note) | Remote | Enterprise (IPG subsidiary) | **Winter 2027, starts Jan 11 2027** | Confirm ≤ Mar 12 | Paid (amount unconfirmed) | 2 | ~2 | Low | closed | [Intern Insider](https://interninsider.me/internships/acxiom/enterprise-solutions-consulting-intern-945140ee-5605-4c76-8729-56777cdc8f52) |
| A137 | Acxiom | Intern, Financial Analyst | Data/Finance | New York, NY | In-person | Enterprise (IPG subsidiary) | **Winter 2027, starts Jan 11 2027** | Confirm ≤ Mar 12 | Paid (amount unconfirmed) | 2 | ~2 | Low | closed | [Intern Insider](https://interninsider.me/internships/acxiom/intern-financial-analyst-7d934d45-ad65-48dc-aead-3a42da19e9cf) |
| A138 | Heron Power | Intern, Business Development Associate (Fall 2026/Winter 2027) | BD | Scotts Valley, CA (Bay Area-adjacent, not core metro) | In-person | a16z-backed (power electronics/grid) | Fall 2026/Winter 2027 (tagged); term boundaries unclear ⚠ | Confirm ≤ Mar 12 | Unconfirmed | 3 | ~3 | Low | unverified | [Ashby](https://jobs.ashbyhq.com/heron-power/823aab95-be9b-485e-a8fc-4024440a91cd) |
| A139 | Tesla | Product Manager Intern, Residential Energy Engineering | PM | Palo Alto, CA | Unconfirmed | Public | Winter 2027 (tagged) | Unconfirmed | Unconfirmed | 4 | ~4 | Low | unverified | [Tesla Careers](https://www.tesla.com/careers/search/job/283841) |
| A140 | Acxiom | Data Scientist Intern | Data | Remote (US) | Remote | Enterprise (IPG subsidiary) | **Winter 2027, starts Jan 11 2027** | Confirm ≤ Mar 12 | Paid (amount unconfirmed) | 2 | ~4 | Med | closed | [Intern Insider](https://interninsider.me/internships/acxiom/data-scientist-intern-4cbf6892-4c7d-4cdc-b96a-0ce4b538fd8c) |
| A141 | Acxiom | Data Engineer Intern | Data | Remote (US) | Remote | Enterprise (IPG subsidiary) | **Winter 2027, starts Jan 11 2027** | N/A — no longer posted | Paid (amount unconfirmed) | 2 | ~3 | Low | closed | [Intern Insider](https://interninsider.me/internships/acxiom/data-engineer-intern-6c7445b5-ef99-4431-8856-72ecbe810648) |
| A142 | Acxiom | Intern - Product Strategy & Innovation | Strategy | Remote (US) | Remote | Enterprise (IPG subsidiary) | **Winter 2027, starts Jan 11 2027** | Confirm ≤ Mar 12 | Paid (amount unconfirmed) | 2 | ~2 | Low | closed | [Intern Insider](https://interninsider.me/internships/acxiom/intern-product-strategy-innovation-637d488b-b4f8-4e61-a1fa-e06ce51470d0) |
| A143 | CBIZ | Business Operations Intern (Spring 2027) | Strategy | New York, NY | Hybrid (≥3 days/wk onsite) | Enterprise (accounting/advisory) | Spring 2027 (tagged) | Unconfirmed | $45–55K/yr (aggregator estimate, not employer-stated) | 3 | ~3 | Low/Med | unverified | [CBIZ Careers](https://ebez.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/6474) |
| A144 | Rundoo | Product Manager Intern | PM | Redwood City, CA | In-person | Series-funded ($48M raised; Battery/Bessemer/CRV) | **Summer 2027 term (confirmed) ⚠** | Rolling | $2,461/wk (~$122K/yr annualized) | 2 | ~5 | Low | closed | [Ashby](https://jobs.ashbyhq.com/rundoo/b7d71a5a-4a88-4e97-a6db-e0446eefb389) |
| A145 | Energy and Environmental Economics (E3) | 2027 Consulting Internship | Strategy | San Francisco, CA / Boston, MA / New York, NY / Calgary, AB | Hybrid (≥3 days/wk office) | Boutique (energy economics consulting) | Flexible, 8–12 wk min ⚠ (grad-year eligibility unclear) | Confirm ≤ Mar 12 | $30–45/hr | 3 | ~3 | Med | live | [Lever](https://jobs.lever.co/ethree/4e029b3e-2c44-4f90-a04c-3980f4dedd57) |
| A146 | Gemini | Product Management Intern (Winter 2027) | PM | New York, NY | In-person (3 days/wk) | Public (crypto/Web3 exchange) | **"January to April 2027" (explicit, semester-long) ⚠** | Unconfirmed | Unconfirmed | 3 | 4 | Low | conflict | [Greenhouse](https://boards.greenhouse.io/embed/job_app?for=gemini&token=8214332&gh_jid=8214332) |
| A147 | Tesla | Service Program & Project Management Intern | PM | Austin, TX | Unconfirmed | Public | Spring 2027 (tagged); SimplifyJobs README tags this exact req 🎓 (advanced-degree marker) ⚠ | Unconfirmed | Unconfirmed | 4 | 3 | Med | blocked | [Tesla Careers](https://www.tesla.com/careers/search/job/283443) |
| A148 | Clearwater Analytics (CWAN) | Product Management Intern (Technical Product Manager) | PM | New York, NY | Unconfirmed | Public (NYSE: CWAN) | Unconfirmed ("Winter 2026" tag ambiguous ⚠) | Unconfirmed | Unconfirmed | 3 | 3 | Low/Med | unverified | [Built In NYC](https://www.builtinnyc.com/job/product-management-intern/11265249) |
| A149 | MetLife | Group Benefits Sales Intern | Sales | New York, NY | Hybrid | Public (Fortune 100) | Unconfirmed ⚠ (no season stated) | Unconfirmed | $24/hr | 4 | 3 | Low | unverified | [Built In NYC](https://www.builtinnyc.com/job/group-benefits-sales-intern-new-york-ny/11265346) |
| A150 | HP (Hewlett Packard) | Personal Systems Product Management Intern | PM | Austin, TX | Unconfirmed | Public | Unconfirmed ("Winter 2026" tag ambiguous ⚠) | Unconfirmed | $29–33/hr | 3 | 3 | Low/Med | unverified | [HP Workday](https://hp.wd5.myworkdayjobs.com/EXTEU-AC-CareerSite/job/Austin-Texas-United-States-of-America/Personal-Systems-Product-Management-Intern_UNI4755) |
| A151 | Kroll | Intern, Trade and Customs | Strategy (economic/policy analysis, econ-consulting-adjacent) | New York, NY | In-person | Established (global risk/financial advisory) | Rolling, no stated term ⚠ | Rolling (no deadline set — see note) | $20–35/hr | 3 | 4 | Med | live | [Kroll Careers](https://careers.kroll.com/en/job/new-york/intern-trade-and-customs/21014747) |
| A152 | GE Aerospace | SaaS – Flight Analytics Platform, Data Science Co-op (Spring 2027) | Data | Austin, TX | In-person | Public (Fortune 500 aerospace) | Spring 2027 (tagged); full-time co-op, no exact term dates stated ⚠ | Confirm ≤ Mar 12 | $24/hr+ (rises per undergrad year) | 3 | ~4 | Med | unverified | [GE Workday, req R5040450](https://geaerospace.wd5.myworkdayjobs.com/ge_externalsite/job/Austin/SaaS---Flight-Analytics-Platform---Data-Science-Co-op---Spring-2027_R5040450-2) |
| A153 | Contoro Robotics | Business Development Intern | BD | Austin, TX | In-person | Early-stage (robotics) | Rolling, no stated term | Rolling | Unconfirmed | 2 | ~4 | Med | closed | [Built In Austin](https://builtin.com/job/business-development-intern/11318430) |
| A154 | Compass Lexecon (FTI Consulting) | Intern, Competition Practice | Strategy | Madrid, Spain | Hybrid | Established (economic consulting) | No fixed start stated; firm describes 3–6 month internships "during, in-between, or shortly after" the economics degree ⚠ | Rolling review; apps close 26 Feb 2027 | Unconfirmed ("competitive salary and benefits") | 3 | ~4 | Low | blocked* | [Compass Lexecon Workday, req JR261344](https://fticonsulting.wd108.myworkdayjobs.com/CompassLexeconCareers/job/Madrid-Spain/Intern---Competition-Practice---Madrid_JR261344) |
| A155 | Clearwater Analytics (CWAN) | Data Management & Reporting Intern | Data | New York, NY (1 Rockefeller Plaza) | Hybrid | Public (NYSE: CWAN) | Unconfirmed (no season/term field on posting; datePosted 2026-09-23, validThrough 2026-10-23 is an application window, not a term) | Unconfirmed | Unconfirmed (listing shows a $0–$10,000,000/yr placeholder — clearly bad data, not real) | 3 | ~4 | Med | unverified | [Built In NYC](https://www.builtinnyc.com/job/data-management-reporting-intern/11340560) |
| A156 | Workiva | Spring 2027 Intern – Data Analytics | Data | Remote (US); hybrid option near NYC/SF/Austin office hub | Remote | Public (NASDAQ: WK) | Same Spring 2027 cycle pattern as closed sibling reqs A115/A117/A118 (Jan 4, 2027 start, 15–20 hrs/wk) — inferred, not independently confirmed on this specific req's own page ⚠ | **Closed 30 Sep 2026 (confirmed — req returns 0 results)** | $22.00/hr (confirmed, req R12319) | 2 | ~3 | Med | closed | [Workiva Workday, req R12319](https://workiva.wd503.myworkdayjobs.com/careers/job/USA---Remote/Spring-2027-Intern---Data-Analytics_R12319) |
| A157 | Scout (YC) | Growth & Operations Intern | Growth | San Francisco, CA | Remote (in-person SF optional) | YC-backed | Rolling | Rolling | $20/hr | 2 | ~3 | Med | live | [Work at a Startup](https://www.workatastartup.com/jobs/68076) |
| A158 | Utilyze | Partnerships Intern | Partnerships | Austin, TX / Boston, MA / New York, NY / San Antonio, TX / San Francisco, CA | In-person or Remote (candidate's choice) | Early-stage | Rolling | Rolling | Unpaid (equity/commission possible; academic credit supported) | 1 | ~4 | Med | live | [Wellfound](https://wellfound.com/jobs/4658879-investment-marketing-intern-clone) |
| A159 | Wonder | Growth & Marketing Analytics Intern | Growth/Data | New York, NY | Hybrid (3 days/wk, up to 5) | Late-stage (food-tech, Marc Lore-founded) | Unconfirmed — no explicit dates in posting; Simplify tags "Winter 2026" term ⚠ | Confirm ≤ Mar 12 | $36/hr | 3 | ~5 | Med | unverified | [Workday](https://wonder.wd1.myworkdayjobs.com/WG/job/New-York-NY/Growth---Marketing-Analytics-Intern_JR101323) |
| A160 | Metropolitan Transportation Authority (MTA) | Ridership Analysis and Modeling, Emerging Talent Intern (Spring) | Data | New York, NY (Manhattan) | In-person | Public agency | Spring (title confirms) | Confirm ≤ Mar 12 | $21/hr (Grad only — no undergrad tier found, confirmed twice) | 2 | ~1 | Low | blocked | [MTA/Jobvite](https://jobs.jobvite.com/metropolitantransportationauthority/job/oW1PAfw6) |
| A161 | Metropolitan Transportation Authority (MTA) | EAM Value Realization, Emerging Talent Intern (Spring) | Data | New York, NY (Manhattan) | In-person | Public agency | Spring (title confirms) | Confirm ≤ Mar 12 | $19/hr (Undergrad) / $21/hr (Grad) | 2 | ~4 | Med | live | [MTA/Jobvite](https://jobs.jobvite.com/metropolitantransportationauthority/job/orDQAfwe) |
| A162 | VaynerMedia | Resident - Data Analytics | Growth | New York, NY | Hybrid (3–4 days/wk onsite) | Established (agency) | "Next residency class" starts Jan 2027; fixed 3-month term ⚠ | Apr 2027 ⚠ (inferred, 3mo from Jan start) | $20/hr ($30/hr OT) | 3 | ~4 | Low | conflict | [VaynerMedia careers](https://vaynermedia.com/careers?gh_jid=8126062) |
| A163 | Fenwick & West | Forward Deployed Operations Intern | Strategy (technical-adjacent) | New York, NY / San Francisco, CA (candidate's choice; also Boston/Seattle/Santa Monica/DC) | In-person, part-time ("on occasion") | Established (AmLaw 100) | "Expected to run through fall of 2026 and into winter of 2027" — ambiguous cohort ⚠ | Confirm ≤ Mar 12 | $21–25/hr | 3 | ~4 | Med | unverified | [Fenwick Workday, req R2964](https://fenwick.wd1.myworkdayjobs.com/Fenwick_External_Careers/job/Silicon-Valley/Forward-Deployed-Operations-Intern_R2964) |
| A164 | Energy and Environmental Economics, Inc. (E3) | 2027 Consulting Internship | Strategy | San Francisco, CA / New York, NY / Boston, MA / Calgary, AB (candidate's choice) | Hybrid (min. 3 days/wk in-office) | Established (boutique energy/climate-policy econ consulting) | 8–12 weeks, candidate-proposed dates; hiring cycle interviews Jan / decisions Feb 2027 ⚠ | Confirm ≤ Mar 12 | Unconfirmed ("full time hourly internship position") | 3 | ~4 | Med | conflict | [E3 Lever](https://jobs.lever.co/ethree/4e029b3e-2c44-4f90-a04c-3980f4dedd57) |
| A165 | Figma | Data Science Intern (2027) | Data | San Francisco, CA / New York, NY | In-person (assumed; not explicitly labeled) | Established (public, design/dev-tool) | Unconfirmed — no season or dates stated anywhere in posting ⚠ | Unconfirmed | $46/hr + housing stipend + travel reimbursement | 4 | ~4 | Med | unverified | [Figma Greenhouse](https://job-boards.greenhouse.io/figma/jobs/6178857004) |
| A166 | Stripe | Data Analyst, Intern | Data | Chicago, IL / New York, NY / Seattle, WA / South San Francisco, CA | Hybrid (min. 50% time in local office stated) | Established (public-adjacent, API/fintech) | Unconfirmed — no term length/dates stated; eligibility targets Dec 2027/Spring-Summer 2028 grads ⚠ | Unconfirmed | $117,000/yr stated as base-salary field — unusual annual framing for an internship, flagged ⚠ | 5 | ~4 | Med | unverified | [Stripe careers](https://stripe.com/jobs/search?gh_jid=8194291) |
| A167 | Dell Technologies | Corporate Strategy Undergraduate Intern | Strategy | Austin, TX | In-person | Enterprise (public) | Unconfirmed — no term/duration/start date stated anywhere ⚠ | Nov 1 2026 (rolled from Oct 17) | $27.10–$31.80/hr | 3 | ~4 | Med | closed | [Intern Insider](https://interninsider.me/internships/dell-technologies/corporate-strategy-undergraduate-intern-5d8b93b4-cec5-46fa-8607-0970c493600a) |
| A168 | xAI | Business Operations Internship/Co-op (Spring 2027) | Strategy (Business Ops) | Palo Alto, CA | In-person (onsite required) | Frontier AI (private) | Jan or Mar 2027 start, 12-wk min — overruns Mar 12 by ~2.5 wks ⚠ | Rolling | $24.50–$26/hr + relocation stipend | 5 | ~4 | Med | conflict | [xAI Greenhouse](https://job-boards.greenhouse.io/xai/jobs/5255113007) |
| A169 | Metropolitan Transportation Authority (MTA) | Data Analysis (Supplier Relations), Emerging Talent Intern (Spring) | Data | New York, NY (Manhattan) | In-person | Public agency | Spring (title confirms) | Confirm ≤ Mar 12 | $19/hr (Undergrad) | 2 | ~3 | Med | live | [MTA/Jobvite](https://jobs.jobvite.com/metropolitantransportationauthority/job/oOvWAfwz) |
| A170 | FOX News Media | Spring 2027 FOX News Media Internship Program – Data Analytics (New York) | Data | New York, NY | In-person, part-time (16–24 hrs/wk) | Enterprise (FOX Corp subsidiary) | **Monday, February 8, 2027 – Friday, April 16, 2027 (explicit, employer-stated)** | **Apr 16 2027 ⚠** (explicit, ~5 wks past hard stop) | $20.00/hr (employer-stated pay disclosure) | 4 | ~3 | Low | conflict | [FOX Workday](https://fox.wd1.myworkdayjobs.com/Domestic/job/New-York-New-York-USA/Spring-2027-FOX-News-Media-Internship-Program---Data-Analytics---New-York_R50033950) |
| A171 | Metropolitan Transportation Authority (MTA) | Operations Support, Emerging Talent Intern (Spring) | Data/Ops | Brooklyn, NY | In-person | Public agency | Spring (title confirms) | Confirm ≤ Mar 12 | $19/hr (Undergrad) / $21/hr (Grad) | 2 | ~3 | Med | live | [MTA/Jobvite](https://jobs.jobvite.com/metropolitantransportationauthority/job/oBqYAfwj) |
| A172 | Tesla | Data Analyst Intern, People Products | Data | Palo Alto, CA / Austin, TX | Unconfirmed | Public | Spring 2027 (tagged) | Unconfirmed | Unconfirmed | 4 | ~4 | Low | unverified | [Tesla Careers](https://www.tesla.com/careers/search/job/286085) |
| A173 | Pennant (YC S26) | Founder Fellow – GTM, Growth & Strategy | Strategy | New York, NY | In-person (IRL required) | YC S26 | Seasonal, rolling — no fixed dates stated | Confirm ≤ Mar 12 | Unconfirmed (no pay listed on posting) | 2 | ~4 | Med | live | [Work at a Startup](https://www.workatastartup.com/jobs/111722) |
| A174 | Zipline | Change Management Intern (Spring 2027) | Data/Ops | South San Francisco, CA | In-person | Series C | Jan–Apr 2027 (explicit) ⚠ | Rolling | Unconfirmed | 4 | ~3 | Low | conflict | [Greenhouse](https://job-boards.greenhouse.io/flyzipline/jobs/7990677003) |
| A175 | GE Aerospace | SaaS – Flight Analytics Platform, Data Science Co-op (Spring 2027) | Data | Austin, TX | Unconfirmed | Enterprise (public) | Unconfirmed — no term/duration/start date stated anywhere | Confirm ≤ Mar 12 | Unconfirmed | 4 | ~4 | Med | unverified | [GE Workday](https://geaerospace.wd5.myworkdayjobs.com/ge_externalsite/job/Austin/SaaS---Flight-Analytics-Platform---Data-Science-Co-op---Spring-2027_R5040450-2) |
| A176 | Gemini | Product Management Intern (Winter 2027) | PM | New York, NY | Hybrid (3 days/wk in-person stated) | Public (crypto/Web3) | Jan–Apr 2027 (explicit, "January to April 2027") ⚠ | Apr 2027 ⚠ | $45/hr | 4 | ~4 | Med | conflict | [Gemini Greenhouse](https://job-boards.greenhouse.io/gemini/jobs/8214332) |
| A177 | Snowflake | Product Marketing, AI-Powered Data Engineering Intern (Winter 2027) | Growth (ambiguous — GTM/storytelling, flagged) | Menlo Park, CA | In-person | Public (cloud data platform) | Winter 2027, 12 wks (exact dates unconfirmed) | **Apply by Oct 31 2026 (rolled from Oct 23; same soft/rolling pattern as A93/A95/A167)** | $40–47/hr | 5 | ~3 | Med | closed | [Intern Insider](https://interninsider.me/internships/snowflake/product-marketing-ai-powered-data-engineering-intern-bce11b17-b8bc-41f3-aaf2-82f86d363f52) |
| A178 | 1Password | Data Intern – Product Analytics (Winter 2027) | Data | Remote (US/Canada) | Remote | Private, late-stage ($500M+ ARR security) | **Jan–Apr 2027 (explicit, "4 months") ⚠** | Apr 2027 ⚠ | Unconfirmed | 3 | ~3 | Med | closed | [Ashby](https://jobs.ashbyhq.com/1password/412c1aac-13ce-4cc9-9c81-90a9a7a2ee48) |
| A179 | Four Hands | Business Operations Analyst Intern (Spring 2027) | Strategy | Austin, TX | In-person (listing tagged Hybrid, inconsistent) | Private, mid-size (furniture/home goods) | **Jan–Apr 2027 (explicit, through Spring term) ⚠** | Apr 2027 ⚠ | Unconfirmed | 2 | ~3 | Med | conflict | [Built In Austin](https://builtin.com/job/business-operations-analyst-intern/11757970) |
| A180 | Metis Strategy | Strategy & Management Consultant Intern | Strategy | Walnut Creek, CA (East Bay) | In-person (stated) | Boutique (C-level/executive advisory) | Unconfirmed — no term, duration, or start/end date stated | Confirm ≤ Mar 12 | Unconfirmed (bonus-eligible mentioned, no base rate) | 3 | ~4 | Med | unverified | [Simplify.jobs listing](https://simplify.jobs/p/936f4d3a-b666-4fd0-9058-179c23beac04/Strategy--Management-Consultant-Intern) |
| A181 | PatientPoint | Business Development Intern | BD | New York, NY | Hybrid (listing header says "In-Office," but company copy on the same posting describes PatientPoint as "remote-first" with a "Hybrid Workspace," "Typical time on-site: Flexible" — flagged as the classic onsite-that's-really-remote pattern) | Private, mid-size (healthcare/patient-engagement tech) | Unconfirmed — no season stated on the NYC posting itself; a sibling PatientPoint internship (Inside Sales, Cincinnati, same $20–23/hr band, posted Oct 23 2026) is explicitly an 8-week rolling term with "flexible working hours to accommodate academic schedules," comfortably inside the 10-week window if this role runs the same way | Confirm ≤ Mar 12 | $20–23/hr | 2 | ~3 | Med | live | [Built In NYC](https://builtin.com/job/business-development-intern/11883424) |
| A182 | PatientPoint | Client Sales Intern | Sales | New York, NY | Hybrid (listing header says "In-Office," but the role description itself says "Hybrid Schedule" — same onsite-that's-really-remote ambiguity as A181) | Private, mid-size (healthcare/patient-engagement tech) | Unconfirmed — no season stated; same sibling-program logic as A181 | Confirm ≤ Mar 12 | $20–23/hr | 2 | ~3 | Med | live | [Built In NYC](https://builtin.com/job/client-sales-intern/11916671) |

**2026-10-08 sweep — no corrections to status (A112/A114 TikTok Sydney re-verified, no drift; A152
GE Aerospace and A163 Fenwick & West re-verified via direct Workday API fetch, notes updated with
newly confirmed facts, status unchanged on both), 3 new Tier A rows (A164 E3 Consulting Internship,
conflict; A165 Figma Data Science Intern, unverified; A166 Stripe Data Analyst Intern, unverified),
no closures.** See the "Last swept" header at the top of this file for full detail.

**2026-10-07 sweep — 1 correction (A160 downgraded `unverified` → `blocked` on confirmed grad-only
eligibility), 3 new Tier A rows (A161 MTA, live; A162 VaynerMedia, conflict; A163 Fenwick & West,
unverified), no closures.** See the "Last swept" header at the top of this file for full detail on
today's re-verification pass and both sweep passes.

**2026-10-06 sweep — no corrections to status, 1 new Tier A row (A160 MTA, unverified), no
closures.** See the "Last swept" header at the top of this file for full detail on today's
re-verification pass and source sweep.

**2026-10-05 sweep — no corrections, 1 new Tier A row (A159 Wonder, unverified), no closures.** See
the "Last swept" header at the top of this file for full detail on today's re-verification pass and
both sweep passes.

**2026-10-01 sweep — 5 corrections, 2 new Tier A rows (A157, A158), no closures.** New: **A157,
Scout** — a YC-backed CPG-focused startup's Growth & Operations Intern, San Francisco, $20/hr,
remote by default with an in-person SF seat available, verified directly on the YC mirror page
(workatastartup.com itself is still a client-rendered shell for automated fetch, same standing
limitation as A5/A9/A13/A65/A75/A82/A83). One listed task — drafting/publishing LinkedIn posts —
is a content-creation sliver inside an otherwise ops/data-research role; kept rather than excluded
per PROFILE.md's substance test, but flagged. **A158, Utilyze** — Partnerships Intern, unpaid,
in-person-or-remote candidate's choice across five cities including Austin (home market); found on
Wellfound under a mislabeled "Investment Marketing Intern" URL slug left over from a cloned listing,
but the live page content is the Partnerships Intern role — direct BD/partnerships work matching a
named-priority function. Corrections: A5 (Dalus) mode resolved to confirm an actual SF in-person
seat exists; A75 (Surface Labs) mode flipped again in its ongoing oscillation, now SF-preferred/
India-remote with a newly-confirmed 3-month commission-only → full-time conversion; A88 (FairwAI)
dropped Austin from its hub-city list (never actually listed) and added the unpaid/10–20 hrs-wk
detail; A120 (MTA) resolved its "Confirm ≤ Jan 2027" flag — the posting's own title now reads
"...(Spring)"; A145 (E3) corrected from in-person/SF-only to hybrid (≥3 days/wk office) across four
cities (SF/Boston/NYC/Calgary), plus a newly-found $30–45/hr pay figure. Checked without changing:
A136's Intern Insider mirror re-asserted the NYC-on-site claim this tracker already resolved in
Workday's favor on 2026-09-20 (left as Remote/Homebased); A134/A135/A137/A140/A142's Intern Insider
"Apply by" badges advanced to Sep 30/Oct 2/Oct 8 exactly as the already-documented non-authoritative
countdown pattern predicts (not real deadlines); A82/A83's in-person classification could not be
independently re-confirmed this round (location only) — worth a closer look, not downgraded on
partial evidence; A65's "rolling" read stands against the primary YC source despite a secondary
aggregator describing a fixed 3-month term; A121's Workday req still wouldn't render for fetch, and
an external same-titled posting carries a different, unconfirmed cohort label.

**2026-09-27 sweep — no corrections, full re-verification of all 36 `live` Tier A rows found every
previously-logged caveat still accurate, nothing drifted.** The 7 `workatastartup.com`-hosted rows
(A5, A9, A13, A65, A75, A82, A83) remained unreadable via WebFetch — pure client-rendered JS shells,
same standing limitation as every prior sweep, no status change. Everything else opened cleanly with
real content and matched the tracker exactly: A92 (TraceRoot.AI), A88 (FairwAI), A22 (CertiK),
A70/A128–A133 (Base Power, 6 reqs), A96 (Crowe Global), A98 (Cresta), A120 (MTA), A121 (Ankura), A130
(Kodiak), A145 (E3), A151 (Kroll), A153 (Contoro) all confirmed unchanged from prior sweeps.

**New: A155, Clearwater Analytics (CWAN) — Data Management & Reporting Intern, New York.** A second,
distinct CWAN NYC intern req (companion to A148's PM Intern, same office/company) — SQL/Python/
Tableau/Power BI reporting work on CWAN's platform, and unlike A148 explicitly names **Economics**
as a qualifying major for a sophomore/junior. Kept `unverified` (not `live`) for the same reason as
A148: the posting's own schema.org metadata carries no season/term field at all, so a Jan–Mar 2027
fit is unconfirmed. Listed pay is broken placeholder data ($0–$10,000,000/yr), not real.

**Considered and correctly left out:** Compass Lexecon's sibling US req ("2027 Analyst Interns – US,"
JR261385, Chicago/NYC/Boston/LA/DC, $50/hr) — explicitly Summer 2027 (June–Aug), confirmed still out
of window. Envoy's SF "Solutions Engineering Intern" (found via the SimplifyJobs off-season README)
was checked and left out: no dates/pay/eligibility stated anywhere, and the actual substance is
AI/LLM-agent tooling work, not the customer-facing pre-sales lane PROFILE.md targets — too thin and
too poor a fit to clear the quality bar.

Fresh sweep of every-run sources found nothing else clearing the bar: `workatastartup.com` still a
pure client-rendered shell with zero visible postings; `wellfound.com/jobs` general listing was
full-time-only this run; Analysis Group, Cornerstone Research, and NERA's own careers pages showed
nothing intern-relevant (NERA's search-hit postings are now 410 Gone); CRA's Greenhouse board had
only EU (Brussels/Düsseldorf/Munich) intern reqs, no US; Brattle's live-openings page was bot-gated
(403/empty shell) — genuinely inconclusive, not confirmed-empty. Peer firms Bates White and BRG both
confirmed summer-only programs; Edgeworth had no intern-level roles at all. Coral Capital, TokyoDev,
and japan-dev.com re-checked — no Tokyo internships in scope. Australia's GradConnection Sydney page:
EY and Treasury vacationer programs are citizen/PR-only (hard-blocked for a 462 visa); KPMG's
rolling-intake vacationer program runs only 3–8 weeks from ~November, too short and too early for the
Jan 4 window.

**2026-09-26 sweep — three corrections (A115/A117/A118 Workiva upgraded unverified → live), one new
Tier A row (A154 Compass Lexecon Madrid, blocked).** Re-verified the imminent-deadline rows via
primary sources rather than aggregators: **A112/A114 (TikTok)** unchanged, still closing 30 Sep 2026
1:59pm. **A134–A137/A140/A142 (Acxiom cluster)** all 8 reqs confirmed still open/live directly on
Acxiom's own Workday tenant (`acxiomllc.wd5.myworkdayjobs.com/AcxiomUSA` — the correct tenant; prior
notes' domain guess was wrong), Jan 11 2027 start unchanged across the board. **A115/A117/A118
(Workiva)** confirmed directly on Workiva's own Workday (`workiva.wd503.myworkdayjobs.com/careers`,
not the 403'ing workiva.com/careers or the aggregator) — all three still open, closing Sept 27 2026
as flagged. Two real corrections here: pay is now confirmed for A115 ($22/hr, previously
unconfirmed) and A118 ($21/hr, previously unconfirmed; also revealed as two separate live reqs
sharing one title). And Workiva's own site labels this intake "Spring 2027" (A117: "Spring & Summer
2027"), not "Winter 2027" as this tracker had it — the actual Jan 4, 2027 start date is unchanged, so
this is a label correction, not a schedule change. Upgraded all three unverified → live given the
primary-source confirmation.

**New: A154, Compass Lexecon's Madrid Competition Practice internship** — found on the firm's real
ATS (Workday, not a snippet), a genuine hit from the every-run economic-consulting search and
PROFILE.md's #1-named firm alongside Analysis Group/Cornerstone/CRA. Real, unresolved caveats kept it
out of `live`: (1) **gated on the same Spain convenio de prácticas question as the Barcelona/Madrid
Tier C rows below** — UT Austin has not yet been asked to sign, so this is blocked on the same
unresolved prerequisite; (2) no explicit start date — the posting describes 3–6 month internships
taken "during, in-between, or shortly after" the economics degree and says the firm typically hires
"in their final year," which is a plausible eligibility mismatch for a rising junior; applications
are reviewed on a rolling basis through 26 Feb 2027, so an actual Jan–Mar 2027 start is not confirmed
either way. Kept per the never-drop-a-strong-lead rule rather than dropped, `blocked*` rather than
`live`, pending both the convenio answer and a direct question about start-date flexibility. A
sibling req on the same board, "2027 Analyst Interns – US" (Chicago/NYC/Boston/LA/DC), is explicitly
Summer 2027 (June–Aug) and out of window — not added.

Fresh sweep of the other every-run sources (workatastartup.com, wellfound.com/jobs, the remaining
economic-consulting firms' own careers pages, Palantir's Lever board for Deployment Strategist) found
nothing else clearing the bar — workatastartup.com is still a bare JS shell (YC Winter 2027 batch not
expected until ~November 2026), Palantir's board shows only full-time Deployment Strategist reqs (Tel
Aviv/Copenhagen/London/NYC-Government, no internship version), and Analysis Group/Cornerstone/CRA/
Brattle/NERA's own careers pages showed no internship-specific req (CRA's jobs subdomain failed to
resolve this run — inconclusive rather than confirmed-empty, worth another look next sweep).

**2026-09-23 sweep — no corrections, two new Tier A rows (A152 GE Aerospace, unverified; A153 Contoro
Robotics, live), no closures.** Re-verified the two nearest-term deadlines (A115 Workiva, still
unverified for the major-mismatch reason documented 2026-09-20; A112/A114 TikTok, still closing 30
Sep 2026) with zero drift. A152: GE Aerospace's SaaS – Flight Analytics Platform Data Science Co-op
(Austin) — confirmed directly on GE's own Workday API, genuinely quantitative content (dashboards,
A/B testing, KPI tracking, feature engineering), $24/hr+ rising per undergrad year, but the posting's
own `timeType` reads "Full time" with no explicit end date beyond a "Spring 2027" tag, which risks
overrunning the 12 Mar hard stop and sits in tension with staying enrolled — kept `unverified` rather
than `conflict` pending a direct question on exact term length. A153: Contoro Robotics' Business
Development Intern (Austin) — confirmed directly on Built In Austin's own page, real CRM/pipeline/
account-research/outbound substance clearing the analytical-BD bar, one caveat (field role, requires
a driver's license and overnight travel to customer sites) — kept `live`. Fresh sweep of economic
consulting firms and the SimplifyJobs off-season README found nothing else clearing the bar (all
previously tracked or hard exclusions, e.g. grad-only Rivian/Tesla/Block postings).

**2026-09-16 sweep — two corrections (A112, A114 — imminent deadline pulled forward from Dec to
Sep), seven new Tier A rows (A131–A137), no closures.** Full detail is in the header summary above;
per-row notes below.

**A131–A133 (Base Power Company)** — a fresh crawl of Base Power's own company jobs page (already
today's second visit, following up on the A128/A129 finds from 2026-09-15) turned up three more
open reqs not seen yesterday: **A131 (Financial Planning Intern)** — budgeting, forecasting,
variance analysis, financial modeling, same Data/Finance lane as A129, scored the same. **A132
(Marketing Intern)** — sits on the Growth team, campaign-performance analysis via HubSpot, funnel
work, member acquisition, plus some outbound support alongside sales; clears the substance-over-
title test (real analytics/CRM work, not content/social), so kept in scope per PROFILE.md's
quantitative-growth carve-out. **A133 (Deployments Operations Intern)** — physical-logistics
coordination (installation scheduling, crew coordination, inventory flow, KPI tracking for
on-time performance) for Base's field deployment teams. A weaker fit than A128/A129/A131/A132 —
closer to field/supply-chain ops than the economics-flavored Strategy & Ops lane PROFILE.md
describes for Uber/DoorDash — kept in per the never-drop-a-real-open-role rule but scored low.
All three: home market (Austin), no relocation cost, no season/dates or pay stated on the postings
(same "Unconfirmed" pattern as every other Base Power row), confirmed live via direct fetch.

**A134–A137 (Acxiom)** — best new find of this sweep. Four distinct internship reqs at Acxiom (data
and identity-resolution services for marketing/advertising agencies, part of the Interpublic Group
of Companies), surfaced via Intern Insider's Winter 2027 term page and each opened directly at its
own URL (not a search snippet). All four explicitly state **Winter 2027, starting January 11,
2027** — an unusually clean near-match to the 4 Jan 2027 target start — 20–25 hrs/week during the
semester (up to 40 hrs/week during breaks), paid, and require permanent US work authorization with
no future visa sponsorship (fine for Sam). None state an explicit end date beyond "during the
semester," which could plausibly run into April/May — kept `Confirm ≤ Mar 12` rather than assumed
either way. **A134 (Intern, Agency Partnerships)** — New York, in-person; Economics and Data
Science both explicitly named among relevant fields — strong Partnerships fit. **A135 (Intern,
Product Management)** — remote, part-time; PM function. **A136 (Enterprise Solutions Consulting
Intern)** — New York, in-person; broad consulting-generalist scope (Business Administration,
Marketing, Finance, Economics, Data Science, CS all listed as relevant fields) — the closest of the
four to PROFILE.md's Strategy lane. **A137 (Intern, Financial Analyst)** — New York, in-person;
Finance/Accounting/Economics/Business Administration relevant fields, same Data/Finance lane as
A129/A131. One flag worth noting: Intern Insider's own "Apply by Sep 18" badge on all four postings
is explicitly self-labeled ("No official deadline listed — this is our recommended window"), not a
real deadline — treated as rolling per the same aggregator-invented-deadline skepticism already
applied to A92/A98/A121, not as a real Sept 18 cutoff. Status kept `unverified` rather than `live`:
two attempts to independently corroborate on Acxiom's own site (acxiom.com/careers/, and a guessed
Workday tenant) both failed (timeout, then HTTP 500) — genuine access limitation, not a content
problem, so kept per the never-drop rule pending a future direct hit.

**Correction: A112 and A114 (TikTok, GradConnection Sydney) — application deadline pulled forward
by three months.** Both postings were re-opened directly and their shared GradConnection campaign's
own embedded JSON now exposes an explicit `interval` field: `{"start":"2026-09-01T00:00:00+00:00",
"end":"2026-09-30T13:59:00+00:00"}`, matching the page's own "Closing in 14 days" banner exactly.
The 25 Dec 2026 deadline tracked since 2026-08-28/08-30 was wrong (likely a stale read of the
platform-wide "Closing in 3 months" language seen on an earlier sweep, never corrected against the
campaign's own structured data until this run). **Real, actionable correction — both close 30 Sep
2026, roughly two weeks from this sweep.** No other field changed on either row.

**Fresh sweep of all ten required sources found nothing else that clears the quality bar beyond the
above.** YC Winter 2027 batch: still pre-landing, consistent with 2026-09-15's finding (applications
close Nov 2 2026, decisions land Dec 11 2026); workatastartup.com/wellfound.com general listing
pages remain pure client-rendered carousels with no server-side job data, same standing limitation.
Economic consulting, checked directly again: Analysis Group's `/careers/students/` still 404s;
Cornerstone's general `/careers/` page (the "March 1, 2027" language found on 08-27 lives on a
different sub-page not re-located this run) is still generic program-description-only with zero
`2027` or `intern`-context matches beyond boilerplate; Charles River Associates' Greenhouse board
still shows exactly the same two Brussels/Düsseldorf/Munich European-practice reqs, no new US req;
Compass Lexecon's `/careers/` page still has no readable role content (only nav-menu false-positive
matches on "international"); Brattle still 403s; NERA's FAQ verbatim: "Yes, we offer summer
internships to final-year undergraduate candidates as well as current master's and PhD students" —
still no real off-cycle track. Palantir: `jobs.lever.co/palantir` crawled in full again — the
"Deployment Strategist, Internship" reqs are still exactly Paris and Honolulu, unchanged, despite a
much larger non-internship Deployment Strategist req count this run (new Tokyo, Madrid, Seoul, and
multiple US-government full-time postings). Uber: careers page is a pure Next.js client shell with
no server-rendered job data. DoorDash: `careersatdoordash.com` still 403s direct fetch. Flexport:
still exactly one internship company-wide (Tradelane Operations, unchanged locations). Tokyo:
`coralcap.co/jobs/` still 404s; `japan-dev.com/jobs` is now a heavier Nuxt/Algolia client app with
no server-rendered job titles at all (genuinely unparseable from raw HTML, not merely dry — a
slightly worse state than the prior "loads but SWE-only" finding); `tokyodev.com/jobs` loaded fully
and still shows only engineering titles (DevOps/Full-Stack/QA). GradConnection Sydney
business-and-commerce board: 94 listed roles, all already-tracked (TikTok) or already-excluded
(EY/KPMG/ANZ vacationer programs, Treasury, SG Fleet, NTT DATA Marketing Intern) — zero new
companies. SimplifyJobs off-season README (1,652,031 bytes fetched raw, PM table 254 rows / DS
table 1,936 rows parsed programmatically): beyond the three Base Power/Acxiom-adjacent finds above
and already-tracked Tesla/Zipline/Kodiak/MTA rows, every other target-city Winter/Spring 2027 match
was wrong-function (engineering, hardware, PhD-only) or wrong-candidate-level — one specifically
checked and excluded: Google's "Data Analytics Apprentice – February 2027 Start" (NYC among four
locations, Winter 2027 tag) explicitly states the apprenticeship is for people who do *not* hold or
are not pursuing a related degree ("If you are currently pursuing or hold a degree in data
analytics... browse our University Graduate and Internship opportunities instead") — disqualifying
for an Econ/Stats-DS-minor candidate. BuiltIn NYC/Austin/SF general internship pages (25 listings
each): all target-function-adjacent titles found were either already-tracked/excluded (PwC
CMAAS/audit/tax across all three metros, Smartly's Fall-2026 Creative Strategy/Product Marketing
Interns in NYC) or clearly wrong-function (customer-onboarding, recruiting-operations) — nothing
addable beyond the Base Power company-page crawl. Intern Insider's five role-facet URLs from prior
sweeps now all 404 (site restructured its facet paths since 2026-09-13); substituted the Winter 2027
term page (368,094 bytes, 54 distinct company/role pairs after de-duplication) as the working
equivalent this run — surfaced the four new Acxiom rows above; everything else on the page was
either wrong-function (agronomy, HR co-op, construction, chemical/mechanical/industrial engineering
co-ops) or wrong-candidate-level (PhD/co-op programs at J&J, Marmon, Raytheon).

**A70 (Base Power) corrected, not closed.** The tracked `builtinaustin.com/job/growth-intern/10000211`
URL now serves "Sales Intern," reposted 26 days ago — customer acquisition, HubSpot relationship
management, outbound lead generation, supporting sales targets. Same URL-reuse pattern as A22
(CertiK) on 2026-08-20. Function moved Growth → Sales (`PROFILE.md`'s #3 priority function down to
#8), Fit trimmed ~4 → ~3, Priority Med → Low/Med. Kept `live` since the posting itself is genuinely
open today, just not the role originally tracked.

**A128 (Base Power), Business Operations Intern, Commercial Partnerships — Austin, TX. Added `live`,
High priority.** Found via a direct crawl of Base Power's own `builtinaustin.com/company/base-power-
company/jobs` listing (triggered by investigating the A70 URL-reuse above), posted 12 hours before
this sweep. Real Strategy/Partnerships generalist work — market and competitive analysis, financial
modeling, GTM planning, identifying and standing up new channel partnerships — home market, no
relocation cost, no stated season/dates (same as A70's original pattern).

**A129 (Base Power), Finance – Analytics Intern — Austin, TX. Added `live`, Med priority.** Sibling
req from the same company-page crawl, posted 12 hours before this sweep. Budgeting, forecasting,
variance analysis, and financial modeling work — genuinely quantitative but leans Finance more than
core Data/DS, so scored a notch below A128. Two other sibling reqs from the same page were checked
and excluded: "Business Operations, MBA Intern" requires current MBA enrollment (wrong candidate
level); "Quantitative Developer Intern" is a Markets-team software-engineering role requiring "strong
software engineering practices" (excluded pure-engineering lane).

**A130 (Kodiak Robotics), Winter 2027 Intern, Data Engineering — Mountain View, CA. Added `live`, Med
priority.** Sourced from the SimplifyJobs off-season README's Data Science table, confirmed directly
on Greenhouse (primary source, no access blocker — unlike every Tesla Data Engineer row in this
tracker). The posting states explicitly: "Start Date: January 2027. Our internship program is 12-16
weeks; the end date is flexible based on individual needs" — a direct, named solution to the March
hard-stop constraint, on par with A5 (Dalus)'s "fits around your studies" language. Function is
pipeline/ETL/dashboarding-leaning (AuroraDB, ElasticSearch, QuickSight), so Fit is scored cautiously
in line with Tesla's Data Engineer Intern rows, but full primary-source confirmation plus the explicit
date flexibility justify `live`/Med rather than `unverified`/Low. Pay shown as a flat "$10,000 USD"
range — likely a stipend total rather than an hourly/monthly rate, but the posting doesn't clarify;
flagged rather than assumed.

**2026-09-13 sweep — 3 new Tier A rows (A124, A125, A126, all Tesla, all access-blocked/inferred),
1 exclusion checked (BeamNG), no closures.** Full detail is in the header summary above; per-row
notes below.

**A124 (Tesla), Commercial Charging Product Management Intern, Energy Engineering — Palo Alto, CA.**
Added `unverified`. Sourced from the SimplifyJobs off-season README's Product Management table
(parsed programmatically this run rather than summarized, after the first WebFetch pass on the same
URL truncated before reaching the PM/DS sections). Tagged "Winter 2027, Spring 2027," 1 day old per
the README's own age column, job 283156. This is the first Tesla PM-function req tracked — the two
existing Tesla rows (A68, A122) are both Data Engineer. tesla.com 403s on every direct-fetch attempt
(WebFetch and curl with a browser UA), consistent with every prior sweep's experience with this
domain; WebSearch found no cached copy of this exact req but did surface prior-cycle sibling postings
for the same Energy/Commercial-Charging PM family paying $20–50/hr, not confirmed for this specific
req. Pay, exact term dates, and mode remain unconfirmed.

**A125 (Tesla), Data Engineer Intern, Fleet Data – Self-Driving — Palo Alto, CA.** Added
`unverified`. Same source and method as A124; tagged "Spring 2027," 2 days old, job 281612. A third
distinct Tesla Data Engineer req alongside A68 (Cell Engineering) and A122 (Fleet Analytics) — kept
per the instruction that a clearly-distinct new req at an already-tracked company still counts. Same
403/unconfirmed pattern as A124; not upgraded to `conflict` since (unlike Zipline's A105/A107/A119
sibling pattern) no Tesla req in this tracker has independently confirmed a Jan–Apr overrun.

**A126 (Tesla), Machine Learning Engineer Intern, Charging Data Modeling — Palo Alto, CA.** Added
`unverified`. Same source and method; tagged "Winter 2027, Spring 2027," 11 days old, job 281940.
Leans ML-engineering rather than core analytics, so scored the same cautious Fit as A68/A122 rather
than assumed strong. Same 403/unconfirmed pattern.

**Excluded: BeamNG GmbH, Business Development Intern (remote).** Surfaced via Intern Insider's
sales-business-development facet page, with Economics explicitly named among qualifying majors — a
promising signal on paper. The linked apply URL (shortcode BF01D9961F) 404'd; found the live posting
via Workable's own JSON widget API instead (current shortcode 4EB1B41E44, published 2026-09-11,
function tagged "Business Development"). The posting's own `locations` field allows telecommuting
only from Germany, the Netherlands, France, Singapore, Sweden, and the UK — the US is not among the
permitted remote countries, so this is not actually open to a US-based applicant despite reading as a
plain remote role at first glance. Excluded as a genuine mismatch rather than flagged ambiguous.

**2026-09-12 sweep — 2 new Tier A rows (A122, A123, both access-blocked/inferred rather than
directly confirmed), 3 confirmations (A121, A13, A92), no closures.** Full detail is in the header
summary above; per-row notes below.

**A121 (Ankura) — disputed deadline confirmed wrong, not just unverified.** Today is the exact date
Intern Insider claimed as the deadline. The primary Workday source (CXS API, req R104943) still
shows the role open with no deadline field in its schema at all — the date has now passed with
nothing materializing on the source of record.

**A13 (DeepAware AI) — "Robotics Center of Silicon Valley" rebrand confirmed.** No longer a
suspicion: the live posting's entire body text only ever uses the new name. `sponsorsVisa: "Will
sponsor"` also newly noticed on this posting.

**A92 (TraceRoot.AI) — visa sponsorship confirmed, one date flag.** `sponsorsVisa: "Will sponsor"`
noticed. Also: the posting's own copy now includes "You won't own everything in one summer" — worth
asking directly about a Jan–Mar slice before assuming the role is truly open-ended on dates. Not a
confirmed conflict, no status change.

**A122 (Tesla), Data Engineer Intern, Fleet Analytics — Palo Alto, CA. Added `unverified`.** A
distinct req (283138) from the already-tracked A68 (Cell Engineering, req 278622), tagged Winter
2027/Spring 2027. tesla.com 403s all direct fetch (WebFetch and curl, multiple UA/header
combinations) — same as A68 and every prior sweep's experience with this domain. Function reads as
pipeline/ETL/SWE-leaning "Data Engineer" work rather than the analytics core of the target Data
function, so scored the same cautious `~3` fit as A68 rather than assumed strong. Kept per the
never-silently-drop rule rather than dropped for being unverifiable.

**A123 (Zipline), Data Analytics Intern (Spring 2027) — South San Francisco, CA. Added
`conflict`.** A ninth distinct Zipline req (7990420003), separate from A4/A16/A64/A105/A106/A107/
A119. The page is JS-rendered and returned no body text via WebFetch or curl — this specific req's
dates are not independently confirmed. But every other Zipline "Spring 2027"/"Winter 2027"-tagged
req tracked here has confirmed a Jan–Apr overrun past the Mar 12 cutoff, the same sibling-pattern
reasoning already used to justify A119's `conflict` status without a direct per-req confirmation.
Applied the same logic here rather than adding it `live` on an assumption or dropping it outright.

**2026-09-10 sweep — 1 new Tier A row (A121), no corrections, no closures.** Full re-verification of
all 18 `live` rows found zero drift (see the header summary above for detail); this is the first
sweep in several days with no field corrections at all. New-lead sweep of all ten sources surfaced
one genuinely new, time-sensitive candidate.

**A121 (Ankura), University Intern, Forensic Data & Analytics — New York, NY.** Found by browsing
Intern Insider's Ankura company page directly rather than the term-facet pages (which don't surface
this title), then opening the specific listing rather than trusting the company-page summary. Ankura
is a global advisory/consulting firm; this role is forensic accounting and litigation-support data
work — SQL, Python, and Tableau for data cleansing, analysis, and visualization feeding regulatory
investigations and litigation matters — genuinely the same functional lane as the Analysis
Group/Cornerstone/CRA economic-consulting targets `PROFILE.md` calls out by name, with Economics
explicitly listed among qualifying majors alongside CS, Math, Finance, and Accounting. On-site, paid
$34/hr, no stated season/term (unlike its own sibling req, "University Intern, Strategic Finance,
Turnaround & Restructuring," which is explicitly tagged Summer 2027 — this listing carries no such
tag, a real signal it may run on a different cycle). **Deadline is September 12, 2026 — two days out
at time of sweep, the most time-critical row in the tracker right now.** Kept `unverified` rather
than `live`: Ankura's own Workday board (`ankura.wd5.myworkdayjobs.com`) returned 403 on both a
direct fetch and the underlying CXS API via curl, so the primary source could not independently
corroborate the term/dates — Intern Insider's own listing page is the only source, opened directly
rather than via search snippet. One nuance worth flagging before investing time: the posting states
a graduation-date requirement of "December 2027 – June 2028," which a UT Austin Class of 2028
candidate satisfies, but the phrasing reads like a near-graduate conversion-track internship rather
than a pure off-cycle slot — confirm the actual internship dates directly given how little time
remains before the deadline.

**Everything else came back empty of new in-scope leads.** Full detail (economic consulting,
Uber/DoorDash/Flexport/Palantir, Tokyo, BuiltIn, SimplifyJobs, GradConnection) is in the header
summary above rather than repeated here — nothing beyond A121 cleared the quality bar. Two near-miss
checks worth recording: Coinbase's Associate Product Manager Intern (SF) explicitly states a
12-week Summer 2027 program — hard-excluded, not a stretch. NTT DATA's Sydney "Marketing Intern"
(GradConnection) is a real, open, 6-month placement — but targets an early-November-2026 start
(during Sam's enrolled fall semester) and runs 6 months past that, the same structural mismatch that
has excluded every other ANZ corporate program this year — not added.

**A2, A4, A8 — closed 2026-08-18, re-verification sweep.** A2 (Magnet Media) is titled "Social Media
Intern," a hard exclusion per `PROFILE.md` — it should not have been tracked live in the first place.
A4 (Zipline Community Engagement, Austin) turned out wrong on every axis once opened: the tracked req
is dead, and the live posting under that title is actually **Summer 2026** in Fort Worth/Dallas TX or
South SF, not Spring 2027 Austin — this was not a date conflict, it was a bad lead from the start. A8
(GutGutGoose) now 404s with no replacement listing found. All three kept per the never-drop rule in
case Zipline or GutGutGoose reopen a matching role.

**A3 — corrected 2026-08-18.** The tracked URL redirects to a generic About page; the real posting
found via search is titled "Finance & Controlling," not "Marketing Controller," and states a
**6-month minimum** — too long for the 10-week window regardless of the Spain convenio question.
Downgraded to `conflict`/Low.

**A1 — corrected 2026-08-18.** LinkedIn access opened this sweep and the posting reads very
differently in full: it's **remote**, not in-person (the NY title is misleading — the actual
employer, Brilliant Agency, is a fully remote PR firm; the job header even shows Council Bluffs,
IA), and the term is **January 11 – May or June 2027**, well past the hard stop. Downgraded from
`live`/High priority to `conflict`/Low. Kept rather than deleted per the never-drop rule.

**A5 — Dalus is the best new find of this sweep.** The posting for its GTM Intern explicitly says
the role **"fits around your studies"** — a direct, named solution to the stay-enrolled constraint
that almost nothing else in this tracker offers. Multi-location (SF, Melbourne AU, Munich, remote),
hourly, and $18–25/hr. Confirm which location is actually available before applying.

**A6/A7 — Uplane's two intern roles both carry minimum-duration language** ("at least three months"
/ "at least four months") that, starting Jan 4, runs into April and May respectively — past the hard
stop. Function fit is excellent (BD is a top-ranked function; the AI Marketing Strategist role is a
strong Growth fit) and it's a tiny YC startup, so a shortened 10-week ask is plausible. Worth the
email, same logic as A4/A16.

**A13 — DeepAware AI has three parallel intern openings** (BD/Partnerships, Marketing, Operations),
all on-site SF, all YC S25. Pick whichever function fits best; only one row was added to keep the
table from tripling for one company.

**A15 — downgraded to unverified 2026-08-18.** The tracked req (R_00047706) would not load this
sweep. Search turned up a same-titled req with a different Workday ID that ran Aug–Sep 2025,
suggesting this may be a recurring seasonal posting reused each cycle rather than a confirmed
Winter/Spring 2027 opening. Check UT Workday directly for the current live req before counting on it.

**A16 — a second, separate Zipline internship**, this one in South San Francisco
(Strategic Engagements & Events, $34/hr) rather than Austin (A4). Same seasonal Jan–April overrun.
The Techstars req page wouldn't render for the sweep agent — find the live posting directly.

**A17 — unblocked 2026-08-18.** A reposted listing confirms this is fully remote ("Remote —
Everywhere," EU/CET timezones preferred), not in-person Barcelona as the mode was previously
unconfirmed. That sidesteps the Spain convenio question entirely per `PROFILE.md`'s remote-for-a-
foreign-company option — moved from `blocked` to `live`, though remote still scores the priority down.

**A18 — Datadog's Winter PM Intern session is real and dated** (Jan 4 – Apr 23, 2027) but overruns
the hard stop by three weeks. Separate from Datadog's existing Tier C Data Science outreach target.

**A19 — closed 2026-08-18.** Confirmed location is Research Triangle Park, NC — not Austin as
previously assumed — which fails the target-location filter outright. Recruiting window also closes
1 September 2026. Kept per the never-drop rule; a genuine Austin-based IBM sales-engineer req would
be a strong fit if one surfaces.

**A20 — Agentio's Creator Partnerships Intern is a direct Partnerships-function match** (NYC, paid,
in-office) but the posting asks for candidates "ideally graduating in '25 or '26" — near-graduation,
not a rising junior. No season/term stated either. Real mismatch signal; included per the
never-drop rule.

**A21 — Crustdata is the strongest new find of this sweep.** YC F24, real-time company/people-data
API platform, Brooklyn (Williamsburg) NYC, on-site. Exactly the technical-adjacent "translation not
implementation" solutions-engineering lane called out in `PROFILE.md` — strong pay ($4–6K/mo),
rolling dates. Posting noted an ~Aug 26 2026 application deadline at time of sweep; confirm it's
still open before delaying.

**A22 — CertiK is a light, part-time "ambassador" role** (blockchain meetups, intros), not a
substantive BD seat — the $1K/mo pay reflects a 5 hrs/week commitment. Worth pairing with a bigger
internship rather than treating as a primary target.

**A23, A25, A26, A28, A30 — BuiltIn sweep, all real but each carries an unresolved caveat rather
than a clean apply-now status.** Chubb (A23) has an excellent skill-tag match and pay but no season
stated — insurers usually run named summer cohorts. SOUKMEDIA (A25) is genuine quantitative
demand-gen work with a stated "3 months" but no fixed start or pay. Treasure (A26) is flagged
ambiguous per `PROFILE.md`'s substance-over-title rule: real BD/pipeline work is described, but the
posting opens with social-content tasks for a collectibles brand — right on the excluded line, so
it's included rather than dropped. Unify (A28) is similarly ambiguous: "GTM Engineering" reads more
like the excluded software-engineering lane (API integration, internal tooling) than analytics/
growth — also included with the flag rather than guessed away. Guidepoint (A30) has conflicting
season signals across two searches (Class of 2028 vs. Summer 2028) — confirm the actual cohort
before investing time.

**A24 — Lieberman Research Worldwide is genuine quantitative market research** (SPSS, fieldwork,
tabulation) on a rolling, year-round basis, so there's no date conflict — but it's fully remote and
scores down accordingly.

**A27 — Anthelion Capital's Winter 2026 cohort undershoots the window** (roughly Dec–Feb) rather
than overshooting it — starts before Sam is available (still in fall semester) and doesn't span the
full 4 Jan–12 Mar range. Strong pay and NYC in-person data-science-adjacent work; worth asking if a
Jan-start version exists.

**A29 — Rocket Internet's Founders' Associate Intern is the exact high-signal generalist title**
`PROFILE.md` calls out by name. Strong brand, but unpaid and no dates stated — worth it only if the
brand/access clears the strategically-valuable-unpaid bar.

**A31 — Global Pathways AI reads as a low-signal intern-mill posting** (three near-identical generic
tracks, "no experience required," pay hedged as "may become paid"). Included as a low-priority
option since it's genuinely open, fresh, and remote-flexible.

**A19 — corrected 2026-08-19, re-opened.** The 2026-08-18 close relied on a single mirror showing
only Research Triangle Park, NC. A separate WayUp mirror of the same req lists a much longer
location set — **Austin, San Francisco, and New York are all included** alongside RTP, Dallas,
Chicago, Atlanta, DC, Irvine, and Durham — confirmed via direct web search of the posting text.
IBM's own careers site still would not load directly for the sweep, so status moves to
`unverified` rather than `live`, but the target-location objection that closed it no longer holds.
Priority raised Low → Med. **Deadline (1 Sep 2026) is inside three weeks — act soon if pursuing.**

**A64 — a third, separate Zipline internship**, distinct from the Austin Community Engagement (A4)
and South SF Strategic Engagements (A16) roles already tracked. Supply-chain BI/reporting work
(SQL, Python, Tableau, Power BI) is a direct DS/analytics skill match, but it carries the same
Jan–Apr/May overrun as the other two Zipline rows. Series C, so date flexibility is uncertain —
worth asking directly rather than assuming, same as A4/A16/A6/A7.

**A65/A66 — Peakflo's two intern roles (YC W22)** are both remote and priced for India-based
candidates in rupees (~$4–6K/yr equivalent) even though the posting says US citizenship/visa isn't
required. The PM role (A65) is a clean function match at low pay; the SDR role (A66) is deprioritized
by function (pure SDR) and carries a 6-month minimum that overruns the window. Included per the
never-drop rule; both are low priority on every axis.

**A67 — Closure's PM Intern (YC W25, 10-person startup)** is dated Summer 2027 — a full season past
the window, not a slight overrun. Strong PM fit and small enough that an earlier/shorter stint is
plausible to negotiate; worth an email rather than a straight application. No direct job-page ID
could be located — the company page is linked instead.

**A68 — Tesla Data Engineer Intern (Cell Engineering)** surfaced via the SimplifyJobs off-season
README, which as of this sweep now carries real Data Science/AI/ML and PM sections that didn't
exist on 2026-08-17 — worth re-checking regularly going forward. Tagged for both Winter 2027 and
Spring 2027 terms (good window signal), but the function is manufacturing/cell-engineering data
engineering rather than core growth/BD/analytics. Tesla's careers site is JS-rendered; pay, exact
dates, and mode could not be fetched directly — status `unverified`.

**2026-08-20 sweep — re-verification of all 13 "live" Tier A rows found real drift on four.**
**A12 (Mosaic)** and **A21 (Crustdata)** now 404 on their tracked URLs — both listings have expired
and are closed, kept per the never-drop rule. **A22 (CertiK)** — the same Lever URL now shows a
Hong Kong/Shenzhen listing (Hybrid), not the tracked New York in-person role; CertiK appears to have
reused the req ID for a different region. A same-titled NY role still appears on an interninsider.me
mirror, but no live NY application URL could be recovered this sweep — closed pending a fresh link.
**A17 (Axo Longevity)** — the "fully remote" posting was found to restrict applicants to Spain only
(`applicantLocationRequirements`), missed in the 2026-08-18 correction — not viable for a US-based
applicant, closed. The other nine live rows (A5, A9, A10, A11, A13, A14, A20, A24, A65) were
confirmed accurate as tracked.

**New this sweep: 12 new rows added (A70–A81), plus one Tier C outreach target (C70).** Best find is
**A80 (Notion)** — a real, dated Winter 2027 Data Science Intern posting on Ashby at a company
already tracked as a Tier C outreach target (C13) for its PM/Growth fit. Also notable: **A71
(Zettabyte)**, a genuine growth-analytics role with an explicitly flexible "3–6 months, with possible
extension" window that should accommodate Jan–Mar cleanly, and **A70 (Base Power Company)**, an
Austin-native growth role (home market, no relocation). **A75 (Surface Labs)** is a strong functional
fit (technical-adjacent GTM engineering) but pays commission-only with no base — flagged as high pay
risk rather than dropped. **A76 (Novaflow)** and several BuiltIn corporate programs (Capital One,
Citadel, Mastercard, New York Life, Databricks) were checked and are Summer-2027-only or predate the
window entirely with no stated flex — Novaflow was kept as `conflict` since it's a small YC startup
worth asking directly; the large corporate Summer-only programs were not added at all, since they're
structurally incompatible with the window and unlikely to move. **A77, A78** carry explicit ambiguity/
date-uncertainty flags per the substance-over-title and never-guess-away rules rather than being
silently included or dropped.

**2026-08-21 sweep — 20 new Tier A rows (A82–A101), one new Tier C target (C71), two corrections,
one reopen, and three imminent deadlines surfaced.** Re-verification of 13 previously live/unverified
Tier A rows found: **A13 corrected** — the live posting's actual title is "Business Development
Intern," not "BD/Marketing/Ops Intern (3 openings)"; content is 100% BD, no marketing/ops
responsibilities appear anywhere — title/scope overstated in the prior entry. **A22 reopened** — the
tracked Lever URL was still showing the wrong-region (Hong Kong/Shenzhen) listing that closed it on
2026-08-20, but a fresh New York/Hybrid listing of the same role was found at a new URL
(`241dde9b-...`) and swapped in. **A19 (IBM)** confirmed still open — expires 1 Sept 2026, ~11 days
out at sweep time, act soon. **A21 (Crustdata) and A12 (Mosaic) confirmed still dead**, no
replacements found, left closed. The other nine re-checked rows (A9, A10, A11, A14, A20, A24, A65,
A75, A80) held exactly as tracked.

**Best new finds:** **A96 (Crowe Global)**, an Austin AI-adoption-consulting internship explicitly
titled "Winter 2027" with ongoing applications and strong pay ($27–42/hr) — the cleanest term-match
of the whole sweep. **A92 (TraceRoot.AI, YC S25)**, a technical-adjacent GTM Engineer role (funnel
instrumentation, outbound automation, dev-community growth, $4–6K/mo) that's close to an exact match
for the technical-adjacent lane. **A82 (Soren)**, a cross-functional SF growth generalist role at
$6–11K/mo with no stated duration minimum. **A101 (Advancy Partners)**, a boutique Sydney strategy-
consulting internship with genuinely flexible 2–6 month dates — the small-firm-sets-its-own-dates
profile Australia has been missing.

**Three postings carry deadlines inside the next five days** — flagging prominently since they'd
otherwise be missed before the next sweep: **A92 (TraceRoot.AI)** closes **Aug 24 2026**; **A91
(Trellis AI)**, **A98 (Cresta)**, and **A100 (APX/Aster)** all close **Aug 26 2026**. All four were
found only on Intern Insider, which doesn't expose external application URLs — apply through the
Intern Insider listing page directly.

**Six rows carry a `conflict` status from this sweep** (A84, A85 Dedalus Labs; A86 Sixtyfour; A87
GutGutGoose new posting; A99 Scale AI) — all dated Summer 2027 or Fall 2026, outside the window, kept
per the never-drop rule since the underlying companies/functions are strong fits and worth a direct
ask about a Jan–Mar slot. **A89 (Peggy)** is flagged ambiguous on purpose: titled "Growth & PR Intern"
but the substance is journalist/influencer media-placement outreach — closer to PR/comms than
quantitative growth, included with the flag rather than guessed away.

**Considered and excluded per the hard-exclusion rules, not padded in:** Comena's GTM Associate
Intern (Munich, Germany — real BD/outbound fit but outside the target-location list); Point72's
Quantitative Developer Intern (NYC, dates align unusually well with the window, but "Developer"
implies real software/quant engineering depth outside the target functions); HeyGen's Growth
Marketing Intern (Los Angeles — strong brand/function fit but outside the target-location list, and
LA isn't an adjacent metro to SF/Bay Area).

**Tokyo and Australia came back empty again** for the named Tokyo sources, but produced one new
Australia lead. Coral Capital confirmed still directory/talent-
matching only (checked all three career-adjacent pages, not just the homepage) — no portfolio job
board exists to sweep. Japan Dev and TokyoDev remain structurally engineering-first with no BD/
Growth/Partnerships/Solutions-Engineer/DevRel category; the only internship on either site (HENNGE's
"Global Internship Program – Full Stack") is pure software engineering. GradConnection's Sydney (92)
and Melbourne (112) boards are still 100% Big-4/big-bank/large-corporate programs with zero startup
listings — though the year-labeling problem from earlier sweeps has resolved (listings now correctly
read "2026/27," the right cycle). **Tooling note for future sweeps: `WebFetch` now returns 403 on
`au.gradconnection.com`; `curl` with a browser user-agent still returns clean server-rendered HTML.**

> **The co-op channel is still worth searching even though Delta and Wayfair failed the date test.**
> Co-op programs run Jan–June and are posted for January starts, so `co-op` as a keyword surfaces a
> different set of postings than `intern`. Nearly all of them run past mid-March and many forbid
> concurrent enrollment — read the fine print before investing time, but search the term.

**2026-08-22 sweep — re-verification pass over the imminent-deadline and 2026-08-21 rows, plus
sweeps of economic consulting, YC/Wellfound, and Uber/DoorDash/Flexport/Palantir. No new Tier A
postings surfaced (YC W27 batch doesn't land until November; Wellfound's search index continues to
turn up mostly dead 410s on new queries) — the day's yield is corrections.**

**A92 (TraceRoot.AI) upgraded `unverified` → `live`** — independently confirmed via the primary YC
company jobs page, which matches the Intern Insider mirror exactly (SF/remote hybrid, ≥3 days
onsite, $4–6K/mo, "best applied by Aug 24"). Link swapped to the YC listing, which also exposes a
direct Work at a Startup apply route — Intern Insider's lack of an external URL is no longer a
blocker for this one. **Deadline is one to two days out — act immediately if pursuing.**

**A98 (Cresta) upgraded `unverified` → `live`** — found and confirmed the actual Greenhouse posting
(`job-boards.greenhouse.io/cresta/jobs/5213417008`), independent of Intern Insider. Remote US, data
science on the customer-success team; pay still unconfirmed on the primary source. Link swapped to
the direct Greenhouse URL.

**A91 (Trellis AI) — discrepancy found, left `unverified` pending a direct check.** The Intern
Insider mirror still shows "Apply Now," but Trellis AI's own current YC company jobs board (7 open
roles) no longer lists a Business Operations Intern req at all — only Head of Business Ops and other
full-time roles. The aggregator's Aug 26 deadline may be stale. Treat this one as lower-confidence
than the other three imminent-deadline rows; check trellis.ai's careers page directly before relying
on the Intern Insider apply link.

**A100 (APX/Aster) — still unverified beyond Intern Insider.** Attempted to corroborate via a direct
company URL: APX/Aster isn't a YC company, `tokenjobs.io` returned no listing content, and
`asterdex.com` blocked the fetch outright (HTTP 403). No independent confirmation either way — status
and Aug 26 2026 deadline unchanged, confidence unchanged (real lead, unverified beyond the aggregator).

**Uber, DoorDash, Flexport, and Palantir (C76–C79) checked directly — none has converted from a
cold-outreach target to a live posting.** Uber's board has no Strategy & Operations internship listed;
DoorDash's internship track is Summer-2026-only (ML/design/SWE, no S&O); Flexport's Strategy/Ops
analyst roles are all full-time, not internships; Palantir's two "Deployment Strategist, Internship"
Lever postings (NY and DC) both explicitly show "no longer available." All four remain `monitor`/
cold-outreach — the play is still a direct approach in Sept–Oct, not waiting for a posting.

**2026-08-23 sweep — corrections only, no new Tier A rows.** Re-verified the four imminent-deadline
rows from 2026-08-22 (A91, A92, A98, A100) plus five rows added 2026-08-21 not yet double-checked
(A82, A83, A88, A96, A101). Also swept Work at a Startup, Wellfound, Simplify, BuiltIn (all three
metros), Coral Capital, Japan Dev, TokyoDev, and Australian sources (gradconnection plus AirTree's
and Blackbird's VC portfolio boards, checked for the first time) for new postings — all came back
empty of genuinely new, verified, in-scope candidates. One Work at a Startup lead (Operations Intern
at DeepAware AI, `100906`, admin/facilities ops not strategic ops) was found but not added — too weak
a function fit to clear the quality bar.

**A91 (Trellis AI) closed, definitively this time.** The specific YC job URL now 404s, and Trellis
AI's own current jobs list (confirmed again) has no internship req of any kind — only full-time
roles. The Intern Insider listing was carrying a dead posting. Closed rather than left `unverified`.

**A92 (TraceRoot.AI) and A98 (Cresta) — deadlines corrected to "unconfirmed."** Both roles are
confirmed genuinely open (YC page still has a working Apply button for A92; Cresta's Greenhouse form
is live and functional for A98), so `live` status stands — but neither company's own posting states
the Aug 24 / Aug 26 2026 deadline this tracker had been carrying. Those dates likely came from the
aggregator (Intern Insider) rather than the source. Treat both as rolling/no fixed deadline unless a
firmer date turns up; no need to rush applying past when they'd normally be submitted anyway.

**A100 (APX/Aster) — confidence lowered further, kept `unverified`.** Exhausted every reasonable
independent channel (Ashby, LinkedIn, BNB Chain job board, company sites) with no corroboration
found. Intern Insider itself shows the listing as "posted 87 days ago," a staleness signal on top of
the earlier no-second-source problem. Still kept per the never-drop rule since the URL and function
match are real, but this is now a low-confidence lead — verify directly before investing time.

**A82, A83, A88, A96, A101 — all confirmed accurate, no drift.** Pay, location, mode, and stated
duration all matched exactly what was tracked; none had rotted (Wellfound listings in particular
often do, but A88 held).

**2026-08-24 sweep — no new rows, two corrections, one urgent deadline flag.** Full sweep across
Work at a Startup, Wellfound, Simplify, the SimplifyJobs off-season README, and Intern Insider
surfaced nothing new and verifiable — everything found was wrong-window (Summer 2027/Fall 2026),
wrong-location, or already tracked. Direct re-check of every economic consulting firm and every
Strategy & Ops target (Uber, DoorDash, Flexport, Palantir, Anduril, Tesla) plus four peer consulting
firms (Bates White, Edgeworth, Secretariat, BRG) found no live off-cycle posting anywhere in that
lane — all remain summer-only or full-time-only. BuiltIn (all three metros), Coral Capital, Japan
Dev, TokyoDev, and GradConnection Sydney also came back empty; two new Australia sources were tried
for the first time (AirTree, Blackbird VC portfolio pages) and both 404 — no portfolio job board
exists at either, so they're not addable as sweep sources going forward.

**A80 (Notion) — pay confirmed.** Previously "Unconfirmed"; the Ashby posting now states
**$55/hr for Bachelor's candidates, $59/hr for Master's**. No other fields changed.

**A19 (IBM) — urgent deadline flag, act within a day or two.** The tracked deadline (1 Sept 2026,
sourced from a Clemson mirror) may already be stale: a WayUp mirror of the same req states it was
posted 7 Aug 2026 and "anticipated to remain posted for 15 days," i.e. roughly 22 Aug — already
passed by this sweep. IBM's own careers page is still blocked by an AWS WAF bot-check and could not
be read directly to resolve the discrepancy. Treat this as more urgent than the tracked date rather
than waiting for 1 Sept.

**2026-08-25 sweep — no new Tier A/B/C rows, two real corrections, one confidence downgrade.**
Full sweep of Work at a Startup, Wellfound, Simplify, the SimplifyJobs off-season README, and Intern
Insider (winter-2027 and spring-2027) surfaced nothing new that clears the quality bar — Wellfound's
SEO role pages (`/role/l/{role}/{location}`) were tried as a workaround for its broken search/filter
UI and turned up a Faire Data Science Intern (requires current Master's/PhD + top-venue ML
publications, not addable) and a Workhelix Forward-Deployed Strategist (a strong functional match but
full-time, 4+ yrs experience required, not an internship). The SimplifyJobs README's three
target-location/target-window matches (NBCUniversal PM, Crusoe PM, Disney Insights & Analytics) are
all marked closed (🔒) in the source. Economic consulting and Strategy & Ops targets (Analysis Group,
Cornerstone, CRA, Compass Lexecon, Brattle, NERA, Bates White, Edgeworth, Secretariat, BRG, Uber,
DoorDash, Flexport, Palantir, Anduril, Tesla) re-checked directly — no live winter/spring 2027 posting
at any of them; Palantir's Deployment Strategist internship cohorts run May–September, confirmed not
a January fit. Tokyo (Coral Capital, Japan Dev, TokyoDev) and Australia (GradConnection, 403'd
directly but search-checked) came back empty as usual.

**A80 (Notion) corrected — downgraded from `unverified`/High to `conflict`/Med.** The tracked
"Winter 2027 (season confirmed)" window undersold a real problem: independent corroboration (a
BuiltIn NYC mirror plus other sources, since Ashby's own posting page is JS-rendered and won't yield
body text to a direct fetch) confirms the internship runs **January through April 2027**, working
in-person out of the SF or NYC office — a 3–4 week overrun past the 12 Mar hard stop. Still a strong
role on every other axis (confirmed $55–59/hr pay, direct stats/econ qualification match, prestige
brand already a Tier C target) — worth an email asking whether a shorter Jan–Mar slice is possible,
same play as A18 (Datadog) and the Zipline rows.

**A19 (IBM) corrected — deadline confirmed real, urgency flag resolved.** The 2026-08-24 worry that
the listing might have already expired (per a stale WayUp snapshot) is resolved: a fresh check of the
Clemson mirror shows an active "Apply Now" button and explicit text that the listing "Expires on
September 1, 2026." IBM's own careers page remains blocked by AWS WAF and unreadable directly.
Deadline is about a week out from this sweep — apply soon if pursuing.

**A100 (APX/Aster) — confidence lowered further, still kept per the never-drop rule.** Checked BNB
Chain's own Aster company job board directly this sweep — it currently lists **zero** open positions
at Aster, including no Developer Relations Intern req. Combined with the existing 87+-day staleness
signal on Intern Insider and three prior sweeps finding no corroboration anywhere else, this is now a
likely-dead lead. Left `unverified` rather than closed since the original Intern Insider posting
itself was not directly re-checked today (only independent corroboration sources were), but treat
this as low-confidence — verify directly via Intern Insider before investing any time.

**Economic consulting (C72–C75) direct sweep, plus two new peer firms added — see the new section
above.** No live winter/spring 2027 posting exists at Analysis Group, Cornerstone, Compass Lexecon,
Brattle, or NERA as of this check; CRA has a live internship track but it's EU-only and
Master's/PhD-only, not addable. **C102 (Brattle)** and **C103 (NERA)** added as peer cold-outreach
targets. This whole lane stays a September cold-outreach play, exactly as `PROFILE.md` describes it
— these firms simply don't post off-cycle internships on a rolling job board the way startups do.

**2026-08-28 sweep — 2 new Tier A rows (A112–A113), Australia lane's first genuinely new company in
several sweeps, no corrections needed.** Full sweep of Work at a Startup, Wellfound, Simplify, the
SimplifyJobs off-season README, Intern Insider (winter-2027 and spring-2027 term pages), BuiltIn
(all three metros), economic consulting firms (quick recheck of Analysis Group, Cornerstone, CRA,
Compass Lexecon, Brattle, NERA — all still summer-only/no internship, unchanged), Tokyo (Coral
Capital, Japan Dev, TokyoDev), and Australia (GradConnection Sydney, fetched via `curl` with a
browser user-agent since `WebFetch` still 403s the domain).

**Best find: A112 (TikTok, Client Solution Intern, GBS AU).** GradConnection's Sydney
business-and-commerce board, previously checked repeatedly and found "100% Big-4/big-bank/large-
corporate programs," this time surfaced two TikTok internship listings that hadn't appeared before.
The Client Solution Intern role (TikTok's Global Business Solutions/ad-sales org) is consultative
selling plus real analytics — campaign performance analysis, media-metrics reporting, Excel — a
genuine Sales/BD-with-quant-substance fit. Two things make it a standout: the posting text literally
instructs applicants to "clearly state your availability in your resume (Start date, End date)," an
explicit invitation to propose a custom Jan–Mar slice that almost nothing else in this tracker
offers; and its work-rights list names "Australian Working Visa" alongside citizen/PR/student-visa
options — a direct match to the subclass 462 working-holiday route `PROFILE.md` confirms Sam is
eligible for. Verified by opening the actual GradConnection posting directly (not a search snippet),
which required a `curl`+browser-UA workaround since `WebFetch` 403s this domain. No external ATS
link exists — applications go through GradConnection's own login/apply flow, so the GradConnection
URL is the correct application link. Mode (in-person vs. hybrid) is not explicitly stated on this
particular posting, unlike a same-company SWE listing found alongside it that does require ≥3
days/week on-site — flagged rather than assumed.

**A113 (TikTok, Revenue Product Operations Intern, TikTok LIVE-Revenue) is a second, separate TikTok
Sydney posting from the same sweep**, PM/product-ops flavored (data monitoring systems, A/B testing,
user research feeding product strategy) — but its qualifications section explicitly requires
"Available to undertake a 6-month internship commitment," a hard, stated-not-inferred conflict with
the 10-week window. Kept per the strong-fit/dates-clash rule rather than dropped; TikTok's Global
Business Solutions internship program is confirmed to exist and run in Sydney with international
work rights, so a direct ask about a shorter Jan–Mar arrangement is plausible given A112 already
demonstrates the same employer accepting candidate-proposed dates on a sibling role. A third listing
title, "AI Product Manager Intern (TikTok Live-Revenue) - 2027 Start," was seen in the same
GradConnection feed but not independently opened — likely the same team, not confirmed as a distinct
requisition, not added per the never-guess-away rule.

**Every other source came back empty of new in-scope leads.** The SimplifyJobs off-season README
(fetched raw) now shows only Disney software-engineering roles in its readable section — no new
data/strategy/growth/BD/PM matches. Intern Insider's winter-2027 and spring-2027 term pages surfaced
nothing beyond already-tracked companies or wrong-location/wrong-function postings (HOOPP and RBC in
Toronto; Disney Park Yield Optimization in Florida; Deloitte GPS analyst roles; a Brooklyn seasonal
strategy internship at BSE Global that turned out to be sports-league/community-facing, not
quantitative). BuiltIn (all three metros) surfaced only already-tracked companies (Notion, Celonis,
Motive, Zipline, Zello, Datadog, Cloudflare-titled roles outside target functions) or wrong-season
postings (Capital One and Mastercard Summer 2027, BDO Winter 2028). Work at a Startup continued the
406/title-only regression from the 2026-08-27 sweep on direct fetch; WebSearch fallback surfaced only
already-tracked companies (Dedalus Labs, Novaflow) and Summer-2027-dated postings (Domu Technology,
CTGT). Wellfound WebSearch surfaced only unrelated small remote BD/growth internships that didn't
independently verify as fresh or in-scope (Remotely Good, PipeLoom, TaskLabs, Polar) — none opened
cleanly enough to clear the quality bar. Targeted searches for "founder's associate," "chief of
staff," "solutions engineer," "sales engineer," "developer relations," "revenue operations," and
"business analyst" intern titles crossed with the target cities returned nothing new and dated for
the window — mostly Summer 2027 corporate postings or generic aggregator noise. Tokyo (Coral Capital,
Japan Dev, TokyoDev) held exactly as every prior sweep found it: no BD/growth/partnerships/solutions-
engineering internship category exists on any of the three, only the same HENNGE full-stack SWE
listing.

**2026-09-05 sweep — 4 new Tier A rows (A117–A120), one real correction, no closures.** Full sweep
of Work at a Startup (curl+UA — still 406, direct-fetch regression continues unchanged), Wellfound,
Simplify, the SimplifyJobs off-season README (downloaded raw and grepped programmatically — Product
Management and Data Science/AI/ML sections both checked in full), Intern Insider (worked the
`/internships/roles/{role}` facet pages this time instead of the term pages, which only server-render
a first slice — `consulting-strategy`, `data-science`, `product-management`,
`sales-business-development`, and `operations-supply-chain` facets pulled 65 full listings apiece),
BuiltIn (all three metros), economic consulting firms (Analysis Group, Cornerstone, CRA, Compass
Lexecon, Brattle, and **NERA direct via nera.com/open-roles.html, checked for the first time this
run** — its own FAQ confirms "summer internships to final-year undergraduate candidates as well as
current master's and PhD students," consistent with C103's existing final-year-only finding), Uber/
DoorDash/Flexport/Palantir (Palantir's two live Deployment Strategist Lever reqs re-confirmed Paris
and Honolulu, unchanged from prior sweeps), Tokyo (Coral Capital's `/jobs/` path now 404s outright;
Japan Dev and TokyoDev unchanged — HENNGE/Morningstar SWE-only), and GradConnection Sydney (curl+UA)
all swept.

**Correction — A115 (Workiva) URL finally resolved.** Every prior sweep back to 2026-08-31 could not
find a working direct req URL for the Commercial Strategy Intern title itself. This sweep found it by
browsing Intern Insider's company page directly (`interninsider.me/companies/workiva`, 22 open reqs)
rather than the term-facet pages that only surface a partial slice — the exact posting
(`commercial-strategy-intern-8a881fb9-...`) confirms **Winter 2027 term starts Monday, January 4,
2027**, 15–20 hrs/week, primarily remote with hybrid near an office hub, closing **September 27,
2026**. Link swapped in. Pay remains unconfirmed on this exact title (no `baseSalary` field on the
listing); end date remains unconfirmed beyond "Winter 2027," so status stays `unverified`/Med.

**Best new finds: A117 and A118, two more Workiva Winter/Spring 2027 reqs from the same 22-req
company page, both with confirmed direct URLs and a confirmed Jan 4, 2027 start** — direct evidence
the company's whole multi-function Winter 2027 cohort (Sales Analytics, Sales Planning, Partnerships,
Commercial Strategy, Product Management, Data Analytics, and more) starts on Sam's exact target date.
**A117 (Product Management Intern)** is Spring 2027, $40/hr confirmed, 15–20 hrs/wk, remote with
hybrid option — but its qualifications list "prior experience in software development," a lean toward
the excluded engineering side rather than product-analytics; kept but fit trimmed to ~3 for the
mismatch. **A118 (Intern – Partnerships)** is Winter 2027, paid (amount unconfirmed), and is the one
Workiva req in the batch with an explicit `jobLocation` of New York City rather than just "US" —
Salesforce/Crossbeam partner-data work, a clean Partnerships-function match. Both close **September
27, 2026**, same as A115 and the sibling Data Analytics req — an internal application-window signal
worth acting on soon if pursuing any of the three. The company's own careers page remains an
unfetchable client-rendered SPA; Intern Insider is the only working source for all three.

**A119 (Zipline), a fourth distinct location for an eighth tracked Zipline internship — Austin, TX.**
Every prior Zipline row (A4, A16, A64, A105–A107) is South San Francisco; this "Commercial Strategy &
Operations Intern" req lists Austin, TX first among six locations (Houston, Phoenix, San Antonio,
Dallas, LA) and explicitly offers a **"Winter 2027"** term alongside Summer 2027 — real SQL/Excel/
dashboard-and-forecasting Strategy & Ops work, a direct match to the Uber/DoorDash-style lane
`PROFILE.md` calls out, in Sam's home market. Kept `conflict` rather than `live`: every other
Zipline req naming a "Winter 2027" term (A105, A107) has independently confirmed that label actually
means Jan–Apr, a five-week overrun; this exact req doesn't restate its own dates, so the overrun is
inferred from company pattern, not confirmed on this posting — flagged accordingly, worth the same
direct-ask play as the other seven Zipline rows given the Austin location removes the relocation cost
entirely.

**A120 (MTA), a new public-sector NYC data-analytics find via the SimplifyJobs README's Data Science
section** — the README's "Spring 2027"-tagged EAM (Enterprise Assets Management) Analyst Intern,
Emerging Talent posting was independently verified live and open on MTA's own Jobvite ATS: Brooklyn,
NY, explicitly **in-person** ("all internship positions are onsite and require regular, in-person
attendance"), $19/hr undergrad ($21/hr grad), real SQL/data-transformation/EAM-systems work. Kept
`live` since the primary source is confirmed real and open; the only gap is that MTA's own posting
states no explicit start/end dates at all — "Spring 2027" is an aggregator tag, not primary-sourced —
so Window carries a `Confirm ≤` flag rather than a firm range. A sibling req at the same pay
(**Technology Support Intern, Emerging Talent**, also Brooklyn, Power Platform/dashboard work rather
than SQL) was found alongside it and not added separately to avoid padding — mention it if reaching
out to MTA directly.

**Considered and excluded, not padded in.** Google's "Data Analytics Apprentice – February 2027
Start" (NYC among 4 locations, surfaced via the SimplifyJobs README) is disqualifying on two axes at
once: it explicitly requires *not* currently being enrolled in a degree program, and it's an 18-month
Department-of-Labor apprenticeship, nowhere near a 10-week shape — a hard exclusion, not a stretch.
ZS Associates' "Strategy Insights & Planning Associate" and "Decision Analytics Associate" intern
reqs (BuiltIn SF, deadline Oct 1 2026) are a strong econ/stats-consulting function match, but WebSearch
corroboration confirms ZS's internship program is an 11-week **Summer 2027** cohort with applications
opening Sept–Nov 2026 for that cycle — no off-cycle track exists, same structural problem as the
economic-consulting lane. VelocityEHS's "Customer Experience Intern (Spring 2027)," despite appearing
on Built In Austin, is actually remote/open-to-US-or-Canada with an optional hybrid option in
Oakville, Ontario — not Austin at all — and runs Jan–Apr 2027 (14–16 weeks), both a location
mismatch and an overrun; not added. A second GradConnection listing for CommBank's "2026/27 Summer
Intern Program: Product Management, Business & Commerce" (Sydney) was checked directly and confirmed
to start Nov 2026 — the same enrolled-fall-semester conflict that has excluded every other ANZ
big-corporate program this year. PwC's "Deals – CMAAS Intern – Winter 2027" (NYC, $29.25–$48/hr,
found on Built In NYC) confirms Big 4 firms have started posting their 2027 cycle on schedule per the
recruiting calendar, but doesn't warrant its own row beyond the existing generic B4 monitor entry
since no Big 4 program has ever been found to close before April.

**2026-09-02 sweep — no new Tier A/B rows, no closures, three field corrections on `live` rows, one
new Tier C outreach target.** Re-verified all 18 rows currently marked `live` (A5, A9, A10, A13, A14,
A22, A65, A70, A75, A82, A83, A88, A92, A96, A98, A101, A112, A114). `workatastartup.com` job pages
kept returning a JS-only shell to WebFetch/plain curl as in prior sweeps, so the run leaned on
`curl` with a full browser User-Agent, which now recovers the underlying Inertia.js JSON — a more
reliable source than prose scraping and worth keeping as the default technique for that domain going
forward. 15 of 18 rows confirmed fully unchanged (several with pay figures re-confirmed that were
already tracked, not new). Three real corrections:

- **A13 (DeepAware AI)** — the posting now displays under the name "DeepAware AI (Robotics Center of
  Silicon Valley)," an apparent rebrand or DBA. SF in-person and BD scope unchanged; the listing now
  also notes it's open to full-time as well as intern candidates. No status change, note-only.
- **A75 (Surface Labs)** — location narrowed: the tracked "San Francisco, CA / India" option is
  confirmed **SF/Remote(US) only**, with an explicit US-citizen/visa-only note — India was never
  actually available to Sam anyway, but the row is corrected for accuracy. More importantly, the
  same structured listing data now states pay of **$10–20K/month**, directly contradicting the
  "commission-only, no base ⚠" text this row has carried since 2026-08-20. Left unresolved rather
  than silently overwritten — one of these two pay claims is stale, unclear which — pay field changed
  to "Conflicting — see note ⚠" pending a direct check before relying on either figure.
- **A92 (TraceRoot.AI)** — same URL, renamed role: "GTM Engineer Intern" → **"Developer Marketing
  Intern"**, confirmed via direct WebFetch (technical writing + developer-focused marketing, same
  $4–6K/mo, same hybrid/3-days-onsite arrangement). Substance still reads as technical-adjacent
  GTM/DevRel work, not the excluded content-marketing lane, so kept `live` — but the title drift is
  worth watching on future sweeps in case the role substance shifts along with the name.

**New: C116 (BuildPass), Founder's Associate, Austin, TX — Tier C outreach target only, no live
posting found.** Australian construction-tech SaaS (~$5M seed 2024, ~10% MoM growth) that has
recently opened a US presence in Austin — Sam's home market. Turned up only via aggregator search
snippets (ZipRecruiter, CB Insights, a Texas Association of Builders member listing) describing a
Founder's Associate role — drafting business cases, turning data into insights, sales-prospect
follow-up — a high-signal generalist title `PROFILE.md` calls out by name. No live application URL
exists on any channel tried (company site, LinkedIn, Ashby, Greenhouse, Lever) — `buildpass.ai/us/about-us`
doesn't mention the role at all and routes applicants to LinkedIn or `hello@buildpass.ai` directly.
Dates, pay, and duration are entirely unconfirmed, including whether this is internship-length at
all. Added to Tier C rather than Tier A since there is no posting to mark `unverified` against — this
is a cold-email target, per the company's own stated preference for direct outreach.

**Everything else came back empty of new in-scope leads, matching the pattern of most recent
sweeps.** Work at a Startup (curl+UA and WebSearch), Wellfound, Simplify, the SimplifyJobs off-season
README (parsed programmatically — no Strategy/Growth/BD/Partnerships/Sales section exists in that
repo at all; only Data Science and PM tables are relevant, and every target-city/target-window row in
those two was already excluded for wrong season, locked status, or non-internship duration), Intern
Insider (both winter-2027 and spring-2027 term pages returned HTTP 429 on every attempt today,
including after backoff — not checked this sweep, retry next time), BuiltIn (all three metros),
GradConnection Sydney (both `curl`+UA and WebFetch hit a JS shell / 429 today — worth retrying the
curl+UA technique that has worked in prior sweeps), and Tokyo sources (Coral Capital, Japan Dev,
TokyoDev — still zero non-engineering internships on any of the three) all came back empty.
Re-checked the five core economic consulting firms plus peers directly (Analysis Group, Cornerstone,
CRA, Compass Lexecon, Brattle, NERA) — CRA's Greenhouse board shows exactly one open internship req,
Brussels/Düsseldorf/Munich-only (EU work authorization required), no change from prior sweeps; the
rest remain summer-only. Uber, DoorDash, Flexport, and Palantir re-checked — Palantir's Deployment
Strategist internship explicitly requires the applicant's *final* internship before a 2026
graduation, disqualifying a rising junior outright; no other change. One candidate considered and
excluded: a "Growth & Partnerships Intern" role at Tackle (YC-backed) surfaced in search, but both
the Work at a Startup and YC company-page URLs 404'd/redirected to the wrong company on every attempt
— could not confirm the posting is even still real, so not added; flagged here in case a working link
resurfaces on a future sweep.

**2026-09-01 sweep — no new Tier A/B rows, two closures from full `live`-row re-verification, one
Tier C row resolved.** Re-verified all 19 rows currently marked `live`: A5, A9, A10, A13, A65, A75,
A82, A83, A88 (WorkAtStartup/Wellfound — still 406/title-only on direct fetch, so confirmed via
WebSearch fallback against each company's YC jobs page instead) all still open, no field drift. A14
(Celonis), A22 (CertiK — recovered full content via curl+browser-UA after a WebFetch 403), A70 (Base
Power, "Reposted 12 Days Ago"), A92 (TraceRoot.AI), A96 (Crowe Global), A98 (Cresta), and A101
(Advancy Partners) all independently re-opened and confirmed unchanged. A112 and A114 (TikTok) both
re-confirmed via direct curl+UA fetch of the GradConnection page's embedded JSON: closing date is
25 Dec 2026, 3:59pm Sydney time on both, matching what was already tracked. **Two closures:** A19
(IBM) — the Clemson mirror that had held "Expires on September 1, 2026" verbatim across four sweeps
now confirms that date has arrived; a fresh WebFetch of the same mirror reads "the job listing
Expires on September 1, 2026 ... This position is no longer accepting applications," and IBM's own
SmartRecruiters/careers listing could not be found at all. Closed rather than left `unverified` —
the deadline was the one fact this row was always going to resolve cleanly. A24 (Lieberman Research
Worldwide) — WebFetch on the Built In listing now reads "this job was removed at 10:52 a.m. (UTC) on
Friday, Aug 28, 2026"; no replacement listing found.

New-lead sweep across all ten sources came back empty of addable rows, but surfaced enough on two
near-misses and one existing Tier C target to be worth recording rather than silently dropping.
**Wardstone (YC F25), Business Development Intern – Space and Missile Defense** (found via
WorkAtStartup WebSearch, $6–10K/mo, US-citizenship-required which Sam clears) is based in
**Los Angeles, CA** — not one of the target metros or an adjacent one (LA is not Bay Area-adjacent
the way Oakland or Palo Alto is) — so it was left off per the location hard exclusion rather than
added as a stretch. **Dexter (YC), Founders' Associate Intern** is Berlin-only, same exclusion.
**NAB's Sydney Summer Intern Program – Finance and Strategy** runs 23 Nov 2026 – 29 Jan 2027 — genuinely
inside the broader window on the back end, but it starts six weeks before Sam's target date, during
his enrolled fall semester, the same structural mismatch already documented for Canva/Atlassian in
the Australia section above — not added as its own row for the same reason those weren't. The five
target economic-consulting firms (Analysis Group, Cornerstone Research, CRA, Compass Lexecon,
Brattle) were checked directly again: all run Summer-only analyst/associate programs with
application windows opening Aug–Oct 2026 for a Summer 2027 start, no off-cycle track exists at any
of them — consistent with every prior sweep of this lane, C72–C75/C102 kept as-is. The SimplifyJobs
off-season README was downloaded raw and grepped programmatically for target functions crossed with
every target city and Winter 2027/Spring 2027 tags; the only match outside already-tracked
companies was an NBCUniversal "Academic Year" internship family (Advertising & Partnerships Ad
Products Intern, Data Science & Analytics Intern, Peacock Customer Journey – Decision Sciences
Intern) — chased down to a concrete finding below rather than added as a new row, since the existing
C70 already tracks this company/function. GradConnection Sydney's Business & Commerce category
returned nothing beyond already-tracked TikTok postings and more "2026/27 Summer" vacation programs
(CommBank, KPMG, EY, Pitcher Partners) on the same Nov/Dec-2026-start cycle already ruled structurally
out. BuiltIn (all three metros), Intern Insider, and Tokyo sources (Coral Capital 404s at the URL
tried, Japan Dev, TokyoDev) returned nothing new in scope — Tokyo remains software-engineering-only
on every source checked to date.

**C70 (NBCUniversal) resolved from a vague README pointer to a concrete, dated finding.** The
Advertising & Partnerships Ad Products Intern is not a Winter/Spring-specific req — it's NBCU's
"Academic Year" program, confirmed via WebSearch to run **Sept 2026 – Apr 2027** (two full semesters,
16–24 hrs/wk, $19/hr), a hard conflict with the Jan 4–Mar 12 window on both ends regardless of when
Sam could start. The specific SmartRecruiters requisition found (744000121820063) was then opened
directly and confirmed expired — this cohort's applications already closed earlier in 2026. Status
changed `monitor` → `conflict` with the dated note kept in place so this doesn't get re-discovered
as "new" on a future sweep; still worth a direct ask to NBCU about a standalone Jan–Mar arrangement,
since the fit on function (Partnerships) and seniority is otherwise real.

**2026-08-31 sweep — 1 new Tier A row (A115), two data-integrity corrections, no closures.**
Re-verified A19 (IBM, urgent) plus six other `live` Tier A rows not re-checked in the last couple of
sweeps (A5 Dalus, A10 Naive, A13 DeepAware AI, A14 Celonis, A96 Crowe Global, A97 Cadence Design
Systems) — **all seven confirmed accurate, no drift.** A5/A10/A13 still return title-only on direct
Work at a Startup fetch (the ongoing 406 regression) but are independently confirmed open and
unchanged via each company's YC jobs-page fallback. A14 and A96 held exactly as tracked. A97 (Cadence)
was found "Reposted 4 Days Ago" — a mild freshness signal, no other field changed.

**Correction — A11 (Claim Health) and A20 (Agentio) status desync fixed.** Both rows in this file
still read `live` despite a note immediately below the table (dated 2026-08-21) stating they were
closed under the social-media hard-exclusion rule, and despite `dashboard.html`'s `RAW` array already
correctly showing both as `closed` — a sync gap between the two files that had persisted for ten days.
Corrected both rows here to `closed` to match. No new information; this is a bookkeeping fix, not a
re-verification finding.

**A19 (IBM) — re-confirmed live and unchanged, deadline is TODAY/TOMORROW.** The Clemson mirror still
shows "Expires on September 1, 2026" verbatim, unchanged across four consecutive sweeps. A fresh WayUp
mirror check re-confirms the same 10-city location list (including Austin, SF, NYC) and
$71,100–$130,350/yr pay. IBM's own careers.ibm.com remains unreachable (403/empty) on every attempt
this month, so status stays `unverified` from the primary source. **This is the single most
time-critical row in the entire tracker — act today if pursuing at all.**

**New: A115 (Workiva), Commercial Strategy Intern — genuinely new company, `unverified`, Strategy
function.** Discovered via Intern Insider's Winter 2027 term page, which lists ~18 open Workiva intern
reqs spanning Sales Analytics, Sales Planning, Sales Enablement, Sales Program Management,
Partnerships, Commercial Strategy, Business Systems, and Financial Reporting — a real, structured,
multi-function internship program at a public company (NASDAQ: WK) with confirmed offices in NYC, SF,
and Austin (all three top domestic target markets). Could not resolve the exact live req URL for the
Winter-2027-tagged Commercial Strategy title itself (the cached Workday link from search results
redirected to a Workday maintenance page — a dead/stale req ID; the company's own
`/careers/internships` page is a client-rendered SPA that returns no listing content to any fetch
tool; the Workday CXS search API rejected every endpoint pattern tried). Instead independently
corroborated the program via two sibling sources: (1) a **live** Workday req for "Spring 2027 Intern -
Data Analytics" (`R12319`, posted 2026-08-27 — four days old — closes 2026-09-27) confirms the
company's Jan-start intern cycle begins **Monday, January 4, 2027**, exactly matching Sam's target
start date, part-time at 15–20 hrs/week, $22/hr, remote-primary with hybrid available near an office
hub; (2) a Welcome to the Jungle mirror of last year's **identical title**, "Commercial Strategy
Intern," confirms the role is a real recurring annual posting (Spring 2026 cycle: Jan 5 2026 start,
remote, part-time 20 hrs/week, now closed) — strong evidence the current Winter 2027 listing is this
same role's 2027 edition. **What's confirmed:** company, function, historical Jan-start pattern,
part-time format (a genuine plus for staying enrolled), NYC/SF/Austin office presence. **What's not:**
the exact live req URL for this specific title/cycle, the Winter 2027 term's actual end date (the
confirmed Spring-2027-tagged sibling role's cycle historically runs into May, which would overrun the
hard stop — but "Winter 2027" may be a shorter, differently-dated term; this distinction is
unconfirmed either way), and pay for this specific title. Added as `unverified`/Med rather than
`conflict` since the end-date risk itself isn't confirmed, only inferred from a same-company sibling
term. Link points to the company's own internships page since no working direct req URL could be
recovered — open it directly and search "Commercial Strategy" or the sibling titles above before
investing time.

**Everything else came back empty of new in-scope leads, matching every prior sweep.** Work at a
Startup continued the 406/title-only regression on direct fetch; WebSearch fallback and the YC
company-jobs-page technique (used for the A5/A10/A13 re-checks above) surfaced nothing new. The
SimplifyJobs off-season README was downloaded raw and parsed programmatically this time (company,
role, location, and term columns extracted and cross-filtered for target functions × Winter/Spring
2027 tags) — the most thorough pass on this source yet — and turned up nothing new: the Product
Management category's 26 active listings are 100% wrong-function or wrong-location (mostly Toronto
bank co-ops), the one Notion "Data Science Intern, SF, Winter 2027" hit is the same Ashby req already
tracked as A80, and the NBCUniversal "Advertising & Partnerships Ad Products Intern" (the source of
Tier C target C70) is confirmed still in the README's inactive/locked section, unchanged. Intern
Insider (winter-2027 and spring-2027 term pages beyond the Workiva find), BuiltIn (all three metros),
and GradConnection Sydney (re-fetched via curl+browser-UA, `WebFetch` still 403s the domain — one new
title seen, UNIQLO Australia "Management Trainee," excluded as a full-time retail graduate program,
not an internship) surfaced nothing that clears the quality bar. Economic consulting (CRA, Compass
Lexecon, Brattle, NERA checked directly this round) confirmed still summer-only / near-graduate-only
across the board, unchanged. Uber's Strategy & Operations internship is confirmed summer-only, Canada,
requiring Dec 2026–May 2027 graduation (not a rising junior); Palantir's Deployment Strategist
internship re-confirmed as a 10–12 week **summer** placement, not a January fit. Tokyo (Japan Dev,
TokyoDev) checked again — TokyoDev's intern filter returned zero listings of any kind this round
(previously always showed the one HENNGE SWE listing); Japan Dev unchanged, engineering-first, no
BD/growth/partnerships category.

**2026-08-30 sweep — no new Tier A/B/C rows, one status upgrade, two corrections.** Full sweep of
Work at a Startup (WebSearch fallback — direct fetch still returns only page-header text, no listings),
Wellfound, the SimplifyJobs off-season README, Intern Insider (winter-2027 and spring-2027 term pages),
BuiltIn (all three metros), and economic consulting firms (Analysis Group, Cornerstone Research
checked directly this round) surfaced nothing new that clears the quality bar — every result was
either already tracked, wrong-season (Summer/Fall 2026-27), or a generic summer-analyst track with no
off-cycle option, matching the pattern of every sweep since 2026-08-22. Tokyo (Japan Dev, TokyoDev,
Coral Capital) checked again via search — still no BD/growth/strategy/PM internship category exists
on any of the three, only the same HENNGE full-stack SWE listing.

**A114 (TikTok, AI Product Manager Intern, Sydney) upgraded `unverified` → `live`.** The job page still
403s a direct WebFetch, but `curl` with a browser user-agent recovered the full rendered posting
(React's embedded JSON state, not just the HTML shell) — the same workaround already noted for
GradConnection in earlier sweeps. Confirmed: position start date "Dec 2026 (approx)", closing date
25 Dec 2026 3:59pm; the posting does **not** state a 6-month minimum the way sibling A113 does — instead
it carries the identical "please clearly state your availability in your resume, including your start
and end dates" language already seen on A112, inviting a candidate-proposed Jan–Mar slice. The
work-rights list includes "Australian Working Visa" alongside citizen/PR/student-visa options — a
direct match to the subclass 462 route `PROFILE.md` confirms Sam is eligible for. No pay disclosed.
Priority raised Low → Med, Flex raised Low → High.

**A80 (Notion) — dates sharpened from an estimate to a confirmed range.** A BuiltIn SF mirror now
states the Winter 2027 Data Science Intern program runs **January 25 – April 16, 2027** exactly,
replacing the previous "Jan–Apr 2027" approximation carried since 2026-08-25. Still a 5-week overrun
past the 12 Mar hard stop — `conflict`/Med stands, now with a firm date instead of a range estimate.

**A19 (IBM) — re-confirmed live and unchanged, deadline now urgent.** The Clemson mirror still shows
"Expires on September 1, 2026" verbatim, unchanged across three consecutive sweeps. That deadline is
now roughly **2 days out** — the most time-critical row in the entire tracker. IBM's own careers.ibm.com
page remains unreadable (empty response) on every attempt so far this month; status stays `unverified`
from the primary source despite the mirror's consistency.

**2026-08-29 sweep — 1 new Tier A row (A114), three real corrections, no other new leads.**
Re-swept Work at a Startup, Wellfound, Simplify, the SimplifyJobs off-season README, Intern Insider,
BuiltIn (all three metros), economic consulting firms, Tokyo, and Australia/GradConnection. In
parallel, ran a targeted re-verification pass on 10 time-sensitive existing rows (A9, A19, A70, A80,
A82, A92, A98, A100, A101, A104) rather than a full re-check of every live row.

**New: A114 (TikTok, AI Product Manager Intern, TikTok Live-Revenue), Sydney.** A third, distinct
TikTok Sydney role found in GradConnection's search-results feed alongside the already-tracked A112/
A113, same LIVE-Revenue team as A113. The individual job page 403'd on every attempt — only generic
TikTok company boilerplate could be recovered, no req-specific dates or pay — so this is `unverified`
per the never-drop rule rather than guessed at. Circumstantial signals (a description snippet tied to
this listing family mentioning a Nov/Dec 2026 start, and a related TikTok LIVE posting elsewhere
citing a 6-month commitment) suggest it likely shares A113's conflict, but that's not confirmed from
the primary source. Open the GradConnection URL directly before investing time.

**Correction — A104 (Direct Agents) closed, real location error.** Re-opening the tracked Intern
Insider URL directly now shows the location verbatim as "Culver City, California, United States" —
not New York as tracked since 2026-08-26. Culver City is Los Angeles-area, outside every target
market and not an adjacent metro to SF/Bay Area (same logic that excluded HeyGen in an earlier
sweep). Downgraded from `live`/High to `closed`/Low on the location filter; the role itself still
appears open, so it's worth re-adding if a genuine NYC-office req from this company ever surfaces.

**Correction — A100 (APX/Aster) closed, confirmed dead rather than merely unverifiable.** The Intern
Insider listing's own metadata now reveals an application deadline of "Nov 24" — 2025, already ten
months past. Combined with four prior sweeps finding zero independent corroboration anywhere
(Ashby, LinkedIn, BNB Chain's own Aster board showing zero open roles, tokenjobs.io, asterdex.com)
and an 87+-day staleness flag on the listing itself, this is now closed rather than kept as a
low-confidence `unverified` lead.

**Correction — A19 (IBM) mode and pay updated, deadline re-confirmed.** The Sept 1 2026 deadline is
verbatim-confirmed via the Clemson mirror ("Expires on September 1, 2026") — about 4 days out at this
sweep, act now if pursuing. A WayUp mirror of the identical requisition (job ID 128345, retitled
there "Technical Sales Engineer Intern" — same req) newly discloses **hybrid** mode and pay of
**$71,100–$130,350/yr**, both corrected in from prior "In-person"/"Presumed paid" placeholders.
IBM's own careers.ibm.com page still returns empty content — unreadable, not just WAF-blocked — so
this remains sourced from independent mirrors rather than the primary listing, hence still
`unverified` overall.

**Nine other re-verified rows (A9, A70, A80, A82, A92, A98, A101) held with no drift** — A9 (Lambda
Robotics) and A82 (Soren) both still return title-only on direct Work at a Startup fetch (the ongoing
406/JS-shell regression) but are independently confirmed open and unchanged via the YC company jobs
page fallback. A70 (Base Power) was found freshly reposted 8 days ago. A92 (TraceRoot.AI) and A98
(Cresta) both confirmed still live and unchanged. A101 (Advancy) confirmed unchanged. A80 (Notion)
remains genuinely unverifiable beyond a search-confirmed existence check — Ashby's JS-rendered page
still won't yield pay/date/status detail to any direct fetch; the tracked `conflict`/Med status
stands unchanged from the 2026-08-25 corroboration.

**Everything else came back empty of new in-scope leads.** Work at a Startup's direct-fetch
regression (406/title-only) continued; WebSearch fallback surfaced only already-tracked companies or
wrong-window postings. Wellfound, Simplify, and the SimplifyJobs off-season README surfaced nothing
new past what's already tracked or excluded. Intern Insider surfaced one candidate that was checked
and excluded: BSE Global's "China Business Strategy Seasonal Internship" (Brooklyn, NY) — verified
directly to run Oct 14 2026 – May 13 2027 (7 months, hard window failure) and require Mandarin
fluency plus NBA-specific depth aimed at seniors/grad students. BuiltIn (all three metros) and
economic consulting firms confirmed unchanged (still no live winter/spring 2027 posting in the econ
consulting lane). Tokyo (Coral Capital, Japan Dev, TokyoDev) unchanged — no BD/growth/strategy/PM
category exists on any of the three.

**2026-08-27 sweep — 2 new Tier A rows (A110–A111), two corrections, one status upgrade, econ
consulting/Strategy & Ops lane confirmed still dead.** Full sweep of Work at a Startup, Wellfound,
Simplify, the SimplifyJobs off-season README (fetched as raw markdown directly, avoiding the
truncation WebFetch's summarizer was causing), Intern Insider, and BuiltIn (all three metros) —
plus direct checks of every economic consulting firm and Strategy & Ops target, and Tokyo/Australia
sources — surfaced two new conflict-flagged leads and no clean live adds.

**Corrections — A23 (Chubb) and A67 (Closure) both closed.** Chubb's Data Analyst Intern posting
was removed from the board as of 2026-08-26 — no longer live (the tracked "New York, NY (2
locations)" was in any case never independently confirmed as NYC; the posting only ever said "2
locations"). Closure's YC company jobs page now lists 7 full-time roles and zero internships of any
kind — the PM Intern listing appears to have been pulled entirely. Both kept per the never-drop rule.

**A70 (Base Power Company) upgraded `unverified` → `live`** — re-confirmed open, reposted within
the last week. No other field changed.

**A19 (IBM) — re-confirmed still live and unchanged, but the Sept 1 2026 deadline is now 5 days
out.** No drift on any tracked field. Act this week if pursuing.

**A80 (Notion) — re-check inconclusive, left as-is.** The Ashby application page is JS-rendered and
would not yield location/pay/mode detail to a direct fetch on two attempts. The existing
`conflict`/Med status (confirmed Jan–Apr 2027 window, a 3–4 week overrun) stands unchanged since it
was independently corroborated in the 2026-08-25 sweep; a manual browser check would be the only way
to fully re-verify pay/location this round.

**New: A110 (Walt Disney Company / ABC News) and A111 (Motive).** A110 is a genuinely new posting
(posted 2026-08-26, verified directly via Disney's Workday API) for an ABC News Insights and
Analytics Intern in NYC — strong quantitative fit (Excel, Tableau-adjacent audience research,
"Junior or Senior year preferred," $23/hr confirmed) but an explicit six-month Jan–Jun 2027 fixed
program with no flexible-dates language, overrunning the hard stop by ~2.5 months — `conflict`, not
addable as-is, though the Disney/ABC brand may be worth an email asking about a shortened slice.
A111 (Motive) is a Sales Development Intern in Austin found fresh on Built In Austin (verified on
Greenhouse) — home-market fit, but the posting states "Summer internship" with no Jan–Mar option;
`conflict`, worth a direct ask given the no-relocation advantage.

**Econ consulting and Strategy & Ops (C72–C81, C102–C103) re-checked directly — still no live
winter/spring 2027 posting anywhere in either lane.** Two peer firms checked for the first time
(Edgeworth Economics, Secretariat) plus Bates White: Edgeworth has a live "Summer Economist" role
but requires 1–3 years of prior econ-consulting experience and is summer-only — not addable for an
entry-level rising-junior ask. Secretariat and Bates White are both summer-only with no off-cycle
track. On the Strategy & Ops side, Anduril has a real "Strategy and Partnerships Intern" req that
matches the profile well, but it's closed and based in Costa Mesa, CA — not Austin, not addable.
Uber's S&O internship is confirmed summer-2027-only; DoorDash, Flexport, and Tesla show no
internship-level Strategy/Ops postings at all; Palantir's Deployment Strategist Internship req
pages 403'd on direct fetch this round, so the prior May–Sept timing finding is unconfirmed either
way, not re-verified. This lane stays a September–October cold-outreach play as planned.

**Tokyo and Australia came back empty again, confirming every prior finding still holds.** Coral
Capital's `/jobs/` path 404s (still a directory, not a board); Japan Dev remains ~89% engineering by
listing count with no BD/growth/partnerships category; TokyoDev's "Growth Marketing" filter surfaces
only software-engineering-titled roles, none of them internships. GradConnection's Sydney
business-and-commerce board (94 listings, fetched directly via curl) is still 100% Big-4/big-bank/
large-corporate branded graduate programs with zero startup listings.

**Considered and excluded, not padded in:** Buju.ai's Founding Marketing & Growth Intern (Wellfound,
Mountain View, hybrid, "flexible around classes") — genuinely enrollment-friendly like A5 (Dalus),
but the posting explicitly lists running the company's website and social media alongside growth
experiments, sitting on the excluded side of the substance test with pay terms unclear; left out
rather than added at Priority Low per the quality-bar rule. Also excluded: CreativeMode's "Growth
Hacking Intern" (SF, but explicitly social-media/influencer/community work for a gaming platform);
Motive's own Wellfound/YC mirrors (duplicate of the BuiltIn/Greenhouse listing already added as
A111); several wrong-season BuiltIn/Intern Insider postings (Capital One, Mastercard, Raytheon
Canada, GE Appliances, Coastal).

**Tooling note:** Work at a Startup job pages returned only the `<title>` tag to WebFetch on every
job ID tried this sweep (including a previously-confirmed-working one), and direct `curl` returned
HTTP 406 even with a browser user-agent — a regression from prior sweeps. Re-test next run in case
it's transient; WebSearch snippets remained usable as a fallback for discovery. Wellfound individual
job pages continued to fetch fine when live, and cleanly returned HTTP 410 when dead.

**2026-08-26 sweep — 6 new Tier A rows (A104–A109), no corrections needed, all 17 spot-checked
rows confirmed accurate.** Full sweep of Work at a Startup, Wellfound, Simplify, the SimplifyJobs
off-season README, and Intern Insider (worked around its client-rendered term pages via the site's
sitemap facet URLs — e.g. `/internships/roles/{role}/{location}` — a technique worth reusing).
Economic consulting, Strategy & Ops targets (Uber, DoorDash, Flexport, Palantir, Anduril, Tesla),
Tokyo (Coral Capital, Japan Dev, TokyoDev), and Australia (GradConnection, still 403ing direct
fetches) all re-checked directly — no live winter/spring 2027 posting anywhere in those lanes; one
near-miss noted below. Also re-verified: the 9 previously `live` Work at a Startup / Wellfound rows
(A5, A9, A10, A13, A65, A75, A82, A83, A88) and 8 time-sensitive rows (A14, A19, A22, A92, A96, A98,
A100, A101) — **all 17 confirmed accurate, no drift.** A19 (IBM)'s Sept 1 2026 deadline is
independently re-confirmed and still 6 days out at time of sweep.

**Best new find: A104 (Direct Agents)** — an AI Business Strategy & Operations Intern role at an
established NYC marketing/media agency, dashboards + AI-tooling + process work for account teams.
Clean fit with no date conflict (rolling, no stated minimum duration) — the first genuinely
conflict-free new Strategy-function add in several sweeps.

**A105–A107 add three more distinct Zipline internships** (Sales Operations Analyst, Marketing
Intern, Operations Experience Intern), found via Intern Insider — bringing the tracked Zipline count
to seven, all carrying the same Jan–Apr 2027 overrun as A4/A16/A64. Kept per the strong-fit/dates-
clash rule (`conflict`, not dropped) since Zipline is a Series C company where a shorter Jan–Mar ask
remains plausible, same logic as the existing four Zipline rows.

**A108 (Ekimetrics)** is an excellent functional match — a boutique strategy/data-science
consultancy doing Python/R modeling presented directly to clients, arguably the second-closest
econ+stats match on the board after the litigation-consulting firms — but its stated 6-month
minimum overruns the window by roughly four months. `conflict`/Med rather than dropped; worth an
email asking about a 10-week slice.

**A109 (Qureos)** is a real BD-scoped posting but reads as a generic/templated listing (evergreen
copy, stale posting date) — kept as `unverified` with the caveat rather than treated as fully
confirmed, per the never-drop rule.

**Considered and excluded, not padded in:** Audax Group's Data Engineer Co-op (Boston/NYC, tagged
Winter 2027) — the title leans toward the excluded pure-software-engineering lane rather than
analytics, and co-ops at this firm likely run a full ~6-month cycle past the hard stop; doubly
marginal, so left out per the quality-bar rule rather than added as a weak row. Also excluded this
sweep: Genentech's South SF ops internship (requires current Master's/PhD enrollment — fails
eligibility), Blueprint's remote Growth Marketing SEO & Content Intern (sits on the excluded
content-creation side of the substance test), and several Summer-2027/Fall-2026-dated postings
(Ephemeris Net, LinkedIn SF Ad Ops, SAP Palo Alto iXp ×2, Databricks PM, Mars & Co., Rystad Energy,
FTI Consulting ×2, Corient, Praytell, Jomboy Media, Tessera Labs) that don't clear the window filter.

---

## Tier B — Opens on a known date

| # | Company / Program | Role | Function | Location | Mode | Opens | Window | Pay | Diff | Fit | Priority | Status | Link |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B1 | Charles Schwab | 2027 Internship Program | Data/Business | Austin, TX + others | In-person | **Sept–Nov 2026** | 2027 cycles | Paid | 3 | ~3 | **High** | closed | [Schwab Jobs](https://www.schwabjobs.com/internship-academy) |
| B2 | Citi | Summer Analyst — Commercial Banking, APAC | BD/Strategy | Sydney, AU | In-person | Rolling | 10 wks, Dec–Feb | Paid | 4 | ~3 | Med | monitor | [Citi Careers](https://jobs.citi.com/) |
| B3 | Bank of America | Global IB & Capital Markets Summer Analyst 2026/27 | Finance | Sydney, AU | In-person | Rolling | Dec–Feb | Paid | 5 | ~2 | Low | monitor | [BofA Careers](https://careers.bankofamerica.com/en-us/students) |
| B4 | Big 4 advisory (Deloitte / PwC / EY / KPMG) | Advisory & Analytics spring intern | Data/Strategy | Austin, NYC, SF | Hybrid | **Aug–Sept 2026** | Jan–Apr 2027 | Paid | 3 | ~3 | **High** | monitor | search each careers site |


**Confirm the end date on every Tier B row before applying.** B4 is a structured program whose
spring cycle commonly runs into April or May. If it cannot finish by 12 March, it is out —
see the scope note at the top of this file.

**B1 (Charles Schwab) closed 2026-10-17.** Checked directly on Schwab's own Intern Academy page since
the row's "opens" window (Sept–Nov 2026) was active as of this sweep. Schwab's 2027 program is
summer-only — a nine-week cohort running June 7–August 6, 2027, with the page stating "we are not able
to make exceptions" on those dates. No spring or winter cycle exists. This was tracked as "monitor" on
the assumption a spring cycle might open in this window; confirmed that assumption was wrong, so closed
per the hard exclusion on anything that can't finish by Mar 12 (this one hasn't even started by then).

---

## Tier C — Target list for direct outreach

No posting exists. These match the profile on function, stage, and location. **The play is
cold outreach in Sept–Oct 2026**, not waiting for a posting. Ask for a Jan–Mar project-based
stint; frame Q1 availability as solving their understaffing problem.

Search these titles at each: `founder's associate` · `chief of staff` · `growth associate` ·
`business analyst` · `strategy & ops` · `partnerships associate` · `GTM intern`.

### New York City

| # | Company | Why it fits | Function target | Stage | Diff | Fit | Status | Careers |
|---|---|---|---|---|---|---|---|---|
| C1 | Ramp | Famously hires generalist hustlers; strong analytics culture | Growth, Biz Ops | Late-stage | 5 | ~4 | monitor | [ramp.com/careers](https://ramp.com/careers) |
| C2 | Mercury | Fintech, strong data + GTM functions | Growth, Data | Late-stage | 4 | ~4 | monitor | [mercury.com/jobs](https://mercury.com/jobs) |
| C3 | Attentive | Growth-heavy, quantitative marketing | Growth, Data | Late-stage | 3 | ~4 | monitor | [attentive.com/careers](https://www.attentive.com/careers) |
| C4 | Vanta | Fast-growing, partnerships-heavy motion | Partnerships, BD | Late-stage | 4 | ~4 | monitor | [vanta.com/careers](https://www.vanta.com/careers) |
| C5 | Alloy | Fintech infra, small BD team | BD, Partnerships | Series C | 3 | ~4 | monitor | [alloy.com/careers](https://www.alloy.com/careers) |
| C6 | Datadog | Large, structured analytics org | Data Science | Public | 4 | ~3 | monitor | [careers.datadoghq.com](https://careers.datadoghq.com/) |
| C7 | Oscar Health | Econ/stats fit, human-centered mission | Data, Strategy | Public | 3 | ~4 | monitor | [hioscar.com/careers](https://www.hioscar.com/careers) |
| C8 | Justworks | HR tech, social culture, BD motion | BD, Growth | Late-stage | 2 | ~4 | monitor | [justworks.com/careers](https://www.justworks.com/careers) |
| C9 | Sardine | Fraud/risk AI, quantitative | Data, Strategy | Series C | 3 | ~4 | monitor | [sardine.ai/careers](https://www.sardine.ai/careers) |
| C10 | Dorsia | Consumer, NYC-native, social product | Growth, Partnerships | Early | 3 | ~4 | monitor | [Wellfound](https://wellfound.com/) |
| C63 | EINO | Techstars-backed SaaS, North Williamsburg, real GTM Intern req found (currently closed) | Growth, GTM | Early | 2 | ~4 | monitor | [Techstars board](https://jobs.techstars.com/companies/eino/jobs/63449764-gtm-intern) |
| C70 | NBCUniversal | Resolved 2026-09-01: this is NBCU's "Academic Year" internship program (Advertising & Partnerships Ad Products Intern, plus siblings like Data Science & Analytics Intern and Peacock Customer Journey – Decision Sciences Intern), not a Winter/Spring-specific req. Confirmed dates run **Sept 2026 – Apr 2027** (two full semesters, 16–24 hrs/wk, $19/hr), a hard structural conflict with the Jan 4–Mar 12 window on both ends. The specific SmartRecruiters req found (744000121820063) has already expired — this cohort's applications closed in spring 2026. Kept as a Tier C outreach target since NBCU clearly runs Partnerships/Data internships at the right seniority; worth asking directly whether a standalone Jan–Mar block is possible, since the standing req structurally won't be | Partnerships | Enterprise | 4 | ~4 | conflict | [nbcunicareers.com](https://www.nbcunicareers.com/) |
| C71 | Actively | Confirmed to run a generalist Founder's Associate / Business Operations function — a live Wellfound req is real but is a full-time, $140–175K role requiring 1–3 yrs PE/banking/consulting experience, not an internship. Worth a cold email asking about a junior/shorter version rather than applying to the listed req | Biz Ops, Founder's Associate | Early | 3 | ~3 | monitor | [Wellfound](https://wellfound.com/jobs/4064957-business-operations-founder-s-associate) |

### San Francisco / Bay Area

| # | Company | Why it fits | Function target | Stage | Diff | Fit | Status | Careers |
|---|---|---|---|---|---|---|---|---|
| C11 | Rippling | **Confirmed to run off-cycle winter internships** (SWE, Winter 2027) — so the program structure exists; ask for a business-side seat | Growth, Biz Ops | Late-stage | 5 | ~4 | monitor | [rippling.com/careers](https://www.rippling.com/careers) |
| C12 | Scale AI | AI, hustle culture, strong GTM | Growth, Strategy | Late-stage | 5 | ~4 | monitor | [scale.com/careers](https://scale.com/careers) |
| C13 | Notion | Human-centered product, PM-heavy | PM, Growth | Late-stage | 5 | ~4 | monitor | [notion.so/careers](https://www.notion.so/careers) |
| C14 | Retool | Technical-adjacent GTM | BD, Growth | Late-stage | 4 | ~4 | monitor | [retool.com/careers](https://retool.com/careers) |
| C15 | Sierra AI | Applied/human-centered AI | Partnerships, Growth | Early | 5 | ~4 | monitor | [sierra.ai/careers](https://sierra.ai/careers) |
| C16 | Brex | Fintech, quantitative growth org | Growth, Data | Late-stage | 4 | ~4 | monitor | [brex.com/careers](https://www.brex.com/careers) |
| C17 | Dedalus Labs | Early-stage AI/cloud; **posted a 2027 intern role at $20–25/hr** — small enough to ask about off-cycle | Growth, BD | Early | 2 | ~4 | monitor | [Wellfound](https://wellfound.com/) |
| C18 | YC W27 batch companies | Batch runs from **Nov 2026** — brand-new companies desperate for help exactly when you're free | Founder's Associate | Pre-seed | 2 | ~5 | **apply Nov 2026** | [workatastartup.com](https://www.workatastartup.com/) |

> **C18 is the single highest-leverage row in this file.** The YC Winter 2027 batch starts
> November 2026. Those companies are 1–4 people, have just raised, and need generalists
> immediately — with a hiring process measured in days. Your Jan–Mar availability is a
> feature. Set a reminder for early November 2026 to sweep Work at a Startup end to end.

### Austin

| # | Company | Why it fits | Function target | Stage | Diff | Fit | Status | Careers |
|---|---|---|---|---|---|---|---|---|
| C19 | ICON | 3D-printed construction, Austin-native | Strategy, BD | Late-stage | 3 | ~3 | monitor | [iconbuild.com/careers](https://www.iconbuild.com/careers) |
| C20 | Self Financial | Fintech, mission-driven, quantitative | Data, Growth | Late-stage | 2 | ~4 | monitor | [self.inc/careers](https://www.self.inc/careers) |
| C21 | AlertMedia | Austin SaaS, strong BD org | BD, Partnerships | Late-stage | 2 | ~4 | monitor | [alertmedia.com/careers](https://www.alertmedia.com/careers) |
| C22 | Osano | Privacy SaaS, small teams | Growth, BD | Series B | 2 | ~4 | monitor | [osano.com/careers](https://www.osano.com/company/careers) |
| C23 | Firefly Aerospace | High-profile Austin-area, hustle culture | Strategy, Biz Ops | Late-stage | 4 | ~3 | monitor | [firefly.com/careers](https://fireflyspace.com/careers/) |
| C24 | H-E-B Digital | Large Austin employer, real analytics org | Data Science | Enterprise | 3 | ~3 | monitor | [careers.heb.com](https://careers.heb.com/) |
| C25 | Indeed | Austin HQ, huge data org, econ research team | Data Science | Enterprise | 3 | ~4 | monitor | [indeed.jobs](https://www.indeed.jobs/) |
| C69 | Zello | Real SQL/Snowflake/dbt/Omni-BI analytics intern req exists, but it's a Fall 2026 cohort ending early December — ask directly about a winter/spring cohort | Data | Mid-size | 2 | ~4 | monitor | [Built In listing](https://builtin.com/job/analytics-intern/10488836) |
| C116 | BuildPass | Australian construction-tech SaaS (~$5M seed 2024, ~10% MoM growth) that recently opened a US presence in Austin — home market. Aggregator snippets describe a Founder's Associate role (business cases, data-driven insights, sales-prospect follow-up), but no live application URL exists anywhere; company site routes to LinkedIn/email only. Cold-outreach target, not a verified posting | Strategy, Founder's Associate | Early (seed) | 2 | ~4 | monitor | [buildpass.ai](https://buildpass.ai/us/about-us) |

> **Austin is your cheapest shot on goal.** No relocation, no visa, and you can take in-person
> meetings while enrolled. If the light course load turns out heavier than expected, Austin
> roles are the ones that survive that.

### Australia

| # | Company | Why it fits | Function target | Stage | Diff | Fit | Status | Careers |
|---|---|---|---|---|---|---|---|---|
| C26 | Airwallex | Fintech, Melbourne roots, global GTM | Growth, BD | Late-stage | 4 | ~4 | monitor | [airwallex.com/careers](https://www.airwallex.com/careers) |
| C27 | SafetyCulture (now Mitti) | Sydney, strong commercial org | BD, Partnerships | Late-stage | 3 | ~4 | monitor | [mitti.com/safetyculture](https://mitti.com/safetyculture) |
| C28 | Linktree | Melbourne, consumer growth | Growth, Data | Late-stage | 3 | ~4 | monitor | [linktr.ee/careers](https://linktr.ee/s/about/careers/) |
| C29 | Immutable | Sydney, fast-moving | Partnerships, BD | Late-stage | 3 | ~3 | monitor | [immutable.com/careers](https://www.immutable.com/careers) |
| C30 | Employment Hero | Sydney HR tech, aggressive growth | Growth, BD | Late-stage | 3 | ~4 | monitor | [employmenthero.com/careers](https://employmenthero.com/careers/) |
| C31 | SEEK Grad (board) | Aggregates ANZ internships — 98 open business/commerce roles in Sydney at last check | All | — | — | — | **sweep monthly** | [au.gradconnection.com](https://au.gradconnection.com/internships/business-and-commerce/sydney/) |

> **Australia action item:** the 462 visa has a ~2,500/year US cap and closes when hit. If you
> want Australia at all, start the visa before you have an offer — it's a working-holiday visa,
> not employer-sponsored, so it doesn't require one.

### Japan (Tokyo)

`OPEN, UNPAID ONLY.` Sam relocates to Japan 1 April regardless, which makes a Jan–Mar Tokyo stint
uniquely low-friction: no second relocation, a network built before the semester, and a conversion
path to paid part-time work (28 hrs/week) once he's on a student visa in April. Unpaid internships
of ≤90 days on Temporary Visitor status are permitted for students enrolled at an overseas
university — the window is 68 days. See `PROFILE.md` → Location Feasibility.

**Positioning:** lead with the April relocation. It removes visa sponsorship, housing, and
flight-risk objections at once. Target companies with overseas ambitions where native English is a
concrete asset. Don't claim Japanese ability.

| # | Company | Why it fits | Function target | Prestige | Diff | Fit | Status | Careers |
|---|---|---|---|---|---|---|---|---|
| C8 | LayerX | Series B, English-friendly, strong commercial org | BD, Growth | 4 | 3 | ~4 | monitor | [layerx.co.jp](https://layerx.co.jp/en) |
| C11 | Ubie | Health AI, international orientation, hires non-Japanese speakers | BD, Market research | 3 | 3 | ~4 | monitor | [ubiehealth.com](https://ubiehealth.com/) |
| C28 | Mercari | Japan's best-known consumer tech company, international team | Data, Growth | 5 | 4 | ~4 | monitor | [careers.mercari.com](https://careers.mercari.com/) |
| C29 | SmartNews | US–Japan bridge company; native English is a concrete asset | Growth, Data | 4 | 4 | ~4 | monitor | [about.smartnews.com](https://about.smartnews.com/en/careers/) |
| C30 | SmartHR | HR SaaS unicorn expanding internationally | Growth, BD | 3 | 3 | ~3 | monitor | [smarthr.co.jp](https://smarthr.co.jp/en/) |
| C31 | Money Forward | Fintech with a large data org — econ background directly relevant | Data, Fintech | 4 | 4 | ~3 | monitor | [corp.moneyforward.com](https://corp.moneyforward.com/en/) |
| C32 | Coral Capital portfolio | Tokyo VC publishing in English with a portfolio job board. Best entry point to English-friendly Japanese startups. | Startup generalist | 3 | 2 | ~4 | monitor | [coralcap.co](https://coralcap.co/) |
| C58 | Sansan | B2B SaaS with international ambitions; English market research valued | BD, Research | 4 | 3 | ~4 | monitor | [corp-sansan.com](https://jp.corp-sansan.com/en/) |
| C59 | MarqVision | Coral Capital portfolio, global brand-protection SaaS with active Seoul/SF/London/Tokyo hiring on Greenhouse — real signal of an English-operating team | BD, Partnerships, CS | 2 | 2 | ~4 | monitor | [marqvision.com](https://www.marqvision.com/) |
| C60 | GITAI | Space robotics; careers page explicitly seeks "business development professionals," not just engineers. Tokyo HQ, but current open reqs are all LA-based | BD | 3 | 2 | ~3 | monitor | [gitai.tech/careers](https://gitai.tech/careers/) |
| C61 | Shippio | Coral Capital portfolio, international freight-forwarding SaaS — trade with overseas partners is core to the business | BD, Market research | 2 | 2 | ~4 | monitor | [shippio.io](https://www.shippio.io/) |
| C62 | Authlete | Coral Capital portfolio, OAuth/API infrastructure sold globally to developers — English-first docs, developer-relations/BD adjacency | BD, DevRel | 2 | 2 | ~4 | monitor | [authlete.com](https://www.authlete.com/) |

### Spain

| # | Company | Why it fits | Function target | Stage | Diff | Fit | Status | Careers |
|---|---|---|---|---|---|---|---|---|
| C32 | TravelPerk (Perk) | Barcelona, English-first, 50+ nationalities | Growth, BD | Unicorn | 4 | ~4 | blocked* | [travelperk.com/careers](https://www.travelperk.com/careers/) |
| C33 | Factorial | Barcelona + Madrid, HR tech unicorn | Growth, Data | Unicorn | 4 | ~4 | blocked* | [factorialhr.com/careers](https://factorialhr.com/careers) |
| C34 | Typeform | Barcelona, product-led growth | Growth, PM | Late-stage | 4 | ~4 | blocked* | [typeform.com/careers](https://www.typeform.com/careers/) |
| C35 | Glovo | Barcelona, English working language, has intern roles | Growth, Data | Unicorn | 3 | ~4 | blocked* | [jobs.glovoapp.com](https://jobs.glovoapp.com/) |

\* **All Spain rows are gated on the convenio de prácticas question.** English is the working
language at these companies and the roles fit well — the obstacle is purely the UT Austin
signature. **Email Texas Global this month.** If they'll sign, unblock all four and this
becomes a strong market. If not, delete this section and reallocate to Australia + US.

### Israel

| # | Company / Route | Why it fits | Function target | Diff | Fit | Status | Link |
|---|---|---|---|---|---|---|---|
| C36 | Destination Israel | Runs a 1,200-company Israeli internship database; has 2-month tracks | Various | 3 | ~3 | blocked† | [destinationisrael.com](https://www.destinationisrael.com/) |

† **Israel is effectively closed for this window.** The March 12 deadline rules out every
program-mediated route independent of the eligibility question — Masa needs 5+ months, Career
Israel 4–6. Destination Israel's 2-month track is the only shape that could fit, and a January
cohort is unconfirmed. Deprioritize unless something changes.

---

### Economic consulting & Strategy & Operations (added 2026-08-21, synced to this file 2026-08-22)

Economic consulting is the single best functional match on the whole board — an econ major with a
stats minor *is* the qualification these firms recruit for, and they staff case-by-case rather than
running a fixed cohort, so an off-cycle block is a realistic ask. **Search these firms and their
peers every run.** Strategy & Operations (Uber/DoorDash/Flexport) and Deployment Strategist
(Palantir) are the second lane — own a metric, find why it moved, ship the fix.

**Correction 2026-08-22:** these ten rows (C72–C81) were added to `dashboard.html`'s `RAW` array on
2026-08-21 but never synced into this file — a gap in that sweep. Backfilled here now, unchanged.

| # | Company | Role target | Function | Location | Flex | Prestige | Diff | Fit | Careers |
|---|---|---|---|---|---|---|---|---|---|
| C72 | Analysis Group | Analyst intern — economic consulting | Strategy | New York | Med | 4 | 3 | ~5 | [analysisgroup.com](https://www.analysisgroup.com/careers/) |
| C73 | Cornerstone Research | Analyst intern — economic & data analysis | Strategy | New York | Med | 4 | 4 | ~5 | [cornerstone.com](https://www.cornerstone.com/careers/) |
| C74 | Charles River Associates | Consulting intern — economics | Strategy | New York | Med | 4 | 3 | ~5 | [crai.com](https://www.crai.com/careers/) |
| C75 | Compass Lexecon | Economic analyst intern | Strategy | New York | Med | 4 | 3 | ~4 | [compasslexecon.com](https://www.compasslexecon.com/careers/) |
| C76 | Uber | Strategy & Operations | Strategy | San Francisco | Med | 5 | 4 | ~4 | [uber.com/careers](https://www.uber.com/us/en/careers/) |
| C77 | DoorDash | Strategy & Operations | Strategy | New York | Med | 5 | 4 | ~4 | [careers.doordash.com](https://careers.doordash.com/) |
| C78 | Flexport | Strategy / biz ops | Strategy | San Francisco | Med | 4 | 4 | ~4 | [flexport.com/careers](https://www.flexport.com/careers/) |
| C79 | Palantir | Deployment Strategist | Strategy | New York | Low | 5 | 5 | ~4 | [palantir.com/careers](https://www.palantir.com/careers/) |
| C80 | Anduril | Strategy / business operations | Strategy | Austin | Med | 5 | 4 | ~3 | [anduril.com/careers](https://www.anduril.com/careers/) |
| C81 | Tesla | Business operations / strategy | Strategy | Austin | Low | 5 | 4 | ~3 | [tesla.com/careers](https://www.tesla.com/careers) |
| C102 | Brattle Group | Analyst intern — economic consulting | Strategy | New York | Med | 4 | 3 | ~4 | [brattle.com/careers](https://www.brattle.com/careers/) |
| C103 | NERA Economic Consulting | Analyst intern — economic consulting | Strategy | New York | Low | 4 | 4 | ~4 | [nera.com](https://www.nera.com/open-roles.html) |

**New 2026-08-22: C102 (Brattle) and C103 (NERA)**, added as peer economic-consulting outreach
targets per the "search these firms and their peers" instruction — same logic as C72–C75.

**2026-08-22 sweep of C72–C75 direct — no live winter/spring 2027 posting at any of the four.**
Analysis Group and Cornerstone Research show only generic summer-program descriptions with no
individual reqs. Compass Lexecon's careers page routes through a Workday portal that would not
render for the sweep — external sources confirm a summer-only track, but could not independently
verify. **Charles River Associates (C74)** is the one firm with a live rolling internship right now
— three "Intern (European Competition practice)" reqs in Brussels, Düsseldorf, and Munich — but they
explicitly require a Master's/PhD in economics and EU work authorization, and the location is outside
the target list, so none is addable against this profile. Worth noting for future sweeps: CRA's live
board also showed a now-expired "Analyst Intern (Labor & Employment practice) — Winter/Spring 2026"
req, confirming the firm has run a US winter/spring cohort before — re-check periodically for a 2027
successor. Brattle (C102) and NERA (C103) also show summer-only tracks at time of check; NERA's
program additionally requires final-year ("2027 grad") standing, which a rising junior doesn't meet
— both kept as cold-outreach targets on the strength of the firm/function fit, not a live posting.

---

### Technical-adjacent & business development (added 2026-08-17)

Sam wants to sit close to engineering without being an engineer. That is a defined lane with real
titles: **solutions engineer / sales engineer** (pre-sales), **solutions architect**, **technical
account manager**, **deployment strategist**, **developer relations**, **partnerships at an API
company**, and **product / revenue operations**. These screen for translation ability rather than
implementation ability, they are customer-facing and social, and SQL plus product curiosity is
genuinely enough to enter. See the *Technical-adjacent lane* section of `dashboard.html`.

| # | Company | Role target | Function | Location | Flex | Prestige | Diff | Fit | Careers |
|---|---|---|---|---|---|---|---|---|---|
| C43 | Plaid | Partnerships / solutions | Partnerships | New York | High | 5 | 4 | 5 | [plaid.com](https://plaid.com/careers/) |
| C44 | MongoDB | Solutions / BD | BD | New York | Med | 5 | 4 | 4 | [mongodb.com](https://www.mongodb.com/careers) |
| C45 | Modal Labs | BD / growth | BD | New York | High | 3 | 2 | 5 | [modal.com](https://modal.com/careers) |
| C46 | Hightouch | GTM / solutions | Growth | San Francisco | High | 3 | 3 | 5 | [hightouch.com](https://hightouch.com/careers) |
| C47 | Hex | Growth / solutions | Growth | San Francisco | High | 3 | 3 | 5 | [hex.tech](https://hex.tech/careers/) |
| C48 | Amplitude | Solutions consultant / growth | Growth | San Francisco | Med | 4 | 3 | 5 | [amplitude.com](https://amplitude.com/careers) |
| C49 | Twilio | Solutions engineering / BD | BD | San Francisco | Med | 4 | 4 | 4 | [twilio.com](https://www.twilio.com/en-us/company/jobs) |
| C50 | Vercel | DevRel / solutions | BD | San Francisco | High | 4 | 4 | 4 | [vercel.com](https://vercel.com/careers) |
| C51 | Baseten | GTM / BD | BD | San Francisco | High | 3 | 2 | 5 | [baseten.co](https://www.baseten.co/careers/) |
| C52 | Stripe | Partner / BD | Partnerships | San Francisco | Low | 5 | 5 | 4 | [stripe.com](https://stripe.com/jobs) |
| C53 | SailPoint | BD / solutions | BD | Austin | Med | 3 | 3 | 4 | [sailpoint.com](https://www.sailpoint.com/company/careers/) |
| C54 | CrowdStrike | BD / sales development | BD | Austin | Low | 5 | 4 | 3 | [crowdstrike.com](https://www.crowdstrike.com/careers/) |
| C55 | Procore | BD / partnerships | BD | Austin | Med | 4 | 3 | 4 | [procore.com](https://careers.procore.com/) |
| C56 | Braze | BD / solutions | BD | New York | Med | 4 | 3 | 4 | [braze.com](https://www.braze.com/company/careers) |
| C57 | LangChain | DevRel / BD | BD | San Francisco | High | 4 | 3 | 4 | [langchain.com](https://www.langchain.com/careers) |
| C58 | Sansan | BD / market research | BD | Tokyo | Med | 4 | 3 | 4 | [corp-sansan.com](https://jp.corp-sansan.com/en/) |

**Highest-fit of the batch:** Plaid, Modal, Hightouch, Hex, Amplitude, Baseten. All either sell to
data teams (so the stats minor is the qualification) or are small enough that a cold email reaches
someone who decides.

**2026-08-19 sweep note — Tokyo, Australia, and the targeted technical-adjacent title search
all came back empty again**, confirming the 2026-08-18 findings still hold: Coral Capital remains a
directory not a job board, Japan Dev/TokyoDev remain engineering-first, GradConnection's Sydney/
Melbourne/Brisbane counts are unchanged (95/96/70) with zero startup listings, and direct Ashby/
Greenhouse API checks against ~35 named dev-tool/API companies produced zero live Solutions
Engineer/DevRel/RevOps/TAM/Chief-of-Staff intern reqs — Spring 2027 postings for these titles simply
haven't opened yet. One new Tokyo source was checked and ruled out: iAgora surfaced a ByteDance/
BytePlus Sales Intern (Tokyo, English-friendly, BD-adjacent) but it requires a 3-month minimum
commitment against Sam's 68-day window — not addable. SafetyCulture (C27, Australia table above)
rebranded to **Mitti** on 2026-08-11; no live internship req either name, still a cold-outreach target.

**2026-08-18 sweep note — Tokyo and Australia came back empty.** Coral Capital's site is a company
directory plus the fund's own hiring page, not a browsable portfolio job board — no per-company
listings exist to sweep; treat it as a cold-outreach index only. Japan Dev (~284 listings) and
TokyoDev (~149 listings) are both structurally engineering-first — Japan Dev has no BD/DevRel
category at all, and its one Sales/Marketing listing requires business Japanese. GradConnection's
Sydney/Melbourne/Brisbane business-and-commerce boards (95/96/70 listings checked) are entirely
big-bank/Big-4/large-corporate branded graduate programs — zero startup or small-employer listings
turned up anywhere. None of the C8/C11/C28–C32/C58–C62 Tokyo targets or C26–C31 Australia targets
changed status; all remain cold-outreach plays, not live postings.

## Boards to sweep monthly

| Board | Why | Sweep cadence |
|---|---|---|
| [Work at a Startup (YC)](https://www.workatastartup.com/) | Highest leverage. Message founders directly. | **Weekly from Nov 2026** |
| [Wellfound](https://wellfound.com/jobs) | Startup-dense; good BD/growth filtering | Biweekly |
| [UT Austin Handshake](https://utexas.joinhandshake.com/) | Employers targeting UT specifically; off-cycle roles appear here that appear nowhere else | **Weekly** |
| [Built In NYC](https://www.builtinnyc.com/jobs) / [Austin](https://www.builtinaustin.com/jobs) / [SF](https://www.builtinsf.com/jobs) | Local tech concentration | Biweekly |
| [Otta / Welcome to the Jungle](https://app.otta.com/) | Strong filters, Europe coverage | Monthly |
| [SEEK Grad (ANZ)](https://au.gradconnection.com/) | Australian internships | Monthly |
| [Simplify — Winter & Spring list](https://simplify.jobs/l/Top-Winter-and-Spring-Internships) | Dedicated off-cycle list, 230 roles added in a week at last check. Skews engineering/healthcare — filter hard. | Biweekly |
| [SimplifyJobs off-season README (raw)](https://raw.githubusercontent.com/SimplifyJobs/Summer2027-Internships/dev/README-Off-Season.md) | Community-maintained, updated daily. **Verified 2026-08-17: the Winter/Spring 2027 list is ~100% software engineering — zero business, data or growth roles.** That single fact explains why off-season sweeps come back empty. Use the raw URL; the github.com page is not fetchable by the agent. | **Weekly** |
| [Intern Insider — Winter 2027](https://interninsider.me/internships/terms/winter-2027) | ~400 open Winter 2027 roles across ~170 companies, updated continuously. Reachable by the agent. Mostly finance/consulting/engineering, but the best single source of genuinely winter-term postings. | **Weekly** |
| [sndsh404 off-season repo](https://github.com/sndsh404/summer-2027-internships) | Second community repo; explicitly covers off-season data/product roles | Biweekly |
| [intern-list.com](https://www.intern-list.com/da-intern-list) | Daily-updated data analyst intern list | Weekly |
| [Wayfair careers](https://www.wayfair.com/careers) | Runs Jan-start Data Science co-ops (Jan 5 – Jun 19 precedent, $27.50/hr) | Monthly from Sept |

---

## Recruiting calendar

| When | Do this |
|---|---|
| **Aug 2026 (now)** | Upload resume. Email **UT Austin Texas Global** re: Spain convenio. Confirm **Masa eligibility**. Apply for **Australian 462 visa** if pursuing AU (annual cap). Apply to Tier A. |
| **Sept 2026** | Big 4 advisory spring applications open. Schwab 2027 postings begin. Birthright Excel registration opens Sept 1 (summer only). Begin **cold outreach** to Tier C — this is the month it starts working. |
| **Oct 2026** | Peak corporate posting season. Push outreach hard; follow up on non-replies. |
| **Nov 2026** | 🔴 **YC W27 batch starts — sweep Work at a Startup end to end.** Highest-leverage week of the whole search. |
| **Dec 2026** | Startups begin posting Q1 roles. Close out offers. |
| **Jan–Mar 2027** | Start. Late-posting startup roles still appear — keep a light sweep running in case a better option lands. |

---

## Automated monitoring

A cloud routine — **WINTERNSHIP daily job sweep** (`trig_01FJifiSN9LgKwExGsBCo3BZ`) — runs
**every day at 09:00 ET**. It clones this repo, reads `PROFILE.md` for scoring context, sweeps the
boards above, writes new rows into this file and the `RAW` array in `dashboard.html`, marks expired
roles `closed`, and pushes. Manage it at
<https://claude.ai/code/routines/trig_01FJifiSN9LgKwExGsBCo3BZ>.

Two things it can't do: publish the dashboard Artifact (needs a manual republish after it adds
rows), and score against a resume that isn't in `PROFILE.md` yet.

**Expect empty days.** The agent is instructed that finding nothing is the correct outcome and to
make no commit at all rather than pad the tracker. Yield stays near zero until November 2026, when
the YC Winter batch lands.

## ⚠️ Sweep agent network access

**Major update, 2026-08-18: the allowlist was widened substantially since the previous sweep.**
Re-probed and verified with real fetches (not just status codes — a proxy block page can return 200
too, so every domain below was confirmed by actually reading returned content):

**Now reachable (confirmed 2026-08-18):** `WebSearch` (server-side, never blocked),
`raw.githubusercontent.com`, `github.com`, `interninsider.me`, **`workatastartup.com`** (the
highest-leverage source once the YC W27 batch lands in November — and it's already producing real
leads even pre-batch), **`wellfound.com`**, **`simplify.jobs`** (server-side-rendered listings only —
see caveat below), **`builtinnyc.com` / `builtinaustin.com` / `builtinsf.com`**,
**`linkedin.com`** (individual job posting pages fetch cleanly), **`coralcap.co`**,
**`tokyodev.com`**, **`japan-dev.com`**, `job-boards.greenhouse.io` (redirects to greenhouse.com,
both load).

**Still worth checking each run, not yet confirmed:** `au.gradconnection.com`, `jobs.ashbyhq.com`
(returned 404 on a bare root-path probe — inconclusive, try a real job URL next time).

**Partial/caveat:** `simplify.jobs` is a client-rendered SPA — the server only pre-renders the first
~30 of 324 listings (sorted by recency); everything past that is loaded by client-side JS calling an
undocumented backend API. Headless-browser automation (Playwright/Chromium) to drive the real filter
UI was attempted and failed with `ERR_CONNECTION_RESET` at the TLS layer for **all** HTTPS traffic
through the proxy, not just this site — so this is a proxy limitation on headless-browser traffic
specifically, not a Simplify-specific block. `curl`/`WebFetch` work fine on this and every other
domain. Wellfound has the same SPA issue for its search/filter UI specifically — search/filter query
params don't actually filter when fetched directly; individual job-detail-page URLs do fetch
correctly, so discovery has to route through WebSearch/Google-indexed URLs and then verify each one
individually. A large fraction of Wellfound's indexed results turned out to be dead (410/404) —
its search index is stale, verify every lead individually rather than trusting search snippets.

**If this list has drifted by the next run, re-probe and update it here** — do not assume the old
"blocked" list from before 2026-08-18 is still accurate.

## Scope rules

**Wanted functions:** data science/analytics · **strategy** (economic consulting + Strategy & Ops) ·
growth · business development · strategic partnerships · technical-adjacent commercial (solutions
and sales engineering, DevRel, technical account management, product/revenue ops) · product
management · sales.

**Excluded outright:**

| Excluded | Why |
|---|---|
| Social media, content marketing, community management, creator/influencer marketing | Sam does not want this work. The test is substance, not title: producing posts and managing channels is out; analysing and moving metrics is in. Quantitative growth stays in scope. |
| Anything that cannot finish by **Fri 12 Mar 2027** | Japan study abroad starts 1 April. Immovable. |
| Anything on the removed-roles table above | Already rejected; do not re-add. |

Closed on 2026-08-21 under the social-media rule: **A2 Magnet Media** (Social Media Intern),
**A11 Claim Health** (Content Marketing Intern), **A20 Agentio** (Creator Partnerships Intern).
Kept as `closed` rather than deleted so a future sweep does not re-add them.

**Strategy added 2026-08-21** — see `PROFILE.md`. Economic consulting (C72–C75) is the standout:
it is the only category where an econ major with a stats minor is the *preferred* candidate rather
than an adjacent one.

## Statuses

| Status | Meaning |
|---|---|
| `live` | Verified open posting. Apply. |
| `unverified` | Real lead, posting page could not be opened from the sweep environment. URL is good — **open it yourself**. Scores provisional. |
| `conflict` | Good role, dates clash with the 12 March stop. Worth asking whether a shorter version exists. |
| `drafting` / `applied` / `interviewing` | Your pipeline. Edit by hand. |
| `monitor` | Nothing to apply to yet — dated opening or outreach target. |
| `blocked` | Gated on an unresolved prerequisite (visa, convenio, eligibility). |
| `closed` | Expired or rejected. Kept for history. |

## Maintenance

- **Re-verify every link monthly.** Postings expire fast; Tier A will rot quickest.
- **Confirm dates overlap a January start** before applying — the most common failure mode
  in aggregated listings is a role labeled "Spring" that actually runs Mar–Aug.
- **Update `Status`** by hand: `not started` → `drafting` → `applied` → `interviewing` → `closed`.
  Use `monitor` for Tier B/C rows with nothing to apply to yet, `blocked` where a
  prerequisite is unresolved.
- After the resume lands, all `~` Fit scores get recomputed and the tildes come off.
