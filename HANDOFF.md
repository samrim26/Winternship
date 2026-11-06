# Handoff — 2026-11-05

For the next Claude session. Read `CLAUDE.md` and `PROFILE.md` first, then this file.

## Standing rules (from Sam, all still in force)

- **Never send an email or submit an application.** Draft only. Sam sends and submits.
  Gmail: create drafts only. Applications: fill the form, stop before Submit.
- **Show each batch before acting** (drafts, form fills). "Run it by me first."
- **No YC companies** on either list. Apollo.io (YC W16) was offered as an exception and Sam
  hasn't answered.
- **List 1 = real internship postings only.** Allowed locations: NYC, SF/Bay Area, Austin, Tokyo,
  Australia, Madrid, Barcelona, or remote US. **List 2 = cold-email targets, Austin/NYC only.**
- **Window:** Jan 4 – Mar 12, 2027. Hard stop April 1. Don't mention Japan in cold emails.
- Be realistic: downgrade fit a notch. Never invent facts about Sam (no "big fan of…").
- Personal contact info (phone, address) lives only in gitignored `applications/`.

## Where things are

| What | Where |
|---|---|
| Board (live) | https://claude.ai/artifact/C7fZaovmBMKwAhEmrrAz9P, built from `dashboard.html` (RAW array, 19 fields per row) |
| Listings mirror | `jobs.md` (List 1 = P rows, List 2 = E rows). "Other channels" section documents every source and API |
| Cold emails, repo copy | `cold_emails.md`: all 77 (E3–E79), approved template, signature placeholder |
| Cold emails, send-ready | `applications/cold_emails_ready.md`: same emails with the full signature |
| Email generator | `applications/build_emails.py`: one table (hook, team, proof keys) produces both files. Edit the table and rerun; don't hand-edit the .md files |
| Application drafts | `applications/applications.md`: standard answers, work history, per-role answers |
| Sweep scripts | `sweeps/`: a16z, Consider boards, Getro, Workday CXS, ATS detail printer |
| Link checker | `SSL_CERT_FILE=/etc/ssl/cert.pem python3 check_links.py` |

A scheduled routine also pushes to `main` (liveness checks remove dead P rows, and it sometimes
adds E rows). **Always `git pull --rebase` before editing**, and renumber on collisions.

## Approved cold email template (2026-11-05)

Subject `Jan–Mar internship at {Company}`. Structure: intro (UT Austin econ junior, stats and data
science minor), then one company-specific line, then "free full-time in {city} Jan 4 – Mar 12, … intern on
your {team} team", then 1–2 proof lines with numbers, then "You wouldn't need to set up a program
for me… flexible on pay. Would you be open to a 10-minute call this week? If someone else is better
to ask…", then "I attached my resume", then the full signature. Austin version offers "a call or a coffee".

## Next tasks, in order

1. **Check connectors.** Run `/mcp`; Gmail should show as connected. Then `/chrome`, or have Sam
   relaunch with `claude --chrome`.
2. **Block sending.** List the Gmail tool names, then add a `permissions.deny` rule for the send
   tool in `.claude/settings.json` (use the `update-config` skill). Tell Sam the exact rule.
3. **Contact research for all 77 List 2 companies.** Find a named person matching each
   "Send to" line from team pages, LinkedIn and press. Work out the email pattern; mark guessed
   addresses. Don't probe SMTP. Store names and emails in `applications/` (gitignored), not the repo.
4. **Gmail drafts.** Fill in `[First name]`, attach the resume if the tool allows. Batches of
   15–20, shown to Sam first. Drafts only.
5. **Applications in Chrome.** Approved and still live: #3 PatientPoint (P4/P5), #4–5 Base
   Power (P2/P3), #6 MTA (P6–P8), #7 Kroll (P12). #2 SXSW and #8 Utilyze have closed.
   Fill each form and stop before Submit.
6. **Waiting on Sam:**
   - Approve or skip batch 2 (#18–27). **#18 Whitney is due Nov 9.**
   - P37–P59 have no drafts yet.
   - Decide on Apollo.io.
   - Confirm the LinkedIn note for Patrick at The Boring Company (P48, referral from Eyal Kauf), which was drafted in chat.

## Gotchas

- **Artifact publish refused** because the routine published since: republish the same file. If
  the local file is a superset, the second retry goes through.
- **Escaping in RAW strings:** `&` becomes `&amp;`, `'` becomes `&#39;`.
- **zsh:** doesn't word-split `$var`.
- **Python SSL:** needs `cafile=/etc/ssl/cert.pem`.
