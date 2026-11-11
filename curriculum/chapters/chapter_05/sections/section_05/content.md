# 5.5 Ethane and petrochemical markets

Evidence tags: [S#] = stated in the linked source (curriculum/chapters/chapter_05/sources.md). [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

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
