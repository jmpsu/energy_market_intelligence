# 4.2 Pipeline tariffs and transportation rights

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-016 Calculate Pipeline Transportation Economics (`python3 emi.py run 016`). Full output: `exercises/completed/ex016/report.md`.

## L04.02.1 Tariff structure

**Objective.** Explain tariff structure and show it in the EX-016 output.

**Prerequisites.** L04.01.5

**Lesson.** A tariff lists the services, rates and rules a pipeline must offer every shipper. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: breakeven_load_factor = 0.849057 [EX]

**Do.** `python3 emi.py run 016 | grep '^breakeven_load_factor:'`

**Expect.** `breakeven_load_factor: 0.849057`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.01.5 | After: L04.02.2

## L04.02.2 Rate design and reservation charges

**Objective.** Explain rate design and reservation charges and show it in the EX-016 output.

**Prerequisites.** L04.02.1

**Lesson.** Most fixed costs are recovered through the reservation charge. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: firm_unit_cost_at_100pct = 0.47 [EX]

**Do.** `python3 emi.py run 016 | grep '^firm_unit_cost_at_100pct:'`

**Expect.** `firm_unit_cost_at_100pct: 0.47`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.02.1 | After: L04.02.3

## L04.02.3 Receipt and delivery rights

**Objective.** Explain receipt and delivery rights and show it in the EX-016 output.

**Prerequisites.** L04.02.2

**Lesson.** A contract names primary receipt and delivery points where the shipper has the highest priority. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: firm_unit_cost_at_50pct = 0.92 [EX]

**Do.** `python3 emi.py run 016 | grep '^firm_unit_cost_at_50pct:'`

**Expect.** `firm_unit_cost_at_50pct: 0.92`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.02.2 | After: L04.02.4

## L04.02.4 Path and segmentation rights

**Objective.** Explain path and segmentation rights and show it in the EX-016 output.

**Prerequisites.** L04.02.3

**Lesson.** Shippers may split a path into segments or use other points at lower priority. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: spread = 0.8 [EX]

**Do.** `python3 emi.py run 016 | grep '^spread:'`

**Expect.** `spread: 0.8`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.02.3 | After: L04.02.5

## L04.02.5 Reading a tariff rate sheet

**Objective.** Explain reading a tariff rate sheet and show it in the EX-016 output.

**Prerequisites.** L04.02.4

**Lesson.** A rate sheet gives reservation, usage and fuel for each service and zone. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: firm_monthly_margin_USD = 414000 [EX]

**Do.** `python3 emi.py run 016 | grep '^firm_monthly_margin_USD:'`

**Expect.** `firm_monthly_margin_USD: 414000`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.02.4 | After: L04.03.1
