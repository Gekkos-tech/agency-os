---
description: Where does the project stand? Phase, gate status, blockers, who owes what, next step
argument-hint: [optional: project path if not the current directory]
---

Report the project status for: $ARGUMENTS (default: the current project)

1. Read `docs/project-state.md`. If it exists, verify it against reality with
   quick spot-checks (does the phase's key artifact actually exist — brief,
   concept, design/ handoff, code, QA report, live URL?). Fix discrepancies
   in the file first.
2. If no state file exists, load the `agency-workflow` skill, classify the
   phase from project signals, and CREATE `docs/project-state.md` from the
   template in its references — this command is the recovery path for
   projects started before state tracking existed.
3. Report to the user, compact:
   - **Phase + health** (on track / blocked / at risk, with the reason)
   - **Gate status** — what's passed, what's open in the current phase
   - **Blockers** with owners and age (flag anything older than 7 days)
   - **Client owes / we owe** — the two lists, with dates
   - **The single next step** — and offer to execute it now

Do not start any phase work in this command beyond the spot-checks — /status
reports; the workflow executes.
