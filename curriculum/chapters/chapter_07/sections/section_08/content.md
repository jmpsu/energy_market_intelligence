# 7.8 Battery storage and state-of-charge constraints

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-063 Simulate Battery Energy Storage Arbitrage (`python3 emi.py run 063`). Full output: `exercises/completed/ex063/report.md`.

## L07.08.1 Battery parameters

**Objective.** Explain battery parameters and show it in the EX-063 output.

**Prerequisites.** L07.07.5

**Lesson.** A battery is defined by power (MW), energy (MWh), efficiency and state-of-charge limits. [K]

**Example.** EX-063 (Simulate Battery Energy Storage Arbitrage) on synthetic North American data: lp_revenue_USD = 17731.111111 [EX]

**Do.** `python3 emi.py run 063 | grep '^lp_revenue_USD:'`

**Expect.** `lp_revenue_USD: 17731.111111`

**On the job.** Optimize battery charging and discharging across hourly electricity prices, accounting for efficiency and capacity limits.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.07.5 | After: L07.08.2

## L07.08.2 State-of-charge dynamics

**Objective.** Explain state-of-charge dynamics and show it in the EX-063 output.

**Prerequisites.** L07.08.1

**Lesson.** State of charge rises with charging and falls with discharging. [K]

**Example.** EX-063 (Simulate Battery Energy Storage Arbitrage) on synthetic North American data: rule_of_thumb_revenue_USD = 13875 [EX]

**Do.** `python3 emi.py run 063 | grep '^rule_of_thumb_revenue_USD:'`

**Expect.** `rule_of_thumb_revenue_USD: 13875`

**On the job.** Optimize battery charging and discharging across hourly electricity prices, accounting for efficiency and capacity limits.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.08.1 | After: L07.08.3

## L07.08.3 Round-trip efficiency

**Objective.** Explain round-trip efficiency and show it in the EX-063 output.

**Prerequisites.** L07.08.2

**Lesson.** Round-trip efficiency is the share of charged energy returned. [K]

**Example.** EX-063 (Simulate Battery Energy Storage Arbitrage) on synthetic North American data: lp_gain_over_rule_USD = 3856.111111 [EX]

**Do.** `python3 emi.py run 063 | grep '^lp_gain_over_rule_USD:'`

**Expect.** `lp_gain_over_rule_USD: 3856.111111`

**On the job.** Optimize battery charging and discharging across hourly electricity prices, accounting for efficiency and capacity limits.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.08.2 | After: L07.08.4

## L07.08.4 Arbitrage optimization

**Objective.** Explain arbitrage optimization and show it in the EX-063 output.

**Prerequisites.** L07.08.3

**Lesson.** Arbitrage charges in cheap hours and discharges in dear ones. [K]

**Example.** EX-063 (Simulate Battery Energy Storage Arbitrage) on synthetic North American data: energy_charged_MWh = 355.555556 [EX]

**Do.** `python3 emi.py run 063 | grep '^energy_charged_MWh:'`

**Expect.** `energy_charged_MWh: 355.555556`

**On the job.** Optimize battery charging and discharging across hourly electricity prices, accounting for efficiency and capacity limits.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.08.3 | After: L07.08.5

## L07.08.5 Ancillary service stacking

**Objective.** Explain ancillary service stacking and show it in the EX-063 output.

**Prerequisites.** L07.08.4

**Lesson.** Batteries stack energy arbitrage with ancillary service revenue. [K]

**Example.** EX-063 (Simulate Battery Energy Storage Arbitrage) on synthetic North American data: energy_discharged_MWh = 320 [EX]

**Do.** `python3 emi.py run 063 | grep '^energy_discharged_MWh:'`

**Expect.** `energy_discharged_MWh: 320`

**On the job.** Optimize battery charging and discharging across hourly electricity prices, accounting for efficiency and capacity limits.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.08.4 | After: L07.09.1
