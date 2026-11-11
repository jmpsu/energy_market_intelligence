"""EX-032 LNG feed-gas demand: terminal capacity x utilisation -> feed gas, share of demand, and price effect via the EX-026 balance model."""
from common import *
from ex026 import price_after
def run(utilization_pct=None, base_price=3.25, base_demand=110.0, elasticity=0.25):
    d = data("ex032_terminals.csv", "terminal,region,capacity_Bcf_d,utilization_pct\nGulf_A,Gulf,4.5,92\nGulf_B,Gulf,3.0,95\nGulf_C,Gulf,5.0,88\nGulf_D_new,Gulf,2.5,40\nEast_A,East,0.8,90")
    if utilization_pct is not None: d["utilization_pct"] = float(utilization_pct)
    fuel = 1.10; d["lng_out_Bcf_d"] = d.capacity_Bcf_d * d.utilization_pct / 100; d["feed_gas_Bcf_d"] = d.lng_out_Bcf_d * fuel; base_feed = float(d.feed_gas_Bcf_d.sum()); full = float(d.capacity_Bcf_d.sum() * fuel); out = float(d.feed_gas_Bcf_d[d.terminal == "Gulf_C"].iloc[0])
    r = {"lng_capacity_Bcf_d": float(d.capacity_Bcf_d.sum()), "feed_gas_Bcf_d": base_feed, "feed_gas_share_of_demand_pct": base_feed / base_demand * 100, "gulf_share_of_feed_gas_pct": float(d.feed_gas_Bcf_d[d.region == "Gulf"].sum() / base_feed * 100), "feed_gas_at_full_utilization_Bcf_d": full,
         "price_if_all_terminals_full": price_after(base_price, base_demand, full - base_feed, elasticity), "price_if_Gulf_C_outage": price_after(base_price, base_demand, -out, elasticity), "new_train_rampup_adds_Bcf_d": float(2.5 * 0.6 * fuel)}
    return finish("ex032", r, {"terminals": d}, ["Feed gas = LNG output x 1.10 (liquefaction fuel and losses, assumed).", "Price effects inherit EX-026's assumed elasticity."])
if __name__ == "__main__": run()
