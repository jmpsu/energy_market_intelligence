# 10.3 Power-flow and production-cost simulation

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-089 Create a Power Market Simulation (`python3 emi.py run 089`). Full output: `exercises/completed/ex089/report.md`.

## L10.03.1 AC vs DC power flow

**Objective.** Explain aC vs DC power flow and show it in the EX-089 output.

**Prerequisites.** L10.02.5

**Lesson.** AC power flow is exact and nonlinear; DC is approximate and fast. [K]

**Example.** EX-089 (Create a Power Market Simulation) on synthetic North American data: total_demand_MWh = 105600 [EX]

**Do.** `python3 emi.py run 089 | grep '^total_demand_MWh:'`

**Expect.** `total_demand_MWh: 105600`

**On the job.** Build a simplified production-cost model that dispatches generators against hourly demand and operating constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.02.5 | After: L10.03.2

## L10.03.2 Production-cost model structure

**Objective.** Explain production-cost model structure and show it in the EX-089 output.

**Prerequisites.** L10.03.1

**Lesson.** A production-cost model dispatches units to meet load at least cost. [K]

**Example.** EX-089 (Create a Power Market Simulation) on synthetic North American data: total_production_cost_USD = 3214768.834064 [EX]

**Do.** `python3 emi.py run 089 | grep '^total_production_cost_USD:'`

**Expect.** `total_production_cost_USD: 3214768.834064`

**On the job.** Build a simplified production-cost model that dispatches generators against hourly demand and operating constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.03.1 | After: L10.03.3

## L10.03.3 Chronological simulation

**Objective.** Explain chronological simulation and show it in the EX-089 output.

**Prerequisites.** L10.03.2

**Lesson.** Chronological simulation keeps hours in order so storage and ramps work. [K]

**Example.** EX-089 (Create a Power Market Simulation) on synthetic North American data: average_cost_USD_per_MWh = 30.442887 [EX]

**Do.** `python3 emi.py run 089 | grep '^average_cost_USD_per_MWh:'`

**Expect.** `average_cost_USD_per_MWh: 30.442887`

**On the job.** Build a simplified production-cost model that dispatches generators against hourly demand and operating constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.03.2 | After: L10.03.4

## L10.03.4 Reserve and outage modeling

**Objective.** Explain reserve and outage modeling and show it in the EX-089 output.

**Prerequisites.** L10.03.3

**Lesson.** Reserves and outages reduce usable capacity. [K]

**Example.** EX-089 (Create a Power Market Simulation) on synthetic North American data: load_weighted_price_USD_per_MWh = 53.232538 [EX]

**Do.** `python3 emi.py run 089 | grep '^load_weighted_price_USD_per_MWh:'`

**Expect.** `load_weighted_price_USD_per_MWh: 53.232538`

**On the job.** Build a simplified production-cost model that dispatches generators against hourly demand and operating constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.03.3 | After: L10.03.5

## L10.03.5 Running a production-cost simulation

**Objective.** Explain running a production-cost simulation and show it in the EX-089 output.

**Prerequisites.** L10.03.4

**Lesson.** A run is defined by inputs, horizon and resolution. [K]

**Example.** EX-089 (Create a Power Market Simulation) on synthetic North American data: peak_price = 65 [EX]

**Do.** `python3 emi.py run 089 | grep '^peak_price:'`

**Expect.** `peak_price: 65`

**On the job.** Build a simplified production-cost model that dispatches generators against hourly demand and operating constraints.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.03.4 | After: L10.04.1
