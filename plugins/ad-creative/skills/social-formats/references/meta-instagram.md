# Meta / Facebook & Instagram — Placement Specs

Specs verified July 2026 — always spot-check platform docs before final export.
Sources: Meta Ads Manager guidance + get-ryze.ai, superscale.ai, adsuploader.com,
buffer.com, admanage.ai spec roundups (retrieved 2026-07).

## Global file limits (all Meta placements)

| Asset | Formats | Max size | Notes |
|---|---|---|---|
| Image | JPG, PNG | 30 MB | Target < 5 MB (JPEG q80–90) for load speed |
| Video | MP4, MOV (H.264) | 4 GB | Target < 100 MB, 5–10 Mbps; 1 s – 241 min |

Old 20% text-overlay rule officially removed, but text-heavy creatives still get
algorithmically deprioritized. Design sound-off first.

## Facebook placements

| Placement | Ratio | Recommended px | Length | Notes |
|---|---|---|---|---|
| Feed (image/video) | 4:5 (best) or 1:1 | 1080x1350 / 1080x1080 | video ≤ 241 min; ≤ 15 s optimal | 4:5 takes ~20% more screen than 1:1 |
| Stories | 9:16 | 1080x1920 | ≤ 15 s per card optimal | Full-screen vertical |
| Reels | 9:16 | 1080x1920 | up to 90 s (raised from 60 s) | Same asset as Stories |
| Right Column (desktop) | 1:1 | 1080x1080 (min 254x133) | image only | Old 1.91:1 deprecated → 1:1 standard |
| Marketplace | 1:1 | 1080x1080 | — | Image or video |
| Carousel | 1:1 only | 1080x1080 per card | 2–10 cards | Never feed 4:5 into carousel — Meta crops to 1:1 |
| In-stream video | 16:9 or 1:1 | 1920x1080 | 5–15 s optimal | Brand in first 3 s |

## Instagram placements

| Placement | Ratio | Recommended px | Length | Notes |
|---|---|---|---|---|
| Feed square | 1:1 | 1080x1080 | video ≤ 60 min | Safest cross-placement asset |
| Feed portrait | 4:5 | 1080x1350 | — | Best feed performer 2026 |
| Stories | 9:16 | 1080x1920 | ≤ 15 s per card optimal | |
| Reels | 9:16 | 1080x1920 | ads up to 90 s | Grid preview crops to 3:4 |
| Explore | 1:1 or 4:5 | 1080x1080 / 1080x1350 | — | Rendered from feed asset |
| Carousel | 1:1 (4:5 supported organic) | 1080x1080 | 2–10 cards (ads) | Keep all cards same ratio |

## Safe zones — 9:16 Stories/Reels (1080x1920 canvas)

| Zone | Pixels | ~% | UI element |
|---|---|---|---|
| Top — keep clear | 0–250 px | 14% | Profile icon, name, audio tag |
| Safe band | 250–1248 px | 51% | Put ALL key text/logo/product here |
| Bottom — keep clear | 1248–1920 px | 35% | CTA button, caption, reply bar |

Side margins: keep ~60–87 px (6%) clear left and right.

## Safe zones — Feed & grid

- Feed 4:5 / 1:1: keep text and logos 90–120 px from every edge.
- Instagram profile grid crops previews to **3:4** — keep faces, claims, and logos
  inside the 3:4 center crop of any feed or Reels asset.

## Text recommendations

| Field | Recommended | Truncation |
|---|---|---|
| Primary text | ≤ 125 chars | "See more" after ~125 |
| Headline | ≤ 40 chars (5–7 words on-image) | ~27–40 visible |
| Description | ≤ 30 chars | link placements only |

## 2025/2026 changes noted

- Reels ads extended to 90 s on both Facebook and Instagram.
- Right Column standardized to 1:1; 1.91:1 deprecated.
- Instagram grid preview moved from 1:1 to 3:4 crop — new grid safe zone.
- 20% text rule formally retired.
