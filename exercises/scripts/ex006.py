"""EX-006 Wholesale to retail: build a retail supply cost from wholesale components and compare three retail structures under a wholesale price shock."""
from common import *
def run(shock_pct=50.0):
    c = data("ex006_cost_stack.csv", "component,USD_per_MWh,scales_with_wholesale_energy\nwholesale_energy,45,Yes\nlosses,2.7,Yes\ncapacity,9,No\nancillary_services,2,No\ntransmission,14,No\nrenewable_compliance,5,No\ndistribution,38,No\nretail_margin,6,No")
    base = c.USD_per_MWh.sum(); shocked = (c.USD_per_MWh * np.where(c.scales_with_wholesale_energy == "Yes", 1 + shock_pct / 100, 1)).sum()
    s = pd.DataFrame([{"structure": "regulated_utility_average_cost", "customer_rate_change_pct_now": 0.0, "who_carries_shock_now": "utility until fuel-clause true-up"}, {"structure": "competitive_fixed_price_retail", "customer_rate_change_pct_now": 0.0, "who_carries_shock_now": "retailer (unless hedged)"},
                      {"structure": "index_pass_through_retail", "customer_rate_change_pct_now": (shocked / base - 1) * 100, "who_carries_shock_now": "customer"}]); s["supplier_margin_USD_per_MWh_now"] = [base - shocked, base - shocked, 0.0]; s.loc[2, "supplier_margin_USD_per_MWh_now"] = float(c.USD_per_MWh[c.component == "retail_margin"].iloc[0])
    r = {"retail_cost_USD_per_MWh": base, "wholesale_energy_share_pct": 45 / base * 100, "shock_pct": shock_pct, "retail_cost_after_shock": shocked, "retail_cost_change_pct": (shocked / base - 1) * 100, "unhedged_fixed_retailer_loss_USD_per_MWh": shocked - base, "pass_through_ratio": (shocked / base - 1) * 100 / shock_pct}
    return finish("ex006", r, {"cost_stack": c, "structures": s}, ["A 50% wholesale move changes the retail cost far less because most of the bill is not energy.", "Synthetic cost stack; real tariffs differ by state and utility."])
if __name__ == "__main__": run()
