# 10.6 Python, NumPy, pandas, SciPy, and SQL

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-092 Benchmark Simulation Performance (`python3 emi.py run 092`). Full output: `exercises/completed/ex092/report.md`.

## L10.06.1 Python data stack

**Objective.** Explain python data stack and show it in the EX-092 output.

**Prerequisites.** L10.05.5

**Lesson.** Python with NumPy, pandas and SciPy covers most analytics. [K]

**Example.** EX-092 (Benchmark Simulation Performance) on synthetic North American data: scenarios = 12 [EX]

**Do.** `python3 emi.py run 092 | grep '^scenarios:'`

**Expect.** `scenarios: 12`

**On the job.** Measure runtime, memory consumption, solver performance, and output quality across different model configurations.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.05.5 | After: L10.06.2

## L10.06.2 Vectorized computation with NumPy

**Objective.** Explain vectorized computation with NumPy and show it in the EX-092 output.

**Prerequisites.** L10.06.1

**Lesson.** Vectorised NumPy replaces slow loops. [K]

**Example.** EX-092 (Benchmark Simulation Performance) on synthetic North American data: variables_per_scenario = 864 [EX]

**Do.** `python3 emi.py run 092 | grep '^variables_per_scenario:'`

**Expect.** `variables_per_scenario: 864`

**On the job.** Measure runtime, memory consumption, solver performance, and output quality across different model configurations.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.06.1 | After: L10.06.3

## L10.06.3 pandas data wrangling

**Objective.** Explain pandas data wrangling and show it in the EX-092 output.

**Prerequisites.** L10.06.2

**Lesson.** pandas joins, reshapes and aggregates. [K]

**Example.** EX-092 (Benchmark Simulation Performance) on synthetic North American data: max_relative_objective_difference = 0 [EX]

**Do.** `python3 emi.py run 092 | grep '^max_relative_objective_difference:'`

**Expect.** `max_relative_objective_difference: 0`

**On the job.** Measure runtime, memory consumption, solver performance, and output quality across different model configurations.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.06.2 | After: L10.06.4

## L10.06.4 SciPy optimization

**Objective.** Explain sciPy optimization and show it in the EX-092 output.

**Prerequisites.** L10.06.3

**Lesson.** SciPy solves linear programs. [K]

**Example.** EX-092 (Benchmark Simulation Performance) on synthetic North American data: results_equivalent = True [EX]

**Do.** `python3 emi.py run 092 | grep '^results_equivalent:'`

**Expect.** `results_equivalent: True`

**On the job.** Measure runtime, memory consumption, solver performance, and output quality across different model configurations.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.06.3 | After: L10.06.5

## L10.06.5 SQL analytics

**Objective.** Explain sQL analytics and show it in the EX-092 output.

**Prerequisites.** L10.06.4

**Lesson.** SQL handles set-based queries where the data lives. [K]

**Example.** EX-092 (Benchmark Simulation Performance) on synthetic North American data: max_constraint_violation = 0 [EX]

**Do.** `python3 emi.py run 092 | grep '^max_constraint_violation:'`

**Expect.** `max_constraint_violation: 0`

**On the job.** Measure runtime, memory consumption, solver performance, and output quality across different model configurations.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.06.4 | After: L10.07.1
