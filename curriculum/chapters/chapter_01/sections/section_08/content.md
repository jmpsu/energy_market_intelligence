# 1.8 Energy commodities and financial instruments

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-024 Compare Physical and Financial Gas Contracts (`python3 emi.py run 024`). Full output: `exercises/completed/ex024/report.md`.

## L01.08.1 Commodity units and conversions

**Objective.** Explain commodity units and conversions and show it in the EX-024 output.

**Prerequisites.** L01.07.5

**Lesson.** Gas is priced per MMBtu, measured in Mcf or Bcf; power in MWh; NGLs in gallons or barrels. Conversions are the first check on any number. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: locked_all_in_price = 2.5 [EX]

**Do.** `python3 emi.py run 024 | grep '^locked_all_in_price:'`

**Expect.** `locked_all_in_price: 2.5`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.07.5 | After: L01.08.2

## L01.08.2 Futures and forwards

**Objective.** Explain futures and forwards and show it in the EX-024 output.

**Prerequisites.** L01.08.1

**Lesson.** A future is exchange-traded and margined; a forward is a bilateral contract for later delivery. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: unhedged_cost_range_USD = 1054000 [EX]

**Do.** `python3 emi.py run 024 | grep '^unhedged_cost_range_USD:'`

**Expect.** `unhedged_cost_range_USD: 1054000`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.08.1 | After: L01.08.3

## L01.08.3 Swaps and basis instruments

**Objective.** Explain swaps and basis instruments and show it in the EX-024 output.

**Prerequisites.** L01.08.2

**Lesson.** A swap exchanges a fixed price for a floating index; a basis instrument prices a location relative to a benchmark. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: hh_hedged_cost_range_USD = 279000 [EX]

**Do.** `python3 emi.py run 024 | grep '^hh_hedged_cost_range_USD:'`

**Expect.** `hh_hedged_cost_range_USD: 279000`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.08.2 | After: L01.08.4

## L01.08.4 Options and structured products

**Objective.** Explain options and structured products and show it in the EX-024 output.

**Prerequisites.** L01.08.3

**Lesson.** Options give the right, not the obligation, to buy or sell; structured products bundle several of these. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: fully_hedged_cost_range_USD = 0 [EX]

**Do.** `python3 emi.py run 024 | grep '^fully_hedged_cost_range_USD:'`

**Expect.** `fully_hedged_cost_range_USD: 0`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.08.3 | After: L01.08.5

## L01.08.5 Environmental and capacity products

**Objective.** Explain environmental and capacity products and show it in the EX-024 output.

**Prerequisites.** L01.08.4

**Lesson.** Capacity, renewable certificates and emissions allowances are separate products with their own prices. [K]

**Example.** EX-024 (Compare Physical and Financial Gas Contracts) on synthetic North American data: residual_risk_after_hh_hedge = basis [EX]

**Do.** `python3 emi.py run 024 | grep '^residual_risk_after_hh_hedge:'`

**Expect.** `residual_risk_after_hh_hedge: basis`

**On the job.** Model the cash flows and exposures associated with physical gas purchases, futures, swaps, and basis swaps.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.08.4 | After: L01.09.1
