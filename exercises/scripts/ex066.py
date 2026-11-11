"""EX-066 Gas-electric coordination: limited pipeline deliveries allocated across gas plants; lost MW and margin."""
from common import *
def run(gas_available_MMBtu_per_h=5000.0, power_price=80.0, gas_price=6.0):
    d = data("ex066_gas_plants.csv", """plant,capacity_MW,heat_rate_MMBtu_per_MWh
    P1,400,7.0
    P2,300,8.0
    P3,200,10.0""")
    d = d.sort_values("heat_rate_MMBtu_per_MWh").reset_index(drop=True); left, mw = gas_available_MMBtu_per_h, []
    for x in d.itertuples():
        g = min(x.capacity_MW * x.heat_rate_MMBtu_per_MWh, left); mw.append(g / x.heat_rate_MMBtu_per_MWh); left -= g
    d["fuel_needed_MMBtu_per_h"] = d.capacity_MW * d.heat_rate_MMBtu_per_MWh; d["output_MW"] = mw; d["fuel_burn_MMBtu_per_h"] = d.output_MW * d.heat_rate_MMBtu_per_MWh; d["lost_MW"] = d.capacity_MW - d.output_MW
    d["margin_USD_per_MWh"] = power_price - gas_price * d.heat_rate_MMBtu_per_MWh; d["lost_margin_USD_per_h"] = d.lost_MW * d.margin_USD_per_MWh.clip(lower=0)
    r = {"fuel_needed_MMBtu_per_h": float(d.fuel_needed_MMBtu_per_h.sum()), "fuel_available_MMBtu_per_h": gas_available_MMBtu_per_h, "fuel_shortfall_pct": float((1 - gas_available_MMBtu_per_h / d.fuel_needed_MMBtu_per_h.sum()) * 100), "output_MW": float(d.output_MW.sum()), "lost_MW": float(d.lost_MW.sum()),
         "lost_MW_pct": float(d.lost_MW.sum() / d.capacity_MW.sum() * 100), "lost_margin_USD_per_h": float(d.lost_margin_USD_per_h.sum()), "MW_per_MMBtu_at_margin": 1 / float(d.heat_rate_MMBtu_per_MWh[d.lost_MW > 0].iloc[0]), "value_of_extra_gas_USD_per_MMBtu": float(d.margin_USD_per_MWh[d.lost_MW > 0].iloc[0] / d.heat_rate_MMBtu_per_MWh[d.lost_MW > 0].iloc[0])}
    return finish("ex066", r, {"fuel_allocation": d}, ["A 31% fuel shortfall removes 25% of the MW because the scarce gas goes to the most efficient units first. Value of extra gas is power margin per MMBtu at the first curtailed plant."])
if __name__ == "__main__": run()
