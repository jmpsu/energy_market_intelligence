# 3.4 Futures, swaps, options, and forwards

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-024 Compare Physical and Financial Gas Contracts (`python3 emi.py run 024`). Full output: `exercises/completed/ex024/report.md`.

## L03.04.1 Futures margining

**Objective.** Explain futures margining and show it in the EX-024 output.

**Prerequisites.** L03.03.5

**Lesson.** Futures are marked daily; losses must be covered with variation margin in cash. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: locked_all_in_price = 2.5 [EX]

**Do.** `python3 emi.py run 024 | grep '^locked_all_in_price:'`

**Expect.** `locked_all_in_price: 2.5`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.03.5 | After: L03.04.2

## L03.04.2 Fixed-for-floating swaps

**Objective.** Explain fixed-for-floating swaps and show it in the EX-024 output.

**Prerequisites.** L03.04.1

**Lesson.** A fixed-for-floating swap pays the difference between a fixed price and the index. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: unhedged_cost_range_USD = 1054000 [EX]

**Do.** `python3 emi.py run 024 | grep '^unhedged_cost_range_USD:'`

**Expect.** `unhedged_cost_range_USD: 1054000`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.04.1 | After: L03.04.3

## L03.04.3 Options: calls, puts, collars

**Objective.** Explain options: calls, puts, collars and show it in the EX-024 output.

**Prerequisites.** L03.04.2

**Lesson.** A call caps a buyer's price, a put floors a seller's, a collar does both at lower cost. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: hh_hedged_cost_range_USD = 279000 [EX]

**Do.** `python3 emi.py run 024 | grep '^hh_hedged_cost_range_USD:'`

**Expect.** `hh_hedged_cost_range_USD: 279000`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.04.2 | After: L03.04.4

## L03.04.4 Physical forwards and delivery terms

**Objective.** Explain physical forwards and delivery terms and show it in the EX-024 output.

**Prerequisites.** L03.04.3

**Lesson.** A physical forward specifies point, volume, term and delivery obligations. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: fully_hedged_cost_range_USD = 0 [EX]

**Do.** `python3 emi.py run 024 | grep '^fully_hedged_cost_range_USD:'`

**Expect.** `fully_hedged_cost_range_USD: 0`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.04.3 | After: L03.04.5

## L03.04.5 Instrument selection for a hedge

**Objective.** Explain instrument selection for a hedge and show it in the EX-024 output.

**Prerequisites.** L03.04.4

**Lesson.** Choose the instrument by what must be fixed: price, basis, volume or delivery. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: residual_risk_after_hh_hedge = basis [EX]

**Do.** `python3 emi.py run 024 | grep '^residual_risk_after_hh_hedge:'`

**Expect.** `residual_risk_after_hh_hedge: basis`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.04.4 | After: L03.05.1
