"""EX-011 Canadian gas supply: compare plays by production, growth, share and netback at AECO."""
from common import *
def run(aeco=2.15):
    d = data("ex011_canada_plays.csv", "play,production_2025_Bcf_d,production_2026_Bcf_d,full_cycle_cost_USD_per_MMBtu,transport_to_AECO_USD_per_MMBtu,liquids_credit_USD_per_MMBtu\nMontney,10.2,10.9,1.45,0.35,0.90\nDuvernay,0.9,1.0,1.90,0.30,1.60\nOther_WCSB,7.4,7.1,2.20,0.25,0.20")
    d["growth_pct"] = (d.production_2026_Bcf_d / d.production_2025_Bcf_d - 1) * 100; d["share_pct"] = d.production_2026_Bcf_d / d.production_2026_Bcf_d.sum() * 100
    d["netback_USD_per_MMBtu"] = aeco - d.transport_to_AECO_USD_per_MMBtu - d.full_cycle_cost_USD_per_MMBtu + d.liquids_credit_USD_per_MMBtu; d["netback_ex_liquids"] = d.netback_USD_per_MMBtu - d.liquids_credit_USD_per_MMBtu; d["breakeven_AECO"] = aeco - d.netback_USD_per_MMBtu
    r = {"total_2026_Bcf_d": float(d.production_2026_Bcf_d.sum()), "total_growth_pct": float((d.production_2026_Bcf_d.sum() / d.production_2025_Bcf_d.sum() - 1) * 100)} | {f"{x.play}_netback": x.netback_USD_per_MMBtu for x in d.itertuples()} | {f"{x.play}_share_pct": x.share_pct for x in d.itertuples()}
    r |= {"plays_positive_without_liquids": ",".join(d.play[d.netback_ex_liquids > 0]) or "none", "declining_plays": ",".join(d.play[d.growth_pct < 0])}
    return finish("ex011", r, {"canada_plays": d}, ["Synthetic volumes and costs. Liquids credit shows why liquids-rich plays grow at low gas prices."])
if __name__ == "__main__": run()
