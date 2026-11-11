# 4.4 Available capacity and congestion

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-014 Analyze Pipeline Capacity (`python3 emi.py run 014`). Full output: `exercises/completed/ex014/report.md`.

## L04.04.1 Operationally available capacity

**Objective.** Explain operationally available capacity and show it in the EX-014 output.

**Prerequisites.** L04.03.5

**Lesson.** Operationally available capacity is what a pipeline posts as unscheduled at a point. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: Permian_to_Gulf_utilization_pct = 99.459459 [EX]

**Do.** `python3 emi.py run 014 | grep '^Permian_to_Gulf_utilization_pct:'`

**Expect.** `Permian_to_Gulf_utilization_pct: 99.459459`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.03.5 | After: L04.04.2

## L04.04.2 Scheduling cuts as congestion signal

**Objective.** Explain scheduling cuts as congestion signal and show it in the EX-014 output.

**Prerequisites.** L04.04.1

**Lesson.** Repeated scheduling cuts at a point signal a constraint. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: Appalachia_to_NE_utilization_pct = 78.666667 [EX]

**Do.** `python3 emi.py run 014 | grep '^Appalachia_to_NE_utilization_pct:'`

**Expect.** `Appalachia_to_NE_utilization_pct: 78.666667`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.04.1 | After: L04.04.3

## L04.04.3 Maintenance and outages

**Objective.** Explain maintenance and outages and show it in the EX-014 output.

**Prerequisites.** L04.04.2

**Lesson.** Planned maintenance is posted in advance and lowers capacity for a known period. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: Midcon_to_Chicago_utilization_pct = 64 [EX]

**Do.** `python3 emi.py run 014 | grep '^Midcon_to_Chicago_utilization_pct:'`

**Expect.** `Midcon_to_Chicago_utilization_pct: 64`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.04.2 | After: L04.04.4

## L04.04.4 Congestion and basis blowouts

**Objective.** Explain congestion and basis blowouts and show it in the EX-014 output.

**Prerequisites.** L04.04.3

**Lesson.** When a constraint tightens, basis on either side widens fast. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: Rockies_to_West_utilization_pct = 100.555556 [EX]

**Do.** `python3 emi.py run 014 | grep '^Rockies_to_West_utilization_pct:'`

**Expect.** `Rockies_to_West_utilization_pct: 100.555556`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.04.3 | After: L04.04.5

## L04.04.5 Capacity posting analysis

**Objective.** Explain capacity posting analysis and show it in the EX-014 output.

**Prerequisites.** L04.04.4

**Lesson.** Capacity postings let you see congestion before prices fully react. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: constrained_segments = Permian_to_Gulf [EX]

**Do.** `python3 emi.py run 014 | grep '^constrained_segments:'`

**Expect.** `constrained_segments: Permian_to_Gulf`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.04.4 | After: L04.05.1
