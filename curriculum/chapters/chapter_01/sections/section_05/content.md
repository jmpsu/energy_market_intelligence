# 1.5 Eastern, Western, and ERCOT interconnections

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-045 Map North American Electricity Markets (`python3 emi.py run 045`). Full output: `exercises/completed/ex045/report.md`.

## L01.05.1 Synchronous interconnection concept

**Objective.** Explain synchronous interconnection concept and show it in the EX-045 output.

**Prerequisites.** L01.04.5

**Lesson.** An interconnection is a set of grids running in synchronism at one frequency; trouble anywhere is felt everywhere inside it. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: markets = 7 [EX]

**Do.** `python3 emi.py run 045 | grep '^markets:'`

**Expect.** `markets: 7`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.04.5 | After: L01.05.2

## L01.05.2 Eastern Interconnection scale and mix

**Objective.** Explain eastern Interconnection scale and mix and show it in the EX-045 output.

**Prerequisites.** L01.05.1

**Lesson.** The Eastern Interconnection is the largest in load and capacity and contains several ISOs plus bilateral regions. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: highest_rt_price_market = ISO_NE [EX]

**Do.** `python3 emi.py run 045 | grep '^highest_rt_price_market:'`

**Expect.** `highest_rt_price_market: ISO_NE`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.05.1 | After: L01.05.3

## L01.05.3 Western Interconnection and WECC

**Objective.** Explain western Interconnection and WECC and show it in the EX-045 output.

**Prerequisites.** L01.05.2

**Lesson.** The Western Interconnection is long-distance, hydro and solar rich, and coordinated under WECC. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: largest_rt_minus_da_market = ERCOT [EX]

**Do.** `python3 emi.py run 045 | grep '^largest_rt_minus_da_market:'`

**Expect.** `largest_rt_minus_da_market: ERCOT`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.05.2 | After: L01.05.4

## L01.05.4 ERCOT isolation and DC ties

**Objective.** Explain eRCOT isolation and DC ties and show it in the EX-045 output.

**Prerequisites.** L01.05.3

**Lesson.** ERCOT is its own interconnection with only small DC ties, so it can import little during scarcity. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: largest_rt_minus_da_USD_per_MWh = 7 [EX]

**Do.** `python3 emi.py run 045 | grep '^largest_rt_minus_da_USD_per_MWh:'`

**Expect.** `largest_rt_minus_da_USD_per_MWh: 7`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.05.3 | After: L01.05.5

## L01.05.5 Transfer capability vs commercial access

**Objective.** Explain transfer capability vs commercial access and show it in the EX-045 output.

**Prerequisites.** L01.05.4

**Lesson.** Physical transfer limits cap flows; commercial access also needs transmission service or market membership. [K]

**Example.** EX-045 (Map North American Electricity Markets) on synthetic North American data: highest_renewable_share_market = SPP [EX]

**Do.** `python3 emi.py run 045 | grep '^highest_renewable_share_market:'`

**Expect.** `highest_renewable_share_market: SPP`

**On the job.** Identify CAISO, PJM, MISO, SPP, NYISO, ISO-NE, and ERCOT; classify their market structures.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.05.4 | After: L01.06.1
