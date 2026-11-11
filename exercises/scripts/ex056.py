"""EX-056 Transmission congestion on a three-bus loop: DC-OPF, PTDFs, LMP = energy + congestion, congestion rent, FTR payout."""
from common import *
from market_models.electricity.dcopf import solve
def run(l13_limit=None):
    b, l, ftr = load("ex056_buses.csv"), load("ex056_lines.csv"), load("ex056_ftr.csv"); l["limit_MW"] = l.limit_MW.astype(float)
    if l13_limit is not None: l.loc[l.line == "L13", "limit_MW"] = l13_limit
    s = solve(b, l); unc = solve(b, l.assign(limit_MW=1e6)); bus = b.assign(gen_MW=s["gen"].round(6), lmp=s["lmp"].round(6), energy_component=s["energy"], congestion_component=s["congestion"].round(6), unconstrained_gen_MW=unc["gen"].round(6), unconstrained_lmp=unc["lmp"].round(6))
    line = l.assign(flow_MW=s["flow"].round(6), shadow_price=s["shadow_price"].round(6), binding=np.abs(s["flow"]) >= l.limit_MW - 1e-6); pt = pd.DataFrame(s["ptdf"].round(6), columns=[f"bus_{x}" for x in b.bus]); pt.insert(0, "line", l.line)
    lmp = dict(zip(b.bus, s["lmp"])); ftr["payout_USD_per_h"] = [(lmp[x.sink_bus] - lmp[x.source_bus]) * x.MW for x in ftr.itertuples()]
    load_pay, gen_rev = float((bus.lmp * bus.load_MW).sum()), float((bus.lmp * bus.gen_MW).sum())
    r = {f"lmp_bus_{x.bus}": x.lmp for x in bus.itertuples()} | {f"gen_bus_{x.bus}_MW": x.gen_MW for x in bus.itertuples() if x.gen_capacity_MW > 0} | {f"flow_{x.line}_MW": x.flow_MW for x in line.itertuples()}
    r |= {"binding_lines": ",".join(line.line[line.binding]) or "none", "L13_shadow_price_USD_per_MW": float(line.shadow_price[line.line == "L13"].iloc[0]), "dispatch_cost_USD_per_h": s["cost"], "unconstrained_cost_USD_per_h": unc["cost"], "congestion_cost_USD_per_h": s["cost"] - unc["cost"],
          "load_payment_USD_per_h": load_pay, "generator_revenue_USD_per_h": gen_rev, "congestion_rent_USD_per_h": load_pay - gen_rev, "ftr_payout_USD_per_h": float(ftr.payout_USD_per_h.sum()), "ftr_revenue_adequate": bool(ftr.payout_USD_per_h.sum() <= load_pay - gen_rev + 1e-6)}
    return finish("ex056", r, {"bus_results": bus, "line_results": line, "ptdf": pt, "ftr_settlement": ftr}, ["The load bus price (80) exceeds the cost of every generator (20 and 50): serving 1 more MW at bus 3 needs +2 MW at bus 2 and -1 MW at bus 1 to hold the line at its limit.",
                  "Lossless DC approximation, no contingencies (N-1), no reserves; reference bus = bus 3."])
if __name__ == "__main__": run()
