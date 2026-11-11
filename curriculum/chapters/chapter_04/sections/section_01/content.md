# 4.1 North American pipeline topology

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-018 Build a North American Gas Infrastructure Network (`python3 emi.py run 018`). Full output: `exercises/completed/ex018/report.md`.

## L04.01.1 Network representation: nodes and edges

**Objective.** Explain network representation: nodes and edges and show it in the EX-018 output.

**Prerequisites.** L03.10.5

**Lesson.** A gas network is nodes (basins, hubs, markets) joined by edges (pipelines) with capacities. [K]

**Example.** EX-018 (Build a North American Gas Infrastructure Network) on synthetic North American data: nodes = 11 [EX]

**Do.** `python3 emi.py run 018 | grep '^nodes:'`

**Expect.** `nodes: 11`

**On the job.** Represent production basins, processing plants, pipelines, storage facilities, LNG terminals, and market hubs as a connected network.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L03.10.5 | After: L04.01.2

## L04.01.2 Supply-push vs demand-pull corridors

**Objective.** Explain supply-push vs demand-pull corridors and show it in the EX-018 output.

**Prerequisites.** L04.01.1

**Lesson.** Supply-push corridors exist because a basin must clear; demand-pull corridors because a market must be fed. [K]

**Example.** EX-018 (Build a North American Gas Infrastructure Network) on synthetic North American data: edges = 12 [EX]

**Do.** `python3 emi.py run 018 | grep '^edges:'`

**Expect.** `edges: 12`

**On the job.** Represent production basins, processing plants, pipelines, storage facilities, LNG terminals, and market hubs as a connected network.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.01.1 | After: L04.01.3

## L04.01.3 Flow direction and reversals

**Objective.** Explain flow direction and reversals and show it in the EX-018 output.

**Prerequisites.** L04.01.2

**Lesson.** Flows can reverse when supply patterns change, as they did when shale shifted production. [K]

**Example.** EX-018 (Build a North American Gas Infrastructure Network) on synthetic North American data: most_central_node = HUB_GULF [EX]

**Do.** `python3 emi.py run 018 | grep '^most_central_node:'`

**Expect.** `most_central_node: HUB_GULF`

**On the job.** Represent production basins, processing plants, pipelines, storage facilities, LNG terminals, and market hubs as a connected network.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.01.2 | After: L04.01.4

## L04.01.4 Hubs as network junctions

**Objective.** Explain hubs as network junctions and show it in the EX-018 output.

**Prerequisites.** L04.01.3

**Lesson.** Hubs sit where many pipelines meet and gas can be rerouted. [K]

**Example.** EX-018 (Build a North American Gas Infrastructure Network) on synthetic North American data: max_flow_to_LNG_GULF_Bcf_d = 12 [EX]

**Do.** `python3 emi.py run 018 | grep '^max_flow_to_LNG_GULF_Bcf_d:'`

**Expect.** `max_flow_to_LNG_GULF_Bcf_d: 12`

**On the job.** Represent production basins, processing plants, pipelines, storage facilities, LNG terminals, and market hubs as a connected network.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.01.3 | After: L04.01.5

## L04.01.5 Mapping a regional network

**Objective.** Explain mapping a regional network and show it in the EX-018 output.

**Prerequisites.** L04.01.4

**Lesson.** A regional map is the first deliverable in any basis analysis. [K]

**Example.** EX-018 (Build a North American Gas Infrastructure Network) on synthetic North American data: max_flow_to_MEXICO_EXPORT_Bcf_d = 6 [EX]

**Do.** `python3 emi.py run 018 | grep '^max_flow_to_MEXICO_EXPORT_Bcf_d:'`

**Expect.** `max_flow_to_MEXICO_EXPORT_Bcf_d: 6`

**On the job.** Represent production basins, processing plants, pipelines, storage facilities, LNG terminals, and market hubs as a connected network.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.01.4 | After: L04.02.1
