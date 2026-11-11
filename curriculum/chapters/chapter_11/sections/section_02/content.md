# 11.2 Trader, scheduler, analyst, and risk-manager workflows

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-095 Conduct Energy Market Customer Discovery (`python3 emi.py run 095`). Full output: `exercises/completed/ex095/report.md`.

## L11.02.1 Trader workflow

**Objective.** Explain trader workflow and show it in the EX-095 output.

**Prerequisites.** L11.01.5

**Lesson.** A trader's day runs from the morning market view to end-of-day P&L. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_1 = Automated_basis_monitoring score=25000.0 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_1:'`

**Expect.** `rank_1: Automated_basis_monitoring score=25000.0`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.01.5 | After: L11.02.2

## L11.02.2 Scheduler workflow

**Objective.** Explain scheduler workflow and show it in the EX-095 output.

**Prerequisites.** L11.02.1

**Lesson.** A scheduler nominates, confirms and reconciles. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_2 = Unified_risk_dashboard score=24375.0 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_2:'`

**Expect.** `rank_2: Unified_risk_dashboard score=24375.0`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.02.1 | After: L11.02.3

## L11.02.3 Analyst workflow

**Objective.** Explain analyst workflow and show it in the EX-095 output.

**Prerequisites.** L11.02.2

**Lesson.** An analyst gathers data, models and writes up. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_3 = Automated_nomination_reconciliation score=12000.0 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_3:'`

**Expect.** `rank_3: Automated_nomination_reconciliation score=12000.0`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.02.2 | After: L11.02.4

## L11.02.4 Risk-manager workflow

**Objective.** Explain risk-manager workflow and show it in the EX-095 output.

**Prerequisites.** L11.02.3

**Lesson.** A risk manager checks limits, VaR and stress. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_4 = Integrated_dispatch_simulation score=6666.7 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_4:'`

**Expect.** `rank_4: Integrated_dispatch_simulation score=6666.7`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.02.3 | After: L11.02.5

## L11.02.5 Workflow mapping to product surface

**Objective.** Explain workflow mapping to product surface and show it in the EX-095 output.

**Prerequisites.** L11.02.4

**Lesson.** Map each workflow step to a product screen or API. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_5 = Simulation_performance_optimization score=5000.0 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_5:'`

**Expect.** `rank_5: Simulation_performance_optimization score=5000.0`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.02.4 | After: L11.03.1
