# Agent development setup

## Instruction and skill routing

| Coding tool | Entry point | Workflow discovery |
| --- | --- | --- |
| OpenAI Codex | AGENTS.md | .agents/skills/<name>/SKILL.md |
| Claude Code | CLAUDE.md imports AGENTS.md | .claude/skills/<name>/SKILL.md (generated copies) |
| Gemini CLI | GEMINI.md imports AGENTS.md | .agents/skills/<name>/SKILL.md workspace alias |

`agents-skills.md` and `claude-skills.md` are not standard discovery names.
Keep always-needed rules short in AGENTS.md. Put reusable procedures in SKILL.md
files and growing project context in docs. An import points to instructions;
it does not grant filesystem/network permissions or start other agents.

The project skills are repository files, not personal ChatGPT skill installations.
When updating canonical workflows, run:

```bash
python scripts/sync_skills.py
python scripts/check_repo.py
```

Claude discovery copies are ordinary files so clones on Windows do not require
symlink support. The check rejects missing, modified, and obsolete copies.

## Environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python scripts/check_repo.py
```

The initial checks use only the standard library. Install dependencies and
configure providers only in the task that needs them. Authenticate Codex, Claude
Code, and Gemini CLI individually using each tool's official setup instructions;
this repository does not install them or share credentials between them.

In a fresh session, ask each coding tool to identify the project, shared
instructions, relevant skill path, and check command. For Claude inspect
`/memory`; for Gemini inspect `/memory show` and `/skills list`. Tool versions
and managed settings may change discovery behavior. Record actual tool/version
smoke-test results; filesystem checks alone do not establish that a tool loaded
these instructions.

## Git workflow

Initial bootstrap may populate main. Subsequent tasks:

```bash
git switch main
git pull --ff-only
git switch -c feat/contract-model
# Work, then inspect and stage only intended files.
git diff
git add <specific-files>
git commit -m "Add validated contract model and offline fixture"
git push -u origin feat/contract-model
```

Open a pull request with acceptance criteria and verification evidence. Branch
protection is recommended after the first push; it is not enabled by these files.
CI triggers on pushes and pull requests but does not block merges without
repository settings requiring the check. Use separate worktrees for simultaneous
agents; do not have GPT, Claude, and Gemini edit the same checkout concurrently.

## First implementation prompt

> Read AGENTS.md, docs/PROJECT.md, docs/STATUS.md, and the implement-task skill.
> Implement the first offline contract milestone. Create a validated Python
> contract model and a clearly synthetic fixture including contract ID, event,
> rules, YES/NO executable quotes with available quantities, quote timestamp,
> close time, and expected settlement time. Define price units explicitly and
> validate their ranges without assuming purchase prices must sum to one.
> Add an offline command that displays the contract and research questions it
> raises, without claiming to have researched them. Test malformed quotes,
> missing rules, and time ordering. No live API calls. Add one documented command
> to run it, update the task record and STATUS, and report the checks actually run.
> Work on feat/contract-model and prepare a reviewable pull request.

## References checked during bootstrap

- https://developers.openai.com/codex/guides/agents-md
- https://developers.openai.com/codex/skills
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/skills
- https://geminicli.com/docs/cli/gemini-md/
- https://geminicli.com/docs/cli/skills/
