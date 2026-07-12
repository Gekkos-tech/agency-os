# agency-os eval suite

Behavioral eval cases for `claude plugin eval` (early access). Each case is a
`prompt.md` (the user message) plus `graders/criteria.md` (what a passing
response looks like). The five cases mirror the launch acceptance tests:
correct skill triggering and correct output shape.

Run locally from the repo root, e.g.:

    claude plugin eval agency-core@agency-os --case trigger-new-project
    claude plugin eval seo-marketing@agency-os --case trigger-seo-audit

Note: evals call the model and are therefore NOT run in CI — CI covers the
deterministic layer (`claude plugin validate --strict` + repo consistency
checks via `scripts/validate_frontmatter.py`).
