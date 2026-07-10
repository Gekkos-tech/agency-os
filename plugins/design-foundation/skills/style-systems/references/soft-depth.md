# Soft Depth

Rounded geometry, pastel palettes, layered soft shadows, gentle gradients. The interface feels like friendly physical objects on a soft surface — approachable, calm, consumer-grade. Depth is real but weightless: things rest, they don't slam.

Use for: consumer apps, wellness/health, family products, fintech-for-humans, education, onboarding-heavy mobile-first products.

## Palette philosophy

A tinted (never gray) off-white base, white cards, and a pastel family built around ONE hero hue with 2–3 supporting pastels for categories/illustration. Text stays a soft dark (tinted toward the hero hue) — never pure black, which feels harsh against pastels. Every pastel needs a matching "deep" version for text/icons sitting on it, keeping contrast accessible.

Example tokens (lavender hero):

```css
:root {
  --bg: #F6F5FB;            /* lavender-tinted off-white */
  --card: #FFFFFF;
  --card-tint: #FBFAFE;     /* nested surfaces */
  --text: #2E2A3E;          /* soft ink, tinted toward hero */
  --text-muted: #736E88;
  --border: #E9E6F4;        /* barely-there */
  --hero: #7C6FDE;          /* primary actions */
  --hero-soft: #E8E4FB;     /* selected states, chips */
  --hero-deep: #4C3FA8;     /* text on hero-soft */
  --peach: #FFD9C7;  --peach-deep: #9A4A22;
  --mint:  #C9EEDD;  --mint-deep:  #1E6B4C;
  --butter:#FBEBC2;  --butter-deep:#8A6410;
  --danger:#E05B6D;  --success:#3BA776;
}
```

Rules: supporting pastels appear only as backgrounds/illustration, never as action colors — actions are always `--hero`. Check every `*-deep`-on-pastel pair for ≥4.5:1 contrast.

## Typography

Rounded or humanist faces with soft terminals. Warm, legible, never severe.

Pairings (pick one):
- **Rounded + geometric:** "Nunito" or "Quicksand" for display, "Inter" or "DM Sans" for body/UI.
- **Soft geometric throughout:** "Plus Jakarta Sans" or "Sora" for everything (safest).
- **Friendly serif accent:** "Fraunces" (soft optical size) display + "DM Sans" body — premium-cozy.

Scale — moderate contrast (ratio ≈ 1.25–1.33); this system does not shout:

```
--text-xs: 0.75rem     /* labels */
--text-sm: 0.875rem    /* secondary, captions */
--text-base: 1rem      /* body, line-height 1.6 */
--text-lg: 1.125rem
--text-xl: 1.375rem    /* card titles, weight 600 */
--text-2xl: 1.75rem    /* section heads, weight 700 */
--text-3xl: 2.5rem     /* page titles */
--text-hero: clamp(2.5rem, 6vw, 4rem)  /* line-height 1.1 — never tighter */
```

Rules: headings 600–700, never 900. No uppercase tracking-heavy labels — sentence case everywhere. Slight negative letter-spacing (-0.01em) on headings only.

## Spacing, radius, shadow

- Base unit: **8px**; components are airy — cards get 24–32px padding, sections 80–120px.
- Radius — the signature. Large and consistent:
  - `--radius-sm: 10px` (inputs, chips) · `--radius-md: 16px` (buttons, small cards) · `--radius-lg: 24px` (cards, modals) · `--radius-xl: 32px` (hero panels, sheets) · `--radius-full: 999px` (pills, avatars).
  - Nesting rule: inner radius = outer radius − padding (a 24px card with 12px padding holds 12px-radius children).
- Shadows — layered, colored, soft. Shadow color derives from the hero hue, never pure black:

```css
--shadow-sm: 0 1px 2px rgba(76, 63, 168, 0.06), 0 2px 8px rgba(76, 63, 168, 0.06);
--shadow-md: 0 2px 4px rgba(76, 63, 168, 0.05), 0 8px 24px rgba(76, 63, 168, 0.10);
--shadow-lg: 0 4px 8px rgba(76, 63, 168, 0.06), 0 20px 48px rgba(76, 63, 168, 0.14);
```

  Always ≥2 layers (tight + ambient). Large blur, low opacity, generous y-offset. Never `0 0` glows, never hard edges.
- Gradients — allowed but gentle: two neighboring pastels, ≤15° hue apart in feel, subtle (e.g. `linear-gradient(135deg, #EDE9FD, #FDEDE4)`), on hero panels and buttons. Never rainbow, never dark-purple-to-blue "AI slop" gradients, never gradient text.
- Borders: mostly none (shadow separates); where needed, 1px `--border`.

## Layout

- Cards float on the tinted background with `--shadow-sm/md` — the core layout unit.
- Generous gaps (24–32px) between cards; grids may mix card sizes but keep the radius family constant.
- Mobile-first patterns even on desktop: bottom sheets, segmented pills, horizontally scrolling chip rows, FAB-style primary actions.
- Blob/organic shapes and soft illustration allowed as backgrounds — max one per viewport, low contrast.

## Component treatments

- **Buttons:** pill or radius-md, solid `--hero` fill, white 600-weight label, `--shadow-sm`. Hover: lift 1–2px + shadow-md; active: press back down + shadow-sm. Secondary: `--hero-soft` fill with `--hero-deep` text.
- **Inputs:** filled style — `--card-tint` or `--bg` fill, radius-sm–md, no border at rest; focus = 2px `--hero` border or 3–4px `--hero-soft` ring. Labels above, sentence case.
- **Cards:** white, radius-lg, shadow-sm, 24px+ padding. Category cards may use a supporting pastel fill with its deep text.
- **Chips/tags:** pill, pastel fill + deep text.
- **Toggles/sliders:** chunky (28px+ knobs), hero-colored when on, springy transition.
- **Icons:** rounded stroke (2–2.5px, round caps) or soft duotone using pastel + deep. One family only. No emoji as UI icons.
- **Empty states:** friendly illustration in the pastel family + one-line encouraging copy + primary action.

## Motion character

Springy and warm — objects have gentle mass. Motion should make people smile, quietly.

- Durations: 150ms (micro), 250–350ms (standard), 450ms (sheets/modals).
- Easing: `cubic-bezier(0.34, 1.56, 0.64, 1)` (soft back/overshoot) for entrances and toggles; `cubic-bezier(0.22, 1, 0.36, 1)` for movement; CSS springs / `bounce: 0.15`-style where the stack allows.
- Signature moves: press-scale on tap (`transform: scale(0.97)` on :active); cards rise 2px on hover with shadow deepening; sheets slide up with slight overshoot; staggered 40ms card entrances; checkmark draw-in on success.
- Keep overshoot subtle (≤8% past target). Respect `prefers-reduced-motion`.

## Do / Don't

Do:
- Keep one radius family and one shadow family — sloppiness here kills the style fastest.
- Tint everything (background, text, shadows) toward the hero hue.
- Pair every pastel with its deep partner; verify contrast.
- Use sentence case, plain warm language ("You're all set") in UI copy.
- Give interactive elements a tactile press state.

Don't:
- No pure black text, no pure gray backgrounds — always tinted.
- No neumorphism (inset dual shadows sculpting the background) — this system floats cards, it doesn't emboss them.
- No hard 1px dark borders around cards; no square corners anywhere.
- No saturated/neon colors; no dark-purple SaaS gradients; no gradient text.
- No mixing radius scales (a 4px-radius input inside a 24px card reads broken).
- No aggressive uppercase labels or condensed fonts.
- No heavy black shadows (`rgba(0,0,0,0.3)`); shadow is always colored and soft.
