# 3.6 Transportation and basis contracts

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-016 Calculate Pipeline Transportation Economics (`python3 emi.py run 016`). Full output: `exercises/completed/ex016/report.md`.

## L03.06.1 Transport contract as a spread option

**Objective.** Explain transport contract as a spread option and show it in the EX-016 output.

**Prerequisites.** L03.05.5

**Lesson.** Firm transport lets you buy at one point and sell at another, so its value moves like an option on the spread. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: breakeven_load_factor = 0.849057 [EX]

**Do.** `python3 emi.py run 016 | grep '^breakeven_load_factor:'`

**Expect.** `breakeven_load_factor: 0.849057`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.05.5 | After: L03.06.2

## L03.06.2 Basis swaps

**Objective.** Explain basis swaps and show it in the EX-016 output.

**Prerequisites.** L03.06.1

**Lesson.** A basis swap fixes the difference between a location and Henry Hub. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: firm_unit_cost_at_100pct = 0.47 [EX]

**Do.** `python3 emi.py run 016 | grep '^firm_unit_cost_at_100pct:'`

**Expect.** `firm_unit_cost_at_100pct: 0.47`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.06.1 | After: L03.06.3

## L03.06.3 Locational spread hedging

**Objective.** Explain locational spread hedging and show it in the EX-016 output.

**Prerequisites.** L03.06.2

**Lesson.** Hedging a regional position needs both a benchmark hedge and a basis hedge. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: firm_unit_cost_at_50pct = 0.92 [EX]

**Do.** `python3 emi.py run 016 | grep '^firm_unit_cost_at_50pct:'`

**Expect.** `firm_unit_cost_at_50pct: 0.92`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.06.2 | After: L03.06.4

## L03.06.4 Valuing firm transport

**Objective.** Explain valuing firm transport and show it in the EX-016 output.

**Prerequisites.** L03.06.3

**Lesson.** Transport value is the spread less variable cost, compared with the reservation charge. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: spread = 0.8 [EX]

**Do.** `python3 emi.py run 016 | grep '^spread:'`

**Expect.** `spread: 0.8`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.06.3 | After: L03.06.5

## L03.06.5 Hedge effectiveness

**Objective.** Explain hedge effectiveness and show it in the EX-016 output.

**Prerequisites.** L03.06.4

**Lesson.** A hedge is effective when its P&L offsets the exposure; a Henry Hub hedge alone leaves basis open. [K]

**Example.** EX-016 (Calculate Pipeline Transportation Economics) on synthetic North American data: firm_monthly_margin_USD = 414000 [EX]

**Do.** `python3 emi.py run 016 | grep '^firm_monthly_margin_USD:'`

**Expect.** `firm_monthly_margin_USD: 414000`

**On the job.** Compare firm and interruptible transportation costs under different market conditions.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.06.4 | After: L03.07.1
