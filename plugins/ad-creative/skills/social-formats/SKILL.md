---
name: social-formats
description: Authoritative ad and content format specifications for Meta/Facebook, Instagram, TikTok, LinkedIn, and YouTube, plus a workflow for adapting one master creative into every placement a media plan requires. Use when the user wants to adapt for social, resize for all platforms, or asks about social media formats, Instagram format, TikTok ad specs, LinkedIn or YouTube ad dimensions, safe zones, aspect ratios, file size or video length limits, or says "export the campaign assets" or "Formate anpassen". This skill covers FORMATS and ADAPTATION (dimensions, crops, safe zones, export naming) — not ideation (see ad-concepts) and not copywriting (see ad-copy).
license: MIT (c) GEKKOS Tech
---

# Social Formats — Spec Reference & Adaptation Workflow

Turn ONE master creative into every format the media plan needs, without UI overlap,
bad crops, or spec rejections. Specs verified July 2026 — always spot-check platform
docs before final export.

## Reference files (verified spec tables)

| File | Covers |
|---|---|
| `references/meta-instagram.md` | Facebook Feed, Stories, Reels, Right Column, Marketplace, Carousel; Instagram Feed, Stories, Reels, Explore, Carousel |
| `references/tiktok.md` | In-Feed, TopView, Spark Ads, image/carousel |
| `references/linkedin.md` | Single image, video, carousel, document ads, text ads, Stories status |
| `references/youtube.md` | Shorts, skippable/non-skippable in-stream, bumper, thumbnails, banner |

Load only the reference file(s) for the platforms actually in the media plan.

## Adaptation workflow

### Step 1 — Establish the master creative

Start from ONE master in the richest format you will need:

- **Video-led campaign** → master at **9:16, 1080x1920** (covers Stories, Reels,
  TikTok, Shorts natively; center-crop to 4:5 / 1:1 / 16:9).
- **Static/feed-led campaign** → master at **4:5, 1080x1350** (crops cleanly to 1:1;
  extend background to reach 9:16 — never stretch).

Master rules: build at final pixel size or larger (never upscale), keep the subject
and core message inside a **center 1:1 zone** so every derived crop keeps the story,
keep logo/CTA on separate layers so they can be repositioned per placement.

### Step 2 — Derive the format matrix from the media plan

For each platform+placement in the media plan, read the matching reference file and
list: ratio, px, max file size, max duration, safe zone. The output is a checklist
table — one row per required export. Do not export formats the plan doesn't buy.

Minimum typical matrix from one master pair (4:5 + 9:16):

| Ratio | Px | Serves |
|---|---|---|
| 9:16 | 1080x1920 | FB/IG Stories & Reels, TikTok, YouTube Shorts |
| 4:5 | 1080x1350 | FB/IG Feed |
| 1:1 | 1080x1080 | Carousels, Marketplace, Right Column, LinkedIn |
| 16:9 | 1920x1080 | YouTube in-stream, LinkedIn video |

### Step 3 — Apply safe-zone rules per placement

Safe zones are where platform UI (username, captions, CTA buttons, nav) overlays the
creative. Exact pixel values are in each reference file. Universal rules:

1. Nothing critical in the top ~14% or bottom ~20–35% of any 9:16 asset.
2. On TikTok, additionally keep the right edge clear (like/comment/share rail).
3. Subtitles sit in the vertical center band, never in the bottom caption zone.
4. Logos: top-center or center — never bottom corners on vertical formats.
5. Design the 9:16 knowing IG grid previews crop to 3:4 — keep faces/claims inside.

### Step 4 — Apply text-density rules per platform

- **Meta/IG**: the 20% text rule is retired but text-heavy stills still underperform;
  headline on-image ≤ 7 words; design sound-off (captions burned in, safe-zone aware).
- **TikTok**: native look wins — minimal overlay text, hook in first 2 s, caption
  ≤ 100 chars (only ~40–50 show before "See more").
- **LinkedIn**: more copy tolerated; intro text ≤ 150 chars before truncation,
  headline ≤ 70 chars; keep on-image text legible at feed size.
- **YouTube**: thumbnails ≤ 3–4 words; in-stream must communicate brand + message in
  the first 5 s (skip button appears at 5 s on skippable).

### Step 5 — Export with the naming convention

```
{campaign}-{platform}-{placement}-{WxH}.{ext}
```

Examples: `spring26-meta-reels-1080x1920.mp4`, `spring26-linkedin-carousel-1080x1080-card03.jpg`,
`spring26-youtube-bumper-1920x1080.mp4`. Lowercase, hyphens only, no spaces or
umlauts; append `-cardNN` for carousel cards and `-vNN` for variants.

### Step 6 — Pre-handoff checklist

- [ ] Every media-plan placement has exactly one matching export (no orphans, no gaps)
- [ ] Each file is at or under the platform max file size; videos within duration limits
- [ ] Safe zones verified against the reference tables (overlay a safe-zone template)
- [ ] No upscaled/soft assets; video is H.264 MP4 unless the spec says otherwise
- [ ] Captions/subtitles burned in and positioned inside the safe band
- [ ] Naming convention applied consistently; carousel card order encoded in filename
- [ ] Spot-checked at least one spec per platform against current official docs
- [ ] Thumbnails/poster frames set for every video placement that supports them

## Boundaries

- **ad-concepts** owns ideation (what the creative says/shows).
- **ad-copy** owns copywriting (headlines, primary text, CTAs as language).
- **social-formats** (this skill) owns dimensions, crops, safe zones, limits, export
  naming, and the adaptation pipeline from master to placement-ready assets.
