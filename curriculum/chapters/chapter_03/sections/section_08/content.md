# 3.8 LNG feed-gas demand and international price relationships

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-033 Calculate LNG Export Netbacks (`python3 emi.py run 033`). Full output: `exercises/completed/ex033/report.md`.

## L03.08.1 Feed-gas demand drivers

**Objective.** Explain feed-gas demand drivers and show it in the EX-033 output.

**Prerequisites.** L03.07.5

**Lesson.** LNG feed gas demand depends on terminal capacity, utilisation and global spreads. [K]

**Example.** EX-033 (Calculate LNG Export Netbacks) on synthetic North American data: fob_cost_USD_per_MMBtu = 6.2375 [EX]

**Do.** `python3 emi.py run 033 | grep '^fob_cost_USD_per_MMBtu:'`

**Expect.** `fob_cost_USD_per_MMBtu: 6.2375`

**On the job.** Compare Henry Hub costs with international LNG selling prices after liquefaction, shipping, and regasification costs.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.07.5 | After: L03.08.2

## L03.08.2 Liquefaction tolling economics

**Objective.** Explain liquefaction tolling economics and show it in the EX-033 output.

**Prerequisites.** L03.08.1

**Lesson.** A tolling customer pays a fixed liquefaction fee whether or not it lifts cargoes. [K]

**Example.** EX-033 (Calculate LNG Export Netbacks) on synthetic North American data: Europe_margin_USD_per_MMBtu = 3.4625 [EX]

**Do.** `python3 emi.py run 033 | grep '^Europe_margin_USD_per_MMBtu:'`

**Expect.** `Europe_margin_USD_per_MMBtu: 3.4625`

**On the job.** Compare Henry Hub costs with international LNG selling prices after liquefaction, shipping, and regasification costs.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.08.1 | After: L03.08.3

## L03.08.3 Netback pricing

**Objective.** Explain netback pricing and show it in the EX-033 output.

**Prerequisites.** L03.08.2

**Lesson.** Netback is the destination price less regasification, shipping and liquefaction costs. [K]

**Example.** EX-033 (Calculate LNG Export Netbacks) on synthetic North American data: Asia_margin_USD_per_MMBtu = 3.9625 [EX]

**Do.** `python3 emi.py run 033 | grep '^Asia_margin_USD_per_MMBtu:'`

**Expect.** `Asia_margin_USD_per_MMBtu: 3.9625`

**On the job.** Compare Henry Hub costs with international LNG selling prices after liquefaction, shipping, and regasification costs.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.08.2 | After: L03.08.4

## L03.08.4 Henry Hub-linked export contracts

**Objective.** Explain henry Hub-linked export contracts and show it in the EX-033 output.

**Prerequisites.** L03.08.3

**Lesson.** Many US contracts price LNG as a Henry Hub multiple plus a fixed fee. [K]

**Example.** EX-033 (Calculate LNG Export Netbacks) on synthetic North American data: Europe_cargo_margin_USD = 11772500 [EX]

**Do.** `python3 emi.py run 033 | grep '^Europe_cargo_margin_USD:'`

**Expect.** `Europe_cargo_margin_USD: 11772500`

**On the job.** Compare Henry Hub costs with international LNG selling prices after liquefaction, shipping, and regasification costs.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.08.3 | After: L03.08.5

## L03.08.5 Global price pass-through to Henry Hub

**Objective.** Explain global price pass-through to Henry Hub and show it in the EX-033 output.

**Prerequisites.** L03.08.4

**Lesson.** High global prices pull US gas into export and tighten the domestic balance up to terminal capacity. [K]

**Example.** EX-033 (Calculate LNG Export Netbacks) on synthetic North American data: Asia_cargo_margin_USD = 13472500 [EX]

**Do.** `python3 emi.py run 033 | grep '^Asia_cargo_margin_USD:'`

**Expect.** `Asia_cargo_margin_USD: 13472500`

**On the job.** Compare Henry Hub costs with international LNG selling prices after liquefaction, shipping, and regasification costs.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.08.4 | After: L03.09.1
