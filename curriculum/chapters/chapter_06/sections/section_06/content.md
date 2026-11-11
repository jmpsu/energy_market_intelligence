# 6.6 Locational marginal pricing

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-048 Calculate Locational Marginal Prices (`python3 emi.py run 048`). Full output: `exercises/completed/ex048/report.md`.

## L06.06.1 Marginal pricing principle

**Objective.** Explain marginal pricing principle and show it in the EX-048 output.

**Prerequisites.** L06.05.5

**Lesson.** The price is set by the cost of the next unit needed to serve one more MW. [K]

**Example.** EX-048 (Calculate Locational Marginal Prices) on synthetic North American data: constrained_gen_A_MW = 350 [EX]

**Do.** `python3 emi.py run 048 | grep '^constrained_gen_A_MW:'`

**Expect.** `constrained_gen_A_MW: 350`

**On the job.** Break down electricity prices into energy, congestion, and marginal loss components.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.05.5 | After: L06.06.2

## L06.06.2 Nodal price formation

**Objective.** Explain nodal price formation and show it in the EX-048 output.

**Prerequisites.** L06.06.1

**Lesson.** With congestion, that marginal cost differs by location: locational marginal price. [K]

**Example.** EX-048 (Calculate Locational Marginal Prices) on synthetic North American data: constrained_gen_B_MW = 150 [EX]

**Do.** `python3 emi.py run 048 | grep '^constrained_gen_B_MW:'`

**Expect.** `constrained_gen_B_MW: 150`

**On the job.** Break down electricity prices into energy, congestion, and marginal loss components.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.06.1 | After: L06.06.3

## L06.06.3 Hubs, zones and nodes

**Objective.** Explain hubs, zones and nodes and show it in the EX-048 output.

**Prerequisites.** L06.06.2

**Lesson.** Nodes are individual buses; zones and hubs are averages used for load and trading. [K]

**Example.** EX-048 (Calculate Locational Marginal Prices) on synthetic North American data: constrained_flow_A_to_B_MW = 250 [EX]

**Do.** `python3 emi.py run 048 | grep '^constrained_flow_A_to_B_MW:'`

**Expect.** `constrained_flow_A_to_B_MW: 250`

**On the job.** Break down electricity prices into energy, congestion, and marginal loss components.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.06.2 | After: L06.06.4

## L06.06.4 Price caps and scarcity pricing

**Objective.** Explain price caps and scarcity pricing and show it in the EX-048 output.

**Prerequisites.** L06.06.3

**Lesson.** Offer caps limit prices; scarcity pricing raises them when reserves run short. [K]

**Example.** EX-048 (Calculate Locational Marginal Prices) on synthetic North American data: constrained_lmp_A = 30 [EX]

**Do.** `python3 emi.py run 048 | grep '^constrained_lmp_A:'`

**Expect.** `constrained_lmp_A: 30`

**On the job.** Break down electricity prices into energy, congestion, and marginal loss components.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.06.3 | After: L06.06.5

## L06.06.5 LMP calculation

**Objective.** Explain lMP calculation and show it in the EX-048 output.

**Prerequisites.** L06.06.4

**Lesson.** An LMP can be computed from a dispatch model as the dual of each node's balance. [K]

**Example.** EX-048 (Calculate Locational Marginal Prices) on synthetic North American data: constrained_lmp_B = 60 [EX]

**Do.** `python3 emi.py run 048 | grep '^constrained_lmp_B:'`

**Expect.** `constrained_lmp_B: 60`

**On the job.** Break down electricity prices into energy, congestion, and marginal loss components.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.06.4 | After: L06.07.1
