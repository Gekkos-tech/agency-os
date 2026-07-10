# TikTok — Placement Specs

Specs verified July 2026 — always spot-check platform docs before final export.
Sources: TikTok Ads Help Center (ads.tiktok.com) + admanage.ai, tryvizup.com,
adnabu.com spec roundups (retrieved 2026-07).

## In-Feed Ads (auction)

| Attribute | Spec |
|---|---|
| Aspect ratio | 9:16 vertical (recommended); 1:1 and 16:9 technically accepted but underperform (letterboxed) |
| Resolution | 1080x1920 recommended; minimums 540x960 (V), 640x640 (1:1), 960x540 (H) |
| Duration | up to 10 min supported (ceiling raised from 60 s); 9–15 s recommended, ≤ 30 s sweet spot |
| File size | ≤ 500 MB |
| Formats | .mp4, .mov (.mpeg, .3gp, .avi accepted) |
| Ad caption | ≤ 100 chars; only ~40–50 visible before "See more"; hashtags/@ NOT clickable |
| Display name | 2–20 Latin chars |
| Profile image | 98x98 px, < 50 KB |

## TopView

| Attribute | Spec |
|---|---|
| Aspect ratio | 9:16 vertical ONLY |
| Resolution | 1080x1920 recommended (min 540x960) |
| Duration | 5–60 s; 9–15 s recommended; ~3 s full-screen takeover then transitions in-feed |
| File size | ≤ 500 MB |
| Safe zones | Must satisfy BOTH open-screen and in-feed safe zones (see below); keep top and bottom ~120 px extra clear during takeover phase |

## Spark Ads (boosted organic posts)

| Attribute | Spec |
|---|---|
| Source | Existing organic post (own or authorized creator) |
| Ratio/duration | Inherits organic limits — 9:16 typical, > 60 s supported |
| Caption | ~100 chars; hashtags and @mentions REMAIN clickable (unlike non-Spark) |
| Note | Creative cannot be edited after authorization — the post is the ad |

## Image ads (Global App Bundle / Pangle placements)

| Attribute | Spec |
|---|---|
| Ratio | 9:16 or 1:1 |
| Resolution | 1080x1920 / 720 px+ minimum |
| Formats | .jpg, .png |
| File size | keep ≤ 500 KB (≈100 KB ideal); brand-takeover-style statics historically ≤ 50 KB |
| Note | Image ads do not serve in the main For You feed — app-network placements only |

## Carousel Ads

| Attribute | Spec |
|---|---|
| Cards | 2–35 images (limit raised from 10); 2–10 recommended |
| Ratio | 9:16 or 1:1, consistent across cards |
| Resolution | 720 px+ minimum per image |
| File size | ~100 KB per image recommended, ≤ 500 KB |
| Formats | .jpg, .png; emojis not supported in carousel text |

## Safe zones — 9:16 (1080x1920 canvas)

| Edge | Keep clear | UI element |
|---|---|---|
| Top | ~120–160 px | Status area, "Following / For You" tabs |
| Bottom | ~378–440 px | Caption, CTA button, music ticker, nav bar |
| Right | ~108–180 px | Like / comment / share / profile rail |
| Left | ~44–80 px | Margin |

Practical rule: keep all text, logos, product shots in the center ~60% of the frame;
subtitles above the caption block, never behind the right-side rail.

## Text & creative recommendations

- Hook in the first 2 seconds; sound ON is the norm (unlike Meta) but caption anyway.
- Native, UGC-style creative outperforms polished ad-look assets.
- Shoot native 9:16; never letterbox a 16:9 master into TikTok.

## 2025/2026 changes noted

- In-feed video ceiling raised from 60 s to 10 min (non-Spark).
- Carousel limit raised to 35 images.
- Video Shopping Ads replaced the older Collection Ads format.
