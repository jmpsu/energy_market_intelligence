"""EX-062 Renewable forecast error: error metrics and the cost of settling deviations at real-time prices."""
from common import *
def run():
    px = load("ex047_da_rt.csv"); f = load("capstone_power_market.csv").wind_generation_MW.values.astype(float); dev = np.array([4, -6, 8, -10, 5, -4, 12, -15, 6, -8, 10, -5, 3, -7, 9, -20, -25, -18, 7, 5, -3, 6, -4, 2.0])
    d = pd.DataFrame({"hour": px.hour, "forecast_MW": f, "actual_MW": f + dev, "da_price": px.da_price_USD_per_MWh, "rt_price": px.rt_price_USD_per_MWh}); d["error_MW"] = d.actual_MW - d.forecast_MW
    d["da_revenue_USD"] = d.forecast_MW * d.da_price; d["rt_settlement_USD"] = d.error_MW * d.rt_price; d["revenue_USD"] = d.da_revenue_USD + d.rt_settlement_USD; d["perfect_forecast_revenue_USD"] = d.actual_MW * d.da_price; d["imbalance_cost_USD"] = d.perfect_forecast_revenue_USD - d.revenue_USD
    r = {"mae_MW": float(d.error_MW.abs().mean()), "bias_MW": float(d.error_MW.mean()), "mape_pct": float((d.error_MW.abs() / d.actual_MW).mean() * 100), "rmse_MW": float(np.sqrt((d.error_MW ** 2).mean())), "da_revenue_USD": float(d.da_revenue_USD.sum()), "rt_settlement_USD": float(d.rt_settlement_USD.sum()),
         "revenue_USD": float(d.revenue_USD.sum()), "perfect_forecast_revenue_USD": float(d.perfect_forecast_revenue_USD.sum()), "imbalance_cost_USD": float(d.imbalance_cost_USD.sum()), "worst_hour": int(d.loc[d.imbalance_cost_USD.idxmax(), "hour"]), "imbalance_cost_pct_of_revenue": float(d.imbalance_cost_USD.sum() / d.perfect_forecast_revenue_USD.sum() * 100)}
    return finish("ex062", r, {"forecast_settlement": d}, ["The cost comes from being short in high real-time-price hours (16-18), not from the average error: MAE alone does not measure financial exposure."])
if __name__ == "__main__": run()
