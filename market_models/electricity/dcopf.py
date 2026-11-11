"""DC optimal power flow on an arbitrary small network with LMPs from LP duals (reused by EX-056)."""
import numpy as np
from scipy.optimize import linprog

def ptdf(buses, lines, slack):
    """PTDF[l, i] = MW on line l (from->to) per MW injected at bus i and withdrawn at the slack bus."""
    ids = list(buses); n = len(ids); ix = {b: k for k, b in enumerate(ids)}; B = np.zeros((n, n)); Bf = np.zeros((len(lines), n))
    for k, l in enumerate(lines.itertuples()):
        f, t, b = ix[l.from_bus], ix[l.to_bus], 1.0 / l.reactance_pu
        B[f, f] += b; B[t, t] += b; B[f, t] -= b; B[t, f] -= b; Bf[k, f], Bf[k, t] = b, -b
    keep = [k for k in range(n) if ids[k] != slack]; X = np.zeros((n, n)); X[np.ix_(keep, keep)] = np.linalg.inv(B[np.ix_(keep, keep)])
    return Bf @ X

def solve(buses, lines, slack=None):
    """buses: bus, load_MW, gen_capacity_MW, gen_cost_USD_per_MWh.  lines: line, from_bus, to_bus, reactance_pu, limit_MW."""
    slack = buses.bus.iloc[-1] if slack is None else slack; H = ptdf(buses.bus, lines, slack); load = buses.load_MW.values.astype(float); lim = lines.limit_MW.values.astype(float)
    r = linprog(buses.gen_cost_USD_per_MWh.values, A_eq=np.ones((1, len(buses))), b_eq=[load.sum()], A_ub=np.vstack([H, -H]), b_ub=np.concatenate([lim + H @ load, lim - H @ load]),
                bounds=[(0, c) for c in buses.gen_capacity_MW], method="highs")
    if r.status != 0: raise RuntimeError(r.message)
    L = len(lines); lam = r.eqlin.marginals[0]; mu = r.ineqlin.marginals[:L] - r.ineqlin.marginals[L:]      # d cost / d limit (<= 0 when binding in the + direction)
    lmp = lam + H.T @ mu; flow = H @ (r.x - load)
    return {"gen": r.x, "flow": flow, "lmp": lmp, "energy": lam, "congestion": lmp - lam, "shadow_price": mu, "cost": r.fun, "ptdf": H}
