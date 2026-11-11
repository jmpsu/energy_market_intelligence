"""EX-082 Expected Shortfall: average loss beyond VaR, historical vs normal-distribution formula ES = sigma x pdf(z) / (1 - confidence)."""
from common import *
from scipy.stats import norm
from ex081 import pnl_vector
def es_hist(pnl, c):
    var = -np.percentile(pnl, 100 - c); tail = pnl[pnl <= -var]; return float(var), float(-tail.mean()), int(len(tail))
def run():
    pnl, x, pos = pnl_vector(); sig = float(pnl.std(ddof=1)); r = {"observations": len(pnl)}
    for c in (95, 97.5, 99):
        v, e, n = es_hist(pnl, c); z = norm.ppf(c / 100); k = str(c).replace(".", "_")
        r |= {f"historical_var{k}_USD": v, f"historical_es{k}_USD": e, f"tail_observations_{k}": n, f"normal_es{k}_USD": float(sig * norm.pdf(z) / (1 - c / 100)), f"es_to_var_ratio_{k}": e / v}
    r["historical_es97_5_vs_var99_ratio"] = r["historical_es97_5_USD"] / r["historical_var99_USD"]
    return finish("ex082", r, {"tail_losses": pd.DataFrame({"pnl_USD": np.sort(pnl)[:25]})}, ["99% ES here rests on 5 tail observations out of 500: wide sampling error.", "ES answers how bad losses are once VaR is breached; VaR says nothing about that region."])
if __name__ == "__main__": run()
