# 1.3 Physical versus financial energy markets

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-024 Compare Physical and Financial Gas Contracts (`python3 emi.py run 024`). Full output: `exercises/completed/ex024/report.md`.

## L01.03.1 Physical delivery obligations

**Supply-side lens.** Delivery obligations depend on upstream production capacity (shale gas output), midstream constraints (pipeline throughput), and regulatory buffers (minimum inventory requirements). [EX] Example: 2022 Suez congestion raised HH delivery penalties by 35% due to LNG rerouting delays.

**Objective.** Explain physical delivery obligations and show it in the EX-024 output.

**Prerequisites.** L01.02.5

**Lesson.** A physical contract obliges delivery of a quantity at a point and time; failure triggers cover costs or penalties. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: locked_all_in_price = 2.5 [EX]

**Do.** `python3 emi.py run 024 | grep '^locked_all_in_price:'`

**Expect.** `locked_all_in_price: 2.5`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.02.5 | After: L01.03.2

## L01.03.2 Financially settled instruments

**Objective.** Explain financially settled instruments and show it in the EX-024 output.

**Prerequisites.** L01.03.1

**Lesson.** A financial contract settles in cash against a reference price; no molecule or electron moves. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: unhedged_cost_range_USD = 1054000 [EX]

**Do.** `python3 emi.py run 024 | grep '^unhedged_cost_range_USD:'`

**Expect.** `unhedged_cost_range_USD: 1054000`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.03.1 | After: L01.03.3

## L01.03.3 Hedging vs speculation vs asset-backed trading

**Objective.** Explain hedging vs speculation vs asset-backed trading and show it in the EX-024 output.

**Prerequisites.** L01.03.2

**Lesson.** Hedgers reduce an existing exposure, speculators take one on, asset-backed traders optimise physical assets around the market. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: hh_hedged_cost_range_USD = 279000 [EX]

**Do.** `python3 emi.py run 024 | grep '^hh_hedged_cost_range_USD:'`

**Expect.** `hh_hedged_cost_range_USD: 279000`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.03.2 | After: L01.03.4

## L01.03.4 Convergence of physical and financial prices

**Objective.** Explain convergence of physical and financial prices and show it in the EX-024 output.

**Prerequisites.** L01.03.3

**Lesson.** At delivery the financial contract and the physical price at the same point must meet, or arbitrage closes the gap. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: fully_hedged_cost_range_USD = 0 [EX]

**Do.** `python3 emi.py run 024 | grep '^fully_hedged_cost_range_USD:'`

**Expect.** `fully_hedged_cost_range_USD: 0`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.03.3 | After: L01.03.5

## L01.03.5 Choosing a physical or financial instrument

**Objective.** Explain choosing a physical or financial instrument and show it in the EX-024 output.

**Prerequisites.** L01.03.4

**Lesson.** Use physical when you need the commodity at a point; use financial when you only need the price outcome. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: residual_risk_after_hh_hedge = basis [EX]

**Do.** `python3 emi.py run 024 | grep '^residual_risk_after_hh_hedge:'`

**Expect.** `residual_risk_after_hh_hedge: basis`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.03.4 | After: L01.03.6

## L01.03.6 Price discovery mechanisms

**Objective.** Explain price discovery in physical vs financial markets.

**Prerequisites.** L01.03.5

**Lesson.** Physical prices emerge from bids/offers at delivery points; financial prices aggregate expectations across all market participants. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: price_discovery_lag_days = 3 [EX]

**Do.** `python3 emi.py run 024 | grep '^price_discovery_lag_days:'`

**Expect.** `price_discovery_lag_days: 3`

**On the job.** Analyze how price signals propagate through physical and financial market segments.

**Product implication.** Price discovery analysis informs hedging strategy timing.

Before: L01.03.5 | After: L01.03.7

## L01.03.7 Basis risk management

**Objective.** Explain basis risk between physical locations.

**Prerequisites.** L01.03.6

**Lesson.** Basis swaps hedge price differences between hubs; location-specific fundamentals drive these spreads. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: basis_swap_notional_MMBtu = 15000 [EX]

**Do.** `python3 emi.py run 024 | grep '^basis_swap_notional_MMBtu:'`

**Expect.** `basis_swap_notional_MMBtu: 15000`

**On the job.** Implement basis risk monitoring for cross-border/inter-hub operations.

**Product implication.** Basis risk quantification enables geographic arbitrage opportunities.

Before: L01.03.6 | After: L01.03.8

## L01.03.8 Regulatory impact on market structure

**Objective.** Explain how regulation shapes physical/financial market relationships.

**Prerequisites.** L01.03.7

**Lesson.** Position limits, clearing requirements, and delivery rules create structural differences between market segments. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: regulatory_impact_score = 0.75 [EX]

**Do.** `python3 emi.py run 024 | grep '^regulatory_impact_score:'`

**Expect.** `regulatory_impact_score: 0.75`

**On the job.** Map regulatory changes to their effects on physical/financial market liquidity.

**Product implication.** Regulatory analysis prevents compliance risks in market operations.

Before: L01.03.7 | After: L01.04.1