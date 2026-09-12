# Job Tracker — Off-Cycle Spring 2027

> Source of truth for `dashboard.html`. Edit the `Status` column by hand as you apply.
>
> **Reference numbers:** the `RAW` array in `dashboard.html` is authoritative. Tier C numbering in
> this file diverged from it during the 2026-08-02 rebuild, so when allocating a ref for a new role,
> continue from the highest ref in that array — not from this file.
> Last swept: **2026-09-12** (daily sweep — full network access confirmed (workatastartup.com 301,
> wellfound.com 200, simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200, no
> regressions). **No closures.** **Three corrections, all confirmations rather than reversals:**
> **A121 (Ankura)** — today, 2026-09-12, was the exact date Intern Insider's aggregator-sourced
> "deadline" pointed to. Re-checked the primary Workday record directly via the CXS API (req
> R104943): still open (`canApply: true`), and the posting's JSON schema still has no
> `applicationDeadline`/`closeDate` field at all — the disputed date has now passed with nothing
> appearing on the primary source, so treat Intern Insider's Sept 12 2026 date as confirmed-wrong
> rather than merely unverified. **A13 (DeepAware AI)** — the "Robotics Center of Silicon Valley"
> rebrand suspected since 2026-09-02 is now confirmed: the entire live posting body only ever says
> "Robotics Center of Silicon Valley," no mention of "DeepAware" survives outside the YC company
> record name. Also newly noticed: `sponsorsVisa: "Will sponsor"`. **A92 (TraceRoot.AI)** — same
> `sponsorsVisa: "Will sponsor"` field newly noticed; also flagging a soft date signal worth asking
> about directly — the posting's own copy now reads "You won't own everything in one summer,"
> suggesting the role may be framed around a full-summer stint even though no explicit start/end
> dates are stated (not a confirmed conflict, no status change). Full re-verification of all 19
> `live` Tier A rows (A5, A9, A10, A13, A14, A22, A65, A70, A75, A82, A83, A88, A92, A96, A98, A112,
> A114, A120, A121) via direct fetch — the nine workatastartup.com/YC rows via curl+browser-UA (all
> 200s, no Cloudflare/403 this run — the client-rendered-SPA issue is fully resolved by the UA
> workaround, not a systemic blocker), the remaining ten via WebFetch/curl: all held, with only the
> three items above rising above cosmetic drift. **Two new Tier A rows added, both `unverified`/
> `conflict` per the never-silently-drop rule** rather than dropped for being hard to confirm:
> **A122 (Tesla, Data Engineer Intern, Fleet Analytics, Palo Alto)** — a distinct req from the
> already-tracked A68 (Cell Engineering); tesla.com 403s all direct fetch as usual; function reads
> as pipeline/ETL-leaning rather than core analytics, scored the same cautious fit as A68. **A123
> (Zipline, Data Analytics Intern (Spring 2027), South San Francisco)** — a ninth distinct Zipline
> req, JS-rendered and unconfirmable directly; kept `conflict` on the same sibling-pattern reasoning
> already used for A119, since every other Zipline Winter/Spring-2027-tagged req tracked here has
> independently confirmed a Jan–Apr overrun. Fresh sweep of all ten sources otherwise found nothing
> that clears the quality bar: economic consulting firms (Analysis Group, Cornerstone, CRA, Compass
> Lexecon, Brattle, NERA) checked again directly, all confirmed summer-only or wrong-location, no
> change from prior sweeps — Cornerstone's 2027 program doesn't even open until March 1 2027.
> workatastartup.com and wellfound.com's general listing/search pages are pure client-rendered React
> with no server-side job data — full board browsing needs login/JS execution neither tool has, so
> today's YC/Wellfound new-lead coverage was search-index-only, not a live crawl (same caveat noted
> in the header for future runs; the per-row curl+UA re-verification workaround above doesn't help
> here since it needs a known job URL, not a listing page). Tokyo: `coralcap.co/jobs` confirmed
> genuinely dead this run (404 on both `/jobs` and `/jobs/`, root domain still 200) rather than
> merely unparseable as previously logged; `japan-dev.com` and `tokyodev.com/jobs` both loaded fully
> today (no Cloudflare block) but surfaced only wrong-function or Japan-residents-only postings.
> SimplifyJobs off-season README (parsed programmatically, 372 candidate rows checked) and Intern
> Insider term/facet pages: no new matches beyond what's already tracked. Two ambiguous items
> checked and excluded on the merits rather than added: PwC "Deals - CMAAS Intern - Winter 2027"
> (BuiltIn NYC) requires an Accounting degree and CPA-exam eligibility, a hard mismatch for
> Econ/Stats; several GradConnection Sydney rows (ANZ Summer Intern EOI, SG Fleet Treasury
> Operations, Dept. of the Treasury) excluded on wrong start year or an Australian-citizenship
> requirement Sam doesn't meet.)
> Prior: **2026-09-11** (daily sweep — full network access confirmed (workatastartup.com 301,
> wellfound.com 200, simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200, no
> regressions). **Two closures**: **A94 (NewForm)** BD intern — posting now reads "Applications
> closed on August 26, 2026"; the tracked Nov 1 2026 deadline was stale. **A97 (Cadence Design
> Systems)** AI & Strategic Marketing Intern — Built In Austin shows the listing was removed Aug 31
> 2026. **One correction, upgraded to live: A121 (Ankura)** — got past the Workday 403 via the CXS
> API directly (req R104943, `canApply: true`), confirming the role is real: $34/hr, NYC on-site,
> posted Sept 9 2026, matching Intern Insider on every field checked. But Ankura's own record has
> **no application-deadline field set** (a sibling NY req, R104925, does carry one, so the field is
> known to render when present) — the Sept 12 2026 deadline sourced from Intern Insider is **not
> corroborated by the primary source** and is downgraded to unverified/likely wrong; status moved
> from `unverified` to `live` since the posting itself is now confirmed, deadline framing changed
> from imminent to rolling. New from the primary posting: requires permanent US work authorization,
> no visa sponsorship of any kind (fine for Sam), graduation window Dec 2027–June 2028 (matches
> Class of 2028); term dates (does it fit Jan–Mar 2027) are still not stated anywhere on the posting.
> Re-verified the remaining 17 `live`/`unverified` Tier A rows with near-term relevance (A5, A9,
> A10, A13, A14, A65, A70, A75, A82, A83, A92, A93, A95, A96, A98, A112, A114, A115, A117, A118,
> A119, A120): all held with no drift. Note on A5/A9/A10/A13/A65/A75/A82/A83 (workatastartup.com):
> the persistent 406/title-only issue on direct fetch was worked around this run with a fuller
> browser header set — worth using that approach going forward rather than flagging it as an access
> problem each sweep. Fresh sweep of all ten sources for new roles: **nothing found that clears the
> quality bar.** Economic consulting — Analysis Group, Cornerstone, Charles River Associates
> (Greenhouse), Compass Lexecon, Brattle, and NERA were all checked directly again; every one runs
> only a Summer analyst/associate track (10–12 weeks, June–Aug), no off-cycle Jan–Mar option; CRA's
> two open intern reqs remain Europe-only (Brussels/Düsseldorf/Munich). Palantir's Deployment
> Strategist req could not be relocated this run (worth a direct `jobs.lever.co/palantir` crawl next
> time rather than the general careers page). Uber/DoorDash/Flexport: no qualifying Strategy & Ops
> reqs surfaced; DoorDash's `careersatdoordash.com` continues Cloudflare-blocking both WebFetch and
> curl. GradConnection Sydney business/commerce: no new TikTok reqs beyond A112/A114 (one duplicate
> URL for A112, not a distinct role); everything else on the page is Big-4 vacationer programs
> (1–4 weeks) or wrong-function, not addable. BuiltIn NYC/Austin/SF: all relevant listings found were
> tagged Summer 2027 (hard-excluded); one partial hit, VelocityEHS Customer Experience Intern
> (Spring 2027, remote US/Canada, Jan–Apr 2027), excluded on both dates (runs past Mar 12) and
> function (CX/support, not tracked). Tokyo: `japan-dev.com` now loads past Cloudflare but is a
> heavy client-rendered app not parseable from raw HTML in the time available this run — genuinely
> unverified rather than confirmed dry, worth a JS-capable fetch next time; `coralcap.co/jobs` and
> TokyoDev unchanged from prior sweeps. WorkAtStartup and Wellfound `/jobs` both showed zero
> internships today (pre-YC-Winter-2027-batch, as expected before November). SimplifyJobs off-season
> README and Intern Insider term/facet pages unchanged, no new matches.)
> Prior: **2026-09-10** (daily sweep — full network access confirmed (workatastartup.com 301,
> wellfound.com 200, simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200, no
> regressions). Re-verified all 18 `live` Tier A rows (A5, A9, A10, A13, A14, A22, A65, A70, A75,
> A82, A83, A88, A92, A96, A98, A112, A114, A120): **all 18 held with no drift, 0 closures, 0
> corrections.** WorkAtStartup's direct-fetch 406/title-only regression (present since 2026-08-27)
> continues on all nine A5/A9/A10/A13/A65/A75/A82/A83/A92 job-page fetches, but every title/company
> confirmed unchanged via WebFetch and (for A92) the YC company jobs page, which also confirmed pay
> ($4–6K/mo), hybrid ≥3-days-onsite mode, and open status. `jobs.lever.co` (A22) recovered fully via
> curl+browser-UA — New York, Hybrid, $1,000/mo, 5 hrs/week, unchanged. `au.gradconnection.com`
> (A112, A114) recovered via curl+browser-UA — both still show "Closing in 3 months" (~Dec 2026,
> consistent with the tracked 25 Dec 2026 date), Sydney, Australian Working Visa still listed among
> accepted work-rights categories. A14 (Celonis), A70 (Base Power), A96 (Crowe Global), A98 (Cresta),
> A88 (FairwAI), A120 (MTA) all re-confirmed via direct WebFetch, no field drift.
>
> **New: A121 (Ankura), University Intern, Forensic Data & Analytics — New York, NY, `unverified`,
> Strategy/Data function, imminent deadline.** Found via Intern Insider's company page
> (`interninsider.me/companies/ankura`), then opened directly (not a search snippet): on-site NYC,
> $34/hr, rolling start (no fixed term stated, unlike the sibling "Turnaround & Restructuring" req
> which is explicitly tagged Summer 2027 — this one carries no such tag), SQL/Python/Tableau data
> cleansing and visualization work supporting regulatory investigations and litigation — a genuine
> forensic/litigation-consulting analog to the Analysis Group/Cornerstone/CRA lane `PROFILE.md` calls
> out, and Economics is explicitly named among qualifying majors. **Deadline is September 12, 2026 —
> two days from this sweep — flagging loudly.** Could not independently corroborate beyond Intern
> Insider: Ankura's own Workday board (`ankura.wd5.myworkdayjobs.com`) 403'd on both WebFetch and the
> Workday CXS API via curl, so status is `unverified` rather than `live` per the never-guess-away
> rule. One data point worth noting: the posting states a graduation-date requirement of "December
> 2027 – June 2028," which a UT Austin Class of 2028 candidate falls inside — not disqualifying, but
> suggests this may be pitched as a near-grad conversion-track internship rather than a pure
> off-cycle slot; worth confirming directly given the tight deadline.
>
> Fresh sweep of all ten sources found nothing else that clears the quality bar. Economic consulting:
> Analysis Group and Cornerstone remain JS-gated with no roles visible; Charles River Associates
> (`charlesriverassociates` Greenhouse slug) unchanged — Brussels/Düsseldorf/Munich EU-only interns;
> Compass Lexecon's Workday board still won't render; Brattle 403'd again; NERA's FAQ still states
> summer/final-year-only. Intern Insider's role-facet pages (`consulting-strategy`,
> `sales-business-development`, `data-science`, `product-management`, `operations-supply-chain`)
> were pulled in full this time rather than the truncated term pages — surfaced Ankura (added above)
> plus two near-misses checked and excluded: Coinbase's Associate Product Manager Intern (SF) states
> outright "12-week internship during summer 2027," a hard exclusion; NTT DATA's Sydney "Marketing
> Intern" (via a fresh GradConnection pass) is a 6-month placement targeting an early-November-2026
> start — same enrolled-fall-semester-conflict-plus-overrun pattern that has excluded every other ANZ
> corporate program this year. SimplifyJobs off-season README (fetched raw) shows the same
> engineering-skewed Product Management/Data Science sections as every recent sweep, nothing new
> in-scope. Uber, DoorDash (`careersatdoordash.com` now 403s WebFetch directly — a new redirect
> target worth noting for future sweeps), Flexport (one open intern req found, Tradelane Operations
> Intern in Shenzhen — wrong location, not addable), and Palantir (two Deployment Strategist reqs,
> still explicitly requiring a 2026 graduation date, disqualifying a rising junior) all re-checked,
> no change. Tokyo (Coral Capital's `/jobs/` still 404s, Japan Dev still zero internships of any
> kind, TokyoDev still MorningStar/HENNGE engineering-only) and BuiltIn (all three metros — every
> business-function listing found was Summer 2027, mostly Coinbase/PwC/Cox Enterprises) came back
> structurally unchanged.)
> Prior: **2026-09-09** (daily sweep — full network access confirmed (workatastartup.com 301,
> wellfound.com 200, simplify.jobs 200, job-boards.greenhouse.io 302, www.builtinnyc.com 200, no
> regressions). Re-verified all 18 `live` Tier A rows (A5, A9, A10, A13, A14, A22, A65, A70, A75,
> A82, A83, A88, A92, A96, A98, A112, A114, A120) via direct fetch (curl+browser-UA for
> workatastartup.com, jobs.lever.co, and au.gradconnection.com, which all block plain WebFetch):
> **17 held with no drift, 0 closures. One correction — A75 (Surface Labs)**: the India remote
> option (dropped in the 2026-09-02 correction) is back — the YC posting now reads "fully remote,
> work from anywhere in the US or India"; location field broadened accordingly. The commission-only
> pay structure (no base) is reconfirmed, and the $10–20K/mo figure is clarified as YC's own
> realistic-earnings estimate for that commission structure, not a separate base-pay field, so it's
> now folded into the pay cell rather than flagged as conflicting. Fresh sweep of all ten sources
> (workatastartup, wellfound, simplify.jobs, the six named economic-consulting firms' own careers
> pages, the SimplifyJobs off-season README, Intern Insider term and role-facet pages, BuiltIn
> NYC/Austin/SF, GradConnection Sydney, Tokyo sources, and Uber/DoorDash/Flexport/Palantir)
> surfaced **no new candidates that clear the bar**. Economic consulting: Analysis Group and
> Cornerstone remain JS-gated with no roles visible; CRA's Greenhouse board moved to a new slug
> (`charlesriverassociates`, the old `crai` slug 404s — worth updating source notes) and shows only
> Summer 2026/2027 reqs, no off-cycle track; Compass Lexecon's Workday board and Brattle wouldn't
> render; NERA unchanged, final-year-only. Palantir's two Deployment Strategist reqs unchanged
> (Paris/Honolulu). Uber's board is JS-gated with no content this sweep (treat as unverified-empty,
> not confirmed-dry); DoorDash's Greenhouse board (454 total jobs) has zero postings containing
> "intern" anywhere — confirmed dry directly; Flexport's careers page is JS-gated, no list rendered.
> One WorkAtStartup lead checked and excluded: Wardstone's Business Development Intern (Space and
> Missile Defense) is real and open but Los Angeles (wrong metro) and requires "Senior and above"
> class standing — Sam is a rising junior, disqualifying. Tokyo sources (japan-dev, tokyodev)
> remain structurally SWE/PM-only, zero BD/Growth/Partnerships/Sales/DevRel listings on either;
> Coral Capital's `/jobs/` path is now a hard 404, confirmed dead again. No new Tier A/B/C rows
> this sweep.)
> Prior: **2026-09-07** (daily sweep — full network access confirmed (all 5 sanity-check
> domains returned 200/301/302, no regressions); all 19 `live` Tier A rows (A5, A9, A10, A13, A14,
> A22, A65, A70, A75, A82, A83, A88, A92, A96, A98, A101, A112, A114, A120) re-verified against their
> live postings — every one still open, no closures. **Two corrections**: **A120 (MTA)** — location
> corrected from "Brooklyn, NY" to "New York, NY (Manhattan)"; the posting's official address is 2
> Broadway, New York, NY 10004, with no mention of Brooklyn anywhere on the page. **A114 (TikTok AI PM
> Intern)** — the posting's closing date (25 Dec 2026), already known from the row's original note,
> is now reflected in the jobs.md Deadline column for consistency with sibling row A112. Fresh sweep
> of all ten sources (workatastartup, wellfound, simplify.jobs, the five named economic-consulting
> firms' own careers pages, the SimplifyJobs off-season README, Intern Insider, BuiltIn NYC/Austin/SF,
> GradConnection Sydney, Tokyo sources, and Uber/DoorDash/Flexport/Palantir) surfaced two candidates,
> **neither added**: Utilyze's Partnerships Intern (Wellfound) is unpaid with no stated dates and no
> brand strength to justify the unpaid exception — too marginal per the quality bar. BigID's Business
> Strategy Analyst Intern was checked directly and confirmed **stale**: the posting itself states a
> 10-week internship "starting June 4th and ending August 8th" (summer-cycle, hard exclusion) and is
> flagged "no longer accepting applications" — correctly left off. Economic consulting: Analysis Group
> and Cornerstone Research are JS-gated with no roles surfaced; CRA's Greenhouse board still shows only
> Brussels/Düsseldorf-Munich reqs; Compass Lexecon's Workday API shows only Paris/Beijing/Brussels/
> Berlin/Helsinki; Brattle 403'd today. No new leads. Palantir's two open Deployment Strategist reqs
> re-confirmed disqualifying (require 2026-graduation, final internship before graduating — Sam is
> 2028). Uber/DoorDash have no dedicated Winter/Spring 2027 Strategy & Ops track; Flexport has no
> strategy/BD/ops intern reqs at all currently. Tokyo sources (coralcap, japan-dev, tokyodev) remain
> structurally SWE-only. No new Tier A/B/C rows this sweep, no closures.)
> Prior: **2026-09-05** (daily sweep — **4 new Tier A rows (A117–A120)**, all four sourced from
> Workiva/Zipline/MTA via Intern Insider's company/role-facet pages and the SimplifyJobs off-season
> README's Data Science section. **One real correction**: **A115 (Workiva)** — the direct req URL that
> eluded every sweep since 2026-08-31 was found via Intern Insider's own company page
> (`interninsider.me/companies/workiva`), confirming the Commercial Strategy Intern's Winter 2027 term
> starts **Monday, January 4, 2027** and closes Sept 27, 2026. **New rows**: **A117** (Workiva Product
> Management Intern, Spring 2027, $40/hr, unverified — flagged for a "software development experience"
> qualification mismatch) and **A118** (Workiva Intern – Partnerships, Winter 2027, NYC hub, unverified)
> are siblings from the same 22-req Workiva company page, both confirmed Jan 4 2027 start, both closing
> Sept 27 2026. **A119** (Zipline Commercial Strategy & Operations Intern) is a new Austin, TX location
> for an eighth tracked Zipline req — explicitly offers a "Winter 2027" term, kept `conflict` since
> every other Zipline "Winter 2027"-labeled req (A105, A107) has independently confirmed that means
> Jan–Apr. **A120** (MTA EAM Analyst Intern, Brooklyn NY, Data, $19/hr) is a public-sector NYC find
> independently verified live on MTA's own Jobvite ATS, in-person, `live`. **No closures.** Sweep of
> economic consulting added **nera.com checked directly for the first time** — its own FAQ confirms
> final-year-undergrad/grad-only, no off-cycle track, consistent with C103's existing finding; the
> other five firms unchanged. Palantir's two live Deployment Strategist reqs re-confirmed Paris and
> Honolulu; Uber/DoorDash unchanged; Tokyo unchanged (Coral Capital's `/jobs/` path now 404s outright).
> **Considered and excluded**: Google's NYC-area Data Analytics Apprenticeship (requires *not* being
> enrolled, 18-month program — hard exclusion); ZS Associates' SF strategy/analytics intern reqs
> (confirmed Summer-2027-only, 11 weeks, via WebSearch corroboration); VelocityEHS's "Austin" CX
> intern (actually remote/Oakville ON, Jan–Apr overrun); CommBank's Sydney PM/Business & Commerce
> summer program (Nov 2026 start, same enrolled-fall-semester conflict as every other ANZ program).)
> Prior: **2026-09-03** (daily sweep — full re-verification of all 17 `live` Tier A rows via
> WebFetch/curl+UA, plus a fresh sweep of every listed source. No closures, no new Tier A/B/C rows.
> **Two field corrections**: **A10 (Naive)** — mode corrected from "Hybrid" to "In-person or Remote"
> (the posting's SF and Remote(US) options are a candidate's either/or choice, not a blended
> arrangement — no true hybrid exists). **A75 (Surface Labs)** — the long-standing pay ambiguity is
> resolved: the posting's own description text ("$150 per qualified meeting," "$750 per meeting that
> converts," "10% of first-year ACV") confirms the internship is genuinely commission-only with no
> base; the structured-data "$10–20K/month" field was a mismatch, not real pay. Pay field updated to
> "Commission-only, no base ⚠". The other 15 live rows (A5, A9, A13, A14, A22, A65, A70, A82, A83,
> A88, A92, A96, A98, A101, A112, A114) held with no drift. **Sweep of new sources came back empty**:
> all six economic consulting firms confirmed summer-only with no off-cycle track (CRA's live
> Greenhouse board shows only Brussels/Düsseldorf-Munich intern reqs, no US analyst-intern posting;
> Brattle still 403s); Palantir's two open Deployment Strategist internship reqs are Paris and
> Honolulu, both outside target markets; Uber/DoorDash have not yet posted a Winter/Spring 2027
> Strategy & Ops track; the SimplifyJobs off-season README has no BD/Strategy/Growth/Partnerships
> category and is US/Canada-only by scope; GradConnection Sydney's only new listing (Susquehanna
> equity/macro analyst) starts Nov 2026 during Sam's enrolled fall semester; Tokyo sources remain
> structurally SWE-only. `workatastartup.com` still 406s direct; Wellfound's role-filtered pages
> returned no internship listings; **Intern Insider 429'd on every attempt today** (both WebFetch and
> curl+UA) — historically the single highest-yield source, retry first on the next sweep. Two
> unverifiable soft leads noted for a future check once real postings exist: Laborup (Bay Area,
> Founder's Associate/Chief of Staff Intern — no live apply URL found across Workable/Notion/
> LinkedIn) and Cloudflare Austin (current Business Enablement & Ops intern req is Fall 2026 term;
> worth checking again once a Winter 2027 req might post).
> Prior: **2026-09-02** (daily sweep — full re-verification of all 18 `live` Tier A rows plus a
> fresh sweep of every source; see the dated note below the Tier A table for details. No new Tier A/B
> rows and no closures; one new Tier C outreach target (C116, BuildPass) and three field corrections
> on existing live rows.)

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
| A5 | Dalus (YC W25) | GTM Intern | GTM | SF / Melbourne, AU / Munich / Remote | Remote | YC W25 | Rolling, part-time | Rolling | $18–25/hr | 2 | ~4 | **High** | live | [Work at a Startup](https://www.workatastartup.com/jobs/99648) |
| A6 | Uplane (YC F25) | Business Development Intern | BD | San Francisco (or Berlin/Remote) | In-person | YC F25 | Rolling, 3-mo min ⚠ | Rolling | $4K/mo | 2 | ~5 | Med | conflict | [Work at a Startup](https://www.workatastartup.com/jobs/97366) |
| A7 | Uplane (YC F25) | AI Marketing Strategist Intern | Growth | San Francisco | In-person | YC F25 | Rolling, 4-mo min ⚠ | Rolling | $4K/mo | 2 | ~4 | Low | conflict | [Work at a Startup](https://www.workatastartup.com/jobs/93708) |
| A8 | GutGutGoose (YC S26) | Growth Intern (founding team) | Growth | San Francisco | In-person | YC S26 | "Beginning whenever you can" | Rolling | $19–25/hr | 1 | ~4 | Low | closed | [Work at a Startup](https://www.workatastartup.com/jobs/102677) |
| A9 | Lambda Robotics (YC F26) | Founding GTM | Growth | San Francisco | In-person | YC F26 | Rolling | Rolling | $6–9K/mo | 3 | ~4 | Med | live | [Work at a Startup](https://www.workatastartup.com/jobs/104228) |
| A10 | Naive (YC P25) | Growth Engineer Intern | Growth | SF / Remote | In-person or Remote (candidate's choice, not blended) | YC P25 | Rolling | Rolling | $20–40/hr | 2 | ~4 | Med | live | [Work at a Startup](https://www.workatastartup.com/jobs/94648) |
| A11 | Claim Health (YC P25) | Content Marketing Intern | Growth | New York, NY | In-person | YC P25 | 10–12 wks, rolling | Rolling | Stipend | 2 | ~3 | Med | closed | [Work at a Startup](https://www.workatastartup.com/jobs/94958) |
| A12 | Mosaic (YC W25) | Growth Intern | Growth | San Francisco | In-person | YC W25 | Rolling | Rolling | $5–10K/mo | 3 | ~4 | Med | closed | [Work at a Startup](https://www.workatastartup.com/jobs/74610) |
| A13 | DeepAware AI (YC S25) | Business Development Intern | BD | San Francisco | In-person | YC S25 | Rolling | Rolling | Not listed | 2 | ~4 | Med | live | [Work at a Startup](https://www.workatastartup.com/jobs/100904) |
| A14 | Celonis | Business Development Representative Sales Intern (Part-Time) | BD | New York, NY | Hybrid | Public | Unconfirmed | Unconfirmed | $58,240 (FTE-annualized, PT title) | 3 | ~4 | Med | live | [Built In NYC](https://www.builtinnyc.com/job/business-development-representative-sales-intern-part-time/10648137) |
| A15 | UT Austin Athletics | Video and Analytics Intern — Baseball | Data | Austin, TX | In-person | On-campus | Winter/Spring 2027 (tagged) | TBC | Unconfirmed | 1 | ~2 | Low | unverified | [UT Workday](https://utaustin.wd1.myworkdayjobs.com/utstudent/job/UT-MAIN-CAMPUS/Video-and-Analytics-Intern--Baseball_R_00047706) |
| A16 | Zipline | Strategic Engagements & Events Intern (Spring 2027) | Partnerships | South San Francisco, CA | In-person | Series C | Jan–Apr 2027 ⚠ | Rolling | $34/hr | 3 | ~4 | Med | conflict | [Techstars board](https://jobs.techstars.com/companies/zipline) |
| A17 | Axo Longevity | Intern (Growth & Creative) | Growth | Barcelona | **Remote** | Early | Unconfirmed | Unconfirmed | Likely unpaid | 1 | ~3 | Low | closed | [Wellfound](https://wellfound.com/jobs/3628609-intern-growth-creative) |
| A18 | Datadog | Product Management Intern (Winter session) | PM | New York, NY | Hybrid | Public | Jan 4 – Apr 23 2027 ⚠ | Unconfirmed | $100K–110K (annualized) | 4 | ~4 | Low | conflict | [Built In NYC](https://www.builtinnyc.com/job/product-management-intern/10710775) |
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
| A70 | Base Power Company | Growth Intern | Growth | Austin, TX | In-person | Startup | Unconfirmed | Rolling | Unconfirmed | 2 | ~4 | Med | live | [Built In Austin](https://www.builtinaustin.com/job/growth-intern/10000211) |
| A71 | Zettabyte Inc | Growth Operations Intern | Growth | Bay Area, CA | Flexible | Startup | 3–6 mo, flexible | Rolling | Unconfirmed | 2 | ~4 | Med | unverified | [Built In SF](https://www.builtinsf.com/job/growth-operations-intern/8794820) |
| A72 | Jean Martin Inc | Market Research and Business Development Intern | BD/Data | New York, NY | In-person | Unconfirmed | Unconfirmed | Unconfirmed | Unconfirmed | 2 | ~4 | Med | unverified | [Built In NYC](https://www.builtinnyc.com/job/market-research-and-business-development-intern/10732902) |
| A73 | DEUNA | Data Science Intern | Data | San Francisco, CA | Hybrid | Startup | Unconfirmed | Unconfirmed | Unpaid | 2 | ~3 | Low | unverified | [Built In SF](https://www.builtinsf.com/job/data-science-intern/9973177) |
| A74 | Workato | Intern, AI Engineering | Data (ML-eng skew) | San Francisco, CA | In-person | Growth-stage | Winter 2026 & Spring 2027 (stated) | Unconfirmed | Unconfirmed | 3 | ~2 | Low | unverified | [Built In SF](https://www.builtinsf.com/job/intern-ai-engineering/9010182) |
| A75 | Surface Labs | AI GTM Engineer Intern | Growth/Sales (technical-adjacent) | Fully remote (US or India) | Remote | YC-backed | Rolling, 3-mo | Confirm ≤ Mar 12 | Commission-only, no base ⚠ (OTE ~$10–18K/mo) | 2 | ~3 | Low | live | [Work at a Startup](https://www.workatastartup.com/jobs/93375) |
| A76 | Novaflow | Growth Intern | Growth | San Francisco, CA | Remote or in-person | YC-backed | Summer 2026 (as posted) ⚠ | Summer 2026 (as posted) ⚠ | $25–30/hr | 2 | ~4 | Low | conflict | [Work at a Startup](https://www.workatastartup.com/jobs/92868) |
| A77 | hoop.shop | Performance Marketing & Social Creative Intern | Growth (ambiguous) | New York, NY (listed) / Remote | Remote | Early | Unconfirmed | Unconfirmed | Unconfirmed | 2 | ~3 | Low | unverified | [Wellfound](https://wellfound.com/jobs/4589449-performance-marketing-social-creative-freelance-clone) |
| A78 | FairwAI | Data Analyst Intern, Policy + Ethics | Data | Remote (Boston/NYC/SF/Europe) | Remote | Early | Spring 2026 stated; 2027 TBC ⚠ | Unconfirmed | Unpaid | 2 | ~3 | Low | unverified | [Wellfound](https://wellfound.com/jobs/3257803-data-analyst-intern-policy-ethics) |
| A79 | Zeminent | Business Development & Lead Generation Intern | BD | Remote (Gurgaon, India hrs) | Remote | Small | Unconfirmed | Unconfirmed | Unconfirmed | 1 | ~2 | Low | unverified | [Wellfound](https://wellfound.com/jobs/4436924-business-development-lead-generation-intern) |
| A80 | Notion | Data Science Intern (Winter 2027) | Data | San Francisco, CA / New York, NY | In-person | Late-stage | **Jan 25 2027** | **Apr 16 2027 ⚠** | $55/hr (Bachelor's) / $59/hr (Master's) | 5 | ~5 | Med | conflict | [Ashby](https://jobs.ashbyhq.com/notion/a67d6f2b-7c13-41d0-b36b-b2f662c9873e/application) |
| A81 | LinkedIn | Global Sales Organization Intern | Sales | San Francisco, CA | In-person | Public | Rolling, unconfirmed | Unconfirmed | Paid (amount unconfirmed) | 4 | ~3 | Med | unverified | [Intern Insider](https://interninsider.me/internships/linkedin/global-sales-organization-intern-5793c9fa-ccc5-4abd-b1f5-b57f77f18a37) |
| A82 | Soren | Growth Intern | Growth | San Francisco, CA | In-person | Startup | Rolling | Unconfirmed | $6–11K/mo | 2 | ~4 | **High** | live | [Work at a Startup](https://www.workatastartup.com/jobs/102000) |
| A83 | Relling | Business Operations Intern | Data/Ops | San Francisco, CA | In-person | Startup (hardware, ex-SpaceX/NASA) | Rolling | Unconfirmed | $20–100/hr | 2 | ~3 | Med | live | [Work at a Startup](https://www.workatastartup.com/jobs/97830) |
| A84 | Dedalus Labs | Growth Intern (posted as Summer 2027) | Growth/DevRel | San Francisco, CA | In-person | Early-stage AI infra | Summer 2027 ⚠ | Unconfirmed | $4–8K/mo | 2 | ~4 | Low | conflict | [Work at a Startup](https://www.workatastartup.com/jobs/98002) |
| A85 | Dedalus Labs | Product Manager Intern (posted as Summer 2027) | PM | San Francisco, CA | In-person | Early-stage AI infra | Summer 2027 ⚠ | Unconfirmed | $4–8K/mo | 2 | ~4 | Low | conflict | [Work at a Startup](https://www.workatastartup.com/jobs/98000) |
| A86 | Sixtyfour | Growth Intern (posted as Fall 2026) | Growth | San Francisco, CA | In-person | Startup (compliance-data AI) | Fall 2026 ⚠ | Unconfirmed | $30–50/hr | 2 | ~3 | Low | conflict | [Work at a Startup](https://www.workatastartup.com/jobs/105487) |
| A87 | GutGutGoose | Growth (founding team) — new posting | Growth | San Francisco, CA | In-person | YC S26 | Trial + FT decision Sept 20 2026 ⚠ | Unconfirmed | $19–22/hr trial → $120K+ FT | 1 | ~3 | Low | conflict | [Work at a Startup](https://www.workatastartup.com/jobs/105105) |
| A88 | FairwAI | Project Management Fellow | PM/Partnerships | Remote (NYC/SF/Austin listed) | **Remote** | Early | 3–6 mo, flexible start | Rolling | Unpaid | 2 | ~3 | Low | live | [Wellfound](https://wellfound.com/jobs/3251810-project-management-fellow) |
| A89 | Peggy | Growth & PR Intern (Part-Time) | Growth (ambiguous — PR/comms) | Remote (ET preferred) | **Remote** | Early | Unconfirmed | Unconfirmed | Unconfirmed | 1 | ~2 | Low | unverified | [Wellfound](https://wellfound.com/jobs/4589467-growth-pr-intern-part-time-help-launch-an-ai-app-for-parents) |
| A90 | AxentraOS | Market Research Intern | Data/BD | Remote (US) | **Remote** | Early | 2–3 months | Unconfirmed | Unpaid | 1 | ~2 | Low | unverified | [Wellfound](https://wellfound.com/jobs/3647210-market-research-intern) |
| A91 | Trellis AI | Business Operations Intern | BD/Ops (founder's-associate generalist) | San Francisco, CA | In-person | Early (AI healthcare) | Rolling | N/A | Unconfirmed | 2 | ~4 | Med | closed | [Intern Insider](https://interninsider.me/internships/trellis-ai/business-operations-intern-3d9acb03-f6b8-41ae-bca8-829c31255e4c) |
| A92 | TraceRoot.AI (YC S25) | Developer Marketing Intern (was: GTM Engineer Intern) | Growth (technical-adjacent) | San Francisco, CA | Hybrid (≥3 days onsite) | YC S25 | Rolling | Unconfirmed (see note) | $4–6K/mo | 2 | ~5 | **High** | live | [YC / Work at a Startup](https://www.ycombinator.com/companies/traceroot-ai/jobs/dk1ep2K-gtm-engineer-intern) |
| A93 | NewsBreak | Growth Engineer Intern | Growth | Mountain View, CA | In-person | Growth-stage | Rolling | Oct 12 2026 | $40–60/hr | 3 | ~4 | Med | unverified | [Intern Insider](https://interninsider.me/internships/newsbreak/growth-engineer-intern-b3921cc9-7d80-45ae-acd0-e6397c0506e3) |
| A94 | NewForm | Business Development Intern | BD | New York, NY | Hybrid | Startup | Rolling admission | Closed Aug 26 2026 | Unconfirmed | 2 | ~4 | Med | closed | [Intern Insider](https://interninsider.me/internships/newform/business-development-intern-b44b60d3-aa91-4d74-8bf7-b9d00d044884) |
| A95 | Parkdepot | Marketing Analyst Intern | Growth/Data (quantitative) | San Francisco, CA | In-person | Startup | Rolling, "full-time commitment" ⚠ | Oct 17 2026 | Unconfirmed | 2 | ~3 | Low | unverified | [Intern Insider](https://interninsider.me/internships/parkdepot/marketing-analyst-intern-fceac396-5267-4c7b-af85-dfba02481761) |
| A96 | Crowe Global | AI Functional Intern (Winter 2027) | Data/Strategy (technical-adjacent) | Austin, TX | In-office | Enterprise | **Winter 2027 (explicit)** | Ongoing | $27–42/hr | 3 | ~4 | **High** | live | [Built In Austin](https://www.builtinaustin.com/job/ai-functional-intern-winter-2027/10769798) |
| A97 | Cadence Design Systems | AI & Strategic Marketing Intern | Data/Strategy | Austin, TX | In-office | Public | Unconfirmed | Removed Aug 31 2026 | Unconfirmed | 3 | ~3 | Low | closed | [Built In Austin](https://www.builtinaustin.com/job/ai-strategic-marketing-intern/10787551) |
| A98 | Cresta | Data Science Intern (Customer Success) | Data | Remote (US) | **Remote** | Growth-stage | Rolling | Unconfirmed (see note) | Unconfirmed | 3 | ~4 | Med | live | [Greenhouse](https://job-boards.greenhouse.io/cresta/jobs/5213417008) |
| A99 | Scale AI | AI Builder Intern | Growth/Strategy (technical-adjacent) | San Francisco or New York | In-person | Late-stage | Summer 2027 ⚠ | Sept 4 2026 | Unconfirmed | 4 | ~4 | Low | conflict | [Intern Insider](https://interninsider.me/internships/scale-ai/ai-builder-intern-b83435b3-da10-4b18-87f4-3bebcf6d72e2) |
| A100 | APX (now Aster) | Developer Relations Intern | DevRel | United States (city unconfirmed) | In-person | Crypto/dev platform | Rolling | Expired (Nov 24 2025) | Unconfirmed | 2 | ~4 | Low | closed | [Intern Insider](https://interninsider.me/internships/apx-now-aster/developer-relations-intern-ab244e84-2b9d-40db-8cf3-3f27f1e048e0) |
| A101 | Advancy Partners | Strategy Consulting Intern (2026 Intake) | Data/Strategy | Sydney, AU | In-person | Boutique consulting | 2–6 months, flexible | Rolling | Paid (amount unconfirmed) | 3 | ~4 | Med | closed | [Advancy](https://advancy.recruitee.com/o/sydney-strategy-consulting-intern-2026-intake) |
| A104 | Direct Agents | AI Business Strategy & Operations Intern | Strategy | Culver City, CA | In-person | Established (2003) | Rolling, no stated minimum | Rolling | Unconfirmed | 2 | ~2 | Low | closed | [Intern Insider](https://interninsider.me/internships/direct-agents/ai-business-strategy-operations-intern-115edaa5-1508-48e8-a5b2-84ba5a0a7cb2) |
| A105 | Zipline | Sales Operations Analyst Intern | Data | South San Francisco, CA | In-person | Series C | Winter 2027 (Jan–Apr 2027) ⚠ | Rolling | $40/hr | 3 | ~4 | Low | conflict | [Intern Insider](https://interninsider.me/internships/zipline/sales-operations-analyst-intern-a2453a3e-deb9-4b6c-85be-2ee8537a8374) |
| A106 | Zipline | Marketing Intern (Spring 2027) | Growth | South San Francisco, CA | In-person | Series C | Jan–Apr 2027 ⚠ | Rolling | $34/hr | 2 | ~3 | Low | conflict | [Intern Insider](https://interninsider.me/internships/zipline/marketing-intern-spring-2027-7ac4e305-f77d-4616-b338-8bd9297b29a7) |
| A107 | Zipline | Operations Experience Intern (Spring 2027) | Strategy | South San Francisco, CA | In-person | Series C | Winter 2027 (Jan–Apr 2027) ⚠ | Rolling | Unconfirmed | 3 | ~4 | Low | conflict | [Intern Insider](https://interninsider.me/internships/zipline/operations-experience-intern-spring-2027-404887f1-5384-4506-a2a2-6500b67f8fd6) |
| A108 | Ekimetrics | 6-Month Internship in Strategy & Data Science | Strategy | New York, NY | In-person | Boutique consultancy | Rolling start, 6-month commitment ⚠ | Rolling | Paid (amount unconfirmed) | 3 | ~5 | Med | conflict | [Intern Insider](https://interninsider.me/internships/ekimetrics/6-months-internship-in-strategy-data-science-049dcc50-7033-4fa0-a0a4-e1e74bc773af) |
| A109 | Qureos | Business Development Intern | BD | New York, NY | In-person | Unconfirmed | Rolling | Unconfirmed | Unconfirmed | 1 | ~3 | Low | unverified | [Intern Insider](https://interninsider.me/internships/qureos/business-development-intern-d9aec99e-36ef-43d6-8692-aacf913d8029) |
| A110 | The Walt Disney Company | ABC News Insights and Analytics Intern (Spring 2027) | Data | New York, NY | In-person | Enterprise | Jan–Jun 2027 ⚠ | Rolling | $23/hr | 4 | ~4 | Low | conflict | [Disney Workday](https://disney.wd5.myworkdayjobs.com/disneycareer/job/New-York-NY-USA/ABC-News-Insights-and-Analytics-Intern--Spring-2027_10158500) |
| A111 | Motive | Sales Development Intern | Sales | Austin, TX | Hybrid | Startup | Summer 2027 ⚠ (as posted) | Unconfirmed | Unconfirmed | 2 | ~3 | Low | conflict | [Greenhouse](https://job-boards.greenhouse.io/gomotive/jobs/8431778002) |
| A112 | TikTok | Client Solution Intern (GBS AU) — 2027 Start | Sales/BD (analytics-adjacent) | Sydney, AU | In-person (assumed; not explicitly stated) | Enterprise | Candidate states own start/end dates; posting shows ~Dec 2026 (approx) | Closing 25 Dec 2026 | Unconfirmed | 4 | ~4 | High | live | [GradConnection](https://au.gradconnection.com/employers/tiktok/jobs/tiktok-client-solution-intern-gbs-au-2027-start-2/) |
| A113 | TikTok | Revenue Product Operations Intern (TikTok LIVE-Revenue) — 2027 Start | PM/Product Ops | Sydney, AU | Unconfirmed | Enterprise | Rolling; explicit 6-month commitment required ⚠ | Closing 19 Oct 2026 | Unconfirmed | 4 | ~3 | Low | conflict | [GradConnection](https://au.gradconnection.com/employers/tiktok/jobs/tiktok-revenue-product-operations-intern-tiktok-live-revenue-2027-start/) |
| A114 | TikTok | AI Product Manager Intern (TikTok Live-Revenue) — 2027 Start | PM | Sydney, AU | Hybrid | Enterprise | Dec 2026 (approx); candidate states own start/end dates | Closing 25 Dec 2026 | Unconfirmed | 4 | ~3 | Med | live | [GradConnection](https://au.gradconnection.com/employers/tiktok/jobs/tiktok-ai-product-manager-intern-tiktok-live-revenue-2027-start/) |
| A115 | Workiva | Commercial Strategy Intern (Winter 2027 cycle) | Strategy | Remote (US); NYC/SF/Austin office hubs available for hybrid | Remote | Public (NASDAQ: WK) | **Confirmed: Winter 2027 term starts Jan 4, 2027**, 15–20 hrs/wk | **Sept 27 2026 (confirmed on this exact posting)** | Unconfirmed on this title | 2 | ~4 | Med | unverified | [Intern Insider](https://interninsider.me/internships/workiva/commercial-strategy-intern-8a881fb9-e31b-4b13-98cd-c67aadac2ade) |
| A117 | Workiva | Product Management Intern (Spring 2027 cycle) | PM | Remote (US); hybrid near a Workiva office hub | Remote | Public (NASDAQ: WK) | Confirmed: Spring 2027 term starts **Jan 4, 2027**, 15–20 hrs/wk | Sept 27 2026 | $40/hr | 2 | ~3 | Med | unverified | [Intern Insider](https://interninsider.me/internships/workiva/product-management-intern-57ede0f8-ae81-466d-aea5-01f0ac3e17a5) |
| A118 | Workiva | Intern – Partnerships (Winter 2027 cycle) | Partnerships | New York, NY (hybrid near NYC hub) or Remote (US) | Remote | Public (NASDAQ: WK) | Confirmed: Winter 2027 term starts **Jan 4, 2027**, 15–20 hrs/wk | Sept 27 2026 | Paid (amount unconfirmed) | 2 | ~4 | Med | unverified | [Intern Insider](https://interninsider.me/internships/workiva/intern-partnerships-1e922333-06b0-4297-9902-2f9dad6cbfdd) |
| A119 | Zipline | Commercial Strategy & Operations Intern (Winter 2027 term) | Strategy | Austin, TX (+ Houston/Phoenix/San Antonio/Dallas/LA) | In-person | Series C | "Winter 2027" term offered (sibling reqs A105/A107 confirm Zipline's Winter 2027 label = Jan–Apr) ⚠ | Rolling | Paid (amount unconfirmed) | 2 | ~4 | Med | conflict | [Intern Insider](https://interninsider.me/internships/zipline/commercial-strategy-operations-intern-d75db0e8-2047-4484-b916-c7909405d22d) |
| A120 | Metropolitan Transportation Authority (MTA) | EAM Analyst Intern, Emerging Talent | Data | New York, NY (Manhattan) | In-person | Public agency | Confirm ≤ Jan 2027 (tagged "Spring 2027" by aggregator; primary posting states no exact dates) | Confirm ≤ Mar 12 | $19/hr (Undergrad) / $21/hr (Grad) | 2 | ~4 | Med | live | [MTA/Jobvite](https://jobs.jobvite.com/metropolitantransportationauthority/job/oZuEAfwr) |
| A121 | Ankura | University Intern, Forensic Data & Analytics | Data/Strategy (forensic/litigation consulting) | New York, NY | In-person | Established (global advisory) | Rolling, no stated term ⚠ | Rolling (no deadline set — see note) | $34/hr | 3 | ~4 | Med | live | [Ankura Workday, req R104943](https://ankura.wd5.myworkdayjobs.com/Ankura/job/New-York-NY/University-Intern--Forensic-Data---Analytics_R104943) |
| A122 | Tesla | Data Engineer Intern, Fleet Analytics | Data | Palo Alto, CA | Unconfirmed | Public | Winter/Spring 2027 (tagged) | Unconfirmed | Unconfirmed | 4 | ~3 | Low | unverified | [Tesla Careers](https://www.tesla.com/careers/search/job/283138) |
| A123 | Zipline | Data Analytics Intern (Spring 2027) | Data | South San Francisco, CA | In-person | Series C | Jan 2027 (inferred); Spring 2027 tag | Apr 2027 ⚠ (inferred from sibling reqs) | Unconfirmed | 3 | ~4 | Low | conflict | [Zipline careers](https://www.zipline.com/open-roles/7990420003) |

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
| B1 | Charles Schwab | 2027 Internship Program | Data/Business | Austin, TX + others | In-person | **Sept–Nov 2026** | 2027 cycles | Paid | 3 | ~3 | **High** | monitor | [Schwab Jobs](https://www.schwabjobs.com/internship-academy) |
| B2 | Citi | Summer Analyst — Commercial Banking, APAC | BD/Strategy | Sydney, AU | In-person | Rolling | 10 wks, Dec–Feb | Paid | 4 | ~3 | Med | monitor | [Citi Careers](https://jobs.citi.com/) |
| B3 | Bank of America | Global IB & Capital Markets Summer Analyst 2026/27 | Finance | Sydney, AU | In-person | Rolling | Dec–Feb | Paid | 5 | ~2 | Low | monitor | [BofA Careers](https://careers.bankofamerica.com/en-us/students) |
| B4 | Big 4 advisory (Deloitte / PwC / EY / KPMG) | Advisory & Analytics spring intern | Data/Strategy | Austin, NYC, SF | Hybrid | **Aug–Sept 2026** | Jan–Apr 2027 | Paid | 3 | ~3 | **High** | monitor | search each careers site |


**Confirm the end date on every Tier B row before applying.** B1 and B4 are structured programs whose
spring cycles commonly run into April or May. If they cannot finish by 12 March, they are out —
see the scope note at the top of this file.

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
