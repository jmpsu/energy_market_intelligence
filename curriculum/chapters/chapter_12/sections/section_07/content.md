# 12.7 Portfolio valuation and stress testing

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-100 Complete an Integrated Energy Portfolio Capstone (`python3 emi.py run 100`). Full output: `exercises/completed/ex100/report.md`.

## L12.07.1 Portfolio valuation

**Objective.** Explain portfolio valuation and show it in the EX-100 output.

**Prerequisites.** L12.06.5

**Lesson.** Portfolio valuation marks every asset and trade to the curve. [K]

**Example.** EX-100 (Complete an Integrated Energy Portfolio Capstone) on synthetic North American data: Base_portfolio_value_USD = 1617201.470588 [EX]

**Do.** `python3 emi.py run 100 | grep '^Base_portfolio_value_USD:'`

**Expect.** `Base_portfolio_value_USD: 1617201.470588`

**On the job.** Build and analyze a hypothetical North American energy portfolio spanning natural gas, NGLs, electricity, generation assets, storage, trading positions, and market risk. Execute the analysis through the terminal, validate the results, identify commercial opportunities and risks, and present a product strategy explaining how an integrated simulation and analytics platform could support the decisions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.06.5 | After: L12.07.2

## L12.07.2 Scenario revaluation

**Objective.** Explain scenario revaluation and show it in the EX-100 output.

**Prerequisites.** L12.07.1

**Lesson.** Scenario revaluation reprices under changed inputs. [K]

**Example.** EX-100 (Complete an Integrated Energy Portfolio Capstone) on synthetic North American data: Gas_Spike_portfolio_value_USD = 2579646.764706 [EX]

**Do.** `python3 emi.py run 100 | grep '^Gas_Spike_portfolio_value_USD:'`

**Expect.** `Gas_Spike_portfolio_value_USD: 2579646.764706`

**On the job.** Build and analyze a hypothetical North American energy portfolio spanning natural gas, NGLs, electricity, generation assets, storage, trading positions, and market risk. Execute the analysis through the terminal, validate the results, identify commercial opportunities and risks, and present a product strategy explaining how an integrated simulation and analytics platform could support the decisions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.07.1 | After: L12.07.3

## L12.07.3 Stress loss measurement

**Objective.** Explain stress loss measurement and show it in the EX-100 output.

**Prerequisites.** L12.07.2

**Lesson.** Stress loss is the value drop in the worst scenarios. [K]

**Example.** EX-100 (Complete an Integrated Energy Portfolio Capstone) on synthetic North American data: Power_Scarcity_portfolio_value_USD = 3037356.176471 [EX]

**Do.** `python3 emi.py run 100 | grep '^Power_Scarcity_portfolio_value_USD:'`

**Expect.** `Power_Scarcity_portfolio_value_USD: 3037356.176471`

**On the job.** Build and analyze a hypothetical North American energy portfolio spanning natural gas, NGLs, electricity, generation assets, storage, trading positions, and market risk. Execute the analysis through the terminal, validate the results, identify commercial opportunities and risks, and present a product strategy explaining how an integrated simulation and analytics platform could support the decisions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.07.2 | After: L12.07.4

## L12.07.4 Risk limits check

**Objective.** Explain risk limits check and show it in the EX-100 output.

**Prerequisites.** L12.07.3

**Lesson.** Check each result against limits. [K]

**Example.** EX-100 (Complete an Integrated Energy Portfolio Capstone) on synthetic North American data: Pipeline_Disruption_portfolio_value_USD = 1947938.058824 [EX]

**Do.** `python3 emi.py run 100 | grep '^Pipeline_Disruption_portfolio_value_USD:'`

**Expect.** `Pipeline_Disruption_portfolio_value_USD: 1947938.058824`

**On the job.** Build and analyze a hypothetical North American energy portfolio spanning natural gas, NGLs, electricity, generation assets, storage, trading positions, and market risk. Execute the analysis through the terminal, validate the results, identify commercial opportunities and risks, and present a product strategy explaining how an integrated simulation and analytics platform could support the decisions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.07.3 | After: L12.07.5

## L12.07.5 Risk memo

**Objective.** Explain risk memo and show it in the EX-100 output.

**Prerequisites.** L12.07.4

**Lesson.** A risk memo states exposure, breaches and actions. [K]

**Example.** EX-100 (Complete an Integrated Energy Portfolio Capstone) on synthetic North American data: Renewable_Shortfall_portfolio_value_USD = 2128587.352941 [EX]

**Do.** `python3 emi.py run 100 | grep '^Renewable_Shortfall_portfolio_value_USD:'`

**Expect.** `Renewable_Shortfall_portfolio_value_USD: 2128587.352941`

**On the job.** Build and analyze a hypothetical North American energy portfolio spanning natural gas, NGLs, electricity, generation assets, storage, trading positions, and market risk. Execute the analysis through the terminal, validate the results, identify commercial opportunities and risks, and present a product strategy explaining how an integrated simulation and analytics platform could support the decisions.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.07.4 | After: L12.08.1
