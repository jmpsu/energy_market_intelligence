# 12.5 Renewable and storage scenario modeling

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-065 Optimize a Combined Renewable and Storage Portfolio (`python3 emi.py run 065`). Full output: `exercises/completed/ex065/report.md`.

## L12.05.1 Renewable scenario generation

**Objective.** Explain renewable scenario generation and show it in the EX-065 output.

**Prerequisites.** L12.04.5

**Lesson.** Renewable scenarios span plausible output paths. [K]

**Example.** EX-065 (Optimize a Combined Renewable and Storage Portfolio) on synthetic North American data: direct_solar_revenue_USD = 55910 [EX]

**Do.** `python3 emi.py run 065 | grep '^direct_solar_revenue_USD:'`

**Expect.** `direct_solar_revenue_USD: 55910`

**On the job.** Calculate dispatch decisions across solar generation, battery storage, and market purchases.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.04.5 | After: L12.05.2

## L12.05.2 Storage dispatch under scenarios

**Objective.** Explain storage dispatch under scenarios and show it in the EX-065 output.

**Prerequisites.** L12.05.1

**Lesson.** Storage dispatch is optimised in each. [K]

**Example.** EX-065 (Optimize a Combined Renewable and Storage Portfolio) on synthetic North American data: solar_plus_storage_revenue_USD = 69590 [EX]

**Do.** `python3 emi.py run 065 | grep '^solar_plus_storage_revenue_USD:'`

**Expect.** `solar_plus_storage_revenue_USD: 69590`

**On the job.** Calculate dispatch decisions across solar generation, battery storage, and market purchases.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.05.1 | After: L12.05.3

## L12.05.3 Shortfall analysis

**Objective.** Explain shortfall analysis and show it in the EX-065 output.

**Prerequisites.** L12.05.2

**Lesson.** Shortfall analysis finds when supply misses load. [K]

**Example.** EX-065 (Optimize a Combined Renewable and Storage Portfolio) on synthetic North American data: storage_uplift_USD = 13680 [EX]

**Do.** `python3 emi.py run 065 | grep '^storage_uplift_USD:'`

**Expect.** `storage_uplift_USD: 13680`

**On the job.** Calculate dispatch decisions across solar generation, battery storage, and market purchases.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.05.2 | After: L12.05.4

## L12.05.4 Value of storage

**Objective.** Explain value of storage and show it in the EX-065 output.

**Prerequisites.** L12.05.3

**Lesson.** Storage value is the margin with it less the margin without. [K]

**Example.** EX-065 (Optimize a Combined Renewable and Storage Portfolio) on synthetic North American data: energy_charged_MWh = 266.666667 [EX]

**Do.** `python3 emi.py run 065 | grep '^energy_charged_MWh:'`

**Expect.** `energy_charged_MWh: 266.666667`

**On the job.** Calculate dispatch decisions across solar generation, battery storage, and market purchases.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.05.3 | After: L12.05.5

## L12.05.5 Scenario comparison

**Objective.** Explain scenario comparison and show it in the EX-065 output.

**Prerequisites.** L12.05.4

**Lesson.** Compare scenarios on margin and shortfall. [K]

**Example.** EX-065 (Optimize a Combined Renewable and Storage Portfolio) on synthetic North American data: energy_discharged_MWh = 240 [EX]

**Do.** `python3 emi.py run 065 | grep '^energy_discharged_MWh:'`

**Expect.** `energy_discharged_MWh: 240`

**On the job.** Calculate dispatch decisions across solar generation, battery storage, and market purchases.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.05.4 | After: L12.06.1
