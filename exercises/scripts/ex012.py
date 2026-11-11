"""EX-012 Wellhead-to-market economics: realised wellhead price after transport, fuel retention, gathering and processing, by sales route."""
from common import *
def run(volume_MMBtu_d=100000):
    d = data("ex012_routes.csv", "route,hub_price_USD_per_MMBtu,transport_rate_USD_per_MMBtu,fuel_retention_pct,gathering_USD_per_MMBtu,processing_USD_per_MMBtu,capacity_MMBtu_d\nSell_at_Waha,1.10,0.00,0.0,0.25,0.15,100000\nFirm_to_Gulf_Coast,3.15,0.60,2.0,0.25,0.15,60000\nFirm_to_West,3.60,0.85,3.5,0.25,0.15,30000")
    d["delivered_fraction"] = 1 - d.fuel_retention_pct / 100; d["wellhead_netback_USD_per_MMBtu"] = d.hub_price_USD_per_MMBtu * d.delivered_fraction - d.transport_rate_USD_per_MMBtu - d.gathering_USD_per_MMBtu - d.processing_USD_per_MMBtu
    d = d.sort_values("wellhead_netback_USD_per_MMBtu", ascending=False).reset_index(drop=True); left = volume_MMBtu_d; alloc = []
    for cap in d.capacity_MMBtu_d: q = min(cap, left); alloc.append(q); left -= q
    d["allocated_MMBtu_d"] = alloc; d["revenue_USD_per_d"] = d.allocated_MMBtu_d * d.wellhead_netback_USD_per_MMBtu; local = float(d.wellhead_netback_USD_per_MMBtu[d.route == "Sell_at_Waha"].iloc[0])
    r = {f"{x.route}_netback": x.wellhead_netback_USD_per_MMBtu for x in d.itertuples()} | {"blended_netback_USD_per_MMBtu": float(d.revenue_USD_per_d.sum() / volume_MMBtu_d), "local_only_netback": local, "value_of_firm_transport_USD_per_d": float(d.revenue_USD_per_d.sum() - local * volume_MMBtu_d), "unallocated_MMBtu_d": float(left)}
    return finish("ex012", r, {"route_netbacks": d}, ["Fuel retention is paid in kind: the shipper delivers less gas than it receives.", "Synthetic rates; reservation charges treated as per-unit at full use."])
if __name__ == "__main__": run()
