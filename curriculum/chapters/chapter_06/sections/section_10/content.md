# 6.10 Ancillary services and wholesale settlements

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-050 Analyze Ancillary Services (`python3 emi.py run 050`). Full output: `exercises/completed/ex050/report.md`.

## L06.10.1 Regulation service

**Objective.** Explain regulation service and show it in the EX-050 output.

**Prerequisites.** L06.09.5

**Lesson.** Regulation follows second-to-second imbalances. [K]

**Example.** EX-050 (Analyze Ancillary Services) on synthetic North American data: regulation_requirement_MW = 50 [EX]

**Do.** `python3 emi.py run 050 | grep '^regulation_requirement_MW:'`

**Expect.** `regulation_requirement_MW: 50`

**On the job.** Model reserve requirements, regulation, contingency reserves, and their contribution to generator revenue.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.09.5 | After: L06.10.2

## L06.10.2 Operating reserves

**Objective.** Explain operating reserves and show it in the EX-050 output.

**Prerequisites.** L06.10.1

**Lesson.** Operating reserves stand ready to replace a lost unit within minutes. [K]

**Example.** EX-050 (Analyze Ancillary Services) on synthetic North American data: spin_requirement_MW = 150 [EX]

**Do.** `python3 emi.py run 050 | grep '^spin_requirement_MW:'`

**Expect.** `spin_requirement_MW: 150`

**On the job.** Model reserve requirements, regulation, contingency reserves, and their contribution to generator revenue.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.10.1 | After: L06.10.3

## L06.10.3 Co-optimization of energy and reserves

**Objective.** Explain co-optimization of energy and reserves and show it in the EX-050 output.

**Prerequisites.** L06.10.2

**Lesson.** Energy and reserves are cleared together so each unit provides its most valuable mix. [K]

**Example.** EX-050 (Analyze Ancillary Services) on synthetic North American data: energy_margin_USD_per_MWh = 10 [EX]

**Do.** `python3 emi.py run 050 | grep '^energy_margin_USD_per_MWh:'`

**Expect.** `energy_margin_USD_per_MWh: 10`

**On the job.** Model reserve requirements, regulation, contingency reserves, and their contribution to generator revenue.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.10.2 | After: L06.10.4

## L06.10.4 Settlement statements

**Objective.** Explain settlement statements and show it in the EX-050 output.

**Prerequisites.** L06.10.3

**Lesson.** A settlement statement lists every charge and credit by interval. [K]

**Example.** EX-050 (Analyze Ancillary Services) on synthetic North American data: all_energy_USD_per_h = 2000 [EX]

**Do.** `python3 emi.py run 050 | grep '^all_energy_USD_per_h:'`

**Expect.** `all_energy_USD_per_h: 2000`

**On the job.** Model reserve requirements, regulation, contingency reserves, and their contribution to generator revenue.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.10.3 | After: L06.10.5

## L06.10.5 Charge code reconciliation

**Objective.** Explain charge code reconciliation and show it in the EX-050 output.

**Prerequisites.** L06.10.4

**Lesson.** Reconciling charge codes against your own shadow calculation finds billing errors. [K]

**Example.** EX-050 (Analyze Ancillary Services) on synthetic North American data: energy_plus_regulation_USD_per_h = 2040 [EX]

**Do.** `python3 emi.py run 050 | grep '^energy_plus_regulation_USD_per_h:'`

**Expect.** `energy_plus_regulation_USD_per_h: 2040`

**On the job.** Model reserve requirements, regulation, contingency reserves, and their contribution to generator revenue.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.10.4 | After: L07.01.1
