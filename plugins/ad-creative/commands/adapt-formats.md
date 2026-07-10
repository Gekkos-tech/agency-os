---
description: Adapt a master creative into all needed social/ad formats with correct specs and safe zones
argument-hint: [master asset path/description + target platforms]
---

Adapt creative to platform formats: $ARGUMENTS

Load the `social-formats` skill and:

1. Identify the master creative (asset path or description) and the target
   platforms/placements — if platforms weren't specified, ask once, or
   derive them from the campaign's channel plan in `docs/`.
2. Build the **format matrix**: one row per placement with ratio, pixel
   dimensions, max length/size, and safe-zone notes from the platform
   references.
3. For each target format, specify the adaptation: crop/extend strategy,
   what moves out of unsafe zones, text-density adjustments per platform
   norms.
4. Output the export list with the naming convention
   `{campaign}-{platform}-{placement}-{WxH}` and the pre-handoff checklist.

Where image generation/editing tools are available, offer to produce the
adapted assets; otherwise deliver the matrix as the production brief.
