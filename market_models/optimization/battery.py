"""Battery / solar-plus-storage dispatch as a linear program (reused by EX-065 and EX-100)."""
import numpy as np
from scipy.optimize import linprog

def dispatch(prices, p_ch, p_dis, e_max, e_min, e0, rte, solar=None, grid_charge=False, var_cost=0.0):
    """Maximise sum(price*(solar - charge + discharge)) - var_cost*discharge.
    Variables per hour: charge c, discharge d, end-of-hour state of charge s.  s_t = s_{t-1} + rte*c_t - d_t.
    Round-trip loss is applied on charge. Terminal SOC must be >= initial SOC (no free energy)."""
    pr = np.asarray(prices, float); n = len(pr)
    sol = np.zeros(n) if solar is None else np.asarray(solar, float)
    cost = np.concatenate([pr, -(pr - var_cost), np.zeros(n)])
    A = np.zeros((n, 3 * n)); b = np.zeros(n)
    for t in range(n):
        A[t, t], A[t, n + t], A[t, 2 * n + t] = -rte, 1.0, 1.0
        if t: A[t, 2 * n + t - 1] = -1.0
        else: b[t] = e0
    cmax = np.full(n, p_ch) if grid_charge else np.minimum(p_ch, sol)
    bounds = [(0, c) for c in cmax] + [(0, p_dis)] * n + [(e_min, e_max)] * (n - 1) + [(max(e_min, e0), e_max)]
    r = linprog(cost, A_eq=A, b_eq=b, bounds=bounds, method="highs")
    if r.status != 0: raise RuntimeError(r.message)
    c, d, s = r.x[:n], r.x[n:2 * n], r.x[2 * n:]
    return {"charge": c, "discharge": d, "soc": s, "sales": sol - c + d,
            "revenue": float(pr @ (sol - c + d) - var_cost * d.sum())}
