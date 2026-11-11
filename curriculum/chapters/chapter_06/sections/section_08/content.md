# 6.8 Transmission constraints and network topology

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-056 Model Transmission Congestion (`python3 emi.py run 056`). Full output: `exercises/completed/ex056/report.md`.

## L06.08.1 Thermal and stability limits

**Objective.** Explain thermal and stability limits and show it in the EX-056 output.

**Prerequisites.** L06.07.5

**Lesson.** Lines are limited by heating, voltage and stability. [K]

**Example.** EX-056 (Model Transmission Congestion) on synthetic North American data: lmp_bus_1 = 20 [EX]

**Do.** `python3 emi.py run 056 | grep '^lmp_bus_1:'`

**Expect.** `lmp_bus_1: 20`

**On the job.** Simulate a transmission constraint and calculate its effect on nodal electricity prices.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.07.5 | After: L06.08.2

## L06.08.2 Contingency (N-1) constraints

**Objective.** Explain contingency (N-1) constraints and show it in the EX-056 output.

**Prerequisites.** L06.08.1

**Lesson.** Operators keep the system secure against the loss of any single element (N-1). [K]

**Example.** EX-056 (Model Transmission Congestion) on synthetic North American data: lmp_bus_2 = 50 [EX]

**Do.** `python3 emi.py run 056 | grep '^lmp_bus_2:'`

**Expect.** `lmp_bus_2: 50`

**On the job.** Simulate a transmission constraint and calculate its effect on nodal electricity prices.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.08.1 | After: L06.08.3

## L06.08.3 PTDF and shift factors

**Objective.** Explain pTDF and shift factors and show it in the EX-056 output.

**Prerequisites.** L06.08.2

**Lesson.** A shift factor says how much of an injection at a node flows on a given line. [K]

**Example.** EX-056 (Model Transmission Congestion) on synthetic North American data: lmp_bus_3 = 80 [EX]

**Do.** `python3 emi.py run 056 | grep '^lmp_bus_3:'`

**Expect.** `lmp_bus_3: 80`

**On the job.** Simulate a transmission constraint and calculate its effect on nodal electricity prices.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.08.2 | After: L06.08.4

## L06.08.4 Congestion patterns

**Objective.** Explain congestion patterns and show it in the EX-056 output.

**Prerequisites.** L06.08.3

**Lesson.** The same constraints bind repeatedly, creating predictable congestion patterns. [K]

**Example.** EX-056 (Model Transmission Congestion) on synthetic North American data: gen_bus_1_MW = 150 [EX]

**Do.** `python3 emi.py run 056 | grep '^gen_bus_1_MW:'`

**Expect.** `gen_bus_1_MW: 150`

**On the job.** Simulate a transmission constraint and calculate its effect on nodal electricity prices.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.08.3 | After: L06.08.5

## L06.08.5 Constraint impact analysis

**Objective.** Explain constraint impact analysis and show it in the EX-056 output.

**Prerequisites.** L06.08.4

**Lesson.** Constraint analysis shows who gains and who pays when a limit binds. [K]

**Example.** EX-056 (Model Transmission Congestion) on synthetic North American data: gen_bus_2_MW = 150 [EX]

**Do.** `python3 emi.py run 056 | grep '^gen_bus_2_MW:'`

**Expect.** `gen_bus_2_MW: 150`

**On the job.** Simulate a transmission constraint and calculate its effect on nodal electricity prices.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.08.4 | After: L06.09.1
