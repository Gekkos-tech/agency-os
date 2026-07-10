# agency-os

> **The complete Claude Code toolkit for web & advertising design agencies.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin%20marketplace-d97706)](https://docs.anthropic.com/en/docs/claude-code/plugins)
[![Plugins](https://img.shields.io/badge/bundles-6-blue)](#bundles)
[![Made by GEKKOS Tech](https://img.shields.io/badge/made%20by-GEKKOS%20Tech-black)](https://github.com/gekkos-tech)

Six plugin bundles covering the full agency lifecycle — from client brief to
campaign launch: project workflow, design quality, motion & 3D, QA, SEO, and
ad creative. Built from battle-tested open-source skills (properly attributed)
plus original skills written for agency work, including a legal go-live gate
for German/EU projects (DSGVO, Impressum, Cookie-Consent, BFSG).

## Quick Start

```
/plugin marketplace add gekkos-tech/agency-os
```

Then install the bundles you need:

```
/plugin install agency-core@agency-os
/plugin install design-foundation@agency-os
/plugin install motion-3d@agency-os
/plugin install quality-qa@agency-os
/plugin install seo-marketing@agency-os
/plugin install ad-creative@agency-os
```

Start your first project:

```
/new-project Café in Cologne, modern-minimalist, online reservations
```

## Bundles

| Plugin | What's inside | Skills |
|---|---|---|
| **agency-core** | The project spine: `agency-workflow` routes BRIEF → CONCEPT → DESIGN → BUILD → QA → LAUNCH with phase gates; plus code-discipline and complete-output guards | agency-workflow, complete-output, karpathy-guidelines |
| **design-foundation** | The design quality layer: style/palette/font intelligence, anti-generic creative direction, committed style systems, redesigns, micro-polish, 74 brand reference systems | ui-ux-pro-max, taste, impeccable, style-systems, redesign, interface-polish, awesome-design-md |
| **motion-3d** | Everything that moves: the full official GSAP suite, Three.js/WebGL, React Three Fiber, Lottie, Rive, and Remotion video | gsap-suite, threejs-webgl, react-three-fiber, lottie-animations, rive-interactive, remotion-video |
| **quality-qa** | Ship with evidence: performance, Core Web Vitals, accessibility, best practices, webapp testing, and the German/EU legal pre-launch gate | performance, core-web-vitals, accessibility, best-practices, webapp-testing, pre-launch-checklist |
| **seo-marketing** | The claude-seo powerhouse, consolidated to 9 focused skills with 15 specialist subagents: audits with health scoring, technical, content, schema, local, AI visibility (GEO), competitor pages, backlinks, e-commerce | seo-audit, seo-technical, seo-content, seo-schema, seo-local, seo-ai-visibility, seo-competitor, seo-backlinks, seo-ecommerce |
| **ad-creative** | From idea to export: campaign ideation (AIDA/PAS/JTBD/hooks), performance copy (DE+EN), platform format specs, landing page CRO, brand kits, and AI image direction for web/mobile design references | ad-concepts, ad-copy, social-formats, landingpage-cro, brandkit, imagegen-web, imagegen-mobile, image-to-code |

## Commands

| Command | Plugin | Does |
|---|---|---|
| `/new-project <brief>` | agency-core | Kick off a client project — runs the BRIEF phase |
| `/handoff [verify]` | agency-core | Assemble or audit the binding design handoff |
| `/proposal [terms]` | agency-core | Draft a client proposal from the brief |
| `/design-review [target]` | design-foundation | Structured design review via the `design-reviewer` agent |
| `/pre-launch <url>` | quality-qa | Legal + technical go-live gate via the `qa-auditor` agent |
| `/campaign <client + goal>` | ad-creative | 3 distinct campaign routes with claim, hook, visual, channel |
| `/adapt-formats <asset>` | ad-creative | Adapt a master creative to all platform format specs |

## How the pieces fit

```
BRIEF ──► CONCEPT ──► DESIGN ──► BUILD ──► QA ──► LAUNCH
agency-workflow routes every phase and loads the right specialist:
concept: taste · ad-concepts        build: image-to-code · gsap-suite
design:  style-systems · imagegen-* qa:    performance · accessibility
                                    launch: pre-launch-checklist · seo-audit
```

## Recommended companion plugins

Not bundled (different licenses/ownership), but they pair well:

- [frontend-design](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design) — Anthropic's official frontend design plugin
- [anthropics/skills](https://github.com/anthropics/skills) — official skills incl. document handling
- [Vercel plugin](https://vercel.com/docs) — deploys, envs, previews from Claude Code
- [claude-seo](https://github.com/AgriciDaniel/claude-seo) — the upstream SEO marketplace; adds API-powered skills (DataForSEO, Ahrefs, SE Ranking, Profound, Bing, Firecrawl, Google APIs, image generation) if you have keys

## Credits

agency-os stands on excellent open-source work. Bundled skills keep their
original licenses and LICENSE files — full details in
[THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md):

- [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) — Next Level Builder (MIT)
- [taste](https://github.com/Leonxlnx/taste-skill) — Leonxlnx (MIT)
- [impeccable](https://github.com/pbakaus/impeccable) — Paul Bakaus (Apache-2.0)
- [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) — VoltAgent (MIT)
- [GSAP skills](https://github.com/greensock/gsap-skills) — GreenSock/Webflow (MIT)
- [claude-seo](https://github.com/AgriciDaniel/claude-seo) — Daniel Agrici and Pro Hub Challenge contributors (MIT); FLOW framework prompts (CC BY 4.0)
- [web-quality-skills](https://github.com/addyosmani/web-quality-skills) — Addy Osmani (MIT)
- [webapp-testing](https://github.com/anthropics/skills) — Anthropic (Apache-2.0)
- [claudedesignskills](https://github.com/freshtechbro/claudedesignskills) — freshtechbro (MIT)
- karpathy-guidelines — community skill (MIT), inspired by Andrej Karpathy's writing

Original skills (agency-workflow, style-systems, redesign, interface-polish,
complete-output, remotion-video, brandkit, imagegen-web/mobile, image-to-code,
ad-concepts, ad-copy, social-formats, landingpage-cro, pre-launch-checklist)
© 2026 GEKKOS Tech, MIT.

## Contributing

Issues and PRs welcome. Ground rules:

1. **Licensing first** — third-party content only with a clear MIT/Apache/CC
   license, original LICENSE bundled, entry in THIRD_PARTY_LICENSES.md.
2. **Trigger discipline** — new skill descriptions must state when to use
   them AND which sibling skill covers the neighboring case.
3. **Skill format** — SKILL.md < 500 lines, details in `references/`,
   valid frontmatter (`name` = directory name).

## License

MIT © 2026 [GEKKOS Tech](https://github.com/gekkos-tech). Bundled third-party
skills retain their original licenses — see
[THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md).
