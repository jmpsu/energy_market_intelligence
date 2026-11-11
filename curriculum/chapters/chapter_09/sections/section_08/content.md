# 9.8 Funding, liquidity, and counterparty risk

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-073 Simulate Counterparty Credit Exposure (`python3 emi.py run 073`). Full output: `exercises/completed/ex073/report.md`.

## L09.08.1 Margin and funding needs

**Objective.** Explain margin and funding needs and show it in the EX-073 output.

**Prerequisites.** L09.07.5

**Lesson.** Price moves create margin calls that need cash. [K]

**Example.** EX-073 (Simulate Counterparty Credit Exposure) on synthetic North American data: CP_A_exposure_USD = 600000 [EX]

**Do.** `python3 emi.py run 073 | grep '^CP_A_exposure_USD:'`

**Expect.** `CP_A_exposure_USD: 600000`

**On the job.** Calculate exposure across counterparties and identify concentrations exceeding hypothetical credit limits.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.07.5 | After: L09.08.2

## L09.08.2 Liquidity risk

**Objective.** Explain liquidity risk and show it in the EX-073 output.

**Prerequisites.** L09.08.1

**Lesson.** Liquidity risk is being unable to trade or fund without large cost. [K]

**Example.** EX-073 (Simulate Counterparty Credit Exposure) on synthetic North American data: CP_B_exposure_USD = 150000 [EX]

**Do.** `python3 emi.py run 073 | grep '^CP_B_exposure_USD:'`

**Expect.** `CP_B_exposure_USD: 150000`

**On the job.** Calculate exposure across counterparties and identify concentrations exceeding hypothetical credit limits.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.08.1 | After: L09.08.3

## L09.08.3 Counterparty default risk

**Objective.** Explain counterparty default risk and show it in the EX-073 output.

**Prerequisites.** L09.08.2

**Lesson.** Counterparty default risk is loss when the other side fails. [K]

**Example.** EX-073 (Simulate Counterparty Credit Exposure) on synthetic North American data: CP_C_exposure_USD = 400000 [EX]

**Do.** `python3 emi.py run 073 | grep '^CP_C_exposure_USD:'`

**Expect.** `CP_C_exposure_USD: 400000`

**On the job.** Calculate exposure across counterparties and identify concentrations exceeding hypothetical credit limits.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.08.2 | After: L09.08.4

## L09.08.4 Credit valuation adjustment basics

**Objective.** Explain credit valuation adjustment basics and show it in the EX-073 output.

**Prerequisites.** L09.08.3

**Lesson.** Credit valuation adjustment prices expected default loss. [K]

**Example.** EX-073 (Simulate Counterparty Credit Exposure) on synthetic North American data: CP_D_exposure_USD = 150000 [EX]

**Do.** `python3 emi.py run 073 | grep '^CP_D_exposure_USD:'`

**Expect.** `CP_D_exposure_USD: 150000`

**On the job.** Calculate exposure across counterparties and identify concentrations exceeding hypothetical credit limits.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.08.3 | After: L09.08.5

## L09.08.5 Liquidity stress

**Objective.** Explain liquidity stress and show it in the EX-073 output.

**Prerequisites.** L09.08.4

**Lesson.** A liquidity stress asks whether cash covers margin in a bad week. [K]

**Example.** EX-073 (Simulate Counterparty Credit Exposure) on synthetic North American data: total_exposure_USD = 1300000 [EX]

**Do.** `python3 emi.py run 073 | grep '^total_exposure_USD:'`

**Expect.** `total_exposure_USD: 1300000`

**On the job.** Calculate exposure across counterparties and identify concentrations exceeding hypothetical credit limits.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.08.4 | After: L09.09.1
