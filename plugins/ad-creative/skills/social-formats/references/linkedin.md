# LinkedIn — Placement Specs

Specs verified July 2026 — always spot-check platform docs before final export.
Sources: business.linkedin.com ad specs + adstellar.ai, stackmatix.com,
thebrief.ai spec roundups (retrieved 2026-07).

## Single Image Ads (Sponsored Content)

| Attribute | Spec |
|---|---|
| Ratios / px | 1.91:1 → 1200x627 (landscape); 1:1 → 1200x1200; 4:5 → 720x900 (vertical, mobile-only serving) |
| Formats | JPG, PNG, non-animated GIF |
| Max file size | 5 MB |
| Minimum | 400x400 px (not recommended) |
| Intro text | ≤ 150 chars before truncation (hard cap 600) |
| Headline | ≤ 70 chars |
| Description | ≤ 100 chars (shown mainly on LinkedIn Audience Network) |

## Video Ads

| Attribute | Spec |
|---|---|
| Ratios / px | 16:9 → 1920x1080; 1:1 → 1080x1080; 4:5 → 1080x1350; 9:16 vertical in select placements |
| Format | MP4 only |
| Max file size | 200 MB |
| Duration | 3 s – 30 min; 15–30 s recommended for awareness |
| Thumbnail | Required; JPG/PNG matching the video aspect ratio |
| Sound | Majority watched muted — burn in captions |

## Carousel Ads

| Attribute | Spec |
|---|---|
| Card size | 1080x1080 (1:1 only) |
| Cards | 2–10 |
| Max file size | 10 MB per card |
| Formats | JPG, PNG |
| Headline per card | ≤ 45 chars |
| Intro text | ≤ 255 chars |

## Document Ads

| Attribute | Spec |
|---|---|
| Formats | PDF, DOCX, PPTX |
| Max file size | 100 MB |
| Pages | ≤ 300 (under 10 recommended); landscape or portrait |
| Note | First 2–3 pages preview free — front-load the hook; text must be selectable for lead-gen gating |

## Text Ads (desktop right rail / top banner)

| Attribute | Spec |
|---|---|
| Thumbnail | 100x100 px, square only, JPG/PNG, ≤ 2 MB |
| Headline | ≤ 25 chars |
| Description | ≤ 75 chars |

## Dynamic / Spotlight Ads

| Attribute | Spec |
|---|---|
| Logo | 100x100 px |
| Background (optional) | 300x250 px |

## Stories

LinkedIn Stories was discontinued 2021-09-30. Several third-party posts report a
Stories-style relaunch in early 2026, but as of this retrieval there is NO official
LinkedIn announcement and NO published ad spec for it — treat as unverified. Check
Campaign Manager for an actual Stories placement before promising it in a media plan;
if present, expect standard 9:16 / 1080x1920 vertical.

## Safe zones & text density

- No OS-level UI overlays on feed assets — safe zones are mild; keep 60–80 px edge
  margin so feed rounding/cropping doesn't clip text.
- LinkedIn tolerates more on-image and body copy than Meta/TikTok, but truncation
  points (150-char intro, 70-char headline) still decide what's seen.
- 4:5 vertical image serves mobile only — always pair with a 1:1 or 1.91:1 fallback.

## 2025/2026 changes noted

- 4:5 (720x900) vertical single-image and 9:16 video in select placements reflect
  LinkedIn's ongoing shift toward mobile-vertical inventory.
- Reported Stories relaunch (unverified — see above).
