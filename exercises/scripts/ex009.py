"""EX-009 Integrated market dashboard: one daily table of gas, power, storage, weather and generation with derived indicators and flags."""
from common import *
def run(z_flag=2.0):
    p = SYN / "ex009_daily_market.csv"
    if not p.exists():
        g = np.random.default_rng(9); n = 60; hdd = np.maximum(0, 22 + 10 * np.sin(np.arange(n) / 9) + g.normal(0, 4, n)); gas = 3.2 + 0.03 * (hdd - 22) + g.normal(0, 0.08, n); gas[40] += 1.2
        pd.DataFrame({"day": range(1, n + 1), "hdd": hdd.round(1), "henry_hub": gas.round(3), "power_price": (8.5 * gas + 12 + g.normal(0, 3, n)).round(2), "storage_Bcf": (3200 - np.cumsum(0.9 * hdd)).round(0), "production_Bcf_d": (105 + g.normal(0, 0.6, n)).round(2), "gas_generation_GWh": (4200 + 30 * hdd + g.normal(0, 80, n)).round(0)}).to_csv(p, index=False)
    d = pd.read_csv(p); d["implied_heat_rate"] = d.power_price / d.henry_hub; d["spark_spread_7HR"] = d.power_price - 7 * d.henry_hub; d["storage_change_Bcf"] = d.storage_Bcf.diff()
    for c in ("henry_hub", "power_price", "implied_heat_rate"): d[f"{c}_z"] = (d[c] - d[c].rolling(20).mean()) / d[c].rolling(20).std()
    d["flag"] = (d[["henry_hub_z", "power_price_z", "implied_heat_rate_z"]].abs() > z_flag).any(axis=1)
    if not os.environ.get("EMI_SCENARIO"):
        ax = d.plot(x="day", y=["henry_hub", "power_price", "hdd", "storage_Bcf"], subplots=True, figsize=(10, 8), title="Synthetic integrated dashboard"); (DONE / "ex009").mkdir(exist_ok=True); ax[0].figure.savefig(DONE / "ex009/dashboard.png", dpi=120); plt.close("all")
    r = {"days": len(d), "corr_gas_power": float(d.henry_hub.corr(d.power_price)), "corr_hdd_gas": float(d.hdd.corr(d.henry_hub)), "corr_hdd_storage_change": float(d.hdd.corr(d.storage_change_Bcf)), "mean_implied_heat_rate": float(d.implied_heat_rate.mean()), "flagged_days": ",".join(map(str, d.day[d.flag])),
         "max_gas_z_day": int(d.loc[d.henry_hub_z.idxmax(), "day"]), "storage_draw_total_Bcf": float(d.storage_Bcf.iloc[0] - d.storage_Bcf.iloc[-1])}
    return finish("ex009", r, {"dashboard": d}, ["Synthetic series with an injected gas spike on day 41; the dashboard should flag it."])
if __name__ == "__main__": run()
