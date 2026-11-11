# 9.10 Structured products, options, and weather derivatives

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-085 Build a Weather Derivatives Valuation Model (`python3 emi.py run 085`). Full output: `exercises/completed/ex085/report.md`.

## L09.10.1 Option pricing basics

**Objective.** Explain option pricing basics and show it in the EX-085 output.

**Prerequisites.** L09.09.5

**Lesson.** Option value depends on price, strike, volatility, time and rates. [K]

**Example.** EX-085 (Build a Weather Derivatives Valuation Model) on synthetic North American data: hdd_rows_verified = 15 [EX]

**Do.** `python3 emi.py run 085 | grep '^hdd_rows_verified:'`

**Expect.** `hdd_rows_verified: 15`

**On the job.** Calculate hypothetical financial exposures linked to heating or cooling degree days.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.09.5 | After: L09.10.2

## L09.10.2 Spread options

**Objective.** Explain spread options and show it in the EX-085 output.

**Prerequisites.** L09.10.1

**Lesson.** A spread option pays on the difference of two prices; power plants and transport resemble one. [K]

**Example.** EX-085 (Build a Weather Derivatives Valuation Model) on synthetic North American data: cumulative_HDD = 430 [EX]

**Do.** `python3 emi.py run 085 | grep '^cumulative_HDD:'`

**Expect.** `cumulative_HDD: 430`

**On the job.** Calculate hypothetical financial exposures linked to heating or cooling degree days.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.10.1 | After: L09.10.3

## L09.10.3 Swing and storage optionality

**Objective.** Explain swing and storage optionality and show it in the EX-085 output.

**Prerequisites.** L09.10.2

**Lesson.** Swing and storage contracts embed volume flexibility. [K]

**Example.** EX-085 (Build a Weather Derivatives Valuation Model) on synthetic North American data: strike_HDD = 450 [EX]

**Do.** `python3 emi.py run 085 | grep '^strike_HDD:'`

**Expect.** `strike_HDD: 450`

**On the job.** Calculate hypothetical financial exposures linked to heating or cooling degree days.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.10.2 | After: L09.10.4

## L09.10.4 Weather derivatives

**Objective.** Explain weather derivatives and show it in the EX-085 output.

**Prerequisites.** L09.10.3

**Lesson.** Weather derivatives pay on degree days. [K]

**Example.** EX-085 (Build a Weather Derivatives Valuation Model) on synthetic North American data: payout_USD = 200000 [EX]

**Do.** `python3 emi.py run 085 | grep '^payout_USD:'`

**Expect.** `payout_USD: 200000`

**On the job.** Calculate hypothetical financial exposures linked to heating or cooling degree days.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.10.3 | After: L09.10.5

## L09.10.5 Structured deal decomposition

**Objective.** Explain structured deal decomposition and show it in the EX-085 output.

**Prerequisites.** L09.10.4

**Lesson.** Decompose a structured deal into simple pieces and value each. [K]

**Example.** EX-085 (Build a Weather Derivatives Valuation Model) on synthetic North American data: cap_reached_at_HDD = 250 [EX]

**Do.** `python3 emi.py run 085 | grep '^cap_reached_at_HDD:'`

**Expect.** `cap_reached_at_HDD: 250`

**On the job.** Calculate hypothetical financial exposures linked to heating or cooling degree days.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.10.4 | After: L10.01.1
