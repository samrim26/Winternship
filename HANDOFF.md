# Handoff — 2026-11-10

For the next Claude session. Read `CLAUDE.md` and `PROFILE.md` first, then this file.

## Standing rules (from Sam, all still in force)

- **Never send an email or submit an application.** Draft only. Sam sends and submits.
  Gmail: create drafts only. Applications: fill the form, stop before Submit.
- **Show each batch before acting** (drafts, form fills). "Run it by me first."
- **No YC companies** on either list. **Exception: Apollo.io (YC W16) is allowed** (Sam, 2026-11-10).
- **List 1 = real internship postings only.** Allowed locations: NYC, SF/Bay Area, Austin, Tokyo,
  Australia, Madrid, Barcelona, or remote US. **List 2 = cold-email targets, Austin/NYC only.**
- **Window:** Jan 4 – Mar 12, 2027. Hard stop April 1. Don't mention Japan in cold emails.
- Be realistic: downgrade fit a notch. Never invent facts about Sam (no "big fan of…").
- Personal contact info (phone, address) lives only in gitignored `applications/`.
- **No overlap (2026-11-10):** never cold-email a company Sam is applying to officially. That List 2 row gets status `skip` (E80 Hook, E88 Base Power).
- **Backup addresses + bounce check (Sam, 2026-11-10):** every cold email needs 1–2 backup addresses logged in `applications/contacts.md` before sending. ~15 min after each send, search Gmail for bounces (`from:mailer-daemon newer_than:1d`) and redraft bounced emails to the next backup.
- **Cold-email addresses:** no SMTP probing. Pattern-derived addresses are marked `(guess)` and used only with Sam's OK.
- **Say "coordinate" speakers, never "book".** Resume claims go in word for word (see `applications/applications.md`).
- **Sam picked these targets himself:** Hook and Duetti (NYC music). The VC batch (E82–E87) was added at his request.
- **Window rule (2026-11-09):** apply officially where the term has no fixed end or ends by **Apr 19, 2027** (Mar 25 + 25 days, Sam 2026-11-10); otherwise cold-email. Sam's exception: Base Power (5 roles filled 2026-11-09).

## Where things are

| What | Where |
|---|---|
| Board (live) | https://claude.ai/artifact/C7fZaovmBMKwAhEmrrAz9P, built from `dashboard.html` (RAW array, 19 fields per row) |
| Listings mirror | `jobs.md` (List 1 = P rows, List 2 = E rows). "Other channels" section documents every source and API |
| Cold emails, repo copy | `cold_emails.md`: all 94 (E3–E97, no E32), approved template, signature placeholder |
| Cold emails, send-ready | `applications/cold_emails_ready.md`: same emails with the full signature |
| Email generator | `applications/build_emails.py`: one table (hook, team, proof keys) produces both files. Edit the table and rerun; don't hand-edit the .md files |
| Application drafts | `applications/applications.md`: standard answers, work history, per-role answers |
| Resume (upload this) | `resume/Samuel_Rimland_Resume.pdf` (2026-11-09), text in `resume/resume.txt`. Gitignored. Claims must match it word for word: Epsilon Nu Tau = "coordinate venues and scheduling … with 10+ speakers" (never "book"); STIZ = "demonstration app", "private test" |
| Sweep scripts | `sweeps/`: a16z, Consider boards, Getro, Workday CXS, ATS detail printer |
| Link checker | `SSL_CERT_FILE=/etc/ssl/cert.pem python3 check_links.py` |

A scheduled routine also pushes to `main` (liveness checks remove dead P rows, and it sometimes
adds E rows). **Always `git pull --rebase` before editing**, and renumber on collisions.

## Approved cold email template (revised 2026-11-10)

Subject `Winter internship at {Company}`. ~100 words, plain language (research: short emails, simple wording,
one easy ask). Structure: "I'm Sam, an econ junior at UT Austin." + one company-specific line, then "I'm in Austin / I'll be
in {city} and free from early January through mid-March, and could spend that time helping your {team} team." + 1–2
short proof lines, then "No formal program needed, and I'm flexible on pay. Would you be open to a quick call (or coffee, Austin)?
If someone else is better to ask, I'd appreciate a pointer." then "Resume attached. Thanks!" and the full signature
(LinkedIn as https://www.linkedin.com/in/samuelrimland). No exact start/end dates in cold emails. Postings that run past
Apr 1: "I saw your spring X internship, which runs through April. Could a shorter version work?"

## Next tasks, in order

**START HERE (2026-11-09): `applications/BATCH_1.md`** (see its "Part B status" and "Window rule" sections: 6 forms filled awaiting Sam's Submit; E88–E97 cold emails added for postings that run past Apr 1, 9 drafted) — 10 cold-email drafts (Sam schedules 8 AM CST)
and 10 applications, prioritized, with step-by-step rules. Work history is now verbatim resume bullets
in `applications/applications.md`. Never Submit/Send/Schedule — Sam does.


1. ~~Check connectors.~~ Done 2026-11-05: Gmail connected. **Chrome tools not loaded**; Sam must
   relaunch with `claude --chrome` before tasks 3b and 5.
2. ~~Block sending.~~ Done: `.claude/settings.json` denies `mcp__claude_ai_Gmail__send_message`,
   `__reply`, `__forward` (verified: tools vanished from session). Only `create_draft` remains.
3. **Contact research, pass 1 done** → `applications/contacts.md`. 46/76 named (press, team pages),
   30 unnamed (mid-level roles only findable on LinkedIn). Email patterns: only 4 guessed so far;
   vendor data (LeadIQ/Prospeo/Mailmo) often contradicts itself.
   3b. With Chrome: fill the 30 gaps from LinkedIn, then patterns for all named contacts.
   List 2 is now **76**: E32 Austin Music Foundation dropped (suspended ops Sep 2023); E31 renamed
   Sonic Guild (ex-Black Fret, ED Bobby Garza). Emails regenerated.
4. **Gmail drafts.** Blocked on Sam: (a) unnamed contacts — wait for LinkedIn or use "Hi there"/
   founder? (b) guessed addresses OK for drafts? Fill in `[First name]`, attach the resume if the
   tool allows. Batches of 15–20, shown to Sam first. Drafts only.
4b. **New List 1 rows P60–P62** (from Sam's LinkedIn paste, 2026-11-05): Black Diamond Networks
   sales intern (High), Verkada SDR intern (Med), Matthews CRE brokerage (Low, likely unpaid). All
   need a "can I do Jan 4 – Mar 12?" check before applying.
4c. **VC batch (2026-11-09):** E80 Hook, E81 Duetti (Sam's picks, NYC music). VC cold targets E82 MUSIC,
   E83 Waverley, E84 Courtside (NYC); E85 Capital Factory, E86 Springdale, E87 Next Coast (Austin). Plus
   P64 HOF Capital (rolling VC intern, needs a Jan–Mar ask). VC odds are low except Capital Factory and
   Springdale; E84/E85/E87 need named contacts (LinkedIn, task 3b).
5. **Applications in Chrome.** Approved and still live: #3 PatientPoint (P4/P5), #4–5 Base
   Power (P2/P3), #6 MTA (P6–P8), #7 Kroll (P12). #2 SXSW and #8 Utilyze have closed.
   Fill each form and stop before Submit.
6. **Waiting on Sam:**
   - Approve or skip batch 2 (#19–27). #18 Whitney skipped (Sam, 2026-11-09).
   - P37–P59 have no drafts yet.
   - Apollo.io: allowed (2026-11-10). Check for a live posting (List 1) — remote/SF, not a cold-email city.
   - Confirm the LinkedIn note for Patrick at The Boring Company (P48, referral from Eyal Kauf), which was drafted in chat.

## Gotchas

- **Artifact publish refused** because the routine published since: republish the same file. If
  the local file is a superset, the second retry goes through.
- **Escaping in RAW strings:** `&` becomes `&amp;`, `'` becomes `&#39;`.
- **zsh:** doesn't word-split `$var`.
- **Python SSL:** needs `cafile=/etc/ssl/cert.pem`.
- **grep** is aliased to ugrep, which skips gitignored files (`applications/`, `resume/`). Use `/usr/bin/grep`.
- **git push hangs sometimes:** `GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=20 git push`. macOS has no `timeout`.
- **Gmail connector mangles links:** plain-text URLs in `create_draft` bodies show up as visible `https://www.google.com/url?q=...` text. Fix in the Gmail compose window before sending (replace the anchor's text/href with linkedin.com/in/samuelrimland), or send htmlBody with a proper <a>.
- **PDF text:** no pdftotext/pypdf. Resume text is already in `resume/resume.txt`.
- **~/.zshrc:** editing it was blocked. Sam changes his own PATH.

## Open questions for Sam (ask once, record answer here)

- ~~Email on forms~~ **Answered 2026-11-09: `samuelrimland@utexas.edu`.**
- ~~Resume study-abroad date~~ **Answered 2026-11-10: leave "Summer 2027" as is.**
- ~~Which Gmail account?~~ **Answered 2026-11-09: utexas (samuelrimland@utexas.edu); the Gmail connector drafts there.**
- ~~Apollo.io~~ **Answered 2026-11-10: yes, allowed.**
