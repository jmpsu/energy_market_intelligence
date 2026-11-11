# 8.1 Front, middle, and back office

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-072 Build a Trade Lifecycle (`python3 emi.py run 072`). Full output: `exercises/completed/ex072/report.md`.

## L08.01.1 Front-office functions

**Objective.** Explain front-office functions and show it in the EX-072 output.

**Prerequisites.** L07.10.5

**Lesson.** The front office trades, originates and optimises assets. [K]

**Example.** EX-072 (Build a Trade Lifecycle) on synthetic North American data: events = 13 [EX]

**Do.** `python3 emi.py run 072 | grep '^events:'`

**Expect.** `events: 13`

**On the job.** Model trade capture, confirmation, scheduling, delivery, settlement, and accounting.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L07.10.5 | After: L08.01.2

## L08.01.2 Middle-office functions

**Objective.** Explain middle-office functions and show it in the EX-072 output.

**Prerequisites.** L08.01.1

**Lesson.** The middle office measures risk, validates curves and reports P&L independently. [K]

**Example.** EX-072 (Build a Trade Lifecycle) on synthetic North American data: accepted_events = 11 [EX]

**Do.** `python3 emi.py run 072 | grep '^accepted_events:'`

**Expect.** `accepted_events: 11`

**On the job.** Model trade capture, confirmation, scheduling, delivery, settlement, and accounting.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.01.1 | After: L08.01.3

## L08.01.3 Back-office functions

**Objective.** Explain back-office functions and show it in the EX-072 output.

**Prerequisites.** L08.01.2

**Lesson.** The back office confirms, schedules, invoices and settles. [K]

**Example.** EX-072 (Build a Trade Lifecycle) on synthetic North American data: rejected_events = 2 [EX]

**Do.** `python3 emi.py run 072 | grep '^rejected_events:'`

**Expect.** `rejected_events: 2`

**On the job.** Model trade capture, confirmation, scheduling, delivery, settlement, and accounting.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.01.2 | After: L08.01.4

## L08.01.4 Segregation of duties

**Objective.** Explain segregation of duties and show it in the EX-072 output.

**Prerequisites.** L08.01.3

**Lesson.** Those who trade must not be the ones who value or settle the trades. [K]

**Example.** EX-072 (Build a Trade Lifecycle) on synthetic North American data: rejected_detail = TR002:scheduled(expected confirmed),TR003:invoiced(expected scheduled) [EX]

**Do.** `python3 emi.py run 072 | grep '^rejected_detail:'`

**Expect.** `rejected_detail: TR002:scheduled(expected confirmed),TR003:invoiced(expected scheduled)`

**On the job.** Model trade capture, confirmation, scheduling, delivery, settlement, and accounting.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.01.3 | After: L08.01.5

## L08.01.5 Information flow between offices

**Objective.** Explain information flow between offices and show it in the EX-072 output.

**Prerequisites.** L08.01.4

**Lesson.** A trade's data passes front to middle to back; every re-keying is an error risk. [K]

**Example.** EX-072 (Build a Trade Lifecycle) on synthetic North American data: settled_trades = 1 [EX]

**Do.** `python3 emi.py run 072 | grep '^settled_trades:'`

**Expect.** `settled_trades: 1`

**On the job.** Model trade capture, confirmation, scheduling, delivery, settlement, and accounting.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.01.4 | After: L08.02.1
