---
name: imagegen-mobile
description: Art direction for generating premium mobile app screen concepts for iOS and Android with AI image models. Use when the user asks for "app screen designs", "mobile UI concepts", "app mockups", "design the app screens", or wants a visual concept of a mobile product or app flow. Produces one screen per image inside a subtle premium phone-frame mockup, with a shared token block (palette, type, radius, iconography) enforcing consistency across the whole flow, platform-correct navigation patterns, and a planned 4–8 screen story. Generates images only; it does not write code. Not for website sections (use imagegen-web).
---

# Mobile App Screen Concepts

Generate app screen images that look like a real, premium iOS/Android product — one screen per image, consistent across the whole flow, buildable by a developer who has never seen the brief.

## Core rules

1. **One screen per image.** Never a grid of 6 tiny screens in one image — text becomes noise and layouts get invented. A 6-screen flow = 6 images.
2. **Phone-frame mockup, subtle.** Each screen sits inside a minimal premium phone frame (thin dark bezel, rounded corners, slight presentation margin on a quiet studio background). The frame signals "mobile" and hides edge artifacts — but the app content is the star: the screen fills ~80% of the image. Portrait orientation, ~9:16 to 3:4 image ratio.
3. **The whole flow shares one token block.** Consistency across screens is the difference between "an app" and "six random dribbble shots".

## Workflow

### 1. Plan the flow — which screens tell the product story?

Pick 4–8 screens that together explain what the app does and why it feels good. Default story arc:

```
1. Onboarding / welcome   — brand moment, one-line promise
2. Home / dashboard        — the daily view; the app's identity screen
3. Core action             — the ONE thing users do (book, track, send, scan)
4. Detail view             — one item opened (product, workout, transaction)
5. Secondary value screen  — stats / history / social / library (pick one)
6. Profile or settings     — only if it shows something distinctive
```

Cut screens that don't add to the story (generic login, empty settings). If the user names specific screens, use theirs. Order matters — present the set in flow order.

### 2. Write the token block once, reuse everywhere

Paste this verbatim into EVERY screen prompt:

```
APP TOKENS: [app name] — [one-line concept]. Platform: [iOS | Android].
Background: [hex]. Surface/card: [hex]. Text: [hex]. Accent: [hex] (primary actions only).
Type: [e.g. "clean geometric sans, bold large titles, quiet small labels"].
Corner radius: [e.g. 16px cards, pill buttons]. 
Icons: [e.g. "thin-line minimal icons, 1.5px stroke"] — same style on every screen.
Mood: [3 adjectives]. Frame: minimal dark phone frame on [quiet background hex].
```

Choose light or dark mode for the WHOLE flow — never mix. Palette discipline: background + surface + text + ONE accent (+ optional semantic green/red for finance/health data). If a generated screen introduces a new color, regenerate.

### 3. Classify each screen, then prompt it

Two screen archetypes — pick one per screen and say so in the prompt:

- **Image-led** (onboarding, content feeds, travel/food/fitness detail): a large photo or illustration dominates the top ~50%, UI floats below or overlays it. Gives the flow its emotional screens.
- **Control-led** (dashboard, forms, lists, settings, checkout): typography, cards, and controls carry the screen; images at most as small thumbnails. Gives the flow its credibility screens.

A good set mixes both — roughly ⅓ image-led, ⅔ control-led. Six control-led screens = sterile; six image-led = vaporware.

Use the full template in `references/prompt-templates.md`.

## Platform conventions (get these right or it reads fake)

**iOS feel:**
- Status bar at top (time left, signal/wifi/battery right); home indicator bar at bottom.
- Bottom tab bar with 4–5 items, thin-line icons + tiny labels; active item in accent.
- Large left-aligned screen title on top-level screens; back chevron + title on pushed screens.
- Cards and sheets with generous radius; grouped list styling for settings.

**Android (Material) feel:**
- Status bar + gesture bar; bottom navigation bar (3–5 items) or nav rail.
- Possible FAB (one round accent button, bottom right) for the core action.
- Top app bar on secondary screens.

Safe areas: keep content clear of the status bar, notch area, and home-indicator zone — say "content respects safe areas, nothing cropped by the notch". Tab bar identical (same icons, same active-state logic) on every screen that shows it.

## Type hierarchy and readability

- Specify exact visible text: screen title, section headers, 3–6 labels, button text, and key data values ("$1,248.60", "12,430 steps"). Unspecified text = garbage glyphs.
- Three tiers max per screen: one big title, medium card/section titles, small labels/values. "Comfortably readable text, generous line spacing, no dense text walls."
- Numbers are heroes in dashboards: "the main metric displayed extra large".
- Reject any image where a developer can't tell what a label says.

## Quality gate for the set

View all screens side by side in flow order and verify: identical palette and mode ✱ identical tab bar (where present) ✱ same icon style and radius language ✱ same type feel ✱ platform conventions consistent ✱ every screen's ONE primary action obvious. Regenerate any outlier — one inconsistent screen breaks the illusion of a real app.

## Scope boundaries

- Website/landing sections → **imagegen-web**.
- Implementing screens as code → out of scope; this skill delivers images only.
