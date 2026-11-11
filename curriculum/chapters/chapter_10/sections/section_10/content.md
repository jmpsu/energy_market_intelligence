# 10.10 Simulation performance, scalability, and model governance

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-093 Optimize Model Execution (`python3 emi.py run 093`). Full output: `exercises/completed/ex093/report.md`.

## L10.10.1 Profiling runtime

**Objective.** Explain profiling runtime and show it in the EX-093 output.

**Prerequisites.** L10.09.5

**Lesson.** Profiling finds where runtime goes before optimising. [K]

**Example.** EX-093 (Optimize Model Execution) on synthetic North American data: scenarios = 12 [EX]

**Do.** `python3 emi.py run 093 | grep '^scenarios:'`

**Expect.** `scenarios: 12`

**On the job.** Test scenario batching, caching, parallel processing, model decomposition, and solver configuration against an identical baseline.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.09.5 | After: L10.10.2

## L10.10.2 Sparse formulation and presolve

**Objective.** Explain sparse formulation and presolve and show it in the EX-093 output.

**Prerequisites.** L10.10.1

**Lesson.** Sparse matrices and presolve shrink large models. [K]

**Example.** EX-093 (Optimize Model Execution) on synthetic North American data: parallel_results_equivalent = True [EX]

**Do.** `python3 emi.py run 093 | grep '^parallel_results_equivalent:'`

**Expect.** `parallel_results_equivalent: True`

**On the job.** Test scenario batching, caching, parallel processing, model decomposition, and solver configuration against an identical baseline.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.10.1 | After: L10.10.3

## L10.10.3 Parallel and decomposed execution

**Objective.** Explain parallel and decomposed execution and show it in the EX-093 output.

**Prerequisites.** L10.10.2

**Lesson.** Parallel and decomposed runs use more cores. [K]

**Example.** EX-093 (Optimize Model Execution) on synthetic North American data: reduced_resolution_equivalent = False [EX]

**Do.** `python3 emi.py run 093 | grep '^reduced_resolution_equivalent:'`

**Expect.** `reduced_resolution_equivalent: False`

**On the job.** Test scenario batching, caching, parallel processing, model decomposition, and solver configuration against an identical baseline.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.10.2 | After: L10.10.4

## L10.10.4 Result-equivalence validation

**Objective.** Explain result-equivalence validation and show it in the EX-093 output.

**Prerequisites.** L10.10.3

**Lesson.** A faster model must give equivalent results; prove it. [K]

**Example.** EX-093 (Optimize Model Execution) on synthetic North American data: reduced_resolution_objective_error_pct = 0.041483 [EX]

**Do.** `python3 emi.py run 093 | grep '^reduced_resolution_objective_error_pct:'`

**Expect.** `reduced_resolution_objective_error_pct: 0.041483`

**On the job.** Test scenario batching, caching, parallel processing, model decomposition, and solver configuration against an identical baseline.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.10.3 | After: L10.10.5

## L10.10.5 Model governance and change control

**Objective.** Explain model governance and change control and show it in the EX-093 output.

**Prerequisites.** L10.10.4

**Lesson.** Governance controls who changes models and how. [K]

**Example.** EX-093 (Optimize Model Execution) on synthetic North American data: reduced_resolution_variables = 432 [EX]

**Do.** `python3 emi.py run 093 | grep '^reduced_resolution_variables:'`

**Expect.** `reduced_resolution_variables: 432`

**On the job.** Test scenario batching, caching, parallel processing, model decomposition, and solver configuration against an identical baseline.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.10.4 | After: L11.01.1
