# 6.5 Day-ahead and real-time market operations

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-047 Analyze Day-Ahead and Real-Time Markets (`python3 emi.py run 047`). Full output: `exercises/completed/ex047/report.md`.

## L06.05.1 Day-ahead market clearing

**Objective.** Explain day-ahead market clearing and show it in the EX-047 output.

**Prerequisites.** L06.04.5

**Lesson.** The day-ahead market clears hourly schedules and prices for tomorrow. [K]

**Example.** EX-047 (Analyze Day-Ahead and Real-Time Markets) on synthetic North American data: mean_da_price = 62.125 [EX]

**Do.** `python3 emi.py run 047 | grep '^mean_da_price:'`

**Expect.** `mean_da_price: 62.125`

**On the job.** Compare scheduled electricity prices with actual real-time market prices.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.04.5 | After: L06.05.2

## L06.05.2 Real-time dispatch

**Objective.** Explain real-time dispatch and show it in the EX-047 output.

**Prerequisites.** L06.05.1

**Lesson.** The real-time market redispatches every few minutes to follow actual conditions. [K]

**Example.** EX-047 (Analyze Day-Ahead and Real-Time Markets) on synthetic North American data: mean_rt_price = 68.833333 [EX]

**Do.** `python3 emi.py run 047 | grep '^mean_rt_price:'`

**Expect.** `mean_rt_price: 68.833333`

**On the job.** Compare scheduled electricity prices with actual real-time market prices.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.05.1 | After: L06.05.3

## L06.05.3 Two-settlement system

**Objective.** Explain two-settlement system and show it in the EX-047 output.

**Prerequisites.** L06.05.2

**Lesson.** Day-ahead quantities settle at day-ahead prices; deviations settle at real-time prices. [K]

**Example.** EX-047 (Analyze Day-Ahead and Real-Time Markets) on synthetic North American data: mean_dart_spread = -6.708333 [EX]

**Do.** `python3 emi.py run 047 | grep '^mean_dart_spread:'`

**Expect.** `mean_dart_spread: -6.708333`

**On the job.** Compare scheduled electricity prices with actual real-time market prices.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.05.2 | After: L06.05.4

## L06.05.4 Virtual bidding

**Objective.** Explain virtual bidding and show it in the EX-047 output.

**Prerequisites.** L06.05.3

**Lesson.** Virtual bids take financial positions between the two markets and help prices converge. [K]

**Example.** EX-047 (Analyze Day-Ahead and Real-Time Markets) on synthetic North American data: hours_rt_above_da = 11 [EX]

**Do.** `python3 emi.py run 047 | grep '^hours_rt_above_da:'`

**Expect.** `hours_rt_above_da: 11`

**On the job.** Compare scheduled electricity prices with actual real-time market prices.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.05.3 | After: L06.05.5

## L06.05.5 DA-RT spread analysis

**Objective.** Explain dA-RT spread analysis and show it in the EX-047 output.

**Prerequisites.** L06.05.4

**Lesson.** The DA-RT spread shows forecast error and risk premium. [K]

**Example.** EX-047 (Analyze Day-Ahead and Real-Time Markets) on synthetic North American data: rt_price_std = 54.065714 [EX]

**Do.** `python3 emi.py run 047 | grep '^rt_price_std:'`

**Expect.** `rt_price_std: 54.065714`

**On the job.** Compare scheduled electricity prices with actual real-time market prices.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.05.4 | After: L06.06.1
