# 3.3 Cash markets and monthly index pricing

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-024 Compare Physical and Financial Gas Contracts (`python3 emi.py run 024`). Full output: `exercises/completed/ex024/report.md`.

## L03.03.1 Day-ahead cash trading

**Objective.** Explain day-ahead cash trading and show it in the EX-024 output.

**Prerequisites.** L03.02.5

**Lesson.** Day-ahead cash gas trades for next-day flow at each location. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: locked_all_in_price = 2.5 [EX]

**Do.** `python3 emi.py run 024 | grep '^locked_all_in_price:'`

**Expect.** `locked_all_in_price: 2.5`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.02.5 | After: L03.03.2

## L03.03.2 Bidweek and monthly index

**Objective.** Explain bidweek and monthly index and show it in the EX-024 output.

**Prerequisites.** L03.03.1

**Lesson.** Bidweek deals at the end of a month set the monthly index for the next one. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: unhedged_cost_range_USD = 1054000 [EX]

**Do.** `python3 emi.py run 024 | grep '^unhedged_cost_range_USD:'`

**Expect.** `unhedged_cost_range_USD: 1054000`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.03.1 | After: L03.03.3

## L03.03.3 Gas Daily vs Inside FERC style indices

**Objective.** Explain gas Daily vs Inside FERC style indices and show it in the EX-024 output.

**Prerequisites.** L03.03.2

**Lesson.** Daily indices average each day's cash trades; monthly indices come from bidweek. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: hh_hedged_cost_range_USD = 279000 [EX]

**Do.** `python3 emi.py run 024 | grep '^hh_hedged_cost_range_USD:'`

**Expect.** `hh_hedged_cost_range_USD: 279000`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.03.2 | After: L03.03.4

## L03.03.4 Index vs fixed price deals

**Objective.** Explain index vs fixed price deals and show it in the EX-024 output.

**Prerequisites.** L03.03.3

**Lesson.** An index deal floats with the published price; a fixed-price deal locks it. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: fully_hedged_cost_range_USD = 0 [EX]

**Do.** `python3 emi.py run 024 | grep '^fully_hedged_cost_range_USD:'`

**Expect.** `fully_hedged_cost_range_USD: 0`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.03.3 | After: L03.03.5

## L03.03.5 Index exposure in a book

**Objective.** Explain index exposure in a book and show it in the EX-024 output.

**Prerequisites.** L03.03.4

**Lesson.** A book's index exposure is the volume that will price at a not-yet-known index. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: residual_risk_after_hh_hedge = basis [EX]

**Do.** `python3 emi.py run 024 | grep '^residual_risk_after_hh_hedge:'`

**Expect.** `residual_risk_after_hh_hedge: basis`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.03.4 | After: L03.04.1
