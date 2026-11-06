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

## Standing authorization — finish repository tasks through merge

User clarified that assigned tasks include merging ready changes unless otherwise
specified. Commit and push focused changes, open a PR, verify the final diff and
relevant local/required CI checks, resolve findings, and merge under that standing
authorization. Respect branch protections and explicit task exceptions. Preserve
honest review evidence; this authorization does not turn self-review into an
independent review or authorize unrelated actions.

## November 6, 2026 — PM-led development orchestration

Michael requested specialized roles, parallel execution and cross-checking so
he can direct the project through ideas. Authorize the PM to coordinate
specialized development agents within invoked project sessions. Preserve
exploration-only intent; build requests permit bounded delivery through the
existing PR/merge workflow. Use dependency-aware work splits, isolated concurrent
writers, a separate reviewer and verification of the combined result.

Keep one accountable PM and one owner per task. Use roles as needed rather than
launching a fixed large team. If review or delegation tools are unavailable,
report that honestly and leave orchestrated merges review-pending. No provider
diversity, product success, speedup or autonomous background service is implied.
The bounded product research workflow and external-action/spending constraints
remain unchanged. Operational details are in ORCHESTRATION.md.
