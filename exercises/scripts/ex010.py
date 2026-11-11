"""EX-010 Compare major US gas-producing basins: growth, netback, price sensitivity."""
from common import *
def run(price_shock=-0.50):
    d = load("us_gas_basins.csv")
    d["growth_pct"] = (d.production_2026_Bcf_d / d.production_2025_Bcf_d - 1) * 100
    d["netback_USD_per_MMBtu"] = (d.average_wellhead_price_USD_per_MMBtu - d.production_cost_USD_per_MMBtu
                                  - d.gathering_processing_USD_per_MMBtu - d.transport_cost_USD_per_MMBtu)
    d["netback_shocked_USD_per_MMBtu"] = d.netback_USD_per_MMBtu + price_shock
    d["daily_margin_USD"] = d.netback_USD_per_MMBtu * d.production_2026_Bcf_d * MMBTU_PER_BCF
    d["growth_rank"] = d.growth_pct.rank(ascending=False).astype(int); d["netback_rank"] = d.netback_USD_per_MMBtu.rank(ascending=False).astype(int)
    chart("ex010", "netback", d, "basin", ["netback_USD_per_MMBtu", "netback_shocked_USD_per_MMBtu"], "bar", "Modeled netback by basin")
    r = {f"{b.basin}_netback_USD_per_MMBtu": b.netback_USD_per_MMBtu for b in d.itertuples()}
    r |= {f"{b.basin}_growth_pct": b.growth_pct for b in d.itertuples()}
    r |= {"best_netback": d.loc[d.netback_USD_per_MMBtu.idxmax(), "basin"], "most_transport_exposed": d.loc[d.transport_cost_USD_per_MMBtu.idxmax(), "basin"],
          "basins_negative_after_shock": int((d.netback_shocked_USD_per_MMBtu < 0).sum())}
    return finish("ex010", r, {"basin_comparison": d}, ["The field is named wellhead price yet transport cost is deducted from it; confirm the price point definition before commercial use."])
if __name__ == "__main__": run()
