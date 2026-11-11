#!/usr/bin/env python3
"""SYNTHETIC (hypothetical) datasets for the NGL exercises 037-044 and tier 1 exercises 047, 056, 063, 081, 082, 084, 094."""
from pathlib import Path
import numpy as np, pandas as pd
S = Path(__file__).resolve().parents[1] / "data/synthetic"
W = lambda n, t: (S / n).write_text(t.strip() + "\n")
W("ngl_components.csv", """
product,carbon,mol_pct,gal_per_Mcf_per_molpct,MMBtu_per_gal,lb_per_gal,recovery_recover,recovery_reject
Ethane,C2,10.5,0.2669,0.0665,2.97,0.85,0.10
Propane,C3,5.0,0.2749,0.0915,4.22,0.98,0.90
Isobutane,iC4,0.7,0.3265,0.0996,4.69,0.99,0.99
Normal_Butane,nC4,1.5,0.3146,0.1037,4.87,0.99,0.99
Natural_Gasoline,C5+,1.3,0.3650,0.1100,5.50,1.00,1.00""")
W("ex037_plant.csv", """
parameter,value,unit
inlet_Mcf_per_d,200000,Mcf_per_day
gas_price,3.25,USD_per_MMBtu
transport_frac_fee,0.08,USD_per_gallon
price_date,2026-01-05,date""")
W("ex041_propane_balance.csv", """
month,days,production_MMb_d,domestic_demand_MMb_d,exports_MMb_d
Apr,30,2.90,0.80,1.95
May,31,2.90,0.65,1.95
Jun,30,2.90,0.60,1.95
Jul,31,2.90,0.60,1.95
Aug,31,2.90,0.62,1.95
Sep,30,2.90,0.70,1.95
Oct,31,2.90,0.95,1.95
Nov,30,2.90,1.15,1.95
Dec,31,2.90,1.40,1.95
Jan,31,2.90,1.45,1.95
Feb,28,2.90,1.35,1.95
Mar,31,2.90,1.05,1.95""")
W("ex041_assumptions.csv", """
parameter,value,unit
opening_inventory,45,MMbbl
minimum_operating_inventory,30,MMbbl
cold_winter_demand_multiplier,1.20,multiple""")
W("ex042_cracker_feeds.csv", """
feed,price_USD_per_gal,lb_per_gal,ethylene_yield_lb_per_lb,coproduct_credit_c_per_lb_ethylene,conversion_cost_c_per_lb_ethylene
Ethane,0.235,2.97,0.78,1.0,4.0
Propane,0.720,4.22,0.42,20.0,5.0""")
W("ex042_assumptions.csv", """
parameter,value,unit
ethylene_price,22.0,cents_per_lb
cracker_ethylene_capacity,3300,million_lb_per_year""")
W("ex043_nodes.csv", """
node,supply_bbl,demand_bbl
Conway,60000,0
Marcellus,40000,0
Mont_Belvieu,0,70000
East_Coast_Export,0,30000""")
W("ex043_arcs.csv", """
arc_id,origin,destination,mode,capacity_bbl,cost_USD_per_bbl
A1,Conway,Mont_Belvieu,pipeline,45000,1.90
A2,Conway,Mont_Belvieu,rail,30000,4.50
A3,Conway,Mont_Belvieu,truck,10000,7.00
A4,Conway,East_Coast_Export,rail,15000,5.50
A5,Marcellus,East_Coast_Export,pipeline,25000,1.50
A6,Marcellus,East_Coast_Export,rail,20000,3.20
A7,Marcellus,Mont_Belvieu,rail,20000,6.00
A8,Marcellus,Mont_Belvieu,marine,30000,4.00""")
W("ex044_ngl_positions.csv", """
position_id,side,product,hub,volume_gal,trade_price_USD_per_gal
P1,BUY,Propane,mont_belvieu,2000000,0.700
P2,SELL,Propane,conway,1500000,0.650
P3,BUY,Ethane,mont_belvieu,3000000,0.240
P4,SELL,Natural_Gasoline,mont_belvieu,500000,1.460
P5,BUY,Normal_Butane,conway,800000,0.830
P6,BUY,Isobutane,mont_belvieu,400000,1.000""")
da = [35,32,30,28,25,30,40,55,65,70,68,60,55,58,75,95,125,150,115,85,65,50,42,38]
dev = [-3,-2,-4,-1,2,5,-6,8,-5,-10,-8,-4,3,6,12,25,60,110,-15,-9,-4,2,1,-2]
pd.DataFrame({"hour": range(1, 25), "da_price_USD_per_MWh": da, "rt_price_USD_per_MWh": [a + b for a, b in zip(da, dev)], "da_award_MW": 300,
              "rt_actual_MW": [200 if h in (17, 18) else 300 for h in range(1, 25)]}).to_csv(S / "ex047_da_rt.csv", index=False)
W("ex056_buses.csv", """
bus,load_MW,gen_capacity_MW,gen_cost_USD_per_MWh
1,0,400,20
2,0,400,50
3,300,0,0""")
W("ex056_lines.csv", """
line,from_bus,to_bus,reactance_pu,limit_MW
L12,1,2,0.1,1000
L13,1,3,0.1,150
L23,2,3,0.1,1000""")
W("ex056_ftr.csv", """
ftr_id,source_bus,sink_bus,MW
FTR1,1,3,100
FTR2,2,3,50""")
rng = np.random.default_rng(21); n = 500; C = np.array([[1, .5, .6], [.5, 1, .3], [.6, .3, 1]]); sd = np.array([0.12, 0.30, 6.0])
z = rng.standard_t(4, (n, 3)) / np.sqrt(2.0); x = z @ np.linalg.cholesky(C).T * sd
pd.DataFrame(x.round(4), columns=["henry_hub_USD_per_MMBtu", "waha_USD_per_MMBtu", "pjm_west_USD_per_MWh"]).assign(day=range(1, n + 1)).to_csv(S / "ex081_price_changes.csv", index=False)
W("ex081_positions.csv", """
factor,position,unit
henry_hub_USD_per_MMBtu,500000,MMBtu
waha_USD_per_MMBtu,-200000,MMBtu
pjm_west_USD_per_MWh,20000,MWh""")
W("ex084_stress_scenarios.csv", """
scenario,gas_price_change_percent,power_price_change_percent,gas_supply_reduction_percent,pipeline_capacity_reduction_percent,renewable_generation_change_percent
Base,0,0,0,0,0
Gas_Spike_Flat_Power,150,0,0,0,0
Power_Collapse,0,-50,0,0,0
Mild_Winter,-30,-30,0,0,0
Gas_Collapse,-60,-10,0,0,0
Fuel_Cutoff_Scarcity,400,900,50,60,-40
Renewable_Drought_Low_Price,0,-20,0,0,-70""")
W("ex084_limits.csv", """
parameter,value,unit
stress_loss_limit,-300000,USD""")
rng = np.random.default_rng(5); h = np.arange(48); dem = (4400 + 1400 * np.sin(2 * np.pi * (h - 9) / 24)).round(0)
st = pd.read_csv(S / "power_generation_stack.csv").sort_values("marginal_cost_USD_per_MWh"); cum = st.available_capacity_MW.cumsum().values; mc = st.marginal_cost_USD_per_MWh.values
model = np.array([mc[np.searchsorted(cum, d)] for d in dem]); obs = model + rng.normal(0, 2, 48) + 0.05 * np.maximum(dem - 5200, 0)
pd.DataFrame({"hour": h, "demand_MW": dem, "observed_price_USD_per_MWh": obs.round(2)}).to_csv(S / "ex094_observed.csv", index=False)
print("synthetic files:", len(list(S.glob("*.csv"))))
