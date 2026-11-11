"""EX-024 Physical and financial gas contracts: cash flows of an index purchase alone, with a futures hedge, with a swap, and with a basis swap."""
from common import *
def run(volume=310000, fixed=3.40, basis_fixed=-0.90):
    s = pd.DataFrame({"scenario": ["low", "base", "high"], "henry_hub_settle": [2.40, 3.40, 4.90], "hub_index": [1.20, 2.50, 4.60]}); s["actual_basis"] = s.hub_index - s.henry_hub_settle
    s["physical_index_cost"] = volume * s.hub_index; s["futures_or_swap_pnl"] = volume * (s.henry_hub_settle - fixed); s["basis_swap_pnl"] = volume * (s.actual_basis - basis_fixed)
    s["net_cost_unhedged"] = s.physical_index_cost; s["net_cost_hh_hedged"] = s.physical_index_cost - s.futures_or_swap_pnl; s["net_cost_fully_hedged"] = s.net_cost_hh_hedged - s.basis_swap_pnl
    for k in ("unhedged", "hh_hedged", "fully_hedged"): s[f"unit_cost_{k}"] = s[f"net_cost_{k}"] / volume
    r = {"locked_all_in_price": fixed + basis_fixed, "unhedged_cost_range_USD": float(s.net_cost_unhedged.max() - s.net_cost_unhedged.min()), "hh_hedged_cost_range_USD": float(s.net_cost_hh_hedged.max() - s.net_cost_hh_hedged.min()), "fully_hedged_cost_range_USD": float(s.net_cost_fully_hedged.max() - s.net_cost_fully_hedged.min()),
         "residual_risk_after_hh_hedge": "basis", "futures_margin_call_low_scenario_USD": float(-s.futures_or_swap_pnl.iloc[0]), "fully_hedged_unit_cost": float(s.unit_cost_fully_hedged.iloc[0])}
    assert abs(r["fully_hedged_cost_range_USD"]) < 1e-6
    return finish("ex024", r, {"cash_flows": s}, ["Futures and swap give the same settlement P&L here; they differ in margining, clearing and credit, not in payoff.", "A Henry Hub hedge on a regional purchase leaves basis risk; the basis swap removes it."])
if __name__ == "__main__": run()
