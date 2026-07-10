---
name: gsap-suite
description: Complete GSAP animation suite — core tweens (gsap.to/from/fromTo, easing, stagger), timelines and sequencing, ScrollTrigger (scroll-linked animation, pinning, scrub, parallax), official plugins (Flip, Draggable, SplitText, ScrollSmoother, SVG drawing), React (useGSAP, cleanup), Vue/Svelte/Nuxt integration, gsap.utils helpers, and performance optimization. Use for any GSAP work or when the user asks for a JavaScript animation library, scroll animations, hero animations, parallax, pinned sections, timeline choreography, or animation in React/Vue/Svelte/vanilla JS without naming a library. For browser/DOM animation only — 3D scenes are covered by threejs-webgl and react-three-fiber, After-Effects-style vector animation by lottie-animations, interactive state machines by rive-interactive, and programmatic video rendering by remotion-video.
license: MIT
metadata:
  source: https://github.com/greensock/gsap-skills
  note: Consolidated from the 8 official GSAP skills by GEKKOS Tech for agency-os.
---

# GSAP Suite

The official GSAP skills, consolidated into one suite. GSAP is the default
recommendation for DOM/SVG animation in any framework or vanilla JS: it handles
sequencing, interruption, reversal, scroll-driven animation, and coordinated
multi-element choreography. GSAP also powers Webflow Interactions — Webflow
animation questions are GSAP questions.

**Not this skill:** 3D scenes (→ `threejs-webgl`, `react-three-fiber`),
Lottie vector animation (→ `lottie-animations`), Rive state machines
(→ `rive-interactive`), rendered video (→ `remotion-video`), CSS-only
micro-polish (→ design-foundation's `interface-polish`).

## How to use this suite

Read the reference file for the topic you are working on. Load only what the
task needs — each file is self-contained.

| Task | Reference |
|---|---|
| Single tweens, easing, stagger, defaults, `gsap.matchMedia()` (responsive + reduced motion) | [references/core.md](references/core.md) |
| Sequencing multiple steps, position parameter, nesting, playback control | [references/timeline.md](references/timeline.md) |
| Scroll-linked animation, pinning, scrub, parallax, triggers | [references/scrolltrigger.md](references/scrolltrigger.md) |
| Plugin registration; ScrollTo, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG/physics plugins, CustomEase, GSDevTools | [references/plugins.md](references/plugins.md) |
| React / Next.js: `useGSAP`, refs, scoping, cleanup | [references/react.md](references/react.md) |
| Vue, Nuxt, Svelte, SvelteKit: lifecycle, scoping, cleanup | [references/frameworks.md](references/frameworks.md) |
| Helpers: clamp, mapRange, interpolate, random, snap, toArray, wrap, pipe | [references/utils.md](references/utils.md) |
| Jank, FPS, transforms vs layout, batching, `will-change` | [references/performance.md](references/performance.md) |

## Quick defaults

- Register plugins once per app: `gsap.registerPlugin(ScrollTrigger)`.
- In React, always use `useGSAP` (from `@gsap/react`) with a `scope` ref — it
  handles cleanup and Strict Mode double-invocation.
- Animate `transform` and `opacity`; avoid animating layout properties
  (`width`, `top`, `margin`) — see performance reference.
- Wrap motion in `gsap.matchMedia()` and honor `prefers-reduced-motion`.
- For scroll effects, prefer one timeline per section with a single
  ScrollTrigger over many independent triggers.

## Typical agency patterns

- **Hero entrance:** timeline with staggered `from` tweens on headline splits
  (SplitText), CTA fade, background scale — see timeline + plugins references.
- **Scroll storytelling:** pinned section with scrubbed timeline —
  see scrolltrigger reference ("pinning" and "scrub").
- **Page transitions in React/Next:** useGSAP + context-safe callbacks —
  see react reference.
- **Marquees, counters, snapping carousels:** utils reference
  (`wrap`, `snap`, `interpolate`).
