"""EX-078 Energy price volatility: log returns, rolling annualised volatility, unusual-volatility flags."""
from common import *
def run(window=20, flag_multiple=1.5):
    d = load("ex077_hh_daily_synthetic.csv"); d["log_return"] = np.log(d.henry_hub_USD_per_MMBtu).diff(); d["rolling_vol_annualised"] = d.log_return.rolling(int(window)).std(ddof=1) * np.sqrt(252); med = float(d.rolling_vol_annualised.median())
    d["high_vol_flag"] = d.rolling_vol_annualised > flag_multiple * med; chart("ex078", "rolling_vol", d, "day", ["rolling_vol_annualised"], title="Rolling annualised volatility")
    r = {"observations": int(d.log_return.notna().sum()), "daily_vol": float(d.log_return.std(ddof=1)), "annualised_vol": float(d.log_return.std(ddof=1) * np.sqrt(252)), "median_rolling_vol": med, "max_rolling_vol": float(d.rolling_vol_annualised.max()), "min_rolling_vol": float(d.rolling_vol_annualised.min()),
         "high_vol_days": int(d.high_vol_flag.sum()), "largest_daily_move_pct": float(d.log_return.abs().max() * 100), "day_of_largest_move": int(d.loc[d.log_return.abs().idxmax(), "day"]), "excess_kurtosis": float(d.log_return.kurt())}
    return finish("ex078", r, {"volatility": d}, ["The synthetic series has constant noise, so rolling volatility varies only by sampling error: a reminder that a 20-day window moves a lot with no regime change. Real gas volatility is seasonal and clustered."])
if __name__ == "__main__": run()
