# 8.5 Confirmations and eConfirms

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-072 Build a Trade Lifecycle (`python3 emi.py run 072`). Full output: `exercises/completed/ex072/report.md`.

## L08.05.1 Confirmation process

**Objective.** Explain confirmation process and show it in the EX-072 output.

**Prerequisites.** L08.04.5

**Lesson.** Both parties confirm the trade's terms after execution. [K]

**Example.** EX-072 (Build a Trade Lifecycle) on synthetic North American data: events = 13 [EX]

**Do.** `python3 emi.py run 072 | grep '^events:'`

**Expect.** `events: 13`

**On the job.** Model trade capture, confirmation, scheduling, delivery, settlement, and accounting.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.04.5 | After: L08.05.2

## L08.05.2 Electronic confirmation matching

**Objective.** Explain electronic confirmation matching and show it in the EX-072 output.

**Prerequisites.** L08.05.1

**Lesson.** Electronic matching compares the two records automatically. [K]

**Example.** EX-072 (Build a Trade Lifecycle) on synthetic North American data: accepted_events = 11 [EX]

**Do.** `python3 emi.py run 072 | grep '^accepted_events:'`

**Expect.** `accepted_events: 11`

**On the job.** Model trade capture, confirmation, scheduling, delivery, settlement, and accounting.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.05.1 | After: L08.05.3

## L08.05.3 Discrepancy resolution

**Objective.** Explain discrepancy resolution and show it in the EX-072 output.

**Prerequisites.** L08.05.2

**Lesson.** Mismatches are investigated and corrected before delivery. [K]

**Example.** EX-072 (Build a Trade Lifecycle) on synthetic North American data: rejected_events = 2 [EX]

**Do.** `python3 emi.py run 072 | grep '^rejected_events:'`

**Expect.** `rejected_events: 2`

**On the job.** Model trade capture, confirmation, scheduling, delivery, settlement, and accounting.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.05.2 | After: L08.05.4

## L08.05.4 Regulatory reporting

**Objective.** Explain regulatory reporting and show it in the EX-072 output.

**Prerequisites.** L08.05.3

**Lesson.** Many trades must be reported to regulators. [K]

**Example.** EX-072 (Build a Trade Lifecycle) on synthetic North American data: rejected_detail = TR002:scheduled(expected confirmed),TR003:invoiced(expected scheduled) [EX]

**Do.** `python3 emi.py run 072 | grep '^rejected_detail:'`

**Expect.** `rejected_detail: TR002:scheduled(expected confirmed),TR003:invoiced(expected scheduled)`

**On the job.** Model trade capture, confirmation, scheduling, delivery, settlement, and accounting.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.05.3 | After: L08.05.5

## L08.05.5 Confirmation workflow

**Objective.** Explain confirmation workflow and show it in the EX-072 output.

**Prerequisites.** L08.05.4

**Lesson.** Unconfirmed trades are tracked until resolved. [K]

**Example.** EX-072 (Build a Trade Lifecycle) on synthetic North American data: settled_trades = 1 [EX]

**Do.** `python3 emi.py run 072 | grep '^settled_trades:'`

**Expect.** `settled_trades: 1`

**On the job.** Model trade capture, confirmation, scheduling, delivery, settlement, and accounting.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.05.4 | After: L08.06.1
