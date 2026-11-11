# 1.6 RTOs, ISOs, utilities, generators, marketers, and traders

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-045 Map North American Electricity Markets (`python3 emi.py run 045`). Full output: `exercises/completed/ex045/report.md`.

## L01.06.1 RTO and ISO functions

**Objective.** Explain rTO and ISO functions and show it in the EX-045 output.

**Prerequisites.** L01.05.5

**Lesson.** An ISO or RTO runs the grid and the wholesale market for a region without owning generation or wires. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: markets = 7 [EX]

**Do.** `python3 emi.py run 045 | grep '^markets:'`

**Expect.** `markets: 7`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.05.5 | After: L01.06.2

## L01.06.2 Vertically integrated utilities

**Objective.** Explain vertically integrated utilities and show it in the EX-045 output.

**Prerequisites.** L01.06.1

**Lesson.** Vertically integrated utilities own generation, transmission and distribution and recover costs through regulated rates. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: highest_rt_price_market = ISO_NE [EX]

**Do.** `python3 emi.py run 045 | grep '^highest_rt_price_market:'`

**Expect.** `highest_rt_price_market: ISO_NE`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.06.1 | After: L01.06.3

## L01.06.3 Independent power producers

**Objective.** Explain independent power producers and show it in the EX-045 output.

**Prerequisites.** L01.06.2

**Lesson.** Independent power producers own merchant plants and live on market revenue or contracts. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: largest_rt_minus_da_market = ERCOT [EX]

**Do.** `python3 emi.py run 045 | grep '^largest_rt_minus_da_market:'`

**Expect.** `largest_rt_minus_da_market: ERCOT`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.06.2 | After: L01.06.4

## L01.06.4 Power marketers and trading desks

**Objective.** Explain power marketers and trading desks and show it in the EX-045 output.

**Prerequisites.** L01.06.3

**Lesson.** Power marketers buy and resell energy and manage portfolios without necessarily owning assets. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: largest_rt_minus_da_USD_per_MWh = 7 [EX]

**Do.** `python3 emi.py run 045 | grep '^largest_rt_minus_da_USD_per_MWh:'`

**Expect.** `largest_rt_minus_da_USD_per_MWh: 7`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.06.3 | After: L01.06.5

## L01.06.5 Balancing authorities and reliability roles

**Objective.** Explain balancing authorities and reliability roles and show it in the EX-045 output.

**Prerequisites.** L01.06.4

**Lesson.** Balancing authorities keep supply and demand matched in their area; reliability coordinators watch the wider system. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: highest_renewable_share_market = SPP [EX]

**Do.** `python3 emi.py run 045 | grep '^highest_renewable_share_market:'`

**Expect.** `highest_renewable_share_market: SPP`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.06.4 | After: L01.07.1
