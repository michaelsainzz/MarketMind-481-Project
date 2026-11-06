# Decisions

## Bootstrap: shared instructions and repository workflows

Keep shared rules in AGENTS.md. Use CLAUDE.md and GEMINI.md imports.
Keep canonical SKILL.md workflows in .agents/skills and generate ordinary copies
for Claude discovery. Avoid manually maintained duplicate instructions.

Use Python 3.11+ and standard-library checks at bootstrap. Introduce application
dependencies, provider adapters, and a reproducible dependency lock when they
are needed by implementation tasks.

Keep coding-agent evaluation separate from product evaluation. Use recorded
evidence and explicit unknowns; start with a single accountable implementation
agent per task and a distinct review pass.

Runtime provider/model/search choice, API access, and experiment position limits
remain undecided. Do not silently treat these as configured.
