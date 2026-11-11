# 9.3 Energy price forecasting

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-077 Build a Natural Gas Price Forecast (`python3 emi.py run 077`). Full output: `exercises/completed/ex077/report.md`.

## L09.03.1 Forecast horizons

**Objective.** Explain forecast horizons and show it in the EX-077 output.

**Prerequisites.** L09.02.5

**Lesson.** Short horizons lean on weather and current data; long horizons on fundamentals. [K]

**Example.** EX-077 (Build a Natural Gas Price Forecast) on synthetic North American data: train_rows = 300 [EX]

**Do.** `python3 emi.py run 077 | grep '^train_rows:'`

**Expect.** `train_rows: 300`

**On the job.** Use historical prices and explanatory variables to develop a baseline forecasting model.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.02.5 | After: L09.03.2

## L09.03.2 Time-series models

**Objective.** Explain time-series models and show it in the EX-077 output.

**Prerequisites.** L09.03.1

**Lesson.** Time-series models use the series' own past. [K]

**Example.** EX-077 (Build a Natural Gas Price Forecast) on synthetic North American data: test_rows = 99 [EX]

**Do.** `python3 emi.py run 077 | grep '^test_rows:'`

**Expect.** `test_rows: 99`

**On the job.** Use historical prices and explanatory variables to develop a baseline forecasting model.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.03.1 | After: L09.03.3

## L09.03.3 Regression with fundamentals

**Objective.** Explain regression with fundamentals and show it in the EX-077 output.

**Prerequisites.** L09.03.2

**Lesson.** Regression adds drivers such as weather and storage. [K]

**Example.** EX-077 (Build a Natural Gas Price Forecast) on synthetic North American data: intercept = 0.270758 [EX]

**Do.** `python3 emi.py run 077 | grep '^intercept:'`

**Expect.** `intercept: 0.270758`

**On the job.** Use historical prices and explanatory variables to develop a baseline forecasting model.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.03.2 | After: L09.03.4

## L09.03.4 Forecast evaluation

**Objective.** Explain forecast evaluation and show it in the EX-077 output.

**Prerequisites.** L09.03.3

**Lesson.** Evaluate out of sample against a naive forecast. [K]

**Example.** EX-077 (Build a Natural Gas Price Forecast) on synthetic North American data: coef_lag_price = 0.889493 [EX]

**Do.** `python3 emi.py run 077 | grep '^coef_lag_price:'`

**Expect.** `coef_lag_price: 0.889493`

**On the job.** Use historical prices and explanatory variables to develop a baseline forecasting model.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.03.3 | After: L09.03.5

## L09.03.5 Model selection

**Objective.** Explain model selection and show it in the EX-077 output.

**Prerequisites.** L09.03.4

**Lesson.** Prefer the simplest model that beats the benchmark. [K]

**Example.** EX-077 (Build a Natural Gas Price Forecast) on synthetic North American data: coef_hdd = 0.004145 [EX]

**Do.** `python3 emi.py run 077 | grep '^coef_hdd:'`

**Expect.** `coef_hdd: 0.004145`

**On the job.** Use historical prices and explanatory variables to develop a baseline forecasting model.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.03.4 | After: L09.04.1
