# Phase 7 — MAINTAIN (the loop after launch)

Goal: keep the live site healthy, catch regressions before the client does,
and turn the launch into a retainer relationship. This phase never "exits" —
it loops monthly (or per the retainer agreement).

## Set up once (launch week)

1. **Baselines** — capture reference states to diff against later:
   - SEO drift baseline via `seo-audit` (drift mode) for the key pages
   - Core Web Vitals numbers from the QA report as the performance baseline
   - A full-page screenshot set per template (desktop + mobile)
2. **Monitoring** — uptime check on the live URL, form-delivery test contact,
   SSL expiry reminder, domain/DNS renewal dates in the handover doc.
3. **Retainer scope** — write down what maintenance includes (updates, content
   changes, reports) and what is billed separately. Ambiguity here is where
   agencies lose money.

## Monthly loop (or per retainer cadence)

Run `/monthly-report` — it executes this sequence:

1. **Drift check** — `seo-audit` drift mode against the stored baseline:
   did meta tags, schema, robots, canonicals, or content change unexpectedly?
2. **Performance spot-check** — `core-web-vitals` on the top pages; compare
   against baseline, flag regressions.
3. **Function re-test** — forms still deliver, reservation/checkout flows
   still complete, no new console errors.
4. **Content & legal freshness** — opening hours/prices still correct,
   Impressum/privacy policy still match reality (new tools added? new
   processors?), certificate valid.
5. **Report** — write `docs/reports/YYYY-MM.md` in the client's language:
   what was checked, what changed, what was fixed, recommendations. Short,
   evidence-based, non-technical summary at the top.

## After every deploy (not just monthly)

- Rerun the drift check immediately — deploys are when regressions happen.
- Update the baseline deliberately after intended changes, so the next diff
  is clean. Never let the baseline drift silently.

## When MAINTAIN escalates

- Broad visual/quality decay → route back through `redesign` (design-foundation)
- Ranking losses → full `seo-audit`
- New features → open a fresh BUILD increment (plan-before-code applies again)
- Legal changes (new laws, new site features) → rerun `pre-launch-checklist`
  sections A on the affected items
