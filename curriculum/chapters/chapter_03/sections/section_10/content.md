# 3.10 Basis, volume, operational, and market risk

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-027 Build a Regional Gas Trading Portfolio (`python3 emi.py run 027`). Full output: `exercises/completed/ex027/report.md`.

## L03.10.1 Basis risk

**Objective.** Explain basis risk and show it in the EX-027 output.

**Prerequisites.** L03.09.5

**Lesson.** Basis risk is the chance that the local price moves differently from the hedge. [K]

**Example.** EX-027 (Build a Regional Gas Trading Portfolio) on synthetic North American data: net_position_MMBtu = 40000 [EX]

**Do.** `python3 emi.py run 027 | grep '^net_position_MMBtu:'`

**Expect.** `net_position_MMBtu: 40000`

**On the job.** Combine multiple hub positions and calculate aggregate exposure, basis risk, and P&L.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.09.5 | After: L03.10.2

## L03.10.2 Volume and swing risk

**Objective.** Explain volume and swing risk and show it in the EX-027 output.

**Prerequisites.** L03.10.1

**Lesson.** Volume risk comes from demand or production differing from plan, often in the worst price conditions. [K]

**Example.** EX-027 (Build a Regional Gas Trading Portfolio) on synthetic North American data: gross_position_MMBtu = 1100000 [EX]

**Do.** `python3 emi.py run 027 | grep '^gross_position_MMBtu:'`

**Expect.** `gross_position_MMBtu: 1100000`

**On the job.** Combine multiple hub positions and calculate aggregate exposure, basis risk, and P&L.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.10.1 | After: L03.10.3

## L03.10.3 Operational risk

**Objective.** Explain operational risk and show it in the EX-027 output.

**Prerequisites.** L03.10.2

**Lesson.** Operational risk covers outages, cuts and human error. [K]

**Example.** EX-027 (Build a Regional Gas Trading Portfolio) on synthetic North American data: henry_hub_equivalent_MMBtu = 40000 [EX]

**Do.** `python3 emi.py run 027 | grep '^henry_hub_equivalent_MMBtu:'`

**Expect.** `henry_hub_equivalent_MMBtu: 40000`

**On the job.** Combine multiple hub positions and calculate aggregate exposure, basis risk, and P&L.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.10.2 | After: L03.10.4

## L03.10.4 Market price risk and liquidity

**Objective.** Explain market price risk and liquidity and show it in the EX-027 output.

**Prerequisites.** L03.10.3

**Lesson.** Price risk grows when a market is illiquid and positions cannot be closed at the quoted price. [K]

**Example.** EX-027 (Build a Regional Gas Trading Portfolio) on synthetic North American data: basis_exposure_MMBtu = 450000 [EX]

**Do.** `python3 emi.py run 027 | grep '^basis_exposure_MMBtu:'`

**Expect.** `basis_exposure_MMBtu: 450000`

**On the job.** Combine multiple hub positions and calculate aggregate exposure, basis risk, and P&L.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.10.3 | After: L03.10.5

## L03.10.5 Risk reporting for a gas book

**Objective.** Explain risk reporting for a gas book and show it in the EX-027 output.

**Prerequisites.** L03.10.4

**Lesson.** A risk report shows positions, P&L, limits and the biggest drivers on one page. [K]

**Example.** EX-027 (Build a Regional Gas Trading Portfolio) on synthetic North American data: mtm_day1_USD = 26500 [EX]

**Do.** `python3 emi.py run 027 | grep '^mtm_day1_USD:'`

**Expect.** `mtm_day1_USD: 26500`

**On the job.** Combine multiple hub positions and calculate aggregate exposure, basis risk, and P&L.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.10.4 | After: L04.01.1
