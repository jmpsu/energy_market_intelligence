# 8.9 Credit and counterparty management

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-073 Simulate Counterparty Credit Exposure (`python3 emi.py run 073`). Full output: `exercises/completed/ex073/report.md`.

## L08.09.1 Credit exposure calculation

**Objective.** Explain credit exposure calculation and show it in the EX-073 output.

**Prerequisites.** L08.08.5

**Lesson.** Credit exposure is what a counterparty would owe if it defaulted today. [K]

**Example.** EX-073 (Simulate Counterparty Credit Exposure) on synthetic North American data: CP_A_exposure_USD = 600000 [EX]

**Do.** `python3 emi.py run 073 | grep '^CP_A_exposure_USD:'`

**Expect.** `CP_A_exposure_USD: 600000`

**On the job.** Calculate exposure across counterparties and identify concentrations exceeding hypothetical credit limits.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.08.5 | After: L08.09.2

## L08.09.2 Limits and collateral

**Objective.** Explain limits and collateral and show it in the EX-073 output.

**Prerequisites.** L08.09.1

**Lesson.** Limits cap exposure; collateral reduces it. [K]

**Example.** EX-073 (Simulate Counterparty Credit Exposure) on synthetic North American data: CP_B_exposure_USD = 150000 [EX]

**Do.** `python3 emi.py run 073 | grep '^CP_B_exposure_USD:'`

**Expect.** `CP_B_exposure_USD: 150000`

**On the job.** Calculate exposure across counterparties and identify concentrations exceeding hypothetical credit limits.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.09.1 | After: L08.09.3

## L08.09.3 Master agreements (ISDA, NAESB, EEI)

**Objective.** Explain master agreements (ISDA, NAESB, EEI) and show it in the EX-073 output.

**Prerequisites.** L08.09.2

**Lesson.** Master agreements such as ISDA, NAESB and EEI set default and netting terms. [K]

**Example.** EX-073 (Simulate Counterparty Credit Exposure) on synthetic North American data: CP_C_exposure_USD = 400000 [EX]

**Do.** `python3 emi.py run 073 | grep '^CP_C_exposure_USD:'`

**Expect.** `CP_C_exposure_USD: 400000`

**On the job.** Calculate exposure across counterparties and identify concentrations exceeding hypothetical credit limits.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.09.2 | After: L08.09.4

## L08.09.4 Margining

**Objective.** Explain margining and show it in the EX-073 output.

**Prerequisites.** L08.09.3

**Lesson.** Margin calls move collateral as exposure changes. [K]

**Example.** EX-073 (Simulate Counterparty Credit Exposure) on synthetic North American data: CP_D_exposure_USD = 150000 [EX]

**Do.** `python3 emi.py run 073 | grep '^CP_D_exposure_USD:'`

**Expect.** `CP_D_exposure_USD: 150000`

**On the job.** Calculate exposure across counterparties and identify concentrations exceeding hypothetical credit limits.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.09.3 | After: L08.09.5

## L08.09.5 Credit monitoring

**Objective.** Explain credit monitoring and show it in the EX-073 output.

**Prerequisites.** L08.09.4

**Lesson.** Credit monitoring compares exposure to limits daily. [K]

**Example.** EX-073 (Simulate Counterparty Credit Exposure) on synthetic North American data: total_exposure_USD = 1300000 [EX]

**Do.** `python3 emi.py run 073 | grep '^total_exposure_USD:'`

**Expect.** `total_exposure_USD: 1300000`

**On the job.** Calculate exposure across counterparties and identify concentrations exceeding hypothetical credit limits.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.09.4 | After: L08.10.1
