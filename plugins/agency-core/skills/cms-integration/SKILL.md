---
name: cms-integration
description: Choose and integrate the right CMS for a client website — decision tree (client editing needs, budget, hosting, stack) plus integration patterns for Payload, Sanity, Storyblok, Strapi, Decap, and headless WordPress, and a client-handover checklist. Use when the user asks "which CMS", "add a CMS", "the client wants to edit content themselves", "Kunde soll Inhalte selbst pflegen", "WordPress or something modern", "headless CMS", or when the BUILD phase reveals editable content requirements. Covers selection, modeling content from the design handoff, preview setup, and editor training. NOT for building the site's frontend (BUILD phase skills), NOT for content strategy or SEO content (seo-content), NOT for one-off static sites where nothing needs client editing — recommending "no CMS" is a valid outcome of this skill.
---

# CMS Integration

Most client sites need SOME editable content — and most agencies either
over-engineer (full CMS for two text fields) or under-engineer (client calls
you for every typo). This skill picks the right tier and integrates it without
breaking the design handoff.

## Step 1 — Establish what actually needs editing

Before naming any system, list the editable surfaces from the brief/concept:

- Which content changes, how often, and by whom? (opening hours weekly ≠
  legal pages yearly)
- Structured data (menu items, team members, jobs) or free-form pages?
- Does the client add PAGES, or only edit content within existing ones?
- Media uploads? Multilingual? Scheduled publishing? Multiple editors/roles?

If the honest answer is "a phone number and opening hours twice a year" —
recommend **no CMS**: keep content in typed config/content files, offer a
maintenance retainer instead. Say this explicitly; it's often the right call.

## Step 2 — Decision tree

| Situation | Recommendation |
|---|---|
| Few fields, rare edits, technical-ish client | **No CMS** (content files + retainer) |
| Git-based site, budget-sensitive, simple editing | **Decap CMS** (free, edits commit to the repo) |
| Next.js project, client edits structured content, self-hosted preferred | **Payload** (TypeScript-native, lives in the repo, DSGVO-friendly self-hosting) |
| Content-heavy, multiple editors, real-time collaboration, budget exists | **Sanity** (hosted, excellent editor UX, GROQ) |
| Marketing team edits page LAYOUTS (visual composition), multi-language | **Storyblok** (visual editor, EU-hosted option) |
| Client insists on the WordPress admin they know / migration from WP | **Headless WordPress** (WP admin + REST/WPGraphQL, frontend stays yours) |
| Self-hosted requirement + non-JS backend team | **Strapi** |

DACH note: for DSGVO-sensitive clients, prefer self-hosted (Payload, Strapi,
Decap, WP on German hosting) or EU-region SaaS (Storyblok EU, Sanity EU
dataset) — and record the choice + data location in the privacy policy via
`pre-launch-checklist`.

## Step 3 — Integration rules

1. **Model content FROM the handoff, not from the CMS's defaults.** Every
   design section that contains editable content becomes a typed
   block/document with exactly the fields the design needs — no generic
   "rich text everything" fields that let editors break the layout.
2. **Constrain the editor.** Character limits matching the design (headline
   lengths!), image fields with required aspect ratios, no free-form color or
   font options. The design system survives editors only if the schema
   enforces it.
3. **Preview before publish.** Wire draft preview (framework preview mode or
   the CMS's preview URL) so the client sees changes in the real design.
4. **Keep the frontend the source of truth for presentation.** CMS delivers
   content; components decide rendering. Never store HTML/CSS in the CMS.
5. **Plan the QA impact.** CMS-driven pages need one extra QA pass with
   deliberately hostile content: longest realistic headline, missing image,
   empty optional field. See per-system patterns and the handover checklist
   in [references/systems.md](references/systems.md).

## Step 4 — Handover

A CMS without editor training is a support contract you didn't price. Deliver:
a 1-page editor guide per content type (in the client's language), a 15-minute
walkthrough, and a named fallback contact. Details + checklist in
[references/systems.md](references/systems.md).
