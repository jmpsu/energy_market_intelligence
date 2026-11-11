# 1.9 Market-data sources and industry information

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-007 Build an Energy Market Reference Database (`python3 emi.py run 007`). Full output: `exercises/completed/ex007/report.md`.

## L01.09.1 Price reporting agencies and indices

**Objective.** Explain price reporting agencies and indices and show it in the EX-007 output.

**Prerequisites.** L01.08.5

**Lesson.** Price reporting agencies survey trades and publish indices that contracts settle against. [K]

**Example.** EX-007 (Build an Energy Market Reference Database) on synthetic North American data: tables = dim_location,location,ref_pipeline_segment,ref_power_market [EX]

**Do.** `python3 emi.py run 007 | grep '^tables:'`

**Expect.** `tables: dim_location,location,ref_pipeline_segment,ref_power_market`

**On the job.** Create structured records for major North American energy hubs, pipelines, power markets, and trading locations.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.08.5 | After: L01.09.2

## L01.09.2 ISO/RTO public data

**Objective.** Explain iSO/RTO public data and show it in the EX-007 output.

**Prerequisites.** L01.09.1

**Lesson.** ISOs publish prices, load, generation and constraints, usually free and in bulk. [K]

**Example.** EX-007 (Build an Energy Market Reference Database) on synthetic North American data: locations = 14 [EX]

**Do.** `python3 emi.py run 007 | grep '^locations:'`

**Expect.** `locations: 14`

**On the job.** Create structured records for major North American energy hubs, pipelines, power markets, and trading locations.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.09.1 | After: L01.09.3

## L01.09.3 EIA and regulatory datasets

**Objective.** Explain eIA and regulatory datasets and show it in the EX-007 output.

**Prerequisites.** L01.09.2

**Lesson.** EIA and regulators publish production, storage, flows and filings; coverage is broad, timing is lagged. [K]

**Example.** EX-007 (Build an Energy Market Reference Database) on synthetic North American data: gas_locations = 5 [EX]

**Do.** `python3 emi.py run 007 | grep '^gas_locations:'`

**Expect.** `gas_locations: 5`

**On the job.** Create structured records for major North American energy hubs, pipelines, power markets, and trading locations.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.09.2 | After: L01.09.4

## L01.09.4 Pipeline electronic bulletin boards

**Objective.** Explain pipeline electronic bulletin boards and show it in the EX-007 output.

**Prerequisites.** L01.09.3

**Lesson.** Pipeline bulletin boards post capacity, scheduled volumes and notices each cycle. [K]

**Example.** EX-007 (Build an Energy Market Reference Database) on synthetic North American data: ngl_locations = 2 [EX]

**Do.** `python3 emi.py run 007 | grep '^ngl_locations:'`

**Expect.** `ngl_locations: 2`

**On the job.** Create structured records for major North American energy hubs, pipelines, power markets, and trading locations.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.09.3 | After: L01.09.5

## L01.09.5 Data licensing and provenance

**Objective.** Explain data licensing and provenance and show it in the EX-007 output.

**Prerequisites.** L01.09.4

**Lesson.** Licences limit redistribution and derived use; a product must track where every data point came from. [K]

**Example.** EX-007 (Build an Energy Market Reference Database) on synthetic North American data: power_markets = 7 [EX]

**Do.** `python3 emi.py run 007 | grep '^power_markets:'`

**Expect.** `power_markets: 7`

**On the job.** Create structured records for major North American energy hubs, pipelines, power markets, and trading locations.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.09.4 | After: L01.10.1
