"""EX-084 Portfolio stress testing: revalue the capstone portfolio under adverse scenarios, rank losses, test a stress-loss limit. Reuses EX-100 evaluate()."""
from common import *
from ex100 import evaluate
def run(limit=None):
    gas, assets, mkt, a = load("capstone_gas_positions.csv"), load("capstone_power_assets.csv"), load("capstone_power_market.csv"), params("capstone_assumptions.csv"); sc = load("ex084_stress_scenarios.csv")
    lim = params("ex084_limits.csv")["stress_loss_limit"] if limit is None else limit; t = pd.DataFrame([evaluate(s, gas, assets, mkt, a)[0] for s in sc.itertuples()])
    t["portfolio_value_USD"] = t.gas_book_value_USD + t.gas_unit_margin_USD + t.renewable_revenue_USD + t.battery_margin_USD; base = t.iloc[0]
    for k in ("gas_book_value_USD", "gas_unit_margin_USD", "renewable_revenue_USD", "battery_margin_USD", "portfolio_value_USD"): t[k.replace("_USD", "_change_USD")] = t[k] - base[k]
    t["limit_breach"] = t.portfolio_value_change_USD < lim; t = t.sort_values("portfolio_value_change_USD").reset_index(drop=True); w = t.iloc[0]; t.to_csv(ROOT / "trading_simulation/risk/ex084_stress_results.csv", index=False)
    drivers = {k: w[k] for k in ("gas_book_value_change_USD", "gas_unit_margin_change_USD", "renewable_revenue_change_USD", "battery_margin_change_USD")}
    r = {f"{x.scenario}_change_USD": x.portfolio_value_change_USD for x in t.itertuples()} | {"worst_scenario": w.scenario, "worst_loss_USD": float(w.portfolio_value_change_USD), "worst_loss_main_driver": min(drivers, key=drivers.get),
         "stress_loss_limit_USD": lim, "scenarios_breaching_limit": ",".join(t.scenario[t.limit_breach]) or "none", "loss_scenarios": int((t.portfolio_value_change_USD < 0).sum())}
    return finish("ex084", r, {"stress_results": t}, ["EX-100's supplied scenarios contain no loss case; these scenarios add falling-price and gas-up/power-flat cases, which are the ones that hurt a long-asset portfolio.",
                  "Same simplifications as EX-100: gas book as long inventory, one power day, demand obligation not priced."])
if __name__ == "__main__": run()
