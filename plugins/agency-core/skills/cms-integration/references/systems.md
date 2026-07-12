# CMS integration patterns per system

Practical patterns for the systems in the decision tree. Version specifics
change — verify current docs before scaffolding; these are the stable shapes.

## Payload (self-hosted, TypeScript, lives in your repo)

- **Fits:** Next.js projects; agencies wanting one repo, one deploy, full
  control; DSGVO-sensitive clients (data stays on your German/EU host).
- **Shape:** Payload runs inside the Next.js app (`@payloadcms/next`).
  Collections/globals as typed configs; generated types imported by the
  frontend. Postgres or MongoDB.
- **Pattern:** one Global per singleton surface (header, footer, contact
  data), one Collection per repeatable type (menu items, team, jobs, posts).
  Blocks field for section-based pages mirroring the design handoff sections.
- **Preview:** draft mode + Live Preview panel; wire `generatePreviewPath`.
- **Watch out:** migrations on schema changes; admin UI is part of YOUR
  deploy — include it in QA.

## Sanity (hosted, best-in-class editor UX)

- **Fits:** content-heavy sites, several editors, collaboration.
- **Shape:** Studio (self-hostable React app) + Content Lake (hosted; choose
  the EU dataset region for DACH clients). Query via GROQ.
- **Pattern:** schema types per handoff section; Portable Text for rich text
  (render with your own components — never raw HTML); image pipeline with
  hotspot/crop so editors can't break aspect ratios.
- **Preview:** Presentation tool / draft perspective with your frontend URL.
- **Watch out:** pricing tiers per seats/requests — put the plan in the
  proposal; free tier is fine for small sites.

## Storyblok (hosted, visual editor, EU option)

- **Fits:** marketing sites where non-technical editors compose page layouts
  from approved blocks; multilingual.
- **Shape:** components (bloks) map 1:1 to your frontend components; the
  visual editor renders your real site in an iframe with click-to-edit.
- **Pattern:** build the block library from the style-system components ONLY —
  editors compose, they don't style. Use presets for approved variants.
- **Watch out:** choose the EU server location at space creation (can't move
  later easily); iframe preview needs your dev/staging URL configured.

## Strapi (self-hosted, Node, REST/GraphQL)

- **Fits:** self-hosted requirement, separate backend team, custom roles.
- **Pattern:** content-types per handoff structure; components for repeatable
  section blocks; roles & permissions locked down before handover (public
  role = read-only on published content, nothing else).
- **Watch out:** admin customization is heavier than Payload; plan updates
  (Strapi major upgrades are real work — price them into the retainer).

## Decap CMS (free, git-based)

- **Fits:** small budgets, static sites, content as markdown in the repo.
- **Shape:** admin SPA at `/admin` editing markdown/YAML via git commits
  (works with any SSG; auth via GitHub/GitLab or Netlify Identity).
- **Pattern:** collections mirroring content files; strict widget config
  (string widgets with `pattern` for length limits).
- **Watch out:** no real preview without extra setup; media handling is
  basic; editors need a git-provider login — set this up FOR the client.

## Headless WordPress (WP admin + your frontend)

- **Fits:** clients who insist on the WP admin, or migrations where content
  and editor habits already live in WP.
- **Shape:** WP on managed/German hosting as content backend; WPGraphQL (or
  REST) feeding your frontend. ACF (+ ACF to WPGraphQL) for structured
  fields matching the handoff.
- **Pattern:** disable the WP frontend (headless mode), strip plugins to
  content-only ones, lock the editor to approved blocks (theme.json /
  block allowlist) so the design survives.
- **Watch out:** two systems to maintain and secure (WP updates! — retainer
  item); DSGVO: keep WP hosting in the EU, no default emoji/font CDN calls.

---

# Client handover checklist (any CMS)

- [ ] Roles configured: client editors CANNOT change schema/structure/design
- [ ] Every content type has a 1-page editor guide (client's language,
      screenshots, "do this / never this")
- [ ] 15-minute walkthrough done (record it — the video IS the documentation)
- [ ] Hostile-content QA pass done: longest headline, missing image, empty
      optional fields, oversized upload
- [ ] Preview flow works from the editor's seat (not just yours)
- [ ] Backup/restore path documented (who restores a deleted page, how fast)
- [ ] CMS + hosting + data location recorded in the privacy policy
      (pre-launch-checklist section A)
- [ ] Update responsibility named: who patches the CMS, on what cadence,
      billed how (→ MAINTAIN retainer)
