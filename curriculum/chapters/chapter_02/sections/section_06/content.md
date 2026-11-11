# 2.6 Pipeline topology, capacity, and constraints

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-014 Analyze Pipeline Capacity (`python3 emi.py run 014`). Full output: `exercises/completed/ex014/report.md`.

## L02.06.1 Nameplate vs operational capacity

**Objective.** Explain nameplate vs operational capacity and show it in the EX-014 output.

**Prerequisites.** L02.05.5

**Lesson.** Nameplate is design capacity; operational capacity is what the pipeline can move today. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: Permian_to_Gulf_utilization_pct = 99.459459 [EX]

**Do.** `python3 emi.py run 014 | grep '^Permian_to_Gulf_utilization_pct:'`

**Expect.** `Permian_to_Gulf_utilization_pct: 99.459459`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.05.5 | After: L02.06.2

## L02.06.2 Contracted vs available capacity

**Objective.** Explain contracted vs available capacity and show it in the EX-014 output.

**Prerequisites.** L02.06.1

**Lesson.** Contracted capacity is sold under firm agreements; available capacity is what remains to sell. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: Appalachia_to_NE_utilization_pct = 78.666667 [EX]

**Do.** `python3 emi.py run 014 | grep '^Appalachia_to_NE_utilization_pct:'`

**Expect.** `Appalachia_to_NE_utilization_pct: 78.666667`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.06.1 | After: L02.06.3

## L02.06.3 Throughput and utilization

**Objective.** Explain throughput and utilization and show it in the EX-014 output.

**Prerequisites.** L02.06.2

**Lesson.** Utilisation is scheduled volume divided by operational capacity. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: Midcon_to_Chicago_utilization_pct = 64 [EX]

**Do.** `python3 emi.py run 014 | grep '^Midcon_to_Chicago_utilization_pct:'`

**Expect.** `Midcon_to_Chicago_utilization_pct: 64`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.06.2 | After: L02.06.4

## L02.06.4 Bottlenecks and constraint points

**Objective.** Explain bottlenecks and constraint points and show it in the EX-014 output.

**Prerequisites.** L02.06.3

**Lesson.** A constraint point is a segment or compressor that fills before the rest of the system. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: Rockies_to_West_utilization_pct = 100.555556 [EX]

**Do.** `python3 emi.py run 014 | grep '^Rockies_to_West_utilization_pct:'`

**Expect.** `Rockies_to_West_utilization_pct: 100.555556`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.06.3 | After: L02.06.5

## L02.06.5 Constraint impact on price

**Objective.** Explain constraint impact on price and show it in the EX-014 output.

**Prerequisites.** L02.06.4

**Lesson.** When a constraint binds, prices upstream fall and prices downstream rise. [K]

**Example.** EX-014 (Analyze Pipeline Capacity) on synthetic North American data: constrained_segments = Permian_to_Gulf [EX]

**Do.** `python3 emi.py run 014 | grep '^constrained_segments:'`

**Expect.** `constrained_segments: Permian_to_Gulf`

**On the job.** Compare nameplate capacity, operational capacity, contracted capacity, available capacity, and actual throughput.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.06.4 | After: L02.07.1
