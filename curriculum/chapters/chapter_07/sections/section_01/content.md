# 7.1 Generation technologies and operating characteristics

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-053 Calculate Generator Dispatch Economics (`python3 emi.py run 053`). Full output: `exercises/completed/ex053/report.md`.

## L07.01.1 Thermal technologies

**Objective.** Explain thermal technologies and show it in the EX-053 output.

**Prerequisites.** L06.10.5

**Lesson.** Thermal plants burn gas, coal or oil; combined cycles are efficient, peakers are flexible. [K]

**Example.** EX-053 (Calculate Generator Dispatch Economics) on synthetic North American data: NUC_cost = 9.28 [EX]

**Do.** `python3 emi.py run 053 | grep '^NUC_cost:'`

**Expect.** `NUC_cost: 9.28`

**On the job.** Rank generators by marginal operating cost and determine their dispatch order.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L06.10.5 | After: L07.01.2

## L07.01.2 Nuclear and hydro

**Objective.** Explain nuclear and hydro and show it in the EX-053 output.

**Prerequisites.** L07.01.1

**Lesson.** Nuclear runs flat out; hydro is flexible but limited by water. [K]

**Example.** EX-053 (Calculate Generator Dispatch Economics) on synthetic North American data: CC1_cost = 24.6 [EX]

**Do.** `python3 emi.py run 053 | grep '^CC1_cost:'`

**Expect.** `CC1_cost: 24.6`

**On the job.** Rank generators by marginal operating cost and determine their dispatch order.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.01.1 | After: L07.01.3

## L07.01.3 Wind and solar

**Objective.** Explain wind and solar and show it in the EX-053 output.

**Prerequisites.** L07.01.2

**Lesson.** Wind and solar have near-zero marginal cost and weather-driven output. [K]

**Example.** EX-053 (Calculate Generator Dispatch Economics) on synthetic North American data: COAL_cost = 25.92 [EX]

**Do.** `python3 emi.py run 053 | grep '^COAL_cost:'`

**Expect.** `COAL_cost: 25.92`

**On the job.** Rank generators by marginal operating cost and determine their dispatch order.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.01.2 | After: L07.01.4

## L07.01.4 Operating constraints: ramp, min run, start cost

**Objective.** Explain operating constraints: ramp, min run, start cost and show it in the EX-053 output.

**Prerequisites.** L07.01.3

**Lesson.** Ramp rates, minimum run times and start costs limit how units follow prices. [K]

**Example.** EX-053 (Calculate Generator Dispatch Economics) on synthetic North American data: CC2_cost = 27.05 [EX]

**Do.** `python3 emi.py run 053 | grep '^CC2_cost:'`

**Expect.** `CC2_cost: 27.05`

**On the job.** Rank generators by marginal operating cost and determine their dispatch order.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.01.3 | After: L07.01.5

## L07.01.5 Technology comparison

**Objective.** Explain technology comparison and show it in the EX-053 output.

**Prerequisites.** L07.01.4

**Lesson.** Compare technologies on cost, flexibility and availability, not capacity alone. [K]

**Example.** EX-053 (Calculate Generator Dispatch Economics) on synthetic North American data: GT_cost = 39.125 [EX]

**Do.** `python3 emi.py run 053 | grep '^GT_cost:'`

**Expect.** `GT_cost: 39.125`

**On the job.** Rank generators by marginal operating cost and determine their dispatch order.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.01.4 | After: L07.02.1
