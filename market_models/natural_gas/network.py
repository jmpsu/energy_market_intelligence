"""Minimum-cost gas network flow (transport model, no pressure physics) with unmet-demand slack."""
import numpy as np
from scipy.optimize import linprog

def min_cost_flow(nodes, edges, penalty=100.0):
    """Variables: flow per edge, supply per production node, delivery per market node, unmet per market node.
    Node balance: inflow + supply = outflow + delivery. delivery + unmet >= minimum demand; delivery <= maximum demand.
    Objective: transport cost + penalty*unmet (USD/MMBtu x Bcf/d; multiply by 1e6 for USD/d)."""
    N, E = list(nodes.node_id), len(edges); n = len(N); idx = {k: i for i, k in enumerate(N)}
    nv = E + 3 * n; A = np.zeros((n, nv))
    for j, e in enumerate(edges.itertuples()):
        A[idx[e.to_node], j] += 1; A[idx[e.from_node], j] -= 1
    for i in range(n): A[i, E + i] = 1; A[i, E + n + i] = -1
    Aub = np.zeros((n, nv)); bub = -nodes.minimum_demand_Bcf_d.values.astype(float)
    for i in range(n): Aub[i, E + n + i] = -1; Aub[i, E + 2 * n + i] = -1
    c = np.concatenate([edges.transport_cost_USD_per_MMBtu.values, np.zeros(2 * n), np.full(n, penalty)])
    bounds = ([(0, k) for k in edges.capacity_Bcf_d] + [(0, s) for s in nodes.maximum_supply_Bcf_d]
              + [(0, d) for d in nodes.maximum_demand_Bcf_d] + [(0, d) for d in nodes.minimum_demand_Bcf_d])
    r = linprog(c, A_eq=A, b_eq=np.zeros(n), A_ub=Aub, b_ub=bub, bounds=bounds, method="highs")
    if r.status != 0: raise RuntimeError(r.message)
    x = r.x; fl = edges.assign(flow_Bcf_d=x[:E].round(6)); fl["binding"] = fl.flow_Bcf_d >= fl.capacity_Bcf_d - 1e-9
    nd = nodes[["node_id"]].assign(supply_Bcf_d=x[E:E + n].round(6), delivery_Bcf_d=x[E + n:E + 2 * n].round(6), unmet_Bcf_d=x[E + 2 * n:].round(6))
    return fl, nd, float(edges.transport_cost_USD_per_MMBtu.values @ x[:E])
