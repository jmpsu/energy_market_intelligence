# 12.8 Integrated data and simulation architecture

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-099 Design an Energy Exemplar Product Integration (`python3 emi.py run 099`). Full output: `exercises/completed/ex099/report.md`.

## L12.08.1 Data architecture for integrated analytics

**Objective.** Explain data architecture for integrated analytics and show it in the EX-099 output.

**Prerequisites.** L12.07.5

**Lesson.** Integrated analytics needs one model of locations, units and time. [K]

**Example.** EX-099 (Design an Energy Exemplar Product Integration) on synthetic North American data: components = 13 [EX]

**Do.** `python3 emi.py run 099 | grep '^components:'`

**Expect.** `components: 13`

**On the job.** Develop a conceptual architecture connecting market data, simulation engines, analytical services, user workflows, and reporting. Distinguish verified product capabilities from proposed capabilities.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.07.5 | After: L12.08.2

## L12.08.2 Simulation orchestration

**Objective.** Explain simulation orchestration and show it in the EX-099 output.

**Prerequisites.** L12.08.1

**Lesson.** Orchestration runs simulations in order. [K]

**Example.** EX-099 (Design an Energy Exemplar Product Integration) on synthetic North American data: interfaces = 14 [EX]

**Do.** `python3 emi.py run 099 | grep '^interfaces:'`

**Expect.** `interfaces: 14`

**On the job.** Develop a conceptual architecture connecting market data, simulation engines, analytical services, user workflows, and reporting. Distinguish verified product capabilities from proposed capabilities.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.08.1 | After: L12.08.3

## L12.08.3 Integration interfaces

**Objective.** Explain integration interfaces and show it in the EX-099 output.

**Prerequisites.** L12.08.2

**Lesson.** Interfaces link models, ETRM and reporting. [K]

**Example.** EX-099 (Design an Energy Exemplar Product Integration) on synthetic North American data: demonstrated_components = 9 [EX]

**Do.** `python3 emi.py run 099 | grep '^demonstrated_components:'`

**Expect.** `demonstrated_components: 9`

**On the job.** Develop a conceptual architecture connecting market data, simulation engines, analytical services, user workflows, and reporting. Distinguish verified product capabilities from proposed capabilities.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.08.2 | After: L12.08.4

## L12.08.4 Governance and lineage

**Objective.** Explain governance and lineage and show it in the EX-099 output.

**Prerequisites.** L12.08.3

**Lesson.** Governance and lineage make results auditable. [K]

**Example.** EX-099 (Design an Energy Exemplar Product Integration) on synthetic North American data: proposed_components = 4 [EX]

**Do.** `python3 emi.py run 099 | grep '^proposed_components:'`

**Expect.** `proposed_components: 4`

**On the job.** Develop a conceptual architecture connecting market data, simulation engines, analytical services, user workflows, and reporting. Distinguish verified product capabilities from proposed capabilities.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.08.3 | After: L12.08.5

## L12.08.5 Architecture document

**Objective.** Explain architecture document and show it in the EX-099 output.

**Prerequisites.** L12.08.4

**Lesson.** The architecture document records components and flows. [K]

**Example.** EX-099 (Design an Energy Exemplar Product Integration) on synthetic North American data: demonstrated_interfaces = 7 [EX]

**Do.** `python3 emi.py run 099 | grep '^demonstrated_interfaces:'`

**Expect.** `demonstrated_interfaces: 7`

**On the job.** Develop a conceptual architecture connecting market data, simulation engines, analytical services, user workflows, and reporting. Distinguish verified product capabilities from proposed capabilities.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.08.4 | After: L12.09.1
