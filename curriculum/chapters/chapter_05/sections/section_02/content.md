# 5.2 NGL extraction and recovery

Evidence tags: [S#] = stated in the linked source (curriculum/chapters/chapter_05/sources.md). [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

## L05.02.1 Cryogenic vs lean-oil recovery

**Objective.** Explain how a gas plant extracts NGLs.

**Lesson.** Raw wet gas is cooled and pressurised so the heavier hydrocarbons condense and separate from the gas stream [S3]. Liquids extracted at gas plants are called natural gas plant liquids [S3].

**Example.** Synthetic plant: 200,000 Mcf/d inlet, 979,408 gal/d of liquids in recovery mode.

**Do.** `python3 emi.py run 037`

**Expect.** ngl_gal_per_d: 979407.6

**On the job.** Plant operators choose operating mode daily or monthly; commercial teams tell them which mode pays.

**Product implication.** Plant-level operating mode is a time series the product must store, not a static attribute.

**Before:** L05.01.5 | **Next:** L05.02.2

## L05.02.2 Recovery efficiency by component

**Objective.** Apply component recovery factors.

**Lesson.** A plant recovers a different fraction of each component. Heavier components are recovered almost completely; ethane recovery is the one that swings [S10].

**Example.** Synthetic factors: ethane 85% in recovery mode, 10% in rejection; propane 98% vs 90%.

**Do.** `python3 emi.py run 037 mode=reject`

**Expect.** ngl_bbl_per_d: 12786.86; Ethane_bbl_per_d: 1334.5

**On the job.** Recovery factors are how analysts turn a gas forecast into a product-by-product supply forecast.

**Product implication.** Recovery factors by plant and mode are calibration data: version them and show their source.

**Before:** L05.02.1 | **Next:** L05.02.3

## L05.02.3 Shrink and plant fuel

**Objective.** Compute shrink and its cost.

**Lesson.** Shrink cost = shrink MMBtu x gas price. It is the largest variable cost of making liquids [EX].

**Example.** Recovery mode: 80,968 MMBtu/d x 3.25 = 263,144 USD/d.

**Do.** `python3 emi.py run 037`

**Expect.** shrink_cost_USD_per_d: 263144.38

**On the job.** Shrink links the NGL book to the gas book: long liquids, short gas.

**Product implication.** Cross-commodity exposure (NGL vs gas) must be reportable in one view.

**Before:** L05.02.2 | **Next:** L05.02.4

## L05.02.4 Processing margin (frac spread)

**Objective.** Compute the frac spread (processing margin).

**Lesson.** Frac spread = NGL value per MMBtu of shrink minus gas price. It is the uplift from selling molecules as liquids instead of as gas. Gross: before transport, fractionation and plant fuel [EX].

**Example.** Base: 7.075 - 3.25 = 3.825 USD/MMBtu. Gas at 5.00 cuts it to 2.075.

**Do.** `python3 emi.py run 037 gas_price=5`

**Expect.** frac_spread_USD_per_MMBtu: 2.075042

**On the job.** The frac spread is the single most watched processing-margin indicator.

**Product implication.** A frac-spread calculator with user-set composition is a table-stakes analytics feature.

**Before:** L05.02.3 | **Next:** L05.02.5

## L05.02.5 Recovery optimization

**Objective.** State how contract type decides who bears frac-spread risk.

**Lesson.** Fee-based: processor earns a fee, producer keeps commodity exposure. Percent-of-proceeds: both share NGL and gas price. Keep-whole: processor keeps liquids, returns the Btu as gas, and holds the full frac-spread exposure [K].

**Example.** Under keep-whole the 3.825 USD/MMBtu spread belongs to the processor; a gas spike can turn it negative.

**Do.** `python3 emi.py run 037 gas_price=7.5`

**Expect.** frac_spread_USD_per_MMBtu: -0.424958 (negative: liquids worth less than their gas value)

**On the job.** Knowing a counterparty's contract mix tells you how they will react to prices.

**Product implication.** Contract type must be a field on processing agreements; it changes the exposure calculation.

**Before:** L05.02.4 | **Next:** L05.03.1
