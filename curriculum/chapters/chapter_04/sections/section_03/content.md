# 4.3 Firm and interruptible transportation

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-016 Calculate Pipeline Transportation Economics (`python3 emi.py run 016`). Full output: `exercises/completed/ex016/report.md`.

## L04.03.1 Firm service priority

**Objective.** Explain firm service priority and show it in the EX-016 output.

**Prerequisites.** L04.02.5

**Lesson.** Primary firm service is scheduled first and cut last. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: breakeven_load_factor = 0.849057 [EX]

**Do.** `python3 emi.py run 016 | grep '^breakeven_load_factor:'`

**Expect.** `breakeven_load_factor: 0.849057`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.02.5 | After: L04.03.2

## L04.03.2 Interruptible service economics

**Objective.** Explain interruptible service economics and show it in the EX-016 output.

**Prerequisites.** L04.03.1

**Lesson.** Interruptible service is cheap per unit but flows only when capacity is spare. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: firm_unit_cost_at_100pct = 0.47 [EX]

**Do.** `python3 emi.py run 016 | grep '^firm_unit_cost_at_100pct:'`

**Expect.** `firm_unit_cost_at_100pct: 0.47`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.03.1 | After: L04.03.3

## L04.03.3 Secondary firm and out-of-path

**Objective.** Explain secondary firm and out-of-path and show it in the EX-016 output.

**Prerequisites.** L04.03.2

**Lesson.** Secondary firm ranks between primary firm and interruptible. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: firm_unit_cost_at_50pct = 0.92 [EX]

**Do.** `python3 emi.py run 016 | grep '^firm_unit_cost_at_50pct:'`

**Expect.** `firm_unit_cost_at_50pct: 0.92`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.03.2 | After: L04.03.4

## L04.03.4 Curtailment order

**Objective.** Explain curtailment order and show it in the EX-016 output.

**Prerequisites.** L04.03.3

**Lesson.** Under constraint, the pipeline cuts interruptible, then secondary, then primary pro rata. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: spread = 0.8 [EX]

**Do.** `python3 emi.py run 016 | grep '^spread:'`

**Expect.** `spread: 0.8`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.03.3 | After: L04.03.5

## L04.03.5 Firm vs interruptible cost comparison

**Objective.** Explain firm vs interruptible cost comparison and show it in the EX-016 output.

**Prerequisites.** L04.03.4

**Lesson.** Firm wins at high load factors; interruptible wins when capacity is rarely needed. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: firm_monthly_margin_USD = 414000 [EX]

**Do.** `python3 emi.py run 016 | grep '^firm_monthly_margin_USD:'`

**Expect.** `firm_monthly_margin_USD: 414000`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.03.4 | After: L04.04.1
