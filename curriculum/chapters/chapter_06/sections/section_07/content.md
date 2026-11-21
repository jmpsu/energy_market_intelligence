# 6.7 Energy, congestion, and marginal losses

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-048 Calculate Locational Marginal Prices (`python3 emi.py run 048`). Full output: `exercises/completed/ex048/report.md`.

## L06.07.1 Energy component

**Objective.** Explain energy component and show it in the EX-048 output.

**Prerequisites.** L06.06.5

**Lesson.** The energy component is the system-wide marginal cost at the reference bus. [K]

**Example.** EX-048 (Calculate Locational Marginal Prices) on synthetic North American data: constrained_gen_A_MW = 350 [EX]

**Do.** `python3 emi.py run 048 | grep '^constrained_gen_A_MW:'`

**Expect.** `constrained_gen_A_MW: 350`

**On the job.** Break down electricity prices into energy, congestion, and marginal loss components.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

**Supply-Side Economics.**
The energy component of LMPs reflects supply-side factors like generation costs, fuel prices, and the marginal cost of producing electricity at the reference bus. This component shows how supply conditions affect pricing across the system. In competitive markets, the price should reflect the marginal cost of the last unit needed to meet demand.

**Market example:** When natural gas prices rise, the energy component increases across all nodes in the system because generators face higher marginal costs. This effect is visible when comparing LMPs during different periods of fuel cost volatility.

**Illustrative relationship:** ![Supply-Side Economics: Energy Component](../../../diagrams/diagram_19_m_S_renewables.svg)

Before: L06.06.5 | After: L06.07.2

## L06.07.2 Congestion component

**Objective.** Explain congestion component and show it in the EX-048 output.

**Prerequisites.** L06.07.1

**Lesson.** The congestion component is the cost of binding transmission limits at that node. [K]

**Example.** EX-048 (Calculate Locational Marginal Prices) on synthetic North American data: constrained_gen_B_MW = 150 [EX]

**Do.** `python3 emi.py run 048 | grep '^constrained_gen_B_MW:'`

**Expect.** `constrained_gen_B_MW: 150`

**On the job.** Break down electricity prices into energy, congestion, and marginal loss components.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.07.1 | After: L06.07.3

## L06.07.3 Marginal loss component

**Objective.** Explain marginal loss component and show it in the EX-048 output.

**Prerequisites.** L06.07.2

**Lesson.** The loss component reflects marginal transmission losses. [K]

**Example.** EX-048 (Calculate Locational Marginal Prices) on synthetic North American data: constrained_flow_A_to_B_MW = 250 [EX]

**Do.** `python3 emi.py run 048 | grep '^constrained_flow_A_to_B_MW:'`

**Expect.** `constrained_flow_A_to_B_MW: 250`

**On the job.** Break down electricity prices into energy, congestion, and marginal loss components.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.07.2 | After: L06.07.4

## L06.07.4 Shadow prices of constraints

**Objective.** Explain shadow prices of constraints and show it in the EX-048 output.

**Prerequisites.** L06.07.3

**Lesson.** Each binding constraint has a shadow price: the saving from one more MW of limit. [K]

**Example.** EX-048 (Calculate Locational Marginal Prices) on synthetic North American data: constrained_lmp_A = 30 [EX]

**Do.** `python3 emi.py run 048 | grep '^constrained_lmp_A:'`

**Expect.** `constrained_lmp_A: 30`

**On the job.** Break down electricity prices into energy, congestion, and marginal loss components.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.07.3 | After: L06.07.5

## L06.07.5 Decomposing an LMP

**Objective.** Explain decomposing an LMP and show it in the EX-048 output.

**Prerequisites.** L06.07.4

**Lesson.** LMP equals energy plus congestion plus losses. [K]

**Example.** EX-048 (Calculate Locational Marginal Prices) on synthetic North American data: constrained_lmp_B = 60 [EX]

**Do.** `python3 emi.py run 048 | grep '^constrained_lmp_B:'`

**Expect.** `constrained_lmp_B: 60`

**On the job.** Break down electricity prices into energy, congestion, and marginal loss components.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.07.4 | After: L06.08.1
