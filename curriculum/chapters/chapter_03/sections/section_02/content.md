# 3.2 Regional hubs and location basis

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-019 Calculate Regional Gas Basis (`python3 emi.py run 019`). Full output: `exercises/completed/ex019/report.md`.

## L03.02.1 Basis definition and sign convention

**Objective.** Explain basis definition and sign convention and show it in the EX-019 output.

**Prerequisites.** L03.01.5

**Lesson.** Basis is the local price minus Henry Hub; negative means the location is cheaper. [K]

**Example.** EX-019 (Calculate Regional Gas Basis) on synthetic North American data: Waha_basis_day1 = -2.15 [EX]

**Do.** `python3 emi.py run 019 | grep '^Waha_basis_day1:'`

**Expect.** `Waha_basis_day1: -2.15`

**On the job.** Compare Henry Hub with Waha, AECO, Dawn, Algonquin Citygate, and other regional pricing locations.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.01.5 | After: L03.02.2

## L03.02.2 Supply-area vs market-area basis

**Objective.** Explain supply-area vs market-area basis and show it in the EX-019 output.

**Prerequisites.** L03.02.1

**Lesson.** Supply areas with excess gas trade at a discount, market areas with tight delivery at a premium. [K]

**Example.** EX-019 (Calculate Regional Gas Basis) on synthetic North American data: AECO_basis_day1 = -1.1 [EX]

**Do.** `python3 emi.py run 019 | grep '^AECO_basis_day1:'`

**Expect.** `AECO_basis_day1: -1.1`

**On the job.** Compare Henry Hub with Waha, AECO, Dawn, Algonquin Citygate, and other regional pricing locations.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.02.1 | After: L03.02.3

## L03.02.3 Negative prices at constrained hubs

**Objective.** Explain negative prices at constrained hubs and show it in the EX-019 output.

**Prerequisites.** L03.02.2

**Lesson.** A hub with no spare takeaway can trade below zero: sellers pay to dispose of gas. [K]

**Example.** EX-019 (Calculate Regional Gas Basis) on synthetic North American data: Dawn_basis_day1 = -0.45 [EX]

**Do.** `python3 emi.py run 019 | grep '^Dawn_basis_day1:'`

**Expect.** `Dawn_basis_day1: -0.45`

**On the job.** Compare Henry Hub with Waha, AECO, Dawn, Algonquin Citygate, and other regional pricing locations.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.02.2 | After: L03.02.4

## L03.02.4 Basis volatility and seasonality

**Objective.** Explain basis volatility and seasonality and show it in the EX-019 output.

**Prerequisites.** L03.02.3

**Lesson.** Basis is seasonal and can be more volatile than the benchmark itself. [K]

**Example.** EX-019 (Calculate Regional Gas Basis) on synthetic North American data: Chicago_basis_day1 = -0.15 [EX]

**Do.** `python3 emi.py run 019 | grep '^Chicago_basis_day1:'`

**Expect.** `Chicago_basis_day1: -0.15`

**On the job.** Compare Henry Hub with Waha, AECO, Dawn, Algonquin Citygate, and other regional pricing locations.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.02.3 | After: L03.02.5

## L03.02.5 Basis position P&L

**Objective.** Explain basis position P&L and show it in the EX-019 output.

**Prerequisites.** L03.02.4

**Lesson.** Basis P&L is position times the change in basis, independent of the Henry Hub move. [K]

**Example.** EX-019 (Calculate Regional Gas Basis) on synthetic North American data: Henry_Hub_basis_day1 = 0 [EX]

**Do.** `python3 emi.py run 019 | grep '^Henry_Hub_basis_day1:'`

**Expect.** `Henry_Hub_basis_day1: 0`

**On the job.** Compare Henry Hub with Waha, AECO, Dawn, Algonquin Citygate, and other regional pricing locations.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.02.4 | After: L03.03.1
