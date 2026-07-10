---
name: brandkit
description: Art direction for generating premium brand identity imagery with AI image models — brand-guideline boards, logo concept sheets, identity decks, and visual-world moodboards. Use when the user asks for a "brand kit", "logo concepts", "brand guidelines board", "identity deck", "moodboard", "visual identity", or wants a full brand presented as polished images. Derives a symbolic brand concept before any prompting, then produces restrained, gallery-grade boards with grid layouts, logo lockups, hex-labeled color swatches, type specimens, and business-matched mockups. Generates images only; it does not write code.
---

# Brand Kit — Premium Identity Image Direction

Direct an AI image model to produce brand identity imagery that looks like the work of a top-tier design studio, not a template generator. The output is a set of images: guideline boards, logo sheets, moodboards, mockup tiles.

**Iron law: concept before prompt.** Never generate a single image until you have written down the brand concept. A prompt without a concept produces generic "AI branding" — gradient blobs, meaningless geometric marks, ten fonts fighting each other.

## Step 1 — Derive the brand concept

Before prompting, answer these four questions in writing (2–4 sentences total). Ask the user only if the answers cannot be inferred from context.

1. **Symbol** — What ONE visual idea carries the brand? (a form, a letter construction, a natural object, a geometric operation). One symbol. Not three.
2. **Meaning** — Why that symbol? What does it say about what the company does or believes? If you cannot state the meaning in one sentence, pick a different symbol.
3. **Personality** — Three adjectives, ordered by priority (e.g. "precise, calm, quietly confident"). These drive every later vocabulary choice.
4. **Register** — Pick exactly ONE aesthetic register from `references/registers.md` (minimal, cinematic, editorial, dark-tech, luxury, playful-consumer). The register supplies the prompt vocabulary; do not mix registers within one brand kit.

Write the concept as a short block and reuse it verbatim at the top of every prompt in the set. This is what keeps a 6-image kit looking like one brand.

```
BRAND CONCEPT: [name] — [symbol] representing [meaning].
Personality: [adj1], [adj2], [adj3]. Register: [register].
Palette: [1 base + 1–2 neutrals + max 1 accent, with hex].
Type feel: [e.g. "grotesque sans, tight tracking, lowercase wordmark"].
```

## Step 2 — Plan the deliverable set

A standard kit is 4–8 images. Choose from:

| Board | What it shows |
|---|---|
| Logo concept sheet | 3–6 mark explorations of the SAME symbol idea, black on white |
| Primary guideline board | Hero board: lockup, palette, type, one mockup, in a grid |
| Color & type board | Swatches with hex labels + type specimen lines |
| Visual-world moodboard | Photography/texture direction, no logos, 6–9 tiles |
| Mockup tiles | The identity applied to 1–2 real objects per image |
| Icon / app-mark board | The mark reduced to favicon and app-icon sizes |

Do not generate all of these by default. Match the set to the request: "logo concepts" = concept sheet + one guideline board; "full brand kit" = 5–6 boards.

## Step 3 — Prompt structure for guideline boards

Build every board prompt in this order:

1. **Format line** — "Premium brand guidelines board, clean grid layout, [aspect ratio, usually 16:9 or 4:3], flat graphic design presentation, studio quality."
2. **Concept block** — paste the BRAND CONCEPT block.
3. **Grid contents** — enumerate the cells explicitly. Image models compose far better when told exactly what sits where:
   - "Top left: primary logo lockup, large, generous margin."
   - "Top right: logotype-only variant."
   - "Middle row: four color swatches as flat rectangles, each labeled with its hex code in small monospaced text ([#0A0A0A], [#F4F1EA], …)."
   - "Bottom left: type specimen — the brand name set large, plus one line of alphabet sample and one paragraph of small placeholder text."
   - "Bottom right: one photographic mockup tile ([chosen mockup])."
4. **Register vocabulary** — 5–10 keywords pulled from `references/registers.md` for the chosen register.
5. **Restraint clause** — always end with: "Sparse typography, only the brand name and short labels as text. Large negative space. One symbolic idea. No decorative clutter, no random icons, no lorem-ipsum walls, no watermark."

Keep in-image text minimal and specify it exactly (brand name, tagline if any, hex codes). Every word you don't specify is a word the model will misspell.

## Step 4 — Logo concept sheets

- Prompt for **variations of one idea**, not six unrelated logos: "Six variations of a [symbol] mark: outlined, filled, negative-space cut, contained in a circle, deconstructed, combined with the letter [X]."
- Black marks on white (or single accent on near-black for dark-tech). Never rainbow sets.
- "Flat vector style, precise geometry, even stroke weights, presented in a 2×3 grid with generous spacing, each mark the same visual size."
- Add the brand name in small text under each mark — nothing else.

## Rules of restraint (apply to every image)

- ONE symbolic idea per brand. If a draft board shows two competing motifs, regenerate.
- Max 2 typefaces implied (one display feel, one text feel). Describe the *feel*, not font names — models render feels more reliably.
- Palette: 1 base, 1–2 neutrals, max 1 accent. List hex codes in every prompt.
- Negative space is a feature. Ask for "generous margins", "airy composition", "gallery presentation".
- Forbid by default: gradients on logos (unless register calls for it), drop shadows, bevels, mockups with hands, busy backgrounds behind logo lockups, more than ~15 words of visible text per board.

## Mockup selection — match the business

Pick mockups the business would actually print or ship. Wrong mockups instantly cheapen a kit.

| Business type | Good mockups | Avoid |
|---|---|---|
| SaaS / dev tool | app icon, dark laptop screen, conference lanyard, terminal window | wine bottles, storefront awnings |
| Agency / studio | business card, letterhead, portfolio cover, tote | app store screenshots |
| Restaurant / café | menu, cup sleeve, signage, apron | letterheads, lanyards |
| Fashion / luxury | embossed box, hangtag, shopping bag, foil card | mugs, pens |
| Local service / trade | van livery, uniform patch, yard sign, invoice header | perfume boxes |
| Consumer app | app icon on home screen, social avatar, billboard | stationery suites |

1–2 mockups per image, described physically: "matte black business card with blind-debossed mark, soft top-light, shallow depth of field".

## Quality gate before delivering

For each generated image, check: single readable symbol ✱ correct palette (spot-check against hex list) ✱ text legible and correctly spelled ✱ negative space present ✱ consistent with the other boards in the set. Regenerate any image that fails — never deliver an off-concept board because it "looks nice".

See `references/registers.md` for the full vocabulary of each aesthetic register.
