# 2.4 Production, supply, and demand fundamentals

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-026 Analyze Henry Hub Price Sensitivity (`python3 emi.py run 026`). Full output: `exercises/completed/ex026/report.md`.

## L02.04.1 Supply stack components

**Objective.** Explain supply stack components and show it in the EX-026 output.

**Prerequisites.** L02.03.5

**Lesson.** Supply is production plus imports plus storage withdrawals. [K]

**Example.** EX-026 (Analyze Henry Hub Price Sensitivity) on synthetic North American data: Production_plus_2_price = 3.020005 [EX]

**Do.** `python3 emi.py run 026 | grep '^Production_plus_2_price:'`

**Expect.** `Production_plus_2_price: 3.020005`

**On the job.** Simulate how changes in production, LNG exports, weather, and storage affect benchmark prices.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.03.5 | After: L02.04.2

## L02.04.2 Demand sectors: res/com, industrial, power, exports

**Objective.** Explain demand sectors: res/com, industrial, power, exports and show it in the EX-026 output.

**Prerequisites.** L02.04.1

**Lesson.** Demand is residential/commercial, industrial, power burn, LNG and pipeline exports. [K]

**Example.** EX-026 (Analyze Henry Hub Price Sensitivity) on synthetic North American data: LNG_exports_plus_3_price = 3.619315 [EX]

**Do.** `python3 emi.py run 026 | grep '^LNG_exports_plus_3_price:'`

**Expect.** `LNG_exports_plus_3_price: 3.619315`

**On the job.** Simulate how changes in production, LNG exports, weather, and storage affect benchmark prices.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.04.1 | After: L02.04.3

## L02.04.3 Weather and degree days

**Objective.** Explain weather and degree days and show it in the EX-026 output.

**Prerequisites.** L02.04.2

**Lesson.** Heating and cooling degree days translate temperature into demand. [K]

**Example.** EX-026 (Analyze Henry Hub Price Sensitivity) on synthetic North American data: Cold_winter_price = 3.749143 [EX]

**Do.** `python3 emi.py run 026 | grep '^Cold_winter_price:'`

**Expect.** `Cold_winter_price: 3.749143`

**On the job.** Simulate how changes in production, LNG exports, weather, and storage affect benchmark prices.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.04.2 | After: L02.04.4

## L02.04.4 Weekly storage balance

**Objective.** Explain weekly storage balance and show it in the EX-026 output.

**Prerequisites.** L02.04.3

**Lesson.** The weekly storage change is the market's scorecard of the balance. [K]

**Example.** EX-026 (Analyze Henry Hub Price Sensitivity) on synthetic North American data: Mild_winter_price = 2.802438 [EX]

**Do.** `python3 emi.py run 026 | grep '^Mild_winter_price:'`

**Expect.** `Mild_winter_price: 2.802438`

**On the job.** Simulate how changes in production, LNG exports, weather, and storage affect benchmark prices.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.04.3 | After: L02.04.5

## L02.04.5 Building a supply-demand balance

**Objective.** Explain building a supply-demand balance and show it in the EX-026 output.

**Prerequisites.** L02.04.4

**Lesson.** A balance table that does not sum to zero has a data error or a missing flow. [K]

**Example.** EX-026 (Analyze Henry Hub Price Sensitivity) on synthetic North American data: Storage_deficit_refill_price = 3.369803 [EX]

**Do.** `python3 emi.py run 026 | grep '^Storage_deficit_refill_price:'`

**Expect.** `Storage_deficit_refill_price: 3.369803`

**On the job.** Simulate how changes in production, LNG exports, weather, and storage affect benchmark prices.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.04.4 | After: L02.05.1
