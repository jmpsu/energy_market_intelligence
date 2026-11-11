# 9.5 Forward-curve construction

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-023 Build a Natural Gas Forward Curve (`python3 emi.py run 023`). Full output: `exercises/completed/ex023/report.md`.

## L09.05.1 Quote sources

**Objective.** Explain quote sources and show it in the EX-023 output.

**Prerequisites.** L09.04.5

**Lesson.** Curve inputs are exchange settlements and broker quotes. [K]

**Example.** EX-023 (Build a Natural Gas Forward Curve) on synthetic North American data: calendar_strip_USD_per_MMBtu = 3.25 [EX]

**Do.** `python3 emi.py run 023 | grep '^calendar_strip_USD_per_MMBtu:'`

**Expect.** `calendar_strip_USD_per_MMBtu: 3.25`

**On the job.** Construct a forward price curve from monthly market observations and calculate its shape.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.04.5 | After: L09.05.2

## L09.05.2 Interpolation and seasonality shaping

**Objective.** Explain interpolation and seasonality shaping and show it in the EX-023 output.

**Prerequisites.** L09.05.1

**Lesson.** Missing months are interpolated and shaped by seasonality. [K]

**Example.** EX-023 (Build a Natural Gas Forward Curve) on synthetic North American data: winter_strip = 3.52 [EX]

**Do.** `python3 emi.py run 023 | grep '^winter_strip:'`

**Expect.** `winter_strip: 3.52`

**On the job.** Construct a forward price curve from monthly market observations and calculate its shape.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.05.1 | After: L09.05.3

## L09.05.3 Arbitrage-free checks

**Objective.** Explain arbitrage-free checks and show it in the EX-023 output.

**Prerequisites.** L09.05.2

**Lesson.** Monthly prices must average to the quoted strip. [K]

**Example.** EX-023 (Build a Natural Gas Forward Curve) on synthetic North American data: summer_strip = 3.057143 [EX]

**Do.** `python3 emi.py run 023 | grep '^summer_strip:'`

**Expect.** `summer_strip: 3.057143`

**On the job.** Construct a forward price curve from monthly market observations and calculate its shape.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.05.2 | After: L09.05.4

## L09.05.4 Shaping to hourly or daily

**Objective.** Explain shaping to hourly or daily and show it in the EX-023 output.

**Prerequisites.** L09.05.3

**Lesson.** Monthly values are shaped to daily or hourly profiles. [K]

**Example.** EX-023 (Build a Natural Gas Forward Curve) on synthetic North American data: winter_minus_summer = 0.462857 [EX]

**Do.** `python3 emi.py run 023 | grep '^winter_minus_summer:'`

**Expect.** `winter_minus_summer: 0.462857`

**On the job.** Construct a forward price curve from monthly market observations and calculate its shape.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.05.3 | After: L09.05.5

## L09.05.5 Curve validation

**Objective.** Explain curve validation and show it in the EX-023 output.

**Prerequisites.** L09.05.4

**Lesson.** Validate curves before using them to value anything. [K]

**Example.** EX-023 (Build a Natural Gas Forward Curve) on synthetic North American data: jan_minus_jul_spread = 0.5 [EX]

**Do.** `python3 emi.py run 023 | grep '^jan_minus_jul_spread:'`

**Expect.** `jan_minus_jul_spread: 0.5`

**On the job.** Construct a forward price curve from monthly market observations and calculate its shape.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.05.4 | After: L09.06.1
