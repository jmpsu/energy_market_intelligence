"""EX-025 Gas storage arbitrage: implied schedule from the supplied inventory path, economics with fuel and fees, LP optimum."""
from common import *
from scipy.optimize import linprog
def economics(price, inj, wd, p):
    bought = inj / (1 - p["injection_fuel_loss"]); sold = wd * (1 - p["withdrawal_fuel_loss"])
    purchase, revenue = float(bought @ price), float(sold @ price); fees = float(inj.sum() * p["injection_cost"] + wd.sum() * p["withdrawal_cost"])
    return {"purchase_cost_USD": purchase, "sales_revenue_USD": revenue, "operating_fees_USD": fees, "gross_margin_USD": revenue - purchase, "net_margin_USD": revenue - purchase - fees}
def run():
    d = load("gas_storage.csv"); p = params("ex025_storage_assumptions.csv"); price = d.market_price_USD_per_MMBtu.values; n = len(d)
    inv = d.storage_inventory_MMBtu.values.astype(float); I0 = inv[-1]            # inventory read as END-of-month, opening = December close
    flow = np.diff(np.concatenate([[I0], inv])); inj, wd = np.maximum(flow, 0), np.maximum(-flow, 0)
    d["injection_MMBtu"], d["withdrawal_MMBtu"] = inj, wd
    d["within_limits"] = (inj <= d.injection_capacity_MMBtu) & (wd <= d.withdrawal_capacity_MMBtu) & (inv <= p["maximum_inventory"]) & (inv >= 0)
    e = economics(price, inj, wd, p)
    c = np.concatenate([price / (1 - p["injection_fuel_loss"]) + p["injection_cost"], -(price * (1 - p["withdrawal_fuel_loss"]) - p["withdrawal_cost"])])
    cum = np.tril(np.ones((n, n))); A = np.hstack([cum, -cum])                    # inventory_m = I0 + cum(inj - wd)
    res = linprog(c, A_ub=np.vstack([A, -A]), b_ub=np.concatenate([np.full(n, p["maximum_inventory"] - I0), np.full(n, I0)]),
                  A_eq=A[-1:], b_eq=[0], bounds=[(0, k) for k in d.injection_capacity_MMBtu] + [(0, k) for k in d.withdrawal_capacity_MMBtu], method="highs")
    oi, ow = res.x[:n], res.x[n:]; d["optimal_injection_MMBtu"], d["optimal_withdrawal_MMBtu"] = oi.round(3), ow.round(3)
    d["optimal_inventory_MMBtu"] = (I0 + np.cumsum(oi - ow)).round(3); eo = economics(price, oi, ow, p)
    chart("ex025", "inventory_vs_price", d.assign(inventory_10k_MMBtu=inv / 1e4), "month", ["inventory_10k_MMBtu", "market_price_USD_per_MMBtu"], title="Inventory (10k MMBtu) vs price")
    r = {"interpretation": "inventory = end-of-month; opening = December close", "all_months_within_limits": bool(d.within_limits.all()),
         "total_injected_MMBtu": float(inj.sum()), "total_withdrawn_MMBtu": float(wd.sum())} | e | {"no_storage_margin_USD": 0.0, "lp_optimal_net_margin_USD": eo["net_margin_USD"],
         "lp_optimal_cycled_MMBtu": float(oi.sum())}
    return finish("ex025", r, {"storage_schedule": d}, ["Read as start-of-month, the supplied inventory path violates September and October capacity limits; end-of-month is the only reading consistent with the limits.",
                  "No discounting, no bid-offer, forward prices assumed locked in (intrinsic value only)."])
if __name__ == "__main__": run()
