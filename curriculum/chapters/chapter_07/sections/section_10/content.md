# 7.10 Integrated generation, storage, and portfolio optimization

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-065 Optimize a Combined Renewable and Storage Portfolio (`python3 emi.py run 065`). Full output: `exercises/completed/ex065/report.md`.

## L07.10.1 Portfolio dispatch

**Objective.** Explain portfolio dispatch and show it in the EX-065 output.

**Prerequisites.** L07.09.5

**Lesson.** Portfolio dispatch runs several assets against one price view. [K]

**Example.** EX-065 (Optimize a Combined Renewable and Storage Portfolio) on synthetic North American data: direct_solar_revenue_USD = 55910 [EX]

**Do.** `python3 emi.py run 065 | grep '^direct_solar_revenue_USD:'`

**Expect.** `direct_solar_revenue_USD: 55910`

**On the job.** Calculate dispatch decisions across solar generation, battery storage, and market purchases.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.09.5 | After: L07.10.2

## L07.10.2 Co-optimization of assets

**Objective.** Explain co-optimization of assets and show it in the EX-065 output.

**Prerequisites.** L07.10.1

**Lesson.** Co-optimising beats optimising each asset alone. [K]

**Example.** EX-065 (Optimize a Combined Renewable and Storage Portfolio) on synthetic North American data: solar_plus_storage_revenue_USD = 69590 [EX]

**Do.** `python3 emi.py run 065 | grep '^solar_plus_storage_revenue_USD:'`

**Expect.** `solar_plus_storage_revenue_USD: 69590`

**On the job.** Calculate dispatch decisions across solar generation, battery storage, and market purchases.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.10.1 | After: L07.10.3

## L07.10.3 Hedge overlay

**Objective.** Explain hedge overlay and show it in the EX-065 output.

**Prerequisites.** L07.10.2

**Lesson.** Hedges are layered on the expected physical position. [K]

**Example.** EX-065 (Optimize a Combined Renewable and Storage Portfolio) on synthetic North American data: storage_uplift_USD = 13680 [EX]

**Do.** `python3 emi.py run 065 | grep '^storage_uplift_USD:'`

**Expect.** `storage_uplift_USD: 13680`

**On the job.** Calculate dispatch decisions across solar generation, battery storage, and market purchases.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.10.2 | After: L07.10.4

## L07.10.4 Constraint interactions

**Objective.** Explain constraint interactions and show it in the EX-065 output.

**Prerequisites.** L07.10.3

**Lesson.** Shared limits such as an interconnection cap couple the assets. [K]

**Example.** EX-065 (Optimize a Combined Renewable and Storage Portfolio) on synthetic North American data: energy_charged_MWh = 266.666667 [EX]

**Do.** `python3 emi.py run 065 | grep '^energy_charged_MWh:'`

**Expect.** `energy_charged_MWh: 266.666667`

**On the job.** Calculate dispatch decisions across solar generation, battery storage, and market purchases.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.10.3 | After: L07.10.5

## L07.10.5 Portfolio margin optimization

**Objective.** Explain portfolio margin optimization and show it in the EX-065 output.

**Prerequisites.** L07.10.4

**Lesson.** The objective is total margin subject to every constraint. [K]

**Example.** EX-065 (Optimize a Combined Renewable and Storage Portfolio) on synthetic North American data: energy_discharged_MWh = 240 [EX]

**Do.** `python3 emi.py run 065 | grep '^energy_discharged_MWh:'`

**Expect.** `energy_discharged_MWh: 240`

**On the job.** Calculate dispatch decisions across solar generation, battery storage, and market purchases.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.10.4 | After: L08.01.1
