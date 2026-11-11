# 11.7 Product backlog and technical requirements

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-096 Design a Market Intelligence Product (`python3 emi.py run 096`). Full output: `exercises/completed/ex096/report.md`.

## L11.07.1 Epics and user stories

**Objective.** Explain epics and user stories and show it in the EX-096 output.

**Prerequisites.** L11.06.5

**Lesson.** Epics are large goals; user stories are small deliverable slices. [K]

**Example.** EX-096 (Design a Market Intelligence Product) on synthetic North American data: requirements = 8 [EX]

**Do.** `python3 emi.py run 096 | grep '^requirements:'`

**Expect.** `requirements: 8`

**On the job.** Create a product specification for an integrated gas and power analytics platform, including users, workflows, data requirements, and acceptance criteria.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.06.5 | After: L11.07.2

## L11.07.2 Acceptance criteria

**Objective.** Explain acceptance criteria and show it in the EX-096 output.

**Prerequisites.** L11.07.1

**Lesson.** Acceptance criteria define done. [K]

**Example.** EX-096 (Design a Market Intelligence Product) on synthetic North American data: distinct_users = 8 [EX]

**Do.** `python3 emi.py run 096 | grep '^distinct_users:'`

**Expect.** `distinct_users: 8`

**On the job.** Create a product specification for an integrated gas and power analytics platform, including users, workflows, data requirements, and acceptance criteria.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.07.1 | After: L11.07.3

## L11.07.3 Non-functional requirements

**Objective.** Explain non-functional requirements and show it in the EX-096 output.

**Prerequisites.** L11.07.2

**Lesson.** Non-functional requirements cover performance, security and reliability. [K]

**Example.** EX-096 (Design a Market Intelligence Product) on synthetic North American data: requirements_with_working_exercise = 8 [EX]

**Do.** `python3 emi.py run 096 | grep '^requirements_with_working_exercise:'`

**Expect.** `requirements_with_working_exercise: 8`

**On the job.** Create a product specification for an integrated gas and power analytics platform, including users, workflows, data requirements, and acceptance criteria.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.07.2 | After: L11.07.4

## L11.07.4 Technical debt management

**Objective.** Explain technical debt management and show it in the EX-096 output.

**Prerequisites.** L11.07.3

**Lesson.** Technical debt is rework owed; plan it. [K]

**Example.** EX-096 (Design a Market Intelligence Product) on synthetic North American data: requirements_with_automated_test = 8 [EX]

**Do.** `python3 emi.py run 096 | grep '^requirements_with_automated_test:'`

**Expect.** `requirements_with_automated_test: 8`

**On the job.** Create a product specification for an integrated gas and power analytics platform, including users, workflows, data requirements, and acceptance criteria.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.07.3 | After: L11.07.5

## L11.07.5 Backlog grooming

**Objective.** Explain backlog grooming and show it in the EX-096 output.

**Prerequisites.** L11.07.4

**Lesson.** Grooming keeps the backlog ordered and ready. [K]

**Example.** EX-096 (Design a Market Intelligence Product) on synthetic North American data: untested_requirements = none [EX]

**Do.** `python3 emi.py run 096 | grep '^untested_requirements:'`

**Expect.** `untested_requirements: none`

**On the job.** Create a product specification for an integrated gas and power analytics platform, including users, workflows, data requirements, and acceptance criteria.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.07.4 | After: L11.08.1
