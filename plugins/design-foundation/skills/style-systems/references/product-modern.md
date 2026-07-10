# Product Modern

Clean contemporary product/app UI: neutral surfaces, one confident accent, strict 8pt grid, crisp components, dashboards that are dense but airy. The design disappears behind the product — precision and restraint signal quality.

Use for: SaaS apps, B2B dashboards, admin panels, settings-heavy tools, developer consoles, startup landing-plus-app combos.

## Palette philosophy

Neutral-first. 90% of every screen is a disciplined gray ramp with a barely-perceptible cool or warm cast (pick one cast and keep it). ONE accent, confident but not loud, reserved for primary actions, active states, and focus. Semantic colors (success/warning/danger) exist but appear only when meaning demands. If a screenshot in grayscale still communicates its hierarchy, the palette is right.

Example tokens (light, cool-cast, blue accent):

```css
:root {
  --bg: #F8F9FB;            /* app canvas */
  --surface: #FFFFFF;       /* cards, panels */
  --surface-2: #F1F3F6;     /* hovers, wells, table stripes */
  --text: #16181D;
  --text-secondary: #5A6170;
  --text-tertiary: #8A91A0; /* placeholders, meta */
  --border: #E3E6EB;        /* default hairline */
  --border-strong: #C9CED8; /* inputs at rest */
  --accent: #3D63F5;        /* or #16A34A green, #7C3AED violet, #0D9488 teal — ONE */
  --accent-hover: #2F51D6;
  --accent-soft: #EBF0FE;   /* selected rows, active nav */
  --success: #17995F; --warning: #B45309; --danger: #DC2F42;
  --success-soft: #E4F6EE; --warning-soft: #FCF1E3; --danger-soft: #FDECEE;
}
```

Dark variant: `--bg #101216`, `--surface #16181D`, `--surface-2 #1D2026`, `--text #EDEFF3`, `--border #262A32`; lighten the accent one step (`#5B7CFF`). Elevation in dark mode = lighter surface, not bigger shadow.

## Typography

One UI family, one optional mono for data/code. No display face — hierarchy comes from size, weight, and color steps.

Pairings (pick one):
- **Inter + "JetBrains Mono"** — the default; enable `font-feature-settings: "cv11", "ss01"` if desired.
- **"Geist"-style + "Geist Mono"-style** (e.g. Inter Tight + IBM Plex Mono) — slightly more contemporary.
- **"IBM Plex Sans" + "IBM Plex Mono"** — more enterprise.

Scale — compact, small steps; product UI lives at 13–14px:

```
--text-xs: 0.75rem     /* 12px — meta, table headers (500, uppercase optional at +0.04em) */
--text-sm: 0.8125rem   /* 13px — dense UI default: tables, sidebars */
--text-base: 0.875rem  /* 14px — forms, body in app, line-height 1.5 */
--text-md: 1rem        /* 16px — card titles (600) */
--text-lg: 1.25rem     /* 20px — page titles (600) */
--text-xl: 1.5rem      /* 24px — dashboard headline numbers */
--text-2xl: 2rem       /* rare: empty states, marketing bleed-through */
```

Rules:
- Weights: 400 body, 500 emphasized/labels, 600 headings. Never 700+ in app UI.
- Hierarchy via the three text colors before reaching for size changes.
- All numeric data: `font-variant-numeric: tabular-nums`. Metrics/IDs/timestamps may use the mono at sm.
- Marketing pages of the same product may scale headlines up (clamp to ~4rem) but keep the same family and accent.

## Spacing, radius, shadow

- **8pt grid, strictly.** All spacing ∈ {4, 8, 12, 16, 24, 32, 40, 48, 64}px. 4px only within compact components.
- Component metrics: buttons/inputs 32px (compact) or 36–40px (default) tall; table rows 40–44px; sidebar 240–260px; card padding 16–24px; page gutter 24–32px.
- Radius: `--radius-sm: 6px` (buttons, inputs, tags) · `--radius-md: 8px` (cards, menus) · `--radius-lg: 12px` (modals, large panels) · full for avatars/status dots. Nothing else.
- Shadows — near-invisible; borders do most separation:

```css
--shadow-xs: 0 1px 2px rgba(16, 24, 40, 0.05);                                /* buttons, inputs */
--shadow-sm: 0 1px 3px rgba(16, 24, 40, 0.07), 0 1px 2px rgba(16, 24, 40, 0.05); /* cards (optional) */
--shadow-md: 0 4px 12px rgba(16, 24, 40, 0.10), 0 1px 3px rgba(16, 24, 40, 0.06); /* dropdowns, popovers */
--shadow-lg: 0 12px 32px rgba(16, 24, 40, 0.14), 0 2px 6px rgba(16, 24, 40, 0.06); /* modals */
```

- Elevation rule: static containers = border, floating ephemerals (menus, popovers, modals) = border + shadow. Never shadow without border on floating elements.
- Gradients: effectively none in app UI. Marketing hero may use one very subtle neutral wash.

## Layout: dense but airy

- App shell: slim sidebar (icon+label rows, 32–36px tall, radius-sm hover with `--surface-2`, active = `--accent-soft` + accent text) + 48–56px top bar + content region on `--bg`.
- Content sits in `--surface` cards with `--border`, or directly on canvas with section dividers.
- Density comes from small type and tight row heights; airiness from consistent 24px gaps between blocks and real whitespace around groups. Never cram by shrinking gaps below grid values.
- Dashboards: KPI stat cards (label xs secondary → value xl 600 tabular → delta chip), chart cards with title + toolbar row, tables with sticky headers. Vary card spans; avoid uniform grids of identical cards.
- Every list/table needs designed empty, loading (skeleton), and error states.

## Component treatments

- **Buttons:** radius-sm, 500 weight, sm/base text. Primary: accent fill + shadow-xs, hover `--accent-hover`. Secondary: surface fill + `--border-strong` border. Ghost: text only, hover `--surface-2`. Destructive: danger equivalents.
- **Inputs:** surface fill, 1px `--border-strong`, radius-sm; focus: accent border + 3px `--accent-soft` ring (`box-shadow: 0 0 0 3px`). Labels: sm 500 above; help/error text xs below.
- **Tables:** xs 500 uppercase-optional headers in `--text-secondary`, 1px row borders, hover `--surface-2`, right-aligned tabular numerics, row actions revealed on hover.
- **Badges:** soft-fill pattern — `--*-soft` background + strong-color text, radius-sm or pill, xs 500.
- **Menus/popovers:** surface, border, shadow-md, 4px padding, radius-md; items 32px radius-sm.
- **Modals:** radius-lg, shadow-lg, 24px padding, max-width 480–640px, dimmed overlay `rgba(16,24,40,0.4)`.
- **Tabs:** underline style (2px accent on active) or segmented control on `--surface-2`.
- **Icons:** one stroke family (Lucide-style, 1.5px), 16px in dense UI, 20px in nav, `--text-secondary` default. Never emoji, never mixed families.
- **Charts:** accent as first series, then a muted categorical ramp; hairline gridlines (`--border`), xs axis labels, no 3D, no heavy gradient fills (≤8% opacity area fill allowed).

## Motion character

Quick, subtle, functional — motion confirms, never entertains.

- Durations: 100–150ms (hover/focus/press), 200ms (menus, tooltips), 250–300ms (modals, drawers). Nothing over 300ms in app UI.
- Easing: `cubic-bezier(0.16, 1, 0.3, 1)` (ease-out-expo feel) for entrances; `ease-out` for micro-states. No bounce, no spring overshoot.
- Signature moves: menus fade + 4px slide from trigger; modals fade + scale 0.98→1; skeleton shimmer while loading; count-up on dashboard numbers (once, ≤600ms); 150ms background-color transitions on rows/nav.
- Transition specific properties only (`background-color`, `border-color`, `box-shadow`, `transform`, `opacity`) — never `transition: all`. Respect `prefers-reduced-motion`.

## Do / Don't

Do:
- Keep 90% of pixels neutral; let the accent mark what matters.
- Snap every dimension to the 8pt grid; audit for stray 5px/18px values.
- Use borders for structure and shadows only for floating layers.
- Design empty/loading/error states for every data view.
- Keep app typography at 13–14px with tabular numbers.

Don't:
- No second decorative accent; no accent used for large background areas.
- No purple-gradient heroes, glassmorphism, glows, or gradient text.
- No radius outside {6, 8, 12, full}; no mixed radii on siblings.
- No heavy shadows on static cards; no shadow-only floating elements.
- No 700+ weights, no letter-spacing on body text, no proportional digits in tables.
- No uniform grids of identical cards on dashboards; vary spans by content priority.
- No motion longer than 300ms inside the app; no bounce easing.
