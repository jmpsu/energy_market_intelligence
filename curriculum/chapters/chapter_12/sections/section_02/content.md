# 12.2 Cross-commodity portfolio exposure

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-068 Build a Multi-Commodity Asset Optimization Model (`python3 emi.py run 068`). Full output: `exercises/completed/ex068/report.md`.

## L12.02.1 Exposure mapping across commodities

**Objective.** Explain exposure mapping across commodities and show it in the EX-068 output.

**Prerequisites.** L12.01.5

**Lesson.** Map each asset's exposure to gas, power and NGL prices. [K]

**Example.** EX-068 (Build a Multi-Commodity Asset Optimization Model) on synthetic North American data: gas_unit_margin_USD = 343055.555556 [EX]

**Do.** `python3 emi.py run 068 | grep '^gas_unit_margin_USD:'`

**Expect.** `gas_unit_margin_USD: 343055.555556`

**On the job.** Optimize a portfolio containing gas supply, gas-fired generation, renewable assets, storage, and electricity market positions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.01.5 | After: L12.02.2

## L12.02.2 Cross-commodity correlations

**Objective.** Explain cross-commodity correlations and show it in the EX-068 output.

**Prerequisites.** L12.02.1

**Lesson.** Correlations determine how exposures offset. [K]

**Example.** EX-068 (Build a Multi-Commodity Asset Optimization Model) on synthetic North American data: gas_unit_margin_unconstrained_USD = 429400 [EX]

**Do.** `python3 emi.py run 068 | grep '^gas_unit_margin_unconstrained_USD:'`

**Expect.** `gas_unit_margin_unconstrained_USD: 429400`

**On the job.** Optimize a portfolio containing gas supply, gas-fired generation, renewable assets, storage, and electricity market positions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.02.1 | After: L12.02.3

## L12.02.3 Net position

**Objective.** Explain net position and show it in the EX-068 output.

**Prerequisites.** L12.02.2

**Lesson.** Net position sums exposures in common units. [K]

**Example.** EX-068 (Build a Multi-Commodity Asset Optimization Model) on synthetic North American data: cost_of_gas_limit_USD = 86344.444444 [EX]

**Do.** `python3 emi.py run 068 | grep '^cost_of_gas_limit_USD:'`

**Expect.** `cost_of_gas_limit_USD: 86344.444444`

**On the job.** Optimize a portfolio containing gas supply, gas-fired generation, renewable assets, storage, and electricity market positions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.02.2 | After: L12.02.4

## L12.02.4 Hedge ratio

**Objective.** Explain hedge ratio and show it in the EX-068 output.

**Prerequisites.** L12.02.3

**Lesson.** Hedge ratio is hedge size per unit of exposure. [K]

**Example.** EX-068 (Build a Multi-Commodity Asset Optimization Model) on synthetic North American data: gas_burn_MMBtu = 40000 [EX]

**Do.** `python3 emi.py run 068 | grep '^gas_burn_MMBtu:'`

**Expect.** `gas_burn_MMBtu: 40000`

**On the job.** Optimize a portfolio containing gas supply, gas-fired generation, renewable assets, storage, and electricity market positions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.02.3 | After: L12.02.5

## L12.02.5 Exposure report

**Objective.** Explain exposure report and show it in the EX-068 output.

**Prerequisites.** L12.02.4

**Lesson.** An exposure report shows net position by commodity and period. [K]

**Example.** EX-068 (Build a Multi-Commodity Asset Optimization Model) on synthetic North American data: gas_unit_MWh = 5555.555556 [EX]

**Do.** `python3 emi.py run 068 | grep '^gas_unit_MWh:'`

**Expect.** `gas_unit_MWh: 5555.555556`

**On the job.** Optimize a portfolio containing gas supply, gas-fired generation, renewable assets, storage, and electricity market positions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.02.4 | After: L12.03.1
