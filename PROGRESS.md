# agency-os — Build Progress

> Claude Code Plugin-Marketplace für Web- & Werbedesign-Agenturen.
> GitHub: gekkos-tech/agency-os (GEKKOS Tech)
> Bei Session-Ende: "Lies PROGRESS.md und arbeite weiter."

**Regeln:**
- Nur bei den 3 FREIGABE-Punkten stoppen + bei unklaren Lizenzen
- Nach jedem abgeschlossenen Schritt committen
- Plugin-Skills (Kategorie d) NIEMALS kopieren

---

## [1] REPO-SETUP ✅
- [x] git init
- [x] gh: public Repo gekkos-tech/agency-os erstellt + verbunden (https://github.com/gekkos-tech/agency-os)
- [x] Struktur: .claude-plugin/marketplace.json, plugins/{agency-core, design-foundation, motion-3d, quality-qa, seo-marketing, ad-creative}/
- [x] THIRD_PARTY_LICENSES.md, README.md (Platzhalter), LICENSE (MIT, © 2026 GEKKOS Tech)
- [x] marketplace.json: 6 Plugins registriert, owner "GEKKOS Tech", offizielles Schema
- [x] Jedes Plugin: plugin.json mit version 0.1.0
- [x] gh: Topics (claude-code, claude-skills, web-agency, web-design, ai-skills) + Description (bei Repo-Erstellung gesetzt)
- [x] .gitignore mit launch/ (für Schritt 11 vorbereitet)

## [2] SKILL-MIGRATION (installierte Skills) ✅
- [x] Inventar ~/.claude/skills: 58 Skills, Herkunft + Lizenz geprüft (siehe Notizen unten)
- [x] Kategorisieren: (a) eigene, (b) fremd MIT/Apache, (c) fremd ohne Lizenz, (d) Plugin-Skills (keine in ~/.claude/skills)
- [x] ► FREIGABE 1 erteilt (siehe Notizen) — Migration + Neufassungen umgesetzt
- [x] Kopiert: ui-ux-pro-max, taste (v1+v2 konsolidiert), impeccable, awesome-design-md, karpathy-guidelines; Attributionen + LICENSE-Dateien gebündelt; Trigger-Descriptions abgegrenzt
- [x] Neu geschrieben (Freigabe-1-Entscheidung): style-systems, redesign, interface-polish, complete-output, brandkit, imagegen-web, imagegen-mobile, image-to-code, remotion-video
  - Mapping-Vorgabe:
    - design-foundation: ui-ux-pro-max, taste (taste-skill + taste-skill-v1 + gpt-tasteskill → EIN Skill), impeccable, redesign-skill, make-interfaces-feel-better, awesome-design-md; minimalist/brutalist/soft/stitch → style-systems (references/ pro Stil)
    - motion-3d: remotion-best-practices
    - agency-core: output-skill, karpathy-guidelines
    - ad-creative: brandkit, imagegen-frontend-web, imagegen-frontend-mobile, image-to-code-skill
    - Kategorie (c): nur Link in README "Recommended skills"

## [3] EXTERNE MIT/APACHE-SKILLS ✅
- [x] frontend-design NICHT gebündelt: anthropics/claude-code ist proprietär (© Anthropic, All rights reserved) → nur README-Link "Recommended companion plugins"
- [x] ui-ux-pro-max durch frische Upstream-Version v2.6.2 ersetzt (84 Styles, motion.csv etc.); taste-skill v2 war bereits identisch mit Upstream
- [x] quality-qa: performance, core-web-vitals, accessibility, best-practices (addyosmani, MIT — seo + web-quality-audit NICHT) + webapp-testing (anthropics/skills, Apache 2.0)
- [x] motion-3d: threejs-webgl, react-three-fiber, lottie-animations, rive-interactive (freshtechbro, MIT)
- [x] Original-LICENSE je Skill gebündelt, THIRD_PARTY_LICENSES.md ergänzt
- Übersprungen (keine LICENSE im Quell-Repo): remotion-dev/skills (→ eigener remotion-video-Skill), jakubkrehel/make-interfaces-feel-better (→ eigener interface-polish-Skill)

## [4] AGENCY-WORKFLOW-SKILL (Router, mit skill-creator) ✅
- [x] build-Skill analysiert; Prinzipien generalisiert (Plan-vor-Code, Handoff = Wahrheit, Quality-Layer prüft statt neu zu generieren, Scope-Disziplin) — keine GEKKOS-Interna/Kundennamen übernommen
- [x] agency-workflow: Router BRIEF → CONCEPT → DESIGN → BUILD → QA → LAUNCH, Phase-Detection + Routing-Tabelle + Exit-Gates
- [x] SKILL.md 73 Zeilen + references/{brief,concept,design,build,qa,launch}.md; Trigger DE+EN ("neues Projekt", "Website für Kunde", "Kundenprojekt starten", "new project", ...)

## [5] GSAP-KONSOLIDIERUNG ✅
- [x] 8 gsap-* Skills → gsap-suite in motion-3d (Router-SKILL.md + references/{core,timeline,scrolltrigger,plugins,react,frameworks,utils,performance}.md)
- [x] Trigger-Abgrenzung: Description grenzt explizit gegen threejs-webgl, react-three-fiber, lottie-animations, rive-interactive, remotion-video ab
- [x] Quelle: greensock/gsap-skills (offiziell, MIT), LICENSE gebündelt

## [6] SEO-KONSOLIDIERUNG ✅
- [x] 31 seo-* Skills analysiert (alle AgriciDaniel/claude-seo v2.2.0, MIT; Kern-Skill "seo" = 1MB Engine + 506MB lokale .venv, die natürlich nicht mitkopiert wurde)
- [x] ► FREIGABE 2 erteilt: 31 → 9 (seo-audit, seo-technical, seo-content, seo-schema, seo-local, seo-ai-visibility, seo-competitor, seo-backlinks, seo-ecommerce)
- [x] Konsolidiert nach plugins/seo-marketing/: gemergte Bodies als references/, Descriptions neu für Trigger-Abgrenzung ("SEO-Audit" → genau seo-audit), 15 Spezialisten-Agenten nach agents/
- [x] NICHT gebündelt (API-Key nötig): seo-ahrefs, seo-dataforseo, seo-seranking, seo-profound, seo-bing, seo-firecrawl, seo-google, seo-image-gen → README-Link auf claude-seo
- [x] FLOW-Framework (CC BY 4.0) mit Attribution in THIRD_PARTY_LICENSES.md

## [7] AD-CREATIVE-SKILLS (eigene, mit skill-creator) ✅
- [x] ad-concepts: 3 Kampagnenrouten (Titel, Claim, Hook, Visual, Kanal, Framework), AIDA/PAS/JTBD/4U + Hook-Formelbank, Register-Diversitätsregel
- [x] social-formats: Specs online verifiziert (Juli 2026) für Meta/IG, TikTok, LinkedIn, YouTube; Safe-Zones, Adaptions-Workflow, Naming-Konvention. Nicht verifizierbar (im Skill markiert): LinkedIn-Stories-Relaunch, TikTok-Safe-Zone-Varianz, YouTube Pause Ads
- [x] ad-copy: 4 Headline-Systeme DE+EN, CTA-Bibliothek nach Funnel-Stufe, A/B/C-Protokoll mit Hypothesen, Tonalitäts-Matrix (4 Stimmen × 3 Funnel-Stufen), Du/Sie-Entscheidungsbaum, UWG/HWG-Compliance
- [x] landingpage-cro: 8-Sektionen-Conversion-Narrativ, Message-Match-Regel, Friction-Audit, DACH-Trust-Elemente, Mobile-First-Regeln, Messplan
- [x] pre-launch-checklist in quality-qa: DSGVO, Impressum (§5 DDG), TDDDG-Consent, BFSG, SSL, Redirects, 404, OG-Tags, Sitemap, Google-Fonts-Selbsthosting

## [8] COMMANDS & AGENTS ✅
- [x] agency-core: /new-project, /handoff, /proposal
- [x] design-foundation: /design-review + Agent design-reviewer
- [x] quality-qa: /pre-launch + Agent qa-auditor
- [x] ad-creative: /campaign, /adapt-formats
- [x] (Bonus aus Schritt 6: 15 SEO-Spezialisten-Agenten in seo-marketing/agents/)

## [9] README (Englisch) ✅
- [x] Hero-Pitch, Badges, Quick Start (/plugin marketplace add gekkos-tech/agency-os), Bundle-Tabelle, Command-Übersicht, Workflow-Diagramm, Credits (alle Attributionen), Recommended companion plugins (frontend-design, anthropics/skills, Vercel, claude-seo Power-ups), Contributing-Regeln, License

## [10] END-TO-END-TEST ✅
- [x] claude plugin marketplace add ./ + alle 6 Plugins installiert (user-scope), `claude plugin validate --strict` grün für Marketplace + alle 6 Plugins
- [x] `claude plugin details`: alle Skills/Commands/Agenten korrekt erkannt (agency-core 6 Skills, ad-creative 10, seo-marketing 9 Skills + 15 Agenten)
- [x] Trigger-Tests 4/4 PASS (Judge-Agent gegen den echten Skill-Katalog): Café Köln → agency-workflow; Scroll-Hero → gsap-suite; SEO-Audit → genau seo-audit (Deferral-Klauseln der 8 anderen SEO-Skills greifen); Fitnessstudio-Kampagne → ad-concepts
- [x] Fix aus Test: impeccable-Description grenzt jetzt explizit gegen gsap-suite ab (als Modification in THIRD_PARTY_LICENSES.md notiert)
- [x] Frontmatter aller 34 Skills + 15 Agenten YAML-validiert (name==dir, description <1024)
- Hinweis: Live-Trigger-Test in frischer Session war headless nicht möglich (claude -p ohne CLI-Login in dieser Desktop-Session); Test lief als Simulation gegen die echten Descriptions. Empfehlung: einmal manuell in neuer Session "Neues Projekt: Café Köln..." eingeben.

## [11] RELEASE & LAUNCH
- [ ] git push, gh Release v1.0.0 mit Changelog
- [ ] launch/-Ordner (in .gitignore!): Show-HN, r/ClaudeAI, X-Thread (5 Tweets), Screencast-Drehbuch
- [ ] ► FREIGABE 3: Launch-Posts zur Abnahme zeigen

---

## Notizen / Entscheidungen

### Skill-Inventar (Stand 2026-07-10, 58 Skills in ~/.claude/skills)

**(a) Eigene:**
- `build` (GEKKOS-Workflow) — wird NICHT kopiert, sondern generalisiert als Basis für agency-workflow (Schritt 4)

**(b) Fremd, MIT/Apache — kopierbar mit Attribution:**
- `ui-ux-pro-max` — nextlevelbuilder/ui-ux-pro-max-skill, MIT
- `taste-skill`, `taste-skill-v1` — Leonxlnx/taste-skill, MIT
- `impeccable` — Apache 2.0 (Frontmatter)
- `karpathy-guidelines` — MIT (Frontmatter)
- `awesome-design-md` — VoltAgent/awesome-design-md, MIT
- `gsap-*` (8 Skills) — greensock/gsap-skills (offiziell), MIT
- `seo*` (31 Skills) — AgriciDaniel/claude-seo v2.2.0, MIT (einzelne mit original_author aus "Pro Hub Challenge", in Attribution nennen)

**(c) Fremd/unklar OHNE Lizenznachweis — Rückfrage bei FREIGABE 1:**
- `minimalist-skill`, `brutalist-skill`, `soft-skill`, `stitch-skill` (Herkunft unbekannt)
- `redesign-skill`, `make-interfaces-feel-better` (Herkunft unbekannt)
- `remotion-best-practices` — stammt aus remotion-dev/skills, Repo hat KEINE LICENSE-Datei → nicht kopierbar ohne Klärung
- `gpt-tasteskill`, `output-skill`, `brandkit`, `imagegen-frontend-web`, `imagegen-frontend-mobile`, `image-to-code-skill` — keine Lizenz-/Autor-Marker; falls eigene Skills des Users → kopierbar

**(d) Plugin-Skills:** keine in ~/.claude/skills (vercel/design/searchfit/anthropic-skills liegen im Plugin-Cache, werden nie kopiert)

### FREIGABE 1 — Ergebnis (2026-07-10):
- Mapping freigegeben ("mach alles als Bundle wenn es geht") — frontend-design bleibt Link (proprietär, geht nicht)
- Style-Skills + redesign + make-interfaces-feel-better: NEU SCHREIBEN → style-systems, redesign, interface-polish
- brandkit/imagegen-web/imagegen-mobile/image-to-code/gpt-tasteskill/output-skill: NEU SCHREIBEN → brandkit, imagegen-web, imagegen-mobile, image-to-code, complete-output
- remotion: EIGENEN Skill schreiben → remotion-video
- NACHTRÄGLICHER FUND: Leonxlnx/taste-skill (MIT) enthält ALLE diese "unklaren" Skills (brandkit, imagegen-*, image-to-code, redesign, output, minimalist/brutalist/soft/stitch, gpt-tasteskill) — Originale wären also doch bündelbar. Da User explizit "neu schreiben" gewählt hat, bleiben die Neufassungen; Originale können später bei Bedarf ersetzt werden.

### Lizenz-Befunde Schritt 3 (extern):
- ⚠️ `anthropics/claude-code` ist PROPRIETÄR (© Anthropic PBC, All rights reserved) — frontend-design darf NICHT gebündelt werden → nur als "Recommended companion plugin" verlinken
- `anthropics/skills` webapp-testing: eigene LICENSE.txt Apache 2.0 → OK
- `addyosmani/web-quality-skills`: MIT → OK
- `freshtechbro/claudedesignskills`: MIT → OK (threejs-webgl, react-three-fiber, lottie-animations, rive-interactive unter plugins/individual/)
- `remotion-dev/skills`: KEINE LICENSE → überspringen (Regel), Remotion selbst NOASSERTION-Lizenz
