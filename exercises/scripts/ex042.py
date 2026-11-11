"""EX-042 Ethane cracker margin: feed cost per lb of ethylene = (price/gal / lb/gal) / yield; margin = ethylene price - feed cost + co-product credit - conversion cost."""
from common import *
def run(ethane_price=None, ethylene_price=None):
    f = load("ex042_cracker_feeds.csv"); p = params("ex042_assumptions.csv"); eth = p["ethylene_price"] if ethylene_price is None else ethylene_price
    if ethane_price is not None: f.loc[f.feed == "Ethane", "price_USD_per_gal"] = ethane_price
    f["feed_cost_c_per_lb_feed"] = f.price_USD_per_gal * 100 / f.lb_per_gal; f["feed_cost_c_per_lb_ethylene"] = f.feed_cost_c_per_lb_feed / f.ethylene_yield_lb_per_lb
    f["cash_cost_c_per_lb_ethylene"] = f.feed_cost_c_per_lb_ethylene - f.coproduct_credit_c_per_lb_ethylene + f.conversion_cost_c_per_lb_ethylene; f["margin_c_per_lb_ethylene"] = eth - f.cash_cost_c_per_lb_ethylene
    f["breakeven_feed_price_USD_per_gal"] = (eth + f.coproduct_credit_c_per_lb_ethylene - f.conversion_cost_c_per_lb_ethylene) * f.ethylene_yield_lb_per_lb * f.lb_per_gal / 100
    f["annual_margin_USD_million"] = f.margin_c_per_lb_ethylene / 100 * p["cracker_ethylene_capacity"]; f["feed_gal_per_lb_ethylene"] = 1 / (f.ethylene_yield_lb_per_lb * f.lb_per_gal)
    e = f.set_index("feed"); r = {f"{x.feed}_{k}": getattr(x, k) for x in f.itertuples() for k in ("feed_cost_c_per_lb_ethylene", "cash_cost_c_per_lb_ethylene", "margin_c_per_lb_ethylene", "breakeven_feed_price_USD_per_gal")}
    r |= {"preferred_feed": f.loc[f.margin_c_per_lb_ethylene.idxmax(), "feed"], "ethane_advantage_c_per_lb": float(e.margin_c_per_lb_ethylene["Ethane"] - e.margin_c_per_lb_ethylene["Propane"]),
          "ethane_annual_margin_USD_million": float(e.annual_margin_USD_million["Ethane"]), "ethane_feed_bbl_per_d_at_capacity": float(p["cracker_ethylene_capacity"] * 1e6 * e.feed_gal_per_lb_ethylene["Ethane"] / 42 / 365)}
    return finish("ex042", r, {"cracker_economics": f}, ["Yields, co-product credits and conversion costs are single-number synthetic assumptions; real crackers use full yield slates by feed and severity.", "Ethylene price is a hypothetical input, not a quote."])
if __name__ == "__main__": run()
