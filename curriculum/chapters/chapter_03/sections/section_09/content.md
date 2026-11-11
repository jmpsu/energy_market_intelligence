# 3.9 Natural gas position management and valuation

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-027 Build a Regional Gas Trading Portfolio (`python3 emi.py run 027`). Full output: `exercises/completed/ex027/report.md`.

## L03.09.1 Position aggregation by hub and tenor

**Objective.** Explain position aggregation by hub and tenor and show it in the EX-027 output.

**Prerequisites.** L03.08.5

**Lesson.** Positions are summed by hub and delivery month to see net exposure. [K]

**Example.** EX-027 (Build a Regional Gas Trading Portfolio) on synthetic North American data: net_position_MMBtu = 40000 [EX]

**Do.** `python3 emi.py run 027 | grep '^net_position_MMBtu:'`

**Expect.** `net_position_MMBtu: 40000`

**On the job.** Combine multiple hub positions and calculate aggregate exposure, basis risk, and P&L.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.08.5 | After: L03.09.2

## L03.09.2 Mark-to-market valuation

**Objective.** Explain mark-to-market valuation and show it in the EX-027 output.

**Prerequisites.** L03.09.1

**Lesson.** Mark-to-market values each position at the current curve. [K]

**Example.** EX-027 (Build a Regional Gas Trading Portfolio) on synthetic North American data: gross_position_MMBtu = 1100000 [EX]

**Do.** `python3 emi.py run 027 | grep '^gross_position_MMBtu:'`

**Expect.** `gross_position_MMBtu: 1100000`

**On the job.** Combine multiple hub positions and calculate aggregate exposure, basis risk, and P&L.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.09.1 | After: L03.09.3

## L03.09.3 Fixed, index and basis exposure decomposition

**Objective.** Explain fixed, index and basis exposure decomposition and show it in the EX-027 output.

**Prerequisites.** L03.09.2

**Lesson.** A regional position splits into a Henry Hub exposure and a basis exposure. [K]

**Example.** EX-027 (Build a Regional Gas Trading Portfolio) on synthetic North American data: henry_hub_equivalent_MMBtu = 40000 [EX]

**Do.** `python3 emi.py run 027 | grep '^henry_hub_equivalent_MMBtu:'`

**Expect.** `henry_hub_equivalent_MMBtu: 40000`

**On the job.** Combine multiple hub positions and calculate aggregate exposure, basis risk, and P&L.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.09.2 | After: L03.09.4

## L03.09.4 Daily P&L calculation

**Objective.** Explain daily P&L calculation and show it in the EX-027 output.

**Prerequisites.** L03.09.3

**Lesson.** Daily P&L is position times price change plus the effect of new trades. [K]

**Example.** EX-027 (Build a Regional Gas Trading Portfolio) on synthetic North American data: basis_exposure_MMBtu = 450000 [EX]

**Do.** `python3 emi.py run 027 | grep '^basis_exposure_MMBtu:'`

**Expect.** `basis_exposure_MMBtu: 450000`

**On the job.** Combine multiple hub positions and calculate aggregate exposure, basis risk, and P&L.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.09.3 | After: L03.09.5

## L03.09.5 Position limits

**Objective.** Explain position limits and show it in the EX-027 output.

**Prerequisites.** L03.09.4

**Lesson.** Limits cap position size or risk by trader, book and location. [K]

**Example.** EX-027 (Build a Regional Gas Trading Portfolio) on synthetic North American data: mtm_day1_USD = 26500 [EX]

**Do.** `python3 emi.py run 027 | grep '^mtm_day1_USD:'`

**Expect.** `mtm_day1_USD: 26500`

**On the job.** Combine multiple hub positions and calculate aggregate exposure, basis risk, and P&L.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.09.4 | After: L03.10.1
