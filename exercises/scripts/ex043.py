"""EX-043 NGL transport optimisation: minimum-cost shipment across pipeline, rail, truck and marine arcs with capacity limits (LP)."""
from common import *
from scipy.optimize import linprog
def solve(nodes, arcs):
    N = list(nodes.node); A = np.zeros((len(N), len(arcs)))
    for j, a in enumerate(arcs.itertuples()): A[N.index(a.origin), j] = 1; A[N.index(a.destination), j] = -1
    r = linprog(arcs.cost_USD_per_bbl.values, A_eq=A, b_eq=(nodes.supply_bbl - nodes.demand_bbl).values, bounds=[(0, c) for c in arcs.capacity_bbl], method="highs")
    if r.status != 0: return None, float("nan")
    o = arcs.assign(shipped_bbl=r.x.round(4)); o["cost_USD"] = o.shipped_bbl * o.cost_USD_per_bbl; o["at_capacity"] = o.shipped_bbl >= o.capacity_bbl - 1e-6; return o, float(r.fun)
def run(outage_arc="A1", outage_frac=0.5):
    nodes, arcs = load("ex043_nodes.csv"), load("ex043_arcs.csv"); arcs["capacity_bbl"] = arcs.capacity_bbl.astype(float); base, c0 = solve(nodes, arcs)
    a2 = arcs.copy(); a2.loc[a2.arc_id == outage_arc, "capacity_bbl"] *= 1 - float(outage_frac); dis, c1 = solve(nodes, a2); vol = float(nodes.supply_bbl.sum())
    if dis is None:
        out_cap = a2.groupby("origin").capacity_bbl.sum(); stranded = {o: float(max(q - out_cap.get(o, 0), 0)) for o, q in zip(nodes.node, nodes.supply_bbl) if q > 0}
        return finish("ex043", {"base_total_cost_USD": c0, "outage_arc": outage_arc, "outage_feasible": False} | {f"stranded_at_{o}_bbl": v for o, v in stranded.items()}, {"shipment_plan": base},
                      ["With this outage the remaining arcs cannot move all supply: barrels are stranded at the origin (storage build, production shut-in or price collapse at that hub)."])
    mode = base.groupby("mode", as_index=False).agg(shipped_bbl=("shipped_bbl", "sum"), cost_USD=("cost_USD", "sum")); mode["avg_cost_USD_per_bbl"] = mode.cost_USD / mode.shipped_bbl.where(mode.shipped_bbl > 0)
    cmp = base[["arc_id", "origin", "destination", "mode", "capacity_bbl", "cost_USD_per_bbl", "shipped_bbl", "at_capacity"]].merge(dis[["arc_id", "capacity_bbl", "shipped_bbl"]], on="arc_id", suffixes=("_base", "_outage"))
    r = {"base_total_cost_USD": c0, "base_avg_cost_USD_per_bbl": c0 / vol, "base_arcs_at_capacity": ",".join(base.arc_id[base.at_capacity]), "outage_arc": outage_arc, "outage_total_cost_USD": c1, "outage_cost_increase_USD": c1 - c0,
         "outage_cost_increase_USD_per_bbl_lost": (c1 - c0) / max(float(arcs.capacity_bbl[arcs.arc_id == outage_arc].iloc[0]) * float(outage_frac), 1e-9), "truck_bbl_base": float(base.shipped_bbl[base["mode"] == "truck"].sum()), "truck_bbl_outage": float(dis.shipped_bbl[dis["mode"] == "truck"].sum())}
    r |= {f"base_{x.arc_id}_{x.mode}_bbl": x.shipped_bbl for x in base.itertuples()}
    return finish("ex043", r, {"shipment_plan": cmp, "mode_summary": mode}, ["Single period, single product, costs linear in volume; no minimum tenders, batching, railcar lease terms, demurrage or vessel lot sizes.", "The cost increase per barrel of lost pipeline capacity is the value of that capacity for the period: the number a shipper would compare with a tariff."])
if __name__ == "__main__": run()
