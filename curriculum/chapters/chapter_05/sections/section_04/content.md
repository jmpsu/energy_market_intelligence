# 5.4 Ethane recovery and rejection

Evidence tags: [S#] = stated in the linked source (curriculum/chapters/chapter_05/sources.md). [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

## L05.04.1 Ethane economics

**Objective.** State what ethane rejection is.

**Lesson.** Unlike the heavier liquids, significant ethane can be left in pipeline gas and sold as gas; this is ethane rejection [S6]. It happens when ethane's price falls to or below its fuel value, or when infrastructure is lacking [S10][S7].

**Example.** EIA: the ethane share of plant liquids production fell from 42% in 2010 to 34% in 2015 [S6].

**Do.** `python3 emi.py run 038`

**Expect.** decision: REJECT

**On the job.** Ethane is the swing barrel of NGL supply: recovery rises and falls with price.

**Product implication.** Supply models need rejection as an explicit, price-driven switch.

**Before:** L05.03.5 | **Next:** L05.04.2

## L05.04.2 Rejection decision rule

**Objective.** Apply the per-gallon rejection rule.

**Lesson.** Recover when hub price - T&F fee > gas price x 0.0665 MMBtu/gal. Simple breakeven ethane price = fuel value + fee [EX].

**Example.** Gas 3.25, fee 0.08: breakeven 0.2961 USD/gal. Market 0.235. Reject.

**Do.** `python3 emi.py run 038`

**Expect.** simple_breakeven_ethane_USD_per_gal: 0.296125

**On the job.** This rule of thumb is quoted daily on NGL desks.

**Product implication.** Expose breakeven as a live derived metric per plant, with the fee assumption visible.

**Before:** L05.04.1 | **Next:** L05.04.3

## L05.04.3 Btu limits on rejection

**Objective.** Extend the rule to the whole plant.

**Lesson.** Rejection mode also loses some propane recovery, so the plant-level breakeven is lower than the simple one [EX]. Residue-gas Btu limits can cap how much ethane a plant may reject [K].

**Example.** Rejection gains 25,695 USD/d on ethane and loses 7,535 USD/d of propane uplift: net 18,160 USD/d. Plant breakeven 0.2782 vs simple 0.2961.

**Do.** `python3 emi.py run 038`

**Expect.** plant_breakeven_ethane_USD_per_gal: 0.2782; rejection_advantage_USD_per_d: 18159.95

**On the job.** Plant optimisation is a whole-barrel decision, not an ethane-only one.

**Product implication.** Models must carry mode-dependent recovery for every component.

**Before:** L05.04.2 | **Next:** L05.04.4

## L05.04.4 Pipeline and frac capacity effects

**Objective.** Recognise when infrastructure, not price, forces the outcome.

**Lesson.** Where ethane pipelines or local markets are missing, recovery is limited regardless of price [S6]. New pipelines, crackers and export docks pull ethane out of rejection [S7].

**Example.** EIA cites the Marcellus and Utica as regions where missing ethane outlets limited recovery [S6].

**Do.** `python3 emi.py run 038 ethane_price=0.30`

**Expect.** decision: RECOVER (price alone flips it; capacity is not modeled)

**On the job.** Basin-level ethane supply forecasts depend on takeaway capacity additions.

**Product implication.** Capacity constraints need to be modeled alongside price logic or the forecast is wrong in constrained basins.

**Before:** L05.04.3 | **Next:** L05.04.5

## L05.04.5 Price signals for rejection

**Objective.** Find the gas price that flips the decision.

**Lesson.** Higher gas price raises ethane's fuel value and pushes plants toward rejection; lower gas price favours recovery [EX]. Rising pipeline-gas heat content is an observable sign of rejection [S6].

**Example.** At ethane 0.235 the plant flips to recovery when gas falls below 2.644 USD/MMBtu.

**Do.** `python3 emi.py run 038 gas_price=2`

**Expect.** decision: RECOVER; rejection_advantage_USD_per_d: -19298.43

**On the job.** Ethane-to-gas ratio is the first chart an ethane trader looks at.

**Product implication.** Alerting on the ethane-gas relationship per basin is a natural monitoring feature.

**Before:** L05.04.4 | **Next:** L05.05.1
