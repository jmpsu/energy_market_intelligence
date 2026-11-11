"""EX-017 Pipeline maintenance outage: rerun the EX-090 network with a segment derated and measure flows, unmet demand and cost."""
from common import *
from market_models.natural_gas.network import min_cost_flow
def run(edge="P001", cut=0.5):
    nodes, edges = load("gas_network_nodes.csv"), load("gas_network_edges.csv"); edges["capacity_Bcf_d"] = edges.capacity_Bcf_d.astype(float); f0, n0, c0 = min_cost_flow(nodes, edges); e2 = edges.copy(); e2.loc[e2.edge_id == edge, "capacity_Bcf_d"] *= 1 - float(cut); f1, n1, c1 = min_cost_flow(nodes, e2)
    t = f0[["edge_id", "from_node", "to_node", "capacity_Bcf_d", "flow_Bcf_d"]].merge(f1[["edge_id", "capacity_Bcf_d", "flow_Bcf_d", "binding"]], on="edge_id", suffixes=("_base", "_outage")); t["flow_change_Bcf_d"] = t.flow_Bcf_d_outage - t.flow_Bcf_d_base
    d0, d1 = float(n0.delivery_Bcf_d.sum()), float(n1.delivery_Bcf_d.sum()); u = n1.assign(extra_unmet=n1.unmet_Bcf_d - n0.unmet_Bcf_d)
    r = {"edge": edge, "capacity_cut_Bcf_d": float(edges.capacity_Bcf_d[edges.edge_id == edge].iloc[0] * float(cut)), "base_cost_USD_per_d": c0 * 1e6, "outage_cost_USD_per_d": c1 * 1e6, "base_avg_cost_USD_per_MMBtu": c0 / d0, "outage_avg_cost_USD_per_MMBtu": c1 / d1,
         "extra_unmet_Bcf_d": float(n1.unmet_Bcf_d.sum() - n0.unmet_Bcf_d.sum()), "node_short": ",".join(u.node_id[u.extra_unmet > 1e-9]) or "none", "rerouted_edges": ",".join(t.edge_id[t.flow_change_Bcf_d > 1e-9]) or "none", "newly_binding": ",".join(t.edge_id[t.binding & (t.flow_Bcf_d_outage > t.flow_Bcf_d_base + 1e-9)]) or "none"}
    return finish("ex017", r, {"flow_comparison": t, "nodes_outage": n1}, ["Higher average delivered cost and unmet demand downstream are the model's stand-in for a basis blowout; no price is solved.", "Compare EX-090: that outage had no effect because the segment had spare capacity."])
if __name__ == "__main__": run()
