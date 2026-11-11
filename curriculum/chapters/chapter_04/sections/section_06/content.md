# 4.6 Canadian natural gas infrastructure and AECO

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-011 Analyze Canadian Natural Gas Supply (`python3 emi.py run 011`). Full output: `exercises/completed/ex011/report.md`.

## L04.06.1 WCSB and Montney supply

**Objective.** Explain wCSB and Montney supply and show it in the EX-011 output.

**Prerequisites.** L04.05.5

**Lesson.** Western Canada's basin, led by the Montney, supplies Canada and exports to the US. [K]

**Example.** EX-011 (Analyze Canadian Natural Gas Supply) on synthetic North American data: total_2026_Bcf_d = 19 [EX]

**Do.** `python3 emi.py run 011 | grep '^total_2026_Bcf_d:'`

**Expect.** `total_2026_Bcf_d: 19`

**On the job.** Compare production from the Montney, Duvernay, and Western Canadian Sedimentary Basin.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.05.5 | After: L04.06.2

## L04.06.2 NGTL and Canadian mainline systems

**Objective.** Explain nGTL and Canadian mainline systems and show it in the EX-011 output.

**Prerequisites.** L04.06.1

**Lesson.** Large gathering and mainline systems move that gas to Alberta markets and export points. [K]

**Example.** EX-011 (Analyze Canadian Natural Gas Supply) on synthetic North American data: total_growth_pct = 2.702703 [EX]

**Do.** `python3 emi.py run 011 | grep '^total_growth_pct:'`

**Expect.** `total_growth_pct: 2.702703`

**On the job.** Compare production from the Montney, Duvernay, and Western Canadian Sedimentary Basin.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.06.1 | After: L04.06.3

## L04.06.3 AECO pricing and basis

**Objective.** Explain aECO pricing and basis and show it in the EX-011 output.

**Prerequisites.** L04.06.2

**Lesson.** AECO is the Alberta benchmark and usually trades below Henry Hub. [K]

**Example.** EX-011 (Analyze Canadian Natural Gas Supply) on synthetic North American data: Montney_netback = 1.25 [EX]

**Do.** `python3 emi.py run 011 | grep '^Montney_netback:'`

**Expect.** `Montney_netback: 1.25`

**On the job.** Compare production from the Montney, Duvernay, and Western Canadian Sedimentary Basin.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.06.2 | After: L04.06.4

## L04.06.4 Export points to the US

**Objective.** Explain export points to the US and show it in the EX-011 output.

**Prerequisites.** L04.06.3

**Lesson.** Exports cross into the US Northwest, Midwest and Northeast. [K]

**Example.** EX-011 (Analyze Canadian Natural Gas Supply) on synthetic North American data: Duvernay_netback = 1.55 [EX]

**Do.** `python3 emi.py run 011 | grep '^Duvernay_netback:'`

**Expect.** `Duvernay_netback: 1.55`

**On the job.** Compare production from the Montney, Duvernay, and Western Canadian Sedimentary Basin.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.06.3 | After: L04.06.5

## L04.06.5 Canada-US flow economics

**Objective.** Explain canada-US flow economics and show it in the EX-011 output.

**Prerequisites.** L04.06.4

**Lesson.** Canadian gas flows south when the price difference covers transport. [K]

**Example.** EX-011 (Analyze Canadian Natural Gas Supply) on synthetic North American data: Other_WCSB_netback = -0.1 [EX]

**Do.** `python3 emi.py run 011 | grep '^Other_WCSB_netback:'`

**Expect.** `Other_WCSB_netback: -0.1`

**On the job.** Compare production from the Montney, Duvernay, and Western Canadian Sedimentary Basin.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.06.4 | After: L04.07.1
