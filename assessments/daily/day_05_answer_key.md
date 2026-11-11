# Day 5 answer key

1. `ngl_bbl_per_d: 34978.84 (1.5x the base 23319.23)` - Barrels per day by product = inlet Mcf/d x GPM x recovery / 42. Ethane dominates volume but not value [EX].
2. `frac_spread_USD_per_MMBtu: -0.424958 (negative: liquids worth less than their gas value)` - Fee-based: processor earns a fee, producer keeps commodity exposure. Percent-of-proceeds: both share NGL and gas price. Keep-whole: processor keeps liquids, returns the Btu as gas, and holds the full frac-spread exposure [K].
3. `outage_feasible: False; stranded_at_Conway_bbl: 5000` - When the cheapest arc is cut, barrels move to costlier modes or are stranded. The extra cost per barrel of lost capacity is what that capacity is worth [EX].
4. `decision: RECOVER; rejection_advantage_USD_per_d: -19298.43` - Higher gas price raises ethane's fuel value and pushes plants toward rejection; lower gas price favours recovery [EX]. Rising pipeline-gas heat content is an observable sign of rejection [S6].
5. `Ethane_margin_c_per_lb_ethylene: 3.891652` - Breakeven feed price is where margin is zero. Between the plant's rejection breakeven (floor) and the cracker's breakeven (ceiling) lies the range ethane can trade in [EX]. Exports add a second demand outlet [S7].
6. `cold_winter_min_inventory_MMbbl: 22.9; cold_winter_months_below_minimum: Feb,Mar` - A 20% rise in December to February demand is enough to breach an operating minimum [EX]. Regional shortages can occur before the national number looks tight [K].
7. `P5_pnl_USD: 12000` - MtM = signed gallons x (mark - trade price) [EX].
8. `Composition only; no spec limits present.` - Purity products must meet composition specifications; off-spec product is discounted or rejected [K]. Purity means at least 90% of one molecule [S3].
9. `products_never_positive: Ethane; best_shipment: 2026-01-12 Propane` - Ship when basis exceeds transport plus handling. Net margin = basis - logistics cost [EX].
10. `net_position_bbl: 100000; gross_notional_USD: 5057000` - Outright price, hub basis, product spreads (for example ethane vs gas, butane vs crude), volume and operational risk, and proxy-hedge basis when hedging with gas or crude [EX][K].
