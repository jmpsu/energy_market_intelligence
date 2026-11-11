# 5.6 Propane pricing, storage, and seasonality

Evidence tags: [S#] = stated in the linked source (curriculum/chapters/chapter_05/sources.md). [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

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
