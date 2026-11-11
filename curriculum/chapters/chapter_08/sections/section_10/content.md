# 8.10 ETRM architecture, integrations, and data warehouses

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-076 Design an ETRM Data Integration (`python3 emi.py run 076`). Full output: `exercises/completed/ex076/report.md`.

## L08.10.1 ETRM functional modules

**Objective.** Explain eTRM functional modules and show it in the EX-076 output.

**Prerequisites.** L08.09.5

**Lesson.** An ETRM has trade capture, scheduling, risk, settlement and accounting modules. [K]

**Example.** EX-076 (Design an ETRM Data Integration) on synthetic North American data: trades_in_store = 4 [EX]

**Do.** `python3 emi.py run 076 | grep '^trades_in_store:'`

**Expect.** `trades_in_store: 4`

**On the job.** Build a simplified integration connecting trading records, market data, risk calculations, scheduling, and settlement systems.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.09.5 | After: L08.10.2

## L08.10.2 Integration patterns

**Objective.** Explain integration patterns and show it in the EX-076 output.

**Prerequisites.** L08.10.1

**Lesson.** It integrates with market data, schedulers, the ledger and analytics by files, APIs or messages. [K]

**Example.** EX-076 (Design an ETRM Data Integration) on synthetic North American data: locations_in_market_data = 5 [EX]

**Do.** `python3 emi.py run 076 | grep '^locations_in_market_data:'`

**Expect.** `locations_in_market_data: 5`

**On the job.** Build a simplified integration connecting trading records, market data, risk calculations, scheduling, and settlement systems.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.10.1 | After: L08.10.3

## L08.10.3 Data warehouse design

**Objective.** Explain data warehouse design and show it in the EX-076 output.

**Prerequisites.** L08.10.2

**Lesson.** A warehouse stores trades, prices and positions for reporting. [K]

**Example.** EX-076 (Design an ETRM Data Integration) on synthetic North American data: trades_priced = 2 [EX]

**Do.** `python3 emi.py run 076 | grep '^trades_priced:'`

**Expect.** `trades_priced: 2`

**On the job.** Build a simplified integration connecting trading records, market data, risk calculations, scheduling, and settlement systems.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.10.2 | After: L08.10.4

## L08.10.4 Endur as an enterprise ETRM example

**Objective.** Explain endur as an enterprise ETRM example and show it in the EX-076 output.

**Prerequisites.** L08.10.3

**Lesson.** Endur is one widely used enterprise ETRM; verify capabilities from vendor documentation before citing. [K]

**Example.** EX-076 (Design an ETRM Data Integration) on synthetic North American data: price_coverage_pct = 50 [EX]

**Do.** `python3 emi.py run 076 | grep '^price_coverage_pct:'`

**Expect.** `price_coverage_pct: 50`

**On the job.** Build a simplified integration connecting trading records, market data, risk calculations, scheduling, and settlement systems.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.10.3 | After: L08.10.5

## L08.10.5 Build vs buy and deployment

**Objective.** Explain build vs buy and deployment and show it in the EX-076 output.

**Prerequisites.** L08.10.4

**Lesson.** Build-versus-buy weighs fit, cost, time and upkeep. [K]

**Example.** EX-076 (Design an ETRM Data Integration) on synthetic North American data: integration_breaks = TR002:Algonquin,TR004:Mont_Belvieu [EX]

**Do.** `python3 emi.py run 076 | grep '^integration_breaks:'`

**Expect.** `integration_breaks: TR002:Algonquin,TR004:Mont_Belvieu`

**On the job.** Build a simplified integration connecting trading records, market data, risk calculations, scheduling, and settlement systems.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.10.4 | After: L09.01.1
