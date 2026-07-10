# Website Section Prompt Templates

Fill the brackets. Paste the same STYLE TOKENS block into every prompt of the set.

## Master template (any section)

```
Website [SECTION TYPE] section design, horizontal 16:9, full-width screenshot
of a single page section, high-end [industry] marketing site.

STYLE TOKENS: [paste the set's token block verbatim]

CONTENT:
Headline: "[exact headline, ≤ 8 words]"
Subheadline: "[exact subline, ≤ 15 words]" (omit if none)
Primary action: "[exact button label]" as a prominent [accent hex] button
Other visible text: [list every label/badge/stat exactly]
Visual: [describe the section's image/illustration/UI element]

COMPOSITION: [one of the variety options — see below]. Focal point: [the one
thing the eye should land on].

Clean modern web design, realistic proportions, consistent spacing,
professional SaaS-quality UI, large legible typography, no watermark,
no browser chrome, no lorem-ipsum walls, no duplicate buttons.
```

## Composition options (rotate — never repeat in adjacent sections)

- `centered statement: headline centered, elements stacked vertically, wide margins`
- `split left-text right-visual, 40/60`
- `split right-text left-visual, 40/60`
- `full-bleed background [photo/gradient/texture] with overlaid text bottom-left`
- `asymmetric: content in left third, oversized visual bleeding off the right edge`
- `horizontal row of [3] equal cards with generous gaps`
- `zigzag: two feature rows with alternating text/visual sides`
- `stat layout: one huge number dominating, small caption beneath`
- `single centered quote in display type, small attribution line`

## Per-section notes

**Hero** — pick a scale first:
- Oversized: `headline set gigantic across 80% of the width, one small CTA below, tiny nav hints at top`
- Balanced: `headline + subline + CTA left or centered, product screenshot as the visual`
- Minimal: `small refined centered headline, one CTA, vast negative space`
Include a slim top navigation bar (logo left, 3–4 links, one CTA) unless another section covers it.

**Logo strip / social proof** — `single quiet row of 5–6 grayscale company logos, small caption above: "[exact caption]"`. No buttons.

**Feature** — the product visual carries it: `large UI screenshot / abstract diagram / photo` per the token texture. One short headline, 2–3 bullet labels max, each ≤ 4 words.

**How it works** — `three numbered steps in a horizontal row, each with a small icon, 3-word title, one short line`. Numbers big, text small.

**Testimonial** — `one quote only`: `quote in large display type, "[exact quote, ≤ 20 words]", avatar + name + role small beneath`. Never a 3-card testimonial grid unless the user asks.

**Pricing** — `[2–3] pricing cards in a row, middle card visually emphasized with the accent, each card: plan name, large price "[$X/mo]", 4 short feature lines, one button "[label]"`. Emphasized card gets the ONLY accent-filled button.

**FAQ** — `vertical accordion list of [5] question rows, first row expanded showing one short answer line, chevron icons`.

**Final CTA** — often inverted: `full-width band in [accent or dark hex], centered headline "[exact]", one high-contrast button "[exact]"`. Nothing else competes.

**Footer** — `slim footer: logo left, [3] link columns with 4 short labels each, legal line at bottom, muted text on [hex]`. Low contrast, quiet.

## Regeneration fixes

| Symptom | Add to prompt |
|---|---|
| Garbled text | shorten copy, list every word explicitly, "text sharp and legible" |
| Palette drift | move hex codes earlier, add "strictly limited palette: [hexes] only" |
| Section looks like a full page | "single page section only, cropped as one full-width band" |
| Three competing buttons | "exactly one button, labeled [X]" |
| Same layout as previous section | swap the COMPOSITION line for an unused option |
| Cramped / cluttered | "generous whitespace, airy spacing, fewer elements" |
