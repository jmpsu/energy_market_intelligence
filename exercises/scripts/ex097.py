"""EX-097 Roadmap prioritisation: weighted scoring of competing features and a rank-stability check under alternative weights."""
from common import *
def score(d, w): return (d.customer_value * w["customer_value"] + d.commercial_impact * w["commercial_impact"] + d.feasibility * w["feasibility"] - d.risk * w["risk"]) / d.effort_weeks
def run():
    d = data("ex097_features.csv", """feature,customer_value,commercial_impact,feasibility,risk,effort_weeks
    Basis_monitor,7,5,9,2,4
    NGL_netback_screen,8,6,8,2,5
    Ethane_rejection_optimizer,8,7,6,4,8
    Unified_risk_dashboard,9,8,6,3,8
    Nomination_reconciliation,6,4,7,2,6
    Dispatch_simulation,8,7,4,4,12
    Performance_engine,7,8,3,5,10
    Data_quality_console,5,6,8,1,5""")
    W = {"balanced": dict(customer_value=1, commercial_impact=1, feasibility=1, risk=1), "revenue_first": dict(customer_value=1, commercial_impact=3, feasibility=1, risk=1), "risk_averse": dict(customer_value=1, commercial_impact=1, feasibility=2, risk=3)}
    for k, w in W.items(): d[f"score_{k}"] = score(d, w); d[f"rank_{k}"] = d[f"score_{k}"].rank(ascending=False, method="min").astype(int)
    d["rank_range"] = d[[f"rank_{k}" for k in W]].max(axis=1) - d[[f"rank_{k}" for k in W]].min(axis=1); d = d.sort_values("rank_balanced").reset_index(drop=True); d["cumulative_weeks"] = d.effort_weeks.cumsum(); d.to_csv(ROOT / "product_management/roadmap/ex097_ranked_features.csv", index=False)
    top3 = {k: set(d.sort_values(f"rank_{k}").feature.head(3)) for k in W}
    r = {f"rank_{i}": f for i, f in enumerate(d.feature, 1)} | {"top_score_balanced": float(d.score_balanced.iloc[0]), "features_in_first_26_weeks": int((d.cumulative_weeks <= 26).sum()), "stable_top3": ",".join(sorted(set.intersection(*top3.values()))), "most_weight_sensitive_feature": d.loc[d.rank_range.idxmax(), "feature"], "max_rank_range": int(d.rank_range.max())}
    return finish("ex097", r, {"ranked_features": d}, ["Scores are 1-10 judgments, not measurements; the stability check shows which rankings survive a change of weights and which depend on them."])
if __name__ == "__main__": run()
