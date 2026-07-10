---
name: redesign
description: Upgrades an EXISTING website or app to premium visual quality without breaking functionality. Audit-first workflow - inventories current pages and components, identifies generic-AI and template patterns (centered-everything, purple gradients, uniform card grids, emoji icons), produces a prioritized redesign plan, then applies changes in safe increments that preserve markup semantics, routes, and JS behavior, ending with a before/after verification checklist. Framework-agnostic (Tailwind, vanilla CSS, CSS-in-JS). Use when the user says "redesign", "make this site look premium", "upgrade the design", "this looks AI-generated", "modernize the UI", or "improve the design without breaking it". NOT for greenfield builds - for new projects use taste (creative direction) plus style-systems (visual system); NOT for micro-detail passes on already-good UIs (use interface-polish).
---

# Redesign

Upgrade an existing site or app to premium quality. The prime directive: **the product must work identically after the redesign.** Every change is visual; behavior, content, routes, and data flow are untouchable.

Never start restyling on sight. Follow the phases in order.

## Phase 1: Inventory

Build a factual map before judging anything.

1. **Pages/routes:** list every page or route (router config, `pages/`/`app/` dir, sitemap, nav links). Note which are high-traffic/high-stakes (home, pricing, main app view) vs. long-tail.
2. **Styling architecture:** identify the system — Tailwind (which version, config location), CSS Modules, styled-components/Emotion, SCSS, plain CSS, inline styles, UI kit (shadcn, MUI, Bootstrap). Find where global tokens/theme live, if anywhere.
3. **Component inventory:** list shared components (buttons, cards, inputs, nav, modals, tables) and where they're defined. Note duplicated one-off variants — these are consolidation targets.
4. **Current tokens:** extract actual values in use — every font-family, the set of font sizes, all colors (grep hex/rgb/hsl and Tailwind color classes), radius values, shadow values. A long messy list is itself a finding.
5. **Behavior to preserve:** note JS-driven UI (dropdowns, modals, carousels, form validation, charts) and the selectors/classes/data-attributes the JS depends on.
6. **Screenshots (if a browser tool is available):** capture key pages at desktop and mobile widths as the "before" record.

## Phase 2: Diagnose — generic-AI and template patterns

Score the current design against this list. Each hit goes into the findings with file/location.

**Layout tells:**
- Centered-everything: every section a centered heading + centered paragraph + centered buttons, stacked forever.
- Uniform card grids: 3×2 identical cards with icon-title-text, repeated per section.
- Every section same width, same padding, same rhythm — no full-bleed moments, no asymmetry.
- Hero = headline + subline + two buttons + floating screenshot, dead center.

**Color tells:**
- Purple/indigo-to-blue gradients (the default AI palette), gradient text on headlines, glow blobs.
- Pure #000 on pure #FFF, or gray-on-gray with no committed direction.
- 10+ arbitrary colors with no ramp; accent color used everywhere so nothing stands out.

**Component tells:**
- Emoji as icons (🚀 ✨ 💡 in feature cards) or mixed icon families.
- Default-styled UI-kit components (untouched shadcn/Bootstrap look).
- Same border-radius and same shadow on literally everything.
- Badges/pills above every heading saying "✨ New" or the section name.

**Type tells:**
- One font, one weight-jump (400/700), timid scale (h1 barely 2× body).
- Headlines that are generic value-prop mad-libs ("Unlock the power of X", "Supercharge your workflow").
- Lorem-adjacent or placeholder copy anywhere.

**Content tells:**
- Fake testimonials/logos, "Trusted by 10,000+ teams" with no evidence, stock-photo energy.

Also audit real quality issues beyond slop: contrast failures, inconsistent spacing, missing hover/focus states, unstyled empty/error states, mobile breakage.

## Phase 3: Plan

Produce a prioritized plan and present it before editing (unless the user asked to just proceed).

1. **Direction:** commit to one coherent visual direction. If the `style-systems` skill is available, pick a system from it; otherwise define tokens explicitly (palette ramp + accent, type pairing + scale, spacing unit, radius set, shadow set, motion set). One direction for the whole product.
2. **Order of work** (highest leverage first):
   1. Foundations: tokens/theme — colors, fonts, scale, spacing, radius, shadows. Changing these upgrades every page at once.
   2. Shared components: buttons, inputs, cards, nav, footer.
   3. Highest-stakes pages: hero/home, then main app views, then the rest.
   4. Slop-pattern fixes from Phase 2 (break up uniform grids, replace emoji icons, kill gradient text, rewrite mad-lib headlines if the user permits copy changes).
   5. States: hover/focus/empty/loading/error.
3. **Risk register:** list every place where restyling touches JS-coupled markup, and the plan to avoid breakage (see rules below).
4. **Out of scope:** explicitly note what will NOT change (routes, copy meaning, features, data).

## Phase 4: Apply in safe increments

Work in small, verifiable increments — one foundation layer or one component family or one page section per increment. After each, verify (Phase 5 quick pass) before continuing.

**Preservation rules:**
- Keep markup semantics: don't change tag types that carry behavior or a11y meaning (`button` stays `button`, form structure stays intact, heading hierarchy stays ordered).
- Never rename or remove ids, `data-*` attributes, ARIA attributes, or classes referenced by JS/tests. Grep for a class in `.js`/`.ts` files before deleting it from markup. Add new classes alongside instead of replacing when unsure.
- Never change routes, hrefs, form actions/methods, input names.
- Don't restructure DOM that JS traverses (carousel/dropdown/menu internals) — restyle via CSS on the existing structure.
- Copy changes only if the user approved them; even then, preserve meaning and keywords (SEO).
- Prefer additive CSS and token redefinition over markup surgery. In Tailwind, prefer editing the theme config over hand-editing thousands of utility classes — theme-level change is the highest-leverage, lowest-risk move.
- Keep every increment in its own commit if the project uses git, so any regression bisects cleanly.
- Respect the existing styling architecture. Do not introduce a second styling system (e.g. adding styled-components to a Tailwind project) — that's a maintenance regression, not a redesign.

**Framework notes:**
- **Tailwind:** redefine `theme` (colors, fontFamily, borderRadius, boxShadow, spacing) first; then sweep components for arbitrary values (`[#7c3aed]`, `[13px]`) and slop utilities (`bg-gradient-to-r from-purple-...`).
- **Vanilla CSS/SCSS:** introduce `:root` custom properties, then migrate rules to reference them; leave selectors alone.
- **CSS-in-JS:** update the theme object; sweep for hardcoded values inside `styled`/`css` blocks.
- **UI kits:** override at the theme/provider level (MUI theme, shadcn CSS variables) rather than per-instance.

## Phase 5: Verify — before/after checklist

Run after each increment (quick) and fully at the end.

**Functionality (must all pass):**
- [ ] Build compiles with no new errors/warnings; existing tests still pass.
- [ ] Every route from the Phase 1 inventory still renders.
- [ ] All interactive elements work: nav (incl. mobile menu), dropdowns, modals, forms submit, validation messages appear, carousels/tabs/accordions operate.
- [ ] No JS console errors introduced.
- [ ] No id/data-attribute/JS-referenced class was renamed (re-grep).
- [ ] Keyboard navigation and focus visibility still work; heading order still valid.

**Visual (compare against "before" screenshots):**
- [ ] Every Phase 2 finding is resolved or consciously deferred (say which).
- [ ] One coherent direction: single accent, one type system, consistent radius/shadow/spacing tokens everywhere.
- [ ] No remaining raw hex/arbitrary values outside token definitions (grep).
- [ ] Text contrast ≥ 4.5:1 for body, 3:1 for large text.
- [ ] Mobile (~375px), tablet (~768px), desktop (~1280px) all intact; no horizontal scroll.
- [ ] Hover and focus states exist on all interactive elements.
- [ ] Images not distorted; no layout shift from missing dimensions.

**Report:** summarize per page — what changed, before/after screenshots if captured, findings deferred and why.

## Failure modes to avoid

- Restyling before inventorying → JS breakage discovered late. Always Phase 1 first.
- "While I'm here" feature changes or copy rewrites the user never asked for.
- Replacing one generic template look with a different generic template look (swapping purple gradients for teal gradients is not a redesign).
- Big-bang rewrite of all styles in one pass — impossible to verify, impossible to bisect.
- Polishing micro-details while foundations are still incoherent. Finish this skill's work first; micro-detail passes belong to `interface-polish` afterwards.
