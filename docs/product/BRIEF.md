# MarketMind product brief

Planning baseline: November 5, 2026. Product scope is accepted in PROJECT.md; the delivery decomposition in BACKLOG.md is a PM recommendation for review. No application behavior is implemented. This brief is the maintained summary, not a transcript archive.

## Product outcome

Help a user investigate available Kalshi contracts and make an informed paper-trading decision from current evidence, settlement rules, prices, costs, and uncertainty. Test whether structured AI research produces useful guidance and better prospective results than the declared market-favorite baseline. Profitability is a hypothesis to evaluate.

Primary user: someone browsing opportunities who can also ask, “I like this contract because it appears to have a 60% chance; can the AI look deeper?” A displayed market price is not independently established event probability. Secondary users: the three student developers and evaluators who must reproduce decisions and explain the engineering contribution.

Core journey: browse day/week/month contracts -> save one with a research question -> inspect rules and evidence -> receive YES/NO/skip guidance -> record a paper decision -> follow settlement and evaluate results. Daily/weekly AI-researched picks provide another entry to the same journey. Monthly browsing is accepted; a separately automated monthly research service is not a current commitment.

## Source map and reconciliation

Reviewed the message history of these chats through the connected Codex app, plus repository files at starting commit `7586c603379e2b169699832acc62480764cfae9a`:

| Source | Evidence carried forward |
| --- | --- |
| Project Proposal Strategy, chat `6aea714b-a518-83e9-b226-f18fc9afff70` | User proposed testing information-driven decisions using AI research on Kalshi and agent-driven development. Earlier CourtIQ, NBA-first, named-provider, and multi-agent architecture suggestions are historical options, superseded where later direction differs. |
| Create Proposal Draft, chat `6aed133e-61ec-83e8-9ff2-a6334136fc86` | User requested generic “LLM” pending API access; no fixed categories; scrolling day/week/month contracts; selected-contract investigations; daily/weekly researched picks; refreshed odds; $1,000/week for 30 days and a 15% gain target. Added Dustin; Jeremy focuses on graphics, Michael on LLM work, with shared development. |
| Set Up Agent Repo, chat `6aed3cc5-d378-83e8-9b43-79a35b03d6ba` | User authorized the shared coding-agent foundation and measurement of agent-driven development. Chat reports bootstrap completion; local checkout confirms foundation files. This review did not rerun remote CI or native discovery. |
| PROJECT.md and EVALUATION.md | Repository makes the evaluation precise: exact $1,000/7 daily contributions, cost separation, executable quote/quantity evidence, prospective hold-to-settlement, matching baseline, source review, and an offline first milestone. |
| STATUS.md, DEVELOPMENT.md, AGENTS.md and repository inventory | Foundation only; first implementation is a validated synthetic contract and offline detail command. Python 3.11+, proposed Streamlit/Plotly/SQLite; providers and budgets unresolved. |

Proposal chat text and repository scope were reviewed. PDF exports in the parent output folder were not independently extracted or visually verified in this planning task. No private transcript or proposal export is copied into the repository.

## Accepted boundaries

- Browse available Kalshi contracts across categories. Supporting a category does not imply enough evidence to recommend every contract.
- Preserve settlement rules, source links, publication/retrieval times, quotes, quantities, and decision times.
- LLM handles research planning, tool selection, evidence synthesis, and uncertainty. Python calculates costs, value, budgets, and returns.
- Separate quotes, market-implied probability, and model estimates; allow missing estimates and explicit skips.
- Paper trading only. No live order execution.
- Use a scrolling Streamlit interface and Plotly charts, periodically refreshed quotes, persistent watchlist/research state, proposed SQLite and CSV exports.
- Prospective 30-day evaluation, daily capital allowance of exactly $1,000/7, about $4,285.71 total contributions. A 15% gain means about $642.86 profit / $4,928.57 ending value after trading fees and estimated execution costs. Show LLM/search costs separately and a second result after them. The benchmark is not proof of future profitability.
- Match eligible contracts, timing, budget, and costs for the market-favorite baseline; review approximately 20 research answers. Report unresolved positions, failures, skips, and sample size.
- Preserve shared human ownership and measure coding-agent work separately from product results.

## Recommended delivery approach

Deliver an offline vertical slice first, then a single-contract live-data/research path, then the broader feed and experiment. A stub response demonstrates wiring only. Broad discovery can ship before every category has useful research coverage. Start with one bounded research workflow; add providers or multiple runtime agents only when evidence justifies the complexity. Keep framework choices open.

Prefer manual/on-demand runs until budgets and collection procedures are agreed. Daily/weekly run support is a product requirement; enabling an unattended scheduler is a later authorization and operational choice.

The prospective experiment requires 30 calendar days after a functioning, frozen collection protocol exists. The earlier four-week schedule was an assistant suggestion, not a verified current deadline. Obtain the actual course due date before promising a final report with 30 days of observations. If necessary, deliver a clearly labeled interim result and continue collection; do not substitute hindsight testing or synthetic returns for prospective results.

## Open decisions

These block only dependent stories; the offline first milestone can proceed.

| ID | Decision | Suggested lead | Unblocks |
| --- | --- | --- | --- |
| D1 | Available LLM/search access, provider/model, limits and allowed spend | Michael | Real research integration |
| D2 | Refresh interval, stale-quote cutoff and tolerated data gaps | Dustin + Jeremy | Live UI and eligibility |
| D3 | Day/week/month boundary semantics and timezone; close vs expected settlement | Jeremy + Dustin | Horizon filtering |
| D4 | Research time/tool/cost ceilings and candidate selection policy per daily/weekly run | Michael | Bounded research and picks |
| D5 | Experiment start/end, contribution/rounding rules, position/exposure limits, edge thresholds, fees, fill rules, baseline selection/ties, unresolved valuation | Dustin + team | Prospective collection |
| D6 | Course deadline, team capacity, and whether complete 30-day results fit | Michael + team | Calendar commitments |
| D7 | Approximate 20-answer sample method, rubric and sufficient sample for calibration metrics | Team | Final evaluation |

Capture decisions when actually resolved; these are not approval gates for unrelated work.
