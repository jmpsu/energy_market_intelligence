# 2.7 Storage, injection, and withdrawal

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-025 Calculate Gas Storage Arbitrage (`python3 emi.py run 025`). Full output: `exercises/completed/ex025/report.md`.

## L02.07.1 Storage facility types

**Objective.** Explain storage facility types and show it in the EX-025 output.

**Prerequisites.** L02.06.5

**Lesson.** Depleted reservoirs hold the most gas; salt caverns cycle fastest; aquifers sit between. [K]

**Example.** EX-025 (Calculate Gas Storage Arbitrage) on synthetic North American data: interpretation = inventory = end-of-month; opening = December close [EX]

**Do.** `python3 emi.py run 025 | grep '^interpretation:'`

**Expect.** `interpretation: inventory = end-of-month; opening = December close`

**On the job.** Compare injection costs, withdrawal costs, seasonal price spreads, and storage economics.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.06.5 | After: L02.07.2

## L02.07.2 Working gas vs base gas

**Objective.** Explain working gas vs base gas and show it in the EX-025 output.

**Prerequisites.** L02.07.1

**Lesson.** Working gas can be withdrawn; base gas stays to hold pressure. [K]

**Example.** EX-025 (Calculate Gas Storage Arbitrage) on synthetic North American data: all_months_within_limits = True [EX]

**Do.** `python3 emi.py run 025 | grep '^all_months_within_limits:'`

**Expect.** `all_months_within_limits: True`

**On the job.** Compare injection costs, withdrawal costs, seasonal price spreads, and storage economics.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.07.1 | After: L02.07.3

## L02.07.3 Injection and withdrawal ratchets

**Objective.** Explain injection and withdrawal ratchets and show it in the EX-025 output.

**Prerequisites.** L02.07.2

**Lesson.** Ratchets cut allowed injection or withdrawal rates as inventory moves. [K]

**Example.** EX-025 (Calculate Gas Storage Arbitrage) on synthetic North American data: total_injected_MMBtu = 90000 [EX]

**Do.** `python3 emi.py run 025 | grep '^total_injected_MMBtu:'`

**Expect.** `total_injected_MMBtu: 90000`

**On the job.** Compare injection costs, withdrawal costs, seasonal price spreads, and storage economics.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.07.2 | After: L02.07.4

## L02.07.4 Seasonal storage cycle

**Objective.** Explain seasonal storage cycle and show it in the EX-025 output.

**Prerequisites.** L02.07.3

**Lesson.** Storage fills in the low-demand months and empties in winter. [K]

**Example.** EX-025 (Calculate Gas Storage Arbitrage) on synthetic North American data: total_withdrawn_MMBtu = 90000 [EX]

**Do.** `python3 emi.py run 025 | grep '^total_withdrawn_MMBtu:'`

**Expect.** `total_withdrawn_MMBtu: 90000`

**On the job.** Compare injection costs, withdrawal costs, seasonal price spreads, and storage economics.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.07.3 | After: L02.07.5

## L02.07.5 Deliverability vs inventory

**Objective.** Explain deliverability vs inventory and show it in the EX-025 output.

**Prerequisites.** L02.07.4

**Lesson.** Deliverability is the daily rate, not the inventory: plenty of gas in the ground can still be too slow on a peak day. [K]

**Example.** EX-025 (Calculate Gas Storage Arbitrage) on synthetic North American data: purchase_cost_USD = 257142.857143 [EX]

**Do.** `python3 emi.py run 025 | grep '^purchase_cost_USD:'`

**Expect.** `purchase_cost_USD: 257142.857143`

**On the job.** Compare injection costs, withdrawal costs, seasonal price spreads, and storage economics.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.07.4 | After: L02.08.1
