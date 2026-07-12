# docs/project-state.md — the project's single source of truth

The router maintains this file at the END of every phase step (and whenever
something material changes mid-phase: a blocker appears, the client delivers
content, scope shifts). Keep it under ~40 lines — it's a dashboard, not a log.
Write it in the working language of the team; keep the field labels as-is so
tooling and `/status` can rely on them.

## Template

```markdown
# Project State — {client / project}

**Phase:** {BRIEF | CONCEPT | DESIGN | BUILD | QA | LAUNCH | MAINTAIN}
**Updated:** {YYYY-MM-DD}
**Health:** {on track | blocked | at risk} — {one-line reason if not on track}

## Gate status (current phase)
- [x] {passed gate item}
- [ ] {open gate item}

## Blockers
- {blocker} — owner: {us | client}, since {date}

## Client owes us
- {content, approval, credentials…} — requested {date}, needed for {phase/step}

## We owe the client
- {deliverable} — promised for {date}

## Next step
{The single next action, concrete enough to start immediately.}

## Decisions log (append-only, one line each)
- {YYYY-MM-DD} — {decision, e.g. "style system: minimalist-editorial approved"}
```

## Rules

- **One next step**, not a list. If you can't name one, the phase gate will
  tell you what's missing.
- Blockers name an **owner**. A blocker without an owner never gets resolved.
- The decisions log is append-only — it exists so nobody relitigates the
  style system in week 4.
- On phase transitions, reset the gate-status section to the NEW phase's
  gates and update `Phase:`.
- `/status` reads this file and reports it; if reality and file disagree,
  fix the file first, then report.
