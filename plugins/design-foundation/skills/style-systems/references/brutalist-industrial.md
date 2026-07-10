# Brutalist Industrial

Swiss print discipline fused with terminal utilitarianism. The page looks like a declassified technical document: rigid grids, raw 1–2px borders, extreme type contrast, mono metadata everywhere, zero decoration. Everything visible is structural.

Use for: dev tools, engineering brands, data-heavy dashboards, technical portfolios, documentation-first products, anti-corporate statements.

## Palette philosophy

Utilitarian, not expressive. A paper-or-carbon base, hard ink, and ONE signal color used like a highlighter on a blueprint — warnings, active states, key data. Optionally one secondary signal for semantic status only (error/ok). Color never decorates; it flags.

Example tokens (light "print" mode):

```css
:root {
  --paper: #EDEBE6;       /* unbleached print stock, or #F4F3EF */
  --panel: #E2DFD8;       /* recessed panels */
  --ink: #111110;         /* text, borders */
  --ink-muted: #55534E;
  --line: #111110;        /* borders are INK-colored, not soft gray */
  --signal: #FF4D00;      /* safety orange — or acid #C6F016, blueprint #0037FF, red #E30613 */
  --signal-ink: #111110;  /* text on signal */
}
```

Dark "terminal" mode:

```css
:root {
  --paper: #0C0C0B;  --panel: #151513;
  --ink: #E8E6DF;    --ink-muted: #8A877E;
  --line: #2E2C28;   /* borders may soften in dark */
  --signal: #FF4D00; /* or phosphor green #33FF66, amber #FFB000 */
}
```

Pick light OR dark as primary; do not gradient between them.

## Typography

Two voices, violently contrasted in size, never in decoration:

Pairings (pick one):
- **Grotesque + mono:** "Helvetica Now"/Inter Tight/Archivo for display, "JetBrains Mono"/"IBM Plex Mono"/"Space Mono" for data and labels.
- **Condensed industrial:** "Archivo Expanded" or "Druk"-style compressed for display, "IBM Plex Mono" body annotations.
- **All-mono terminal:** everything in one mono family; hierarchy purely via size and background inversions. (Hardest mode; only for terminal-native products.)

Scale — extreme contrast, ratio ≥ 2 between tiers:

```
--text-mono-xs: 0.6875rem  /* 11px mono — labels, coordinates, timestamps. UPPERCASE, letter-spacing 0.05em */
--text-mono-sm: 0.8125rem  /* 13px mono — table data, code */
--text-base: 1rem          /* body, line-height 1.55, max 70ch */
--text-lg: 1.5rem
--text-3xl: 3rem           /* section heads — uppercase, tight */
--text-display: clamp(4rem, 12vw, 11rem)  /* hero — line-height 0.92, letter-spacing -0.03em, uppercase */
```

Rules:
- Display type is HUGE and tight; body/labels are small and precise. Nothing in between — the middle sizes are what make pages look generic.
- All labels, buttons, nav items: uppercase mono at xs/sm.
- Number everything: sections get index prefixes (`01 — SPECIFICATIONS`), figures get `FIG. 03`, mono timestamps and coordinates as ambient metadata.
- Tabular figures (`font-variant-numeric: tabular-nums`) on all data.

## Spacing, radius, shadow

- Base unit: **4px** (denser than consumer UI). Section spacing 64–120px.
- Radius: **0. Everywhere. No exceptions.** Not even on avatars — crop square.
- Shadows: **none.** If depth is unavoidable, use a hard offset block: `box-shadow: 4px 4px 0 var(--ink)` — solid, no blur. Use rarely.
- Borders: 1px or 2px solid `--line`. Borders are the primary layout device: full grid lines between cells, boxes around everything meaningful.
- Grid lines may run the full viewport width/height — visible structure is the aesthetic.

## Layout

- Rigid 12-column grid with VISIBLE structure: bordered cells sharing edges (collapse borders — no double lines).
- Dense data tables with row hairlines; header row inverted (ink background, paper text).
- Asymmetric splits from the grid: 8/4, 9/3 — never soft centered heroes.
- Marginalia: mono annotations in gutters (version numbers, dates, crosshair "+" marks at grid intersections).
- Footer as an index: dense multi-column bordered link table.

## Component treatments

- **Buttons:** rectangle, 1–2px ink border, uppercase mono label, square corners. Hover: invert (ink fill, paper text) — instantly, ≤100ms. Primary variant: solid ink or solid signal fill.
- **Links:** mono, uppercase or `[BRACKETED]`, underline or `→` suffix on hover.
- **Inputs:** 1px border box, square, mono text; focus = 2px signal border, no glow.
- **Tables:** the flagship component. 1px row separators, uppercase mono headers, right-aligned tabular numbers.
- **Tags/badges:** bordered rectangles, uppercase mono, no fill (fill = signal only for alerts).
- **Cards:** bordered cells in the shared grid — never floating.
- **Charts:** hairline axes, ink series + one signal series, mono axis labels; no gradient fills, no smoothed curves unless the data warrants.
- **Icons:** avoid where a mono label works. If needed: 1.5px stroke, geometric, monochrome. Never emoji.

## Motion character

Mechanical, instant, stepped — the machine responds; it does not perform.

- Durations: 0–120ms for interaction states (hover inversions may be instant, `transition: none`); 200–300ms for panel/layout shifts.
- Easing: `linear` or `steps()` for terminal effects; `cubic-bezier(0.7, 0, 0.3, 1)` for the few smooth moves. Never bounce, never spring.
- Signature moves: instant hover inversion; typewriter/scramble text reveal on hero (once, fast, respect reduced-motion); blinking block cursor `▌`; stepped counters.
- Optional analog degradation, at low opacity only: subtle scanline or grain overlay (≤4% opacity), slight misregistration on the signal color. One such effect max per project.

## Do / Don't

Do:
- Make the grid visible; let borders do the layout.
- Push type contrast further than feels safe — 11px mono next to 160px display is the look.
- Annotate relentlessly: indices, timestamps, coordinates, version strings.
- Keep interaction feedback binary and instant.
- Invert (ink↔paper) as the main state change.

Don't:
- No border-radius, ever.
- No blur shadows, glows, or glassmorphism.
- No gradients (a hard two-stop split is not a gradient; anything smooth is banned).
- No pastel or "friendly" colors; no second decorative accent.
- No lowercase buttons/labels; no proportional-font data.
- No easing that overshoots; no floating/breathing ambient animation.
- No soft gray borders in light mode — borders are ink.
- Never dilute with "a little rounding to soften it" — that's mixing systems.
