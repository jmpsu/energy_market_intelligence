# 7.7 Wind and solar curtailment

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-062 Model Renewable Generation Forecast Errors (`python3 emi.py run 062`). Full output: `exercises/completed/ex062/report.md`.

## L07.07.1 Curtailment causes

**Objective.** Explain curtailment causes and show it in the EX-062 output.

**Prerequisites.** L07.06.5

**Lesson.** Curtailment happens when output cannot be delivered or is not wanted. [K]

**Example.** EX-062 (Model Renewable Generation Forecast Errors) on synthetic North American data: mae_MW = 8.416667 [EX]

**Do.** `python3 emi.py run 062 | grep '^mae_MW:'`

**Expect.** `mae_MW: 8.416667`

**On the job.** Compare forecast and actual wind or solar production; calculate the resulting financial exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.06.5 | After: L07.07.2

## L07.07.2 Negative pricing

**Objective.** Explain negative pricing and show it in the EX-062 output.

**Prerequisites.** L07.07.1

**Lesson.** Prices go negative when generators pay to keep running. [K]

**Example.** EX-062 (Model Renewable Generation Forecast Errors) on synthetic North American data: bias_MW = -2 [EX]

**Do.** `python3 emi.py run 062 | grep '^bias_MW:'`

**Expect.** `bias_MW: -2`

**On the job.** Compare forecast and actual wind or solar production; calculate the resulting financial exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.07.1 | After: L07.07.3

## L07.07.3 Economic vs reliability curtailment

**Objective.** Explain economic vs reliability curtailment and show it in the EX-062 output.

**Prerequisites.** L07.07.2

**Lesson.** Economic curtailment follows price; reliability curtailment is an operator order. [K]

**Example.** EX-062 (Model Renewable Generation Forecast Errors) on synthetic North American data: mape_pct = 35.290738 [EX]

**Do.** `python3 emi.py run 062 | grep '^mape_pct:'`

**Expect.** `mape_pct: 35.290738`

**On the job.** Compare forecast and actual wind or solar production; calculate the resulting financial exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.07.2 | After: L07.07.4

## L07.07.4 PPA settlement effects

**Objective.** Explain pPA settlement effects and show it in the EX-062 output.

**Prerequisites.** L07.07.3

**Lesson.** Contract terms decide who bears curtailed energy. [K]

**Example.** EX-062 (Model Renewable Generation Forecast Errors) on synthetic North American data: rmse_MW = 10.161201 [EX]

**Do.** `python3 emi.py run 062 | grep '^rmse_MW:'`

**Expect.** `rmse_MW: 10.161201`

**On the job.** Compare forecast and actual wind or solar production; calculate the resulting financial exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.07.3 | After: L07.07.5

## L07.07.5 Curtailment valuation

**Objective.** Explain curtailment valuation and show it in the EX-062 output.

**Prerequisites.** L07.07.4

**Lesson.** Curtailment value is lost energy times the price plus lost credits. [K]

**Example.** EX-062 (Model Renewable Generation Forecast Errors) on synthetic North American data: da_revenue_USD = 73150 [EX]

**Do.** `python3 emi.py run 062 | grep '^da_revenue_USD:'`

**Expect.** `da_revenue_USD: 73150`

**On the job.** Compare forecast and actual wind or solar production; calculate the resulting financial exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.07.4 | After: L07.08.1
