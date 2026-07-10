---
name: ad-copy
description: Writes performance ad and landing page copy in German and English. Use when the user asks for "ad copy", "Werbetext", "headlines for", "CTA ideas", "A/B variants", "copy for the campaign", or needs finished text for Meta/Google/LinkedIn ads, landing pages, or banners. Provides headline systems (benefit, curiosity, social-proof, urgency), a funnel-stage CTA library (DE+EN), an A/B/C variant protocol with per-variant hypotheses, a tonality matrix, German-specific rules (Du/Sie, compound words, character lengths), and compliance guardrails. NOT for campaign ideation or creative routes (use ad-concepts), NOT for long-form content strategy, blog posts, or SEO articles (use seo-content skills).
---

# Ad Copy — Performance Copywriting (DE + EN)

Write conversion-focused copy for ads and landing pages in German, English, or both. Output is finished, publishable text — not concepts, not briefs.

© GEKKOS Tech. Licensed under MIT.

## Before writing

Establish from the brief (infer and state assumptions if missing):
1. **Language(s):** DE, EN, or both. If the market is DACH and the user didn't specify, default to German and offer English variants.
2. **Funnel stage:** cold (never heard of the brand), warm (knows the problem/brand), hot (retargeting, cart, comparison shoppers).
3. **Voice position:** locate the brand on the tonality matrix in [references/tonality-matrix.md](references/tonality-matrix.md) before writing a single line. State the chosen cell.
4. **German address form:** run the Du/Sie decision tree (below) and state the decision.
5. **Channel + placement:** determines length limits and register (see tonality matrix, platform axis).

## Headline systems

Four systems. Pick the system that matches funnel stage and channel; write within it, don't mix systems inside one headline.

### 1. Benefit-led
Formula: `[Outcome] in/ohne/without [timeframe/pain]` — lead with what the customer gets, stated concretely.
- EN: *"Payroll done in 4 minutes. Every month."*
- DE: *"Lohnabrechnung in 4 Minuten. Jeden Monat."*
Use for: cold traffic, search ads (matches query intent), products with a clear measurable outcome.

### 2. Curiosity
Formula: `[Specific subject] + [information gap]` — open a gap the reader can only close by clicking. Must pay off; never bait.
- EN: *"The onboarding email 9 out of 10 SaaS teams get wrong."*
- DE: *"Der Fehler, den fast jedes Onboarding-Mailing macht."*
Use for: content-adjacent ads, advertorials, warm audiences. Avoid for: search (intent mismatch), regulated categories.

### 3. Social-proof
Formula: `[Number/name of adopters] + [what they did/found]`.
- EN: *"14,000 clinics switched. Here's why."*
- DE: *"14.000 Praxen sind umgestiegen. Aus gutem Grund."*
Use for: skeptical audiences, high-consideration B2B, retargeting. Proof must be real and current.

### 4. Urgency
Formula: `[Deadline/scarcity fact] + [benefit at stake]`. Only when the urgency is true.
- EN: *"Early pricing ends Friday — lock in 30% off."*
- DE: *"Frühbucherpreis nur bis Freitag – 30 % sichern."*
Use for: hot traffic, launches, seasonal offers. Fake countdowns are a compliance and trust violation — refuse to write them.

For every headline task, deliver at least 5 candidates per language across at least 2 systems, then mark your recommended pick with one line of reasoning.

## CTA library by funnel stage

Match CTA commitment level to funnel temperature. High-commitment CTAs on cold traffic kill CTR.

| Stage | EN | DE |
|---|---|---|
| Cold — learn | *See how it works* · *Get the free guide* · *Watch the 2-min demo* | *So funktioniert's* · *Gratis-Guide sichern* · *2-Minuten-Demo ansehen* |
| Cold — soft try | *Try it free* · *Explore examples* | *Kostenlos ausprobieren* · *Beispiele ansehen* |
| Warm — evaluate | *Compare plans* · *Get your quote* · *Book a demo* | *Pakete vergleichen* · *Angebot anfordern* · *Demo buchen* |
| Warm — start | *Start your free trial* · *Create your account* | *Jetzt kostenlos testen* · *Konto erstellen* |
| Hot — buy | *Get started now* · *Claim your discount* · *Complete your order* | *Jetzt loslegen* · *Rabatt einlösen* · *Bestellung abschließen* |
| Hot — reassure | *Try risk-free for 30 days* | *30 Tage risikofrei testen* |

Rules: verb-first, first-person framing where the platform allows ("Get my quote" / "Mein Angebot anfordern" lifts on landing pages), one primary CTA per asset, never "Submit"/"Absenden".

## A/B variant protocol

Every copy deliverable ships as **A/B/C** — never a single version:

- **Variant A — Safe:** the proven pattern for this category and stage. Benefit-led, clear, no risk. This is the control candidate.
- **Variant B — Bold:** same core message, aggressive execution — stronger claim framing, curiosity or urgency system, punchier voice. Tests whether the audience rewards salience.
- **Variant C — Different angle:** a genuinely different persuasive angle (different benefit, different objection addressed, different emotional register) — not a rewrite of A. Tests the message, not the wording.

For each variant, state the **hypothesis** in one line: *"B tests whether loss-framing ('Stop overpaying…') outperforms gain-framing for this retargeting audience."* A variant without a hypothesis teaches nothing when it wins.

Keep everything except the tested element constant across variants where the user is running a real test (same offer, same CTA unless the CTA is the test).

## German-specific rules

### Du/Sie decision tree
1. Existing brand voice documented? → follow it, flag if it clashes with audience norms.
2. B2B, audience 40+, finance/legal/medical/insurance, or high ticket? → **Sie**.
3. B2C lifestyle, fitness, apps, fashion, gaming, or audience skews under ~35? → **Du**.
4. B2B SaaS targeting startups/tech/marketing teams? → **Du** is now standard; Sie reads distant.
5. Genuinely ambiguous? → recommend **Du** for Meta/TikTok placements, **Sie** for LinkedIn/print, and say so explicitly. Never mix forms within one asset.

### Compound words & readability
German compounds inflate visually: "Kundenbindungsmanagement" is one unreadable brick in a headline. Prefer verb constructions ("Kunden binden – automatisch") or split with a hyphen only where Duden-conform. In headlines, avoid words over ~16 characters; rewrite around them.

### Character-length pitfalls
German runs ~20–35% longer than English. Never translate EN copy 1:1 into a character-limited field — rewrite natively.
- Google RSA headline: 30 chars — an EN benefit headline often needs a different German construction, not a translation.
- Meta primary text truncates around ~125 chars on mobile: front-load the benefit in the first ~90 chars in German.
- CTA buttons: German verb phrases get long ("Jetzt kostenlos herunterladen" = 29 chars); check button width, shorten to "Gratis laden" style if needed.

## Compliance guardrails

- **No misleading claims:** every factual claim (numbers, test results, "clinically proven") must come from the user's brief or be marked `[VERIFY: source needed]`. Never invent statistics, reviews, or awards.
- **Superlative caution:** "der beste / the best / Nr. 1" requires substantiation (DE: Alleinstellungswerbung under UWG); default to defensible framing ("one of", specific dimension, or verified rating source).
- **Health:** no healing promises (DE: HWG restricts Heilversprechen), no before/after implications for medical outcomes, no "prevents/cures/treats" without approved substantiation.
- **Finance:** no guaranteed-return language, include risk framing where the user's legal team requires; never write copy that promises specific investment outcomes.
- **Urgency/scarcity:** only when factually true.
- Flag any brief that requires claims you cannot verify, and deliver compliant alternatives alongside.

## Output format

For each asset: language(s) → chosen tonality cell + Du/Sie decision (one line) → A/B/C variants with hypotheses → character counts for length-limited fields → any `[VERIFY]` flags. Stay out of ideation (ad-concepts) and long-form strategy (seo-content) — if the user needs a campaign idea first, say so and hand off.
