"""EX-089 Production-cost simulation: chronological hourly merit-order dispatch over a day with wind and solar profiles; cost, prices, energy by technology."""
from common import *
from market_models.electricity.dispatch import merit_order
def run(demand_scale=1.0, gas_cost_scale=1.0):
    stack = load("power_generation_stack.csv"); dem = load("ex094_observed.csv").iloc[:24].demand_MW.values * demand_scale; hrs = np.arange(24); solar_cf = np.clip(np.sin(np.pi * (hrs - 6) / 12), 0, None); wind_cf = 0.55 + 0.25 * np.cos(2 * np.pi * hrs / 24)
    stack["available_capacity_MW"] = stack.available_capacity_MW.astype(float); stack["marginal_cost_USD_per_MWh"] = stack.marginal_cost_USD_per_MWh.astype(float); stack.loc[stack.technology == "Natural_Gas", "marginal_cost_USD_per_MWh"] *= gas_cost_scale; rows, gen = [], []
    for h in hrs:
        s = stack.copy(); s.loc[s.technology == "Solar", "available_capacity_MW"] *= solar_cf[h]; s.loc[s.technology == "Wind", "available_capacity_MW"] *= wind_cf[h]; disp, price, unmet = merit_order(s, dem[h])
        rows.append({"hour": h, "demand_MW": dem[h], "price_USD_per_MWh": price, "production_cost_USD": float((disp.dispatch_MW * disp.marginal_cost_USD_per_MWh).sum()), "unmet_MW": unmet, "available_MW": float(s.available_capacity_MW.sum())}); gen.append(disp.groupby("technology").dispatch_MW.sum())
    t = pd.DataFrame(rows); g = pd.DataFrame(gen).fillna(0).sum(); mix = (g / g.sum() * 100).rename("share_pct").reset_index().rename(columns={"index": "technology"}); mix["MWh"] = g.values; chart("ex089", "hourly_price", t, "hour", ["price_USD_per_MWh"], title="Simulated hourly price")
    r = {"total_demand_MWh": float(t.demand_MW.sum()), "total_production_cost_USD": float(t.production_cost_USD.sum()), "average_cost_USD_per_MWh": float(t.production_cost_USD.sum() / t.demand_MW.sum()), "load_weighted_price_USD_per_MWh": float((t.price_USD_per_MWh * t.demand_MW).sum() / t.demand_MW.sum()), "peak_price": float(t.price_USD_per_MWh.max()), "min_price": float(t.price_USD_per_MWh.min()),
         "unserved_MWh": float(t.unmet_MW.sum()), "min_reserve_margin_MW": float((t.available_MW - t.demand_MW).min())} | {f"{x.technology}_share_pct": x.share_pct for x in mix.itertuples()}
    return finish("ex089", r, {"hourly_results": t, "generation_mix": mix}, ["Hour-by-hour merit order with no inter-temporal constraints (no starts, ramps, storage), no network, no reserves: the simplest member of the production-cost model family. Wind and solar profiles are formula-generated."])
if __name__ == "__main__": run()
