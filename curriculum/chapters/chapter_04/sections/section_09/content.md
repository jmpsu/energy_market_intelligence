# 4.9 Global Henry Hub, TTF, and JKM relationships

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-034 Compare Henry Hub, TTF, and JKM (`python3 emi.py run 034`). Full output: `exercises/completed/ex034/report.md`.

## L04.09.1 Global benchmark definitions

**Objective.** Explain global benchmark definitions and show it in the EX-034 output.

**Prerequisites.** L04.08.5

**Lesson.** TTF is the European gas benchmark; JKM is the Northeast Asian LNG benchmark. [K]

**Example.** EX-034 (Compare Henry Hub, TTF, and JKM) on synthetic North American data: months = 36 [EX]

**Do.** `python3 emi.py run 034 | grep '^months:'`

**Expect.** `months: 36`

**On the job.** Analyze the relationship between North American, European, and Asian gas benchmarks.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.08.5 | After: L04.09.2

## L04.09.2 Arbitrage and netback spreads

**Objective.** Explain arbitrage and netback spreads and show it in the EX-034 output.

**Prerequisites.** L04.09.1

**Lesson.** The export arbitrage is open when the netback to the US Gulf exceeds Henry Hub-based cost. [K]

**Example.** EX-034 (Compare Henry Hub, TTF, and JKM) on synthetic North American data: mean_ttf_minus_hh = 4.970833 [EX]

**Do.** `python3 emi.py run 034 | grep '^mean_ttf_minus_hh:'`

**Expect.** `mean_ttf_minus_hh: 4.970833`

**On the job.** Analyze the relationship between North American, European, and Asian gas benchmarks.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.09.1 | After: L04.09.3

## L04.09.3 Shipping and tolling wedges

**Objective.** Explain shipping and tolling wedges and show it in the EX-034 output.

**Prerequisites.** L04.09.2

**Lesson.** Shipping and tolling are the wedges between destination price and US price. [K]

**Example.** EX-034 (Compare Henry Hub, TTF, and JKM) on synthetic North American data: corr_hh_ttf_changes = -0.191259 [EX]

**Do.** `python3 emi.py run 034 | grep '^corr_hh_ttf_changes:'`

**Expect.** `corr_hh_ttf_changes: -0.191259`

**On the job.** Analyze the relationship between North American, European, and Asian gas benchmarks.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.09.2 | After: L04.09.4

## L04.09.4 Price transmission and decoupling

**Objective.** Explain price transmission and decoupling and show it in the EX-034 output.

**Prerequisites.** L04.09.3

**Lesson.** Regional prices connect when cargoes can move and decouple when capacity is full. [K]

**Example.** EX-034 (Compare Henry Hub, TTF, and JKM) on synthetic North American data: corr_ttf_jkm_changes = 0.913289 [EX]

**Do.** `python3 emi.py run 034 | grep '^corr_ttf_jkm_changes:'`

**Expect.** `corr_ttf_jkm_changes: 0.913289`

**On the job.** Analyze the relationship between North American, European, and Asian gas benchmarks.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.09.3 | After: L04.09.5

## L04.09.5 Spread scenario analysis

**Objective.** Explain spread scenario analysis and show it in the EX-034 output.

**Prerequisites.** L04.09.4

**Lesson.** Spread scenarios show which destination pulls cargoes and when lifting stops. [K]

**Example.** EX-034 (Compare Henry Hub, TTF, and JKM) on synthetic North American data: months_full_cost_arb_open = 15 [EX]

**Do.** `python3 emi.py run 034 | grep '^months_full_cost_arb_open:'`

**Expect.** `months_full_cost_arb_open: 15`

**On the job.** Analyze the relationship between North American, European, and Asian gas benchmarks.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.09.4 | After: L04.10.1
