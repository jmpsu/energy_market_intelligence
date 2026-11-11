# 3.1 Henry Hub and benchmark pricing

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-019 Calculate Regional Gas Basis (`python3 emi.py run 019`). Full output: `exercises/completed/ex019/report.md`.

## L03.01.1 Henry Hub as benchmark

**Objective.** Explain henry Hub as benchmark and show it in the EX-019 output.

**Prerequisites.** L02.10.5

**Lesson.** Henry Hub in Louisiana is the delivery point of the main US gas futures contract and the pricing reference for most deals. [K]

**Example.** EX-019 (Calculate Regional Gas Basis) on synthetic North American data: Waha_basis_day1 = -2.15 [EX]

**Do.** `python3 emi.py run 019 | grep '^Waha_basis_day1:'`

**Expect.** `Waha_basis_day1: -2.15`

**On the job.** Compare Henry Hub with Waha, AECO, Dawn, Algonquin Citygate, and other regional pricing locations.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L02.10.5 | After: L03.01.2

## L03.01.2 NYMEX NG contract specification

**Objective.** Explain nYMEX NG contract specification and show it in the EX-019 output.

**Prerequisites.** L03.01.1

**Lesson.** The contract is a standard monthly volume in MMBtu for physical delivery at the hub. [K]

**Example.** EX-019 (Calculate Regional Gas Basis) on synthetic North American data: AECO_basis_day1 = -1.1 [EX]

**Do.** `python3 emi.py run 019 | grep '^AECO_basis_day1:'`

**Expect.** `AECO_basis_day1: -1.1`

**On the job.** Compare Henry Hub with Waha, AECO, Dawn, Algonquin Citygate, and other regional pricing locations.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.01.1 | After: L03.01.3

## L03.01.3 Settlement and expiry mechanics

**Objective.** Explain settlement and expiry mechanics and show it in the EX-019 output.

**Prerequisites.** L03.01.2

**Lesson.** Trading in a month ends shortly before delivery; the final settlement price is widely used in indices. [K]

**Example.** EX-019 (Calculate Regional Gas Basis) on synthetic North American data: Dawn_basis_day1 = -0.45 [EX]

**Do.** `python3 emi.py run 019 | grep '^Dawn_basis_day1:'`

**Expect.** `Dawn_basis_day1: -0.45`

**On the job.** Compare Henry Hub with Waha, AECO, Dawn, Algonquin Citygate, and other regional pricing locations.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.01.2 | After: L03.01.4

## L03.01.4 Prompt month and price reporting

**Objective.** Explain prompt month and price reporting and show it in the EX-019 output.

**Prerequisites.** L03.01.3

**Lesson.** The prompt month is the nearest contract; published prices come from exchanges and price reporting agencies. [K]

**Example.** EX-019 (Calculate Regional Gas Basis) on synthetic North American data: Chicago_basis_day1 = -0.15 [EX]

**Do.** `python3 emi.py run 019 | grep '^Chicago_basis_day1:'`

**Expect.** `Chicago_basis_day1: -0.15`

**On the job.** Compare Henry Hub with Waha, AECO, Dawn, Algonquin Citygate, and other regional pricing locations.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.01.3 | After: L03.01.5

## L03.01.5 Benchmark limits as a regional proxy

**Objective.** Explain benchmark limits as a regional proxy and show it in the EX-019 output.

**Prerequisites.** L03.01.4

**Lesson.** Henry Hub does not tell you the price in a constrained region; that is what basis measures. [K]

**Example.** EX-019 (Calculate Regional Gas Basis) on synthetic North American data: Henry_Hub_basis_day1 = 0 [EX]

**Do.** `python3 emi.py run 019 | grep '^Henry_Hub_basis_day1:'`

**Expect.** `Henry_Hub_basis_day1: 0`

**On the job.** Compare Henry Hub with Waha, AECO, Dawn, Algonquin Citygate, and other regional pricing locations.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.01.4 | After: L03.02.1
