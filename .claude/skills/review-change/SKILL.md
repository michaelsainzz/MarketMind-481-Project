---
name: review-change
description: Review a MarketMind change against its task acceptance criteria, checking correctness, evidence integrity, market assumptions, and regression risks.
---

# Review a change

1. Read AGENTS.md, the task/acceptance criteria, diff, and relevant tests.
   Inspect changed behavior in its surrounding code.
2. Check correctness before style. For market/research changes, check price
   units, executable quotes and quantities, settlement rules, timestamp
   ordering, fee handling, missing-data/skip behavior, and future leakage.
3. Check that external documents cannot redirect tool use or disclose secrets.
   Check relevant edge cases and failure behavior.
4. Run relevant available checks. Distinguish a reproduced defect from a
   suspected risk and unavailable verification. Do not claim to run unavailable
   providers or to validate profitability from synthetic data.
5. Report actionable findings with severity, file location, concrete trigger,
   impact, and suggested correction. State no findings when none are supported.
6. Assess each acceptance criterion and record verification limitations.
   Record whether this was a separate agent/person or a self-review.
7. Do not modify implementation or merge as part of a review unless asked.
