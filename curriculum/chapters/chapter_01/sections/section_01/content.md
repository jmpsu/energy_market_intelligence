# 1.1 North American energy industry structure

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-001 Map the North American Energy System (`python3 emi.py run 001`). Full output: `exercises/completed/ex001/report.md`.

## L01.01.1 Upstream, midstream, downstream segments

**Objective.** Explain upstream, midstream, downstream segments and show it in the EX-001 output.

**Prerequisites.** none

**Lesson.** Upstream finds and produces, midstream gathers, processes, moves and stores, downstream delivers to end users. [K]

**Example.** EX-001 (Map the North American Energy System) on synthetic North American data: nodes = 18 [EX]

**Do.** `python3 emi.py run 001 | grep '^nodes:'`

**Expect.** `nodes: 18`

**On the job.** Build a geographic and logical map connecting natural gas production, pipelines, storage, power generation, transmission, and end-use demand.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: None | After: L01.01.2

## L01.01.2 Molecules vs electrons as commodities

**Objective.** Explain molecules vs electrons as commodities and show it in the EX-001 output.

**Prerequisites.** L01.01.1

**Lesson.** Gas and NGLs can be stored and shipped as molecules; electricity must be produced the instant it is used. [K]

**Example.** EX-001 (Map the North American Energy System) on synthetic North American data: links = 19 [EX]

**Do.** `python3 emi.py run 001 | grep '^links:'`

**Expect.** `links: 19`

**On the job.** Build a geographic and logical map connecting natural gas production, pipelines, storage, power generation, transmission, and end-use demand.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.01.1 | After: L01.01.3

## L01.01.3 Regulated vs competitive segments

**Objective.** Explain regulated vs competitive segments and show it in the EX-001 output.

**Prerequisites.** L01.01.2

**Lesson.** Pipelines, wires and utility distribution earn regulated rates; production, generation and trading mostly earn market prices. [K]

**Example.** EX-001 (Map the North American Energy System) on synthetic North American data: gas_to_power_customer_path = Gas_Basin > Gathering > Processing_Plant > Interstate_Pipeline > Gas_Power_Plant > Transmission_Grid > Electric_Utility > Power_Customers [EX]

**Do.** `python3 emi.py run 001 | grep '^gas_to_power_customer_path:'`

**Expect.** `gas_to_power_customer_path: Gas_Basin > Gathering > Processing_Plant > Interstate_Pipeline > Gas_Power_Plant > Transmission_Grid > Electric_Utility > Power_Customers`

**On the job.** Build a geographic and logical map connecting natural gas production, pipelines, storage, power generation, transmission, and end-use demand.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.01.2 | After: L01.01.4

## L01.01.4 Federal, state and provincial jurisdiction

**Objective.** Explain federal, state and provincial jurisdiction and show it in the EX-001 output.

**Prerequisites.** L01.01.3

**Lesson.** FERC regulates interstate transmission and wholesale sales; states and provinces regulate retail, siting and intrastate systems. [K]

**Example.** EX-001 (Map the North American Energy System) on synthetic North American data: path_handoffs = 7 [EX]

**Do.** `python3 emi.py run 001 | grep '^path_handoffs:'`

**Expect.** `path_handoffs: 7`

**On the job.** Build a geographic and logical map connecting natural gas production, pipelines, storage, power generation, transmission, and end-use demand.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.01.3 | After: L01.01.5

## L01.01.5 Reading an industry structure map

**Objective.** Explain reading an industry structure map and show it in the EX-001 output.

**Prerequisites.** L01.01.4

**Lesson.** A structure map shows who hands the commodity to whom; each handoff is a contract, a meter and a data feed. [K]

**Example.** EX-001 (Map the North American Energy System) on synthetic North American data: most_connected_node = Interstate_Pipeline [EX]

**Do.** `python3 emi.py run 001 | grep '^most_connected_node:'`

**Expect.** `most_connected_node: Interstate_Pipeline`

**On the job.** Build a geographic and logical map connecting natural gas production, pipelines, storage, power generation, transmission, and end-use demand.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.01.4 | After: L01.01.6

## L01.01.6 Market participants and roles

**Objective.** Explain market participants and their roles in the energy system.

**Prerequisites.** L01.01.5

**Lesson.** Producers, transporters, storage operators, generators, and consumers each play specific roles in the value chain. [K]

**Example.** EX-001 (Map the North American Energy System) on synthetic North American data: participants_count = 8 [EX]

**Do.** `python3 emi.py run 001 | grep '^participants_count:'`

**Expect.** `participants_count: 8`

**On the job.** Identify and document all key participants in your energy system model.

**Product implication.** A comprehensive model requires participant roles to be clearly defined and mapped.

Before: L01.01.5 | After: L01.01.7

## L01.01.7 Data integrity and validation

**Objective.** Explain data integrity requirements for energy system maps.

**Prerequisites.** L01.01.6

**Lesson.** Data must be validated for completeness, consistency, and accuracy across all segments. [K]

**Example.** EX-001 (Map the North American Energy System) on synthetic North American data: validation_checks = 12 [EX]

**Do.** `python3 emi.py run 001 | grep '^validation_checks:'`

**Expect.** `validation_checks: 12`

**On the job.** Implement automated validation checks for all data inputs.

**Product implication.** Data integrity is critical for reliable market intelligence.

Before: L01.01.6 | After: L01.02.1