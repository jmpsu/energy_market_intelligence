# 7.6 Renewable generation and forecasting

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-062 Model Renewable Generation Forecast Errors (`python3 emi.py run 062`). Full output: `exercises/completed/ex062/report.md`.

## L07.06.1 Wind and solar forecast methods

**Objective.** Explain wind and solar forecast methods and show it in the EX-062 output.

**Prerequisites.** L07.05.5

**Lesson.** Wind and solar forecasts combine weather models with plant data. [K]

**Example.** EX-062 (Model Renewable Generation Forecast Errors) on synthetic North American data: mae_MW = 8.416667 [EX]

**Do.** `python3 emi.py run 062 | grep '^mae_MW:'`

**Expect.** `mae_MW: 8.416667`

**On the job.** Compare forecast and actual wind or solar production; calculate the resulting financial exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.05.5 | After: L07.06.2

## L07.06.2 Forecast error metrics

**Objective.** Explain forecast error metrics and show it in the EX-062 output.

**Prerequisites.** L07.06.1

**Lesson.** Error is measured with MAE, RMSE and bias. [K]

**Example.** EX-062 (Model Renewable Generation Forecast Errors) on synthetic North American data: bias_MW = -2 [EX]

**Do.** `python3 emi.py run 062 | grep '^bias_MW:'`

**Expect.** `bias_MW: -2`

**On the job.** Compare forecast and actual wind or solar production; calculate the resulting financial exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.06.1 | After: L07.06.3

## L07.06.3 Financial exposure from forecast error

**Objective.** Explain financial exposure from forecast error and show it in the EX-062 output.

**Prerequisites.** L07.06.2

**Lesson.** A forecast miss is bought or sold at the real-time price. [K]

**Example.** EX-062 (Model Renewable Generation Forecast Errors) on synthetic North American data: mape_pct = 35.290738 [EX]

**Do.** `python3 emi.py run 062 | grep '^mape_pct:'`

**Expect.** `mape_pct: 35.290738`

**On the job.** Compare forecast and actual wind or solar production; calculate the resulting financial exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.06.2 | After: L07.06.4

## L07.06.4 Net load

**Objective.** Explain net load and show it in the EX-062 output.

**Prerequisites.** L07.06.3

**Lesson.** Net load is demand minus wind and solar. [K]

**Example.** EX-062 (Model Renewable Generation Forecast Errors) on synthetic North American data: rmse_MW = 10.161201 [EX]

**Do.** `python3 emi.py run 062 | grep '^rmse_MW:'`

**Expect.** `rmse_MW: 10.161201`

**On the job.** Compare forecast and actual wind or solar production; calculate the resulting financial exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.06.3 | After: L07.06.5

## L07.06.5 Forecast evaluation

**Objective.** Explain forecast evaluation and show it in the EX-062 output.

**Prerequisites.** L07.06.4

**Lesson.** Evaluate forecasts against a naive benchmark. [K]

**Example.** EX-062 (Model Renewable Generation Forecast Errors) on synthetic North American data: da_revenue_USD = 73150 [EX]

**Do.** `python3 emi.py run 062 | grep '^da_revenue_USD:'`

**Expect.** `da_revenue_USD: 73150`

**On the job.** Compare forecast and actual wind or solar production; calculate the resulting financial exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.06.4 | After: L07.07.1
