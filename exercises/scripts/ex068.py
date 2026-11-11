"""EX-068 Multi-commodity optimisation: allocate a limited daily gas supply to the best hours (LP), plus battery and renewables. Reuses the EX-065 battery model."""
from common import *
from scipy.optimize import linprog
from market_models.optimization.battery import dispatch
def run(gas_limit_MMBtu=40000.0, heat_rate=7.2, vom=3.0, capacity_MW=500.0):
    m = load("capstone_power_market.csv"); a = params("capstone_assumptions.csv"); margin = (m.market_price_USD_per_MWh - heat_rate * m.gas_price_USD_per_MMBtu - vom).values
    res = linprog(-margin, A_ub=np.full((1, 24), heat_rate), b_ub=[gas_limit_MMBtu], bounds=[(0, capacity_MW)] * 24, method="highs"); gen = res.x; unlimited = float(np.maximum(margin, 0).sum() * capacity_MW)
    b = dispatch(m.market_price_USD_per_MWh, 100, 100, a["battery_energy_capacity"], a["battery_min_soc"], a["battery_initial_soc"], a["battery_round_trip_efficiency"], grid_charge=True, var_cost=5.0); ren = float(((m.solar_generation_MW + m.wind_generation_MW) * m.market_price_USD_per_MWh).sum())
    t = m[["hour", "market_price_USD_per_MWh"]].assign(gas_unit_margin_USD_per_MWh=margin, gas_unit_MW=gen.round(6), battery_net_MW=(b["discharge"] - b["charge"]).round(6), renewables_MW=m.solar_generation_MW + m.wind_generation_MW); gm = float(margin @ gen)
    r = {"gas_unit_margin_USD": gm, "gas_unit_margin_unconstrained_USD": unlimited, "cost_of_gas_limit_USD": unlimited - gm, "gas_burn_MMBtu": float(gen.sum() * heat_rate), "gas_unit_MWh": float(gen.sum()), "full_load_hours": int((gen > capacity_MW - 1e-6).sum()), "shadow_price_of_gas_USD_per_MMBtu": float(-res.ineqlin.marginals[0]),
         "lowest_price_hour_run_USD_per_MWh": float(t.market_price_USD_per_MWh[t.gas_unit_MW > 1e-6].min()), "battery_margin_USD": b["revenue"], "renewable_revenue_USD": ren, "portfolio_margin_USD": gm + b["revenue"] + ren}
    return finish("ex068", r, {"portfolio_dispatch": t}, ["The gas limit's shadow price is what one more MMBtu is worth to this portfolio: the number to compare with the cost of extra supply or transport.", "Assets are separable here (price-taker, no shared constraint); a shared interconnection limit would couple them."])
if __name__ == "__main__": run()
