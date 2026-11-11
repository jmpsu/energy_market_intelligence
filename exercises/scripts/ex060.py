"""EX-060 Generator outage: merit-order redispatch, clearing price and reserve margin before and after."""
from common import *
from market_models.electricity.dispatch import merit_order
def run():
    stack = load("power_generation_stack.csv"); sc = load("ex060_market_demand_assumptions.csv"); r, frames = {}, {}
    for s in sc.itertuples():
        st = stack[stack.generator != s.outage_generator]; disp, price, unmet = merit_order(st, s.demand_MW); cap = st.available_capacity_MW.sum()
        frames[f"dispatch_{s.scenario.lower()}"] = disp
        r |= {f"{s.scenario}_price_USD_per_MWh": price, f"{s.scenario}_available_capacity_MW": float(cap), f"{s.scenario}_reserve_margin_pct": (cap - s.demand_MW) / s.demand_MW * 100,
              f"{s.scenario}_unmet_MW": unmet, f"{s.scenario}_marginal_unit": disp[disp.dispatch_MW > 0].generator.iloc[-1], f"{s.scenario}_production_cost_USD_per_h": float((disp.dispatch_MW * disp.marginal_cost_USD_per_MWh).sum())}
    r["price_change_USD_per_MWh"] = r["Outage_price_USD_per_MWh"] - r["Baseline_price_USD_per_MWh"]
    r["load_payment_change_USD_per_h"] = r["price_change_USD_per_MWh"] * float(sc.demand_MW.iloc[0])
    return finish("ex060", r, frames, ["Single-node, single-hour, no reserves requirement, no transmission, wind and solar at full available capacity."])
if __name__ == "__main__": run()
