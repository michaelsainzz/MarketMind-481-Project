---
name: implement-task
description: Implement a scoped MarketMind feature or fix with observable acceptance criteria, meaningful checks, and an honest task evidence record.
---

# Implement a task

1. Read AGENTS.md, PROJECT.md, STATUS.md, and the current task/issue.
2. Inspect the working tree. Identify acceptance criteria and affected behavior.
   Make routine choices within scope; surface only material blockers.
3. Use a focused branch or assigned worktree. Record the starting commit,
   tool/model when visible, and time only when measured in a task record.
4. Implement the smallest complete change. For external integrations, check
   current primary docs; use injectable adapters and offline fixtures.
5. Exercise meaningful acceptance cases and relevant failures. Report unrun
   checks as unrun. Do not weaken tests just to pass.
6. Inspect the diff for secrets, unrelated edits, accidental generated files,
   and misleading claims. Run python scripts/check_repo.py from the repo root.
7. Update STATUS.md and the task record. Capture human interventions, failures,
   usage costs when available, and unresolved limitations.
8. Publish a PR with verification evidence. Follow the standing user authorization
   in AGENTS.md to merge when the final change and relevant local/required CI
   checks are ready, unless the active task says otherwise. Honor branch protections
   and resolve actionable findings. Report review limitations honestly; self-review
   is not independent validation. Do not request merge permission already granted.

Paths in these steps are relative to the repository root; project documents
are under docs/. Use docs/TASK_TEMPLATE.md to start a record.
