# Minimalist Editorial

Warm monochrome, typographic contrast, flat bento grids, muted accents. The page reads like a well-set magazine: the typography IS the design. Nothing glows, nothing floats, nothing bounces.

Use for: editorial sites, portfolios, studios, publications, luxury brands, content-first marketing.

## Palette philosophy

Warm monochrome, not cold gray. Grays lean toward beige/cream (hue 30–50, low saturation). One near-black, one warm paper background, three or four steps between. At most ONE muted accent — desaturated, never neon — used sparingly (links, small markers, one highlight per viewport at most). Color never carries hierarchy; size, weight, and space do.

Example tokens:

```css
:root {
  --paper: #FAF7F2;        /* page background — warm off-white */
  --surface: #F1EDE6;      /* cards, alternate sections */
  --surface-2: #E7E1D8;    /* pressed / tertiary */
  --ink: #1A1815;          /* primary text — warm near-black */
  --ink-muted: #6B6459;    /* secondary text */
  --ink-faint: #A39B8D;    /* captions, metadata */
  --line: #DDD6CA;         /* hairline borders */
  --accent: #8C5E3C;       /* muted terracotta — pick ONE: terracotta, olive #6B7052, slate #5C6670, oxblood #6E3B3B */
  --accent-soft: #EFE4D9;  /* accent background tint */
}
```

Dark variant (optional): invert to warm charcoal `#161412` paper with `#EDE8E0` ink; keep the same accent, slightly lightened.

## Typography

The core of the system. Extreme contrast between display and body — that contrast replaces color and decoration.

Pairings (pick one):
- **Serif display + grotesque body:** Fraunces / Inter. Or: Canela-style ("GT Sectra", "Source Serif 4") / "Neue Haas"-style ("Archivo").
- **All-serif editorial:** Newsreader for display AND body — vary only size/weight/italic.
- **Grotesque display + serif body:** "Space Grotesk" / "Source Serif 4" (more contemporary studio feel).

Scale — large jumps, few steps (ratio ≈ 1.5–1.6):

```
--text-xs: 0.75rem     /* metadata, ALL-CAPS labels with letter-spacing: 0.08em */
--text-sm: 0.875rem    /* captions */
--text-base: 1.0625rem /* body — 17px, line-height 1.65, max-width 65ch */
--text-lg: 1.375rem    /* lead paragraphs, line-height 1.5 */
--text-2xl: 2.25rem    /* section headings */
--text-4xl: 3.75rem    /* page titles */
--text-hero: clamp(3rem, 8vw, 7rem)  /* hero — tight: line-height 1.02, letter-spacing -0.02em */
```

Rules:
- Headings: normal weight (400–500) at huge sizes reads more editorial than bold at medium sizes.
- Use italic of the display face as the "second voice" (pull quotes, emphasized words inside headings).
- ALL-CAPS only at xs size with generous tracking, for labels/eyebrows.
- `text-wrap: balance` on headings.

## Spacing, radius, shadow

- Base unit: **8px**; section padding is generous — 96–160px vertical between sections.
- Whitespace is the primary luxury signal. When in doubt, double the space.
- Radius: **0 or 2px** on almost everything. Images may use 4px. No pills except tiny metadata tags (full radius allowed at ≤24px height).
- Shadows: **none.** Elevation does not exist in this system. Separation comes from 1px hairlines (`--line`) and background shifts (`--paper` vs `--surface`).
- Borders: 1px solid `--line`. Full-width horizontal rules between sections are a signature move.

## Layout: flat bento grids

- 12-column grid, wide outer margins (min 5vw).
- Bento sections: CSS grid of flat cells separated by 1px gaps (gap renders as hairline via background color) or 1px borders — NOT floating shadowed cards.
- Asymmetry is mandatory: cells span different column/row counts; never a uniform 3×2 of identical cards.
- Big numbers/stats: display face at 2xl–4xl, label in xs caps below.
- Editorial layouts: text column offset from center, generous left margin used for metadata (dates, tags, figure numbers).

## Component treatments

- **Buttons:** text-only with underline on hover, or 1px-bordered rectangle (radius 0–2px), ink border, transparent fill; invert to ink fill / paper text on hover. Never gradient, never shadowed.
- **Links:** underlined by default (`text-decoration-thickness: 1px; text-underline-offset: 3px`), accent or ink colored.
- **Inputs:** bottom-border only, or 1px full border; label above in xs caps.
- **Cards:** flat surface shift + hairline border. Hover: background darkens one step, no lift.
- **Images:** full-bleed or grid-aligned, radius ≤4px, optional 1px inset hairline. Duotone/warm-grade treatments fit; saturated stocky photos do not.
- **Nav:** thin top bar, wordmark left, sparse text links right, 1px bottom hairline.

## Motion character

Restrained and precise. Nothing bounces, nothing springs.

- Durations: 150ms (micro), 300ms (standard), 600–800ms (page-level reveals only).
- Easing: `cubic-bezier(0.25, 0.1, 0.25, 1)` or plain `ease-out`. Never bounce/elastic.
- Signature moves: fade + 12px rise on scroll-in; underline grows from left on link hover; image scale 1.00→1.03 over 600ms on hover (inside overflow-hidden frame).
- No parallax, no floating blobs, no continuous ambient animation.

## Do / Don't

Do:
- Let one huge headline carry an entire section.
- Use hairline rules and background shifts for structure.
- Keep the accent rare enough to feel deliberate.
- Set metadata in small caps with wide tracking — it signals editorial craft.
- Use real (or realistic) copy; lorem destroys this style instantly.

Don't:
- No gradients of any kind (backgrounds, text, buttons).
- No drop shadows, glows, or glassmorphism.
- No pure #000/#FFF — always warm-shifted.
- No more than one accent color; no saturated/neon values.
- No border-radius above 4px (except tiny tags).
- No icon noise — prefer text labels; if icons, thin 1.5px stroke, monochrome.
- No uniform card grids; no centered-everything layouts.
