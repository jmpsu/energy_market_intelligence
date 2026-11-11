# 5.7 Butane and isobutane markets

Evidence tags: [S#] = stated in the linked source (curriculum/chapters/chapter_05/sources.md). [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

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
