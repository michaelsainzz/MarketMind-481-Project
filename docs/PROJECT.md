# Project scope

## Accepted direction

MarketMind: AI Market Research. The current project proposal supersedes the earlier CourtIQ NBA concept. This summary follows the revised proposal reviewed on November 5, 2026.

Build a Python application that:
- Browses available Kalshi contracts across topics, with day/week/month horizons.
- Saves contracts to a watchlist and accepts user-selected research questions.
- Uses an LLM to read settlement rules, create research questions, choose search/data tools, gather current evidence, and decide when to stop.
- Shows daily/weekly researched picks with YES, NO, or skip guidance.
- Shows sources, timestamps, uncertainty, and a separately labeled probability estimate when supported.
- Uses deterministic Python calculations for estimated value, costs, and paper-trading results.
- Presents a scrolling Streamlit dashboard with Plotly charts and periodically refreshed quotes.

Proposed storage: SQLite, with CSV exports. Provider, model, search service, and exact dependencies remain to be selected after access checks. Research requires explicit time, tool-call, and cost limits before enabling paid calls.

## Product evaluation

Run a prospective 30-day paper-trading test. Add an exact $1,000 / 7 daily allowance, approximately $4,285.71 over 30 days. Budget is available capital, not a daily trading requirement. Predeclare position and selection rules.

The project target is a 15% gain on contributions after trading fees and estimated execution costs (approximately $642.86 profit, $4,928.57 final value). Report LLM/search costs separately and also show performance after those costs. This is a benchmark, not an established capability.

Use recorded executable prices and quantities. Hold to settlement and choose contracts scheduled to settle within the window. Report delayed/unresolved positions separately with conservative available exit quotes. Compare against a market-favorite baseline with matching eligible contracts, timing, budget, and costs. Review about 20 research answers for source support, factual accuracy, usefulness, and missing-information handling.

## Team

| Member | Primary focus |
| --- | --- |
| Michael Angelo Sainz | LLM integration, agent tools, research workflow |
| Jeremy Pham | Streamlit interface, graphics, Plotly |
| Dustin Demetria | Market data, paper trading, evaluation |

Everyone shares development direction, review, testing, documentation, and presentation. Preserve human ownership and credit AI assistance and reused code.

## First implementation milestone

A single offline contract fixture travels through a validated data model to a readable contract detail output. No API keys or live network needed. The fixture must be clearly synthetic; it is not evidence of market or investment performance.
