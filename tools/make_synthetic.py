#!/usr/bin/env python3
"""Create the additional SYNTHETIC (hypothetical, not historical) datasets for the Tier 1 gap-filler exercises."""
from pathlib import Path
import numpy as np, pandas as pd
S = Path(__file__).resolve().parents[1] / "data/synthetic"
W = lambda n, t: (S / n).write_text(t.strip() + "\n")
W("ng_001_basis_prices.csv", """
location,period,henry_hub_USD_per_MMBtu,hub_price_USD_per_MMBtu,long_basis_position_MMBtu
Waha,1,3.25,1.10,10000
Waha,2,3.25,-0.40,10000
Algonquin,1,3.25,8.75,10000
Algonquin,2,3.25,10.25,10000""")
W("ex033_lng_netback.csv", """
parameter,value,unit
henry_hub,3.25,USD_per_MMBtu
liquefaction_fuel_factor,1.15,multiple_of_henry_hub
liquefaction_toll,2.50,USD_per_MMBtu
regas_cost,0.40,USD_per_MMBtu
cargo_size,3400000,MMBtu""")
W("ex033_lng_destinations.csv", """
destination,benchmark,benchmark_price_USD_per_MMBtu,shipping_USD_per_MMBtu
Europe,TTF,11.00,0.90
Asia,JKM,12.50,1.90""")
W("ex039_ygrade.csv", """
product,gallon_fraction
Ethane,0.40
Propane,0.28
Normal_Butane,0.11
Isobutane,0.07
Natural_Gasoline,0.14""")
W("ex039_frac_assumptions.csv", """
parameter,value,unit
ygrade_purchase_price,0.55,USD_per_gallon
fractionation_fee,0.07,USD_per_gallon
gallons_per_barrel,42,gallons
volume,50000,barrels
price_date,2026-01-05,date""")
W("ex048_two_bus.csv", """
parameter,value,unit
gen_A_cost,30,USD_per_MWh
gen_A_capacity,600,MW
gen_B_cost,60,USD_per_MWh
gen_B_capacity,500,MW
load_A,100,MW
load_B,400,MW
line_limit_A_to_B,250,MW""")
W("ex023_hh_forward_quotes.csv", """
contract_month,day1_USD_per_MMBtu,day2_USD_per_MMBtu
2027-01,3.60,3.70
2027-02,3.50,3.60
2027-03,3.20,3.30
2027-04,3.00,2.95
2027-05,2.95,2.90
2027-06,3.00,2.95
2027-07,3.10,3.05
2027-08,3.12,3.07
2027-09,3.08,3.03
2027-10,3.15,3.10
2027-11,3.45,3.40
2027-12,3.85,3.80""")
W("ex023_trades.csv", """
trade_id,trade_day,side,contract_month,volume_MMBtu,price_USD_per_MMBtu
T1,1,BUY,2027-01,310000,3.40
T2,1,SELL,2027-02,280000,3.55
T3,1,BUY,2027-07,300000,3.00
T4,1,SELL,2027-12,310000,3.70
T5,2,BUY,2027-03,150000,3.25""")
W("capstone_assumptions.csv", """
parameter,value,unit
battery_energy_capacity,400,MWh
battery_round_trip_efficiency,0.85,fraction
battery_initial_soc,200,MWh
battery_min_soc,0,MWh""")
rng = np.random.default_rng(7); n = 400; t = np.arange(n)
hdd = np.maximum(0, 20 + 15 * np.cos(2 * np.pi * t / 365) + rng.normal(0, 4, n)); p = np.empty(n); p[0] = 3.3
for i in range(1, n): p[i] = 0.9 * p[i - 1] + 0.1 * (2.5 + 0.04 * hdd[i]) + rng.normal(0, 0.08)
pd.DataFrame({"day": t, "hdd": hdd.round(2), "henry_hub_USD_per_MMBtu": p.round(4)}).to_csv(S / "ex077_hh_daily_synthetic.csv", index=False)
rng = np.random.default_rng(11); G, T = 12, 72
cap = rng.integers(200, 900, G); pd.DataFrame({"generator": [f"G{i:02d}" for i in range(G)], "capacity_MW": cap,
    "cost_USD_per_MWh": rng.uniform(8, 90, G).round(2), "ramp_MW_per_h": (cap * rng.uniform(0.2, 0.6, G)).round(0)}).to_csv(S / "ex092_generators.csv", index=False)
h = np.arange(T); pd.DataFrame({"hour": h, "demand_MW": (0.55 * cap.sum() + 0.15 * cap.sum() * np.sin(2 * np.pi * (h - 8) / 24)).round(1)}).to_csv(S / "ex092_demand.csv", index=False)
print("synthetic files:", len(list(S.glob("*.csv"))))
