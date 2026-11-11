# 4.5 Capacity release and secondary markets

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-014 Analyze Pipeline Capacity (`python3 emi.py run 014`). Full output: `exercises/completed/ex014/report.md`.

## L04.05.1 Capacity release mechanics

**Objective.** Explain capacity release mechanics and show it in the EX-014 output.

**Prerequisites.** L04.04.5

**Lesson.** A firm shipper can release unused capacity to another shipper for a period. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: Permian_to_Gulf_utilization_pct = 99.459459 [EX]

**Do.** `python3 emi.py run 014 | grep '^Permian_to_Gulf_utilization_pct:'`

**Expect.** `Permian_to_Gulf_utilization_pct: 99.459459`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.04.5 | After: L04.05.2

## L04.05.2 Asset management agreements

**Objective.** Explain asset management agreements and show it in the EX-014 output.

**Prerequisites.** L04.05.1

**Lesson.** In an asset management agreement a marketer runs a holder's capacity and shares the value. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: Appalachia_to_NE_utilization_pct = 78.666667 [EX]

**Do.** `python3 emi.py run 014 | grep '^Appalachia_to_NE_utilization_pct:'`

**Expect.** `Appalachia_to_NE_utilization_pct: 78.666667`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.05.1 | After: L04.05.3

## L04.05.3 Biddable vs prearranged releases

**Objective.** Explain biddable vs prearranged releases and show it in the EX-014 output.

**Prerequisites.** L04.05.2

**Lesson.** Releases are either posted for bidding or prearranged with a named replacement shipper. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: Midcon_to_Chicago_utilization_pct = 64 [EX]

**Do.** `python3 emi.py run 014 | grep '^Midcon_to_Chicago_utilization_pct:'`

**Expect.** `Midcon_to_Chicago_utilization_pct: 64`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.05.2 | After: L04.05.4

## L04.05.4 Valuing released capacity

**Objective.** Explain valuing released capacity and show it in the EX-014 output.

**Prerequisites.** L04.05.3

**Lesson.** Released capacity is worth about the expected spread it can capture. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: Rockies_to_West_utilization_pct = 100.555556 [EX]

**Do.** `python3 emi.py run 014 | grep '^Rockies_to_West_utilization_pct:'`

**Expect.** `Rockies_to_West_utilization_pct: 100.555556`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.05.3 | After: L04.05.5

## L04.05.5 Secondary market strategy

**Objective.** Explain secondary market strategy and show it in the EX-014 output.

**Prerequisites.** L04.05.4

**Lesson.** Secondary capacity lets you get transport without a long-term contract. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: constrained_segments = Permian_to_Gulf [EX]

**Do.** `python3 emi.py run 014 | grep '^constrained_segments:'`

**Expect.** `constrained_segments: Permian_to_Gulf`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.05.4 | After: L04.06.1
