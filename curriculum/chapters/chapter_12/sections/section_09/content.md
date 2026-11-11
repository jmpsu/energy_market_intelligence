# 12.9 Product roadmap and commercial opportunity

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-098 Build Product Performance Metrics (`python3 emi.py run 098`). Full output: `exercises/completed/ex098/report.md`.

## L12.09.1 Opportunity sizing

**Objective.** Explain opportunity sizing and show it in the EX-098 output.

**Prerequisites.** L12.08.5

**Lesson.** Opportunity sizing estimates value before building. [K]

**Example.** EX-098 (Build Product Performance Metrics) on synthetic North American data: adoption_wau_pct_of_licensed = 46 [EX]

**Do.** `python3 emi.py run 098 | grep '^adoption_wau_pct_of_licensed:'`

**Expect.** `adoption_wau_pct_of_licensed: 46`

**On the job.** Define KPIs for model accuracy, execution runtime, data quality, user adoption, customer retention, and commercial value.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.08.5 | After: L12.09.2

## L12.09.2 Roadmap construction

**Objective.** Explain roadmap construction and show it in the EX-098 output.

**Prerequisites.** L12.09.1

**Lesson.** A roadmap sequences the work. [K]

**Example.** EX-098 (Build Product Performance Metrics) on synthetic North American data: week8_retention_of_week1_users_pct = 47.826087 [EX]

**Do.** `python3 emi.py run 098 | grep '^week8_retention_of_week1_users_pct:'`

**Expect.** `week8_retention_of_week1_users_pct: 47.826087`

**On the job.** Define KPIs for model accuracy, execution runtime, data quality, user adoption, customer retention, and commercial value.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.09.1 | After: L12.09.3

## L12.09.3 KPI definition

**Objective.** Explain kPI definition and show it in the EX-098 output.

**Prerequisites.** L12.09.2

**Lesson.** KPIs define success. [K]

**Example.** EX-098 (Build Product Performance Metrics) on synthetic North American data: data_completeness_pct = 85.714286 [EX]

**Do.** `python3 emi.py run 098 | grep '^data_completeness_pct:'`

**Expect.** `data_completeness_pct: 85.714286`

**On the job.** Define KPIs for model accuracy, execution runtime, data quality, user adoption, customer retention, and commercial value.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.09.2 | After: L12.09.4

## L12.09.4 Business case

**Objective.** Explain business case and show it in the EX-098 output.

**Prerequisites.** L12.09.3

**Lesson.** A business case compares benefit to cost. [K]

**Example.** EX-098 (Build Product Performance Metrics) on synthetic North American data: model_backcast_mae_USD_per_MWh = 1.549857 [EX]

**Do.** `python3 emi.py run 098 | grep '^model_backcast_mae_USD_per_MWh:'`

**Expect.** `model_backcast_mae_USD_per_MWh: 1.549857`

**On the job.** Define KPIs for model accuracy, execution runtime, data quality, user adoption, customer retention, and commercial value.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.09.3 | After: L12.09.5

## L12.09.5 Roadmap review

**Objective.** Explain roadmap review and show it in the EX-098 output.

**Prerequisites.** L12.09.4

**Lesson.** Review tests the roadmap against evidence. [K]

**Example.** EX-098 (Build Product Performance Metrics) on synthetic North American data: net_revenue_retention_pct = 90.4 [EX]

**Do.** `python3 emi.py run 098 | grep '^net_revenue_retention_pct:'`

**Expect.** `net_revenue_retention_pct: 90.4`

**On the job.** Define KPIs for model accuracy, execution runtime, data quality, user adoption, customer retention, and commercial value.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.09.4 | After: L12.10.1
