---
description: Run the full pre-launch gate — legal (DSGVO, Impressum, Cookie-Consent, BFSG) + technical launch checklist
argument-hint: [staging URL or project path]
---

Run the pre-launch gate on: $ARGUMENTS

Delegate to the `qa-auditor` agent with the `pre-launch-checklist` skill as
its rulebook. The agent must:

1. Work through section A (legal — DACH/EU) and section B (technical) of the
   checklist against the actual site/code, collecting evidence per item —
   no checkbox theater: verify third-party requests in the code, test the
   consent gate both ways, send a real test form submission where possible.
2. Produce `docs/launch-checklist.md` in the client's language with the
   GO / NO-GO result table.

Then report back: the verdict (GO / NO-GO), every legal blocker verbatim,
and the top technical items. Legal blockers are non-negotiable — if any
exist, state plainly that launch is not recommended until they are fixed.
