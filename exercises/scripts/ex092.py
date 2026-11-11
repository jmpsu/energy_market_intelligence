"""EX-092 Simulation performance benchmark: same multi-scenario ramp-constrained dispatch LP run two ways, with result-equivalence validation.
Baseline: reload inputs per scenario, dense matrices built with Python loops, presolve off, loop-based outputs.
Optimised: cached inputs, sparse matrices built once, only the demand right-hand side changes, presolve on, vectorised outputs."""
from common import *
import time, tracemalloc
from scipy import sparse
from scipy.optimize import linprog
SCALES = np.linspace(0.85, 1.10, 12)
def read(): return load("ex092_generators.csv"), load("ex092_demand.csv")
def baseline():
    t = dict(load=0.0, preprocess=0.0, solve=0.0, output=0.0); obj, nit, viol = [], 0, 0.0
    for sc in SCALES:
        a = time.perf_counter(); g, dm = read(); G, T = len(g), len(dm); b = time.perf_counter()
        Aeq = np.zeros((T, T * G)); Aub = np.zeros((2 * (T - 1) * G, T * G)); bub = np.zeros(2 * (T - 1) * G); k = 0
        for h in range(T):
            for i in range(G): Aeq[h, h * G + i] = 1.0
        for h in range(1, T):
            for i in range(G):
                Aub[k, h * G + i], Aub[k, (h - 1) * G + i], bub[k] = 1.0, -1.0, g.ramp_MW_per_h[i]; k += 1
                Aub[k, h * G + i], Aub[k, (h - 1) * G + i], bub[k] = -1.0, 1.0, g.ramp_MW_per_h[i]; k += 1
        cost = [g.cost_USD_per_MWh[i] for _ in range(T) for i in range(G)]; bounds = [(0, g.capacity_MW[i]) for _ in range(T) for i in range(G)]; c = time.perf_counter()
        r = linprog(cost, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=dm.demand_MW.values * sc, bounds=bounds, method="highs", options={"presolve": False}); d = time.perf_counter()
        tot = 0.0
        for h in range(T):
            for i in range(G): tot += r.x[h * G + i] * g.cost_USD_per_MWh[i]
        viol = max(viol, float(np.abs(Aeq @ r.x - dm.demand_MW.values * sc).max()), float(np.maximum(Aub @ r.x - bub, 0).max())); e = time.perf_counter()
        obj.append(tot); nit += r.nit; t["load"] += b - a; t["preprocess"] += c - b; t["solve"] += d - c; t["output"] += e - d
    return t, np.array(obj), nit, viol
def optimised():
    t = dict(load=0.0, preprocess=0.0, solve=0.0, output=0.0); a = time.perf_counter(); g, dm = read(); G, T = len(g), len(dm); b = time.perf_counter()
    Aeq = sparse.kron(sparse.eye(T, dtype=float), np.ones((1, G)), format="csr"); D = sparse.kron(sparse.diags([-1.0, 1.0], [0, 1], shape=(T - 1, T)), sparse.eye(G, dtype=float), format="csr")
    Aub = sparse.vstack([D, -D], format="csr"); bub = np.tile(g.ramp_MW_per_h.values, 2 * (T - 1)); cost = np.tile(g.cost_USD_per_MWh.values, T); bounds = np.column_stack([np.zeros(T * G), np.tile(g.capacity_MW.values, T)])
    c = time.perf_counter(); t["load"], t["preprocess"] = b - a, c - b; obj, nit, viol = [], 0, 0.0
    for sc in SCALES:
        d0 = time.perf_counter(); r = linprog(cost, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=dm.demand_MW.values * sc, bounds=bounds, method="highs"); d1 = time.perf_counter()
        obj.append(float(cost @ r.x)); viol = max(viol, float(np.abs(Aeq @ r.x - dm.demand_MW.values * sc).max()), float(np.maximum(Aub @ r.x - bub, 0).max())); d2 = time.perf_counter()
        nit += r.nit; t["solve"] += d1 - d0; t["output"] += d2 - d1
    return t, np.array(obj), nit, viol
def measure(fn):
    tracemalloc.start(); t0 = time.perf_counter(); out = fn(); wall = time.perf_counter() - t0; peak = tracemalloc.get_traced_memory()[1] / 1e6; tracemalloc.stop(); return out, wall, peak
def run():
    (tb, ob, nb, vb), wb, mb = measure(baseline); (to, oo, no, vo), wo, mo = measure(optimised); rel = float(np.abs(ob - oo).max() / np.abs(ob).max())
    t = pd.DataFrame([{"config": "baseline", "wall_s": wb, "peak_memory_MB": mb, "simplex_iterations": nb, "max_constraint_violation": vb} | {f"{k}_s": v for k, v in tb.items()},
                      {"config": "optimised", "wall_s": wo, "peak_memory_MB": mo, "simplex_iterations": no, "max_constraint_violation": vo} | {f"{k}_s": v for k, v in to.items()}])
    t.to_csv(ROOT / "reports/model_validation/ex092_benchmark.csv", index=False)
    pd.DataFrame({"demand_scale": SCALES, "baseline_objective_USD": ob, "optimised_objective_USD": oo}).to_csv(ROOT / "reports/model_validation/ex092_objective_equivalence.csv", index=False)
    r = {"scenarios": len(SCALES), "variables_per_scenario": 864, "max_relative_objective_difference": rel, "results_equivalent": bool(rel < 1e-6), "max_constraint_violation": max(vb, vo),
         "constraints_satisfied": bool(max(vb, vo) < 1e-6), "speedup_x": wb / wo, "memory_ratio": mb / mo, "baseline_wall_s": wb, "optimised_wall_s": wo}
    return finish("ex092", r, {"benchmark": t}, ["Timings vary by machine and run; only the equivalence and feasibility results are deterministic.", "The 5-8 hour to 30 minute target in the brief is a hypothetical scenario; this toy problem demonstrates the measurement method, not that ratio.",
                  "Not tested here: parallel scenario execution, decomposition, warm starts, reduced temporal/spatial resolution, incremental recalculation."])
if __name__ == "__main__": run()
