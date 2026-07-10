---
name: interface-polish
description: Design-engineering micro-detail pass for interfaces that already work but feel unrefined. Applies concrete CSS/JS rules for hover/active/focus states, transition timing and easing, enter/exit animations, stagger patterns, layered shadows, border-vs-shadow elevation, nested border-radius, optical alignment, typography details (tabular numbers, letter-spacing, text-wrap balance), image treatment, scroll behavior, and reduced-motion support. Use when the user says "polish", "make it feel better", "it feels off", "micro-interactions", "finishing touches", "add the last 10 percent", or when a UI is functionally done but flat. NOT for full visual overhauls of unrefined designs (use redesign), NOT for choosing a visual direction or creative concept (use taste or style-systems) - this skill refines execution details within an already-chosen design.
---

# Interface Polish

The last 10% that separates "works" from "feels great". Apply these rules to an interface whose layout, palette, and structure are already decided. Do not change the design direction — refine its execution.

Work through the sections as a checklist against the actual code. Fix what's missing; leave what's already right.

## 1. Interactive states

Every interactive element needs four distinct states: rest, hover, active, focus-visible. Missing states are the #1 "feels unfinished" signal.

```css
.button {
  transition: background-color 150ms ease, box-shadow 150ms ease, transform 100ms ease;
}
.button:hover  { background-color: var(--accent-hover); }
.button:active { transform: scale(0.98); transition-duration: 50ms; } /* press responds FASTER than hover */
.button:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;   /* never outline: none without a replacement */
}
```

Rules:
- Hover changes must be subtle but unmistakable: one step of background shift, or 1–2px lift with shadow deepening — not both plus a color change.
- `:active` should feel physically pressed: scale 0.97–0.98 or translateY(1px), with a shorter duration than hover.
- Use `:focus-visible`, not `:focus`, so mouse clicks don't paint rings but keyboards do.
- Rows/list items: hover = `background-color` shift only; don't move them.
- Disabled: reduce opacity to ~0.5 AND remove hover effects (`pointer-events: none` or explicit rules).
- Touch: hover states must not be load-bearing; anything revealed on hover needs a touch/focus path too.

## 2. Transition timing and easing

- Durations: 100–150ms hover/press · 200ms dropdowns, tooltips · 250–300ms modals, drawers, layout shifts · 400–600ms only for page-level or decorative reveals. When unsure, subtract 50ms — slow transitions read as lag.
- **Never `transition: all`.** List properties explicitly; `all` causes accidental animation of layout properties and jank.
- Easing: `ease-out` for things appearing/responding to the user (start fast, settle). `ease-in` or `ease-in-out` for things leaving. `cubic-bezier(0.16, 1, 0.3, 1)` (expo-out) makes entrances feel expensive. Bounce/overshoot only if the design system is playful — and subtle (≤8% past target).
- Exit faster than enter: a modal opening at 250ms should close in ~180ms. Users wait for what appears; they've already dismissed what's leaving.
- Animate only compositor-friendly properties where possible: `transform`, `opacity`. Animating `width/height/top/left/margin` causes layout jank; if unavoidable, keep the element small or use `transform` tricks. Never animate `box-shadow` directly on large surfaces — crossfade a pseudo-element's opacity instead:

```css
.card::after {
  content: ""; position: absolute; inset: 0; border-radius: inherit;
  box-shadow: var(--shadow-lg); opacity: 0; transition: opacity 200ms ease;
  pointer-events: none;
}
.card:hover::after { opacity: 1; }
```

## 3. Enter/exit animations

Elements should arrive from somewhere, not pop into existence.

- Pattern: fade + small movement. Opacity 0→1 plus translateY(8–12px)→0, or scale(0.96–0.98)→1 for popovers/modals. Movement over ~16px looks theatrical.
- Origin matters: dropdowns scale/slide from the trigger (`transform-origin: top left` or as appropriate), toasts slide from the edge they live on, modals scale from center.
- Exit animations require keeping the node until the animation ends. In CSS-only setups, prefer `@starting-style` + `transition-behavior: allow-discrete` (modern) or toggle a class and remove on `transitionend`. In React, use a presence utility or a two-step state (closing → closed).

```css
dialog {
  opacity: 1; transform: scale(1);
  transition: opacity 200ms ease-out, transform 200ms cubic-bezier(0.16, 1, 0.3, 1),
              overlay 200ms allow-discrete, display 200ms allow-discrete;
}
@starting-style { dialog[open] { opacity: 0; transform: scale(0.97); } }
dialog:not([open]) { opacity: 0; transform: scale(0.98); }
```

- Height-into-view (accordions): animate `grid-template-rows: 0fr → 1fr` on a grid wrapper with `min-height: 0` on the child — smooth without measuring heights.

## 4. Stagger

Lists that animate in as one block feel cheap; a small cascade feels orchestrated.

- Delay step: 30–60ms between items. Total cascade should finish under ~600ms — cap the delay after 8–10 items (`min(index, 8) * 40ms`).
- Stagger only on first entrance (page load, list appearing) — not on every re-render or filter change.

```css
.list > * { animation: item-in 350ms cubic-bezier(0.16, 1, 0.3, 1) backwards; }
.list > :nth-child(1) { animation-delay: 0ms; }
.list > :nth-child(2) { animation-delay: 40ms; }
/* or dynamically: */
```

```js
document.querySelectorAll(".list > *").forEach((el, i) => {
  el.style.animationDelay = `${Math.min(i, 8) * 40}ms`;
});
```

```css
@keyframes item-in { from { opacity: 0; transform: translateY(10px); } }
```

`animation-fill-mode: backwards` prevents the pre-delay flash of the final state.

## 5. Shadows and elevation

- Single-layer shadows look flat. Layer a tight contact shadow with a soft ambient one:

```css
--shadow-md: 0 1px 2px rgba(16, 24, 40, 0.06),   /* contact: small blur, small offset */
             0 8px 24px rgba(16, 24, 40, 0.10);  /* ambient: large blur, large offset */
```

- Shadow color: tint toward the background/brand hue instead of pure black — `rgba(16,24,40,…)` on cool UIs, warm equivalents on warm UIs. Pure black shadows look dirty on colored backgrounds.
- Y-offset grows with elevation; blur ≈ 2–3× offset; opacity DROPS as blur grows.
- **Border vs shadow:** static containers on a page → 1px border (or background shift), no shadow or a whisper (`--shadow-xs`). Floating ephemerals (menus, popovers, modals, drag previews) → shadow, plus a hairline border so edges survive on white-on-white. Shadow communicates "above the page"; if it doesn't float, it shouldn't cast much.
- Dark mode: shadows nearly disappear against dark backgrounds — convey elevation with lighter surface colors and borders instead; keep only a faint shadow for grounding.
- Inset highlight for a crisp premium edge on raised elements: `box-shadow: inset 0 1px 0 rgba(255,255,255,0.08)` (dark UIs) as an extra layer.

## 6. Border-radius nesting

Concentric corners: **inner radius = outer radius − padding.** A 16px-radius card with 8px padding needs 8px-radius children; giving them 16px too makes corners visibly clash.

```css
.card  { border-radius: 16px; padding: 8px; }
.card > .thumb { border-radius: calc(16px - 8px); } /* = 8px */
```

- If the math gives ≤2px, use a small consistent value (2–4px) rather than 0 next to a large outer radius.
- Never mix radius scales on siblings (a 4px button beside a 12px button).
- Pills inside rounded containers are exempt (radius 999px reads as its own shape).
- Elements clipped at a rounded parent's edge need `overflow: hidden` on the parent or matching radius on the child, or corners will poke out.

## 7. Optical alignment

Mathematical centering is often visually wrong; trust the eye and nudge.

- Play/triangle icons in circles: shift right ~1–2px (visual mass sits left of the bounding box).
- Icons beside text: align to cap-height/x-height feel, not baseline math — usually `translateY(-0.5px – 1px)` or flexbox `align-items: center` plus a nudge.
- Text in buttons: many fonts render slightly low; `padding-bottom: 1px` less than top, or line-height tuning, makes labels look centered.
- Large display text: the bounding box includes side bearings; pull the first line left with `margin-left: -0.05em` to flush-align it with body text below.
- Chevrons/arrows following labels: optical gap ≈ 4–6px, less than the grid would suggest.
- Rule of thumb: when something "looks off-center" but the inspector says it's centered, the inspector is wrong. Nudge by 1–2px and re-check by eye (or screenshot).

## 8. Typography details

- **Tabular numbers** wherever digits change or align (tables, timers, counters, prices in lists): `font-variant-numeric: tabular-nums;` — otherwise columns wobble and timers jitter.
- **Letter-spacing scales inversely with size:** large display text needs negative tracking (`-0.01em` to `-0.03em` above ~32px); small ALL-CAPS labels need positive tracking (`0.04em`–`0.08em`). Body text: none.
- **`text-wrap: balance`** on headings (≤4 lines); **`text-wrap: pretty`** on paragraphs to prevent orphan words.
- **Font smoothing:** on macOS, light-on-dark text renders heavy; `-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;` slims it. Apply globally on dark UIs; use judgment on light ones.
- Line-height pairs inversely with size: body 1.5–1.65, headings 1.1–1.2, giant display 0.95–1.05.
- Truncation: single line `text-overflow: ellipsis; white-space: nowrap; overflow: hidden;`; multi-line `-webkit-line-clamp`. Always add `title` or a tooltip for truncated content.
- Hyphens/`overflow-wrap: anywhere` on user-generated strings so long tokens can't blow layouts.
- Interpolate `font-variation-settings`/weight rather than swapping weights on hover (weight-swap causes width jump; if you must, reserve width with a bold hidden twin).

## 9. Image treatment

- Subtle inset outline stops light images from bleeding into light backgrounds:

```css
.img-frame { position: relative; }
.img-frame::after {
  content: ""; position: absolute; inset: 0; border-radius: inherit;
  box-shadow: inset 0 0 0 1px rgba(16, 24, 40, 0.08);
  pointer-events: none;
}
```

- Reserve space to kill layout shift: always set `width`/`height` attributes or `aspect-ratio` on the container; `object-fit: cover` for fills.
- Background-color placeholder (`background: var(--surface-2)`) behind every image so slow loads show a designed surface, not a void.
- Avatars: add the inset ring above plus a background color for missing images; never let a broken-image glyph render.
- Hover zoom belongs inside an `overflow: hidden` frame: image scales 1→1.03–1.05, frame stays put.
- `loading="lazy"` below the fold; never on the LCP/hero image.

## 10. Scroll behavior

- `scroll-margin-top` on anchor targets so sticky headers don't cover them: `[id] { scroll-margin-top: calc(var(--header-h) + 16px); }`
- `scroll-behavior: smooth` for in-page anchors — gate it behind reduced-motion (see §11).
- Horizontal scrollers (chip rows, card rails): `scroll-snap-type: x mandatory` + `scroll-snap-align: start`, hide scrollbar only if arrows/affordances exist, add `overscroll-behavior-x: contain`.
- Modals/drawers: lock body scroll while open (`overflow: hidden` on body or `overscroll-behavior: contain` on the panel) — background scroll bleed feels broken.
- Custom scrollbars: thin and unobtrusive is fine (`scrollbar-width: thin; scrollbar-color: var(--border) transparent`); never remove scrollbars from long content.
- Scroll-triggered reveals: threshold ~0.15–0.25, animate once, never re-hide on scroll-up:

```js
const io = new IntersectionObserver((entries) => {
  for (const e of entries) if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
}, { threshold: 0.2 });
document.querySelectorAll("[data-reveal]").forEach((el) => io.observe(el));
```

## 11. Reduced motion

Non-negotiable. Every animation added by this pass must respect `prefers-reduced-motion`.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

- The blanket rule above is the safety net; prefer targeted alternatives where motion carries meaning (e.g. keep the fade, drop the movement).
- In JS animation code, check `matchMedia("(prefers-reduced-motion: reduce)").matches` before starting loops, parallax, or auto-playing sequences.
- Opacity fades are generally safe under reduced motion; large translations, scaling, parallax, and auto-scroll are not.

## Final pass checklist

- [ ] All interactive elements: hover, active, focus-visible, disabled states present and distinct.
- [ ] No `transition: all`; all durations ≤300ms in-app; exits faster than entrances.
- [ ] Entering elements fade+move ≤16px; ephemerals originate from their trigger.
- [ ] First-load lists stagger ≤60ms/item, capped.
- [ ] Shadows layered and tinted; borders on static, shadows on floating; dark mode uses surface steps.
- [ ] Nested radii follow inner = outer − padding.
- [ ] Icon/text alignment checked by eye, not just by flexbox.
- [ ] Tabular nums on data; tracking tightened on display, widened on caps labels; headings balanced.
- [ ] Images: aspect-ratio reserved, placeholder background, inset outline where needed.
- [ ] Anchor scroll-margin set; body locked under modals; reveals fire once.
- [ ] `prefers-reduced-motion` handled globally and in JS.
