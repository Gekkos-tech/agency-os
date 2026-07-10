# Image-to-Code Checklists

Copy these into working notes and fill them in. One analysis block per source image; one verification block per built section.

## Per-image analysis block (Phase 1)

```
IMAGE: [file] → SECTION: [name]

Layout
- Composition: [centered | split L/R | full-bleed bg | card row | zigzag | stat | quote]
- Split ratio / columns: [e.g. 5/7 of 12]
- Container: [boxed ~1200px | full-bleed]
- Alignment: [left | center]

Spacing
- Base unit guess: [4 | 8]px
- Section vertical padding: [~Npx top / ~Npx bottom]
- Card gap: [~Npx]   Card padding: [~Npx]
- Density: [airy | balanced | compact]

Palette (eyedropped, hex)
- bg: [#]  surface: [#]  text: [#]  text-muted: [#]
- accent: [#]  border: [#]  other: [#]

Type
- Distinct sizes visible: [N]
- Headline ≈ [N]× body; weight [light|regular|semibold|bold]; case [sentence|caps|lower]
- Letter-spacing: [tight | normal | wide]; line-height: [tight | normal | airy]
- Closest real font: [name]

Component inventory (exact counts)
- Nav: [logo + N links + N buttons]
- Buttons: [N primary (label: "..."), N secondary]
- Cards: [N, contents each: ...]
- Icons: [N, style: ...]
- Images/visuals: [N, aspect ~..., treatment: rounded/full-bleed/shadowed]
- Other: [badges, dividers, stats, avatars...]

Effects
- Radius: [px]  Shadow: [none | subtle | pronounced]
- Gradient: [where]  Borders: [where, color]
```

## Shared token block (write once after analyzing all images)

```
:root {
  --bg: [#]; --surface: [#]; --text: [#]; --text-muted: [#];
  --accent: [#]; --border: [#];
  --radius: [px]; --shadow: [value or none];
  --space-section: [px]; --space-card: [px]; --gap: [px];
  --font-display: [stack]; --font-body: [stack];
  /* type scale */ --fs-hero: [px]; --fs-h2: [px]; --fs-h3: [px]; --fs-body: [px]; --fs-small: [px];
}
```

## Per-section verification block (Phase 3)

```
SECTION: [name] vs IMAGE: [file]

[ ] Composition & split ratio match
[ ] Element count matches inventory (no missing, no invented)
[ ] Palette exact (spot-check 3 pixels: bg, accent, text)
[ ] Hierarchy ratios preserved (headline still ≈ [N]× body)
[ ] Spacing feel matches (section padding, gaps)
[ ] Visuals: correct aspect ratio and treatment
[ ] One clear primary action, styled like the comp
[ ] Real, focusable interactive elements; hover + focus-visible present
[ ] No cards-in-cards beyond what the image shows
Mismatches found: [list] → fixed: [y/n]
```

## Global pass (once per page)

```
[ ] All sections share the token block — no local color/radius overrides
[ ] Hero fully visible at 1440×800 including primary CTA
[ ] Section order matches the image set order
[ ] Mobile width: splits stack, rows wrap, nothing overflows
[ ] Alt text on images; headings in sane order (one h1)
[ ] Remaining deviations listed explicitly for the user: [list or "none"]
```
