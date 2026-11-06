# Measuring success

## Coding-agent experiment

Keep coding-agent performance separate from the product's paper-trading results.
Create one record per task/run from TASK_TEMPLATE.md. Record:
- Tool and exact model/version/settings when visible; otherwise unknown.
- Task and acceptance criteria declared before implementation.
- Starting commit, scope, and allowed tools.
- Start/end timestamps, elapsed time, and human review time when measured.
- Interventions: clarifications, redirected attempts, and human code corrections.
- Checks with command, exit status, and evidence.
- Independent review findings, rework cycles, regressions, and final outcome.
- API cost/token usage only when actually supplied by a provider or tool.
- Linked commit/PR and relevant artifacts, with secrets removed.

First-pass success = tasks accepted on the first submitted candidate without
corrective rework / completed tasks with an evaluated first candidate.
Report abandoned, blocked, and failed tasks separately to avoid survivorship bias.
Report the number of tasks and task complexity alongside any aggregate.

Do not call a cross-tool comparison controlled unless tasks, initial state,
acceptance criteria, permissions, and budgets are comparable. Record tool
limitations and learning effects. Do not infer productivity gains without a
measured comparison baseline. Avoid claiming agents wrote 100% of the project
unless the evidence supports that statement.

## Product experiment

See PROJECT.md for the accepted 30-day budget, target, and baseline.
Before collection begins, freeze eligibility, position limits, fee assumptions,
research budgets, fill rules, and the treatment of unresolved positions.
Do not let later evidence or settlement data enter earlier decisions.

Track source support and freshness, fabricated/unsupported claims, correct skip
behavior, and research usefulness; review approximately 20 answers.
Report calibration metrics only when there are sufficient resolved probability
forecasts and describe sample size. Never present the 15% target as a result.

## Bootstrap verification boundary

The repository check verifies instruction imports, workflow-copy consistency,
required files, and Python syntax. It does not test any market integration,
research quality, profitability, or installed coding tool. There is no product
test suite or completed product experiment at bootstrap.
