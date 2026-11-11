# 9.1 Energy price time series and returns

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-078 Analyze Energy Price Volatility (`python3 emi.py run 078`). Full output: `exercises/completed/ex078/report.md`.

## L09.01.1 Price series properties

**Objective.** Explain price series properties and show it in the EX-078 output.

**Prerequisites.** L08.10.5

**Lesson.** Energy prices show seasonality, spikes and mean reversion. [K]

**Example.** EX-078 (Analyze Energy Price Volatility) on synthetic North American data: observations = 399 [EX]

**Do.** `python3 emi.py run 078 | grep '^observations:'`

**Expect.** `observations: 399`

**On the job.** Calculate rolling volatility and identify periods of unusual market behavior.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L08.10.5 | After: L09.01.2

## L09.01.2 Return calculation

**Objective.** Explain return calculation and show it in the EX-078 output.

**Prerequisites.** L09.01.1

**Lesson.** Returns are usually log price changes. [K]

**Example.** EX-078 (Analyze Energy Price Volatility) on synthetic North American data: daily_vol = 0.024941 [EX]

**Do.** `python3 emi.py run 078 | grep '^daily_vol:'`

**Expect.** `daily_vol: 0.024941`

**On the job.** Calculate rolling volatility and identify periods of unusual market behavior.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.01.1 | After: L09.01.3

## L09.01.3 Seasonality and mean reversion

**Objective.** Explain seasonality and mean reversion and show it in the EX-078 output.

**Prerequisites.** L09.01.2

**Lesson.** Mean reversion pulls prices back toward cost-based levels. [K]

**Example.** EX-078 (Analyze Energy Price Volatility) on synthetic North American data: annualised_vol = 0.395929 [EX]

**Do.** `python3 emi.py run 078 | grep '^annualised_vol:'`

**Expect.** `annualised_vol: 0.395929`

**On the job.** Calculate rolling volatility and identify periods of unusual market behavior.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.01.2 | After: L09.01.4

## L09.01.4 Spikes and jumps

**Objective.** Explain spikes and jumps and show it in the EX-078 output.

**Prerequisites.** L09.01.3

**Lesson.** Spikes are short, large moves from scarcity. [K]

**Example.** EX-078 (Analyze Energy Price Volatility) on synthetic North American data: median_rolling_vol = 0.387589 [EX]

**Do.** `python3 emi.py run 078 | grep '^median_rolling_vol:'`

**Expect.** `median_rolling_vol: 0.387589`

**On the job.** Calculate rolling volatility and identify periods of unusual market behavior.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.01.3 | After: L09.01.5

## L09.01.5 Stationarity testing

**Objective.** Explain stationarity testing and show it in the EX-078 output.

**Prerequisites.** L09.01.4

**Lesson.** Stationarity tests tell you if a series can be modelled directly. [K]

**Example.** EX-078 (Analyze Energy Price Volatility) on synthetic North American data: max_rolling_vol = 0.613041 [EX]

**Do.** `python3 emi.py run 078 | grep '^max_rolling_vol:'`

**Expect.** `max_rolling_vol: 0.613041`

**On the job.** Calculate rolling volatility and identify periods of unusual market behavior.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.01.4 | After: L09.02.1
