# 11.6 Roadmap design and prioritization

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-097 Prioritize a Product Roadmap (`python3 emi.py run 097`). Full output: `exercises/completed/ex097/report.md`.

## L11.06.1 Prioritization frameworks

**Objective.** Explain prioritization frameworks and show it in the EX-097 output.

**Prerequisites.** L11.05.5

**Lesson.** Prioritisation frameworks score value against effort. [K]

**Example.** EX-097 (Prioritize a Product Roadmap) on synthetic North American data: rank_1 = Basis_monitor [EX]

**Do.** `python3 emi.py run 097 | grep '^rank_1:'`

**Expect.** `rank_1: Basis_monitor`

**On the job.** Rank competing feature requests using customer value, commercial impact, technical feasibility, risk, and development effort.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.05.5 | After: L11.06.2

## L11.06.2 Roadmap formats

**Objective.** Explain roadmap formats and show it in the EX-097 output.

**Prerequisites.** L11.06.1

**Lesson.** Roadmaps show themes over time. [K]

**Example.** EX-097 (Prioritize a Product Roadmap) on synthetic North American data: rank_2 = NGL_netback_screen [EX]

**Do.** `python3 emi.py run 097 | grep '^rank_2:'`

**Expect.** `rank_2: NGL_netback_screen`

**On the job.** Rank competing feature requests using customer value, commercial impact, technical feasibility, risk, and development effort.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.06.1 | After: L11.06.3

## L11.06.3 Dependencies and sequencing

**Objective.** Explain dependencies and sequencing and show it in the EX-097 output.

**Prerequisites.** L11.06.2

**Lesson.** Dependencies set order. [K]

**Example.** EX-097 (Prioritize a Product Roadmap) on synthetic North American data: rank_3 = Data_quality_console [EX]

**Do.** `python3 emi.py run 097 | grep '^rank_3:'`

**Expect.** `rank_3: Data_quality_console`

**On the job.** Rank competing feature requests using customer value, commercial impact, technical feasibility, risk, and development effort.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.06.2 | After: L11.06.4

## L11.06.4 Capacity planning

**Objective.** Explain capacity planning and show it in the EX-097 output.

**Prerequisites.** L11.06.3

**Lesson.** Capacity limits what fits. [K]

**Example.** EX-097 (Prioritize a Product Roadmap) on synthetic North American data: rank_4 = Unified_risk_dashboard [EX]

**Do.** `python3 emi.py run 097 | grep '^rank_4:'`

**Expect.** `rank_4: Unified_risk_dashboard`

**On the job.** Rank competing feature requests using customer value, commercial impact, technical feasibility, risk, and development effort.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.06.3 | After: L11.06.5

## L11.06.5 Stakeholder alignment

**Objective.** Explain stakeholder alignment and show it in the EX-097 output.

**Prerequisites.** L11.06.4

**Lesson.** Alignment is agreement from the teams that deliver and sell. [K]

**Example.** EX-097 (Prioritize a Product Roadmap) on synthetic North American data: rank_5 = Nomination_reconciliation [EX]

**Do.** `python3 emi.py run 097 | grep '^rank_5:'`

**Expect.** `rank_5: Nomination_reconciliation`

**On the job.** Rank competing feature requests using customer value, commercial impact, technical feasibility, risk, and development effort.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.06.4 | After: L11.07.1
