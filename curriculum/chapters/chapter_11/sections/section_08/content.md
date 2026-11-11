# 11.8 Adoption, retention, revenue, and customer value

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-098 Build Product Performance Metrics (`python3 emi.py run 098`). Full output: `exercises/completed/ex098/report.md`.

## L11.08.1 Adoption metrics

**Objective.** Explain adoption metrics and show it in the EX-098 output.

**Prerequisites.** L11.07.5

**Lesson.** Adoption metrics count active use. [K]

**Example.** EX-098 (Build Product Performance Metrics) on synthetic North American data: adoption_wau_pct_of_licensed = 46 [EX]

**Do.** `python3 emi.py run 098 | grep '^adoption_wau_pct_of_licensed:'`

**Expect.** `adoption_wau_pct_of_licensed: 46`

**On the job.** Define KPIs for model accuracy, execution runtime, data quality, user adoption, customer retention, and commercial value.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.07.5 | After: L11.08.2

## L11.08.2 Retention and churn

**Objective.** Explain retention and churn and show it in the EX-098 output.

**Prerequisites.** L11.08.1

**Lesson.** Retention is customers kept; churn is customers lost. [K]

**Example.** EX-098 (Build Product Performance Metrics) on synthetic North American data: week8_retention_of_week1_users_pct = 47.826087 [EX]

**Do.** `python3 emi.py run 098 | grep '^week8_retention_of_week1_users_pct:'`

**Expect.** `week8_retention_of_week1_users_pct: 47.826087`

**On the job.** Define KPIs for model accuracy, execution runtime, data quality, user adoption, customer retention, and commercial value.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.08.1 | After: L11.08.3

## L11.08.3 Revenue metrics

**Objective.** Explain revenue metrics and show it in the EX-098 output.

**Prerequisites.** L11.08.2

**Lesson.** Revenue metrics include recurring revenue and net revenue retention. [K]

**Example.** EX-098 (Build Product Performance Metrics) on synthetic North American data: data_completeness_pct = 85.714286 [EX]

**Do.** `python3 emi.py run 098 | grep '^data_completeness_pct:'`

**Expect.** `data_completeness_pct: 85.714286`

**On the job.** Define KPIs for model accuracy, execution runtime, data quality, user adoption, customer retention, and commercial value.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.08.2 | After: L11.08.4

## L11.08.4 Customer value measurement

**Objective.** Explain customer value measurement and show it in the EX-098 output.

**Prerequisites.** L11.08.3

**Lesson.** Customer value is the outcome achieved. [K]

**Example.** EX-098 (Build Product Performance Metrics) on synthetic North American data: model_backcast_mae_USD_per_MWh = 1.549857 [EX]

**Do.** `python3 emi.py run 098 | grep '^model_backcast_mae_USD_per_MWh:'`

**Expect.** `model_backcast_mae_USD_per_MWh: 1.549857`

**On the job.** Define KPIs for model accuracy, execution runtime, data quality, user adoption, customer retention, and commercial value.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.08.3 | After: L11.08.5

## L11.08.5 KPI dashboard

**Objective.** Explain kPI dashboard and show it in the EX-098 output.

**Prerequisites.** L11.08.4

**Lesson.** A KPI dashboard shows a few metrics with targets. [K]

**Example.** EX-098 (Build Product Performance Metrics) on synthetic North American data: net_revenue_retention_pct = 90.4 [EX]

**Do.** `python3 emi.py run 098 | grep '^net_revenue_retention_pct:'`

**Expect.** `net_revenue_retention_pct: 90.4`

**On the job.** Define KPIs for model accuracy, execution runtime, data quality, user adoption, customer retention, and commercial value.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.08.4 | After: L11.09.1
