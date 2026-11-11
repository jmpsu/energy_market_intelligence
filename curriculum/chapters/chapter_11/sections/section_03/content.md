# 11.3 Customer discovery and requirements gathering

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-095 Conduct Energy Market Customer Discovery (`python3 emi.py run 095`). Full output: `exercises/completed/ex095/report.md`.

## L11.03.1 Interview technique

**Objective.** Explain interview technique and show it in the EX-095 output.

**Prerequisites.** L11.02.5

**Lesson.** Interviews ask about past behaviour, not hypotheticals. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_1 = Automated_basis_monitoring score=25000.0 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_1:'`

**Expect.** `rank_1: Automated_basis_monitoring score=25000.0`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.02.5 | After: L11.03.2

## L11.03.2 Jobs-to-be-done framing

**Objective.** Explain jobs-to-be-done framing and show it in the EX-095 output.

**Prerequisites.** L11.03.1

**Lesson.** Jobs-to-be-done frames what the customer is trying to accomplish. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_2 = Unified_risk_dashboard score=24375.0 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_2:'`

**Expect.** `rank_2: Unified_risk_dashboard score=24375.0`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.03.1 | After: L11.03.3

## L11.03.3 Evidence synthesis

**Objective.** Explain evidence synthesis and show it in the EX-095 output.

**Prerequisites.** L11.03.2

**Lesson.** Synthesis groups evidence into themes. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_3 = Automated_nomination_reconciliation score=12000.0 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_3:'`

**Expect.** `rank_3: Automated_nomination_reconciliation score=12000.0`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.03.2 | After: L11.03.4

## L11.03.4 Requirement writing

**Objective.** Explain requirement writing and show it in the EX-095 output.

**Prerequisites.** L11.03.3

**Lesson.** A requirement states user, need and acceptance test. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_4 = Integrated_dispatch_simulation score=6666.7 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_4:'`

**Expect.** `rank_4: Integrated_dispatch_simulation score=6666.7`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.03.3 | After: L11.03.5

## L11.03.5 Validation with customers

**Objective.** Explain validation with customers and show it in the EX-095 output.

**Prerequisites.** L11.03.4

**Lesson.** Validate with the customers who raised the need. [K]

**Example.** EX-095 (Conduct Energy Market Customer Discovery) on synthetic North American data: rank_5 = Simulation_performance_optimization score=5000.0 [EX]

**Do.** `python3 emi.py run 095 | grep '^rank_5:'`

**Expect.** `rank_5: Simulation_performance_optimization score=5000.0`

**On the job.** Translate trader, analyst, scheduler, and portfolio manager workflows into documented product requirements.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.03.4 | After: L11.04.1
