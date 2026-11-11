# 5.10 NGL transportation, exports, trading, and risk

Evidence tags: [S#] = stated in the linked source (curriculum/chapters/chapter_05/sources.md). [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

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
