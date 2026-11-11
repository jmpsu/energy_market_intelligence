# 10.4 Linear, mixed-integer, and stochastic optimization

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-091 Develop a Capacity Expansion Model (`python3 emi.py run 091`). Full output: `exercises/completed/ex091/report.md`.

## L10.04.1 Linear programming

**Objective.** Explain linear programming and show it in the EX-091 output.

**Prerequisites.** L10.03.5

**Lesson.** Linear programming solves linear problems to proven optimality. [K]

**Example.** EX-091 (Develop a Capacity Expansion Model) on synthetic North American data: total_cost_USD_per_yr = 550080000 [EX]

**Do.** `python3 emi.py run 091 | grep '^total_cost_USD_per_yr:'`

**Expect.** `total_cost_USD_per_yr: 550080000`

**On the job.** Determine which generation resources should be added to meet future electricity demand at minimum modeled cost.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.03.5 | After: L10.04.2

## L10.04.2 Mixed-integer programming

**Objective.** Explain mixed-integer programming and show it in the EX-091 output.

**Prerequisites.** L10.04.1

**Lesson.** Mixed-integer programming adds on/off decisions and is much slower. [K]

**Example.** EX-091 (Develop a Capacity Expansion Model) on synthetic North American data: average_cost_USD_per_MWh = 48.422535 [EX]

**Do.** `python3 emi.py run 091 | grep '^average_cost_USD_per_MWh:'`

**Expect.** `average_cost_USD_per_MWh: 48.422535`

**On the job.** Determine which generation resources should be added to meet future electricity demand at minimum modeled cost.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.04.1 | After: L10.04.3

## L10.04.3 Stochastic programming

**Objective.** Explain stochastic programming and show it in the EX-091 output.

**Prerequisites.** L10.04.2

**Lesson.** Stochastic programming optimises over scenarios. [K]

**Example.** EX-091 (Develop a Capacity Expansion Model) on synthetic North American data: Baseload_MW = 1000 [EX]

**Do.** `python3 emi.py run 091 | grep '^Baseload_MW:'`

**Expect.** `Baseload_MW: 1000`

**On the job.** Determine which generation resources should be added to meet future electricity demand at minimum modeled cost.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.04.2 | After: L10.04.4

## L10.04.4 Decomposition methods

**Objective.** Explain decomposition methods and show it in the EX-091 output.

**Prerequisites.** L10.04.3

**Lesson.** Decomposition splits large problems. [K]

**Example.** EX-091 (Develop a Capacity Expansion Model) on synthetic North American data: Combined_Cycle_MW = 600 [EX]

**Do.** `python3 emi.py run 091 | grep '^Combined_Cycle_MW:'`

**Expect.** `Combined_Cycle_MW: 600`

**On the job.** Determine which generation resources should be added to meet future electricity demand at minimum modeled cost.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.04.3 | After: L10.04.5

## L10.04.5 Solver selection

**Objective.** Explain solver selection and show it in the EX-091 output.

**Prerequisites.** L10.04.4

**Lesson.** Solver choice depends on problem type, size and licence. [K]

**Example.** EX-091 (Develop a Capacity Expansion Model) on synthetic North American data: Combustion_Turbine_MW = 400 [EX]

**Do.** `python3 emi.py run 091 | grep '^Combustion_Turbine_MW:'`

**Expect.** `Combustion_Turbine_MW: 400`

**On the job.** Determine which generation resources should be added to meet future electricity demand at minimum modeled cost.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.04.4 | After: L10.05.1
