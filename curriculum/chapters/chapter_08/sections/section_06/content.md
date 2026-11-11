# 8.6 Scheduling, nominations, and physical operations

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-074 Build a Physical Gas Scheduling Workflow (`python3 emi.py run 074`). Full output: `exercises/completed/ex074/report.md`.

## L08.06.1 Power scheduling and e-Tags

**Objective.** Explain power scheduling and e-Tags and show it in the EX-074 output.

**Prerequisites.** L08.05.5

**Lesson.** Power schedules are communicated with e-Tags naming the path from source to sink. [K]

**Example.** EX-074 (Build a Physical Gas Scheduling Workflow) on synthetic North American data: receipt_needed_MMBtu = 56122.44898 [EX]

**Do.** `python3 emi.py run 074 | grep '^receipt_needed_MMBtu:'`

**Expect.** `receipt_needed_MMBtu: 56122.44898`

**On the job.** Connect trade quantities to transportation capacity, nominations, confirmations, and delivery schedules.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.05.5 | After: L08.06.2

## L08.06.2 Gas nominations

**Objective.** Explain gas nominations and show it in the EX-074 output.

**Prerequisites.** L08.06.1

**Lesson.** Gas schedules are nominated to pipelines. [K]

**Example.** EX-074 (Build a Physical Gas Scheduling Workflow) on synthetic North American data: receipt_nominated_MMBtu = 50000 [EX]

**Do.** `python3 emi.py run 074 | grep '^receipt_nominated_MMBtu:'`

**Expect.** `receipt_nominated_MMBtu: 50000`

**On the job.** Connect trade quantities to transportation capacity, nominations, confirmations, and delivery schedules.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.06.1 | After: L08.06.3

## L08.06.3 Actualization

**Objective.** Explain actualization and show it in the EX-074 output.

**Prerequisites.** L08.06.2

**Lesson.** Actualisation replaces scheduled volumes with measured ones. [K]

**Example.** EX-074 (Build a Physical Gas Scheduling Workflow) on synthetic North American data: fuel_retained_MMBtu = 1000 [EX]

**Do.** `python3 emi.py run 074 | grep '^fuel_retained_MMBtu:'`

**Expect.** `fuel_retained_MMBtu: 1000`

**On the job.** Connect trade quantities to transportation capacity, nominations, confirmations, and delivery schedules.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.06.2 | After: L08.06.4

## L08.06.4 Scheduling systems

**Objective.** Explain scheduling systems and show it in the EX-074 output.

**Prerequisites.** L08.06.3

**Lesson.** Scheduling systems send nominations and receive confirmations. [K]

**Example.** EX-074 (Build a Physical Gas Scheduling Workflow) on synthetic North American data: delivered_MMBtu = 49000 [EX]

**Do.** `python3 emi.py run 074 | grep '^delivered_MMBtu:'`

**Expect.** `delivered_MMBtu: 49000`

**On the job.** Connect trade quantities to transportation capacity, nominations, confirmations, and delivery schedules.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.06.3 | After: L08.06.5

## L08.06.5 Schedule reconciliation

**Objective.** Explain schedule reconciliation and show it in the EX-074 output.

**Prerequisites.** L08.06.4

**Lesson.** Scheduled, confirmed and actual volumes are reconciled daily. [K]

**Example.** EX-074 (Build a Physical Gas Scheduling Workflow) on synthetic North American data: delivery_shortfall_MMBtu = 6000 [EX]

**Do.** `python3 emi.py run 074 | grep '^delivery_shortfall_MMBtu:'`

**Expect.** `delivery_shortfall_MMBtu: 6000`

**On the job.** Connect trade quantities to transportation capacity, nominations, confirmations, and delivery schedules.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.06.4 | After: L08.07.1
