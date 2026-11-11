"""EX-015 Pipeline constraint: scheduled = min(requested, available); unscheduled volume and lost transport value."""
from common import *
def run(capacity_scale=1.0):
    d = load("pipeline_constraints.csv"); p = params("ex015_additional_pricing_assumptions.csv")
    cap = d.available_capacity_MMBtu * capacity_scale
    d["scheduled_MMBtu"] = np.minimum(d.requested_flow_MMBtu, cap); d["unscheduled_MMBtu"] = d.requested_flow_MMBtu - d.scheduled_MMBtu
    d["constrained"] = d.unscheduled_MMBtu > 0; d["supply_not_moved_MMBtu"] = d.upstream_supply_MMBtu - d.scheduled_MMBtu
    spread = p["unconstrained_downstream_price"] - p["upstream_price"]; net = spread - p["transport_cost"]
    chart("ex015", "flow_vs_capacity", d, "hour", ["requested_flow_MMBtu", "available_capacity_MMBtu", "scheduled_MMBtu"], title="Requested flow vs capacity")
    r = {"constrained_hours": ",".join(map(str, d.hour[d.constrained])), "total_unscheduled_MMBtu": float(d.unscheduled_MMBtu.sum()),
         "gross_spread_USD_per_MMBtu": spread, "net_transport_margin_USD_per_MMBtu": net, "lost_transport_value_USD": float(d.unscheduled_MMBtu.sum() * net),
         "constrained_spread_USD_per_MMBtu": p["constrained_downstream_price"] - p["upstream_price"]}
    return finish("ex015", r, {"pipeline_constraint_report": d}, ["Supplied constrained downstream price (3.50) is BELOW the unconstrained price (4.75); a downstream bottleneck normally raises the downstream price. Field semantics need clarification; lost value uses the unconstrained spread."])
if __name__ == "__main__": run()
