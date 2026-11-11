# 6.9 Capacity markets and resource adequacy

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-051 Calculate Capacity Market Economics (`python3 emi.py run 051`). Full output: `exercises/completed/ex051/report.md`.

## L06.09.1 Capacity market design

**Objective.** Explain capacity market design and show it in the EX-051 output.

**Prerequisites.** L06.08.5

**Lesson.** Capacity markets pay resources to be available in future peak periods. [K]

**Example.** EX-051 (Calculate Capacity Market Economics) on synthetic North American data: installed_MW = 1100 [EX]

**Do.** `python3 emi.py run 051 | grep '^installed_MW:'`

**Expect.** `installed_MW: 1100`

**On the job.** Analyze capacity obligations, accreditation, resource adequacy, and capacity revenues.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.08.5 | After: L06.09.2

## L06.09.2 Accreditation and ELCC

**Objective.** Explain accreditation and ELCC and show it in the EX-051 output.

**Prerequisites.** L06.09.1

**Lesson.** Accreditation discounts nameplate to expected availability at peak; ELCC does this for variable resources. [K]

**Example.** EX-051 (Calculate Capacity Market Economics) on synthetic North American data: accredited_MW = 649 [EX]

**Do.** `python3 emi.py run 051 | grep '^accredited_MW:'`

**Expect.** `accredited_MW: 649`

**On the job.** Analyze capacity obligations, accreditation, resource adequacy, and capacity revenues.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.09.1 | After: L06.09.3

## L06.09.3 Demand curves and auction clearing

**Objective.** Explain demand curves and auction clearing and show it in the EX-051 output.

**Prerequisites.** L06.09.2

**Lesson.** A sloped demand curve sets the price where offers meet it. [K]

**Example.** EX-051 (Calculate Capacity Market Economics) on synthetic North American data: fleet_accreditation_pct = 59 [EX]

**Do.** `python3 emi.py run 051 | grep '^fleet_accreditation_pct:'`

**Expect.** `fleet_accreditation_pct: 59`

**On the job.** Analyze capacity obligations, accreditation, resource adequacy, and capacity revenues.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.09.2 | After: L06.09.4

## L06.09.4 Resource adequacy obligations

**Objective.** Explain resource adequacy obligations and show it in the EX-051 output.

**Prerequisites.** L06.09.3

**Lesson.** Load-serving entities must hold capacity equal to peak load plus a reserve margin. [K]

**Example.** EX-051 (Calculate Capacity Market Economics) on synthetic North American data: annual_capacity_revenue_USD = 35532750 [EX]

**Do.** `python3 emi.py run 051 | grep '^annual_capacity_revenue_USD:'`

**Expect.** `annual_capacity_revenue_USD: 35532750`

**On the job.** Analyze capacity obligations, accreditation, resource adequacy, and capacity revenues.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.09.3 | After: L06.09.5

## L06.09.5 Capacity revenue calculation

**Objective.** Explain capacity revenue calculation and show it in the EX-051 output.

**Prerequisites.** L06.09.4

**Lesson.** Capacity revenue is accredited MW times the clearing price times the period. [K]

**Example.** EX-051 (Calculate Capacity Market Economics) on synthetic North American data: obligation_MW = 690 [EX]

**Do.** `python3 emi.py run 051 | grep '^obligation_MW:'`

**Expect.** `obligation_MW: 690`

**On the job.** Analyze capacity obligations, accreditation, resource adequacy, and capacity revenues.

**Product implication.** Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.

Before: L06.09.4 | After: L06.10.1
