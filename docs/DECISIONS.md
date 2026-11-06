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

## November 5, 2026 — Reusable product manager and proposed backlog

Implement the requested product manager role as a repository-local skill in
the existing shared workflow system, with context in docs/product/BRIEF.md and
stable epic/story IDs in docs/product/BACKLOG.md. This is invocable planning
guidance, not an additional runtime LLM service or unattended worker. Generate
the Claude copy through the existing sync script. Use explicit file loading
where native discovery is unverified.

Keep accepted product scope separate from proposed delivery decomposition.
Do not revive historical NBA-only, weather-first or named-provider proposals.
Preserve the agreed offline first milestone as MM-101. Recommend a bounded
single research workflow initially; multi-agent runtime architecture is an
optional idea, not a settled requirement.

The full prospective evaluation requires 30 days after collection readiness.
No delivery dates, accepted story assignments, paid-call budgets, or experiment
parameters are set by this planning change. Resolve those decisions before
dependent execution, without blocking unrelated offline work.
