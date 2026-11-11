# 6.2 RTO and ISO operating models

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-046 Compare ISO/RTO and Bilateral Markets (`python3 emi.py run 046`). Full output: `exercises/completed/ex046/report.md`.

## L06.02.1 ISO core functions

**Objective.** Explain iSO core functions and show it in the EX-046 output.

**Prerequisites.** L06.01.5

**Lesson.** An ISO dispatches generation, runs markets, manages transmission and settles participants. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: iso_spot_seller = 42 [EX]

**Do.** `python3 emi.py run 046 | grep '^iso_spot_seller:'`

**Expect.** `iso_spot_seller: 42`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.01.5 | After: L06.02.2

## L06.02.2 Market operations timeline

**Objective.** Explain market operations timeline and show it in the EX-046 output.

**Prerequisites.** L06.02.1

**Lesson.** Operations follow a daily timeline: bids, day-ahead clearing, reliability commitment, real-time dispatch, settlement. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: bilateral_physical_with_wheeling_seller = 45 [EX]

**Do.** `python3 emi.py run 046 | grep '^bilateral_physical_with_wheeling_seller:'`

**Expect.** `bilateral_physical_with_wheeling_seller: 45`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.02.1 | After: L06.02.3

## L06.02.3 Reliability coordination

**Objective.** Explain reliability coordination and show it in the EX-046 output.

**Prerequisites.** L06.02.2

**Lesson.** Reliability coordination keeps flows within limits and manages emergencies. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: iso_plus_cfd_at_gen_node_seller = 45 [EX]

**Do.** `python3 emi.py run 046 | grep '^iso_plus_cfd_at_gen_node_seller:'`

**Expect.** `iso_plus_cfd_at_gen_node_seller: 45`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.02.2 | After: L06.02.4

## L06.02.4 Transmission planning role

**Objective.** Explain transmission planning role and show it in the EX-046 output.

**Prerequisites.** L06.02.3

**Lesson.** ISOs plan regional transmission expansion. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: iso_plus_cfd_at_load_node_seller = 39 [EX]

**Do.** `python3 emi.py run 046 | grep '^iso_plus_cfd_at_load_node_seller:'`

**Expect.** `iso_plus_cfd_at_load_node_seller: 39`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.02.3 | After: L06.02.5

## L06.02.5 Stakeholder governance

**Objective.** Explain stakeholder governance and show it in the EX-046 output.

**Prerequisites.** L06.02.4

**Lesson.** Rules change through stakeholder committees and regulator approval. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: iso_spot_buyer = 48 [EX]

**Do.** `python3 emi.py run 046 | grep '^iso_spot_buyer:'`

**Expect.** `iso_spot_buyer: 48`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.02.4 | After: L06.03.1
