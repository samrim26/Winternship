# Winternship

Off-cycle internship search — **Monday 4 January to Friday 12 March 2027** (10 weeks).

Hard stop: study abroad in Japan begins **1 April 2027**.

Sam Rimland · UT Austin, Class of 2028 · Economics, minor in Statistics & Data Science.

## Files

| File | What it is |
|---|---|
| [`PROFILE.md`](PROFILE.md) | Candidate context, constraints, work-authorization analysis, location feasibility, positioning angles, keyword bank, scoring rubric. **Read this first.** |
| [`jobs.md`](jobs.md) | The tracker. Every role, tiered by whether it's live, dated, or an outreach target. Source of truth. |
| [`dashboard.html`](dashboard.html) | Sortable, filterable dashboard plus the dated recruiting timeline. Published as a private Artifact. |
| [`CLAUDE.md`](CLAUDE.md) | Loads `PROFILE.md` automatically for any Claude Code session in this folder. |
| `resume/` | Resume goes here. Gitignored by default. |

## How it's organized

Two lists, both screened against the actual resume (realistic roles only, not reaches):

- **List 1 — Posted jobs.** Real postings in any allowed location or remote. `conflict` rows are
  realistic but end after the Apr 1 hard stop.
- **List 2 — Cold-email targets.** Austin and NYC only. No posting exists, but the resume gives a
  specific reason to email. Warm leads (FEVO, Ualett) first.

Music and live events are in scope. YC is not.

## Automation

A cloud routine runs twice daily (13:00 and 22:00 UTC). It checks every List 1 posting with
`check_links.py`, closes dead ones, adds realistic new roles to both lists, commits, and
republishes the dashboard Artifact.

## The three long-lead items

Each is one message that either unblocks a market or closes it. All were open as of the last sweep:

1. **UT Austin Texas Global** — will they sign a *convenio de prácticas*? Gates Madrid and Barcelona entirely. Ask about Japan in the same email.
2. **Australian Work and Holiday visa (subclass 462)** — US citizens qualify, but the allocation is capped near 2,500 a year and closes when hit. Not employer-sponsored, so it can be started before an offer exists.
3. **Japan** — Tokyo is open but unpaid-only (no US working-holiday agreement; ≤90 days on Temporary Visitor status). Worth pursuing precisely *because* of the April relocation. Israel is now closed — every program-mediated route needs 4+ months and cannot finish by 12 March.
