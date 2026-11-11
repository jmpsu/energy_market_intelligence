# 4.7 Mexican natural gas imports and exports

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-035 Model US-Canada-Mexico Gas Flows (`python3 emi.py run 035`). Full output: `exercises/completed/ex035/report.md`.

## L04.07.1 US pipeline exports to Mexico

**Objective.** Explain uS pipeline exports to Mexico and show it in the EX-035 output.

**Prerequisites.** L04.06.5

**Lesson.** US pipeline exports to Mexico are a major, steady demand source. [K]

**Example.** EX-035 (Model US-Canada-Mexico Gas Flows) on synthetic North American data: United_States_residual_Bcf_d = 8 [EX]

**Do.** `python3 emi.py run 035 | grep '^United_States_residual_Bcf_d:'`

**Expect.** `United_States_residual_Bcf_d: 8`

**On the job.** Build a cross-border supply and demand balance incorporating imports, exports, and pipeline constraints.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.06.5 | After: L04.07.2

## L04.07.2 Mexican demand and infrastructure

**Objective.** Explain mexican demand and infrastructure and show it in the EX-035 output.

**Prerequisites.** L04.07.1

**Lesson.** Mexican demand is driven by gas-fired power and industry and depends on in-country pipelines. [K]

**Example.** EX-035 (Model US-Canada-Mexico Gas Flows) on synthetic North American data: Canada_residual_Bcf_d = 1.2 [EX]

**Do.** `python3 emi.py run 035 | grep '^Canada_residual_Bcf_d:'`

**Expect.** `Canada_residual_Bcf_d: 1.2`

**On the job.** Build a cross-border supply and demand balance incorporating imports, exports, and pipeline constraints.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.07.1 | After: L04.07.3

## L04.07.3 Waha-Mexico linkage

**Objective.** Explain waha-Mexico linkage and show it in the EX-035 output.

**Prerequisites.** L04.07.2

**Lesson.** Much of the export gas comes from the Permian, so Mexican takeaway affects Waha prices. [K]

**Example.** EX-035 (Model US-Canada-Mexico Gas Flows) on synthetic North American data: Mexico_residual_Bcf_d = 0.5 [EX]

**Do.** `python3 emi.py run 035 | grep '^Mexico_residual_Bcf_d:'`

**Expect.** `Mexico_residual_Bcf_d: 0.5`

**On the job.** Build a cross-border supply and demand balance incorporating imports, exports, and pipeline constraints.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.07.2 | After: L04.07.4

## L04.07.4 Cross-border balance reconciliation

**Objective.** Explain cross-border balance reconciliation and show it in the EX-035 output.

**Prerequisites.** L04.07.3

**Lesson.** Border flow data from each side must be reconciled before use. [K]

**Example.** EX-035 (Model US-Canada-Mexico Gas Flows) on synthetic North American data: United_States_import_break_Bcf_d = 4.5 [EX]

**Do.** `python3 emi.py run 035 | grep '^United_States_import_break_Bcf_d:'`

**Expect.** `United_States_import_break_Bcf_d: 4.5`

**On the job.** Build a cross-border supply and demand balance incorporating imports, exports, and pipeline constraints.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.07.3 | After: L04.07.5

## L04.07.5 Regulatory and operational risks

**Objective.** Explain regulatory and operational risks and show it in the EX-035 output.

**Prerequisites.** L04.07.4

**Lesson.** Cross-border flows carry regulatory, payment and infrastructure-delay risks. [K]

**Example.** EX-035 (Model US-Canada-Mexico Gas Flows) on synthetic North American data: Canada_import_break_Bcf_d = -3 [EX]

**Do.** `python3 emi.py run 035 | grep '^Canada_import_break_Bcf_d:'`

**Expect.** `Canada_import_break_Bcf_d: -3`

**On the job.** Build a cross-border supply and demand balance incorporating imports, exports, and pipeline constraints.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.07.4 | After: L04.08.1
