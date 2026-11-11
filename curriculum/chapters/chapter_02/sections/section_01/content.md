# 2.1 Natural gas production and resource basins

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-010 Compare Major US Gas-Producing Basins (`python3 emi.py run 010`). Full output: `exercises/completed/ex010/report.md`.

## L02.01.1 Shale basin geography

**Objective.** Explain shale basin geography and show it in the EX-010 output.

**Prerequisites.** L01.10.5

**Lesson.** Major US gas comes from a few shale basins; each has different costs, liquids content and distance to market. [K]

**Example.** EX-010 (Compare Major US Gas-Producing Basins) on synthetic North American data: Appalachian_netback_USD_per_MMBtu = 0.55 [EX]

**Do.** `python3 emi.py run 010 | grep '^Appalachian_netback_USD_per_MMBtu:'`

**Expect.** `Appalachian_netback_USD_per_MMBtu: 0.55`

**On the job.** Analyze production volumes, growth rates, and economic characteristics across the Appalachian, Permian, and Haynesville basins.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L01.10.5 | After: L02.01.2

## L02.01.2 Production volumes and growth rates

**Objective.** Explain production volumes and growth rates and show it in the EX-010 output.

**Prerequisites.** L02.01.1

**Lesson.** Growth rate matters as much as level: fast-growing basins outrun their pipelines. [K]

**Example.** EX-010 (Compare Major US Gas-Producing Basins) on synthetic North American data: Permian_netback_USD_per_MMBtu = -0.45 [EX]

**Do.** `python3 emi.py run 010 | grep '^Permian_netback_USD_per_MMBtu:'`

**Expect.** `Permian_netback_USD_per_MMBtu: -0.45`

**On the job.** Analyze production volumes, growth rates, and economic characteristics across the Appalachian, Permian, and Haynesville basins.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.01.1 | After: L02.01.3

## L02.01.3 Decline curves and drilling economics

**Objective.** Explain decline curves and drilling economics and show it in the EX-010 output.

**Prerequisites.** L02.01.2

**Lesson.** Shale wells decline steeply, so steady output needs continuous drilling. [K]

**Example.** EX-010 (Compare Major US Gas-Producing Basins) on synthetic North American data: Haynesville_netback_USD_per_MMBtu = 0.85 [EX]

**Do.** `python3 emi.py run 010 | grep '^Haynesville_netback_USD_per_MMBtu:'`

**Expect.** `Haynesville_netback_USD_per_MMBtu: 0.85`

**On the job.** Analyze production volumes, growth rates, and economic characteristics across the Appalachian, Permian, and Haynesville basins.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.01.2 | After: L02.01.4

## L02.01.4 Breakeven and netback by basin

**Objective.** Explain breakeven and netback by basin and show it in the EX-010 output.

**Prerequisites.** L02.01.3

**Lesson.** Netback is the market price minus the cost to get there; breakeven is the price at which a new well earns its return. [K]

**Example.** EX-010 (Compare Major US Gas-Producing Basins) on synthetic North American data: Appalachian_growth_pct = 3.529412 [EX]

**Do.** `python3 emi.py run 010 | grep '^Appalachian_growth_pct:'`

**Expect.** `Appalachian_growth_pct: 3.529412`

**On the job.** Analyze production volumes, growth rates, and economic characteristics across the Appalachian, Permian, and Haynesville basins.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.01.3 | After: L02.01.5

## L02.01.5 Basin takeaway dependence

**Objective.** Explain basin takeaway dependence and show it in the EX-010 output.

**Prerequisites.** L02.01.4

**Lesson.** A basin with too little takeaway capacity sells at a discount until new pipe arrives. [K]

**Example.** EX-010 (Compare Major US Gas-Producing Basins) on synthetic North American data: Permian_growth_pct = 6.521739 [EX]

**Do.** `python3 emi.py run 010 | grep '^Permian_growth_pct:'`

**Expect.** `Permian_growth_pct: 6.521739`

**On the job.** Analyze production volumes, growth rates, and economic characteristics across the Appalachian, Permian, and Haynesville basins.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.01.4 | After: L02.02.1
