# PM-led development orchestration

## Intent and authorization

Michael directs MarketMind through product ideas. The PM translates that direction
into bounded, testable work and coordinates specialists during an invoked session.
This is standing authorization for development-agent delegation, parallel work
where useful, independent review, and the existing ready-change PR/merge workflow.
It does not require Michael to assign each agent or decide routine implementation
details. It does not start an unattended service or execute the whole backlog.

Interpret the current request before acting:
- “Explore this” or “what do you think?”: develop options, investigate feasibility,
  and recommend a slice; specialists may analyze in parallel, without implementing
  the proposed feature.
- “Build this” or “go ahead”: define observable acceptance, refine the backlog,
  and deliver the smallest coherent ready slice through review and integration.
- An ambiguous idea: develop a recommendation and do useful discovery; ask only
  if implementation intent or a material product choice remains unclear.
- “You may propose ideas”: recommend and evaluate ideas; permission to propose
  does not by itself authorize building every proposed feature.

Paid API/research spend, new credentials, deployments, unattended scheduling,
external messages/issues and real-money actions are not granted by delegation.
Existing PR authorization is retained. Preserve paper-only scope. Ask only for
unresolved choices required by the dependent work, while advancing independent
work. Do not assign dates or human commitments. Runtime product research agents
are a separate architecture decision from the coding agents in this workflow.

## Specialist roles

| Role | Responsibility | Expected handoff |
| --- | --- | --- |
| PM / coordinator | Value, scope, story readiness, task split, dependencies, integration and communication | Acceptance, task map, final evidence and next slice |
| Technical lead | Interfaces, schema, design risks and integration plan when complexity warrants it | Minimal design and contracts before dependent work |
| Implementation specialist | Data/backend, research tooling, UI or paper evaluation as needed | Focused diff/commit, behavior checks and limitations |
| QA / independent reviewer | Challenge acceptance, failures, regressions and unsupported claims | Findings, checks actually run, reviewed revision and disposition |

Roles are assignments to agents, not claims of separately installed tools or
human team ownership. Instantiate only the roles that help the task. A small
change can use one implementer and one separate reviewer; a shared-model reviewer
is still a separate agent, not proof of independent judgment or model diversity.
Do not claim GPT/Claude/Gemini participation unless each was actually invoked.

## Execution loop

1. Read current source-of-truth files and working-tree state. State the user
   outcome, boundaries, acceptance including relevant failures, and evidence
   required. Check story dependencies; blocked live work may have an explicitly
   labeled offline slice, but cannot be marked live-complete.
2. Record a task using TASK_TEMPLATE.md. Choose a small dependency graph and
   assign an accountable owner to each unit. Check delegation/tool availability.
   Start with one implementer plus reviewer; add parallel specialists only for
   independently useful work. Honor tool concurrency limits and avoid recursive
   fan-out; workers ask the PM before further delegation.
3. Give each worker the story/task ID, starting revision, outcome, constraints,
   inputs, agreed interfaces, allowed files, branch/worktree, dependencies,
   acceptance, checks and required return evidence. Workers report blockers and
   cannot expand scope, change shared interfaces or mark other tasks complete.
4. Resolve shared interfaces before parallel dependent implementation. Parallel
   read-only analysis is safe; simultaneous writers require separate worktrees
   and nonoverlapping ownership. The PM owns shared backlog, STATUS and decision
   files. If isolation is unavailable, serialize writes instead of sharing a
   mutable checkout. Do not have workers switch the coordinator's branch.
5. Integrate focused worker commits sequentially, preserving others' work.
   Resolve conflicts explicitly, inspect the combined diff, and run behavior and
   failure checks on the combined revision plus the repository foundation check.
   Passing isolated worker checks is insufficient to establish integration.
6. Send a separate reviewer the task, acceptance, final combined diff/revision,
   relevant code and raw check evidence. The reviewer must not have authored the
   reviewed changes. Use review-change; allow new tests/inspection and record
   failures. Reviewer agreement alone is not proof of correctness. Resolve
   actionable findings and obtain re-review of affected changes after fixes;
   rerun affected checks. If separate review is unavailable, mark review-pending
   and do not merge an orchestrated delivery as independently verified.
7. Verify the staged/final diff and required CI, honor branch protections, and
   publish/merge under standing authorization. Record the reviewed revision;
   after merge verify the merged result and applicable checks. Report actual
   publication blockers without claiming a local commit is a merged PR.
8. Update task evidence and STATUS with integrated checks, reviewer findings,
   final commit/PR, unknown metrics and limitations. Mark a story Done only on
   demonstrated acceptance. Tell Michael what works, what was verified, what
   remains blocked and the next useful slice.

## Bounded operation and failure handling

Keep each run within the active request and declared task scope; set a finite
worker/review plan. Default to one correction/re-review cycle, then reassess the
cause before retrying. Avoid repeated agent spawning or test retries without new
evidence. Record failure, blocked and abandoned work as well as successes. Stop
dependent work when required access or decisions are unavailable, report the
blocker, and continue useful independent work. Keep measurable model/time/cost
fields unknown when tooling does not expose them. Never guarantee correctness,
profitability, completion dates or a development speedup from agent count.

If delegation is unavailable, say so and prepare useful scoped work with honest
self-review labels; retain the separate review gate for orchestrated delivery.
Native cross-tool discovery and multi-writer product execution require actual
smoke tests before being reported as working. Documentation alone configures
instructions, not external tool installations.
