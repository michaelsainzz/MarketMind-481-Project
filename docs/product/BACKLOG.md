# MarketMind epics and stories

Version 1 — November 5, 2026. This is a proposed delivery backlog derived from the accepted scope, not a record of shipped features or approved sprint commitments. All application stories are unimplemented. Suggested leads reflect PROJECT.md and do not assign people without their agreement.

## Reading and prioritization

P0: unlock the first complete, trustworthy journey or the experiment. P1: complete the accepted experience after that foundation. P2: optional extension. Priority is ordering, not permission to remove accepted scope. Ready means acceptance and inputs are sufficient to begin; Proposed needs refinement; Blocked identifies a material decision/dependency. Technical enablers are explicitly labeled. No points, dates, or velocity are invented.

Basis: **Proposal** = Create Proposal Draft user direction; **Repo** = PROJECT/DEVELOPMENT/EVALUATION/AGENTS requirements; **PM** = recommended implementation slice. See BRIEF.md for traceability and unresolved decisions D1–D7. Dependencies below are prerequisite deliverables; mock work can happen earlier but does not satisfy a live acceptance criterion.

## Epic map

| Epic | Outcome | Priority | Suggested lead | Completion evidence |
| --- | --- | --- | --- | --- |
| E1 Contract foundation | Trustworthy contract representations, snapshots and reproducible offline work | P0 | Dustin | Validated fixture -> detail output -> persisted snapshot |
| E2 Discovery and watchlist | Find relevant contracts across topics and retain research intent | P0/P1 | Jeremy | Multi-category feed -> saved contract/question -> reopen |
| E3 Bounded evidence research | Investigate rules using tools within explicit limits | P0 | Michael | Auditable research with sources, stop reason and safe failures |
| E4 Explainable guidance | Understand YES/NO/skip using evidence and deterministic costs | P0 | Michael + Dustin | Reproducible decision snapshot with appropriate abstention |
| E5 Research dashboard and picks | Browse refreshed opportunities and daily/weekly research | P1 | Jeremy + Michael | End-to-end scrolling interface and inspectable picks |
| E6 Paper portfolio | Record realistic simulated positions and settlement | P0 | Dustin | Reconciled cash/positions, no impossible fills |
| E7 Prospective evaluation | Measure the hypothesis fairly over 30 days | P0 | Dustin + team | Frozen protocol, timestamped collection and honest report |
| E8 Agent development and delivery | Demonstrate engineering contribution with evidence | P0/P1 | Team | Reproducible demo, task evidence and reviewed handoffs |

## E1 — Contract foundation

### MM-101 — Inspect one validated offline contract

As a researcher, I want a trustworthy contract detail view so I can understand what must happen for settlement before researching it.

P0 · **Ready** · Lead: Dustin · Basis: Repo first milestone · Dependencies: none. Technical enabler.

Acceptance:
- A documented offline command runs without keys/network on Python 3.11+ and displays a clearly synthetic fixture, contract ID, event, full rules, YES/NO executable quotes and available quantities, quote time, close time and expected settlement time.
- Price units and timezone-aware time ordering are explicit. Prices and quantities are validated; missing rules and malformed quotes produce actionable errors. Do not require YES/NO purchase quotes to sum to one.
- Output lists unanswered research questions without claiming a completed investigation. Checks cover malformed quotes, missing rules and invalid time ordering; task evidence and STATUS are updated.

### MM-102 — Read available contracts and quote snapshots

As a browser, I want current contract data across topics so I can choose a real contract to investigate.

P0 · **Blocked: MM-101** · Lead: Dustin · Basis: Proposal + Repo · Dependencies: MM-101. Technical enabler.

Acceptance:
- Check current primary Kalshi documentation and record endpoint, field, price-unit and access assumptions before integration; do not guess fees or authentication.
- Normalize supported available contracts into the validated representation, preserving rules, lifecycle status, retrieval/quote timestamps and obtainable executable side prices/quantities. Missing tradability data remains explicit and ineligible for fills.
- Handle pagination, rate limits, empty data and unavailable API without fabricating contracts or labeling old data current. Offline adapter fixtures cover at least two topics and representative failures; a real read smoke test is recorded when access permits.

### MM-103 — Preserve contract and decision history

As an evaluator, I want immutable historical snapshots so refreshes cannot rewrite the information behind an earlier decision.

P0 · **Blocked: MM-101** · Lead: Dustin · Basis: Repo + PM · Dependencies: MM-101. Technical enabler.

Acceptance:
- Persist contract/rule versions and timestamped quote snapshots in the selected local storage (SQLite proposed), with stable IDs linkable from research and paper decisions.
- A changed rule or price creates a new version; reopening the store reproduces earlier snapshots. A failed write is reported and cannot create a partially accepted decision.
- Export non-secret records to CSV with units/timezones and schema/version context; repeated reads do not duplicate snapshots inadvertently.

## E2 — Discovery and watchlist

### MM-201 — Browse day/week/month opportunities

As a user, I want to scroll and filter available contracts across topics and horizons so I can find relevant opportunities.

P0 · **Blocked: MM-102, D3** · Lead: Jeremy · Basis: Proposal · Dependencies: MM-102; resolve D3.

Acceptance:
- Show contract identity, topic, status, close/expected settlement time and quote freshness with day/week/month filters whose boundaries and timezone are visible.
- Filtering works on at least two available topics without a hardcoded NBA/weather constraint; a missing horizon timestamp is labeled and handled by the declared rule.
- Empty, loading and failed-feed states are distinguishable. Pagination/scrolling preserves filters and does not duplicate entries.

### MM-202 — Save a contract and personal research intent

As a user, I want to save an interesting contract and explain my question so the research responds to what I actually want to learn.

P0 · **Blocked: MM-103, MM-201** · Lead: Jeremy · Basis: Proposal · Dependencies: MM-103, MM-201.

Acceptance:
- Save, reopen and remove a watchlist entry; duplicate saves do not duplicate the contract. The saved question persists independently of refreshed market data.
- Open the saved contract with its question and start a linked research request; a closed/unavailable contract remains inspectable with its current status.
- Text such as “60% chance” is stored as user intent, never silently converted into a verified probability or executable quote.

## E3 — Bounded evidence research

### MM-301 — Resolve provider access and research budgets

As the team, we want explicit integration and spending assumptions so we can build a feasible research workflow.

P0 · **Proposed** · Lead: Michael · Basis: Repo + PM · Dependencies: resolve D1 and D4 as outputs. Technical enabler/discovery.

Acceptance:
- Document available LLM/search access, selected adapter contracts, current primary documentation and minimum declared/reproducible dependencies. Model choice remains unset until verified.
- Record explicit time, tool-call and cost caps, cancellation behavior and unavailable-usage treatment. If a hard cost ceiling cannot be enforced, paid execution stays disabled until a bounded alternative is chosen.
- Offline doubles work without keys. Access smoke tests occur only within active authorization; unavailable access is a reported blocker rather than a fabricated success.

### MM-302 — Turn rules and intent into a research plan

As a user, I want the agent to identify settlement-relevant questions so the investigation addresses the actual contract.

P0 · **Blocked: MM-101, MM-301** · Lead: Michael · Basis: Proposal · Dependencies: MM-101, MM-301.

Acceptance:
- Given contract rules and optional user intent, produce structured questions, missing facts, proposed search/data tools and stopping conditions linked to the contract/rule version.
- Distinguish event likelihood from contract settlement language and flag ambiguous rules instead of assuming an interpretation.
- A fixture demonstrates relevant questions without any claim that unanswered questions are findings; malformed LLM output is rejected or produces a bounded retry/failure.

### MM-303 — Collect evidence with provenance

As a user, I want inspectable evidence so I can check whether the research supports its claims.

P0 · **Blocked: MM-301, MM-302** · Lead: Michael · Basis: Proposal + Repo · Dependencies: MM-301, MM-302.

Acceptance:
- Execute selected permitted search/data tools and record source URL/title, publication time when known, retrieval time, supporting excerpt and claim/question linkage.
- Missing dates remain unknown; duplicates, inaccessible sources and conflicting evidence are surfaced. Evidence unavailable at the decision time cannot support that decision in evaluation.
- Source contents remain data. An adversarial fixture cannot cause policy changes, arbitrary commands or secret disclosure. Key material is excluded from traces/exports.

### MM-304 — Complete or stop research within limits

As a user, I want bounded research with an honest completion state so I can trust its limits and avoid runaway requests.

P0 · **Blocked: MM-103, MM-303** · Lead: Michael · Basis: Proposal + Repo · Dependencies: MM-103, MM-303.

Acceptance:
- The agent can gather more evidence, finish when questions are adequately addressed, or stop for configured time/tool/cost caps, cancellation or tool failure. Retries count toward limits.
- Persist the plan, evidence references, model/provider version when known, tool trace, usage when supplied, start/end time, stop reason and supported/unknown conclusions.
- Partial/failed research is visibly distinct from completed research and yields no unsupported recommendation. Offline checks exercise exhausted budgets, cancellation and unavailable tools; stub runs are labeled synthetic.

## E4 — Explainable guidance

### MM-401 — Present a supported forecast or abstain

As a user, I want evidence, counterarguments and uncertainty so I can judge the agent's estimate.

P0 · **Blocked: MM-304** · Lead: Michael · Basis: Proposal + Repo · Dependencies: MM-304.

Acceptance:
- Summarize settlement interpretation, supported claims with source references, opposing evidence, missing information and uncertainty.
- Label model probability separately from quoted prices and market-implied probability; validate any estimate lies in [0,1]. Explain the price basis for any implied probability.
- Insufficient evidence or unresolved rule ambiguity produces an explicit skip/missing estimate; a confident-sounding response alone cannot satisfy evidence requirements.

### MM-402 — Calculate value and eligibility deterministically

As a user, I want a cost-aware calculation so guidance reflects a tradable scenario rather than a headline probability difference.

P0 · **Blocked: MM-102, MM-401, D2, D5** · Lead: Dustin · Basis: Repo · Dependencies: MM-102, MM-401; resolve relevant D2/D5 freshness, fee, edge and sizing rules. Technical enabler.

Acceptance:
- Python computes side-specific expected payoff, entry cost, applicable fees/estimated execution costs and eligible quantity using explicit units and versioned policy; the LLM does not supply calculated totals.
- YES/NO/skip applies the declared evidence, edge, freshness, liquidity and capital constraints. Missing fees, stale quotes or insufficient depth cannot become an apparently executable opportunity.
- Independently worked examples cover both sides, boundary probabilities, fee rounding and an apparent gross edge eliminated by costs. An absent estimate yields skip.

### MM-403 — Record an explainable decision snapshot

As a user and evaluator, I want the exact basis of YES/NO/skip preserved so I can revisit why that decision was made.

P0 · **Blocked: MM-103, MM-402** · Lead: Michael + Dustin · Basis: Repo + PM · Dependencies: MM-103, MM-402.

Acceptance:
- Persist decision time, contract/rule/quote versions, evidence, estimate or absence, deterministic outputs, reason codes and policy version for every YES/NO/skip.
- Later quotes, evidence and settlements do not mutate earlier records; recomputing from the snapshot reproduces calculations.
- Guidance can be viewed without opening a paper position. Re-running research creates a new decision with traceable lineage.

## E5 — Research dashboard and picks

### MM-501 — Inspect research in the scrolling dashboard

As a user, I want contract detail, research and guidance connected so I can move from discovery to an informed paper decision.

P1 · **Blocked: MM-202, MM-403** · Lead: Jeremy · Basis: Proposal · Dependencies: MM-202, MM-403.

Acceptance:
- Streamlit connects feed/watchlist -> contract rules -> request/status -> evidence/uncertainty -> decision, preserving the selected contract and question.
- Plotly compares quotes, implied probability and model estimates with clear units and labels; unavailable estimates remain absent. Synthetic and live runs are visibly distinguished.
- Research failures and skips offer a useful explanation; UI reruns do not accidentally start duplicate paid requests or paper positions.

### MM-502 — Refresh quotes while preserving research context

As a user, I want refreshed quotes and visible freshness so I know when a researched opportunity has changed.

P1 · **Blocked: MM-102, MM-501, D2** · Lead: Jeremy + Dustin · Basis: Proposal · Dependencies: MM-102, MM-501; resolve D2.

Acceptance:
- Refresh at the declared interval while the application is active; show quote time, last refresh and errors. Do not claim a real-time guarantee.
- A changed/stale quote invalidates current action eligibility until recalculated; retain the original research/decision snapshots alongside refreshed values.
- Check rate limiting, lost connectivity and repeated Streamlit reruns without duplicated refresh loops or misleading freshness.

### MM-503 — Produce daily and weekly researched picks

As a user, I want a bounded set of researched opportunities so I can discover contracts I did not save myself.

P1 · **Blocked: MM-201, MM-304, MM-403, D4** · Lead: Michael + Jeremy · Basis: Proposal · Dependencies: MM-201, MM-304, MM-403; resolve D4.

Acceptance:
- A manual daily/weekly run selects candidates by the declared, recorded policy and obeys total run and per-contract budgets; persist candidate exclusions and run time.
- Picks link to full evidence and decision snapshots; no qualifying opportunity produces “no qualifying picks” with reasons. No quota forces trades.
- Display current quotes separately from original decision quotes and recheck eligibility before paper execution. Repeated runs do not duplicate existing run records accidentally.
- Unattended scheduling remains disabled until separately authorized and operational limits are configured.

## E6 — Paper portfolio

### MM-601 — Define and fund a paper portfolio

As an evaluator, I want an auditable contribution ledger so performance is measured against actual available capital.

P0 · **Blocked: MM-103, D5** · Lead: Dustin · Basis: Repo · Dependencies: MM-103; resolve D5 ledger, timing and rounding policy.

Acceptance:
- Over 30 days accrue exactly $1,000/7 per day internally with a declared exact/rounding representation; display approximately $4,285.71 total. Restarting cannot add a second contribution for the same day.
- Distinguish contributions, available cash, committed capital, realized results and unresolved positions; capital is an allowance, not a required daily spend.
- Validate position and aggregate exposure limits from the frozen configuration. No order-submission API or live credentials are required.

### MM-602 — Simulate a position from executable quotes

As a paper trader, I want realistic simulated fills so reported performance does not rely on unavailable prices or quantities.

P0 · **Blocked: MM-403, MM-601, D5** · Lead: Dustin · Basis: Repo · Dependencies: MM-403, MM-601; resolve D5 fill policy.

Acceptance:
- Before opening, validate decision eligibility against the recorded execution quote, freshness, depth, capital and limits. Record execution time, side, price, quantity, costs and rejected/partial/unfilled outcomes under the declared policy.
- Last-trade prices cannot stand in for executable quotes. A changed quote requires recalculation and a linked execution snapshot; fills never exceed recorded available quantity.
- Repeated commands cannot double-fill an intent or overspend. Worked scenarios cover insufficient capital, stale prices, partial/no liquidity and fee-inclusive debits.

### MM-603 — Settle and reconcile positions

As a paper trader, I want resolved outcomes and unresolved risk separated so the ledger accurately reflects results.

P0 · **Blocked: MM-102, MM-602** · Lead: Dustin · Basis: Repo · Dependencies: MM-102, MM-602.

Acceptance:
- Hold positions to official settlement; record authoritative outcome/status evidence and apply the documented payout treatment, including void/cancel cases rather than assuming a binary win/loss.
- Settlement is idempotent and reconciles cash, costs and realized results. Expected settlement dates are not treated as actual outcomes.
- At experiment end report delayed/unresolved positions separately, valued with conservative available exit quotes and their timestamps; missing exit liquidity is explicit, not fabricated cash or automatic profit.

## E7 — Prospective evaluation

### MM-701 — Freeze the experiment protocol

As the team, we want a predeclared experiment so later outcomes cannot change the rules of comparison.

P0 · **Proposed** · Lead: Dustin + team · Basis: Repo · Dependencies: resolve D5, D6, D7 as outputs. Planning can start now.

Acceptance:
- Version the 30-day window, eligible contracts scheduled to settle within it, contribution timing, selection, position/exposure caps, edge thresholds, fees, execution costs, fill rules, research caps and unresolved valuation.
- Define a deterministic market-favorite baseline with matched eligible opportunities, decision times, budget and cost assumptions, including ties, missing quotes and skip handling.
- Define approximately 20-answer source/fact/usefulness/missing-information review sampling and rubric; declare forecast metric eligibility and sample reporting. Confirm calendar feasibility without inventing a course deadline.
- Changes after collection starts create a new protocol version/cohort and are disclosed; do not rewrite earlier decisions.

### MM-702 — Collect prospective decisions and baseline observations

As an evaluator, I want timestamped observations from both policies so results use only information available at each decision.

P0 · **Blocked: MM-403, MM-503, MM-603, MM-701** · Lead: Dustin + Michael · Basis: Repo · Dependencies: MM-403, MM-503, MM-603, MM-701.

Acceptance:
- Readiness rehearsal demonstrates research, executable quote capture, baseline decisions, paper ledger and outcome ingestion before the 30-day clock starts. The cadence can be manually operated; record gaps explicitly.
- Capture decisions/skips/failures and baseline actions prospectively with matching opportunity sets, timestamps, immutable snapshots and policy versions. Prevent future evidence/outcomes from entering earlier decisions.
- Store per-run coverage, missing data and supplied research usage/costs; unknown costs remain unknown. If collection starts late, report the actual shorter window rather than implying 30 days.

### MM-703 — Report performance and research quality

As the team and course reviewer, we want a reproducible result so we can assess what MarketMind actually achieved.

P0 · **Blocked: MM-702 and observation window** · Lead: Dustin + team · Basis: Repo · Dependencies: MM-702 and sufficient elapsed collection time.

Acceptance:
- Reproduce net gain on contributions after trading fees/estimated execution costs against the 15% target and market-favorite baseline. Show contribution totals, realized results, unresolved valuation, denominators and sample sizes.
- Report LLM/search costs separately and a second result after them; if costs are unknown, state that the all-cost result cannot yet be established.
- Report source support, factual errors/fabrication, usefulness, missing-information handling, skips/failures and sampled answer count. Only compute probability/calibration metrics for a declared sufficient resolved sample.
- Include negative results, missing coverage, uncertainty and limitations. Synthetic runs and interim reports cannot be described as a completed prospective experiment or validation of future profitability.

## E8 — Agent development and delivery

### MM-801 — Record and review agent-driven development

As the team, we want task evidence and human review so our portfolio claims about agent engineering are defensible.

P0 · **Ready** · Lead: Team · Basis: Repo · Dependencies: none. Recurring practice, foundation already exists; not a claim that native tools are verified.

Acceptance:
- For an implementation task, declare criteria before coding; record starting commit, accountable owner, tool/model/settings when visible, interventions, actual checks, unknown costs/timing and outcome in TASK_TEMPLATE format.
- Use a focused branch and reviewable handoff. A separate reviewer records findings when available; self-review is labeled accordingly. Record failed/blocked/abandoned runs rather than omitting them.
- Smoke-test instruction/skill loading in each installed coding tool before claiming native compatibility. Do not infer development speedup without measured comparison evidence.

### MM-802 — Deliver a reproducible demo and report

As a course reviewer or portfolio reader, I want a documented end-to-end demonstration so I can understand our contribution and reproduce it.

P1 · **Blocked: MM-501, MM-603** · Lead: Team · Basis: Repo + PM · Dependencies: MM-501, MM-603; final experiment claims additionally depend on MM-703.

Acceptance:
- A fresh checkout has exact dependencies, configuration instructions and a deterministic offline demo through contract -> evidence fixture -> labeled guidance -> paper ledger. Live mode prerequisites and failures are separately documented.
- Explain architecture, tools/algorithms, original integration/contribution, human ownership, AI assistance and reused-code attribution. Include checks and current limitations.
- Present final prospective results only when MM-703 is complete; otherwise show clearly dated interim evidence and the remaining collection plan.

## Proposed release sequence

| Milestone | Demonstrable outcome | Exit stories |
| --- | --- | --- |
| M0 Offline foundation | Synthetic contract can be validated, inspected and saved | MM-101, MM-103; MM-801 evidence |
| M1 Single-contract research | Real contract -> bounded sourced investigation -> recorded guidance | MM-102, MM-301–304, MM-401–403 |
| M2 User experience and paper loop | Browse/save/research plus refreshed quotes, picks and reconciled paper portfolio | MM-201–202, MM-501–503, MM-601–603 |
| M3 Prospective experiment | Frozen protocol and reliable prospective collection | MM-701 early, then MM-702 after readiness rehearsal |
| M4 Evidence and delivery | Honest comparison, source review and reproducible demo/report | MM-703, MM-802 |

Sequence is dependency-based, not a calendar promise. MM-301 and MM-701 discovery can start alongside M0 planning; fee/threshold choices must precede MM-402 and fills. A basic UI shell can use fixtures early, but live acceptance requires real dependencies. Revisit whether all of M2 must precede collection if timing is tight; any reduced collection path needs an explicit protocol decision, not a silent dependency bypass.

Next implementation: **MM-101**, matching the existing DEVELOPMENT.md prompt. In parallel planning (without launching agents), resolve API access/budget and experiment calendar. Native tool discovery can be checked when each tool is available.

## Deferred ideas

Optional P2 candidates, not accepted commitments: multiple runtime forecasting agents/ensembles, extra random/LLM-only baselines, category-specific predictive models, automated monthly research, production hosting and unattended scheduling. Create stories only when there is evidence of value and capacity. Live real-money execution is outside the project scope, not a deferred MVP feature.

## Shared completion rule

A story is Done only when its criteria are demonstrated, meaningful failure checks pass, documentation and STATUS are accurate, and evidence links identify the implementation/checks and review state. Repository foundation checks alone never establish product behavior. Proposed owners, estimates and dates require real team planning; no story here is a sprint commitment.
