# 11.9 Data quality, lineage, governance, and product reliability

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-099 Design an Energy Exemplar Product Integration (`python3 emi.py run 099`). Full output: `exercises/completed/ex099/report.md`.

## L11.09.1 Data quality dimensions

**Objective.** Explain data quality dimensions and show it in the EX-099 output.

**Prerequisites.** L11.08.5

**Lesson.** Data quality has dimensions: accuracy, completeness, timeliness, consistency. [K]

**Example.** EX-099 (Design an Energy Exemplar Product Integration) on synthetic North American data: components = 13 [EX]

**Do.** `python3 emi.py run 099 | grep '^components:'`

**Expect.** `components: 13`

**On the job.** Develop a conceptual architecture connecting market data, simulation engines, analytical services, user workflows, and reporting. Distinguish verified product capabilities from proposed capabilities.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.08.5 | After: L11.09.2

## L11.09.2 Lineage

**Objective.** Explain lineage and show it in the EX-099 output.

**Prerequisites.** L11.09.1

**Lesson.** Lineage traces each number to its source. [K]

**Example.** EX-099 (Design an Energy Exemplar Product Integration) on synthetic North American data: interfaces = 14 [EX]

**Do.** `python3 emi.py run 099 | grep '^interfaces:'`

**Expect.** `interfaces: 14`

**On the job.** Develop a conceptual architecture connecting market data, simulation engines, analytical services, user workflows, and reporting. Distinguish verified product capabilities from proposed capabilities.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.09.1 | After: L11.09.3

## L11.09.3 Governance model

**Objective.** Explain governance model and show it in the EX-099 output.

**Prerequisites.** L11.09.2

**Lesson.** Governance assigns owners and rules. [K]

**Example.** EX-099 (Design an Energy Exemplar Product Integration) on synthetic North American data: demonstrated_components = 9 [EX]

**Do.** `python3 emi.py run 099 | grep '^demonstrated_components:'`

**Expect.** `demonstrated_components: 9`

**On the job.** Develop a conceptual architecture connecting market data, simulation engines, analytical services, user workflows, and reporting. Distinguish verified product capabilities from proposed capabilities.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.09.2 | After: L11.09.4

## L11.09.4 SLAs and reliability

**Objective.** Explain sLAs and reliability and show it in the EX-099 output.

**Prerequisites.** L11.09.3

**Lesson.** SLAs promise availability and timeliness. [K]

**Example.** EX-099 (Design an Energy Exemplar Product Integration) on synthetic North American data: proposed_components = 4 [EX]

**Do.** `python3 emi.py run 099 | grep '^proposed_components:'`

**Expect.** `proposed_components: 4`

**On the job.** Develop a conceptual architecture connecting market data, simulation engines, analytical services, user workflows, and reporting. Distinguish verified product capabilities from proposed capabilities.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.09.3 | After: L11.09.5

## L11.09.5 Incident management

**Objective.** Explain incident management and show it in the EX-099 output.

**Prerequisites.** L11.09.4

**Lesson.** Incident management detects, fixes and explains failures. [K]

**Example.** EX-099 (Design an Energy Exemplar Product Integration) on synthetic North American data: demonstrated_interfaces = 7 [EX]

**Do.** `python3 emi.py run 099 | grep '^demonstrated_interfaces:'`

**Expect.** `demonstrated_interfaces: 7`

**On the job.** Develop a conceptual architecture connecting market data, simulation engines, analytical services, user workflows, and reporting. Distinguish verified product capabilities from proposed capabilities.

**Product implication.** Every roadmap item should cite customer evidence and a measurable KPI.

Before: L11.09.4 | After: L11.10.1
