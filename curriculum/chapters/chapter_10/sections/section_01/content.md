# 10.1 Mathematical foundations of energy-market models

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-090 Build a Gas Network Simulation (`python3 emi.py run 090`). Full output: `exercises/completed/ex090/report.md`.

## L10.01.1 Optimization problem structure

**Objective.** Explain optimization problem structure and show it in the EX-090 output.

**Prerequisites.** L09.10.5

**Lesson.** An optimisation has decision variables, an objective and constraints. [K]

**Example.** EX-090 (Build a Gas Network Simulation) on synthetic North American data: base_transport_cost_USD_per_d = 19750000 [EX]

**Do.** `python3 emi.py run 090 | grep '^base_transport_cost_USD_per_d:'`

**Expect.** `base_transport_cost_USD_per_d: 19750000`

**On the job.** Model interconnected supply sources, pipelines, storage facilities, demand centers, and transportation constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L09.10.5 | After: L10.01.2

## L10.01.2 Objective functions

**Objective.** Explain objective functions and show it in the EX-090 output.

**Prerequisites.** L10.01.1

**Lesson.** The objective is cost to minimise or margin to maximise. [K]

**Example.** EX-090 (Build a Gas Network Simulation) on synthetic North American data: disrupted_transport_cost_USD_per_d = 19750000 [EX]

**Do.** `python3 emi.py run 090 | grep '^disrupted_transport_cost_USD_per_d:'`

**Expect.** `disrupted_transport_cost_USD_per_d: 19750000`

**On the job.** Model interconnected supply sources, pipelines, storage facilities, demand centers, and transportation constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.01.1 | After: L10.01.3

## L10.01.3 Constraints and bounds

**Objective.** Explain constraints and bounds and show it in the EX-090 output.

**Prerequisites.** L10.01.2

**Lesson.** Constraints express physical and contractual limits. [K]

**Example.** EX-090 (Build a Gas Network Simulation) on synthetic North American data: base_unmet_Bcf_d = 5 [EX]

**Do.** `python3 emi.py run 090 | grep '^base_unmet_Bcf_d:'`

**Expect.** `base_unmet_Bcf_d: 5`

**On the job.** Model interconnected supply sources, pipelines, storage facilities, demand centers, and transportation constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.01.2 | After: L10.01.4

## L10.01.4 Duality and shadow prices

**Objective.** Explain duality and shadow prices and show it in the EX-090 output.

**Prerequisites.** L10.01.3

**Lesson.** A shadow price is the objective change per unit of constraint relaxed; LMPs are shadow prices. [K]

**Example.** EX-090 (Build a Gas Network Simulation) on synthetic North American data: disrupted_unmet_Bcf_d = 5 [EX]

**Do.** `python3 emi.py run 090 | grep '^disrupted_unmet_Bcf_d:'`

**Expect.** `disrupted_unmet_Bcf_d: 5`

**On the job.** Model interconnected supply sources, pipelines, storage facilities, demand centers, and transportation constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.01.3 | After: L10.01.5

## L10.01.5 Formulating a market model

**Objective.** Explain formulating a market model and show it in the EX-090 output.

**Prerequisites.** L10.01.4

**Lesson.** Formulate first on paper: variables, objective, constraints. [K]

**Example.** EX-090 (Build a Gas Network Simulation) on synthetic North American data: base_binding_edges = P001,P004,P005,P007,P008 [EX]

**Do.** `python3 emi.py run 090 | grep '^base_binding_edges:'`

**Expect.** `base_binding_edges: P001,P004,P005,P007,P008`

**On the job.** Model interconnected supply sources, pipelines, storage facilities, demand centers, and transportation constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.01.4 | After: L10.02.1
