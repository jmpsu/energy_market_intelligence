# 6.3 PJM, MISO, SPP, ERCOT, CAISO, NYISO, and ISO-NE

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-045 Map North American Electricity Markets (`python3 emi.py run 045`). Full output: `exercises/completed/ex045/report.md`.

## L06.03.1 PJM and MISO features

**Objective.** Explain pJM and MISO features and show it in the EX-045 output.

**Prerequisites.** L06.02.5

**Lesson.** PJM and MISO are large multi-state markets with nodal energy pricing. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: markets = 7 [EX]

**Do.** `python3 emi.py run 045 | grep '^markets:'`

**Expect.** `markets: 7`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.02.5 | After: L06.03.2

## L06.03.2 SPP and ERCOT features

**Objective.** Explain sPP and ERCOT features and show it in the EX-045 output.

**Prerequisites.** L06.03.1

**Lesson.** SPP covers the central plains; ERCOT is an energy-only Texas market under state oversight. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: highest_rt_price_market = ISO_NE [EX]

**Do.** `python3 emi.py run 045 | grep '^highest_rt_price_market:'`

**Expect.** `highest_rt_price_market: ISO_NE`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.03.1 | After: L06.03.3

## L06.03.3 CAISO and Western EIM

**Objective.** Explain cAISO and Western EIM and show it in the EX-045 output.

**Prerequisites.** L06.03.2

**Lesson.** CAISO runs California and a wider Western real-time imbalance market. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: largest_rt_minus_da_market = ERCOT [EX]

**Do.** `python3 emi.py run 045 | grep '^largest_rt_minus_da_market:'`

**Expect.** `largest_rt_minus_da_market: ERCOT`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.03.2 | After: L06.03.4

## L06.03.4 NYISO and ISO-NE features

**Objective.** Explain nYISO and ISO-NE features and show it in the EX-045 output.

**Prerequisites.** L06.03.3

**Lesson.** NYISO and ISO-NE are single-state and six-state markets with tight gas dependence. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: largest_rt_minus_da_USD_per_MWh = 7 [EX]

**Do.** `python3 emi.py run 045 | grep '^largest_rt_minus_da_USD_per_MWh:'`

**Expect.** `largest_rt_minus_da_USD_per_MWh: 7`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.03.3 | After: L06.03.5

## L06.03.5 Cross-market comparison

**Objective.** Explain cross-market comparison and show it in the EX-045 output.

**Prerequisites.** L06.03.4

**Lesson.** Markets differ in capacity mechanisms, scarcity pricing and settlement detail. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: highest_renewable_share_market = SPP [EX]

**Do.** `python3 emi.py run 045 | grep '^highest_renewable_share_market:'`

**Expect.** `highest_renewable_share_market: SPP`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.03.4 | After: L06.04.1
