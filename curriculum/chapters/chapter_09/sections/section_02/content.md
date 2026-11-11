# 9.2 Statistical volatility and regime changes

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-078 Analyze Energy Price Volatility (`python3 emi.py run 078`). Full output: `exercises/completed/ex078/report.md`.

## L09.02.1 Historical volatility

**Objective.** Explain historical volatility and show it in the EX-078 output.

**Prerequisites.** L09.01.5

**Lesson.** Historical volatility is the standard deviation of returns, annualised. [K]

**Example.** EX-078 (Analyze Energy Price Volatility) on synthetic North American data: observations = 399 [EX]

**Do.** `python3 emi.py run 078 | grep '^observations:'`

**Expect.** `observations: 399`

**On the job.** Calculate rolling volatility and identify periods of unusual market behavior.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.01.5 | After: L09.02.2

## L09.02.2 Rolling and EWMA volatility

**Objective.** Explain rolling and EWMA volatility and show it in the EX-078 output.

**Prerequisites.** L09.02.1

**Lesson.** Rolling windows weight days equally; EWMA weights recent days more. [K]

**Example.** EX-078 (Analyze Energy Price Volatility) on synthetic North American data: daily_vol = 0.024941 [EX]

**Do.** `python3 emi.py run 078 | grep '^daily_vol:'`

**Expect.** `daily_vol: 0.024941`

**On the job.** Calculate rolling volatility and identify periods of unusual market behavior.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.02.1 | After: L09.02.3

## L09.02.3 Volatility clustering

**Objective.** Explain volatility clustering and show it in the EX-078 output.

**Prerequisites.** L09.02.2

**Lesson.** High-volatility days cluster. [K]

**Example.** EX-078 (Analyze Energy Price Volatility) on synthetic North American data: annualised_vol = 0.395929 [EX]

**Do.** `python3 emi.py run 078 | grep '^annualised_vol:'`

**Expect.** `annualised_vol: 0.395929`

**On the job.** Calculate rolling volatility and identify periods of unusual market behavior.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.02.2 | After: L09.02.4

## L09.02.4 Regime identification

**Objective.** Explain regime identification and show it in the EX-078 output.

**Prerequisites.** L09.02.3

**Lesson.** Regimes are periods with distinct levels of volatility. [K]

**Example.** EX-078 (Analyze Energy Price Volatility) on synthetic North American data: median_rolling_vol = 0.387589 [EX]

**Do.** `python3 emi.py run 078 | grep '^median_rolling_vol:'`

**Expect.** `median_rolling_vol: 0.387589`

**On the job.** Calculate rolling volatility and identify periods of unusual market behavior.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.02.3 | After: L09.02.5

## L09.02.5 Regime-aware analysis

**Objective.** Explain regime-aware analysis and show it in the EX-078 output.

**Prerequisites.** L09.02.4

**Lesson.** Analyse and limit risk by regime. [K]

**Example.** EX-078 (Analyze Energy Price Volatility) on synthetic North American data: max_rolling_vol = 0.613041 [EX]

**Do.** `python3 emi.py run 078 | grep '^max_rolling_vol:'`

**Expect.** `max_rolling_vol: 0.613041`

**On the job.** Calculate rolling volatility and identify periods of unusual market behavior.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.02.4 | After: L09.03.1
