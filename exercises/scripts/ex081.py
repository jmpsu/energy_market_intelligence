"""EX-081 Value at Risk: one-day parametric (variance-covariance) and historical-simulation VaR, with component VaR by position."""
from common import *
from scipy.stats import norm
def pnl_vector():
    x = load("ex081_price_changes.csv"); pos = load("ex081_positions.csv").set_index("factor").position; return x[pos.index].values @ pos.values, x[pos.index], pos
def run(confidence=95.0):
    pnl, x, pos = pnl_vector(); cov = np.cov(x.values, rowvar=False, ddof=1); w = pos.values.astype(float); sig = float(np.sqrt(w @ cov @ w)); a = confidence / 100
    comp = pd.DataFrame({"factor": pos.index, "position": w, "daily_vol": np.sqrt(np.diag(cov)), "standalone_var_USD": norm.ppf(a) * np.abs(w) * np.sqrt(np.diag(cov)), "component_var_USD": norm.ppf(a) * w * (cov @ w) / sig})
    hv = lambda c: float(-np.percentile(pnl, 100 - c))
    r = {"observations": len(pnl), "portfolio_daily_vol_USD": sig, "parametric_var95_USD": float(norm.ppf(0.95) * sig), "parametric_var99_USD": float(norm.ppf(0.99) * sig), "historical_var95_USD": hv(95), "historical_var99_USD": hv(99),
         "historical_to_parametric_99_ratio": hv(99) / float(norm.ppf(0.99) * sig), "sum_standalone_var_USD": float(comp.standalone_var_USD.sum()), "diversification_benefit_USD": float(comp.standalone_var_USD.sum() - norm.ppf(a) * sig),
         "worst_day_loss_USD": float(-pnl.min()), "excess_kurtosis": float(((pnl - pnl.mean()) ** 4).mean() / pnl.var() ** 2 - 3)} | {f"component_var_{f}": v for f, v in zip(comp.factor, comp.component_var_USD)}
    pd.DataFrame({"day": range(1, len(pnl) + 1), "pnl_USD": pnl}).to_csv(ROOT / "trading_simulation/risk/ex081_daily_pnl.csv", index=False)
    return finish("ex081", r, {"component_var": comp}, ["Returns are synthetic fat-tailed (Student-t) draws: historical 99% VaR exceeds the normal-distribution figure.", "Component VaRs sum to portfolio parametric VaR; the short Waha leg can carry a negative component (it hedges).", "One-day horizon, linear positions, constant covariance."])
if __name__ == "__main__": run()
