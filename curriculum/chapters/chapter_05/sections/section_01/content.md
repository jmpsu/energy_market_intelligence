# 5.1 Natural gas liquids and hydrocarbon composition

Evidence tags: [S#] = stated in the linked source (curriculum/chapters/chapter_05/sources.md). [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

## L05.01.1 NGL component properties

**Objective.** Name the five NGL purity products and place each on the carbon ladder.

**Lesson.** NGLs are ethane (C2), propane (C3), normal butane and isobutane (C4) and natural gasoline or pentanes-plus (C5+) [S1]. EIA groups them with refinery olefins as hydrocarbon gas liquids (HGL) [S1]. Heavier molecule = more Btu per gallon, more pounds per gallon, higher price per gallon [EX].

**Example.** In data/synthetic/ngl_components.csv ethane carries 0.0665 MMBtu/gal and natural gasoline 0.1100 MMBtu/gal (rounded engineering factors).

**Do.** `cat data/synthetic/ngl_components.csv`

**Expect.** Five rows, C2 to C5+, MMBtu_per_gal and lb_per_gal rising down the table.

**On the job.** Every NGL report you will read is organised by these five products; a number without the product name is unusable.

**Product implication.** Product is a mandatory dimension on every price, volume and position record.

**Before:** L04.10.5 | **Next:** L05.01.2

## L05.01.2 Gallons per Mcf (GPM)

**Objective.** Convert a gas analysis in mol% to gallons per Mcf (GPM).

**Lesson.** GPM = mol% x a component factor (gal per Mcf per mol%). Summed over C2+ it measures how rich (wet) the gas is [K]. Rich gas means more liquids revenue per Mcf processed.

**Example.** Synthetic inlet gas: 10.5% C2, 5.0% C3, 0.7% iC4, 1.5% nC4, 1.3% C5+ gives 5.3519 GPM.

**Do.** `python3 emi.py run 037`

**Expect.** theoretical_gpm: 5.3519

**On the job.** Producers and processors quote gas richness in GPM when negotiating processing deals and forecasting plant liquids.

**Product implication.** A composition table per meter or plant inlet is core reference data; GPM is derived, never typed in.

**Before:** L05.01.1 | **Next:** L05.01.3

## L05.01.3 Btu content and value

**Objective.** Convert recovered gallons to shrink in MMBtu and to fuel value.

**Lesson.** Liquids removed from the gas stream take their Btu with them: shrink (MMBtu) = gallons x MMBtu/gal. Fuel value per gallon = MMBtu/gal x gas price. That is what the molecule is worth if left in the gas [EX].

**Example.** At 3.25 USD/MMBtu, ethane fuel value = 0.0665 x 3.25 = 0.2161 USD/gal; propane = 0.0915 x 3.25 = 0.2974 USD/gal.

**Do.** `python3 emi.py run 037`

**Expect.** shrink_MMBtu_per_d: 80967.50

**On the job.** Shrink is the gas the plant owner must make whole or account for in settlement statements.

**Product implication.** Settlement and P&L need both a gallon ledger and an MMBtu ledger that reconcile.

**Before:** L05.01.2 | **Next:** L05.01.4

## L05.01.4 Purity vs mixed products

**Objective.** Distinguish purity products from mixed streams.

**Lesson.** Fractionators separate mixed NGLs into purity products that are at least 90% one molecule [S3]. LPG is a mix of propane and butanes; Y-grade is the unfractionated mix leaving the gas plant [S4][S9].

**Example.** EX-039 values one Y-grade barrel (40% ethane by volume) at 28.05 USD at Mont Belvieu purity prices.

**Do.** `python3 emi.py run 039`

**Expect.** purity_value_USD_per_barrel: 28.0518

**On the job.** Deals are struck on either a mixed barrel or purity basis; confusing the two misprices the trade.

**Product implication.** A stream entity (composition + volume) must be distinct from a product entity in the data model.

**Before:** L05.01.3 | **Next:** L05.01.5

## L05.01.5 Composition analysis

**Objective.** Read a composition analysis and compute the barrel a plant will make.

**Lesson.** Barrels per day by product = inlet Mcf/d x GPM x recovery / 42. Ethane dominates volume but not value [EX].

**Example.** 200,000 Mcf/d plant in full recovery: 23,319 bbl/d, 48.6% of it ethane.

**Do.** `python3 emi.py run 037 inlet_Mcf_per_d=300000`

**Expect.** ngl_bbl_per_d: 34978.84 (1.5x the base 23319.23)

**On the job.** Supply forecasting starts here: gas volume forecast x composition x recovery = NGL supply.

**Product implication.** Supply forecast features need gas-volume inputs linked to plant composition and recovery assumptions.

**Before:** L05.01.4 | **Next:** L05.02.1
