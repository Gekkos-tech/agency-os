---
name: imagegen-web
description: Art direction for generating website design reference images that developers can faithfully rebuild. Use when the user asks for "design reference images", "generate the design first", "section images for the landing page", "website mockup images", or wants visual comps of a marketing site or landing page before coding. Core law — one horizontal image per page section (8 sections = 8 images), never a compressed full-page board; enforces a shared style-token block across all images, composition variety, readable in-image text, and a clear focal action per section. Not for mobile app screens (use imagegen-mobile) and not for implementing code from images (use image-to-code).
---

# Website Design Reference Images

Generate image-model comps that a developer (or coding model) can rebuild section by section with high fidelity. The output of this skill is a SET of images — one per page section — that together read as one coherent website.

## The one law: one section = one image

**Never generate a full-page board.** A single tall image containing hero + features + pricing + footer compresses every section into unreadable postage stamps and the model invents mush. Instead:

- List the page's sections first. A landing page with 8 sections produces **8 separate horizontal images**.
- Each image shows exactly ONE section at full width, as if screenshotted from a real site — roughly 16:9 or 3:2, landscape.
- If a section is genuinely tall (long pricing table), it may get a 4:3 image, never portrait.
- If the user asks for "the design" of a whole page, translate that into the section list and confirm it before generating.

## Workflow

### 1. Plan the page

Write the section list with one line of purpose each. Typical marketing page:

```
1. Hero            — value prop + primary CTA
2. Social proof    — logo strip / one metric
3. Feature A       — core capability, visual-led
4. Feature B       — secondary capability
5. How it works    — 3-step process
6. Testimonial     — one strong quote
7. Pricing         — 2–3 tiers
8. Final CTA + footer
```

4–10 sections is normal. Fewer than 4: probably fine to design; more than 10: cut.

### 2. Define the style-token block (before any image)

One consistent palette and type feel across ALL images is what makes the set look like one website. Write this block ONCE and paste it verbatim into every prompt:

```
STYLE TOKENS: [Site name / vibe in 5 words].
Background: [hex]. Surface: [hex]. Text: [hex]. Accent: [hex] (used for CTAs and highlights only).
Type: [display feel, e.g. "large tight grotesque headlines"] + [body feel].
Corners: [sharp | 8px rounded | pill buttons]. Density: [airy | balanced | compact].
Lighting/texture: [flat | soft gradients on background only | grain | glass].
```

Pick real hex values. If the user has a brand, extract from it; otherwise choose one deliberate palette (dark-on-light or light-on-dark — commit to one for the whole page, footer/CTA sections may invert).

### 3. Prompt each section

Use the template in `references/prompt-templates.md`. Every section prompt contains, in order: format line → STYLE TOKENS block → section content (exact headline and CTA text) → composition instruction → focal-action clause → cleanliness clause.

### 4. Review the set together

Lay out all generated images in section order and check: same palette everywhere ✱ same type feel ✱ no two adjacent sections with identical composition ✱ every headline readable and correctly spelled. Regenerate outliers with a corrected prompt — do not hand a developer an inconsistent set.

## Composition variety rules

The #1 tell of lazy AI comps: every section is left-text / right-image. Forbidden as a default.

- Across the set, use at least 4 distinct compositions. Rotate through: centered statement; left-text/right-visual; right-text/left-visual; full-bleed background image with overlaid text; asymmetric split (⅓–⅔); horizontal card row; alternating zigzag; big-number/stat layout; single centered quote.
- **No two consecutive sections may share the same composition.**
- Vary hero scale deliberately — choose one:
  - **Oversized statement**: headline spans ~80% of width, minimal supporting elements.
  - **Balanced**: headline + subline + CTA + one product visual.
  - **Minimal**: small centered type, huge negative space, one CTA.
- Backgrounds are free real estate: flat color, soft gradient, full-bleed photo, abstract texture — but stay inside the token block.

## Text in images

- Specify the EXACT headline, subheadline, button label, and 3–5 short labels per image. Unspecified text becomes garbage glyphs.
- Keep in-image copy short: headlines ≤ 8 words, body snippets ≤ 15 words. Long paragraphs will render as pseudo-text — that's acceptable ONLY for obvious body-copy areas; say "small placeholder body text" explicitly.
- Ask for readable sizes: "large legible headline typography, UI text crisp and readable". Reject images where the developer cannot read what a label says.

## Conversion awareness

Every section image needs one clear focal action or takeaway:

- Hero, pricing, final CTA → a visually dominant button with exact label ("Start free trial").
- Feature sections → the feature visual itself is the focus; at most a subtle text link.
- Social proof / testimonial → the proof element is the focus; no competing buttons.
- One PRIMARY accent-colored action per image, max. Secondary actions are ghost/outline. If a draft shows three equal buttons, regenerate.

## Cleanliness clause (append to every prompt)

"Clean modern web design, realistic proportions, consistent spacing, professional SaaS-quality UI, no watermark, no browser chrome, no lorem-ipsum walls, no duplicate buttons, text sharp and legible."

## Scope boundaries

- Mobile app screens → **imagegen-mobile**.
- Turning these images into HTML/CSS/React → **image-to-code**.
- This skill ends when the image set is generated and consistency-checked.
