# Phase 3 — DESIGN

Goal: a binding design source the BUILD phase can implement 1:1. Either a set
of design reference images per section, or a token-level style guide — ideally
both. This becomes the **handoff** and the single source of truth.

## Work

1. **Commit to one style system** — load `style-systems`; pick exactly one
   system from the concept's creative direction and never mix. Pull concrete
   tokens (palette, type scale, spacing, radius, shadows, motion character).
   Use `ui-ux-pro-max` for palette/font-pairing candidates and UX rules;
   use `brandkit` first if the client needs identity assets (logo, brand
   board) before screens can exist.
2. **Design the screens** — load `imagegen-web` (or `imagegen-mobile` for
   apps): one reference image per section/screen, all prompts carrying the
   same style-token block. Follow the concept's page narratives —
   sections in the images must match the narrative one-to-one.
3. **Assemble the handoff** — a `design/` folder in the project:
   - `design/tokens.md` (or tokens file) — palette hex, type scale, spacing,
     radius, shadows, motion rules
   - `design/sections/` — the reference images, named `{page}-{nn}-{section}`
   - `design/notes.md` — anything the images can't show (breakpoints,
     interaction behavior, animation intent)

## Rules

- The handoff is complete when a developer who never saw the concept could
  build the site from it.
- Client feedback loops happen HERE, on images — changing a generated image
  is cheap; changing built code is not.
- If the client supplies finished designs (Figma etc.), skip generation:
  extract tokens into `design/tokens.md` and treat the supplied files as the
  handoff.

## Exit gate

- [ ] One style system, token block written down
- [ ] Every page section has a reference image (or supplied design)
- [ ] `design/` folder complete: tokens, sections, notes
- [ ] Client approved the design — or user waived approval
