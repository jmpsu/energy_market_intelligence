"""EX-093 Optimise model execution: on the EX-092 problem, test cached sequential, thread-parallel and reduced-temporal-resolution runs against the identical baseline, with result validation."""
from common import *
import time
from concurrent.futures import ThreadPoolExecutor
from scipy import sparse
from scipy.optimize import linprog
from ex092 import read, SCALES
def build(g, T, hours_per_step=1):
    G = len(g); Aeq = sparse.kron(sparse.eye(T, dtype=float), np.ones((1, G)), format="csr"); D = sparse.kron(sparse.diags([-1.0, 1.0], [0, 1], shape=(T - 1, T)), sparse.eye(G, dtype=float), format="csr")
    return Aeq, sparse.vstack([D, -D], format="csr"), np.tile(g.ramp_MW_per_h.values * hours_per_step, 2 * (T - 1)), np.tile(g.cost_USD_per_MWh.values * hours_per_step, T), np.column_stack([np.zeros(T * G), np.tile(g.capacity_MW.values, T)])
def solve_all(g, demand, hours_per_step=1, workers=1):
    Aeq, Aub, bub, cost, bounds = build(g, len(demand), hours_per_step); one = lambda sc: linprog(cost, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=demand * sc, bounds=bounds, method="highs").fun
    if workers == 1: return np.array([one(s) for s in SCALES])
    with ThreadPoolExecutor(int(workers)) as ex: return np.array(list(ex.map(one, SCALES)))
def run(workers=4):
    g, dm = read(); d = dm.demand_MW.values; out = {}
    for name, kw, dem in (("cached_sequential", {}, d), ("thread_parallel", {"workers": workers}, d), ("two_hour_resolution", {"hours_per_step": 2}, d.reshape(-1, 2).mean(axis=1))):
        t0 = time.perf_counter(); obj = solve_all(g, dem, **kw); out[name] = (time.perf_counter() - t0, obj)
    ref = out["cached_sequential"][1]; t = pd.DataFrame([{"variant": k, "wall_s": w, "max_relative_objective_difference": float(np.abs(o - ref).max() / np.abs(ref).max()), "variables_per_scenario": len(g) * (len(d) if k != "two_hour_resolution" else len(d) // 2)} for k, (w, o) in out.items()])
    t["speedup_vs_cached_sequential"] = t.wall_s.iloc[0] / t.wall_s; t["results_equivalent"] = t.max_relative_objective_difference < 1e-6; t.to_csv(ROOT / "reports/model_validation/ex093_variants.csv", index=False); e = t.set_index("variant")
    r = {"scenarios": len(SCALES), "parallel_results_equivalent": bool(e.results_equivalent["thread_parallel"]), "parallel_speedup": float(e.speedup_vs_cached_sequential["thread_parallel"]), "reduced_resolution_equivalent": bool(e.results_equivalent["two_hour_resolution"]),
         "reduced_resolution_objective_error_pct": float(e.max_relative_objective_difference["two_hour_resolution"] * 100), "reduced_resolution_speedup": float(e.speedup_vs_cached_sequential["two_hour_resolution"]), "reduced_resolution_variables": int(e.variables_per_scenario["two_hour_resolution"]), "safe_optimisations": "caching,parallel", "result_changing_optimisations": "temporal_resolution"}
    return finish("ex093", r, {"variants": t}, ["Timings vary by run and machine; equivalence flags are deterministic.", "Parallel execution leaves results unchanged. Halving temporal resolution is faster but changes the answer: it must be reported to the user as an approximation with a measured error, not shipped as a pure speed-up.",
                  "Not tested: decomposition, warm starts, spatial aggregation, incremental recalculation."])
if __name__ == "__main__": run()
