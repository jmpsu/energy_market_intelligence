# 10.7 Snowflake, Databricks, and analytical data architecture

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-087 Build an Energy Market Data Warehouse (`python3 emi.py run 087`). Full output: `exercises/completed/ex087/report.md`.

## L10.07.1 Cloud data warehouse concepts

**Objective.** Explain cloud data warehouse concepts and show it in the EX-087 output.

**Prerequisites.** L10.06.5

**Lesson.** A cloud warehouse separates storage from compute. [K]

**Example.** EX-087 (Build an Energy Market Data Warehouse) on synthetic North American data: dim_location_rows = 12 [EX]

**Do.** `python3 emi.py run 087 | grep '^dim_location_rows:'`

**Expect.** `dim_location_rows: 12`

**On the job.** Design a relational database for prices, generation, transmission, demand, storage, and market participants.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.06.5 | After: L10.07.2

## L10.07.2 Lakehouse concepts

**Objective.** Explain lakehouse concepts and show it in the EX-087 output.

**Prerequisites.** L10.07.1

**Lesson.** A lakehouse stores raw files with table features. [K]

**Example.** EX-087 (Build an Energy Market Data Warehouse) on synthetic North American data: dim_time_rows = 3 [EX]

**Do.** `python3 emi.py run 087 | grep '^dim_time_rows:'`

**Expect.** `dim_time_rows: 3`

**On the job.** Design a relational database for prices, generation, transmission, demand, storage, and market participants.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.07.1 | After: L10.07.3

## L10.07.3 Dimensional modeling for energy data

**Objective.** Explain dimensional modeling for energy data and show it in the EX-087 output.

**Prerequisites.** L10.07.2

**Lesson.** Dimensional models split facts from dimensions. [K]

**Example.** EX-087 (Build an Energy Market Data Warehouse) on synthetic North American data: dim_provider_rows = 2 [EX]

**Do.** `python3 emi.py run 087 | grep '^dim_provider_rows:'`

**Expect.** `dim_provider_rows: 2`

**On the job.** Design a relational database for prices, generation, transmission, demand, storage, and market participants.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.07.2 | After: L10.07.4

## L10.07.4 Time-series storage patterns

**Objective.** Explain time-series storage patterns and show it in the EX-087 output.

**Prerequisites.** L10.07.3

**Lesson.** Time series are partitioned by date and location. [K]

**Example.** EX-087 (Build an Energy Market Data Warehouse) on synthetic North American data: fact_price_rows = 6 [EX]

**Do.** `python3 emi.py run 087 | grep '^fact_price_rows:'`

**Expect.** `fact_price_rows: 6`

**On the job.** Design a relational database for prices, generation, transmission, demand, storage, and market participants.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.07.3 | After: L10.07.5

## L10.07.5 Architecture design

**Objective.** Explain architecture design and show it in the EX-087 output.

**Prerequisites.** L10.07.4

**Lesson.** Design follows the queries users run. [K]

**Example.** EX-087 (Build an Energy Market Data Warehouse) on synthetic North American data: orphan_facts = 0 [EX]

**Do.** `python3 emi.py run 087 | grep '^orphan_facts:'`

**Expect.** `orphan_facts: 0`

**On the job.** Design a relational database for prices, generation, transmission, demand, storage, and market participants.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.07.4 | After: L10.08.1
