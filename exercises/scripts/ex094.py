"""EX-094 Simulation validation: backcast a merit-order price model against observed prices, diagnose structural bias, calibrate on one day, validate on the next."""
from common import *
from market_models.electricity.dispatch import merit_order
def score(obs, mod):
    e = mod - obs; return {"mae": float(np.abs(e).mean()), "bias": float(e.mean()), "rmse": float(np.sqrt((e ** 2).mean())), "corr": float(np.corrcoef(obs, mod)[0, 1])}
def run(mae_threshold=3.0, scarcity_threshold_MW=5200):
    stack = load("power_generation_stack.csv"); d = load("ex094_observed.csv"); sim = [merit_order(stack, x) for x in d.demand_MW]
    d["model_price"] = [s[1] for s in sim]; d["dispatch_total_MW"] = [float(s[0].dispatch_MW.sum()) for s in sim]; d["energy_balance_ok"] = (d.dispatch_total_MW - d.demand_MW).abs() < 1e-6
    d["error"] = d.model_price - d.observed_price_USD_per_MWh; d["high_load"] = d.demand_MW > scarcity_threshold_MW; cal, val = d[d.hour < 24], d[d.hour >= 24]
    x = (cal.demand_MW - scarcity_threshold_MW).clip(lower=0); k = float((x * -cal.error).sum() / (x ** 2).sum())                      # least-squares slope of residual on MW above threshold
    d["calibrated_price"] = d.model_price + k * (d.demand_MW - scarcity_threshold_MW).clip(lower=0); val = d[d.hour >= 24]
    raw, hi, lo, calv = score(val.observed_price_USD_per_MWh, val.model_price), score(val.observed_price_USD_per_MWh[val.high_load], val.model_price[val.high_load]), score(val.observed_price_USD_per_MWh[~val.high_load], val.model_price[~val.high_load]), score(val.observed_price_USD_per_MWh, val.calibrated_price)
    chart("ex094", "backcast", d, "hour", ["observed_price_USD_per_MWh", "model_price", "calibrated_price"], title="Backcast: observed vs model"); d.to_csv(ROOT / "reports/model_validation/ex094_backcast.csv", index=False)
    r = {"hours": len(d), "energy_balance_all_hours": bool(d.energy_balance_ok.all()), "model_prices_are_stack_costs": bool(d.model_price.isin(stack.marginal_cost_USD_per_MWh).all()), "validation_mae_raw": raw["mae"], "validation_bias_raw": raw["bias"],
         "validation_corr_raw": raw["corr"], "high_load_bias_raw": hi["bias"], "normal_load_bias_raw": lo["bias"], "raw_model_passes": bool(raw["mae"] < mae_threshold), "calibrated_scarcity_adder_USD_per_MWh_per_MW": k,
         "validation_mae_calibrated": calv["mae"], "validation_bias_calibrated": calv["bias"], "calibrated_model_passes": bool(calv["mae"] < mae_threshold), "mae_threshold": mae_threshold, "high_load_hours_in_validation": int(val.high_load.sum())}
    return finish("ex094", r, {"backcast": d}, ["Diagnosis: error is concentrated in high-load hours (structural: the stack has no scarcity pricing), not spread evenly (which would suggest a cost-level calibration error).",
                  "Calibrated on hours 0-23, validated on hours 24-47; the synthetic observed series was generated with an adder of 0.05 USD/MWh per MW above 5200 MW plus noise (sd 2).", "Passing a backcast does not validate the model for conditions outside the sample (outages, new capacity, fuel price changes)."])
if __name__ == "__main__": run()
