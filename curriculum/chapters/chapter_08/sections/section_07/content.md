# 8.7 Settlements and reconciliation

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-052 Model Electricity Market Settlements (`python3 emi.py run 052`). Full output: `exercises/completed/ex052/report.md`.

## L08.07.1 Invoice generation

**Objective.** Explain invoice generation and show it in the EX-052 output.

**Prerequisites.** L08.06.5

**Lesson.** Invoices are generated from actual volumes and contract prices. [K]

**Example.** EX-052 (Model Electricity Market Settlements) on synthetic North American data: day_ahead_energy_USD = 21000 [EX]

**Do.** `python3 emi.py run 052 | grep '^day_ahead_energy_USD:'`

**Expect.** `day_ahead_energy_USD: 21000`

**On the job.** Calculate the financial difference between scheduled quantities, actual generation, and market settlement prices.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.06.5 | After: L08.07.2

## L08.07.2 Price and volume checks

**Objective.** Explain price and volume checks and show it in the EX-052 output.

**Prerequisites.** L08.07.1

**Lesson.** Price and volume are checked against the counterparty's statement. [K]

**Example.** EX-052 (Model Electricity Market Settlements) on synthetic North American data: real_time_deviation_USD = 1800 [EX]

**Do.** `python3 emi.py run 052 | grep '^real_time_deviation_USD:'`

**Expect.** `real_time_deviation_USD: 1800`

**On the job.** Calculate the financial difference between scheduled quantities, actual generation, and market settlement prices.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.07.1 | After: L08.07.3

## L08.07.3 Netting

**Objective.** Explain netting and show it in the EX-052 output.

**Prerequisites.** L08.07.2

**Lesson.** Netting offsets amounts owed both ways. [K]

**Example.** EX-052 (Model Electricity Market Settlements) on synthetic North American data: ancillary_services_USD = 795 [EX]

**Do.** `python3 emi.py run 052 | grep '^ancillary_services_USD:'`

**Expect.** `ancillary_services_USD: 795`

**On the job.** Calculate the financial difference between scheduled quantities, actual generation, and market settlement prices.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.07.2 | After: L08.07.4

## L08.07.4 Dispute handling

**Objective.** Explain dispute handling and show it in the EX-052 output.

**Prerequisites.** L08.07.3

**Lesson.** Disputes are logged, investigated and resolved under contract terms. [K]

**Example.** EX-052 (Model Electricity Market Settlements) on synthetic North American data: shadow_total_USD = 23595 [EX]

**Do.** `python3 emi.py run 052 | grep '^shadow_total_USD:'`

**Expect.** `shadow_total_USD: 23595`

**On the job.** Calculate the financial difference between scheduled quantities, actual generation, and market settlement prices.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.07.3 | After: L08.07.5

## L08.07.5 Settlement reconciliation

**Objective.** Explain settlement reconciliation and show it in the EX-052 output.

**Prerequisites.** L08.07.4

**Lesson.** Settlement reconciliation ties invoices to cash. [K]

**Example.** EX-052 (Model Electricity Market Settlements) on synthetic North American data: average_cost_USD_per_MWh = 44.518868 [EX]

**Do.** `python3 emi.py run 052 | grep '^average_cost_USD_per_MWh:'`

**Expect.** `average_cost_USD_per_MWh: 44.518868`

**On the job.** Calculate the financial difference between scheduled quantities, actual generation, and market settlement prices.

**Product implication.** ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.

Before: L08.07.4 | After: L08.08.1
