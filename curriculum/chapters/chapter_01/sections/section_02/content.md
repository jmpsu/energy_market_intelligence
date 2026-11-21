# 1.2 Energy market participants and commercial relationships

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-002 Identify Market Participants (`python3 emi.py run 002`). Full output: `exercises/completed/ex002/report.md`.

## L01.02.1 Producers and processors

**Objective.** Explain producers and processors and show it in the EX-002 output.

**Prerequisites.** L01.01.5

**Lesson.** Producers sell commodity-price exposure; processors turn raw gas into residue gas and NGLs for a fee or a share. [K]

**Example.** EX-002 (Identify Market Participants) on synthetic North American data: participant_types = 12 [EX]

**Do.** `python3 emi.py run 002 | grep '^participant_types:'`

**Expect.** `participant_types: 12`

**On the job.** Create a structured dataset of producers, utilities, generators, pipelines, ISOs, RTOs, marketers, traders, and regulators; classify their commercial roles.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.01.5 | After: L01.02.2

## L01.02.2 Pipelines, storage operators and LDCs

**Objective.** Explain pipelines, storage operators and LDCs and show it in the EX-002 output.

**Prerequisites.** L01.02.1

**Lesson.** Pipelines and storage sell capacity under tariffs; LDCs buy gas and deliver it to homes and businesses at regulated rates. [K]

**Example.** EX-002 (Identify Market Participants) on synthetic North American data: full_price_risk_takers = Producer,Independent_Power_Producer,Marketer_Trader,Financial_Counterparty [EX]

**Do.** `python3 emi.py run 002 | grep '^full_price_risk_takers:'`

**Expect.** `full_price_risk_takers: Producer,Independent_Power_Producer,Marketer_Trader,Financial_Counterparty`

**On the job.** Create a structured dataset of producers, utilities, generators, pipelines, ISOs, RTOs, marketers, traders, and regulators; classify their commercial roles.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.02.1 | After: L01.02.3

## L01.02.3 Generators, utilities and load-serving entities

**Objective.** Explain generators, utilities and load-serving entities and show it in the EX-002 output.

**Prerequisites.** L01.02.2

**Lesson.** Generators sell energy, capacity and ancillary services; load-serving entities buy them to meet customer demand. [K]

**Example.** EX-002 (Identify Market Participants) on synthetic North American data: rate_regulated = Interstate_Pipeline,LDC_Gas_Utility,Vertically_Integrated_Utility,ISO_RTO [EX]

**Do.** `python3 emi.py run 002 | grep '^rate_regulated:'`

**Expect.** `rate_regulated: Interstate_Pipeline,LDC_Gas_Utility,Vertically_Integrated_Utility,ISO_RTO`

**On the job.** Create a structured dataset of producers, utilities, generators, pipelines, ISOs, RTOs, marketers, traders, and regulators; classify their commercial roles.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.02.2 | After: L01.02.4

## L01.02.4 Marketers, traders and financial counterparties

**Objective.** Explain marketers, traders and financial counterparties and show it in the EX-002 output.

**Prerequisites.** L01.02.3

**Lesson.** Marketers and traders connect buyers and sellers and warehouse risk; financial counterparties provide hedges without touching the molecule. [K]

**Example.** EX-002 (Identify Market Participants) on synthetic North American data: fee_earners_without_price_risk = Interstate_Pipeline,Storage_Operator,NGL_Fractionator,ISO_RTO [EX]

**Do.** `python3 emi.py run 002 | grep '^fee_earners_without_price_risk:'`

**Expect.** `fee_earners_without_price_risk: Interstate_Pipeline,Storage_Operator,NGL_Fractionator,ISO_RTO`

**On the job.** Create a structured dataset of producers, utilities, generators, pipelines, ISOs, RTOs, marketers, traders, and regulators; classify their commercial roles.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.02.3 | After: L01.02.5

## L01.02.5 Contract chains between participants

**Objective.** Explain contract chains between participants and show it in the EX-002 output.

**Prerequisites.** L01.02.4

**Lesson.** One delivered molecule sits under a chain of contracts: purchase, gathering, processing, transport, storage, sale. [K]

**Example.** EX-002 (Identify Market Participants) on synthetic North American data: etrm_users = Independent_Power_Producer,Vertically_Integrated_Utility,Marketer_Trader [EX]

**Do.** `python3 emi.py run 002 | grep '^etrm_users:'`

**Expect.** `etrm_users: Independent_Power_Producer,Vertically_Integrated_Utility,Marketer_Trader`

**On the job.** Create a structured dataset of producers, utilities, generators, pipelines, ISOs, RTOs, marketers, traders, and regulators; classify their commercial roles.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.02.4 | After: L01.02.6

## L01.02.6 Regulatory frameworks and compliance

**Objective.** Explain regulatory frameworks governing market participants.

**Prerequisites.** L01.02.5

**Lesson.** FERC, state regulators, and international bodies enforce rules on market conduct, pricing, and operational standards. [K]

**Example.** EX-002 (Identify Market Participants) on synthetic North American data: compliance_entities = FERC,State_Regulators [EX]

**Do.** `python3 emi.py run 002 | grep '^compliance_entities:'`

**Expect.** `compliance_entities: FERC,State_Regulators`

**On the job.** Map regulatory requirements to each participant type in your system.

**Product implication.** Compliance data is essential for risk management and audit readiness.

Before: L01.02.5 | After: L01.02.7

## L01.02.7 Data management and integration

**Objective.** Explain data management needs for participant tracking.

**Prerequisites.** L01.02.6

**Lesson.** Participant data must be integrated with transaction, contract, and operational datasets. [K]

**Example.** EX-002 (Identify Market Participants) on synthetic North American data: data_integrations = 4 [EX]

**Do.** `python3 emi.py run 002 | grep '^data_integrations:'`

**Expect.** `data_integrations: 4`

**On the job.** Design data pipelines connecting participant databases to analytics systems.

**Product implication.** Integrated data enables comprehensive market analysis.

Before: L01.02.6 | After: L01.02.8

## L01.02.8 Risk mitigation strategies

**Objective.** Explain risk mitigation strategies for market participants.

**Prerequisites.** L01.02.7

**Lesson.** Hedging, diversification, and contractual safeguards reduce exposure to price, credit, and operational risks. [K]

**Example.** EX-002 (Identify Market Participants) on synthetic North American data: risk_mitigation_tools = Futures_Options,Swaps,Netting_Agreements [EX]

**Do.** `python3 emi.py run 002 | grep '^risk_mitigation_tools:'`

**Expect.** `risk_mitigation_tools: Futures_Options,Swaps,Netting_Agreements`

**On the job.** Document risk management practices for each participant type.

**Product implication.** Risk profiles inform product design and pricing models.

Before: L01.02.7 | After: L01.03.1