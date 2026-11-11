# 8.8 P&L attribution and explain

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-071 Calculate Daily Trading P&L (`python3 emi.py run 071`). Full output: `exercises/completed/ex071/report.md`.

## L08.08.1 New-deal P&L

**Objective.** Explain new-deal P&L and show it in the EX-071 output.

**Prerequisites.** L08.07.5

**Lesson.** New-deal P&L is the value of today's trades against today's curve. [K]

**Example.** EX-071 (Calculate Daily Trading P&L) on synthetic North American data: mtm_day1_USD = 59500 [EX]

**Do.** `python3 emi.py run 071 | grep '^mtm_day1_USD:'`

**Expect.** `mtm_day1_USD: 59500`

**On the job.** Revalue a portfolio using updated market prices and calculate daily gains and losses.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.07.5 | After: L08.08.2

## L08.08.2 Price (delta) P&L

**Objective.** Explain price (delta) P&L and show it in the EX-071 output.

**Prerequisites.** L08.08.1

**Lesson.** Delta P&L is existing position times price change. [K]

**Example.** EX-071 (Calculate Daily Trading P&L) on synthetic North American data: mtm_day2_USD = 70500 [EX]

**Do.** `python3 emi.py run 071 | grep '^mtm_day2_USD:'`

**Expect.** `mtm_day2_USD: 70500`

**On the job.** Revalue a portfolio using updated market prices and calculate daily gains and losses.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.08.1 | After: L08.08.3

## L08.08.3 Time and carry effects

**Objective.** Explain time and carry effects and show it in the EX-071 output.

**Prerequisites.** L08.08.2

**Lesson.** Time and carry effects come from moving a day closer to delivery. [K]

**Example.** EX-071 (Calculate Daily Trading P&L) on synthetic North American data: daily_pnl_USD = 11000 [EX]

**Do.** `python3 emi.py run 071 | grep '^daily_pnl_USD:'`

**Expect.** `daily_pnl_USD: 11000`

**On the job.** Revalue a portfolio using updated market prices and calculate daily gains and losses.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.08.2 | After: L08.08.4

## L08.08.4 Unexplained P&L

**Objective.** Explain unexplained P&L and show it in the EX-071 output.

**Prerequisites.** L08.08.3

**Lesson.** Unexplained P&L is whatever the attribution cannot assign. [K]

**Example.** EX-071 (Calculate Daily Trading P&L) on synthetic North American data: price_pnl_USD = 3500 [EX]

**Do.** `python3 emi.py run 071 | grep '^price_pnl_USD:'`

**Expect.** `price_pnl_USD: 3500`

**On the job.** Revalue a portfolio using updated market prices and calculate daily gains and losses.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.08.3 | After: L08.08.5

## L08.08.5 P&L explain report

**Objective.** Explain p&L explain report and show it in the EX-071 output.

**Prerequisites.** L08.08.4

**Lesson.** A P&L explain report lists each driver. [K]

**Example.** EX-071 (Calculate Daily Trading P&L) on synthetic North American data: new_deal_pnl_USD = 7500 [EX]

**Do.** `python3 emi.py run 071 | grep '^new_deal_pnl_USD:'`

**Expect.** `new_deal_pnl_USD: 7500`

**On the job.** Revalue a portfolio using updated market prices and calculate daily gains and losses.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.08.4 | After: L08.09.1
