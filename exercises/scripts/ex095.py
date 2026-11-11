"""EX-095 Customer discovery: pain quantification, transparent prioritisation score, requirements and 90-day roadmap."""
from common import *
ACCEPT = {"Automated_basis_monitoring": ("basis by hub vs Henry Hub refreshed within 5 minutes of each curated price load; alert when basis moves beyond a user-set threshold", "analyst hours on basis analysis per week"),
          "Unified_risk_dashboard": ("one view of position, MtM, VaR and stress loss by book, reconciling to the position ledger to the dollar", "share of books covered; time to produce the daily risk pack"),
          "Automated_nomination_reconciliation": ("contracted, scheduled and delivered volumes matched per trade with every break above tolerance listed with a reason code", "breaks found before invoice issue; scheduler hours per week"),
          "Integrated_dispatch_simulation": ("dispatch run for a gas unit plus storage reproduces an independent benchmark within 0.1 percent of objective value", "simulations run per user per week"),
          "Simulation_performance_optimization": ("runtime on the reference study reduced with identical objective value (relative difference below 1e-6) and zero constraint violations", "median study runtime; scenarios per study")}
def run():
    con = sqlite3.connect(":memory:"); load("customer_interviews.csv").to_sql("interviews", con, index=False); load("product_development_estimates.csv").to_sql("estimates", con, index=False)
    d = pd.read_sql_query("""SELECT i.customer_id, i.persona, i.primary_problem, i.requested_capability AS capability, i.frequency_per_week, i.time_spent_hours_per_week,
        i.time_spent_hours_per_week * 52 AS hours_per_year, i.estimated_annual_financial_impact_USD AS impact_USD, e.estimated_development_weeks AS dev_weeks,
        e.engineering_effort_person_weeks AS effort_pw, e.estimated_customer_value_USD AS value_USD, e.technical_risk_1_to_5 AS risk
        FROM interviews i JOIN estimates e ON e.capability = i.requested_capability""", con); con.close()
    d["value_per_person_week_USD"] = d.value_USD / d.effort_pw; d["risk_factor"] = (6 - d.risk) / 5; d["priority_score"] = d.value_per_person_week_USD * d.risk_factor
    d = d.sort_values("priority_score", ascending=False).reset_index(drop=True); d["rank"] = d.index + 1; d["cumulative_dev_weeks"] = d.dev_weeks.cumsum(); d["in_90_day_window"] = d.cumulative_dev_weeks <= 13
    pm = ROOT / "product_management"; d.to_csv(pm / "backlog/ex095_prioritized_backlog.csv", index=False)
    req = [f"# EX-095 Product requirements ({LABEL})\n\nScore = customer value / engineering person-weeks x (6 - technical risk) / 5. Single-interview evidence per persona: treat as hypotheses.\n"]
    for x in d.itertuples():
        a, k = ACCEPT[x.capability]
        req.append(f"## REQ-{x.rank:02d} {x.capability.replace('_', ' ')}\n- Persona: {x.persona} ({x.customer_id}); problem: {x.primary_problem}; {x.hours_per_year} h/yr; stated impact ${x.impact_USD:,.0f}/yr\n- Requirement: the product shall provide {a}.\n- Acceptance test: automated check on the reference dataset passes for the stated condition.\n- Success KPI: {k}.\n- Score {x.priority_score:,.0f}; effort {x.effort_pw} person-weeks; risk {x.risk}/5\n")
    (pm / "requirements/ex095_requirements.md").write_text("\n".join(req))
    (pm / "roadmap/ex095_roadmap_90_day.md").write_text(f"# EX-095 90-day roadmap ({LABEL})\n\nSequential delivery, one team, 13 weeks.\n\n" + "\n".join(
        f"- {'IN ' if x.in_90_day_window else 'OUT'} | rank {x.rank} | {x.capability} | {x.dev_weeks} wk | finishes week {x.cumulative_dev_weeks}" for x in d.itertuples()) + "\n")
    r = {f"rank_{x.rank}": f"{x.capability} score={x.priority_score:.1f}" for x in d.itertuples()} | {"total_stated_impact_USD": float(d.impact_USD.sum()), "total_hours_per_year": float(d.hours_per_year.sum()),
         "capabilities_in_90_days": ",".join(d.capability[d.in_90_day_window]), "highest_risk_capability": d.loc[d.risk.idxmax(), "capability"]}
    return finish("ex095", r, {"discovery_analysis": d}, ["Customer value equals the single interviewee's stated impact in every row: n=1 per capability, unvalidated.", "Sequential single-team schedule; dependencies (dispatch simulation before performance work) are not enforced by the score."])
if __name__ == "__main__": run()
