---
description: Assemble or verify the design handoff (tokens + section images + notes) that BUILD implements 1:1
argument-hint: [optional: path to design assets or "verify"]
---

Design handoff task: $ARGUMENTS

Load the `agency-workflow` skill (DESIGN phase reference) and:

1. **If design assets exist** (generated section images, supplied designs,
   a style guide): assemble the binding handoff structure —
   - `design/tokens.md` — palette hex, type scale, spacing, radius, shadows,
     motion rules (extract from the assets; do not invent)
   - `design/sections/` — reference images named `{page}-{nn}-{section}`
   - `design/notes.md` — breakpoints, interaction behavior, animation intent
2. **If the argument is "verify"**: audit the existing `design/` folder for
   completeness — could a developer who never saw the concept build the site
   from it alone? List gaps.
3. **If nothing exists yet**: state that DESIGN must run first and route to
   the `style-systems` + `imagegen-web` skills.

Close with the DESIGN exit-gate checklist status.
