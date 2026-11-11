"""EX-057 Nodal vs zonal pricing on the EX-056 network: who pays and who is paid under each design."""
from common import *
from market_models.electricity.dcopf import solve
def run():
    b, l = load("ex056_buses.csv"), load("ex056_lines.csv"); nod = solve(b, l); unc = solve(b, l.assign(limit_MW=1e6)); zonal_price = float(unc["lmp"][0]); redispatch = nod["cost"] - unc["cost"]; loadmw = float(b.load_MW.sum())
    t = b[["bus"]].assign(nodal_lmp=nod["lmp"].round(6), nodal_gen_MW=nod["gen"].round(6), market_schedule_MW=unc["gen"].round(6)); t["nodal_revenue_USD_per_h"] = t.nodal_lmp * t.nodal_gen_MW; t["zonal_energy_revenue_USD_per_h"] = zonal_price * t.market_schedule_MW
    t["redispatch_MW"] = t.nodal_gen_MW - t.market_schedule_MW; cost = b.gen_cost_USD_per_MWh.values; t["zonal_redispatch_payment_USD_per_h"] = np.where(t.redispatch_MW > 0, t.redispatch_MW * cost, t.redispatch_MW * zonal_price) - np.where(t.redispatch_MW < 0, t.redispatch_MW * cost, 0)
    t["zonal_total_revenue_USD_per_h"] = t.zonal_energy_revenue_USD_per_h + t.zonal_redispatch_payment_USD_per_h; nodal_pay = float((nod["lmp"] * b.load_MW).sum()); zonal_pay = zonal_price * loadmw + redispatch
    r = {"zonal_price_USD_per_MWh": zonal_price, "redispatch_cost_USD_per_h": redispatch, "nodal_load_payment_USD_per_h": nodal_pay, "zonal_load_payment_USD_per_h": zonal_pay, "load_saving_under_zonal_USD_per_h": nodal_pay - zonal_pay, "nodal_congestion_rent_USD_per_h": nodal_pay - float((nod["lmp"] * nod["gen"]).sum()),
         "bus1_gen_constrained_off_MW": float(-t.redispatch_MW.iloc[0]), "bus1_zonal_profit_without_running_USD_per_h": float(-t.redispatch_MW.iloc[0]) * (zonal_price - cost[0]), "physical_dispatch_identical": True}
    return finish("ex057", r, {"design_comparison": t}, ["Same physical dispatch and production cost under both designs; what changes is the price signal at each location and who receives the congestion rent.",
                  "Zonal redispatch modelled as pay-as-bid up and buy-back at the zonal price down; actual redispatch rules differ by market."])
if __name__ == "__main__": run()
