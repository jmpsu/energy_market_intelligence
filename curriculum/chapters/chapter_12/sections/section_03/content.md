# 12.3 Physical and financial position reconciliation

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-075 Reconcile Physical and Financial Positions (`python3 emi.py run 075`). Full output: `exercises/completed/ex075/report.md`.

## L12.03.1 Physical position ledger

**Objective.** Explain physical position ledger and show it in the EX-075 output.

**Prerequisites.** L12.02.5

**Lesson.** The physical ledger records volumes to deliver and receive. [K]

**Example.** EX-075 (Reconcile Physical and Financial Positions) on synthetic North American data: T001_mtm_USD = 5000 [EX]

**Do.** `python3 emi.py run 075 | grep '^T001_mtm_USD:'`

**Expect.** `T001_mtm_USD: 5000`

**On the job.** Compare contracted volumes, scheduled quantities, delivered quantities, and financial settlements.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.02.5 | After: L12.03.2

## L12.03.2 Financial position ledger

**Objective.** Explain financial position ledger and show it in the EX-075 output.

**Prerequisites.** L12.03.1

**Lesson.** The financial ledger records cash-settled positions. [K]

**Example.** EX-075 (Reconcile Physical and Financial Positions) on synthetic North American data: T002_mtm_USD = -120000 [EX]

**Do.** `python3 emi.py run 075 | grep '^T002_mtm_USD:'`

**Expect.** `T002_mtm_USD: -120000`

**On the job.** Compare contracted volumes, scheduled quantities, delivered quantities, and financial settlements.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.03.1 | After: L12.03.3

## L12.03.3 Break identification

**Objective.** Explain break identification and show it in the EX-075 output.

**Prerequisites.** L12.03.2

**Lesson.** A break is a mismatch between the two. [K]

**Example.** EX-075 (Reconcile Physical and Financial Positions) on synthetic North American data: T003_mtm_USD = -105000 [EX]

**Do.** `python3 emi.py run 075 | grep '^T003_mtm_USD:'`

**Expect.** `T003_mtm_USD: -105000`

**On the job.** Compare contracted volumes, scheduled quantities, delivered quantities, and financial settlements.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.03.2 | After: L12.03.4

## L12.03.4 Root-cause analysis

**Objective.** Explain root-cause analysis and show it in the EX-075 output.

**Prerequisites.** L12.03.3

**Lesson.** Root-cause analysis finds why. [K]

**Example.** EX-075 (Reconcile Physical and Financial Positions) on synthetic North American data: T004_mtm_USD = -15000 [EX]

**Do.** `python3 emi.py run 075 | grep '^T004_mtm_USD:'`

**Expect.** `T004_mtm_USD: -15000`

**On the job.** Compare contracted volumes, scheduled quantities, delivered quantities, and financial settlements.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.03.3 | After: L12.03.5

## L12.03.5 Reconciliation sign-off

**Objective.** Explain reconciliation sign-off and show it in the EX-075 output.

**Prerequisites.** L12.03.4

**Lesson.** Sign-off confirms the books agree. [K]

**Example.** EX-075 (Reconcile Physical and Financial Positions) on synthetic North American data: T005_mtm_USD = 4000 [EX]

**Do.** `python3 emi.py run 075 | grep '^T005_mtm_USD:'`

**Expect.** `T005_mtm_USD: 4000`

**On the job.** Compare contracted volumes, scheduled quantities, delivered quantities, and financial settlements.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.03.4 | After: L12.04.1
