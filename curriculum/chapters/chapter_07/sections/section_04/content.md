# 7.4 Spark spreads and fuel procurement

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-055 Calculate Spark Spreads (`python3 emi.py run 055`). Full output: `exercises/completed/ex055/report.md`.

## L07.04.1 Spark spread definition

**Objective.** Explain spark spread definition and show it in the EX-055 output.

**Prerequisites.** L07.03.5

**Lesson.** Spark spread is power price minus heat rate times gas price. [K]

**Example.** EX-055 (Calculate Spark Spreads) on synthetic North American data: hour_1_spark_USD_per_MWh = 21 [EX]

**Do.** `python3 emi.py run 055 | grep '^hour_1_spark_USD_per_MWh:'`

**Expect.** `hour_1_spark_USD_per_MWh: 21`

**On the job.** Compare electricity revenue with natural gas fuel costs and variable operating expenses.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.03.5 | After: L07.04.2

## L07.04.2 Clean spark and emissions costs

**Objective.** Explain clean spark and emissions costs and show it in the EX-055 output.

**Prerequisites.** L07.04.1

**Lesson.** The clean spark spread also subtracts emissions cost. [K]

**Example.** EX-055 (Calculate Spark Spreads) on synthetic North American data: hour_2_spark_USD_per_MWh = 29.25 [EX]

**Do.** `python3 emi.py run 055 | grep '^hour_2_spark_USD_per_MWh:'`

**Expect.** `hour_2_spark_USD_per_MWh: 29.25`

**On the job.** Compare electricity revenue with natural gas fuel costs and variable operating expenses.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.04.1 | After: L07.04.3

## L07.04.3 Implied market heat rate

**Objective.** Explain implied market heat rate and show it in the EX-055 output.

**Prerequisites.** L07.04.2

**Lesson.** Implied heat rate is power price divided by gas price. [K]

**Example.** EX-055 (Calculate Spark Spreads) on synthetic North American data: hour_3_spark_USD_per_MWh = 37.5 [EX]

**Do.** `python3 emi.py run 055 | grep '^hour_3_spark_USD_per_MWh:'`

**Expect.** `hour_3_spark_USD_per_MWh: 37.5`

**On the job.** Compare electricity revenue with natural gas fuel costs and variable operating expenses.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.04.2 | After: L07.04.4

## L07.04.4 Fuel procurement timing

**Objective.** Explain fuel procurement timing and show it in the EX-055 output.

**Prerequisites.** L07.04.3

**Lesson.** Gas must be bought on the gas-day schedule before power needs are certain. [K]

**Example.** EX-055 (Calculate Spark Spreads) on synthetic North American data: hour_4_spark_USD_per_MWh = 45.75 [EX]

**Do.** `python3 emi.py run 055 | grep '^hour_4_spark_USD_per_MWh:'`

**Expect.** `hour_4_spark_USD_per_MWh: 45.75`

**On the job.** Compare electricity revenue with natural gas fuel costs and variable operating expenses.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.04.3 | After: L07.04.5

## L07.04.5 Spark hedging

**Objective.** Explain spark hedging and show it in the EX-055 output.

**Prerequisites.** L07.04.4

**Lesson.** A generator hedges by selling power and buying gas in heat-rate proportion. [K]

**Example.** EX-055 (Calculate Spark Spreads) on synthetic North American data: hour_5_spark_USD_per_MWh = 9 [EX]

**Do.** `python3 emi.py run 055 | grep '^hour_5_spark_USD_per_MWh:'`

**Expect.** `hour_5_spark_USD_per_MWh: 9`

**On the job.** Compare electricity revenue with natural gas fuel costs and variable operating expenses.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.04.4 | After: L07.05.1
