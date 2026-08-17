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

Roles sit in one of three tiers:

- **Tier A** — live now, applyable today.
- **Tier B** — opens on a known date. Monitor it.
- **Tier C** — no posting exists. Direct-outreach targets.

For a January start at a startup, **Tier C is the primary route, not the fallback.** Most off-cycle
roles get posted in January through March 2027 — at or after the intended start date. Cold outreach
in October beats a job board in February.

Fit scores marked `~` are provisional, estimated from the profile alone. They get recomputed against
real qualifications once the resume is uploaded.

## Automation

A cloud routine sweeps the job boards **daily at 09:00 ET**, commits new roles into `jobs.md` and
`dashboard.html`, and pushes. See *Automated monitoring* and *Sweep agent network access* in
[`jobs.md`](jobs.md) — the sweep environment blocks most job boards, so unverifiable leads are
recorded as `unverified` with their real URL rather than discarded.

## The three long-lead items

Each is one message that either unblocks a market or closes it. All were open as of the last sweep:

1. **UT Austin Texas Global** — will they sign a *convenio de prácticas*? Gates Madrid and Barcelona entirely. Ask about Japan in the same email.
2. **Australian Work and Holiday visa (subclass 462)** — US citizens qualify, but the allocation is capped near 2,500 a year and closes when hit. Not employer-sponsored, so it can be started before an offer exists.
3. **Japan** — Tokyo is open but unpaid-only (no US working-holiday agreement; ≤90 days on Temporary Visitor status). Worth pursuing precisely *because* of the April relocation. Israel is now closed — every program-mediated route needs 4+ months and cannot finish by 12 March.
