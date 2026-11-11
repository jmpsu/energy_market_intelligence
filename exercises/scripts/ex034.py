"""EX-034 Henry Hub, TTF and JKM: spreads, correlations and months in which the US export arbitrage is open. Uses EX-033 cost terms."""
from common import *
def run():
    p = SYN / "ex034_global_gas.csv"; c = params("ex033_lng_netback.csv"); dest = load("ex033_lng_destinations.csv").set_index("benchmark")
    if not p.exists():
        g = np.random.default_rng(34); n = 36; hh = 3.2 + np.cumsum(g.normal(0, 0.18, n)); hh = np.clip(hh, 1.8, None); ttf = 10 + np.cumsum(g.normal(0, 0.9, n)); ttf[12:18] += 9; ttf[26:30] -= 4.5; jkm = ttf + 1.2 + g.normal(0, 0.8, n)
        pd.DataFrame({"month": pd.period_range("2024-01", periods=n, freq="M").astype(str), "henry_hub": hh.round(2), "ttf": np.clip(ttf, 4.5, None).round(2), "jkm": np.clip(jkm, 5, None).round(2)}).to_csv(p, index=False)
    d = pd.read_csv(p); cost = c["liquefaction_fuel_factor"] * d.henry_hub + c["liquefaction_toll"]; var_cost = c["liquefaction_fuel_factor"] * d.henry_hub
    for b, k in (("TTF", "ttf"), ("JKM", "jkm")): d[f"{k}_netback"] = d[k] - c["regas_cost"] - dest.shipping_USD_per_MMBtu[b]; d[f"{k}_margin_full_cost"] = d[f"{k}_netback"] - cost; d[f"{k}_margin_variable"] = d[f"{k}_netback"] - var_cost
    d["best_destination"] = np.where(d.jkm_netback > d.ttf_netback, "Asia", "Europe"); d["jkm_minus_ttf"] = d.jkm - d.ttf; ch = d[["henry_hub", "ttf", "jkm"]].diff().dropna()
    r = {"months": len(d), "mean_ttf_minus_hh": float((d.ttf - d.henry_hub).mean()), "corr_hh_ttf_changes": float(ch.henry_hub.corr(ch.ttf)), "corr_ttf_jkm_changes": float(ch.ttf.corr(ch.jkm)), "months_full_cost_arb_open": int((d[["ttf_margin_full_cost", "jkm_margin_full_cost"]].max(axis=1) > 0).sum()),
         "months_variable_arb_open": int((d[["ttf_margin_variable", "jkm_margin_variable"]].max(axis=1) > 0).sum()), "months_asia_preferred": int((d.best_destination == "Asia").sum()), "max_ttf": float(d.ttf.max()), "min_full_cost_margin": float(d[["ttf_margin_full_cost", "jkm_margin_full_cost"]].max(axis=1).min())}
    return finish("ex034", r, {"global_gas": d}, ["Synthetic series with an injected European price spike and a later slump: NOT historical prices.", "Cargoes keep lifting while the variable margin is positive even if the full-cost margin is negative, because the toll is sunk."])
if __name__ == "__main__": run()
