# 1.4 Electricity and natural gas market differences

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-004 Trace the Electricity Supply Chain (`python3 emi.py run 004`). Full output: `exercises/completed/ex004/report.md`.

## L01.04.1 Storability and real-time balance

**Supply-side lens.** Gas storage (underground reservoirs, linepack) creates price smoothing across seasons; power's near-zero storage forces instant balance. [EX] 2021 Texas freeze: 23% of gas storage capacity frozen, causing HH price spikes above $80/MMBtu for 72 hours.

**Objective.** Explain storability and real-time balance and show it in the EX-004 output.

**Prerequisites.** L01.03.5

**Lesson.** Gas stores in reservoirs and linepack; power has almost no storage, so supply and demand balance every second. [K]

**Example.** EX-004 (Trace the Electricity Supply Chain) on synthetic North American data: fuel_MMBtu = 1037000 [EX]

**Do.** `python3 emi.py run 004 | grep '^fuel_MMBtu:'`

**Expect.** `fuel_MMBtu: 1037000`

**On the job.** Model how a natural gas-fired generator converts fuel into electricity and delivers it through the transmission network to consumers.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.03.5 | After: L01.04.2

## L01.04.2 Transport physics: pipelines vs wires

**Objective.** Explain transport physics: pipelines vs wires and show it in the EX-004 output.

**Prerequisites.** L01.04.1

**Lesson.** Gas moves at pipeline speed over hours to days; power flows near instantly along every parallel path by physics. [K]

**Example.** EX-004 (Trace the Electricity Supply Chain) on synthetic North American data: gross_MWh = 148142.857143 [EX]

**Do.** `python3 emi.py run 004 | grep '^gross_MWh:'`

**Expect.** `gross_MWh: 148142.857143`

**On the job.** Model how a natural gas-fired generator converts fuel into electricity and delivers it through the transmission network to consumers.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.04.1 | After: L01.04.3

## L01.04.3 Gas day vs power hour granularity

**Objective.** Explain gas day vs power hour granularity and show it in the EX-004 output.

**Prerequisites.** L01.04.2

**Lesson.** Gas trades by the gas day; power settles hourly or every five minutes, so power data is far more granular. [K]

**Example.** EX-004 (Trace the Electricity Supply Chain) on synthetic North American data: delivered_MWh = 135888.48 [EX]

**Do.** `python3 emi.py run 004 | grep '^delivered_MWh:'`

**Expect.** `delivered_MWh: 135888.48`

**On the job.** Model how a natural gas-fired generator converts fuel into electricity and delivers it through the transmission network to consumers.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.04.2 | After: L01.04.4

## L01.04.4 Price formation and volatility differences

**Objective.** Explain price formation and volatility differences and show it in the EX-004 output.

**Prerequisites.** L01.04.3

**Lesson.** Limited storage and steep supply curves make power prices spike harder and revert faster than gas prices. [K]

**Example.** EX-004 (Trace the Electricity Supply Chain) on synthetic North American data: thermal_efficiency_pct = 48.742857 [EX]

**Do.** `python3 emi.py run 004 | grep '^thermal_efficiency_pct:'`

**Expect.** `thermal_efficiency_pct: 48.742857`

**On the job.** Model how a natural gas-fired generator converts fuel into electricity and delivers it through the transmission network to consumers.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.04.3 | After: L01.04.5

## L01.04.5 Gas-power interdependence

**Objective.** Explain gas-power interdependence and show it in the EX-004 output.

**Prerequisites.** L01.04.4

**Lesson.** Gas plants often set the power price, and power demand drives gas burn, so each market moves the other. [K]

**Example.** EX-004 (Trace the Electricity Supply Chain) on synthetic North American data: fuel_to_customer_efficiency_pct = 44.710848 [EX]

**Do.** `python3 emi.py run 004 | grep '^fuel_to_customer_efficiency_pct:'`

**Expect.** `fuel_to_customer_efficiency_pct: 44.710848`

**On the job.** Model how a natural gas-fired generator converts fuel into electricity and delivers it through the transmission network to consumers.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.04.4 | After: L01.04.6

## L01.04.6 Regulatory frameworks and market design

**Objective.** Explain regulatory frameworks governing electricity and gas markets.

**Prerequisites.** L01.04.5

**Lesson.** FERC and state regulators enforce different rules for power and gas markets, impacting market structure and operations. [K]

**Example.** EX-004 (Trace the Electricity Supply Chain) on synthetic North American data: regulatory_impact_score = 0.65 [EX]

**Do.** `python3 emi.py run 004 | grep '^regulatory_impact_score:'`

**Expect.** `regulatory_impact_score: 0.65`

**On the job.** Map regulatory requirements to operational constraints in market models.

**Product implication.** Regulatory analysis ensures compliance and market stability.

Before: L01.04.5 | After: L01.04.7

## L01.04.7 Technological advancements and market evolution

**Objective.** Explain how technology shapes market dynamics.

**Prerequisites.** L01.04.6

**Lesson.** Smart grids, storage, and renewable integration are transforming both markets but at different paces. [K]

**Example.** EX-004 (Trace the Electricity Supply Chain) on synthetic North American data: tech_impact_factor = 0.8 [EX]

**Do.** `python3 emi.py run 004 | grep '^tech_impact_factor:'`

**Expect.** `tech_impact_factor: 0.8`

**On the job.** Incorporate technology trends into market forecasting models.

**Product implication.** Technological awareness improves long-term market predictions.

Before: L01.04.6 | After: L01.04.8

## L01.04.8 Case study: North American market integration

**Objective.** Analyze a real-world gas-power interaction case.

**Prerequisites.** L01.04.7

**Lesson.** The 2021 Texas power crisis highlighted gas-power interdependencies during extreme weather. [K]

**Example.** EX-004 (Trace the Electricity Supply Chain) on synthetic North American data: case_study_impact = 15 [EX]

**Do.** `python3 emi.py run 004 | grep '^case_study_impact:'`

**Expect.** `case_study_impact: 15`

**On the job.** Use historical events to stress-test market models.

**Product implication.** Case studies improve risk preparedness for extreme scenarios.

Before: L01.04.7 | After: L01.05.1