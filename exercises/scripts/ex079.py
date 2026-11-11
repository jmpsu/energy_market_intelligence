"""EX-079 Power demand forecast: regression on heating and cooling degree days and a weekend effect, validated against a same-day-last-week baseline."""
from common import *
def run(train_n=150):
    p = SYN / "ex079_daily_load.csv"
    if not p.exists():
        rng = np.random.default_rng(79); n = 210; t = np.arange(n); temp = 60 + 22 * np.sin(2 * np.pi * (t - 60) / 365) + rng.normal(0, 5, n); wk = (t % 7 >= 5).astype(int)
        pd.DataFrame({"day": t, "temperature_F": temp.round(1), "weekend": wk, "load_GWh": (300 + 4.0 * np.maximum(temp - 65, 0) + 2.5 * np.maximum(65 - temp, 0) - 25 * wk + rng.normal(0, 6, n)).round(1)}).to_csv(p, index=False)
    d = pd.read_csv(p); d["cdd"] = (d.temperature_F - 65).clip(lower=0); d["hdd"] = (65 - d.temperature_F).clip(lower=0); d["naive"] = d.load_GWh.shift(7); X = lambda f: np.column_stack([np.ones(len(f)), f.cdd, f.hdd, f.weekend])
    tr, te = d.iloc[:train_n], d.iloc[train_n:].copy(); b, *_ = np.linalg.lstsq(X(tr), tr.load_GWh.values, rcond=None); te["forecast"] = X(te) @ b; mape = lambda a, f: float((np.abs(a - f) / a).mean() * 100)
    chart("ex079", "load_forecast", te, "day", ["load_GWh", "forecast", "naive"], title="Daily load forecast, test window")
    r = {"train_days": len(tr), "test_days": len(te), "base_load_GWh": b[0], "GWh_per_CDD": b[1], "GWh_per_HDD": b[2], "weekend_effect_GWh": b[3], "model_mape_pct": mape(te.load_GWh, te.forecast), "naive_mape_pct": mape(te.load_GWh, te.naive), "model_bias_GWh": float((te.forecast - te.load_GWh).mean()),
         "skill_vs_naive_pct": (1 - mape(te.load_GWh, te.forecast) / mape(te.load_GWh, te.naive)) * 100, "true_parameters": "300 base, 4.0/CDD, 2.5/HDD, -25 weekend, noise sd 6"}
    return finish("ex079", r, {"test_forecasts": te}, ["Actual temperature is used as the input: forecast-temperature error would add to load error. The model form matches the generator, so this is a best case."])
if __name__ == "__main__": run()
