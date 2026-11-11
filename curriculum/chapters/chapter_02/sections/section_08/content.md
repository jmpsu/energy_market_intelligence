# 2.8 Pipeline operations, nominations, and scheduling

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-028 Simulate Daily Gas Nominations (`python3 emi.py run 028`). Full output: `exercises/completed/ex028/report.md`.

## L02.08.1 The gas day and nomination cycles

**Objective.** Explain the gas day and nomination cycles and show it in the EX-028 output.

**Prerequisites.** L02.07.5

**Lesson.** The gas day is a 24-hour delivery period with several nomination cycles. [K]

**Example.** EX-028 (Simulate Daily Gas Nominations) on synthetic North American data: nominated_MMBtu = 510000 [EX]

**Do.** `python3 emi.py run 028 | grep '^nominated_MMBtu:'`

**Expect.** `nominated_MMBtu: 510000`

**On the job.** Build a simplified nomination schedule showing requested quantities, pipeline confirmations, and scheduled volumes.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.07.5 | After: L02.08.2

## L02.08.2 Nomination, confirmation, scheduling

**Objective.** Explain nomination, confirmation, scheduling and show it in the EX-028 output.

**Prerequisites.** L02.08.1

**Lesson.** A nomination requests a flow; both ends must confirm it; the pipeline then schedules it. [K]

**Example.** EX-028 (Simulate Daily Gas Nominations) on synthetic North American data: confirmed_MMBtu = 490000 [EX]

**Do.** `python3 emi.py run 028 | grep '^confirmed_MMBtu:'`

**Expect.** `confirmed_MMBtu: 490000`

**On the job.** Build a simplified nomination schedule showing requested quantities, pipeline confirmations, and scheduled volumes.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.08.1 | After: L02.08.3

## L02.08.3 Cuts and priority of service

**Objective.** Explain cuts and priority of service and show it in the EX-028 output.

**Prerequisites.** L02.08.2

**Lesson.** When requests exceed capacity, the pipeline cuts lowest-priority service first. [K]

**Example.** EX-028 (Simulate Daily Gas Nominations) on synthetic North American data: scheduled_MMBtu = 420000 [EX]

**Do.** `python3 emi.py run 028 | grep '^scheduled_MMBtu:'`

**Expect.** `scheduled_MMBtu: 420000`

**On the job.** Build a simplified nomination schedule showing requested quantities, pipeline confirmations, and scheduled volumes.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.08.2 | After: L02.08.4

## L02.08.4 Allocation and measurement

**Objective.** Explain allocation and measurement and show it in the EX-028 output.

**Prerequisites.** L02.08.3

**Lesson.** Measured flows are allocated to shippers after the day and rarely match schedules exactly. [K]

**Example.** EX-028 (Simulate Daily Gas Nominations) on synthetic North American data: confirmation_cuts_MMBtu = 20000 [EX]

**Do.** `python3 emi.py run 028 | grep '^confirmation_cuts_MMBtu:'`

**Expect.** `confirmation_cuts_MMBtu: 20000`

**On the job.** Build a simplified nomination schedule showing requested quantities, pipeline confirmations, and scheduled volumes.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.08.3 | After: L02.08.5

## L02.08.5 Scheduler daily workflow

**Objective.** Explain scheduler daily workflow and show it in the EX-028 output.

**Prerequisites.** L02.08.4

**Lesson.** A scheduler nominates, checks confirmations, fixes cuts and reconciles actuals every day. [K]

**Example.** EX-028 (Simulate Daily Gas Nominations) on synthetic North American data: capacity_cuts_MMBtu = 70000 [EX]

**Do.** `python3 emi.py run 028 | grep '^capacity_cuts_MMBtu:'`

**Expect.** `capacity_cuts_MMBtu: 70000`

**On the job.** Build a simplified nomination schedule showing requested quantities, pipeline confirmations, and scheduled volumes.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.08.4 | After: L02.09.1
