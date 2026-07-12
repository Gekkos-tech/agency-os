---
description: Run the monthly maintenance loop — drift check, CWV spot-check, function re-test, client report
argument-hint: [live URL or project path]
---

Run the MAINTAIN loop for: $ARGUMENTS

Load the `agency-workflow` skill (MAINTAIN phase reference) and execute the
monthly sequence:

1. **Drift check** — run the installed SEO audit skill in drift mode against
   the stored baseline (meta, schema, robots, canonicals, content changes).
   No baseline yet? Capture one now and say so — the first report establishes
   the reference, it can't diff.
2. **Performance spot-check** — `core-web-vitals` on the top pages; compare
   against the QA-report baseline, flag regressions with numbers.
3. **Function re-test** — forms deliver, key flows complete, no new console
   errors (use `webapp-testing` where an environment allows).
4. **Content & legal freshness** — contact data/hours/prices current;
   privacy policy still matches the third-party services actually loaded;
   SSL validity.
5. **Write the report** — `docs/reports/{YYYY-MM}.md` in the client's
   language: non-technical summary first (3 sentences max), then checked /
   changed / fixed / recommended, each with evidence. Update
   `docs/project-state.md` (phase MAINTAIN, next cadence date).

Close by telling the user: the verdict in one line, regressions found (if
any), and whether the baseline was updated or preserved.
