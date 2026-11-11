"""EX-080 Monte Carlo (geometric Brownian motion) Henry Hub paths, terminal distribution, VaR and Expected Shortfall."""
from common import *
def simulate(s0, vol, drift, days, sims, tdy, seed):
    rng = np.random.default_rng(int(seed)); dt = 1 / tdy; z = rng.standard_normal((int(sims), int(days)))
    return s0 * np.exp(np.cumsum((drift - 0.5 * vol ** 2) * dt + vol * np.sqrt(dt) * z, axis=1))
def var_es(pnl, level):
    var = -np.percentile(pnl, 100 - level); return float(var), float(-pnl[pnl <= -var].mean())
def run():
    p = params("monte_carlo_gas_inputs.csv"); q = params("ex080_portfolio_assumptions.csv")
    paths = simulate(p["initial_price"], p["annualized_volatility"], p["annualized_drift"], p["simulation_days"], p["simulations"], p["trading_days_per_year"], p["random_seed"])
    st = paths[:, -1]; pnl = (st - p["initial_price"]) * (q["long_position"] - q["short_position"]); v95, e95 = var_es(pnl, 95); v99, e99 = var_es(pnl, 99)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4)); ax[0].hist(st, 80); ax[0].set_title("Terminal price (synthetic GBM)"); ax[1].hist(pnl, 80); ax[1].set_title("30-day P&L USD")
    (DONE / "ex080").mkdir(exist_ok=True); fig.tight_layout(); fig.savefig(DONE / "ex080/distributions.png", dpi=130); plt.close(fig)
    T = p["simulation_days"] / p["trading_days_per_year"]
    r = {"terminal_mean": float(st.mean()), "analytic_mean": p["initial_price"] * np.exp(p["annualized_drift"] * T), "terminal_median": float(np.median(st)), "terminal_std": float(st.std(ddof=1)),
         "p05": float(np.percentile(st, 5)), "p95": float(np.percentile(st, 95)), "min_simulated_price": float(paths.min()), "var95_USD": v95, "es95_USD": e95, "var99_USD": v99, "es99_USD": e99, "mean_pnl_USD": float(pnl.mean())}
    return finish("ex080", r, {"terminal_distribution": pd.DataFrame({"terminal_price": st, "pnl_USD": pnl})}, ["GBM cannot produce negative prices (compare EX-020) and has no jumps, seasonality or mean reversion; tail risk is understated for regional hubs."])
if __name__ == "__main__": run()
