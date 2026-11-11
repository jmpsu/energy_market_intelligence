"""EX-090 Gas network minimum-cost flow, binding constraints, and a P003 capacity disruption."""
from common import *
import networkx as nx
from market_models.natural_gas.network import min_cost_flow
def run(edge="P003", cut=0.30):
    nodes, edges = load("gas_network_nodes.csv"), load("gas_network_edges.csv")
    f0, n0, c0 = min_cost_flow(nodes, edges); e2 = edges.copy(); e2["capacity_Bcf_d"] = e2.capacity_Bcf_d.astype(float); e2.loc[e2.edge_id == edge, "capacity_Bcf_d"] *= 1 - cut
    f1, n1, c1 = min_cost_flow(nodes, e2)
    g = nx.DiGraph(); [g.add_edge(e.from_node, e.to_node, label=f"{e.flow_Bcf_d:g}/{e.capacity_Bcf_d:g}") for e in f0.itertuples()]
    pos = nx.shell_layout(g); plt.figure(figsize=(9, 6)); nx.draw(g, pos, with_labels=True, node_size=2600, font_size=7, node_color="lightgrey")
    nx.draw_networkx_edge_labels(g, pos, nx.get_edge_attributes(g, "label"), font_size=7); plt.title("Synthetic gas network: flow/capacity Bcf/d")
    (DONE / "ex090").mkdir(exist_ok=True); plt.savefig(DONE / "ex090/network.png", dpi=130); plt.close()
    cmp = f0[["edge_id", "from_node", "to_node", "capacity_Bcf_d", "flow_Bcf_d", "binding"]].merge(f1[["edge_id", "capacity_Bcf_d", "flow_Bcf_d", "binding"]], on="edge_id", suffixes=("_base", "_disrupted"))
    r = {"base_transport_cost_USD_per_d": c0 * MMBTU_PER_BCF, "disrupted_transport_cost_USD_per_d": c1 * MMBTU_PER_BCF, "base_unmet_Bcf_d": float(n0.unmet_Bcf_d.sum()), "disrupted_unmet_Bcf_d": float(n1.unmet_Bcf_d.sum()),
         "base_binding_edges": ",".join(f0.edge_id[f0.binding]), "disrupted_binding_edges": ",".join(f1.edge_id[f1.binding]), "unmet_node": ",".join(n0.node_id[n0.unmet_Bcf_d > 1e-9]),
         f"{edge}_base_flow_Bcf_d": float(f0.flow_Bcf_d[f0.edge_id == edge].iloc[0]), f"{edge}_disrupted_capacity_Bcf_d": float(e2.capacity_Bcf_d[e2.edge_id == edge].iloc[0])}
    return finish("ex090", r, {"flow_comparison": cmp, "node_results_base": n0, "node_results_disrupted": n1}, ["The model delivers minimum demand only (cost minimisation with no revenue term).",
                  "HUB_WEST has 10 Bcf/d of inbound capacity against 15 Bcf/d minimum demand: a structural shortfall independent of the disruption.", "Transport model only: no pressure, linepack, compression fuel or storage inventory dynamics."])
if __name__ == "__main__": run()
