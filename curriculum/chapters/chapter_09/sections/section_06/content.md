# 9.6 VaR and Expected Shortfall

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-081 Calculate Value at Risk (`python3 emi.py run 081`). Full output: `exercises/completed/ex081/report.md`.

## L09.06.1 VaR concepts

**Objective.** Explain vaR concepts and show it in the EX-081 output.

**Prerequisites.** L09.05.5

**Lesson.** VaR is the loss not exceeded at a confidence level over a horizon. [K]

**Example.** EX-081 (Calculate Value at Risk) on synthetic North American data: observations = 500 [EX]

**Do.** `python3 emi.py run 081 | grep '^observations:'`

**Expect.** `observations: 500`

**On the job.** Estimate portfolio losses at a specified confidence level and holding period.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.05.5 | After: L09.06.2

## L09.06.2 Parametric VaR

**Objective.** Explain parametric VaR and show it in the EX-081 output.

**Prerequisites.** L09.06.1

**Lesson.** Parametric VaR assumes normal returns. [K]

**Example.** EX-081 (Calculate Value at Risk) on synthetic North American data: portfolio_daily_vol_USD = 142938.498174 [EX]

**Do.** `python3 emi.py run 081 | grep '^portfolio_daily_vol_USD:'`

**Expect.** `portfolio_daily_vol_USD: 142938.498174`

**On the job.** Estimate portfolio losses at a specified confidence level and holding period.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.06.1 | After: L09.06.3

## L09.06.3 Historical simulation

**Objective.** Explain historical simulation and show it in the EX-081 output.

**Prerequisites.** L09.06.2

**Lesson.** Historical simulation replays past returns. [K]

**Example.** EX-081 (Calculate Value at Risk) on synthetic North American data: parametric_var95_USD = 235112.907152 [EX]

**Do.** `python3 emi.py run 081 | grep '^parametric_var95_USD:'`

**Expect.** `parametric_var95_USD: 235112.907152`

**On the job.** Estimate portfolio losses at a specified confidence level and holding period.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.06.2 | After: L09.06.4

## L09.06.4 Monte Carlo VaR

**Objective.** Explain monte Carlo VaR and show it in the EX-081 output.

**Prerequisites.** L09.06.3

**Lesson.** Monte Carlo VaR simulates price paths. [K]

**Example.** EX-081 (Calculate Value at Risk) on synthetic North American data: parametric_var99_USD = 332524.671345 [EX]

**Do.** `python3 emi.py run 081 | grep '^parametric_var99_USD:'`

**Expect.** `parametric_var99_USD: 332524.671345`

**On the job.** Estimate portfolio losses at a specified confidence level and holding period.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.06.3 | After: L09.06.5

## L09.06.5 Expected Shortfall

**Objective.** Explain expected Shortfall and show it in the EX-081 output.

**Prerequisites.** L09.06.4

**Lesson.** Expected Shortfall averages the losses beyond VaR. [K]

**Example.** EX-081 (Calculate Value at Risk) on synthetic North American data: historical_var95_USD = 229811.6 [EX]

**Do.** `python3 emi.py run 081 | grep '^historical_var95_USD:'`

**Expect.** `historical_var95_USD: 229811.6`

**On the job.** Estimate portfolio losses at a specified confidence level and holding period.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.06.4 | After: L09.07.1
