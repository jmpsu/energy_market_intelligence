# 2.2 Gathering systems and processing plants

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-013 Model Raw Gas Processing (`python3 emi.py run 013`). Full output: `exercises/completed/ex013/report.md`.

## L02.02.1 Gathering system function

**Objective.** Explain gathering system function and show it in the EX-013 output.

**Prerequisites.** L02.01.5

**Lesson.** Gathering lines collect gas from many wells at low pressure and deliver it to processing. [K]

**Example.** EX-013 (Model Raw Gas Processing) on synthetic North American data: mode = recover [EX]

**Do.** `python3 emi.py run 013 | grep '^mode:'`

**Expect.** `mode: recover`

**On the job.** Calculate the separation of methane and natural gas liquids from raw natural gas.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.01.5 | After: L02.02.2

## L02.02.2 Compression and treating

**Objective.** Explain compression and treating and show it in the EX-013 output.

**Prerequisites.** L02.02.1

**Lesson.** Compression raises pressure for transport; treating removes CO2, H2S and water. [K]

**Example.** EX-013 (Model Raw Gas Processing) on synthetic North American data: inlet_Mcf_per_d = 200000 [EX]

**Do.** `python3 emi.py run 013 | grep '^inlet_Mcf_per_d:'`

**Expect.** `inlet_Mcf_per_d: 200000`

**On the job.** Calculate the separation of methane and natural gas liquids from raw natural gas.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.02.1 | After: L02.02.3

## L02.02.3 Processing plant inlet and outlet

**Objective.** Explain processing plant inlet and outlet and show it in the EX-013 output.

**Prerequisites.** L02.02.2

**Lesson.** A plant takes wet inlet gas and outputs pipeline-quality residue gas plus an NGL stream. [K]

**Example.** EX-013 (Model Raw Gas Processing) on synthetic North American data: inlet_MMBtu_per_d = 250000 [EX]

**Do.** `python3 emi.py run 013 | grep '^inlet_MMBtu_per_d:'`

**Expect.** `inlet_MMBtu_per_d: 250000`

**On the job.** Calculate the separation of methane and natural gas liquids from raw natural gas.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.02.2 | After: L02.02.4

## L02.02.4 Plant fuel and shrinkage

**Objective.** Explain plant fuel and shrinkage and show it in the EX-013 output.

**Prerequisites.** L02.02.3

**Lesson.** Removing NGLs and burning plant fuel shrinks the gas volume and energy that reaches the tailgate. [K]

**Example.** EX-013 (Model Raw Gas Processing) on synthetic North American data: ngl_bbl_per_d = 23319.228571 [EX]

**Do.** `python3 emi.py run 013 | grep '^ngl_bbl_per_d:'`

**Expect.** `ngl_bbl_per_d: 23319.228571`

**On the job.** Calculate the separation of methane and natural gas liquids from raw natural gas.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.02.3 | After: L02.02.5

## L02.02.5 Processing contract types (POP, fee, keep-whole)

**Objective.** Explain processing contract types (POP, fee, keep-whole) and show it in the EX-013 output.

**Prerequisites.** L02.02.4

**Lesson.** Fee contracts pay per unit, POP shares proceeds, keep-whole returns the producer's Btus and leaves the processor exposed to the frac spread. [K]

**Example.** EX-013 (Model Raw Gas Processing) on synthetic North American data: shrink_MMBtu_per_d = 80967.50303 [EX]

**Do.** `python3 emi.py run 013 | grep '^shrink_MMBtu_per_d:'`

**Expect.** `shrink_MMBtu_per_d: 80967.50303`

**On the job.** Calculate the separation of methane and natural gas liquids from raw natural gas.

**Product implication.** Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.

Before: L02.02.4 | After: L02.03.1
