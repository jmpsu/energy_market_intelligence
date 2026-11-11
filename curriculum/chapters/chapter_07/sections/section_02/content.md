# 7.2 Heat rates and variable generation costs

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-054 Calculate Heat Rates (`python3 emi.py run 054`). Full output: `exercises/completed/ex054/report.md`.

## L07.02.1 Heat rate definition

**Objective.** Explain heat rate definition and show it in the EX-054 output.

**Prerequisites.** L07.01.5

**Lesson.** Heat rate is fuel input per unit of electricity, in MMBtu per MWh; lower is better. [K]

**Example.** EX-054 (Calculate Heat Rates) on synthetic North American data: full_load_heat_rate = 7 [EX]

**Do.** `python3 emi.py run 054 | grep '^full_load_heat_rate:'`

**Expect.** `full_load_heat_rate: 7`

**On the job.** Convert generator fuel consumption into electricity production efficiency.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.01.5 | After: L07.02.2

## L07.02.2 Incremental vs average heat rate

**Objective.** Explain incremental vs average heat rate and show it in the EX-054 output.

**Prerequisites.** L07.02.1

**Lesson.** Incremental heat rate is the fuel for the next MWh; average includes the no-load fuel. [K]

**Example.** EX-054 (Calculate Heat Rates) on synthetic North American data: min_load_heat_rate = 8.5 [EX]

**Do.** `python3 emi.py run 054 | grep '^min_load_heat_rate:'`

**Expect.** `min_load_heat_rate: 8.5`

**On the job.** Convert generator fuel consumption into electricity production efficiency.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.02.1 | After: L07.02.3

## L07.02.3 Variable O&M

**Objective.** Explain variable O&M and show it in the EX-054 output.

**Prerequisites.** L07.02.2

**Lesson.** Variable O&M is the non-fuel cost that scales with output. [K]

**Example.** EX-054 (Calculate Heat Rates) on synthetic North American data: incremental_heat_rate_400_to_500 = 6 [EX]

**Do.** `python3 emi.py run 054 | grep '^incremental_heat_rate_400_to_500:'`

**Expect.** `incremental_heat_rate_400_to_500: 6`

**On the job.** Convert generator fuel consumption into electricity production efficiency.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.02.2 | After: L07.02.4

## L07.02.4 Marginal cost calculation

**Objective.** Explain marginal cost calculation and show it in the EX-054 output.

**Prerequisites.** L07.02.3

**Lesson.** Marginal cost is incremental heat rate times fuel price plus variable O&M. [K]

**Example.** EX-054 (Calculate Heat Rates) on synthetic North American data: full_load_efficiency_pct = 48.742857 [EX]

**Do.** `python3 emi.py run 054 | grep '^full_load_efficiency_pct:'`

**Expect.** `full_load_efficiency_pct: 48.742857`

**On the job.** Convert generator fuel consumption into electricity production efficiency.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.02.3 | After: L07.02.5

## L07.02.5 Heat rate curve

**Objective.** Explain heat rate curve and show it in the EX-054 output.

**Prerequisites.** L07.02.4

**Lesson.** A heat rate curve shows efficiency improving toward full load. [K]

**Example.** EX-054 (Calculate Heat Rates) on synthetic North American data: full_load_Btu_per_kWh = 7000 [EX]

**Do.** `python3 emi.py run 054 | grep '^full_load_Btu_per_kWh:'`

**Expect.** `full_load_Btu_per_kWh: 7000`

**On the job.** Convert generator fuel consumption into electricity production efficiency.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.02.4 | After: L07.03.1
