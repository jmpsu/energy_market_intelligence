# 2.3 Dry gas, associated gas, and gas composition

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-013 Model Raw Gas Processing (`python3 emi.py run 013`). Full output: `exercises/completed/ex013/report.md`.

## L02.03.1 Methane and heavier hydrocarbons

**Objective.** Explain methane and heavier hydrocarbons and show it in the EX-013 output.

**Prerequisites.** L02.02.5

**Lesson.** Raw gas is mostly methane with ethane, propane, butanes and heavier components plus impurities. [K]

**Example.** EX-013 (Model Raw Gas Processing) on synthetic North American data: mode = recover [EX]

**Do.** `python3 emi.py run 013 | grep '^mode:'`

**Expect.** `mode: recover`

**On the job.** Calculate the separation of methane and natural gas liquids from raw natural gas.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.02.5 | After: L02.03.2

## L02.03.2 Heat content and Btu measurement

**Objective.** Explain heat content and Btu measurement and show it in the EX-013 output.

**Prerequisites.** L02.03.1

**Lesson.** Gas is sold on energy (MMBtu), so heat content converts volume to value. [K]

**Example.** EX-013 (Model Raw Gas Processing) on synthetic North American data: inlet_Mcf_per_d = 200000 [EX]

**Do.** `python3 emi.py run 013 | grep '^inlet_Mcf_per_d:'`

**Expect.** `inlet_Mcf_per_d: 200000`

**On the job.** Calculate the separation of methane and natural gas liquids from raw natural gas.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.03.1 | After: L02.03.3

## L02.03.3 Associated gas and oil-price linkage

**Objective.** Explain associated gas and oil-price linkage and show it in the EX-013 output.

**Prerequisites.** L02.03.2

**Lesson.** Associated gas is a by-product of oil wells; it flows whatever the gas price while oil economics work. [K]

**Example.** EX-013 (Model Raw Gas Processing) on synthetic North American data: inlet_MMBtu_per_d = 250000 [EX]

**Do.** `python3 emi.py run 013 | grep '^inlet_MMBtu_per_d:'`

**Expect.** `inlet_MMBtu_per_d: 250000`

**On the job.** Calculate the separation of methane and natural gas liquids from raw natural gas.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.03.2 | After: L02.03.4

## L02.03.4 Pipeline quality specifications

**Objective.** Explain pipeline quality specifications and show it in the EX-013 output.

**Prerequisites.** L02.03.3

**Lesson.** Pipelines set limits on heat content, dew point and contaminants; off-spec gas can be refused. [K]

**Example.** EX-013 (Model Raw Gas Processing) on synthetic North American data: ngl_bbl_per_d = 23319.228571 [EX]

**Do.** `python3 emi.py run 013 | grep '^ngl_bbl_per_d:'`

**Expect.** `ngl_bbl_per_d: 23319.228571`

**On the job.** Calculate the separation of methane and natural gas liquids from raw natural gas.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.03.3 | After: L02.03.5

## L02.03.5 Wet vs dry gas economics

**Objective.** Explain wet vs dry gas economics and show it in the EX-013 output.

**Prerequisites.** L02.03.4

**Lesson.** Wet gas earns extra NGL revenue but needs processing; dry gas does not. [K]

**Example.** EX-013 (Model Raw Gas Processing) on synthetic North American data: shrink_MMBtu_per_d = 80967.50303 [EX]

**Do.** `python3 emi.py run 013 | grep '^shrink_MMBtu_per_d:'`

**Expect.** `shrink_MMBtu_per_d: 80967.50303`

**On the job.** Calculate the separation of methane and natural gas liquids from raw natural gas.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.03.4 | After: L02.04.1
