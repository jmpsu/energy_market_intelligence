# 10.9 Model calibration, validation, and reproducibility

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-094 Build a Simulation Validation Framework (`python3 emi.py run 094`). Full output: `exercises/completed/ex094/report.md`.

## L10.09.1 Calibration methods

**Objective.** Explain calibration methods and show it in the EX-094 output.

**Prerequisites.** L10.08.5

**Lesson.** Calibration tunes parameters so outputs match observations. [K]

**Example.** EX-094 (Build a Simulation Validation Framework) on synthetic North American data: hours = 48 [EX]

**Do.** `python3 emi.py run 094 | grep '^hours:'`

**Expect.** `hours: 48`

**On the job.** Compare model outputs against historical observations and independent calculations; identify calibration errors and structural limitations.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.08.5 | After: L10.09.2

## L10.09.2 Backcasting

**Objective.** Explain backcasting and show it in the EX-094 output.

**Prerequisites.** L10.09.1

**Lesson.** Backcasting runs the model on a past period. [K]

**Example.** EX-094 (Build a Simulation Validation Framework) on synthetic North American data: energy_balance_all_hours = True [EX]

**Do.** `python3 emi.py run 094 | grep '^energy_balance_all_hours:'`

**Expect.** `energy_balance_all_hours: True`

**On the job.** Compare model outputs against historical observations and independent calculations; identify calibration errors and structural limitations.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.09.1 | After: L10.09.3

## L10.09.3 Validation metrics

**Objective.** Explain validation metrics and show it in the EX-094 output.

**Prerequisites.** L10.09.2

**Lesson.** Validation metrics quantify error. [K]

**Example.** EX-094 (Build a Simulation Validation Framework) on synthetic North American data: model_prices_are_stack_costs = True [EX]

**Do.** `python3 emi.py run 094 | grep '^model_prices_are_stack_costs:'`

**Expect.** `model_prices_are_stack_costs: True`

**On the job.** Compare model outputs against historical observations and independent calculations; identify calibration errors and structural limitations.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.09.2 | After: L10.09.4

## L10.09.4 Reproducibility and versioning

**Objective.** Explain reproducibility and versioning and show it in the EX-094 output.

**Prerequisites.** L10.09.3

**Lesson.** Version inputs, code and outputs so runs reproduce. [K]

**Example.** EX-094 (Build a Simulation Validation Framework) on synthetic North American data: validation_mae_raw = 6.674167 [EX]

**Do.** `python3 emi.py run 094 | grep '^validation_mae_raw:'`

**Expect.** `validation_mae_raw: 6.674167`

**On the job.** Compare model outputs against historical observations and independent calculations; identify calibration errors and structural limitations.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.09.3 | After: L10.09.5

## L10.09.5 Validation framework

**Objective.** Explain validation framework and show it in the EX-094 output.

**Prerequisites.** L10.09.4

**Lesson.** A validation framework runs the checks every time. [K]

**Example.** EX-094 (Build a Simulation Validation Framework) on synthetic North American data: validation_bias_raw = -5.136667 [EX]

**Do.** `python3 emi.py run 094 | grep '^validation_bias_raw:'`

**Expect.** `validation_bias_raw: -5.136667`

**On the job.** Compare model outputs against historical observations and independent calculations; identify calibration errors and structural limitations.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.09.4 | After: L10.10.1
