# 12.4 Integrated gas-fired generation optimization

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-068 Build a Multi-Commodity Asset Optimization Model (`python3 emi.py run 068`). Full output: `exercises/completed/ex068/report.md`.

## L12.04.1 Fuel constraints on dispatch

**Objective.** Explain fuel constraints on dispatch and show it in the EX-068 output.

**Prerequisites.** L12.03.5

**Lesson.** Limited gas supply caps how many hours a plant can run. [K]

**Example.** EX-068 (Build a Multi-Commodity Asset Optimization Model) on synthetic North American data: gas_unit_margin_USD = 343055.555556 [EX]

**Do.** `python3 emi.py run 068 | grep '^gas_unit_margin_USD:'`

**Expect.** `gas_unit_margin_USD: 343055.555556`

**On the job.** Optimize a portfolio containing gas supply, gas-fired generation, renewable assets, storage, and electricity market positions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.03.5 | After: L12.04.2

## L12.04.2 Dispatch decision under gas limits

**Objective.** Explain dispatch decision under gas limits and show it in the EX-068 output.

**Prerequisites.** L12.04.1

**Lesson.** Gas is allocated to the highest-margin hours. [K]

**Example.** EX-068 (Build a Multi-Commodity Asset Optimization Model) on synthetic North American data: gas_unit_margin_unconstrained_USD = 429400 [EX]

**Do.** `python3 emi.py run 068 | grep '^gas_unit_margin_unconstrained_USD:'`

**Expect.** `gas_unit_margin_unconstrained_USD: 429400`

**On the job.** Optimize a portfolio containing gas supply, gas-fired generation, renewable assets, storage, and electricity market positions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.04.1 | After: L12.04.3

## L12.04.3 Gas-supply optimization

**Objective.** Explain gas-supply optimization and show it in the EX-068 output.

**Prerequisites.** L12.04.2

**Lesson.** Margin is power revenue less fuel and variable cost. [K]

**Example.** EX-068 (Build a Multi-Commodity Asset Optimization Model) on synthetic North American data: cost_of_gas_limit_USD = 86344.444444 [EX]

**Do.** `python3 emi.py run 068 | grep '^cost_of_gas_limit_USD:'`

**Expect.** `cost_of_gas_limit_USD: 86344.444444`

**On the job.** Optimize a portfolio containing gas supply, gas-fired generation, renewable assets, storage, and electricity market positions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.04.2 | After: L12.04.4

## L12.04.4 Margin calculation

**Objective.** Explain margin calculation and show it in the EX-068 output.

**Prerequisites.** L12.04.3

**Lesson.** Sensitivities show margin change per unit of gas or power price. [K]

**Example.** EX-068 (Build a Multi-Commodity Asset Optimization Model) on synthetic North American data: gas_burn_MMBtu = 40000 [EX]

**Do.** `python3 emi.py run 068 | grep '^gas_burn_MMBtu:'`

**Expect.** `gas_burn_MMBtu: 40000`

**On the job.** Optimize a portfolio containing gas supply, gas-fired generation, renewable assets, storage, and electricity market positions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.04.3 | After: L12.04.5

## L12.04.5 Sensitivity to gas and power prices

**Objective.** Explain sensitivity to gas and power prices and show it in the EX-068 output.

**Prerequisites.** L12.04.4

**Lesson.** Dispatch under a fuel limit is a linear programme. [K]

**Example.** EX-068 (Build a Multi-Commodity Asset Optimization Model) on synthetic North American data: gas_unit_MWh = 5555.555556 [EX]

**Do.** `python3 emi.py run 068 | grep '^gas_unit_MWh:'`

**Expect.** `gas_unit_MWh: 5555.555556`

**On the job.** Optimize a portfolio containing gas supply, gas-fired generation, renewable assets, storage, and electricity market positions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.04.4 | After: L12.05.1
