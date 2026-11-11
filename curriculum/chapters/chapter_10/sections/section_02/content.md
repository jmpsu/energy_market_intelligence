# 10.2 Network-flow and transmission modeling

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-090 Build a Gas Network Simulation (`python3 emi.py run 090`). Full output: `exercises/completed/ex090/report.md`.

## L10.02.1 Graph models

**Objective.** Explain graph models and show it in the EX-090 output.

**Prerequisites.** L10.01.5

**Lesson.** Networks are graphs of nodes and edges. [K]

**Example.** EX-090 (Build a Gas Network Simulation) on synthetic North American data: base_transport_cost_USD_per_d = 19750000 [EX]

**Do.** `python3 emi.py run 090 | grep '^base_transport_cost_USD_per_d:'`

**Expect.** `base_transport_cost_USD_per_d: 19750000`

**On the job.** Model interconnected supply sources, pipelines, storage facilities, demand centers, and transportation constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.01.5 | After: L10.02.2

## L10.02.2 Transport (pipeline) model

**Objective.** Explain transport (pipeline) model and show it in the EX-090 output.

**Prerequisites.** L10.02.1

**Lesson.** A transport model limits flow on each edge by capacity. [K]

**Example.** EX-090 (Build a Gas Network Simulation) on synthetic North American data: disrupted_transport_cost_USD_per_d = 19750000 [EX]

**Do.** `python3 emi.py run 090 | grep '^disrupted_transport_cost_USD_per_d:'`

**Expect.** `disrupted_transport_cost_USD_per_d: 19750000`

**On the job.** Model interconnected supply sources, pipelines, storage facilities, demand centers, and transportation constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.02.1 | After: L10.02.3

## L10.02.3 DC power-flow approximation

**Objective.** Explain dC power-flow approximation and show it in the EX-090 output.

**Prerequisites.** L10.02.2

**Lesson.** DC power flow linearises AC physics. [K]

**Example.** EX-090 (Build a Gas Network Simulation) on synthetic North American data: base_unmet_Bcf_d = 5 [EX]

**Do.** `python3 emi.py run 090 | grep '^base_unmet_Bcf_d:'`

**Expect.** `base_unmet_Bcf_d: 5`

**On the job.** Model interconnected supply sources, pipelines, storage facilities, demand centers, and transportation constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.02.2 | After: L10.02.4

## L10.02.4 PTDF matrices

**Objective.** Explain pTDF matrices and show it in the EX-090 output.

**Prerequisites.** L10.02.3

**Lesson.** PTDFs give the flow on each line per MW injected. [K]

**Example.** EX-090 (Build a Gas Network Simulation) on synthetic North American data: disrupted_unmet_Bcf_d = 5 [EX]

**Do.** `python3 emi.py run 090 | grep '^disrupted_unmet_Bcf_d:'`

**Expect.** `disrupted_unmet_Bcf_d: 5`

**On the job.** Model interconnected supply sources, pipelines, storage facilities, demand centers, and transportation constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.02.3 | After: L10.02.5

## L10.02.5 Network model construction

**Objective.** Explain network model construction and show it in the EX-090 output.

**Prerequisites.** L10.02.4

**Lesson.** Network construction is mostly data cleaning. [K]

**Example.** EX-090 (Build a Gas Network Simulation) on synthetic North American data: base_binding_edges = P001,P004,P005,P007,P008 [EX]

**Do.** `python3 emi.py run 090 | grep '^base_binding_edges:'`

**Expect.** `base_binding_edges: P001,P004,P005,P007,P008`

**On the job.** Model interconnected supply sources, pipelines, storage facilities, demand centers, and transportation constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.02.4 | After: L10.03.1
