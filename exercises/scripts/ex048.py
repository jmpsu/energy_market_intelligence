"""EX-048 LMP on a two-bus system: LP dispatch, LMP from balance-constraint duals, congestion component and rent."""
from common import *
from market_models.electricity.dispatch import two_bus
def run(limit=None):
    p = params("ex048_two_bus.csv"); args = (p["gen_A_cost"], p["gen_A_capacity"], p["gen_B_cost"], p["gen_B_capacity"], p["load_A"], p["load_B"])
    con = two_bus(*args, p["line_limit_A_to_B"] if limit is None else limit); unc = two_bus(*args, 1e6)
    t = pd.DataFrame([{"case": "constrained"} | con, {"case": "unconstrained"} | unc]); t["energy_component"] = t.lmp_A; t["loss_component"] = 0.0
    t["load_payment_USD_per_h"] = t.lmp_A * p["load_A"] + t.lmp_B * p["load_B"]; t["generator_revenue_USD_per_h"] = t.lmp_A * t.gen_A_MW + t.lmp_B * t.gen_B_MW
    r = {f"{c}_{k}": float(v) for c, row in zip(t.case, t.to_dict("records")) for k, v in row.items() if k != "case"}
    r["congestion_cost_increase_USD_per_h"] = con["cost_USD_per_h"] - unc["cost_USD_per_h"]
    return finish("ex048", r, {"lmp_cases": t}, ["Lossless DC approximation: marginal loss component is zero by construction. Reference bus = A.", "Load payment minus generator revenue equals congestion rent, the pool that funds FTR/CRR holders."])
if __name__ == "__main__": run()
