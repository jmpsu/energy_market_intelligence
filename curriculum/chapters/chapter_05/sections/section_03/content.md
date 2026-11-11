# 5.3 Y-grade and mixed NGL transportation

Evidence tags: [S#] = stated in the linked source (curriculum/chapters/chapter_05/sources.md). [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

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
