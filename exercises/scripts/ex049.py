"""EX-049 Market clearing: offer stack vs demand, uniform clearing price, producer surplus by unit."""
from common import *
from market_models.electricity.dispatch import merit_order
def run(demand_MW=4200):
    disp, price, unmet = merit_order(load("power_generation_stack.csv"), demand_MW); disp["revenue_USD_per_h"] = disp.dispatch_MW * price; disp["variable_cost_USD_per_h"] = disp.dispatch_MW * disp.marginal_cost_USD_per_MWh
    disp["producer_surplus_USD_per_h"] = disp.revenue_USD_per_h - disp.variable_cost_USD_per_h; disp["cumulative_MW"] = disp.available_capacity_MW.cumsum(); m = disp[disp.dispatch_MW > 0].iloc[-1]
    chart("ex049", "supply_stack", disp, "cumulative_MW", ["marginal_cost_USD_per_MWh"], title="Offer stack")
    r = {"clearing_price_USD_per_MWh": price, "marginal_unit": m.generator, "marginal_unit_dispatch_MW": float(m.dispatch_MW), "load_payment_USD_per_h": price * demand_MW, "production_cost_USD_per_h": float(disp.variable_cost_USD_per_h.sum()), "producer_surplus_USD_per_h": float(disp.producer_surplus_USD_per_h.sum()),
         "inframarginal_units": int((disp.producer_surplus_USD_per_h > 0).sum()), "unmet_MW": unmet, "MW_to_next_price_step": float(m.available_capacity_MW - m.dispatch_MW)}
    return finish("ex049", r, {"clearing": disp}, ["Offers assumed equal to marginal cost; single node, no reserves, inelastic demand. The marginal unit earns zero surplus."])
if __name__ == "__main__": run()
