# 8.4 Position management and portfolio accounting

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-075 Reconcile Physical and Financial Positions (`python3 emi.py run 075`). Full output: `exercises/completed/ex075/report.md`.

## L08.04.1 Position aggregation

**Objective.** Explain position aggregation and show it in the EX-075 output.

**Prerequisites.** L08.03.5

**Lesson.** Positions aggregate by commodity, location and delivery period. [K]

**Example.** EX-075 (Reconcile Physical and Financial Positions) on synthetic North American data: T001_mtm_USD = 5000 [EX]

**Do.** `python3 emi.py run 075 | grep '^T001_mtm_USD:'`

**Expect.** `T001_mtm_USD: 5000`

**On the job.** Compare contracted volumes, scheduled quantities, delivered quantities, and financial settlements.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.03.5 | After: L08.04.2

## L08.04.2 Book and portfolio hierarchy

**Objective.** Explain book and portfolio hierarchy and show it in the EX-075 output.

**Prerequisites.** L08.04.1

**Lesson.** Books roll up into portfolios and desks. [K]

**Example.** EX-075 (Reconcile Physical and Financial Positions) on synthetic North American data: T002_mtm_USD = -120000 [EX]

**Do.** `python3 emi.py run 075 | grep '^T002_mtm_USD:'`

**Expect.** `T002_mtm_USD: -120000`

**On the job.** Compare contracted volumes, scheduled quantities, delivered quantities, and financial settlements.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.04.1 | After: L08.04.3

## L08.04.3 Hedge designation

**Objective.** Explain hedge designation and show it in the EX-075 output.

**Prerequisites.** L08.04.2

**Lesson.** Hedge designation links a hedge to the exposure it offsets. [K]

**Example.** EX-075 (Reconcile Physical and Financial Positions) on synthetic North American data: T003_mtm_USD = -105000 [EX]

**Do.** `python3 emi.py run 075 | grep '^T003_mtm_USD:'`

**Expect.** `T003_mtm_USD: -105000`

**On the job.** Compare contracted volumes, scheduled quantities, delivered quantities, and financial settlements.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.04.2 | After: L08.04.4

## L08.04.4 Accrual vs mark-to-market accounting

**Objective.** Explain accrual vs mark-to-market accounting and show it in the EX-075 output.

**Prerequisites.** L08.04.3

**Lesson.** Accrual accounting recognises value at delivery; mark-to-market recognises it daily. [K]

**Example.** EX-075 (Reconcile Physical and Financial Positions) on synthetic North American data: T004_mtm_USD = -15000 [EX]

**Do.** `python3 emi.py run 075 | grep '^T004_mtm_USD:'`

**Expect.** `T004_mtm_USD: -15000`

**On the job.** Compare contracted volumes, scheduled quantities, delivered quantities, and financial settlements.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.04.3 | After: L08.04.5

## L08.04.5 Position reporting

**Objective.** Explain position reporting and show it in the EX-075 output.

**Prerequisites.** L08.04.4

**Lesson.** Position reports are the daily common truth for traders and risk. [K]

**Example.** EX-075 (Reconcile Physical and Financial Positions) on synthetic North American data: T005_mtm_USD = 4000 [EX]

**Do.** `python3 emi.py run 075 | grep '^T005_mtm_USD:'`

**Expect.** `T005_mtm_USD: 4000`

**On the job.** Compare contracted volumes, scheduled quantities, delivered quantities, and financial settlements.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.04.4 | After: L08.05.1
