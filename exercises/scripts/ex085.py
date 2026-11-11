"""EX-085 HDD put: payout = min(max(strike - cumulative HDD, 0) x tick, cap); temperature-shift scenarios."""
from common import *
def payout(hdd_total, p): return float(min(max(p["seasonal_HDD_strike"] - hdd_total, 0) * p["payout_per_HDD"], p["maximum_payout"]))
def run(shifts=(-5, 0, 3, 10, 15)):
    d = load("winter_hdd_observations.csv"); p = params("ex085_contract_assumptions.csv")
    d["HDD_recalculated"] = np.maximum(0, 65 - d.average_temperature_F); d["HDD_matches"] = d.HDD == d.HDD_recalculated; d["cumulative_HDD"] = d.HDD_recalculated.cumsum()
    sc = pd.DataFrame([{"temperature_shift_F": s, "cumulative_HDD": float(np.maximum(0, 65 - (d.average_temperature_F + s)).sum())} for s in shifts])
    sc["payout_USD"] = sc.cumulative_HDD.map(lambda h: payout(h, p)); sc["capped"] = sc.payout_USD >= p["maximum_payout"]
    tot = float(d.HDD_recalculated.sum())
    r = {"hdd_rows_verified": int(d.HDD_matches.sum()), "cumulative_HDD": tot, "strike_HDD": p["seasonal_HDD_strike"], "payout_USD": payout(tot, p),
         "cap_reached_at_HDD": p["seasonal_HDD_strike"] - p["maximum_payout"] / p["payout_per_HDD"]} | {f"payout_shift_{int(s.temperature_shift_F):+d}F_USD": s.payout_USD for s in sc.itertuples()}
    return finish("ex085", r, {"hdd_calculation": d, "payout_scenarios": sc}, ["The strike is labelled seasonal but only 15 days are supplied; the payout treats the 15 days as the full contract period.",
                  "Payoff is intrinsic only: no premium, no probability distribution, no station-vs-load basis risk."])
if __name__ == "__main__": run()
