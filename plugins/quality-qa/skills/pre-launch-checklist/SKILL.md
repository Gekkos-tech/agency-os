---
name: pre-launch-checklist
description: The go-live gate for websites, tuned for German/EU agencies — legal compliance (DSGVO/GDPR, Impressum, Cookie-Consent, BFSG accessibility) plus the technical launch checklist (SSL, redirects, 404, OG tags, sitemap, robots, forms, analytics). Use this skill before ANY website goes live or relaunches — trigger on "pre-launch", "go-live check", "launch checklist", "können wir live gehen", "ready to launch?", "vor dem Launch prüfen", "Website abnehmen", or when the agency-workflow LAUNCH phase runs. Legal items are hard blockers, not warnings. Not a general QA pass (use performance/accessibility/webapp-testing for that) — this is the final gate after QA.
---

# Pre-Launch Checklist

Run this as the last gate before DNS cutover. Two sections: **legal** (hard
blockers — a German site going live without these creates liability) and
**technical**. Produce `docs/launch-checklist.md` with pass/fail + evidence
per item. Anything failing legal = no launch recommendation, stated plainly.

## A. Legal (DACH/EU) — hard blockers

### Impressum (§ 5 DDG, formerly TMG)
- [ ] Impressum page exists, reachable from EVERY page within 2 clicks
- [ ] Contains: full legal name + legal form, postal address (no P.O. box),
      email AND a second fast contact channel (usually phone), authorized
      representative, commercial register + number (if registered),
      USt-IdNr. (if assigned), supervisory authority / chamber for regulated
      professions
- [ ] Responsible person for editorial content (§ 18 Abs. 2 MStV) if the
      site has journalistic/editorial content

### Datenschutzerklärung (DSGVO)
- [ ] Privacy policy page linked from every page, current, and matching what
      the site ACTUALLY does — verify against reality:
  - [ ] every third-party service found in the code/network tab is listed
        (fonts, maps, analytics, tag manager, video embeds, forms, CDN, chat)
  - [ ] legal basis named per processing purpose
  - [ ] data subject rights, retention, controller contact,
        Datenschutzbeauftragter (if required)
- [ ] **Google Fonts are self-hosted** (loading from fonts.googleapis.com is
      an established Abmahnung risk in Germany), same logic for other
      third-party assets that leak IPs pre-consent
- [ ] Forms: only necessary fields, HTTPS submission, no pre-checked
      marketing checkboxes, double opt-in for newsletters

### Cookie-Consent (TDDDG § 25 + DSGVO)
- [ ] No non-essential cookies/storage before consent — verify in DevTools
      with a fresh profile: only technically necessary items pre-consent
- [ ] Analytics/marketing tags fire only AFTER opt-in (test both paths)
- [ ] Banner: "Reject all" as prominent as "Accept all", granular choices,
      consent revocable (persistent link/settings), no dark patterns
- [ ] If only essential cookies are used: no banner needed — do not add one
      "for safety"; document it instead

### BFSG (Barrierefreiheitsstärkungsgesetz, in force since 2025-06-28)
- [ ] Determine applicability: B2C e-commerce, booking/reservation systems,
      and consumer-facing digital services generally in scope
      (micro-enterprise exemption < 10 employees AND ≤ 2M € turnover —
      services only). Document the assessment either way.
- [ ] If in scope: WCAG 2.1 AA conformance (EN 301 549) — run the
      `accessibility` skill and fix blockers
- [ ] "Erklärung zur Barrierefreiheit" (accessibility statement) published

## B. Technical

### Security & transport
- [ ] SSL certificate valid for apex + www; auto-renewal configured
- [ ] HTTP → HTTPS redirect; no mixed content (check console)
- [ ] Security headers: HSTS, X-Content-Type-Options, Referrer-Policy,
      sensible CSP (or documented why not)

### Redirects & URLs
- [ ] Relaunch: every indexed old URL 301-mapped (crawl old site / Search
      Console export first); spot-check top-20 pages
- [ ] www vs non-www: one canonical host, the other redirects
- [ ] Trailing-slash behavior consistent
- [ ] Custom 404 page: helpful, branded, links back; returns real 404 status

### Discoverability
- [ ] `robots.txt` present and NOT blocking the site (the classic
      staging-robots-goes-live failure — check explicitly)
- [ ] No stray `noindex` from staging (meta or X-Robots-Tag)
- [ ] XML sitemap generated, referenced in robots.txt, submitted to Search
      Console; contains only canonical, 200-status URLs
- [ ] Canonical tags correct; per-page unique titles + meta descriptions
- [ ] OG tags + Twitter cards on all shareable pages; og:image exists in
      1200×630 and actually renders (test with a share debugger)
- [ ] Favicon set + web manifest; schema markup for the business type
      (LocalBusiness with NAP for local clients)

### Function & content
- [ ] All forms submit successfully AND the mail/CRM actually receives them
      (send real test submissions)
- [ ] All internal links + nav work; no dead anchors; external links open
      correctly
- [ ] Real content everywhere: no lorem ipsum, placeholder images, or
      example@... addresses; phone numbers and opening hours correct
- [ ] Analytics installed, consent-gated, and recording (verify a test
      pageview post-consent); goals/conversions configured

### Ops
- [ ] Backup/rollback plan for the cutover; DNS TTL lowered in advance
- [ ] Monitoring/uptime check on the live URL
- [ ] Post-launch hour-one verification list ready (live URL mobile+desktop,
      forms, consent, Search Console sitemap fetch)

## Output format

```markdown
# Launch-Checkliste — {project} — {date}
## Ergebnis: GO / NO-GO (Blocker: n)
| # | Item | Status | Evidenz/Notiz |
...
## Blocker (müssen vor Launch behoben werden)
## Empfehlungen (nach Launch)
```

Write the client-facing report in the client's language. This checklist is a
practical launch aid, not legal advice — recommend a lawyer's review for
regulated industries (health, finance, legal services).
