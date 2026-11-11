# 9.4 Supply-demand fundamental models

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-049 Model Electricity Market Clearing (`python3 emi.py run 049`). Full output: `exercises/completed/ex049/report.md`.

## L09.04.1 Supply curve construction

**Objective.** Explain supply curve construction and show it in the EX-049 output.

**Prerequisites.** L09.03.5

**Lesson.** A supply curve orders capacity by marginal cost. [K]

**Example.** EX-049 (Model Electricity Market Clearing) on synthetic North American data: clearing_price_USD_per_MWh = 42 [EX]

**Do.** `python3 emi.py run 049 | grep '^clearing_price_USD_per_MWh:'`

**Expect.** `clearing_price_USD_per_MWh: 42`

**On the job.** Construct a simplified supply stack and determine the market-clearing price.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.03.5 | After: L09.04.2

## L09.04.2 Demand modeling

**Objective.** Explain demand modeling and show it in the EX-049 output.

**Prerequisites.** L09.04.1

**Lesson.** Demand is modelled from weather, calendar and economics. [K]

**Example.** EX-049 (Model Electricity Market Clearing) on synthetic North American data: marginal_unit = GAS_02 [EX]

**Do.** `python3 emi.py run 049 | grep '^marginal_unit:'`

**Expect.** `marginal_unit: GAS_02`

**On the job.** Construct a simplified supply stack and determine the market-clearing price.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.04.1 | After: L09.04.3

## L09.04.3 Equilibrium price

**Objective.** Explain equilibrium price and show it in the EX-049 output.

**Prerequisites.** L09.04.2

**Lesson.** Price is where demand crosses supply. [K]

**Example.** EX-049 (Model Electricity Market Clearing) on synthetic North American data: marginal_unit_dispatch_MW = 700 [EX]

**Do.** `python3 emi.py run 049 | grep '^marginal_unit_dispatch_MW:'`

**Expect.** `marginal_unit_dispatch_MW: 700`

**On the job.** Construct a simplified supply stack and determine the market-clearing price.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.04.2 | After: L09.04.4

## L09.04.4 Supply-curve shape and volatility

**Objective.** Explain supply-curve shape and volatility and show it in the EX-049 output.

**Prerequisites.** L09.04.3

**Lesson.** Where the supply curve is steep, small demand changes move price a lot. [K]

**Example.** EX-049 (Model Electricity Market Clearing) on synthetic North American data: load_payment_USD_per_h = 176400 [EX]

**Do.** `python3 emi.py run 049 | grep '^load_payment_USD_per_h:'`

**Expect.** `load_payment_USD_per_h: 176400`

**On the job.** Construct a simplified supply stack and determine the market-clearing price.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.04.3 | After: L09.04.5

## L09.04.5 Fundamental model calibration

**Objective.** Explain fundamental model calibration and show it in the EX-049 output.

**Prerequisites.** L09.04.4

**Lesson.** Calibrate a fundamental model to observed prices. [K]

**Example.** EX-049 (Model Electricity Market Clearing) on synthetic North American data: production_cost_USD_per_h = 91500 [EX]

**Do.** `python3 emi.py run 049 | grep '^production_cost_USD_per_h:'`

**Expect.** `production_cost_USD_per_h: 91500`

**On the job.** Construct a simplified supply stack and determine the market-clearing price.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.04.4 | After: L09.05.1
