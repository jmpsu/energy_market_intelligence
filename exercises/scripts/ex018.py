"""EX-018 North American gas infrastructure network: basins, pipelines, storage, LNG and hubs as a graph; max flow and critical links."""
from common import *
import networkx as nx
def run():
    e = load("gas_network_edges.csv")[["edge_id", "from_node", "to_node", "capacity_Bcf_d"]]; x = data("ex018_extra_edges.csv", "edge_id,from_node,to_node,capacity_Bcf_d\nP009,HUB_GULF,LNG_GULF,12\nP010,HUB_WEST,MEXICO_EXPORT,6\nP011,HUB_EAST,LDC_NORTHEAST,28\nP012,HUB_GULF,POWER_GULF,9")
    e = pd.concat([e, x], ignore_index=True); g = nx.from_pandas_edgelist(e, "from_node", "to_node", edge_attr="capacity_Bcf_d", create_using=nx.DiGraph)
    for s in ("APPALACHIA", "PERMIAN", "HAYNESVILLE"): g.add_edge("SRC", s, capacity_Bcf_d=float(load("gas_network_nodes.csv").set_index("node_id").maximum_supply_Bcf_d[s]))
    sinks = ["LNG_GULF", "MEXICO_EXPORT", "LDC_NORTHEAST", "POWER_GULF"]; mf = {s: nx.maximum_flow_value(g, "SRC", s, capacity="capacity_Bcf_d") for s in sinks}; cut = {s: nx.minimum_cut(g, "SRC", s, capacity="capacity_Bcf_d") for s in sinks}
    def cut_edges(s): a, b = cut[s][1]; return ",".join(sorted(f"{u}>{v}" for u, v in g.edges if u in a and v in b))
    n = pd.DataFrame({"node": [k for k in g if k != "SRC"]}); n["in_capacity_Bcf_d"] = [sum(d["capacity_Bcf_d"] for u, _, d in g.in_edges(k, data=True) if u != "SRC") for k in n.node]; n["out_capacity_Bcf_d"] = [sum(d["capacity_Bcf_d"] for *_, d in g.out_edges(k, data=True)) for k in n.node]; n["betweenness"] = n.node.map(nx.betweenness_centrality(g))
    r = {"nodes": len(n), "edges": len(e), "most_central_node": n.loc[n.betweenness.idxmax(), "node"]} | {f"max_flow_to_{s}_Bcf_d": float(v) for s, v in mf.items()} | {f"bottleneck_to_{s}": cut_edges(s) for s in sinks}
    return finish("ex018", r, {"edges": e, "nodes": n}, ["Max flow to each sink is computed alone (not simultaneous). The minimum cut names the links whose expansion would raise deliverability.", "Synthetic network extending EX-090."])
if __name__ == "__main__": run()
