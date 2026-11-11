# 3.7 Storage economics and seasonal spreads

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-025 Calculate Gas Storage Arbitrage (`python3 emi.py run 025`). Full output: `exercises/completed/ex025/report.md`.

## L03.07.1 Intrinsic storage value

**Objective.** Explain intrinsic storage value and show it in the EX-025 output.

**Prerequisites.** L03.06.5

**Lesson.** Intrinsic value is the spread you can lock today by buying a cheap month and selling a dear one. [K]

**Example.** EX-025 (Calculate Gas Storage Arbitrage) on synthetic North American data: interpretation = inventory = end-of-month; opening = December close [EX]

**Do.** `python3 emi.py run 025 | grep '^interpretation:'`

**Expect.** `interpretation: inventory = end-of-month; opening = December close`

**On the job.** Compare injection costs, withdrawal costs, seasonal price spreads, and storage economics.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.06.5 | After: L03.07.2

## L03.07.2 Extrinsic and optionality value

**Objective.** Explain extrinsic and optionality value and show it in the EX-025 output.

**Prerequisites.** L03.07.1

**Lesson.** Extrinsic value is the extra from re-optimising as spreads move. [K]

**Example.** EX-025 (Calculate Gas Storage Arbitrage) on synthetic North American data: all_months_within_limits = True [EX]

**Do.** `python3 emi.py run 025 | grep '^all_months_within_limits:'`

**Expect.** `all_months_within_limits: True`

**On the job.** Compare injection costs, withdrawal costs, seasonal price spreads, and storage economics.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.07.1 | After: L03.07.3

## L03.07.3 Injection and withdrawal cost and fuel

**Objective.** Explain injection and withdrawal cost and fuel and show it in the EX-025 output.

**Prerequisites.** L03.07.2

**Lesson.** Injection and withdrawal fees plus fuel reduce the captured spread. [K]

**Example.** EX-025 (Calculate Gas Storage Arbitrage) on synthetic North American data: total_injected_MMBtu = 90000 [EX]

**Do.** `python3 emi.py run 025 | grep '^total_injected_MMBtu:'`

**Expect.** `total_injected_MMBtu: 90000`

**On the job.** Compare injection costs, withdrawal costs, seasonal price spreads, and storage economics.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.07.2 | After: L03.07.4

## L03.07.4 Seasonal spread capture

**Objective.** Explain seasonal spread capture and show it in the EX-025 output.

**Prerequisites.** L03.07.3

**Lesson.** Storage monetises the summer-winter spread. [K]

**Example.** EX-025 (Calculate Gas Storage Arbitrage) on synthetic North American data: total_withdrawn_MMBtu = 90000 [EX]

**Do.** `python3 emi.py run 025 | grep '^total_withdrawn_MMBtu:'`

**Expect.** `total_withdrawn_MMBtu: 90000`

**On the job.** Compare injection costs, withdrawal costs, seasonal price spreads, and storage economics.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.07.3 | After: L03.07.5

## L03.07.5 Storage constraint effects on value

**Objective.** Explain storage constraint effects on value and show it in the EX-025 output.

**Prerequisites.** L03.07.4

**Lesson.** Capacity and ratchet limits cap how much of the spread can be captured. [K]

**Example.** EX-025 (Calculate Gas Storage Arbitrage) on synthetic North American data: purchase_cost_USD = 257142.857143 [EX]

**Do.** `python3 emi.py run 025 | grep '^purchase_cost_USD:'`

**Expect.** `purchase_cost_USD: 257142.857143`

**On the job.** Compare injection costs, withdrawal costs, seasonal price spreads, and storage economics.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.07.4 | After: L03.08.1
