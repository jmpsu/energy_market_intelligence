"""EX-073 Counterparty credit exposure: current exposure = max(MtM, 0) + receivables - collateral, against limits; concentration."""
from common import *
def run():
    d = data("ex073_counterparties.csv", """counterparty,mtm_USD,receivables_USD,collateral_held_USD,credit_limit_USD,rating
    CP_A,500000,200000,100000,500000,BBB
    CP_B,-300000,150000,0,400000,A
    CP_C,900000,0,500000,300000,BB
    CP_D,100000,50000,0,1000000,AA""")
    d["exposure_USD"] = (d.mtm_USD.clip(lower=0) + d.receivables_USD - d.collateral_held_USD).clip(lower=0); d["headroom_USD"] = d.credit_limit_USD - d.exposure_USD; d["utilization_pct"] = d.exposure_USD / d.credit_limit_USD * 100; d["breach"] = d.exposure_USD > d.credit_limit_USD
    d["share_of_total_pct"] = d.exposure_USD / d.exposure_USD.sum() * 100; d["collateral_call_USD"] = (-d.headroom_USD).clip(lower=0)
    r = {f"{x.counterparty}_exposure_USD": x.exposure_USD for x in d.itertuples()} | {"total_exposure_USD": float(d.exposure_USD.sum()), "breaches": ",".join(d.counterparty[d.breach]), "collateral_calls_USD": float(d.collateral_call_USD.sum()), "largest_share_pct": float(d.share_of_total_pct.max()),
         "largest_counterparty": d.loc[d.exposure_USD.idxmax(), "counterparty"], "sub_investment_grade_exposure_USD": float(d.exposure_USD[d.rating.isin(["BB", "B"])].sum())}
    return finish("ex073", r, {"credit_exposure": d}, ["Current exposure only: no potential future exposure (EX-083), no netting-agreement detail. A negative MtM is our liability, not exposure, so it floors at zero."])
if __name__ == "__main__": run()
