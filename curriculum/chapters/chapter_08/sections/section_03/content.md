# 8.3 Market data and forward curves

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-070 Build a Market Data Ingestion Pipeline (`python3 emi.py run 070`). Full output: `exercises/completed/ex070/report.md`.

## L08.03.1 Market data sourcing

**Objective.** Explain market data sourcing and show it in the EX-070 output.

**Prerequisites.** L08.02.5

**Lesson.** Market data comes from exchanges, brokers, price agencies and ISOs. [K]

**Example.** EX-070 (Build a Market Data Ingestion Pipeline) on synthetic North American data: raw_rows = 10 [EX]

**Do.** `python3 emi.py run 070 | grep '^raw_rows:'`

**Expect.** `raw_rows: 10`

**On the job.** Import historical prices, validate records, detect missing observations, and store clean market data.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.02.5 | After: L08.03.2

## L08.03.2 Curve building and marking

**Objective.** Explain curve building and marking and show it in the EX-070 output.

**Prerequisites.** L08.03.1

**Lesson.** Curves are built from that data and used to mark the book. [K]

**Example.** EX-070 (Build a Market Data Ingestion Pipeline) on synthetic North American data: rejected_rows = 2 [EX]

**Do.** `python3 emi.py run 070 | grep '^rejected_rows:'`

**Expect.** `rejected_rows: 2`

**On the job.** Import historical prices, validate records, detect missing observations, and store clean market data.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.03.1 | After: L08.03.3

## L08.03.3 End-of-day process

**Objective.** Explain end-of-day process and show it in the EX-070 output.

**Prerequisites.** L08.03.2

**Lesson.** End of day freezes prices, positions and P&L. [K]

**Example.** EX-070 (Build a Market Data Ingestion Pipeline) on synthetic North American data: reject_reasons = missing_price,non_numeric_price [EX]

**Do.** `python3 emi.py run 070 | grep '^reject_reasons:'`

**Expect.** `reject_reasons: missing_price,non_numeric_price`

**On the job.** Import historical prices, validate records, detect missing observations, and store clean market data.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.03.2 | After: L08.03.4

## L08.03.4 Curve validation

**Objective.** Explain curve validation and show it in the EX-070 output.

**Prerequisites.** L08.03.3

**Lesson.** Curve validation checks for gaps, stale values and jumps. [K]

**Example.** EX-070 (Build a Market Data Ingestion Pipeline) on synthetic North American data: duplicate_rows_superseded = 2 [EX]

**Do.** `python3 emi.py run 070 | grep '^duplicate_rows_superseded:'`

**Expect.** `duplicate_rows_superseded: 2`

**On the job.** Import historical prices, validate records, detect missing observations, and store clean market data.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.03.3 | After: L08.03.5

## L08.03.5 Data quality controls

**Objective.** Explain data quality controls and show it in the EX-070 output.

**Prerequisites.** L08.03.4

**Lesson.** Data-quality controls stop bad inputs before they reach valuation. [K]

**Example.** EX-070 (Build a Market Data Ingestion Pipeline) on synthetic North American data: curated_rows = 6 [EX]

**Do.** `python3 emi.py run 070 | grep '^curated_rows:'`

**Expect.** `curated_rows: 6`

**On the job.** Import historical prices, validate records, detect missing observations, and store clean market data.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.03.4 | After: L08.04.1
