"""EX-020 Negative Waha prices: basis vs regional surplus after takeaway capacity and local demand."""
from common import *
def run():
    d = load("negative_waha_prices.csv")
    d["waha_basis_USD_per_MMBtu"] = d.waha_USD_per_MMBtu - d.henry_hub_USD_per_MMBtu
    d["surplus_Bcf_d"] = d.production_Bcf_d - d.pipeline_capacity_Bcf_d - d.regional_demand_Bcf_d
    d["revenue_gap_vs_HH_USD_per_d"] = -d.waha_basis_USD_per_MMBtu * d.production_Bcf_d * MMBTU_PER_BCF
    d["waha_revenue_USD_per_d"] = d.waha_USD_per_MMBtu * d.production_Bcf_d * MMBTU_PER_BCF
    corr = float(np.corrcoef(d.surplus_Bcf_d, d.waha_basis_USD_per_MMBtu)[0, 1]); slope = float(np.polyfit(d.surplus_Bcf_d, d.waha_basis_USD_per_MMBtu, 1)[0])
    chart("ex020", "surplus_vs_basis", d, "period", ["surplus_Bcf_d", "waha_basis_USD_per_MMBtu"], "bar", "Regional surplus and Waha basis")
    r = {f"{x.period}_basis": x.waha_basis_USD_per_MMBtu for x in d.itertuples()} | {f"{x.period}_surplus_Bcf_d": x.surplus_Bcf_d for x in d.itertuples()}
    r |= {"corr_surplus_basis": corr, "basis_slope_USD_per_Bcf_d": slope, "negative_price_periods": int((d.waha_USD_per_MMBtu < 0).sum()),
          "max_revenue_gap_USD_per_d": float(d.revenue_gap_vs_HH_USD_per_d.max())}
    return finish("ex020", r, {"waha_basis_analysis": d}, ["Four observations: the correlation is descriptive, not a calibrated price model."])
if __name__ == "__main__": run()
