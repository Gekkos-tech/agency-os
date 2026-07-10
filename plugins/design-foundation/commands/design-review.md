---
description: Structured design review of the current build or a URL — hierarchy, consistency, taste, polish
argument-hint: [URL, path, or empty for the current project]
---

Run a design review on: $ARGUMENTS (default: the current project's built pages)

Delegate to the `design-reviewer` agent. Give it: the target (URL or local
dev server — start one if needed), the design handoff location (`design/`)
if present, and the style-system token source.

Require the report in this format:

1. **Verdict** — one paragraph: does this look designed or generated? Ship,
   polish, or rework?
2. **Fidelity** (only if a handoff exists) — deviations from tokens/sections
3. **Findings by severity** — each with location, what's wrong, why it
   matters, concrete fix (reference `style-systems` tokens, `interface-polish`
   rules, or `redesign` patterns as applicable)
4. **Quick wins** — fixes under ~15 minutes each

Then summarize the verdict and offer to apply the quick wins.
