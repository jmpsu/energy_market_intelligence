# 5.9 Fractionation, Mont Belvieu, and Conway

Evidence tags: [S#] = stated in the linked source (curriculum/chapters/chapter_05/sources.md). [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

## L05.09.1 Fractionation process

**Objective.** Describe fractionation.

**Lesson.** Fractionators split mixed NGLs into purity products [S3]. Capacity can run full, which backs barrels up and widens differentials [S9].

**Example.** EX-039: frac fee 0.07 USD/gal on a 42-gallon barrel is 2.94 USD/bbl.

**Do.** `python3 emi.py run 039`

**Expect.** cost_USD_per_barrel: 26.04

**On the job.** Frac capacity utilisation is a leading indicator for Y-grade discounts.

**Product implication.** Capacity and utilisation series per hub are essential market data.

**Before:** L05.08.5 | **Next:** L05.09.2

## L05.09.2 Mont Belvieu hub

**Objective.** Characterise Mont Belvieu.

**Lesson.** Mont Belvieu, Texas is the larger of the two main US NGL hubs for trading, storage and fractionation, serving Gulf Coast and export demand [S9]. Several Mont Belvieu propane price assessments exist (non-TET, TET/LST) [S15][S12].

**Example.** Synthetic Mont Belvieu propane: 0.720 then 0.750 USD/gal.

**Do.** `python3 emi.py run 040`

**Expect.** 2026-01-12_Propane_profit_USD: 33000

**On the job.** Always ask which Belvieu price a contract references.

**Product implication.** Price series need a precise location and assessment identifier, not just Mont Belvieu.

**Before:** L05.09.1 | **Next:** L05.09.3

## L05.09.3 Conway hub

**Objective.** Characterise Conway.

**Lesson.** Conway, Kansas is the smaller hub, with far less storage than Mont Belvieu [S9][S14]. Constraints tend to hit the smaller Conway hub harder [K].

**Example.** EIA data cited by RBN: about 18% of US NGL volumes moved to or through Conway in 2023 [S9].

**Do.** `python3 emi.py run 040`

**Expect.** Conway is below Mont Belvieu for every product on both synthetic dates.

**On the job.** Conway is the Midcontinent price marker; its spread to Belvieu is a traded relationship.

**Product implication.** Hub attributes (storage, frac capacity, connectivity) are reference data users expect.

**Before:** L05.09.2 | **Next:** L05.09.4

## L05.09.4 Regional basis

**Objective.** Compute regional basis.

**Lesson.** Basis = Mont Belvieu - Conway. The spread usually reflects transport cost but blows out under constraints or cold weather, and can invert [S15][S12].

**Example.** Synthetic propane basis: 0.065 then 0.090 USD/gal. OPIS: Conway propane traded above Belvieu from September to December 2022 [S12].

**Do.** `python3 emi.py run 044`

**Expect.** propane_basis_move_USD_per_gal: 0.025

**On the job.** Basis is where most NGL trading P&L is made and lost.

**Product implication.** Basis must be computed from two dated, sourced prices; show both legs.

**Before:** L05.09.3 | **Next:** L05.09.5

## L05.09.5 Arbitrage economics

**Objective.** Decide whether the arbitrage is open.

**Lesson.** Ship when basis exceeds transport plus handling. Net margin = basis - logistics cost [EX].

**Example.** Logistics 0.057 USD/gal. Propane on 2026-01-12: 0.090 - 0.057 = 0.033, or 33,000 USD on 1,000,000 gal. Ethane never clears.

**Do.** `python3 emi.py run 040`

**Expect.** products_never_positive: Ethane; best_shipment: 2026-01-12 Propane

**On the job.** Marketers run this screen every day for every product.

**Product implication.** An arbitrage screen with editable costs is a daily-use feature.

**Before:** L05.09.4 | **Next:** L05.10.1
