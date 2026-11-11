"""Merit-order dispatch and a two-bus DC optimal power flow with LMPs from LP duals."""
import pandas as pd
from scipy.optimize import linprog

def merit_order(stack, demand, cap="available_capacity_MW", cost="marginal_cost_USD_per_MWh"):
    s = stack.sort_values([cost, cap], kind="stable").copy(); left, out = demand, []
    for q in s[cap]: g = min(q, left); out.append(g); left -= g
    s["dispatch_MW"] = out; on = s[s.dispatch_MW > 0]
    return s, (float(on[cost].iloc[-1]) if len(on) else 0.0), float(left)

def two_bus(cA, capA, cB, capB, loadA, loadB, limit):
    """min cA*gA + cB*gB  s.t.  gA - f = loadA ; gB + f = loadB ; |f| <= limit. LMP = dual of each bus balance."""
    r = linprog([cA, cB, 0], A_eq=[[1, 0, -1], [0, 1, 1]], b_eq=[loadA, loadB],
                bounds=[(0, capA), (0, capB), (-limit, limit)], method="highs")
    if r.status != 0: raise RuntimeError(r.message)
    gA, gB, f = r.x; lA, lB = r.eqlin.marginals
    return {"gen_A_MW": gA, "gen_B_MW": gB, "flow_A_to_B_MW": f, "lmp_A": lA, "lmp_B": lB,
            "congestion_component_B": lB - lA, "congestion_rent_USD_per_h": (lB - lA) * f, "cost_USD_per_h": r.fun}
