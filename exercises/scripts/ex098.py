"""EX-098 Product performance metrics: adoption, retention, runtime, data quality, model accuracy and revenue retention computed from a usage log and the repo's own outputs."""
from common import *
import ex070, ex094
def run():
    p = SYN / "ex098_usage_log.csv"
    if not p.exists():
        rng = np.random.default_rng(98); rows = []
        for u in range(1, 41):
            for wk in range(1, 9):
                if rng.random() < (0.85 if u <= 25 else 0.35) * (1 - 0.03 * wk): rows.append({"user_id": f"U{u:02d}", "week": wk, "runs": int(rng.integers(1, 12)), "median_runtime_min": round(float(rng.lognormal(3.2, 0.5)), 1)})
        pd.DataFrame(rows).to_csv(p, index=False)
    u = pd.read_csv(p); acct = data("ex098_accounts.csv", """account,arr_start_USD,arr_end_USD
    A1,400000,460000
    A2,250000,250000
    A3,180000,0
    A4,300000,330000
    A5,120000,90000"""); licensed = 50
    wau = u.groupby("week").user_id.nunique(); w1, w8 = set(u.user_id[u.week == 1]), set(u.user_id[u.week == 8]); dq = quiet(ex070.run); mv = quiet(ex094.run)
    k = pd.DataFrame([("adoption_wau_pct_of_licensed", wau.mean() / licensed * 100, ">= 60"), ("week8_retention_of_week1_users_pct", len(w1 & w8) / len(w1) * 100, ">= 70"), ("runtime_p50_min", u.median_runtime_min.median(), "<= 30"), ("runtime_p95_min", u.median_runtime_min.quantile(0.95), "<= 60"),
                      ("data_completeness_pct", dq["completeness_pct"], ">= 99"), ("model_backcast_mae_USD_per_MWh", mv["validation_mae_calibrated"], "<= 3"), ("net_revenue_retention_pct", acct.arr_end_USD.sum() / acct.arr_start_USD.sum() * 100, ">= 100"), ("gross_revenue_retention_pct", np.minimum(acct.arr_end_USD, acct.arr_start_USD).sum() / acct.arr_start_USD.sum() * 100, ">= 90")], columns=["kpi", "value", "target"])
    k["meets_target"] = [eval(f"{v} {t}") for v, t in zip(k.value, k.target)]; k.to_csv(ROOT / "product_management/kpis/ex098_kpis.csv", index=False)
    r = {x.kpi: x.value for x in k.itertuples()} | {"kpis_meeting_target": int(k.meets_target.sum()), "kpis_missing_target": ",".join(k.kpi[~k.meets_target]), "active_users_ever": int(u.user_id.nunique()), "licensed_seats": licensed}
    return finish("ex098", r, {"kpis": k, "weekly_active_users": wau.rename("wau").reset_index()}, ["Usage log, accounts and targets are synthetic. Data-quality and model-accuracy KPIs are read live from EX-070 and EX-094, so the scorecard moves when the product does."])
if __name__ == "__main__": run()
