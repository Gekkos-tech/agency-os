---
name: style-systems
description: Commits a project to ONE named visual style system and applies it consistently at token level. Use when deciding a visual direction for a build — "which style should this be", "pick a visual direction", "style system", "minimalist design", "brutalist site", "soft UI", "clean product UI" — or when a codebase mixes styles and needs to be pulled onto a single coherent system. Contains four complete standalone style specs (minimalist-editorial, brutalist-industrial, soft-depth, product-modern) with palettes, type scales, spacing, shadows, components, and motion. NOT a searchable style/palette database (use ui-ux-pro-max for that), not a workflow command (impeccable), and not creative direction from a brief (taste) — this skill enforces one coherent system end-to-end once a direction is chosen.
---

# Style Systems

One project, one style system. This skill selects a single named visual system and enforces it in every token, component, and animation. Consistency beats novelty: a mediocre system applied perfectly looks better than a great system applied at 80%.

## Step 1: Pick the system from the brief

Read the brief (or existing product) and match it against these signals. Pick exactly one. If two systems seem plausible, pick the one matching the AUDIENCE, not the one that looks most impressive.

| Signal in brief | System |
|---|---|
| Editorial, portfolio, studio, publication, luxury, calm, "less is more", content-first, photography-led | **minimalist-editorial** |
| Dev tools, data-heavy, hacker, engineering culture, "raw", terminal, technical documentation, anti-corporate | **brutalist-industrial** |
| Consumer app, wellness, kids/family, finance-for-humans, "friendly", "approachable", onboarding-heavy, mobile-first | **soft-depth** |
| SaaS dashboard, B2B product, admin panel, settings-heavy app, "clean and professional", startup landing + app combo | **product-modern** |

Tie-breakers:
- Dense data UI + technical audience → brutalist-industrial. Dense data UI + business audience → product-modern.
- Marketing site for a soft consumer brand → soft-depth. Marketing site for a serious brand → minimalist-editorial.
- If the user names a system or vibe explicitly, honor it even if signals disagree.

State the chosen system in one sentence before writing any code, e.g. "Committing to product-modern: neutral surfaces, single blue accent, 8pt grid."

## Step 2: Load the spec

Read the full reference file for the chosen system BEFORE writing CSS. Do not work from the one-line summaries above.

| System | Spec |
|---|---|
| minimalist-editorial | [references/minimalist-editorial.md](references/minimalist-editorial.md) |
| brutalist-industrial | [references/brutalist-industrial.md](references/brutalist-industrial.md) |
| soft-depth | [references/soft-depth.md](references/soft-depth.md) |
| product-modern | [references/product-modern.md](references/product-modern.md) |

## Hard rule: never mix systems

Once committed, every decision comes from the chosen spec. Violations that count as mixing:

- Soft pastel gradients inside a brutalist layout.
- A single "fun" rounded card in an otherwise editorial page.
- Neumorphic shadows on one component of a flat system.
- Borrowing a second system's accent color "just for the CTA".
- Switching type personality between marketing pages and app pages of the same product.

If a component feels impossible within the system, the answer is a more disciplined execution of the system — not a borrowed treatment. The only legitimate exception is embedded third-party UI you cannot restyle; isolate it visually rather than adapting your system toward it.

## Token-level consistency

Define tokens once, at the top, from the chosen spec. Everything downstream references tokens — never raw values scattered in components.

1. **Colors:** define the full palette as CSS custom properties (or Tailwind theme extension). Every color in the app must resolve to a token. If you type a hex value inside a component file, stop and add a token instead.
2. **Type scale:** one scale, one or two families, defined once. No per-component font sizes outside the scale.
3. **Spacing:** one base unit (the spec says which). All margins/paddings/gaps are multiples of it.
4. **Radius:** the spec gives 2–4 radius values. Use only those. Nested radii follow inner = outer − padding.
5. **Shadows:** copy the spec's shadow recipes verbatim into tokens (`--shadow-sm`, `--shadow-md`, ...). Never improvise a `box-shadow` inline.
6. **Motion:** one duration set + one easing set from the spec, as tokens. All transitions reference them.

Example skeleton (adapt names to the spec):

```css
:root {
  /* color */   --bg: ...; --surface: ...; --text: ...; --text-muted: ...; --accent: ...; --border: ...;
  /* type */    --font-display: ...; --font-body: ...; --font-mono: ...;
  /* space */   --space-1: ...; --space-2: ...; /* multiples of the base unit */
  /* radius */  --radius-sm: ...; --radius-md: ...; --radius-lg: ...;
  /* shadow */  --shadow-sm: ...; --shadow-md: ...;
  /* motion */  --duration-fast: ...; --duration-base: ...; --ease-out: ...;
}
```

## Consistency checklist (run before finishing)

- [ ] Every page and component uses only tokens from the single chosen spec.
- [ ] Grep for raw hex values / rgb() in component code; each hit is either a token definition or a bug.
- [ ] Only radius values from the spec appear anywhere.
- [ ] Only the spec's shadow recipes appear anywhere.
- [ ] Font families: at most the ones the spec allows, loaded once.
- [ ] All spacing values are multiples of the spec's base unit.
- [ ] Motion durations/easings come from the token set.
- [ ] Each item on the spec's "don't" list is verifiably absent.
- [ ] Announce which system was applied in your summary to the user.
