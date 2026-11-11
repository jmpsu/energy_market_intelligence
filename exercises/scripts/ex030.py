"""EX-030 Operational Flow Order: shipper imbalances, tolerance breaches, penalties, pro-rata capacity allocation."""
from common import *
def run():
    d = load("operational_flow_order.csv"); p = params("ex030_pipeline_operating_assumptions.csv")
    d["net_imbalance_MMBtu"] = d.actual_receipts_MMBtu - d.actual_deliveries_MMBtu       # + = long on the pipe (packing), - = short (drafting)
    d["imbalance_pct_of_scheduled"] = d.net_imbalance_MMBtu / d.scheduled_MMBtu * 100
    d["tolerance_MMBtu"] = d.scheduled_MMBtu * d.allowable_imbalance_percent / 100
    d["excess_MMBtu"] = np.maximum(d.net_imbalance_MMBtu.abs() - d.tolerance_MMBtu, 0); d["out_of_tolerance"] = d.excess_MMBtu > 0
    d["penalty_USD"] = d.excess_MMBtu * p["imbalance_penalty"]
    d["required_action"] = np.where(~d.out_of_tolerance, "none", np.where(d.net_imbalance_MMBtu > 0, "reduce receipts / increase deliveries", "increase receipts / reduce deliveries"))
    d["allocated_capacity_MMBtu"] = d.scheduled_MMBtu / d.scheduled_MMBtu.sum() * min(p["restricted_capacity"], d.scheduled_MMBtu.sum())
    r = {f"{x.shipper}_imbalance_MMBtu": x.net_imbalance_MMBtu for x in d.itertuples()} | {f"{x.shipper}_penalty_USD": x.penalty_USD for x in d.itertuples()}
    r |= {"shippers_out_of_tolerance": int(d.out_of_tolerance.sum()), "total_penalty_USD": float(d.penalty_USD.sum()), "allocation_rule": "pro-rata by scheduled quantity",
          "total_curtailed_MMBtu": float(d.scheduled_MMBtu.sum() - d.allocated_capacity_MMBtu.sum())}
    return finish("ex030", r, {"ofo_compliance": d}, ["Penalty applied only to volume beyond tolerance; actual tariffs differ by pipeline and tier."])
if __name__ == "__main__": run()
