"""EX-077 Gas price forecast and out-of-sample validation: OLS on lagged price and HDD vs naive persistence."""
from common import *
def metrics(actual, pred):
    e = actual - pred; return {"mae": float(np.abs(e).mean()), "rmse": float(np.sqrt((e ** 2).mean())), "mape_pct": float((np.abs(e) / np.abs(actual)).mean() * 100), "bias": float(e.mean())}
def run(train_n=300):
    d = load("ex077_hh_daily_synthetic.csv"); d["lag_price"] = d.henry_hub_USD_per_MMBtu.shift(1); d = d.dropna().reset_index(drop=True); tr, te = d.iloc[:train_n], d.iloc[train_n:]
    X = lambda f: np.column_stack([np.ones(len(f)), f.lag_price, f.hdd]); beta, *_ = np.linalg.lstsq(X(tr), tr.henry_hub_USD_per_MMBtu.values, rcond=None)
    te = te.assign(model_forecast=X(te) @ beta, naive_forecast=te.lag_price); y = te.henry_hub_USD_per_MMBtu.values
    m, nv, ins = metrics(y, te.model_forecast.values), metrics(y, te.naive_forecast.values), metrics(tr.henry_hub_USD_per_MMBtu.values, X(tr) @ beta)
    chart("ex077", "forecast_vs_actual", te, "day", ["henry_hub_USD_per_MMBtu", "model_forecast", "naive_forecast"], title="One-day-ahead forecast, test window")
    te.to_csv(ROOT / "reports/model_validation/ex077_forecast_test_window.csv", index=False)
    r = {"train_rows": len(tr), "test_rows": len(te), "intercept": beta[0], "coef_lag_price": beta[1], "coef_hdd": beta[2]} | {f"model_{k}": v for k, v in m.items()} | {f"naive_{k}": v for k, v in nv.items()}
    r |= {"in_sample_rmse": ins["rmse"], "rmse_skill_vs_naive_pct": (1 - m["rmse"] / nv["rmse"]) * 100, "generating_process": "price = 0.9*lag + 0.1*(2.5 + 0.04*HDD) + N(0, 0.08)"}
    return finish("ex077", r, {"test_forecasts": te}, ["HDD is used as a known input on the forecast day (perfect weather foresight); a real forecast needs forecast HDD.",
                  "On this sample the fitted model does NOT beat persistence out of sample (negative skill) even though the data were generated from the same linear form: with 0.9 persistence and noise of 0.08 the HDD signal is too weak to estimate reliably from 300 days."])
if __name__ == "__main__": run()
