# 4.8 LNG liquefaction, shipping, and regasification

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-032 Analyze LNG Feedgas Demand (`python3 emi.py run 032`). Full output: `exercises/completed/ex032/report.md`.

## L04.08.1 Liquefaction process and capacity

**Objective.** Explain liquefaction process and capacity and show it in the EX-032 output.

**Prerequisites.** L04.07.5

**Lesson.** Liquefaction chills gas to a liquid for shipping; capacity is counted per train. [K]

**Example.** EX-032 (Analyze LNG Feedgas Demand) on synthetic North American data: lng_capacity_Bcf_d = 15.8 [EX]

**Do.** `python3 emi.py run 032 | grep '^lng_capacity_Bcf_d:'`

**Expect.** `lng_capacity_Bcf_d: 15.8`

**On the job.** Model how LNG terminal utilization affects domestic natural gas demand and regional pricing.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.07.5 | After: L04.08.2

## L04.08.2 Shipping costs and routes

**Objective.** Explain shipping costs and routes and show it in the EX-032 output.

**Prerequisites.** L04.08.1

**Lesson.** Shipping cost depends on distance, charter rates and boil-off. [K]

**Example.** EX-032 (Analyze LNG Feedgas Demand) on synthetic North American data: feed_gas_Bcf_d = 14.421 [EX]

**Do.** `python3 emi.py run 032 | grep '^feed_gas_Bcf_d:'`

**Expect.** `feed_gas_Bcf_d: 14.421`

**On the job.** Model how LNG terminal utilization affects domestic natural gas demand and regional pricing.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.08.1 | After: L04.08.3

## L04.08.3 Regasification

**Objective.** Explain regasification and show it in the EX-032 output.

**Prerequisites.** L04.08.2

**Lesson.** Regasification terminals return LNG to gas at the destination. [K]

**Example.** EX-032 (Analyze LNG Feedgas Demand) on synthetic North American data: feed_gas_share_of_demand_pct = 13.11 [EX]

**Do.** `python3 emi.py run 032 | grep '^feed_gas_share_of_demand_pct:'`

**Expect.** `feed_gas_share_of_demand_pct: 13.11`

**On the job.** Model how LNG terminal utilization affects domestic natural gas demand and regional pricing.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.08.2 | After: L04.08.4

## L04.08.4 Cargo economics and contracts

**Objective.** Explain cargo economics and contracts and show it in the EX-032 output.

**Prerequisites.** L04.08.3

**Lesson.** A cargo's margin is the sale price less feed gas, liquefaction, shipping and regas. [K]

**Example.** EX-032 (Analyze LNG Feedgas Demand) on synthetic North American data: gulf_share_of_feed_gas_pct = 94.508009 [EX]

**Do.** `python3 emi.py run 032 | grep '^gulf_share_of_feed_gas_pct:'`

**Expect.** `gulf_share_of_feed_gas_pct: 94.508009`

**On the job.** Model how LNG terminal utilization affects domestic natural gas demand and regional pricing.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.08.3 | After: L04.08.5

## L04.08.5 Terminal utilization and feed gas

**Objective.** Explain terminal utilization and feed gas and show it in the EX-032 output.

**Prerequisites.** L04.08.4

**Lesson.** Feed gas demand is terminal capacity times utilisation plus plant fuel. [K]

**Example.** EX-032 (Analyze LNG Feedgas Demand) on synthetic North American data: feed_gas_at_full_utilization_Bcf_d = 17.38 [EX]

**Do.** `python3 emi.py run 032 | grep '^feed_gas_at_full_utilization_Bcf_d:'`

**Expect.** `feed_gas_at_full_utilization_Bcf_d: 17.38`

**On the job.** Model how LNG terminal utilization affects domestic natural gas demand and regional pricing.

**Product implication.** Network and scenario features sell when users can change one constraint and see flows and basis respond.

Before: L04.08.4 | After: L04.09.1
