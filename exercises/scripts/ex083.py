"""EX-083 Potential future exposure of a fixed-price gas swap: simulate forward prices monthly, exposure = max(MtM, 0) on the remaining volume."""
from common import *
def run(volume_per_month=100000.0, months=12, fixed=3.25, f0=3.25, vol=0.50, sims=5000, seed=83, confidence=95.0):
    rng = np.random.default_rng(int(seed)); dt = 1 / 12; z = rng.standard_normal((int(sims), int(months))); f = f0 * np.exp(np.cumsum(-0.5 * vol ** 2 * dt + vol * np.sqrt(dt) * z, axis=1)); remaining = volume_per_month * (months - np.arange(1, months + 1))
    mtm = (f - fixed) * remaining; exp = np.maximum(mtm, 0); t = pd.DataFrame({"month": range(1, months + 1), "remaining_volume_MMBtu": remaining, "expected_exposure_USD": exp.mean(axis=0), "pfe_USD": np.percentile(exp, confidence, axis=0), "expected_negative_exposure_USD": np.minimum(mtm, 0).mean(axis=0)})
    chart("ex083", "exposure_profile", t, "month", ["expected_exposure_USD", "pfe_USD"], title="Swap exposure profile")
    r = {"peak_pfe_USD": float(t.pfe_USD.max()), "peak_pfe_month": int(t.loc[t.pfe_USD.idxmax(), "month"]), "peak_expected_exposure_USD": float(t.expected_exposure_USD.max()), "average_expected_exposure_USD": float(t.expected_exposure_USD.mean()), "pfe_at_maturity_USD": float(t.pfe_USD.iloc[-1]),
         "pfe_month_1_USD": float(t.pfe_USD.iloc[0]), "current_exposure_USD": max((f0 - fixed) * volume_per_month * months, 0.0), "notional_USD": fixed * volume_per_month * months, "peak_pfe_pct_of_notional": float(t.pfe_USD.max() / (fixed * volume_per_month * months) * 100)}
    return finish("ex083", r, {"exposure_profile": t}, ["Exposure starts at zero (struck at market), rises as prices diffuse, then falls as volume settles: the hump shape. One forward price for all months, lognormal, no collateral or netting."])
if __name__ == "__main__": run()
