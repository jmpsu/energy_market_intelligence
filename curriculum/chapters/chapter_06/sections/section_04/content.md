# 6.4 Vertically integrated and bilateral markets

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-046 Compare ISO/RTO and Bilateral Markets (`python3 emi.py run 046`). Full output: `exercises/completed/ex046/report.md`.

## L06.04.1 Southeast and Western bilateral markets

**Objective.** Explain southeast and Western bilateral markets and show it in the EX-046 output.

**Prerequisites.** L06.03.5

**Lesson.** Outside ISOs, utilities self-schedule and trade bilaterally. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: iso_spot_seller = 42 [EX]

**Do.** `python3 emi.py run 046 | grep '^iso_spot_seller:'`

**Expect.** `iso_spot_seller: 42`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.03.5 | After: L06.04.2

## L06.04.2 Utility integrated resource planning

**Objective.** Explain utility integrated resource planning and show it in the EX-046 output.

**Prerequisites.** L06.04.1

**Lesson.** Integrated resource plans decide what those utilities build or contract. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: bilateral_physical_with_wheeling_seller = 45 [EX]

**Do.** `python3 emi.py run 046 | grep '^bilateral_physical_with_wheeling_seller:'`

**Expect.** `bilateral_physical_with_wheeling_seller: 45`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.04.1 | After: L06.04.3

## L06.04.3 Bilateral trading hubs

**Objective.** Explain bilateral trading hubs and show it in the EX-046 output.

**Prerequisites.** L06.04.2

**Lesson.** Bilateral power trades at named hubs. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: iso_plus_cfd_at_gen_node_seller = 45 [EX]

**Do.** `python3 emi.py run 046 | grep '^iso_plus_cfd_at_gen_node_seller:'`

**Expect.** `iso_plus_cfd_at_gen_node_seller: 45`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.04.2 | After: L06.04.4

## L06.04.4 Transmission service and OASIS

**Objective.** Explain transmission service and OASIS and show it in the EX-046 output.

**Prerequisites.** L06.04.3

**Lesson.** Transmission service is reserved through each provider's OASIS site. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: iso_plus_cfd_at_load_node_seller = 39 [EX]

**Do.** `python3 emi.py run 046 | grep '^iso_plus_cfd_at_load_node_seller:'`

**Expect.** `iso_plus_cfd_at_load_node_seller: 39`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.04.3 | After: L06.04.5

## L06.04.5 Emerging day-ahead market initiatives

**Objective.** Explain emerging day-ahead market initiatives and show it in the EX-046 output.

**Prerequisites.** L06.04.4

**Lesson.** Western day-ahead market initiatives are extending organized trading into bilateral regions. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: iso_spot_buyer = 48 [EX]

**Do.** `python3 emi.py run 046 | grep '^iso_spot_buyer:'`

**Expect.** `iso_spot_buyer: 48`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.04.4 | After: L06.05.1
