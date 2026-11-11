# 5.8 Natural gasoline and product specifications

Evidence tags: [S#] = stated in the linked source (curriculum/chapters/chapter_05/sources.md). [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

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
