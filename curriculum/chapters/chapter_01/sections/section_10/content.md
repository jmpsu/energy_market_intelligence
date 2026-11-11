# 1.10 The energy value chain and integrated market modeling

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-009 Construct an Integrated Energy Market Dashboard (`python3 emi.py run 009`). Full output: `exercises/completed/ex009/report.md`.

## L01.10.1 Wellhead-to-burner-tip value chain

**Objective.** Explain wellhead-to-burner-tip value chain and show it in the EX-009 output.

**Prerequisites.** L01.09.5

**Lesson.** Value is added or lost at each step from wellhead to burner tip: gathering, processing, transport, distribution. [K]

**Example.** EX-009 (Construct an Integrated Energy Market Dashboard) on synthetic North American data: days = 60 [EX]

**Do.** `python3 emi.py run 009 | grep '^days:'`

**Expect.** `days: 60`

**On the job.** Combine gas prices, electricity prices, production, storage, weather, and generation data into one analytical view.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.09.5 | After: L01.10.2

## L01.10.2 Fuel-to-power conversion link

**Objective.** Explain fuel-to-power conversion link and show it in the EX-009 output.

**Prerequisites.** L01.10.1

**Lesson.** A gas plant converts MMBtu to MWh at its heat rate, which ties the gas price to the power price. [K]

**Example.** EX-009 (Construct an Integrated Energy Market Dashboard) on synthetic North American data: corr_gas_power = 0.566886 [EX]

**Do.** `python3 emi.py run 009 | grep '^corr_gas_power:'`

**Expect.** `corr_gas_power: 0.566886`

**On the job.** Combine gas prices, electricity prices, production, storage, weather, and generation data into one analytical view.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.10.1 | After: L01.10.3

## L01.10.3 Value capture at each stage

**Objective.** Explain value capture at each stage and show it in the EX-009 output.

**Prerequisites.** L01.10.2

**Lesson.** Each stage captures a margin: fees for infrastructure, spreads for traders, spark spread for generators. [K]

**Example.** EX-009 (Construct an Integrated Energy Market Dashboard) on synthetic North American data: corr_hdd_gas = 0.791867 [EX]

**Do.** `python3 emi.py run 009 | grep '^corr_hdd_gas:'`

**Expect.** `corr_hdd_gas: 0.791867`

**On the job.** Combine gas prices, electricity prices, production, storage, weather, and generation data into one analytical view.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.10.2 | After: L01.10.4

## L01.10.4 Integrated gas-power modeling rationale

**Objective.** Explain integrated gas-power modeling rationale and show it in the EX-009 output.

**Prerequisites.** L01.10.3

**Lesson.** Modeling gas and power together captures feedback that separate models miss. [K]

**Example.** EX-009 (Construct an Integrated Energy Market Dashboard) on synthetic North American data: corr_hdd_storage_change = -0.99849 [EX]

**Do.** `python3 emi.py run 009 | grep '^corr_hdd_storage_change:'`

**Expect.** `corr_hdd_storage_change: -0.99849`

**On the job.** Combine gas prices, electricity prices, production, storage, weather, and generation data into one analytical view.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.10.3 | After: L01.10.5

## L01.10.5 Building a reference model of the chain

**Objective.** Explain building a reference model of the chain and show it in the EX-009 output.

**Prerequisites.** L01.10.4

**Lesson.** A reference model fixes locations, units and identifiers so every later analysis joins cleanly. [K]

**Example.** EX-009 (Construct an Integrated Energy Market Dashboard) on synthetic North American data: mean_implied_heat_rate = 12.333135 [EX]

**Do.** `python3 emi.py run 009 | grep '^mean_implied_heat_rate:'`

**Expect.** `mean_implied_heat_rate: 12.333135`

**On the job.** Combine gas prices, electricity prices, production, storage, weather, and generation data into one analytical view.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.10.4 | After: L02.01.1
