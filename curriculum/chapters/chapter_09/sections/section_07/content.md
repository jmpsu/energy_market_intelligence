# 9.7 Potential Future Exposure and Earnings at Risk

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-083 Model Potential Future Exposure (`python3 emi.py run 083`). Full output: `exercises/completed/ex083/report.md`.

## L09.07.1 Exposure profiles

**Objective.** Explain exposure profiles and show it in the EX-083 output.

**Prerequisites.** L09.06.5

**Lesson.** An exposure profile shows possible future value through time. [K]

**Example.** EX-083 (Model Potential Future Exposure) on synthetic North American data: peak_pfe_USD = 1428316.177291 [EX]

**Do.** `python3 emi.py run 083 | grep '^peak_pfe_USD:'`

**Expect.** `peak_pfe_USD: 1428316.177291`

**On the job.** Estimate how counterparty exposure may evolve under simulated future market conditions.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.06.5 | After: L09.07.2

## L09.07.2 Potential Future Exposure

**Objective.** Explain potential Future Exposure and show it in the EX-083 output.

**Prerequisites.** L09.07.1

**Lesson.** Potential Future Exposure is a high percentile of that value. [K]

**Example.** EX-083 (Model Potential Future Exposure) on synthetic North American data: peak_pfe_month = 5 [EX]

**Do.** `python3 emi.py run 083 | grep '^peak_pfe_month:'`

**Expect.** `peak_pfe_month: 5`

**On the job.** Estimate how counterparty exposure may evolve under simulated future market conditions.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.07.1 | After: L09.07.3

## L09.07.3 Earnings at Risk

**Objective.** Explain earnings at Risk and show it in the EX-083 output.

**Prerequisites.** L09.07.2

**Lesson.** Earnings at Risk applies the idea to accounting earnings. [K]

**Example.** EX-083 (Model Potential Future Exposure) on synthetic North American data: peak_expected_exposure_USD = 296168.296199 [EX]

**Do.** `python3 emi.py run 083 | grep '^peak_expected_exposure_USD:'`

**Expect.** `peak_expected_exposure_USD: 296168.296199`

**On the job.** Estimate how counterparty exposure may evolve under simulated future market conditions.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.07.2 | After: L09.07.4

## L09.07.4 Cash-flow at risk

**Objective.** Explain cash-flow at risk and show it in the EX-083 output.

**Prerequisites.** L09.07.3

**Lesson.** Cash-flow at risk applies it to cash. [K]

**Example.** EX-083 (Model Potential Future Exposure) on synthetic North American data: average_expected_exposure_USD = 198617.939286 [EX]

**Do.** `python3 emi.py run 083 | grep '^average_expected_exposure_USD:'`

**Expect.** `average_expected_exposure_USD: 198617.939286`

**On the job.** Estimate how counterparty exposure may evolve under simulated future market conditions.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.07.3 | After: L09.07.5

## L09.07.5 Exposure simulation

**Objective.** Explain exposure simulation and show it in the EX-083 output.

**Prerequisites.** L09.07.4

**Lesson.** Exposure simulation revalues the portfolio along each path. [K]

**Example.** EX-083 (Model Potential Future Exposure) on synthetic North American data: pfe_at_maturity_USD = 0 [EX]

**Do.** `python3 emi.py run 083 | grep '^pfe_at_maturity_USD:'`

**Expect.** `pfe_at_maturity_USD: 0`

**On the job.** Estimate how counterparty exposure may evolve under simulated future market conditions.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.07.4 | After: L09.08.1
