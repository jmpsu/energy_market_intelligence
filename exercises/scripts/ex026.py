"""EX-026 Henry Hub price sensitivity: a constant-elasticity balance model shocked by production, LNG, weather and storage."""
from common import *
def price_after(base_price, base_demand, tightening_Bcf_d, elasticity): return base_price * (1 + tightening_Bcf_d / base_demand) ** (1 / elasticity)
def run(elasticity=0.25, base_price=3.25, base_demand=110.0):
    s = data("ex026_shocks.csv", "shock,tightening_Bcf_d,description\nProduction_plus_2,-2.0,supply growth\nLNG_exports_plus_3,3.0,new liquefaction trains\nCold_winter,4.0,heating demand above normal\nMild_winter,-4.0,heating demand below normal\nStorage_deficit_refill,1.0,extra injections to refill\nLNG_outage,-2.0,terminal outage backs gas into the market")
    s["price_USD_per_MMBtu"] = [price_after(base_price, base_demand, x, elasticity) for x in s.tightening_Bcf_d]; s["change_USD"] = s.price_USD_per_MMBtu - base_price; s["change_pct"] = s.change_USD / base_price * 100; combo = price_after(base_price, base_demand, 7.0, elasticity)
    r = {f"{x.shock}_price": x.price_USD_per_MMBtu for x in s.itertuples()} | {"price_per_1_Bcf_d_tightening": price_after(base_price, base_demand, 1, elasticity) - base_price, "cold_winter_plus_lng_price": combo, "asymmetry_up_vs_down_4Bcf": float(s.change_USD[s.shock == "Cold_winter"].iloc[0] + s.change_USD[s.shock == "Mild_winter"].iloc[0]), "elasticity_assumed": elasticity}
    return finish("ex026", r, {"sensitivities": s}, ["One-parameter model: the elasticity is assumed, not estimated. Halve it and every move roughly doubles (run elasticity=0.125).", "No storage dynamics, no supply response, no regional detail."])
if __name__ == "__main__": run()
