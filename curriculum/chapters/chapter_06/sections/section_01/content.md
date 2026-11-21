# 6.1 North American electricity market structure

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-045 Map North American Electricity Markets (`python3 emi.py run 045`). Full output: `exercises/completed/ex045/report.md`.

## L06.01.1 Regulated vs restructured states

**Objective.** Explain regulated vs restructured states and show it in the EX-045 output.

**Prerequisites.** L05.10.5

**Lesson.** Some states kept regulated utilities; others restructured to competitive wholesale and retail markets. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: markets = 7 [EX]

**Do.** `python3 emi.py run 045 | grep '^markets:'`

**Expect.** `markets: 7`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

**Supply-Side Economics.**
The structure of electricity markets is determined by supply-side factors like generation capacity, transmission constraints, and the physical characteristics of power systems. In restructured markets, competitive forces drive the allocation of resources to meet demand efficiently. In regulated markets, utilities are often incentivized to maintain sufficient capacity to serve customers reliably.

**Market example:** In ERCOT, where there is significant market competition, price signals guide investment in new generation and transmission infrastructure. The system operator can observe how changes in supply (like a power plant outage) or demand (like a heat wave) affect prices across different nodes of the grid.

**Illustrative relationship:** ![Supply-Side Economics: Market Structure](../../../diagrams/diagram_14_m_N_merit_order.svg)

**Predict the shift.** If ERCOT experiences an increase in wind generation capacity, which curve would shift and in what direction?
* A) Demand curve shifts left (decrease in demand)
* B) Supply curve shifts right (increase in supply)
* C) Both curves shift
* D) Neither curve shifts

Answer: B) Supply curve shifts right (increase in supply)

Before: L05.10.5 | After: L06.01.2

## L06.01.2 Wholesale vs retail layers

**Objective.** Explain wholesale vs retail layers and show it in the EX-045 output.

**Prerequisites.** L06.01.1

**Lesson.** Wholesale is generators selling to utilities and retailers; retail is sales to end users. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: highest_rt_price_market = ISO_NE [EX]

**Do.** `python3 emi.py run 045 | grep '^highest_rt_price_market:'`

**Expect.** `highest_rt_price_market: ISO_NE`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.01.1 | After: L06.01.3

## L06.01.3 Federal and state jurisdiction

**Objective.** Explain federal and state jurisdiction and show it in the EX-045 output.

**Prerequisites.** L06.01.2

**Lesson.** Wholesale sales and transmission are federal; retail rates and distribution are state matters. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: largest_rt_minus_da_market = ERCOT [EX]

**Do.** `python3 emi.py run 045 | grep '^largest_rt_minus_da_market:'`

**Expect.** `largest_rt_minus_da_market: ERCOT`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.01.2 | After: L06.01.4

## L06.01.4 Market products overview

**Objective.** Explain market products overview and show it in the EX-045 output.

**Prerequisites.** L06.01.3

**Lesson.** Markets sell energy, capacity, ancillary services and transmission rights. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: largest_rt_minus_da_USD_per_MWh = 7 [EX]

**Do.** `python3 emi.py run 045 | grep '^largest_rt_minus_da_USD_per_MWh:'`

**Expect.** `largest_rt_minus_da_USD_per_MWh: 7`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.01.3 | After: L06.01.5

## L06.01.5 Market geography

**Objective.** Explain market geography and show it in the EX-045 output.

**Prerequisites.** L06.01.4

**Lesson.** About two thirds of US load sits inside ISO/RTO markets; the Southeast and much of the West trade bilaterally. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: highest_renewable_share_market = SPP [EX]

**Do.** `python3 emi.py run 045 | grep '^highest_renewable_share_market:'`

**Expect.** `highest_renewable_share_market: SPP`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.01.4 | After: L06.02.1
