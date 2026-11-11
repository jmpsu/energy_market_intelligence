# 7.5 Economic dispatch and unit commitment

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-049 Model Electricity Market Clearing (`python3 emi.py run 049`). Full output: `exercises/completed/ex049/report.md`.

## L07.05.1 Merit-order dispatch

**Objective.** Explain merit-order dispatch and show it in the EX-049 output.

**Prerequisites.** L07.04.5

**Lesson.** Merit order stacks units from cheapest to dearest; demand sets the marginal unit. [K]

**Example.** EX-049 (Model Electricity Market Clearing) on synthetic North American data: clearing_price_USD_per_MWh = 42 [EX]

**Do.** `python3 emi.py run 049 | grep '^clearing_price_USD_per_MWh:'`

**Expect.** `clearing_price_USD_per_MWh: 42`

**On the job.** Construct a simplified supply stack and determine the market-clearing price.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.04.5 | After: L07.05.2

## L07.05.2 Unit commitment problem

**Objective.** Explain unit commitment problem and show it in the EX-049 output.

**Prerequisites.** L07.05.1

**Lesson.** Unit commitment decides which units to start, given start costs and limits. [K]

**Example.** EX-049 (Model Electricity Market Clearing) on synthetic North American data: marginal_unit = GAS_02 [EX]

**Do.** `python3 emi.py run 049 | grep '^marginal_unit:'`

**Expect.** `marginal_unit: GAS_02`

**On the job.** Construct a simplified supply stack and determine the market-clearing price.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.05.1 | After: L07.05.3

## L07.05.3 Minimum up and down times

**Objective.** Explain minimum up and down times and show it in the EX-049 output.

**Prerequisites.** L07.05.2

**Lesson.** Minimum up and down times stop units switching on and off freely. [K]

**Example.** EX-049 (Model Electricity Market Clearing) on synthetic North American data: marginal_unit_dispatch_MW = 700 [EX]

**Do.** `python3 emi.py run 049 | grep '^marginal_unit_dispatch_MW:'`

**Expect.** `marginal_unit_dispatch_MW: 700`

**On the job.** Construct a simplified supply stack and determine the market-clearing price.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.05.2 | After: L07.05.4

## L07.05.4 Security-constrained dispatch

**Objective.** Explain security-constrained dispatch and show it in the EX-049 output.

**Prerequisites.** L07.05.3

**Lesson.** Security-constrained dispatch honours transmission limits. [K]

**Example.** EX-049 (Model Electricity Market Clearing) on synthetic North American data: load_payment_USD_per_h = 176400 [EX]

**Do.** `python3 emi.py run 049 | grep '^load_payment_USD_per_h:'`

**Expect.** `load_payment_USD_per_h: 176400`

**On the job.** Construct a simplified supply stack and determine the market-clearing price.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.05.3 | After: L07.05.5

## L07.05.5 Dispatch cost calculation

**Objective.** Explain dispatch cost calculation and show it in the EX-049 output.

**Prerequisites.** L07.05.4

**Lesson.** Dispatch cost is the sum of each unit's output times its marginal cost. [K]

**Example.** EX-049 (Model Electricity Market Clearing) on synthetic North American data: production_cost_USD_per_h = 91500 [EX]

**Do.** `python3 emi.py run 049 | grep '^production_cost_USD_per_h:'`

**Expect.** `production_cost_USD_per_h: 91500`

**On the job.** Construct a simplified supply stack and determine the market-clearing price.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.05.4 | After: L07.06.1
