# Mobile Screen Prompt Templates

Fill the brackets. Paste the flow's APP TOKENS block verbatim into every prompt.

## Master template (any screen)

```
Premium [iOS | Android] app screen concept, portrait, single screen shown
inside a minimal dark phone frame on a quiet [hex] studio background,
screen content fills the frame edge to edge.

APP TOKENS: [paste the flow's token block verbatim]

SCREEN: [name] — [image-led | control-led].
Status bar at top; [tab bar with icons: [list 4–5] , "[active item]" active in accent
| no tab bar, back chevron + title "[X]" at top].

CONTENT (top to bottom):
- [element 1, e.g. large title "Today"]
- [element 2, e.g. hero metric "12,430" with small label "steps"]
- [element 3, e.g. horizontal row of 3 rounded cards: "[A]", "[B]", "[C]"]
- [element 4, e.g. list of 3 rows, each: thumbnail, "[title]", "[value]"]
- [primary action: pill button "[exact label]" in accent | FAB bottom right]

All visible text exactly as specified, comfortably readable, three type tiers max.
Content respects safe areas. Clean premium app UI, consistent [radius] corners,
[icon style] icons, no watermark, no extra buttons, no garbled text.
```

## Archetype variants

**Image-led screen** — insert as the top of CONTENT:
```
- full-width [photo/illustration subject] filling the top 50% of the screen,
  [style matching token mood], title "[X]" overlaid bottom-left in white
```
Below the image keep UI sparse: 2–3 elements max.

**Control-led screen** — no hero image. Structure with cards and lists; let one number or one chart be the visual anchor: `- clean [line/bar/ring] chart in accent color, minimal gridlines`.

## Per-screen notes

**Onboarding / welcome** — image-led. `centered brand moment: [illustration/photo], app name, one-line promise "[exact]", single button "[Get started]"`. No tab bar.

**Home / dashboard** — control-led. Big greeting or metric up top, 2–3 content modules, tab bar. This screen defines the app's identity — spend the most iterations here.

**Core action** (book / send / scan / track) — the accent color's big moment: one dominant control (large input, camera viewfinder, map, slider) + one confirm button. Everything else recedes.

**Detail view** — usually image-led for content apps, control-led for finance/tools. Back chevron, one hero element, key facts as label/value rows, one primary action.

**Stats / history** — control-led. One chart as anchor, segmented control ("Week / Month / Year"), short list below.

**Profile / settings** — control-led, quiet. Avatar + name, grouped list rows with chevrons. No accent flooding.

## Consistency add-on (screens 2+)

After the first screen looks right, add to every subsequent prompt:

```
Same app as previous screens: identical palette, identical tab bar,
identical icon style, identical corner radius and type treatment.
```

(Models don't see previous images — this line plus the verbatim token block is what does the work. If the model supports image references, also pass the approved first screen as a style reference.)

## Regeneration fixes

| Symptom | Add to prompt |
|---|---|
| Garbled labels | fewer elements, every word listed explicitly, "text sharp and readable" |
| New random color appeared | "strictly limited palette: [hexes] only, no additional hues" |
| Tab bar differs from other screens | list tab items + active state explicitly again |
| Looks like a website | "native mobile app UI, portrait phone screen, bottom tab bar" |
| Frame dominates the image | "phone frame thin and subtle, screen content fills 80% of image" |
| Cluttered | "reduce to [N] elements, generous vertical spacing" |
| Wrong platform feel | restate platform + its conventions (tab bar vs FAB, title style) |
