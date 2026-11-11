# 8.2 Trade capture and transaction management

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-069 Build a Trade Capture System (`python3 emi.py run 069`). Full output: `exercises/completed/ex069/report.md`.

## L08.02.1 Trade attributes

**Objective.** Explain trade attributes and show it in the EX-069 output.

**Prerequisites.** L08.01.5

**Lesson.** A trade record holds counterparty, commodity, location, volume, price, term and book. [K]

**Example.** EX-069 (Build a Trade Capture System) on synthetic North American data: submitted = 9 [EX]

**Do.** `python3 emi.py run 069 | grep '^submitted:'`

**Expect.** `submitted: 9`

**On the job.** Create a structured trade record containing commodity, counterparty, location, volume, price, delivery period, and contract type.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.01.5 | After: L08.02.2

## L08.02.2 Deal types and templates

**Objective.** Explain deal types and templates and show it in the EX-069 output.

**Prerequisites.** L08.02.1

**Lesson.** Templates standardise common deal types. [K]

**Example.** EX-069 (Build a Trade Capture System) on synthetic North American data: accepted = 4 [EX]

**Do.** `python3 emi.py run 069 | grep '^accepted:'`

**Expect.** `accepted: 4`

**On the job.** Create a structured trade record containing commodity, counterparty, location, volume, price, delivery period, and contract type.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.02.1 | After: L08.02.3

## L08.02.3 Trade validation

**Objective.** Explain trade validation and show it in the EX-069 output.

**Prerequisites.** L08.02.2

**Lesson.** Validation rejects trades with missing or impossible values at entry. [K]

**Example.** EX-069 (Build a Trade Capture System) on synthetic North American data: rejected = 5 [EX]

**Do.** `python3 emi.py run 069 | grep '^rejected:'`

**Expect.** `rejected: 5`

**On the job.** Create a structured trade record containing commodity, counterparty, location, volume, price, delivery period, and contract type.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.02.2 | After: L08.02.4

## L08.02.4 Amendments and audit trail

**Objective.** Explain amendments and audit trail and show it in the EX-069 output.

**Prerequisites.** L08.02.3

**Lesson.** Amendments create new versions; the audit trail keeps the old ones. [K]

**Example.** EX-069 (Build a Trade Capture System) on synthetic North American data: reject_reasons = TR005:missing_counterparty,TR006:non_positive_volume,TR007:end_before_start,TR008:unknown_commodity,TR009:unit_mismatch [EX]

**Do.** `python3 emi.py run 069 | grep '^reject_reasons:'`

**Expect.** `reject_reasons: TR005:missing_counterparty,TR006:non_positive_volume,TR007:end_before_start,TR008:unknown_commodity,TR009:unit_mismatch`

**On the job.** Create a structured trade record containing commodity, counterparty, location, volume, price, delivery period, and contract type.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.02.3 | After: L08.02.5

## L08.02.5 Trade capture implementation

**Objective.** Explain trade capture implementation and show it in the EX-069 output.

**Prerequisites.** L08.02.4

**Lesson.** Trade capture is the first module every other ETRM function depends on. [K]

**Example.** EX-069 (Build a Trade Capture System) on synthetic North American data: accepted_notional_USD = 2950000 [EX]

**Do.** `python3 emi.py run 069 | grep '^accepted_notional_USD:'`

**Expect.** `accepted_notional_USD: 2950000`

**On the job.** Create a structured trade record containing commodity, counterparty, location, volume, price, delivery period, and contract type.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.02.4 | After: L08.03.1
