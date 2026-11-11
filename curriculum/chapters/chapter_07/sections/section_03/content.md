# 7.3 Gas-fired generation economics

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-061 Optimize a Natural Gas-Fired Generator (`python3 emi.py run 061`). Full output: `exercises/completed/ex061/report.md`.

## L07.03.1 Combined-cycle vs peaker economics

**Objective.** Explain combined-cycle vs peaker economics and show it in the EX-061 output.

**Prerequisites.** L07.02.5

**Lesson.** A combined cycle has higher capital cost and lower heat rate than a peaker, so it runs more hours. [K]

**Example.** EX-061 (Optimize a Natural Gas-Fired Generator) on synthetic North American data: marginal_cost_USD_per_MWh = 26.4 [EX]

**Do.** `python3 emi.py run 061 | grep '^marginal_cost_USD_per_MWh:'`

**Expect.** `marginal_cost_USD_per_MWh: 26.4`

**On the job.** Determine when a generator should operate based on gas prices, electricity prices, heat rate, and operating constraints.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.02.5 | After: L07.03.2

## L07.03.2 Start-up and cycling costs

**Objective.** Explain start-up and cycling costs and show it in the EX-061 output.

**Prerequisites.** L07.03.1

**Lesson.** Each start costs fuel and wear; cycling raises maintenance. [K]

**Example.** EX-061 (Optimize a Natural Gas-Fired Generator) on synthetic North American data: committed_start_hour = 1 [EX]

**Do.** `python3 emi.py run 061 | grep '^committed_start_hour:'`

**Expect.** `committed_start_hour: 1`

**On the job.** Determine when a generator should operate based on gas prices, electricity prices, heat rate, and operating constraints.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.03.1 | After: L07.03.3

## L07.03.3 Capacity factor drivers

**Objective.** Explain capacity factor drivers and show it in the EX-061 output.

**Prerequisites.** L07.03.2

**Lesson.** Capacity factor depends on where the unit sits in the merit order. [K]

**Example.** EX-061 (Optimize a Natural Gas-Fired Generator) on synthetic North American data: committed_end_hour = 24 [EX]

**Do.** `python3 emi.py run 061 | grep '^committed_end_hour:'`

**Expect.** `committed_end_hour: 24`

**On the job.** Determine when a generator should operate based on gas prices, electricity prices, heat rate, and operating constraints.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.03.2 | After: L07.03.4

## L07.03.4 Fuel supply arrangements

**Objective.** Explain fuel supply arrangements and show it in the EX-061 output.

**Prerequisites.** L07.03.3

**Lesson.** Fuel can be firm, interruptible or bought daily. [K]

**Example.** EX-061 (Optimize a Natural Gas-Fired Generator) on synthetic North American data: committed_run_hours = 24 [EX]

**Do.** `python3 emi.py run 061 | grep '^committed_run_hours:'`

**Expect.** `committed_run_hours: 24`

**On the job.** Determine when a generator should operate based on gas prices, electricity prices, heat rate, and operating constraints.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.03.3 | After: L07.03.5

## L07.03.5 Unit margin analysis

**Objective.** Explain unit margin analysis and show it in the EX-061 output.

**Prerequisites.** L07.03.4

**Lesson.** Unit margin is power revenue less fuel, variable O&M and start costs. [K]

**Example.** EX-061 (Optimize a Natural Gas-Fired Generator) on synthetic North American data: committed_profit_USD = 408700 [EX]

**Do.** `python3 emi.py run 061 | grep '^committed_profit_USD:'`

**Expect.** `committed_profit_USD: 408700`

**On the job.** Determine when a generator should operate based on gas prices, electricity prices, heat rate, and operating constraints.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.03.4 | After: L07.04.1
