"""EX-051 Capacity market: accredited capacity (ICAP x accreditation), capacity revenue, and a load-serving entity's obligation."""
from common import *
def run(clearing_price_USD_per_MW_day=150.0, peak_load_MW=600.0, reserve_margin=0.15):
    d = data("ex051_capacity_resources.csv", """resource,technology,installed_MW,accreditation_factor
    R1,gas_combined_cycle,500,0.95
    R2,solar,200,0.30
    R3,storage_4h,100,0.60
    R4,wind,300,0.18""")
    d["accredited_MW"] = d.installed_MW * d.accreditation_factor; d["annual_capacity_revenue_USD"] = d.accredited_MW * clearing_price_USD_per_MW_day * 365; d["revenue_USD_per_installed_kW_yr"] = d.annual_capacity_revenue_USD / d.installed_MW / 1000
    ucap = float(d.accredited_MW.sum()); ob = peak_load_MW * (1 + reserve_margin); short = ob - ucap
    r = {"installed_MW": float(d.installed_MW.sum()), "accredited_MW": ucap, "fleet_accreditation_pct": ucap / float(d.installed_MW.sum()) * 100, "annual_capacity_revenue_USD": float(d.annual_capacity_revenue_USD.sum()), "obligation_MW": ob, "position_MW": -short,
         "cost_to_cover_short_USD": max(short, 0) * clearing_price_USD_per_MW_day * 365, "gas_share_of_accredited_pct": float(d.accredited_MW.iloc[0] / ucap * 100), "solar_MW_to_replace_100_MW_gas_accredited": 100 * 0.95 / 0.30}
    return finish("ex051", r, {"capacity_resources": d}, ["Accreditation factors are synthetic; real values are set per market and change as penetration changes. 1,100 MW installed counts as 649 MW."])
if __name__ == "__main__": run()
