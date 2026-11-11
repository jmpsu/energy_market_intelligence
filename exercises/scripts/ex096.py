"""EX-096 Market intelligence product specification: users, workflows, data requirements and acceptance criteria generated from the repo's own exercises and tests (traceability)."""
from common import *
import yaml
def run():
    spec = data("ex096_product_spec.csv", """req_id,user,workflow,capability,data_required,exercise,acceptance_criterion
    R01,Gas_Trader,morning basis review,basis by hub vs benchmark with alerts,hub prices,EX-019,basis equals hub minus benchmark to 1e-6 on the reference set
    R02,NGL_Marketer,daily arbitrage screen,hub-to-hub netback by product,NGL hub prices and logistics costs,EX-040,net margin equals basis minus logistics cost for every product and date
    R03,Plant_Optimiser,monthly ethane decision,recover or reject with plant-level breakeven,composition recovery fees gas and NGL prices,EX-038,decision flips exactly at the reported breakeven price
    R04,Power_Analyst,congestion study,nodal prices with congestion component,network topology limits offers,EX-056,LMPs match the hand-solved three-bus case
    R05,Risk_Manager,daily risk pack,VaR ES and stress losses against limits,positions and factor history,EX-081,component VaR sums to portfolio VaR
    R06,Scheduler,volume reconciliation,contracted scheduled delivered break report,trades nominations actuals,EX-075,every break above tolerance is listed
    R07,Quant_Analyst,study turnaround,faster runs with proven identical results,model inputs and baseline outputs,EX-092,relative objective difference below 1e-6 and zero constraint violation
    R08,Data_Engineer,market data onboarding,validated curated prices with lineage,raw vendor files,EX-070,rejected and superseded records are retained with reasons""")
    seq = {e["id"]: e for e in yaml.safe_load((ROOT / "curriculum/exercise_delivery_sequence.yaml").read_text())["exercises"]}; tests = "".join(p.read_text() for p in (ROOT / "exercises/tests").glob("test_*.py"))
    spec["exercise_exists"] = spec.exercise.map(lambda e: (ROOT / f"exercises/scripts/ex{e[-3:]}.py").exists()); spec["automated_test"] = spec.exercise.map(lambda e: f'"ex{e[-3:]}"' in tests); spec["tier"] = spec.exercise.map(lambda e: seq[e]["tier"])
    md = [f"# EX-096 Integrated gas, NGL and power analytics: product specification ({LABEL})\n", "Hypothetical product. Each requirement is traceable to a working exercise and an automated test in this repository.\n"]
    for x in spec.itertuples(): md.append(f"## {x.req_id} {x.capability}\n- User: {x.user} | Workflow: {x.workflow}\n- Data required: {x.data_required}\n- Acceptance: {x.acceptance_criterion}\n- Evidence: {x.exercise} (exists: {x.exercise_exists}, automated test: {x.automated_test})\n")
    (ROOT / "product_management/requirements/ex096_product_spec.md").write_text("\n".join(md))
    r = {"requirements": len(spec), "distinct_users": int(spec.user.nunique()), "requirements_with_working_exercise": int(spec.exercise_exists.sum()), "requirements_with_automated_test": int(spec.automated_test.sum()), "untested_requirements": ",".join(spec.req_id[~spec.automated_test]) or "none", "tier1_backed_requirements": int((spec.tier == 1).sum())}
    return finish("ex096", r, {"traceability_matrix": spec}, ["A requirement without an executable acceptance test is an opinion; this matrix makes the gap visible. Users and workflows are illustrative, not interview findings."])
if __name__ == "__main__": run()
