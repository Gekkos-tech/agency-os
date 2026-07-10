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

## [2] SKILL-MIGRATION (installierte Skills)
- [x] Inventar ~/.claude/skills: 58 Skills, Herkunft + Lizenz geprüft (siehe Notizen unten)
- [x] Kategorisieren: (a) eigene, (b) fremd MIT/Apache, (c) fremd ohne Lizenz, (d) Plugin-Skills (keine in ~/.claude/skills)
- [ ] ► FREIGABE 1: Mapping-Tabelle alt → neu gezeigt — WARTE AUF USER-OK
- [ ] Nach Freigabe: kopieren, THIRD_PARTY_LICENSES.md, Trigger-Descriptions abgrenzen
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

## [4] AGENCY-WORKFLOW-SKILL (Router, mit skill-creator)
- [ ] build-Skill (GEKKOS) analysieren, generalisieren (keine Interna/Kundennamen!)
- [ ] plugins/agency-core/skills/agency-workflow/: Router für BRIEF → KONZEPT → DESIGN → BUILD → QA → LAUNCH
- [ ] SKILL.md < 500 Zeilen, Details in references/, Trigger: "neues Projekt", "Website für Kunde", "Kundenprojekt starten"

## [5] GSAP-KONSOLIDIERUNG
- [ ] 8 gsap-* Skills → EIN gsap-suite in motion-3d, references/ pro Thema
- [ ] Trigger-Abgrenzung zu 3D-Skills prüfen

## [6] SEO-KONSOLIDIERUNG
- [ ] 30 seo-* Skills analysieren
- [ ] ► FREIGABE 2: Mapping 30 → max. 10 zeigen (Audit, Technical, Content, Schema, Local, AI-Visibility, Competitor, Tools), auf OK warten
- [ ] Nach Freigabe: nach plugins/seo-marketing/ konsolidieren

## [7] AD-CREATIVE-SKILLS (eigene, mit skill-creator)
- [ ] ad-concepts: Kampagnen-Ideation (AIDA, PAS, JTBD, Hooks) → 3 Kampagnenrouten
- [ ] social-formats: Format-Specs Meta/IG/TikTok/LinkedIn/YouTube (Web-Recherche Juli 2026) + Adaptions-Workflow
- [ ] ad-copy: Performance-Copywriting, Headlines/CTAs/A-B, Tonalitäts-Matrix, DE+EN
- [ ] landingpage-cro: Conversion-Struktur (Design + SEO + Copy)
- [ ] pre-launch-checklist in quality-qa: DSGVO, Impressum, Cookie-Consent, BFSG, SSL, Redirects, 404, OG-Tags, Sitemap

## [8] COMMANDS & AGENTS
- [ ] agency-core: /new-project, /handoff, /proposal
- [ ] design-foundation: /design-review + Agent design-reviewer
- [ ] quality-qa: /pre-launch + Agent qa-auditor
- [ ] ad-creative: /campaign, /adapt-formats

## [9] README (Englisch)
- [ ] Hero-Pitch, Badges, Quick Start, Bundle-Tabelle, Command-Übersicht, Credits, Recommended companion plugins, Contributing, License

## [10] END-TO-END-TEST
- [ ] /plugin marketplace add ./ + alle Plugins installieren
- [ ] Trigger-Tests: Café Köln (agency-workflow), Scroll-Animation (gsap-suite), SEO-Audit (1 Skill), Fitnessstudio-Kampagne (ad-concepts)
- [ ] Fehler beheben, Frontmatter validieren

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
