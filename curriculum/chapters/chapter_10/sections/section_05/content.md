# 10.5 Forecasting versus fundamental simulation

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-077 Build a Natural Gas Price Forecast (`python3 emi.py run 077`). Full output: `exercises/completed/ex077/report.md`.

## L10.05.1 Statistical forecasting scope

**Objective.** Explain statistical forecasting scope and show it in the EX-077 output.

**Prerequisites.** L10.04.5

**Lesson.** Statistical forecasting fits patterns in history. [K]

**Example.** EX-077 (Build a Natural Gas Price Forecast) on synthetic North American data: train_rows = 300 [EX]

**Do.** `python3 emi.py run 077 | grep '^train_rows:'`

**Expect.** `train_rows: 300`

**On the job.** Use historical prices and explanatory variables to develop a baseline forecasting model.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.04.5 | After: L10.05.2

## L10.05.2 Fundamental simulation scope

**Objective.** Explain fundamental simulation scope and show it in the EX-077 output.

**Prerequisites.** L10.05.1

**Lesson.** Fundamental simulation models physical supply and demand. [K]

**Example.** EX-077 (Build a Natural Gas Price Forecast) on synthetic North American data: test_rows = 99 [EX]

**Do.** `python3 emi.py run 077 | grep '^test_rows:'`

**Expect.** `test_rows: 99`

**On the job.** Use historical prices and explanatory variables to develop a baseline forecasting model.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.05.1 | After: L10.05.3

## L10.05.3 Hybrid approaches

**Objective.** Explain hybrid approaches and show it in the EX-077 output.

**Prerequisites.** L10.05.2

**Lesson.** Hybrids use fundamentals for structure and statistics for residuals. [K]

**Example.** EX-077 (Build a Natural Gas Price Forecast) on synthetic North American data: intercept = 0.270758 [EX]

**Do.** `python3 emi.py run 077 | grep '^intercept:'`

**Expect.** `intercept: 0.270758`

**On the job.** Use historical prices and explanatory variables to develop a baseline forecasting model.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.05.2 | After: L10.05.4

## L10.05.4 Use-case fit

**Objective.** Explain use-case fit and show it in the EX-077 output.

**Prerequisites.** L10.05.3

**Lesson.** Pick by horizon, data and the decision supported. [K]

**Example.** EX-077 (Build a Natural Gas Price Forecast) on synthetic North American data: coef_lag_price = 0.889493 [EX]

**Do.** `python3 emi.py run 077 | grep '^coef_lag_price:'`

**Expect.** `coef_lag_price: 0.889493`

**On the job.** Use historical prices and explanatory variables to develop a baseline forecasting model.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.05.3 | After: L10.05.5

## L10.05.5 Method comparison

**Objective.** Explain method comparison and show it in the EX-077 output.

**Prerequisites.** L10.05.4

**Lesson.** Compare methods on the same test window. [K]

**Example.** EX-077 (Build a Natural Gas Price Forecast) on synthetic North American data: coef_hdd = 0.004145 [EX]

**Do.** `python3 emi.py run 077 | grep '^coef_hdd:'`

**Expect.** `coef_hdd: 0.004145`

**On the job.** Use historical prices and explanatory variables to develop a baseline forecasting model.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.05.4 | After: L10.06.1
