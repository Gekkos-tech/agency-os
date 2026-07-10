# Phase 5 — QA

Goal: verify the built site against the brief, the handoff, and web-quality
standards — before the client or the public sees it.

## Passes (in order)

1. **Functional** — load `webapp-testing` if installed: exercise every user
   task from the brief end-to-end (forms submit, reservation flows complete,
   navigation works, 404 handling). Test as a user, not as the author.
2. **Fidelity** — compare each page against the design handoff side by side.
   Deviations are either fixed or explicitly accepted and noted.
3. **Performance** — load `performance` and `core-web-vitals`: LCP, INP, CLS
   on the slowest realistic device; image formats/sizes; render-blocking
   assets; font loading.
4. **Accessibility** — load `accessibility`: keyboard path through every
   flow, contrast, focus visibility, alt texts, form labels, reduced-motion.
5. **Cross-cutting** — load `best-practices`: security headers, HTTPS,
   console errors, meta basics.
6. **Content** — spelling (in the client's language), real contact data,
   no lorem ipsum, no placeholder images.

## Rules

- Fix-and-retest: after any fix, rerun the pass that found the issue.
- Log results per pass in `docs/qa-report.md` — pass/fail + evidence. The
  report is a client-facing deliverable for agencies.
- If fidelity or feel is broadly below the bar (not isolated bugs), route
  back through `redesign` rather than patching one-off.

## Exit gate

- [ ] All brief user-tasks pass end-to-end
- [ ] Fidelity check done; deviations accepted in writing
- [ ] CWV within targets on mobile (LCP < 2.5s, INP < 200ms, CLS < 0.1)
- [ ] Keyboard + contrast + labels pass
- [ ] `docs/qa-report.md` written
