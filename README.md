# MarketMind — AI Market Research

CPSC 481 portfolio project by Michael Angelo Sainz, Jeremy Pham, and Dustin Demetria.

MarketMind will research Kalshi event contracts, explain evidence and uncertainty, and evaluate recommendations through paper trading. Development is agent first: humans define outcomes and acceptance criteria; coding agents implement, check, and document changes.

**Status:** repository and agent environment only. Market ingestion, research tools, dashboard, and simulator are not implemented yet.

## Start here

- [Project scope](docs/PROJECT.md)
- [Shared agent instructions](AGENTS.md)
- [Agent setup and first task](docs/DEVELOPMENT.md)
- [Reusable workflow catalog](docs/SKILLS.md)
- [Evaluation plan](docs/EVALUATION.md)
- [Current handoff](docs/STATUS.md)

## Local environment

Use Python 3.11 or newer. No API keys or paid services are needed for foundation checks.

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python scripts/check_repo.py
```

Run coding tools from this repository root. Codex reads `AGENTS.md`; Claude Code and Gemini CLI have import files. These are coding-tool integrations, not automatic integrations in every GPT/Claude/Gemini chat product. Validate loading in each installed tool before claiming compatibility.

## Development loop

1. Define a task with observable acceptance criteria.
2. Give one coding agent ownership on a feature branch.
3. Implement and run relevant checks.
4. Have a separate reviewer examine the diff and evidence.
5. Record failures, human interventions, time, and available usage costs.
6. Submit a pull request linked to the task.

See `docs/DEVELOPMENT.md` for commands and a first prompt. No runtime LLM provider or model is selected yet.
