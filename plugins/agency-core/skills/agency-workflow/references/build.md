# Phase 4 — BUILD

Goal: implement the handoff exactly. Plan before code; the handoff wins every
argument.

## Workflow (per increment)

1. **Gather context** — read the project's CLAUDE.md if present. Locate the
   design source: a `design/` handoff (images + tokens) is binding — layout,
   structure, colors, typography, spacing come from it exactly. Without a
   handoff, existing Tailwind config / CSS variables are the token source.
   Never patch blind.
2. **Restate the goal** in one sentence: what is being built, from which
   design source, and which quality rules apply.
3. **Present the plan** — concrete steps, files touched (and deliberately
   not touched), risks and open questions. For client work, stop for
   approval; in autonomous mode, state the plan and proceed.
4. **Implement** — preserve the handoff/tokens exactly; quality skills refine
   and verify, they never redesign:
   - From design images → `image-to-code` (deep analysis pass, per-section
     fidelity, hero visible on a 13" viewport)
   - Motion → `gsap-suite`; 3D → `threejs-webgl` / `react-three-fiber`
   - Code discipline → `karpathy-guidelines`; full deliverables →
     `complete-output`
   - Scope strict: no structure or design changes without an order.
5. **Close the increment** — list changed files, run the final-feel pass with
   `interface-polish`, and state in one sentence how the result was verified
   (dev-server check, screenshot compare against the section image, test run).

## Rules

- **Handoff drift is a bug.** If implementation reveals the handoff can't
  work (impossible layout, missing state), go back to DESIGN for that
  section — don't improvise silently.
- Build mobile behavior alongside desktop, not after.
- Real content beats placeholder content; where content is missing, use the
  brief's content inventory to request it early.

## Exit gate

- [ ] Every handoff section implemented; side-by-side check done
- [ ] Responsive at common breakpoints; no horizontal scroll
- [ ] Interactive states (hover/focus/active/disabled) exist everywhere
- [ ] No console errors; forms and links actually work
- [ ] Changed-files list reported per increment
