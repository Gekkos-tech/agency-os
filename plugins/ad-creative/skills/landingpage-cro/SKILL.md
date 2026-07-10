---
name: landingpage-cro
description: Structures and audits landing pages for conversion — the bridge between design, SEO, and copy. Use when the user asks about "landing page structure", "CRO", "conversion optimization", "why isn't the page converting", "landingpage aufbauen", or needs a section-by-section page architecture, friction audit, message-match check, or A/B testing plan. Covers the conversion narrative sequence (hero → credibility → problem/solution → offer → proof → objections → risk reversal → CTA), DACH trust elements, mobile-first conversion rules, and a measurement plan. NOT for visual design systems, typography, or component styling (use design-foundation skills), NOT for SEO audits, rankings, or keyword research (use seo-marketing skills), NOT for writing the copy itself (use ad-copy).
---

# Landing Page CRO — Conversion-Focused Page Structure

Design the argument of a landing page: which sections, in which order, doing which persuasive job. Output is a structural blueprint plus audit findings — not visual design, not finished copy.

© GEKKOS Tech. Licensed under MIT.

## Two modes

- **Build mode** (user is creating a page): run the message-match check, then produce the section sequence with per-section jobs and must-contain elements, then the measurement plan.
- **Audit mode** (user asks "why isn't it converting"): fetch/read the page, check message match first, then walk the section sequence for missing/misordered jobs, then run the friction checklist. Report findings ordered by expected conversion impact, not by page order.

## Message-match rule (check this first, always)

The single highest-leverage CRO factor. Two equations must hold:

1. **Ad promise == hero promise.** Whatever the ad (or email, or post) promised is the first thing the hero must confirm — same offer, same benefit, same wording family, same visual world. A visitor who clicked "30% off onboarding" and lands on a generic homepage-style hero bounces before reading anything else.
2. **Keyword == H1 intent.** For search traffic, the H1 must answer the query's intent (not necessarily echo the keyword verbatim, but resolve it). Someone searching "payroll software comparison" must land on a comparison, not a signup pitch.

If traffic comes from multiple distinct promises, recommend separate landing page variants per promise — one page per message, not one page for all messages.

## The conversion narrative — section sequence

Default sequence for a cold-to-warm conversion page. Each section has ONE job; a section doing two jobs is doing neither. Layout patterns per section are in [references/section-patterns.md](references/section-patterns.md).

| # | Section | Job | Must contain |
|---|---|---|---|
| 1 | **Hero promise** | Confirm the click was right, state the core value in 5 seconds | H1 = main benefit (message-matched), supporting subline (how/for whom), primary CTA, hero visual showing product/outcome, above the fold on mobile |
| 2 | **Credibility strip** | Answer "can I trust these people?" before any selling | Client/press logos OR review score OR key number ("12,000 customers"); compact, no headline needed |
| 3 | **Problem / solution** | Create recognition ("that's my problem"), then map product to it | Problem stated in the visitor's words, 2–4 pain points, solution framed as the mechanism (HOW it fixes it, not just "it fixes it") |
| 4 | **Offer detail** | Make the offer concrete and evaluable | What exactly they get (features as benefits), pricing or pricing-path, scope/timeline, visual of the actual product/service |
| 5 | **Social proof** | Let others make the claims the brand can't | 2–3 testimonials with full name + photo/company (specific results > praise), case numbers, ratings with source |
| 6 | **Objection handling / FAQ** | Remove the last "yes, but…" | 4–7 real objections (price, effort, switching, "will it work for MY case", contract terms) answered honestly; sourced from sales/support if available |
| 7 | **Risk reversal** | Make saying yes safer than saying no | Guarantee, free trial, free cancellation, "no credit card required", data portability — whichever is true |
| 8 | **Final CTA** | Convert the reader who scrolled everything | Repeat primary CTA + one-line benefit recap; optionally a lower-commitment secondary path (newsletter, demo) for not-ready visitors |

Adaptation rules:
- **Hot/retargeting traffic:** compress 2–3, expand 6–7 — they know the problem, they have objections.
- **High-ticket B2B:** insert a "process/how we work" section after 4; the offer is a relationship, buyers need to see the path.
- **Simple/cheap offer:** sections 3+4 can merge; never cut 2 or 5.
- Never place the first CTA below section 3 — some visitors arrive ready.

## Friction audit checklist

Run in audit mode; recommend preemptively in build mode.

- **Form length:** every field costs conversions. Justify each field against "do we need this BEFORE the sale?" Name+email beats full address forms for lead gen; move qualification to step 2 (multi-step forms convert better than long single forms).
- **Cognitive load:** one page = one goal = one primary CTA verb. Count distinct decisions the page asks for (plans, options, links); more than one primary decision → simplify or sequence.
- **CTA competition:** navigation menus, footer link farms, outbound links, and multiple differently-worded CTAs all leak clicks. Landing pages for paid traffic should strip or minimize global navigation.
- **Load speed:** every second of load costs conversions, most brutally on mobile paid traffic. Flag: hero images >200KB, render-blocking scripts, autoplaying video above the fold, unoptimized fonts. (Deep performance auditing → hand to the SEO/technical skills.)
- **Clarity frictions:** unexplained jargon in H1, benefit hidden behind cleverness, price nowhere findable, CTA label vague ("Submit", "Mehr erfahren" as primary).

## Trust elements for DACH markets

German-speaking visitors are measurably more trust-sensitive. On any DE/AT/CH page, check:

- **Impressum + Datenschutz** visibly linked (legally required in DE; absence destroys trust AND is abmahnfähig). Footer at minimum.
- **Real company data:** full legal name, address, contact — anonymity reads as scam.
- **Reviews with sources:** Google, Trusted Shops, ProvenExpert, OMR Reviews — named platforms beat unsourced star graphics.
- **Certifications/badges** where genuine: TÜV, Trusted Shops, ISO, "Made in Germany", DSGVO/GDPR compliance statement near forms.
- **Payment/data reassurance at the form:** SSL mention, "Ihre Daten werden nicht weitergegeben", recognizable payment logos for shops.
- Du/Sie consistency with the ad that brought the visitor (mismatch = message-match violation).

## Mobile-first conversion rules

Most paid traffic is mobile; audit mobile first, desktop second.

- **Above-fold offer clarity:** on a 390px viewport, H1 + subline + CTA must be visible without scrolling; hero image must not push the CTA below the fold.
- **Sticky CTA:** persistent bottom CTA bar (or sticky header CTA) once the hero scrolls away; label stays constant with the primary CTA.
- **Tap targets:** min ~44×44px, full-width buttons on mobile, adequate spacing — no adjacent-link misfires.
- **Forms on mobile:** correct input types (email/tel keyboards), autofill enabled, no dropdowns where 3 radio buttons work.
- **Thumb reach:** primary actions in the lower half of natural viewport positions where possible.
- Test the page at 390px width before shipping any structure recommendation.

## Measurement plan

Every blueprint or audit ends with a measurement section:

1. **Primary conversion:** the ONE action that defines success (purchase, qualified lead, booked demo). One per page.
2. **Micro-conversions:** scroll depth past section 3, CTA clicks, form starts vs. form completions, FAQ interactions, time on pricing. These diagnose WHERE the page loses people.
3. **What to A/B test first**, in order of typical leverage: (1) hero H1 / offer framing, (2) hero CTA label + placement, (3) social proof position (above vs. below offer), (4) form length, (5) risk-reversal prominence. Test one variable at a time; state a hypothesis per test; don't test button colors while the headline is unproven.

## Boundaries

Structure and argumentation only. Visual design (colors, typography, components) → design-foundation skills. SEO audits, rankings, technical crawl issues → seo-marketing skills. Writing the actual headlines, body copy, and CTAs → ad-copy skill; this skill specifies WHAT each section must say, ad-copy writes HOW.
