---
name: agency-workflow
description: The agency project router — orchestrates the full client-project lifecycle BRIEF → CONCEPT → DESIGN → BUILD → QA → LAUNCH plus the post-launch MAINTAIN loop, and tells Claude which specialist skill to load at each phase. Use this skill whenever a client web project starts or advances — trigger on "new project", "neues Projekt", "website for a client", "Website für Kunde/Kunden", "Kundenprojekt starten", "start a client project", "we won a pitch", "relaunch for", "where does the project stand", "wo steht das Projekt", or any request to plan, kick off, continue, or maintain a client website, landing page, or web app — even if the user only describes the client and goal ("a website for a café in Cologne"). This skill routes, enforces phase gates, and keeps docs/project-state.md current; the actual design/build/QA work happens in the specialist skills it delegates to.
---

# Agency Workflow

The project spine for web agencies. Every client project moves through six
phases. This skill decides **which phase you are in**, **which specialist
skill to load**, and **which gate must pass before the next phase**. It never
does the specialist work itself — it routes.

## Operating principles

1. **Plan before code.** No production code before the plan for that increment
   is stated and (for client work) approved. State what will be built, from
   which design source, touching which files.
2. **One source of truth for design.** If a design handoff exists (design
   images, a style guide, a token file, a Figma export), it IS the design —
   never regenerate colors/typography/layout that the handoff already defines.
   Quality skills then act as reviewers, not generators. Only without a
   handoff may a design system be generated fresh.
3. **Scope discipline.** Do what the current phase requires, nothing from a
   later phase. Surface scope changes instead of silently absorbing them.
4. **Every phase has an exit gate.** Do not advance until the gate checklist
   for the phase passes (see the phase reference files).

## Phase detection

**Check `docs/project-state.md` first** — if it exists, it names the current
phase, open blockers, and what the client owes; trust it over re-derivation.
If it's missing or stale, classify from project signals:

| Signal | Phase |
|---|---|
| New client/goal mentioned, no brief document yet | **BRIEF** |
| Brief exists; no sitemap/direction/offer yet | **CONCEPT** |
| Concept approved; no visual design/handoff yet | **DESIGN** |
| Design source exists; code missing or incomplete | **BUILD** |
| Feature-complete; not yet verified | **QA** |
| QA passed; not yet live / launch requested | **LAUNCH** |
| Site is live; monitoring, updates, reports, "did anything break" | **MAINTAIN** |

If the user's request names a later phase but earlier gates never happened
(e.g. "build the site" with no brief), do a compressed pass of the earlier
phases first — a 5-line mini-brief beats none — and say so.

## Routing table

Load the phase reference for the current phase, then delegate to the listed
specialist skills **if they are installed**; degrade gracefully to the
reference file's inline guidance if not.

| Phase | Reference | Delegate to (when installed) |
|---|---|---|
| BRIEF | [references/brief.md](references/brief.md) | — (interview + document, done here) |
| CONCEPT | [references/concept.md](references/concept.md) | `taste` (creative direction), `awesome-design-md` (brand reference), `ad-concepts` (campaign angle) |
| DESIGN | [references/design.md](references/design.md) | `style-systems` (commit to one system), `ui-ux-pro-max` (palettes/fonts/UX rules), `imagegen-web` / `imagegen-mobile` (design reference images), `brandkit` (identity assets) |
| BUILD | [references/build.md](references/build.md) | `image-to-code` (from design images), `gsap-suite` (motion), `threejs-webgl` / `react-three-fiber` (3D), `interface-polish` (final feel), `complete-output` (no truncation), `karpathy-guidelines` (code discipline) |
| QA | [references/qa.md](references/qa.md) | `performance`, `core-web-vitals`, `accessibility`, `best-practices`, `webapp-testing`, `redesign` (if quality bar missed) |
| LAUNCH | [references/launch.md](references/launch.md) | `pre-launch-checklist` (legal/technical launch gate), `seo-audit` or installed SEO skills, `social-formats` (launch assets) |
| MAINTAIN | [references/maintain.md](references/maintain.md) | `seo-audit` (drift mode), `core-web-vitals`, `webapp-testing`, `pre-launch-checklist` (legal re-checks after changes) |

## How to run a phase

1. Announce the phase and what its exit gate is (one sentence each).
2. Read the phase reference file.
3. Do the phase work, delegating to specialist skills where the table says so.
4. Run the exit-gate checklist from the reference.
5. Report: what was produced, gate status, and what the next phase needs
   from the client (approvals, content, credentials).
6. **Update `docs/project-state.md`** using the template in
   [references/project-state.md](references/project-state.md) — phase, gate
   status, blockers, client to-dos, next step. This file is how the next
   session (or another teammate) picks the project up without re-deriving
   everything; treat it as part of the phase's deliverable.

## Language

Client-facing documents (brief, proposal, launch checklist) follow the
client's language — German clients get German documents. Code, comments,
and commit messages stay English unless the repo says otherwise.
