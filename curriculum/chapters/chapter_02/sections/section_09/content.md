# 2.9 Balancing, linepack, OFOs, and operational notices

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-029 Model Pipeline Imbalances (`python3 emi.py run 029`). Full output: `exercises/completed/ex029/report.md`.

## L02.09.1 Imbalances and tolerances

**Objective.** Explain imbalances and tolerances and show it in the EX-029 output.

**Prerequisites.** L02.08.5

**Lesson.** An imbalance is the gap between what a shipper scheduled and what actually flowed. [K]

**Example.** EX-029 (Model Pipeline Imbalances) on synthetic North American data: Alpha_imbalance_pct = 1.5 [EX]

**Do.** `python3 emi.py run 029 | grep '^Alpha_imbalance_pct:'`

**Expect.** `Alpha_imbalance_pct: 1.5`

**On the job.** Calculate the difference between nominated, confirmed, scheduled, and actual gas deliveries.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.08.5 | After: L02.09.2

## L02.09.2 Linepack as short-term buffer

**Objective.** Explain linepack as short-term buffer and show it in the EX-029 output.

**Prerequisites.** L02.09.1

**Lesson.** Linepack, the gas held in the pipe, absorbs small short-term mismatches. [K]

**Example.** EX-029 (Model Pipeline Imbalances) on synthetic North American data: Beta_imbalance_pct = -5 [EX]

**Do.** `python3 emi.py run 029 | grep '^Beta_imbalance_pct:'`

**Expect.** `Beta_imbalance_pct: -5`

**On the job.** Calculate the difference between nominated, confirmed, scheduled, and actual gas deliveries.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.09.1 | After: L02.09.3

## L02.09.3 Operational flow orders

**Objective.** Explain operational flow orders and show it in the EX-029 output.

**Prerequisites.** L02.09.2

**Lesson.** An operational flow order tightens tolerances when the system is stressed. [K]

**Example.** EX-029 (Model Pipeline Imbalances) on synthetic North American data: Gamma_imbalance_pct = 11 [EX]

**Do.** `python3 emi.py run 029 | grep '^Gamma_imbalance_pct:'`

**Expect.** `Gamma_imbalance_pct: 11`

**On the job.** Calculate the difference between nominated, confirmed, scheduled, and actual gas deliveries.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.09.2 | After: L02.09.4

## L02.09.4 Critical notices and force majeure

**Objective.** Explain critical notices and force majeure and show it in the EX-029 output.

**Prerequisites.** L02.09.3

**Lesson.** Critical notices and force majeure declarations warn of reduced service. [K]

**Example.** EX-029 (Model Pipeline Imbalances) on synthetic North American data: Delta_imbalance_pct = 0 [EX]

**Do.** `python3 emi.py run 029 | grep '^Delta_imbalance_pct:'`

**Expect.** `Delta_imbalance_pct: 0`

**On the job.** Calculate the difference between nominated, confirmed, scheduled, and actual gas deliveries.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.09.3 | After: L02.09.5

## L02.09.5 Imbalance cash-out and penalties

**Objective.** Explain imbalance cash-out and penalties and show it in the EX-029 output.

**Prerequisites.** L02.09.4

**Lesson.** Imbalances beyond tolerance are cashed out at penal prices. [K]

**Example.** EX-029 (Model Pipeline Imbalances) on synthetic North American data: Alpha_cashout_USD = 146250 [EX]

**Do.** `python3 emi.py run 029 | grep '^Alpha_cashout_USD:'`

**Expect.** `Alpha_cashout_USD: 146250`

**On the job.** Calculate the difference between nominated, confirmed, scheduled, and actual gas deliveries.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.09.4 | After: L02.10.1
