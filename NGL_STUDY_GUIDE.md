# NGL study guide (Chapter 5)

Evidence tags: [S#] = stated in the linked source (curriculum/chapters/chapter_05/sources.md). [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

All prices, volumes and plant data are synthetic and hypothetical unless a sentence carries an [S#] tag.

## Order of study

1. Sections 5.1-5.2 + labs 037
2. Sections 5.3-5.4 + labs 038, 039
3. Sections 5.5-5.6 + labs 041, 042
4. Sections 5.7-5.9 + lab 040
5. Section 5.10 + labs 043, 044, then rerun every completion test unaided

## Formula sheet (as used in the code)

| Quantity | Formula |
|---|---|
| Barrel | 1 bbl = 42 gal |
| Richness | GPM = mol% x gal/Mcf-per-mol% factor |
| Plant liquids | gal/d = inlet Mcf/d x GPM x recovery |
| Shrink | MMBtu = gal x MMBtu/gal |
| Fuel value | USD/gal = MMBtu/gal x gas price |
| Frac spread | NGL value / shrink MMBtu - gas price |
| Netback | hub price - T&F fee |
| Ethane rule | recover if price - fee > gas x 0.0665 |
| Basis | Mont Belvieu - Conway |
| Arbitrage | basis - transport - handling |
| Y-grade barrel | 42 x sum(fraction x purity price) |
| Inventory | opening + (production - demand - exports) x days |
| Days of supply | inventory / (demand + exports) |
| Feed cost | c/lb = USD/gal x 100 / lb per gal; per lb ethylene = / yield |
| Cracker margin | ethylene - feed cost + co-product credit - conversion |
| MtM | signed gal x (mark - trade price) |
| Spread P&L | net gal x Conway move + Belvieu gal x basis move |

## Factors used (rounded engineering approximations [K]; contracts use GPA Midstream standards)

| Product | gal/Mcf per mol% | MMBtu/gal | lb/gal |
|---|---|---|---|
| Ethane | 0.2669 | 0.0665 | 2.97 |
| Propane | 0.2749 | 0.0915 | 4.22 |
| Isobutane | 0.3265 | 0.0996 | 4.69 |
| Normal butane | 0.3146 | 0.1037 | 4.87 |
| Natural gasoline | 0.3650 | 0.1100 | 5.50 |

# 5.1 Natural gas liquids and hydrocarbon composition


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

# 5.2 NGL extraction and recovery


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

# 5.3 Y-grade and mixed NGL transportation


## L05.03.1 Y-grade definition

**Objective.** Define Y-grade.

**Lesson.** Y-grade is the mixed NGL stream from a gas plant, either fractionated locally or piped long distance to a hub [S9].

**Example.** EX-039 Y-grade: 40% ethane, 28% propane, 11% nC4, 7% iC4, 14% C5+ by volume.

**Do.** `cat data/synthetic/ex039_ygrade.csv`

**Expect.** Five fractions summing to 1.00.

**On the job.** Most barrels leave the plant as Y-grade; purity products appear only after the fractionator.

**Product implication.** Volume records need a composition attached or they cannot be valued.

**Before:** L05.02.5 | **Next:** L05.03.2

## L05.03.2 Y-grade pipelines

**Objective.** List how NGLs move.

**Lesson.** HGLs move as mixtures or as purity products by pipeline, rail, truck, ship and barge [S4].

**Example.** EX-043 moves 100,000 bbl over pipeline, rail, truck and marine arcs.

**Do.** `python3 emi.py run 043`

**Expect.** base_total_cost_USD: 246500; base_avg_cost_USD_per_bbl: 2.465

**On the job.** Logistics schedulers pick the mode; marketers price the differential it creates.

**Product implication.** Mode, capacity and cost per arc are the minimum logistics data model.

**Before:** L05.03.1 | **Next:** L05.03.3

## L05.03.3 Transport and fractionation fees

**Objective.** Add transport and fractionation (T&F) fees to get a plant netback.

**Lesson.** Netback at the plant = hub price - T&F fee. The fee is paid per gallon whether or not the product is worth it [EX].

**Example.** Ethane 0.235 at the hub less 0.08 T&F = 0.155 USD/gal netback, below its 0.2161 fuel value.

**Do.** `python3 emi.py run 038`

**Expect.** ethane_netback_USD_per_gal: 0.155

**On the job.** Producers are paid on netbacks, not hub prices; every statement shows the deduction.

**Product implication.** Fee schedules by contract are required inputs to any netback or margin screen.

**Before:** L05.03.2 | **Next:** L05.03.4

## L05.03.4 Quality and batching

**Objective.** Explain why mixed streams need quality tracking.

**Lesson.** A Y-grade barrel's value depends on its composition. The same price per gallon on two streams with different ethane content is a different deal [EX].

**Example.** EX-039: ethane is 40% of the volume but 14.1% of the value.

**Do.** `python3 emi.py run 039`

**Expect.** ethane_volume_share_pct: 40; ethane_value_share_pct: 14.073963

**On the job.** Quality disputes at custody transfer are settled on the component analysis.

**Product implication.** Store measured composition per ticket; compute value from it.

**Before:** L05.03.3 | **Next:** L05.03.5

## L05.03.5 Logistics constraints

**Objective.** Quantify a logistics constraint.

**Lesson.** When the cheapest arc is cut, barrels move to costlier modes or are stranded. The extra cost per barrel of lost capacity is what that capacity is worth [EX].

**Example.** Halving the Conway to Mont Belvieu pipeline raises cost by 73,750 USD (3.28 USD per barrel of lost capacity) and puts 2,500 bbl on trucks. A full outage strands 5,000 bbl at Conway.

**Do.** `python3 emi.py run 043 outage_arc=A1 outage_frac=1`

**Expect.** outage_feasible: False; stranded_at_Conway_bbl: 5000

**On the job.** Constraint value is the argument for (or against) signing a pipeline commitment.

**Product implication.** Constraint what-if is a high-value simulation workflow; show cost and stranded volume together.

**Before:** L05.03.4 | **Next:** L05.04.1

# 5.4 Ethane recovery and rejection


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

# 5.5 Ethane and petrochemical markets


## L05.05.1 Ethane as cracker feedstock

**Objective.** State what ethane is used for.

**Lesson.** Ethane is a key petrochemical feedstock, recovered at gas plants and cracked to ethylene [S7][S1].

**Example.** EX-042 cracker: 3,300 million lb/yr ethylene needs about 92,900 bbl/d of ethane at the assumed yield.

**Do.** `python3 emi.py run 042`

**Expect.** ethane_feed_bbl_per_d_at_capacity: 92922.47

**On the job.** Cracker operating rates and outages move ethane demand by tens of thousands of barrels a day.

**Product implication.** Demand-side data (cracker capacity, outages) is as important as supply data.

**Before:** L05.04.5 | **Next:** L05.05.2

## L05.05.2 Ethylene margin

**Objective.** Convert ethane price per gallon to feed cost per pound of ethylene.

**Lesson.** cents/lb feed = price/gal x 100 / lb/gal. cents/lb ethylene = that / yield [EX]. Yield and density here are synthetic single-number assumptions.

**Example.** 0.235 USD/gal / 2.97 lb/gal = 7.91 c/lb; / 0.78 yield = 10.14 c/lb of ethylene.

**Do.** `python3 emi.py run 042`

**Expect.** Ethane_feed_cost_c_per_lb_ethylene: 10.144177

**On the job.** Petrochemical buyers think in cents per pound; NGL sellers in cents per gallon. You translate.

**Product implication.** Unit conversion must be built in and auditable.

**Before:** L05.05.1 | **Next:** L05.05.3

## L05.05.3 Feedstock switching

**Objective.** Compute the cracker cash margin.

**Lesson.** Margin = ethylene price - feed cost + co-product credit - conversion cost [EX].

**Example.** 22.0 - 10.14 + 1.0 - 4.0 = 8.86 c/lb; about 292 million USD/yr at capacity.

**Do.** `python3 emi.py run 042`

**Expect.** Ethane_margin_c_per_lb_ethylene: 8.855823

**On the job.** Margin sets how much a cracker can pay for ethane before cutting rates or switching feed.

**Product implication.** Margin models are the demand-side analogue of the frac spread.

**Before:** L05.05.2 | **Next:** L05.05.4

## L05.05.4 Export demand

**Objective.** Compare feedstocks.

**Lesson.** Flexible crackers choose the feed with the best margin. Heavier feeds yield less ethylene but more co-products [K].

**Example.** Synthetic case: ethane 8.86 vs propane -3.62 c/lb, a 12.48 c/lb ethane advantage.

**Do.** `python3 emi.py run 042 ethylene_price=30`

**Expect.** Propane_margin_c_per_lb_ethylene: 4.377116; preferred_feed: Ethane

**On the job.** Feed switching links ethane and propane prices.

**Product implication.** Scenario tools should let users vary yields and credits, not hard-code them.

**Before:** L05.05.3 | **Next:** L05.05.5

## L05.05.5 Margin sensitivity

**Objective.** Find the ethane price ceiling a cracker tolerates.

**Lesson.** Breakeven feed price is where margin is zero. Between the plant's rejection breakeven (floor) and the cracker's breakeven (ceiling) lies the range ethane can trade in [EX]. Exports add a second demand outlet [S7].

**Example.** Cracker breakeven 0.440 USD/gal vs plant recovery breakeven 0.278 USD/gal.

**Do.** `python3 emi.py run 042 ethane_price=0.35`

**Expect.** Ethane_margin_c_per_lb_ethylene: 3.891652

**On the job.** This floor-and-ceiling frame is how ethane price forecasts are argued.

**Product implication.** A price-band view combining supply and demand breakevens is a differentiating analytic.

**Before:** L05.05.4 | **Next:** L05.06.1

# 5.6 Propane pricing, storage, and seasonality


## L05.06.1 Propane demand sectors

**Objective.** List propane's demand sectors.

**Lesson.** Propane has consumer (mainly fuel) and non-consumer (feedstock) markets [S2]. US supply exceeds domestic use; exports take the balance [S5].

**Example.** Synthetic balance: exports are 67% of production.

**Do.** `python3 emi.py run 041`

**Expect.** export_share_of_production_pct: 67.241379

**On the job.** Know which demand is weather-driven (heating, crop drying) and which is price-driven (petchem, export).

**Product implication.** Demand must be segmented by sector in the data model.

**Before:** L05.05.5 | **Next:** L05.06.2

## L05.06.2 Inventory cycle

**Objective.** Build the seasonal inventory cycle.

**Lesson.** Heating demand drives a seasonal cycle [S5]: inventory builds in the warm months and draws in winter (the month shape here is synthetic). Ending inventory = opening + (production - demand - exports) x days [EX].

**Example.** Synthetic: build 52.88 MMbbl to a 97.88 MMbbl peak in September, draw 49.75 MMbbl.

**Do.** `python3 emi.py run 041`

**Expect.** peak_inventory_MMbbl: 97.88; peak_month: Sep

**On the job.** The weekly inventory report is the propane market's main scheduled data event.

**Product implication.** Balance models must be reproducible from published series with clear units (MMb/d vs MMbbl).

**Before:** L05.06.1 | **Next:** L05.06.3

## L05.06.3 Export pull

**Objective.** Measure tightness in days of supply.

**Lesson.** Days of supply = inventory / daily disappearance. The same inventory is tighter when exports are higher [EX].

**Example.** Base minimum 15.5 days. Add 0.10 MMb/d of exports all year: ending inventory 11.63 MMbbl, 3.8 days.

**Do.** `python3 emi.py run 041 export_shift=0.10`

**Expect.** base_ending_inventory_MMbbl: 11.63; min_days_of_supply_base: 3.751613

**On the job.** Days of supply is the number retailers and regulators ask about before winter.

**Product implication.** Show inventory and days-of-supply side by side; one without the other misleads.

**Before:** L05.06.2 | **Next:** L05.06.4

## L05.06.4 Price ratio to crude

**Objective.** Quantify export pull.

**Lesson.** US propane exports averaged 2.0 million b/d in the first half of 2026, a record, with 2.1 million b/d in April [S8]. Exports respond to US-versus-overseas price spreads and dock capacity [S8].

**Example.** EIA reports US exports to China fell 28% in 2025 after tariffs while shipments to India and South Asia rose [S8].

**Do.** `python3 emi.py run 041 export_shift=-0.10`

**Expect.** base_ending_inventory_MMbbl: 84.63 (base 48.13): lower exports loosen the balance.

**On the job.** Export economics now set the marginal price of US propane.

**Product implication.** Dock capacity, freight and overseas prices belong in the propane model.

**Before:** L05.06.3 | **Next:** L05.06.5

## L05.06.5 Seasonal spread

**Objective.** Stress the balance with a cold winter.

**Lesson.** A 20% rise in December to February demand is enough to breach an operating minimum [EX]. Regional shortages can occur before the national number looks tight [K].

**Example.** Cold case: extra draw 25.23 MMbbl, inventory 22.9 MMbbl versus a 30 MMbbl floor, breached in February and March.

**Do.** `python3 emi.py run 041`

**Expect.** cold_winter_min_inventory_MMbbl: 22.9; cold_winter_months_below_minimum: Feb,Mar

**On the job.** Winter-readiness analysis is done every autumn by marketers and retailers.

**Product implication.** Scenario runs on the balance are a core user workflow; make the assumptions editable.

**Before:** L05.06.4 | **Next:** L05.07.1

# 5.7 Butane and isobutane markets


## L05.07.1 Blending demand and RVP season

**Objective.** State what butanes are used for.

**Lesson.** Normal butane and isobutane are mostly gasoline blendstocks and petrochemical or refinery feedstocks [S2].

**Example.** EX-044 holds 800,000 gal of normal butane at Conway and 400,000 gal of isobutane at Mont Belvieu.

**Do.** `python3 emi.py run 044`

**Expect.** P5_pnl_USD: 12000; P6_pnl_USD: 12000

**On the job.** Butane desks sit between the NGL and gasoline markets.

**Product implication.** Cross-links to refined-product prices are needed for butane analytics.

**Before:** L05.06.5 | **Next:** L05.07.2

## L05.07.2 Isomerization

**Objective.** Explain butane's seasonality.

**Lesson.** More butane is blended into gasoline in colder months, when vapour-pressure rules allow it [S5]. So butane demand, like propane, is winter-weighted, for a different reason.

**Example.** EIA lists gasoline blending alongside heating as a driver of the seasonal HGL demand cycle [S5].

**Do.** `grep -i butane data/synthetic/ngl_regional_prices.csv`

**Expect.** Four rows: Normal_Butane and Isobutane on two dates.

**On the job.** Blending-season start and end dates are trading events.

**Product implication.** Calendar features (blending seasons) belong in forecasting models.

**Before:** L05.07.1 | **Next:** L05.07.3

## L05.07.3 Alkylation feed

**Objective.** Distinguish isobutane.

**Lesson.** Isobutane comes from gas plants and refineries or is made from normal butane by isomerisation; it feeds alkylation, which makes high-octane gasoline components [S2].

**Example.** Synthetic prices: isobutane 1.020 vs normal butane 0.890 USD/gal at Mont Belvieu, a 0.13 premium.

**Do.** `python3 emi.py run 040`

**Expect.** Isobutane net margin: 0.013 then 0.028 USD/gal.

**On the job.** The iso-normal spread signals whether isomerisation units run.

**Product implication.** Spread series between related products should be first-class objects.

**Before:** L05.07.2 | **Next:** L05.07.4

## L05.07.4 Storage and logistics

**Objective.** Relate butane to crude.

**Lesson.** Because of its gasoline use, butane prices tend to follow oil prices [S11]. Traders quote heavier NGLs as a percentage of crude [S12].

**Example.** OPIS reported Mont Belvieu normal butane at about 60.7% of WTI in early 2023 [S12].

**Do.** `python3 emi.py run 039`

**Expect.** Normal_Butane contributes 4.11 USD of the 28.05 USD barrel.

**On the job.** Ratio-to-crude is the standard way to judge whether a heavy NGL is cheap or rich.

**Product implication.** Ratio analytics need a crude price series in the same store.

**Before:** L05.07.3 | **Next:** L05.07.5

## L05.07.5 Butane spreads

**Objective.** Mark a butane position.

**Lesson.** MtM = signed gallons x (mark - trade price) [EX].

**Example.** P5: long 800,000 gal normal butane at Conway at 0.830; mark 0.825 then 0.840: -4,000 then +8,000 USD.

**Do.** `python3 emi.py run 044`

**Expect.** P5_pnl_USD: 12000

**On the job.** Daily marking by product and hub is the base of every NGL risk report.

**Product implication.** Hub is part of the instrument key: Conway butane and Belvieu butane are different risks.

**Before:** L05.07.4 | **Next:** L05.08.1

# 5.8 Natural gasoline and product specifications


## L05.08.1 Natural gasoline uses

**Objective.** Define natural gasoline.

**Lesson.** Natural gasoline is pentanes-plus: C5 and heavier [S1][S13].

**Example.** It is 9.7% of the synthetic plant's barrels in recovery mode.

**Do.** `python3 emi.py run 037`

**Expect.** Natural_Gasoline_bbl_per_d: 2259.52

**On the job.** It is the highest-priced NGL per gallon and the closest to crude.

**Product implication.** Naming varies (C5+, pentanes-plus, natural gasoline): the product needs an alias table.

**Before:** L05.07.5 | **Next:** L05.08.2

## L05.08.2 Diluent demand

**Objective.** State its uses.

**Lesson.** Natural gasoline is used as a gasoline blendstock and as an ethanol denaturant [S13]. It is also used as diluent for heavy crude [K].

**Example.** EIA shows 0.17 million b/d of US natural gasoline exports in 2022 [S5].

**Do.** `grep Natural_Gasoline data/synthetic/ngl_regional_prices.csv`

**Expect.** Two rows: 1.450 and 1.480 USD/gal at Mont Belvieu.

**On the job.** Demand follows gasoline blending and Canadian heavy-oil output.

**Product implication.** Diluent flows tie the NGL model to Canadian crude data.

**Before:** L05.08.1 | **Next:** L05.08.3

## L05.08.3 Product specifications

**Objective.** See why it dominates barrel value.

**Lesson.** Value share = volume share x price. A small volume at a high price carries the barrel [EX].

**Example.** EX-039: 14% of volume but 8.53 of the 28.05 USD barrel (30.4%), the largest value component.

**Do.** `python3 emi.py run 039`

**Expect.** largest_value_component: Natural_Gasoline

**On the job.** When crude falls, the heavy end drags the whole NGL barrel down.

**Product implication.** Barrel-value attribution by component is a standard chart.

**Before:** L05.08.2 | **Next:** L05.08.4

## L05.08.4 Pricing vs crude

**Objective.** Price it against crude.

**Lesson.** The heavy NGLs track crude [S11]; commentary quotes C5+ moves alongside crude moves [K].

**Example.** EX-044 is short 500,000 gal: a 0.03 USD/gal rise costs 15,000 USD.

**Do.** `python3 emi.py run 044`

**Expect.** P4_pnl_USD: -15000

**On the job.** Hedging natural gasoline often uses crude instruments, leaving basis risk.

**Product implication.** Proxy-hedge tracking (NGL vs crude) is a risk-reporting requirement.

**Before:** L05.08.3 | **Next:** L05.08.5

## L05.08.5 Quality differentials

**Objective.** Apply specifications.

**Lesson.** Purity products must meet composition specifications; off-spec product is discounted or rejected [K]. Purity means at least 90% of one molecule [S3].

**Example.** Not modeled in this repo: no exercise applies a specification test.

**Do.** `cat data/synthetic/ex039_ygrade.csv`

**Expect.** Composition only; no spec limits present.

**On the job.** Quality claims are a routine back-office dispute.

**Product implication.** Gap to note: spec limits per product per pipeline are data the model lacks.

**Before:** L05.08.4 | **Next:** L05.09.1

# 5.9 Fractionation, Mont Belvieu, and Conway


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

# 5.10 NGL transportation, exports, trading, and risk


## L05.10.1 Transport modes

**Objective.** Choose a transport mode.

**Lesson.** Pipeline is cheapest per barrel but capacity-limited; rail, truck and marine fill the gap at higher cost [S4][EX].

**Example.** Synthetic costs per bbl: pipeline 1.50 to 1.90, rail 3.20 to 6.00, marine 4.00, truck 7.00.

**Do.** `python3 emi.py run 043`

**Expect.** base_arcs_at_capacity: A1,A5 (both pipelines full)

**On the job.** Logistics cost is the floor under regional differentials.

**Product implication.** Optimisation needs arc capacities and costs maintained as dated reference data.

**Before:** L05.09.5 | **Next:** L05.10.2

## L05.10.2 Export terminals

**Objective.** Follow export flows.

**Lesson.** The US exported about 2.4 million b/d of HGL in 2022, 1.40 million b/d of it propane [S5]. Propane hit a record 2.1 million b/d in April 2026 [S8]. Growth could be capped by export capacity [S8].

**Example.** EIA: Panama Canal costs on shipments to Asia must be absorbed by buyers and sellers [S8].

**Do.** `python3 emi.py run 041 export_shift=0.10`

**Expect.** base_ending_inventory_MMbbl: 11.63

**On the job.** Export dock capacity and freight are price drivers for the whole US propane market.

**Product implication.** Waterborne data (docks, freight, destinations) is a product-coverage decision.

**Before:** L05.10.1 | **Next:** L05.10.3

## L05.10.3 NGL hedging instruments

**Objective.** Mark an NGL book.

**Lesson.** Mark each position at its product and hub price; sum to book MtM; difference day to day is P&L [EX].

**Example.** Six positions: MtM 26,500 USD on day 1, 118,000 on day 2, P&L 91,500.

**Do.** `python3 emi.py run 044`

**Expect.** weekly_pnl_USD: 91500

**On the job.** This is the daily routine of an NGL risk analyst.

**Product implication.** Position, price and P&L must tie exactly: reconciliation is an acceptance test.

**Before:** L05.10.2 | **Next:** L05.10.4

## L05.10.4 Portfolio exposure

**Objective.** Split P&L into flat price and basis.

**Lesson.** For a long-Belvieu, short-Conway propane spread: P&L = net gallons x Conway move + Belvieu gallons x basis move [EX].

**Example.** Net long 500,000 gal: 2,500 USD flat price + 50,000 USD basis = 52,500.

**Do.** `python3 emi.py run 044`

**Expect.** propane_flat_price_pnl_USD: 2500; propane_basis_pnl_USD: 50000

**On the job.** Attribution tells the desk head whether the trader made money on the view they were paid to take.

**Product implication.** P&L explain by risk factor is a standard ETRM report to replicate.

**Before:** L05.10.3 | **Next:** L05.10.5

## L05.10.5 Risk controls

**Objective.** Name the risks an NGL book carries.

**Lesson.** Outright price, hub basis, product spreads (for example ethane vs gas, butane vs crude), volume and operational risk, and proxy-hedge basis when hedging with gas or crude [EX][K].

**Example.** Net position 100,000 bbl long; gross notional 5.06 million USD; largest P&L product is propane.

**Do.** `python3 emi.py run 044`

**Expect.** net_position_bbl: 100000; gross_notional_USD: 5057000

**On the job.** Limits are set on each of these dimensions.

**Product implication.** Risk views must slice by product, hub and tenor; this repo has no tenor dimension yet.

**Before:** L05.10.4 | **Next:** L06.01.1

# Labs

## Lab EX-037: NGL composition and recovery

**Scenario.** Supply analyst at a gas processor. A 200,000 Mcf/d plant needs a product-by-product liquids forecast and a processing-margin estimate for the monthly commercial review.

**Decision.** How many barrels of each product will the plant make, and what is the gross frac spread?

**Model.** GPM = mol% x factor. gal/d = inlet x GPM x recovery. bbl = gal / 42. shrink MMBtu = gal x MMBtu/gal. frac spread = NGL value / shrink - gas price.

**Code.** exercises/scripts/ex037.py | **Test.** exercises/tests (python3 emi.py test)

**Run (from the repo root).**

```
python3 emi.py run 037
python3 emi.py run 037 mode=reject
python3 emi.py run 037 gas_price=7.5
cat exercises/completed/ex037/ngl_recovery.csv
```

**Reference output of the first command (synthetic).**

```
ex037 | SYNTHETIC HYPOTHETICAL DATA - not historical market data
mode: recover
theoretical_gpm: 5.3519
recovered_gpm: 4.897038
ngl_gal_per_d: 979407.6
ngl_bbl_per_d: 23319.228571
shrink_MMBtu_per_d: 80967.50303
ngl_value_USD_per_d: 572848.4935
shrink_cost_USD_per_d: 263144.384848
gross_frac_spread_USD_per_d: 309704.108652
ngl_value_USD_per_MMBtu: 7.075042
frac_spread_USD_per_MMBtu: 3.825042
weighted_price_USD_per_gal: 0.584893
Ethane_bbl_per_d: 11343.25
Propane_bbl_per_d: 6414.333333
Isobutane_bbl_per_d: 1077.45
Normal_Butane_bbl_per_d: 2224.671429
Natural_Gasoline_bbl_per_d: 2259.52381
ethane_barrel_share_pct: 48.643333
NOTE: Conversion factors (gal/Mcf per mol%, MMBtu/gal, lb/gal) are rounded engineering approximations; contracts use GPA Midstream standards. C5+ uses one factor for the whole pentanes-plus cut.
NOTE: Gross frac spread ignores plant fuel, transport and fractionation fees, and the processing contract split (fee, POP, keep-whole).
```

**Questions.** Answer before reading the key.

1. Ethane is 48.6% of the barrels. What share of the value is it?
2. In rejection mode barrels fall to 12,787 bbl/d but the frac spread per MMBtu rises from 3.83 to 5.73. Why?
3. At gas 7.50 the average frac spread is -0.42. Should the plant stop recovering everything?
4. Which inputs are assumptions rather than measurements?

**Completion test.** Edit data/synthetic/ngl_components.csv: set ethane mol_pct to 6.0. Predict theoretical GPM before running (5.3519 - 4.5 x 0.2669 = 4.15085). Run, confirm, restore 10.5.

**Answer key.**

1. 476,416.5 gal x 0.235 = 111,958 USD of 572,848 USD: 19.5%.
2. The barrels removed are ethane, the lowest-value component per MMBtu. The remaining barrel is richer per MMBtu of shrink. Per-MMBtu spread is not total dollars.
3. No. Check each component: ethane fuel value 0.499 > 0.235 price (reject); propane fuel value 0.686 < 0.720 (recover). An average hides the component decision.
4. Conversion factors, recovery factors, one price date, no fees. All are flagged in the NOTE lines.

## Lab EX-038: Ethane rejection

**Scenario.** Commercial optimiser for the same plant. Ethane is 0.235 USD/gal at Mont Belvieu, gas is 3.25 USD/MMBtu, T&F is 0.08 USD/gal.

**Decision.** Recover or reject ethane this month?

**Model.** Per gallon: recover if price - fee > gas x 0.0665. Plant level: compare total uplift in each mode, including propane lost in rejection.

**Code.** exercises/scripts/ex038.py | **Test.** exercises/tests (python3 emi.py test)

**Run (from the repo root).**

```
python3 emi.py run 038
python3 emi.py run 038 gas_price=2
python3 emi.py run 038 ethane_price=0.30
cat exercises/completed/ex038/gas_price_grid.csv
```

**Reference output of the first command (synthetic).**

```
ex038 | SYNTHETIC HYPOTHETICAL DATA - not historical market data
gas_price: 3.25
ethane_price: 0.235
recover_uplift_USD_per_d: 231351.500652
reject_uplift_USD_per_d: 249511.45509
ethane_swing_gal_per_d: 420367.5
propane_lost_in_rejection_gal_per_d: 21992
ethane_fuel_value_USD_per_gal: 0.216125
ethane_netback_USD_per_gal: 0.155
simple_breakeven_ethane_USD_per_gal: 0.296125
plant_breakeven_ethane_USD_per_gal: 0.2782
rejection_advantage_USD_per_d: 18159.954438
decision: REJECT
gas_price_where_decision_flips: 2.643996
NOTE: Rejection mode also loses propane recovery, so the plant recovers ethane at a price below the simple per-gallon breakeven.
NOTE: Not modeled: residue-gas pipeline Btu limits that cap how much ethane can be rejected, ethane pipeline minimum-volume commitments, and fractionator or pipeline capacity limits that force rejection regardless of price.
```

**Questions.** Answer before reading the key.

1. Why is the plant breakeven (0.2782) below the simple breakeven (0.2961)?
2. At what gas price does the decision flip at today's ethane price?
3. Ethane rallies to 0.30. Decision and value?
4. Name two real-world limits the model ignores.

**Completion test.** Edit data/synthetic/ex037_plant.csv: set transport_frac_fee to 0.05. Predict the simple breakeven (0.266125) and plant breakeven (0.246631) and the decision (still REJECT at 0.235). Run, confirm, restore 0.08.

**Answer key.**

1. Rejecting also drops propane recovery from 98% to 90%: 21,992 gal/d of propane uplift (7,535 USD/d) is lost. Recovery earns that back, so ethane can be worth less and still justify recovery.
2. 2.644 USD/MMBtu. Below it, recover.
3. RECOVER, worth 9,164 USD/d over rejection.
4. Residue-gas Btu limits capping rejection; pipeline or fractionator capacity and minimum-volume commitments.

## Lab EX-039: Fractionation economics

**Scenario.** NGL marketer offered 50,000 bbl of Y-grade at 0.55 USD/gal. Frac fee 0.07 USD/gal. Purity prices are the 2026-01-05 Mont Belvieu table.

**Decision.** Buy the Y-grade?

**Model.** Barrel value = 42 x sum(fraction x purity price). Margin = value - 42 x (purchase + fee).

**Code.** exercises/scripts/ex039.py | **Test.** exercises/tests (python3 emi.py test)

**Run (from the repo root).**

```
python3 emi.py run 039
cat exercises/completed/ex039/barrel_value.csv
```

**Reference output of the first command (synthetic).**

```
ex039 | SYNTHETIC HYPOTHETICAL DATA - not historical market data
composition_sums_to_one: True
purity_value_USD_per_barrel: 28.0518
weighted_price_USD_per_gallon: 0.6679
cost_USD_per_barrel: 26.04
frac_margin_USD_per_barrel: 2.0118
total_margin_USD: 100590
breakeven_ygrade_USD_per_gallon: 0.5979
largest_value_component: Natural_Gasoline
ethane_volume_share_pct: 40
ethane_value_share_pct: 14.073963
NOTE: Reuses the EX-040 price table. No transport to the fractionator, no product losses, no storage or timing.
```

**Questions.** Answer before reading the key.

1. What is one barrel worth and what is the margin?
2. What is the most you can pay for the Y-grade?
3. Which component matters most to the margin?
4. What costs are missing?

**Completion test.** Edit data/synthetic/ex039_ygrade.csv to an ethane-rich barrel (Ethane 0.50, Propane 0.25, Normal_Butane 0.09, Isobutane 0.05, Natural_Gasoline 0.11). Predict the direction of the margin change, run, explain, restore.

**Answer key.**

1. 28.0518 USD value, 26.04 USD cost, 2.0118 USD/bbl margin, 100,590 USD on the lot.
2. 0.5979 USD/gal (weighted purity price 0.6679 less the 0.07 fee).
3. Natural gasoline: 14% of volume, 30.4% of value. A 10% fall in its price removes 0.85 USD/bbl, 42% of the margin.
4. Transport to the fractionator, product loss, storage, and the time between purchase and sale.

## Lab EX-040: Mont Belvieu vs Conway arbitrage

**Scenario.** NGL marketer long product at Conway. Pipeline 0.045 USD/gal plus terminal handling 0.012 USD/gal to reach Mont Belvieu. Lot size 1,000,000 gal.

**Decision.** Which products should move south on each date?

**Model.** Basis = Belvieu - Conway. Net margin = basis - 0.057. Ship when positive.

**Code.** exercises/scripts/ex040.py | **Test.** exercises/tests (python3 emi.py test)

**Run (from the repo root).**

```
python3 emi.py run 040
cat exercises/completed/ex040/ngl_arbitrage.csv
```

**Reference output of the first command (synthetic).**

```
ex040 | SYNTHETIC HYPOTHETICAL DATA - not historical market data
logistics_cost_USD_per_gallon: 0.057
2026-01-05_Ethane_profit_USD: -27000
2026-01-05_Propane_profit_USD: 8000
2026-01-05_Normal_Butane_profit_USD: 8000
2026-01-05_Isobutane_profit_USD: 13000
2026-01-05_Natural_Gasoline_profit_USD: 13000
2026-01-12_Ethane_profit_USD: -27000
2026-01-12_Propane_profit_USD: 33000
2026-01-12_Normal_Butane_profit_USD: 13000
2026-01-12_Isobutane_profit_USD: 28000
2026-01-12_Natural_Gasoline_profit_USD: 28000
products_never_positive: Ethane
best_shipment: 2026-01-12 Propane
NOTE: Ignores pipeline capacity, product quality, timing between purchase and sale, and price impact.
```

**Questions.** Answer before reading the key.

1. Which product never clears the cost?
2. Best shipment?
3. Propane basis widened from 0.065 to 0.090. Name two possible causes.
4. Why might the arbitrage still fail?

**Completion test.** Without editing files, state the transport cost at which propane on 2026-01-05 stops paying (basis 0.065 - handling 0.012 = 0.053 USD/gal).

**Answer key.**

1. Ethane: basis 0.030 both dates, net -0.027 USD/gal.
2. Propane on 2026-01-12: 0.090 - 0.057 = 0.033 USD/gal, 33,000 USD.
3. Stronger Gulf Coast or export pull at Belvieu; surplus or constrained outbound capacity at Conway.
4. No pipeline space, timing risk between purchase and sale, quality differences, moving the market with your own volume.

## Lab EX-041: Propane seasonality

**Scenario.** Supply analyst preparing the pre-winter outlook. Opening inventory 45 MMbbl on 1 April, production 2.90 MMb/d, exports 1.95 MMb/d, operating minimum 30 MMbbl.

**Decision.** Is winter supply adequate, and what breaks it?

**Model.** Ending inventory = opening + (production - demand - exports) x days. Days of supply = inventory / (demand + exports).

**Code.** exercises/scripts/ex041.py | **Test.** exercises/tests (python3 emi.py test)

**Run (from the repo root).**

```
python3 emi.py run 041
python3 emi.py run 041 export_shift=0.10
python3 emi.py run 041 winter_demand_mult=1.10
cat exercises/completed/ex041/propane_balance.csv
```

**Reference output of the first command (synthetic).**

```
ex041 | SYNTHETIC HYPOTHETICAL DATA - not historical market data
peak_inventory_MMbbl: 97.88
peak_month: Sep
base_ending_inventory_MMbbl: 48.13
base_min_inventory_MMbbl: 48.13
build_season_injection_MMbbl: 52.88
winter_draw_MMbbl: 49.75
export_share_of_production_pct: 67.241379
winter_to_summer_demand_ratio: 2.416667
cold_winter_min_inventory_MMbbl: 22.9
cold_winter_months_below_minimum: Feb,Mar
cold_winter_extra_draw_MMbbl: 25.23
min_days_of_supply_base: 15.524242
NOTE: Exports held flat every month; in practice exports respond to the US-overseas price spread and dock capacity.
NOTE: National balance: regional (PADD 2 vs PADD 3) tightness and Conway-Mont Belvieu spreads are not captured (see EX-040).
NOTE: No price response to inventory.
```

**Questions.** Answer before reading the key.

1. When and how high does inventory peak?
2. How much does a 20% colder December to February cost?
3. Exports rise 0.10 MMb/d all year. Effect?
4. What would happen in a real market that this model does not show?

**Completion test.** Find the winter multiplier at which the floor is first breached. Extra draw per 1% = 25.23 / 20 = 1.2615 MMbbl; headroom at end March is 48.13 - 30 = 18.13 MMbbl; breach at about 14.4%. Confirm with winter_demand_mult=1.14 and 1.15.

**Answer key.**

1. 97.88 MMbbl at end September (October is flat).
2. 25.23 MMbbl extra draw. Inventory falls to 26.0 MMbbl in February and 22.9 in March, below the 30 MMbbl floor.
3. 36.5 MMbbl less inventory: ending 11.63 MMbbl and 3.8 days of supply even in a normal winter. Exports matter more than weather in this balance.
4. Prices would rise, exports would fall and inventory would be rationed by price; regional tightness would appear first.

## Lab EX-042: Ethane cracker margin

**Scenario.** Feedstock buyer at an ethylene producer with 3,300 million lb/yr of capacity. Ethylene at a hypothetical 22 c/lb.

**Decision.** How much can the cracker pay for ethane, and would propane be a better feed?

**Model.** c/lb feed = USD/gal x 100 / lb per gal. Feed cost per lb ethylene = that / yield. Margin = ethylene - feed cost + co-product credit - conversion.

**Code.** exercises/scripts/ex042.py | **Test.** exercises/tests (python3 emi.py test)

**Run (from the repo root).**

```
python3 emi.py run 042
python3 emi.py run 042 ethane_price=0.35
python3 emi.py run 042 ethylene_price=30
```

**Reference output of the first command (synthetic).**

```
ex042 | SYNTHETIC HYPOTHETICAL DATA - not historical market data
Ethane_feed_cost_c_per_lb_ethylene: 10.144177
Ethane_cash_cost_c_per_lb_ethylene: 13.144177
Ethane_margin_c_per_lb_ethylene: 8.855823
Ethane_breakeven_feed_price_USD_per_gal: 0.440154
Propane_feed_cost_c_per_lb_ethylene: 40.622884
Propane_cash_cost_c_per_lb_ethylene: 25.622884
Propane_margin_c_per_lb_ethylene: -3.622884
Propane_breakeven_feed_price_USD_per_gal: 0.655788
preferred_feed: Ethane
ethane_advantage_c_per_lb: 12.478707
ethane_annual_margin_USD_million: 292.242165
ethane_feed_bbl_per_d_at_capacity: 92922.467352
NOTE: Yields, co-product credits and conversion costs are single-number synthetic assumptions; real crackers use full yield slates by feed and severity.
NOTE: Ethylene price is a hypothetical input, not a quote.
```

**Questions.** Answer before reading the key.

1. Ethane feed cost per lb of ethylene?
2. Margin and annual value?
3. Maximum ethane price before margin is zero?
4. Together with EX-038, what band can ethane trade in?

**Completion test.** Predict the ethane margin at 0.35 USD/gal by hand (35 / 2.97 / 0.78 = 15.11; 22 - 15.11 + 1 - 4 = 3.89 c/lb). Confirm.

**Answer key.**

1. 23.5 / 2.97 / 0.78 = 10.14 c/lb.
2. 8.86 c/lb, about 292 million USD/yr.
3. 0.440 USD/gal.
4. Floor near the plant recovery breakeven (0.278), ceiling near the cracker breakeven (0.440), under these synthetic assumptions.

## Lab EX-043: NGL transport optimisation

**Scenario.** Logistics scheduler moving 60,000 bbl from Conway and 40,000 bbl from the Marcellus to Mont Belvieu (70,000) and an East Coast export dock (30,000).

**Decision.** Which arcs carry which barrels, and what is pipeline capacity worth?

**Model.** Minimise sum(cost x volume) subject to supply, demand and arc capacity (linear program).

**Code.** exercises/scripts/ex043.py | **Test.** exercises/tests (python3 emi.py test)

**Run (from the repo root).**

```
python3 emi.py run 043
python3 emi.py run 043 outage_arc=A5
python3 emi.py run 043 outage_arc=A1 outage_frac=1
cat exercises/completed/ex043/shipment_plan.csv
```

**Reference output of the first command (synthetic).**

```
ex043 | SYNTHETIC HYPOTHETICAL DATA - not historical market data
base_total_cost_USD: 246500
base_avg_cost_USD_per_bbl: 2.465
base_arcs_at_capacity: A1,A5
outage_arc: A1
outage_total_cost_USD: 320250
outage_cost_increase_USD: 73750
outage_cost_increase_USD_per_bbl_lost: 3.277778
truck_bbl_base: 0
truck_bbl_outage: 2500
base_A1_pipeline_bbl: 45000
base_A2_rail_bbl: 15000
base_A3_truck_bbl: 0
base_A4_rail_bbl: 0
base_A5_pipeline_bbl: 25000
base_A6_rail_bbl: 5000
base_A7_rail_bbl: 0
base_A8_marine_bbl: 10000
NOTE: Single period, single product, costs linear in volume; no minimum tenders, batching, railcar lease terms, demurrage or vessel lot sizes.
NOTE: The cost increase per barrel of lost pipeline capacity is the value of that capacity for the period: the number a shipper would compare with a tariff.
```

**Questions.** Answer before reading the key.

1. Base cost and plan?
2. Half of the Conway pipeline is lost. Cost?
3. The whole Conway pipeline is lost. What happens?
4. Why is 3.28 USD/bbl a useful number?

**Completion test.** Predict the cost of losing half of A5 (Marcellus pipeline): 12,500 bbl move from 1.50 to rail at 3.20, +21,250 USD. Confirm with outage_arc=A5.

**Answer key.**

1. 246,500 USD (2.465 USD/bbl): both pipelines full, 15,000 bbl Conway rail, 5,000 bbl Marcellus rail, 10,000 bbl marine. No trucks.
2. 320,250 USD: +73,750, or 3.28 USD per barrel of lost capacity, and 2,500 bbl go by truck.
3. Infeasible: remaining Conway outlets total 55,000 bbl, so 5,000 bbl are stranded.
4. It is what the lost capacity was worth for the period; compare it with the tariff when deciding on a capacity commitment.

## Lab EX-044: Integrated NGL portfolio

**Scenario.** Risk analyst marking a six-position NGL book across two hubs on 2026-01-05 and 2026-01-12.

**Decision.** What did the book make, and from which risk?

**Model.** MtM = signed gallons x (mark - trade price). Spread P&L = net gallons x Conway move + Belvieu gallons x basis move.

**Code.** exercises/scripts/ex044.py | **Test.** exercises/tests (python3 emi.py test)

**Run (from the repo root).**

```
python3 emi.py run 044
cat exercises/completed/ex044/positions_marked.csv
cat exercises/completed/ex044/by_hub.csv
```

**Reference output of the first command (synthetic).**

```
ex044 | SYNTHETIC HYPOTHETICAL DATA - not historical market data
mtm_day1_USD: 26500
mtm_day2_USD: 118000
weekly_pnl_USD: 91500
P1_pnl_USD: 60000
P2_pnl_USD: -7500
P3_pnl_USD: 30000
P4_pnl_USD: -15000
P5_pnl_USD: 12000
P6_pnl_USD: 12000
net_position_gal: 4200000
net_position_bbl: 100000
gross_notional_USD: 5057000
largest_pnl_product: Propane
propane_net_gal: 500000
propane_flat_price_pnl_USD: 2500
propane_basis_pnl_USD: 50000
propane_total_pnl_USD: 52500
propane_basis_move_USD_per_gal: 0.025
NOTE: Propane P&L = net gallons x Conway move + Belvieu gallons x basis move: the spread leg, not outright price, drives the result.
NOTE: Two price dates only; no VaR, no forward tenor, no physical logistics or storage costs.
```

**Questions.** Answer before reading the key.

1. Book MtM on each date and P&L?
2. Propane made 52,500. How much was outright price?
3. Which position lost and why?
4. What is the book's net position and why is that number weak?

**Completion test.** By hand, compute the P&L if Conway propane had risen 0.03 like Belvieu (basis unchanged): P2 becomes -45,000, propane total 15,000 = 500,000 x 0.03, all flat price.

**Answer key.**

1. 26,500 then 118,000 USD; P&L 91,500.
2. 2,500 (net long 500,000 gal x 0.005). The other 50,000 was basis: 2,000,000 gal x 0.025.
3. P4, short natural gasoline: price rose 0.03, -15,000. P2, short Conway propane: -7,500.
4. 100,000 bbl long, but it adds gallons of different products with different prices and risks. Report by product and hub.

# Chapter 5 sources

Read during the build via web search result excerpts on 2026-11-11; full pages were not fetched.

- S1: [EIA, Hydrocarbon gas liquids explained](https://eia.gov/energyexplained/hydrocarbon-gas-liquids/)
- S2: [EIA, Uses of hydrocarbon gas liquids](https://www.eia.gov/energyexplained/hydrocarbon-gas-liquids/uses-of-hydrocarbon-gas-liquids.php)
- S3: [EIA, Where do hydrocarbon gas liquids come from](https://www.eia.gov/energyexplained/hydrocarbon-gas-liquids/where-do-hydrocarbon-gas-liquids-come-from-in-depth.php)
- S4: [EIA, Transporting and storing hydrocarbon gas liquids](https://www.eia.gov/energyexplained/hydrocarbon-gas-liquids/transporting-and-storing-hydrocarbon-gas-liquids.php)
- S5: [EIA, Imports and exports of hydrocarbon gas liquids](https://www.eia.gov/energyexplained/hydrocarbon-gas-liquids/imports-and-exports-of-hydrocarbon-gas-liquids.php)
- S6: [EIA Today in Energy, First shipment of ethane from U.S. Gulf Coast arrives in Europe (2016)](https://www.eia.gov/todayinenergy/detail.php?id=28052)
- S7: [EIA Today in Energy, Ethane production expected to increase (2016)](https://www.eia.gov/todayinenergy/detail.php?id=25632)
- S8: [EIA Today in Energy, U.S. exports of propane reached records in the first half of 2026](https://www.eia.gov/todayinenergy/detail.php?id=68244)
- S9: [RBN Energy, The strange relationship between Mont Belvieu and Conway NGLs](https://rbnenergy.com/daily-posts/blog/strange-relationship-between-mont-belvieu-and-conway-ngls)
- S10: [ICIS, Estimating US ethane rejection (2017)](https://www.icis.com/resources/news/2017/05/10/10105414/estimating-us-ethane-rejection)
- S11: [Congressional Research Service R45398, Natural Gas Liquids: The Unknown Hydrocarbons (2018)](https://www.everycrsreport.com/files/20181026_R45398_276b160020ed76497f32ec02b5247abba3e60e99.html)
- S12: [OPIS, Most NGLs exit 2022 at lower levels](https://www.opis.com/blog/most-ngls-exit-2022-at-lower-levels/)
- S13: [EIA, STEO hydrocarbon gas liquids module](https://www.eia.gov/analysis/pdfpages/steo_hglindex.php)
- S14: [RBN Energy, The Conway vs. Mont Belvieu propane/NGL differential blowout](https://rbnenergy.com/daily-posts/blog/conway-vs-mont-belvieu-propanengl-differential-blowout)
- S15: [RBN Energy, The differential between us: what drives big propane price spreads](https://rbnenergy.com/the-differential-between-us-what-drives-big-propane-price-spreads)
