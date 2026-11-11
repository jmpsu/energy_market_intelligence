# 2.5 Interstate and intrastate pipeline infrastructure

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-018 Build a North American Gas Infrastructure Network (`python3 emi.py run 018`). Full output: `exercises/completed/ex018/report.md`.

## L02.05.1 Interstate pipeline regulation

**Objective.** Explain interstate pipeline regulation and show it in the EX-018 output.

**Prerequisites.** L02.04.5

**Lesson.** Interstate pipelines are FERC-regulated open-access carriers that sell transport, not gas. [K]

**Example.** EX-018 (Build a North American Gas Infrastructure Network) on synthetic North American data: nodes = 11 [EX]

**Do.** `python3 emi.py run 018 | grep '^nodes:'`

**Expect.** `nodes: 11`

**On the job.** Represent production basins, processing plants, pipelines, storage facilities, LNG terminals, and market hubs as a connected network.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.04.5 | After: L02.05.2

## L02.05.2 Intrastate systems and Texas

**Objective.** Explain intrastate systems and Texas and show it in the EX-018 output.

**Prerequisites.** L02.05.1

**Lesson.** Intrastate systems, large in Texas, operate under state rules. [K]

**Example.** EX-018 (Build a North American Gas Infrastructure Network) on synthetic North American data: edges = 12 [EX]

**Do.** `python3 emi.py run 018 | grep '^edges:'`

**Expect.** `edges: 12`

**On the job.** Represent production basins, processing plants, pipelines, storage facilities, LNG terminals, and market hubs as a connected network.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.05.1 | After: L02.05.3

## L02.05.3 Major long-haul corridors

**Objective.** Explain major long-haul corridors and show it in the EX-018 output.

**Prerequisites.** L02.05.2

**Lesson.** A few long-haul corridors move gas from producing basins to demand centres and export points. [K]

**Example.** EX-018 (Build a North American Gas Infrastructure Network) on synthetic North American data: most_central_node = HUB_GULF [EX]

**Do.** `python3 emi.py run 018 | grep '^most_central_node:'`

**Expect.** `most_central_node: HUB_GULF`

**On the job.** Represent production basins, processing plants, pipelines, storage facilities, LNG terminals, and market hubs as a connected network.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.05.2 | After: L02.05.4

## L02.05.4 Receipt and delivery points

**Objective.** Explain receipt and delivery points and show it in the EX-018 output.

**Prerequisites.** L02.05.3

**Lesson.** Shippers put gas in at receipt points and take it out at delivery points named in their contract. [K]

**Example.** EX-018 (Build a North American Gas Infrastructure Network) on synthetic North American data: max_flow_to_LNG_GULF_Bcf_d = 12 [EX]

**Do.** `python3 emi.py run 018 | grep '^max_flow_to_LNG_GULF_Bcf_d:'`

**Expect.** `max_flow_to_LNG_GULF_Bcf_d: 12`

**On the job.** Represent production basins, processing plants, pipelines, storage facilities, LNG terminals, and market hubs as a connected network.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.05.3 | After: L02.05.5

## L02.05.5 Interconnects and market centers

**Objective.** Explain interconnects and market centers and show it in the EX-018 output.

**Prerequisites.** L02.05.4

**Lesson.** Interconnects and market centres let gas change pipelines and are where hubs form. [K]

**Example.** EX-018 (Build a North American Gas Infrastructure Network) on synthetic North American data: max_flow_to_MEXICO_EXPORT_Bcf_d = 6 [EX]

**Do.** `python3 emi.py run 018 | grep '^max_flow_to_MEXICO_EXPORT_Bcf_d:'`

**Expect.** `max_flow_to_MEXICO_EXPORT_Bcf_d: 6`

**On the job.** Represent production basins, processing plants, pipelines, storage facilities, LNG terminals, and market hubs as a connected network.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.05.4 | After: L02.06.1
