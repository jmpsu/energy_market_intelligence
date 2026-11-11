# 4.10 Infrastructure disruption and scenario analysis

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-036 Simulate a Winter Gas Supply Disruption (`python3 emi.py run 036`). Full output: `exercises/completed/ex036/report.md`.

## L04.10.1 Outage scenario design

**Objective.** Explain outage scenario design and show it in the EX-036 output.

**Prerequisites.** L04.09.5

**Lesson.** An outage scenario states which asset fails, by how much and for how long. [K]

**Example.** EX-036 (Simulate a Winter Gas Supply Disruption) on synthetic North American data: peak_demand_Bcf_d = 25.26 [EX]

**Do.** `python3 emi.py run 036 | grep '^peak_demand_Bcf_d:'`

**Expect.** `peak_demand_Bcf_d: 25.26`

**On the job.** Model how extreme weather, production declines, pipeline constraints, and storage withdrawals affect regional markets.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.09.5 | After: L04.10.2

## L04.10.2 Rerouting and alternative paths

**Objective.** Explain rerouting and alternative paths and show it in the EX-036 output.

**Prerequisites.** L04.10.1

**Lesson.** Gas reroutes over alternative paths until they fill. [K]

**Example.** EX-036 (Simulate a Winter Gas Supply Disruption) on synthetic North American data: peak_day = 4 [EX]

**Do.** `python3 emi.py run 036 | grep '^peak_day:'`

**Expect.** `peak_day: 4`

**On the job.** Model how extreme weather, production declines, pipeline constraints, and storage withdrawals affect regional markets.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.10.1 | After: L04.10.3

## L04.10.3 Storage response

**Objective.** Explain storage response and show it in the EX-036 output.

**Prerequisites.** L04.10.2

**Lesson.** Storage near the market covers the gap up to its deliverability. [K]

**Example.** EX-036 (Simulate a Winter Gas Supply Disruption) on synthetic North American data: production_lost_Bcf = 9 [EX]

**Do.** `python3 emi.py run 036 | grep '^production_lost_Bcf:'`

**Expect.** `production_lost_Bcf: 9`

**On the job.** Model how extreme weather, production declines, pipeline constraints, and storage withdrawals affect regional markets.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.10.2 | After: L04.10.4

## L04.10.4 Price and basis impacts

**Objective.** Explain price and basis impacts and show it in the EX-036 output.

**Prerequisites.** L04.10.3

**Lesson.** What cannot be rerouted shows up as price spikes and wider basis. [K]

**Example.** EX-036 (Simulate a Winter Gas Supply Disruption) on synthetic North American data: total_shortfall_Bcf = 6.8 [EX]

**Do.** `python3 emi.py run 036 | grep '^total_shortfall_Bcf:'`

**Expect.** `total_shortfall_Bcf: 6.8`

**On the job.** Model how extreme weather, production declines, pipeline constraints, and storage withdrawals affect regional markets.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.10.3 | After: L04.10.5

## L04.10.5 Winter disruption stress case

**Objective.** Explain winter disruption stress case and show it in the EX-036 output.

**Prerequisites.** L04.10.4

**Lesson.** A winter stress case combines high demand with lost supply on the same days. [K]

**Example.** EX-036 (Simulate a Winter Gas Supply Disruption) on synthetic North American data: shortfall_days = 3,4,5 [EX]

**Do.** `python3 emi.py run 036 | grep '^shortfall_days:'`

**Expect.** `shortfall_days: 3,4,5`

**On the job.** Model how extreme weather, production declines, pipeline constraints, and storage withdrawals affect regional markets.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.10.4 | After: L05.01.1
