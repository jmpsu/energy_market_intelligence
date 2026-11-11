"""EX-033 LNG export netback: destination price - regas - shipping, versus Gulf Coast cost = fuel factor x Henry Hub + toll."""
from common import *
def run(hh=None):
    p = params("ex033_lng_netback.csv"); d = load("ex033_lng_destinations.csv"); hh = p["henry_hub"] if hh is None else hh
    fob_cost = p["liquefaction_fuel_factor"] * hh + p["liquefaction_toll"]
    d["netback_fob_USD_per_MMBtu"] = d.benchmark_price_USD_per_MMBtu - p["regas_cost"] - d.shipping_USD_per_MMBtu; d["fob_cost_USD_per_MMBtu"] = fob_cost
    d["margin_USD_per_MMBtu"] = d.netback_fob_USD_per_MMBtu - fob_cost; d["cargo_margin_USD"] = d.margin_USD_per_MMBtu * p["cargo_size"]
    d["variable_margin_USD_per_MMBtu"] = d.netback_fob_USD_per_MMBtu - p["liquefaction_fuel_factor"] * hh      # toll treated as sunk
    d["breakeven_henry_hub_USD_per_MMBtu"] = (d.netback_fob_USD_per_MMBtu - p["liquefaction_toll"]) / p["liquefaction_fuel_factor"]
    r = {"fob_cost_USD_per_MMBtu": fob_cost} | {f"{x.destination}_margin_USD_per_MMBtu": x.margin_USD_per_MMBtu for x in d.itertuples()} | {f"{x.destination}_cargo_margin_USD": x.cargo_margin_USD for x in d.itertuples()}
    r |= {f"{x.destination}_breakeven_HH": x.breakeven_henry_hub_USD_per_MMBtu for x in d.itertuples()} | {"preferred_destination": d.loc[d.margin_USD_per_MMBtu.idxmax(), "destination"]}
    return finish("ex033", r, {"lng_netback": d}, ["Regas deducted for both destinations although JKM-style benchmarks are delivered ex-ship; confirm each benchmark's delivery basis.", "No boil-off, canal fees, charter rate variation or destination flexibility value."])
if __name__ == "__main__": run()
