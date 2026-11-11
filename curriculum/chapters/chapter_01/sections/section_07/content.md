# 1.7 Bilateral and organized wholesale markets

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-046 Compare ISO/RTO and Bilateral Markets (`python3 emi.py run 046`). Full output: `exercises/completed/ex046/report.md`.

## L01.07.1 Bilateral contracting mechanics

**Objective.** Explain bilateral contracting mechanics and show it in the EX-046 output.

**Prerequisites.** L01.06.5

**Lesson.** A bilateral deal is negotiated between two parties and needs transmission arranged separately in non-ISO regions. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: iso_spot_seller = 42 [EX]

**Do.** `python3 emi.py run 046 | grep '^iso_spot_seller:'`

**Expect.** `iso_spot_seller: 42`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.06.5 | After: L01.07.2

## L01.07.2 Centrally cleared organized markets

**Objective.** Explain centrally cleared organized markets and show it in the EX-046 output.

**Prerequisites.** L01.07.1

**Lesson.** Organized markets clear all bids and offers centrally and settle against published prices. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: bilateral_physical_with_wheeling_seller = 45 [EX]

**Do.** `python3 emi.py run 046 | grep '^bilateral_physical_with_wheeling_seller:'`

**Expect.** `bilateral_physical_with_wheeling_seller: 45`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.07.1 | After: L01.07.3

## L01.07.3 OTC vs exchange execution

**Objective.** Explain oTC vs exchange execution and show it in the EX-046 output.

**Prerequisites.** L01.07.2

**Lesson.** OTC trades are customised and carry counterparty credit risk; exchange trades are standard and cleared. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: iso_plus_cfd_at_gen_node_seller = 45 [EX]

**Do.** `python3 emi.py run 046 | grep '^iso_plus_cfd_at_gen_node_seller:'`

**Expect.** `iso_plus_cfd_at_gen_node_seller: 45`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.07.2 | After: L01.07.4

## L01.07.4 Clearing, margin and credit support

**Objective.** Explain clearing, margin and credit support and show it in the EX-046 output.

**Prerequisites.** L01.07.3

**Lesson.** Clearing replaces counterparty risk with margin: initial margin up front, variation margin daily. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: iso_plus_cfd_at_load_node_seller = 39 [EX]

**Do.** `python3 emi.py run 046 | grep '^iso_plus_cfd_at_load_node_seller:'`

**Expect.** `iso_plus_cfd_at_load_node_seller: 39`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.07.3 | After: L01.07.5

## L01.07.5 Price discovery across market forms

**Objective.** Explain price discovery across market forms and show it in the EX-046 output.

**Prerequisites.** L01.07.4

**Lesson.** Price discovery is strongest where trading is concentrated: liquid hubs, exchanges and ISO markets. [K]

**Example.** EX-046 (Compare ISO/RTO and Bilateral Markets) on synthetic North American data: iso_spot_buyer = 48 [EX]

**Do.** `python3 emi.py run 046 | grep '^iso_spot_buyer:'`

**Expect.** `iso_spot_buyer: 48`

**On the job.** Model differences between centrally organized wholesale markets and bilateral electricity transactions.

**Product implication.** A market-intelligence product needs one reference model of participants, locations and units before any analytics.

Before: L01.07.4 | After: L01.08.1
