# Current handoff

## Bootstrap

- Product scope and agent development workflow documented.
- Shared AGENTS.md, Claude/Gemini import files, and two repository workflows added.
- Standard-library repository verification and GitHub Actions check added.
- Task/PR templates and development evaluation protocol added.
- Python 3.11 is the minimum project version.
- No product application, market data integration, runtime LLM integration,
  simulator, dashboard, or application dependency set exists yet.
- Native instruction/skill loading in installed Codex, Claude Code, and Gemini
  CLI has not been separately smoke-tested.
- No development speedup, research-quality result, or trading result is claimed.

## Next task

Implement the offline contract model and clearly synthetic fixture described
in DEVELOPMENT.md. Record its acceptance criteria and baseline before coding.

## Product planning — November 5, 2026

- Reviewed Project Proposal Strategy, Create Proposal Draft, and Set Up Agent
  Repo chat history against the repository scope and current implementation.
- Added a reusable repository-local marketmind-product-manager skill, with a
  generated Claude copy and explicit-read fallback. Native discovery remains
  unverified; no unattended agent or runtime integration was deployed.
- Added docs/product/BRIEF.md with source reconciliation and open decisions,
  and docs/product/BACKLOG.md with 8 proposed epics and 23 implementation,
  discovery and delivery stories. Acceptance criteria, dependencies, suggested
  leads and release gates are recorded; these are not sprint commitments.
- Next implementation is MM-101, the existing offline contract milestone.
  API access/budgets and experiment calendar/protocol can be refined now.
- A prospective 30-day evaluation begins after collection readiness, not at
  project bootstrap. The course deadline and experiment start remain unknown.
- Planning evidence: docs/tasks/PM-001.md. Product functionality remains absent.
