# 2.10 Physical delivery and transportation economics

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-012 Calculate Wellhead-to-Market Economics (`python3 emi.py run 012`). Full output: `exercises/completed/ex012/report.md`.

## L02.10.1 Delivered cost build-up

**Objective.** Explain delivered cost build-up and show it in the EX-012 output.

**Prerequisites.** L02.09.5

**Lesson.** Delivered cost is purchase price plus transport charges plus fuel. [K]

**Example.** EX-012 (Calculate Wellhead-to-Market Economics) on synthetic North American data: Firm_to_West_netback = 2.224 [EX]

**Do.** `python3 emi.py run 012 | grep '^Firm_to_West_netback:'`

**Expect.** `Firm_to_West_netback: 2.224`

**On the job.** Model the effects of gathering, processing, transportation, fuel retention, and other costs on realized gas prices.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.09.5 | After: L02.10.2

## L02.10.2 Fuel retention and commodity charges

**Objective.** Explain fuel retention and commodity charges and show it in the EX-012 output.

**Prerequisites.** L02.10.1

**Lesson.** Fuel retention is gas kept by the pipeline to run compressors; commodity charges are per unit shipped. [K]

**Example.** EX-012 (Calculate Wellhead-to-Market Economics) on synthetic North American data: Firm_to_Gulf_Coast_netback = 2.087 [EX]

**Do.** `python3 emi.py run 012 | grep '^Firm_to_Gulf_Coast_netback:'`

**Expect.** `Firm_to_Gulf_Coast_netback: 2.087`

**On the job.** Model the effects of gathering, processing, transportation, fuel retention, and other costs on realized gas prices.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.10.1 | After: L02.10.3

## L02.10.3 Reservation vs usage charges

**Objective.** Explain reservation vs usage charges and show it in the EX-012 output.

**Prerequisites.** L02.10.2

**Lesson.** Reservation charges are paid for capacity whether used or not; usage charges only when gas flows. [K]

**Example.** EX-012 (Calculate Wellhead-to-Market Economics) on synthetic North American data: Sell_at_Waha_netback = 0.7 [EX]

**Do.** `python3 emi.py run 012 | grep '^Sell_at_Waha_netback:'`

**Expect.** `Sell_at_Waha_netback: 0.7`

**On the job.** Model the effects of gathering, processing, transportation, fuel retention, and other costs on realized gas prices.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.10.2 | After: L02.10.4

## L02.10.4 Realized price at the delivery point

**Objective.** Explain realized price at the delivery point and show it in the EX-012 output.

**Prerequisites.** L02.10.3

**Lesson.** Realised price at the delivery point is the market price there less everything paid to arrive. [K]

**Example.** EX-012 (Calculate Wellhead-to-Market Economics) on synthetic North American data: blended_netback_USD_per_MMBtu = 1.9894 [EX]

**Do.** `python3 emi.py run 012 | grep '^blended_netback_USD_per_MMBtu:'`

**Expect.** `blended_netback_USD_per_MMBtu: 1.9894`

**On the job.** Model the effects of gathering, processing, transportation, fuel retention, and other costs on realized gas prices.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.10.3 | After: L02.10.5

## L02.10.5 Transport value vs basis spread

**Objective.** Explain transport value vs basis spread and show it in the EX-012 output.

**Prerequisites.** L02.10.4

**Lesson.** Transport is worth holding when the basis spread exceeds its variable cost. [K]

**Example.** EX-012 (Calculate Wellhead-to-Market Economics) on synthetic North American data: local_only_netback = 0.7 [EX]

**Do.** `python3 emi.py run 012 | grep '^local_only_netback:'`

**Expect.** `local_only_netback: 0.7`

**On the job.** Model the effects of gathering, processing, transportation, fuel retention, and other costs on realized gas prices.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.10.4 | After: L03.01.1
