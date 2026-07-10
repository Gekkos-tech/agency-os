# Third-Party Licenses

agency-os bundles skills from third-party open-source projects. Each bundled skill
retains its original license; a copy of the original LICENSE file is kept alongside
the skill files. This document lists all attributions.

---

## ui-ux-pro-max (plugin: design-foundation)
- Source: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Author: Next Level Builder
- License: MIT (LICENSE file bundled with the skill)
- Modifications: none

## taste (plugin: design-foundation)
- Source: https://github.com/Leonxlnx/taste-skill
- Author: Leonxlnx
- License: MIT (LICENSE file bundled with the skill)
- Modifications: consolidated v2 (`taste-skill`) and v1 (`taste-skill-v1`) into one
  skill (`taste`); v1 ruleset preserved as `references/taste-v1-legacy.md`;
  frontmatter name/description adjusted for trigger separation within agency-os.

## impeccable (plugin: design-foundation)
- Source: https://github.com/pbakaus/impeccable
- Author: Paul Bakaus (https://impeccable.style)
- License: Apache-2.0 (LICENSE file bundled with the skill)
- Modifications: none

## awesome-design-md (plugin: design-foundation)
- Source: https://github.com/VoltAgent/awesome-design-md
- Author: VoltAgent
- License: MIT (LICENSE file bundled with the skill)
- Modifications: none

## karpathy-guidelines (plugin: agency-core)
- Source: community-maintained skill, canonical upstream repository not identified;
  distributed under MIT as declared in its SKILL.md frontmatter
- Inspiration: public writing of Andrej Karpathy on LLM coding practices
- License: MIT
- Modifications: none

## performance, core-web-vitals, accessibility, best-practices (plugin: quality-qa)
- Source: https://github.com/addyosmani/web-quality-skills
- Author: Addy Osmani
- License: MIT (LICENSE file bundled with each skill)
- Modifications: none (the repository's `seo` and `web-quality-audit` skills are
  intentionally not bundled)

## webapp-testing (plugin: quality-qa)
- Source: https://github.com/anthropics/skills (skills/webapp-testing)
- Author: Anthropic, PBC
- License: Apache-2.0 (original LICENSE.txt bundled with the skill)
- Modifications: none

## threejs-webgl, react-three-fiber, lottie-animations, rive-interactive (plugin: motion-3d)
- Source: https://github.com/freshtechbro/claudedesignskills
- Author: freshtechbro
- License: MIT (LICENSE file bundled with each skill)
- Modifications: none

---

## gsap-suite (plugin: motion-3d)
- Source: https://github.com/greensock/gsap-skills (official GSAP skills)
- Author: GreenSock / Webflow
- License: MIT
- Modifications: the 8 official skills (gsap-core, gsap-timeline, gsap-scrolltrigger,
  gsap-plugins, gsap-react, gsap-frameworks, gsap-utils, gsap-performance) were
  consolidated into one skill; original bodies preserved as references/*.md with
  cross-references rewritten; new router SKILL.md by GEKKOS Tech.

## seo-audit, seo-technical, seo-content, seo-schema, seo-local, seo-ai-visibility, seo-competitor, seo-backlinks, seo-ecommerce (plugin: seo-marketing)
- Source: https://github.com/AgriciDaniel/claude-seo (v2.2.0)
- Author: Daniel Agrici; individual sub-skills credit original authors from the
  "Pro Hub Challenge": Lutfiya Miller (clustering), Florian Schmitz (SXO),
  Dan Colta (drift), Matej Marjanovic (e-commerce)
- License: MIT (original LICENSE.txt files retained inside the skills)
- Modifications: 31 skills consolidated into 9 by GEKKOS Tech — merged skill
  bodies preserved as references/*.md, descriptions rewritten for trigger
  separation, API-key-dependent tool skills (ahrefs, dataforseo, seranking,
  profound, bing, firecrawl, google, image-gen) not bundled. 15 specialist
  subagent definitions bundled under agents/.

## FLOW framework prompt library (inside seo-ai-visibility)
- Source: FLOW knowledge base bundled with claude-seo (41 prompts)
- License: CC BY 4.0 (attribution retained in references/flow-framework.md
  and references/flow-framework/bibliography.md)
- Modifications: none
