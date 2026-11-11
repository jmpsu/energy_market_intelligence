"""EX-040 Mont Belvieu vs Conway: regional basis and Conway-to-Belvieu arbitrage net of transport and handling."""
from common import *
def run():
    d = load("ngl_regional_prices.csv"); p = params("ex040_transportation_assumptions.csv")
    cost = p["pipeline_transport_cost"] + p["terminal_handling_cost"]
    d["basis_USD_per_gallon"] = d.mont_belvieu_USD_per_gallon - d.conway_USD_per_gallon; d["net_margin_USD_per_gallon"] = d.basis_USD_per_gallon - cost
    d["shipment_profit_USD"] = d.net_margin_USD_per_gallon * p["transport_volume"]; d["arb_open"] = d.net_margin_USD_per_gallon > 1e-12
    d["rank_within_date"] = d.groupby("date").net_margin_USD_per_gallon.rank(ascending=False).astype(int)
    r = {"logistics_cost_USD_per_gallon": cost} | {f"{x.date}_{x.product}_profit_USD": x.shipment_profit_USD for x in d.itertuples()}
    r |= {"products_never_positive": ",".join(sorted(set(d["product"]) - set(d["product"][d.arb_open]))), "best_shipment": "{date} {product}".format(**d.loc[d.shipment_profit_USD.idxmax()])}
    return finish("ex040", r, {"ngl_arbitrage": d}, ["Ignores pipeline capacity, product quality, timing between purchase and sale, and price impact."])
if __name__ == "__main__": run()
