"""EX-067 Extreme winter event, simplified and HYPOTHETICAL (structure inspired by February 2021 Winter Storm Uri; none of these numbers are actual event data)."""
from common import *
def run(price_cap=9000.0, normal_price=60.0):
    d = data("ex067_extreme_winter.csv", """day,demand_GW,available_generation_GW,gas_supply_pct_of_normal
    1,55,60,95
    2,62,58,80
    3,70,48,55
    4,68,50,60
    5,60,58,85""")
    d["served_GW"] = d[["demand_GW", "available_generation_GW"]].min(axis=1); d["load_shed_GW"] = d.demand_GW - d.served_GW; d["price_USD_per_MWh"] = np.where(d.load_shed_GW > 0, price_cap, normal_price); d["energy_cost_USD"] = d.served_GW * 1000 * 24 * d.price_USD_per_MWh
    d["unserved_GWh"] = d.load_shed_GW * 24; normal = float((d.demand_GW * 1000 * 24 * normal_price).sum())
    r = {"peak_load_shed_GW": float(d.load_shed_GW.max()), "shed_days": int((d.load_shed_GW > 0).sum()), "unserved_GWh": float(d.unserved_GWh.sum()), "energy_cost_USD": float(d.energy_cost_USD.sum()), "energy_cost_at_normal_price_USD": normal, "cost_multiple_of_normal": float(d.energy_cost_USD.sum() / normal),
         "worst_day": int(d.loc[d.load_shed_GW.idxmax(), "day"]), "min_gas_supply_pct": float(d.gas_supply_pct_of_normal.min()), "corr_gas_supply_available_generation": float(d.gas_supply_pct_of_normal.corr(d.available_generation_GW))}
    return finish("ex067", r, {"extreme_event": d}, ["Daily averages; price pinned at a cap parameter whenever load is shed. Not a reconstruction: every number is invented to show the mechanism (gas supply loss -> generation loss -> shedding -> scarcity pricing)."])
if __name__ == "__main__": run()
