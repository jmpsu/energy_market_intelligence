# 11.1 Energy software customer segments

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-095 Conduct Energy Market Customer Discovery (`python3 emi.py run 095`). Full output: `exercises/completed/ex095/report.md`.

## L11.01.1 Segment taxonomy

**Objective.** Explain segment taxonomy and show it in the EX-095 output.

**Prerequisites.** L10.10.5

**Lesson.** Customers segment by what they do: utilities, IPPs, traders, developers, investors, consultants. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_1 = Automated_basis_monitoring score=25000.0 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_1:'`

**Expect.** `rank_1: Automated_basis_monitoring score=25000.0`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L10.10.5 | After: L11.01.2

## L11.01.2 Utility and IPP needs

**Objective.** Explain utility and IPP needs and show it in the EX-095 output.

**Prerequisites.** L11.01.1

**Lesson.** Utilities and IPPs need planning and dispatch tools. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_2 = Unified_risk_dashboard score=24375.0 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_2:'`

**Expect.** `rank_2: Unified_risk_dashboard score=24375.0`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.01.1 | After: L11.01.3

## L11.01.3 Trading shop needs

**Objective.** Explain trading shop needs and show it in the EX-095 output.

**Prerequisites.** L11.01.2

**Lesson.** Trading shops need speed, data and risk. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_3 = Automated_nomination_reconciliation score=12000.0 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_3:'`

**Expect.** `rank_3: Automated_nomination_reconciliation score=12000.0`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.01.2 | After: L11.01.4

## L11.01.4 Developer, investor and consultant needs

**Objective.** Explain developer, investor and consultant needs and show it in the EX-095 output.

**Prerequisites.** L11.01.3

**Lesson.** Developers, investors and consultants need valuation and scenarios. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_4 = Integrated_dispatch_simulation score=6666.7 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_4:'`

**Expect.** `rank_4: Integrated_dispatch_simulation score=6666.7`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.01.3 | After: L11.01.5

## L11.01.5 Segment sizing

**Objective.** Explain segment sizing and show it in the EX-095 output.

**Prerequisites.** L11.01.4

**Lesson.** Size a segment by number of firms times willingness to pay. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_5 = Simulation_performance_optimization score=5000.0 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_5:'`

**Expect.** `rank_5: Simulation_performance_optimization score=5000.0`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.01.4 | After: L11.02.1
