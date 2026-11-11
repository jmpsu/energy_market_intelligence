"""EX-059 Congestion revenue rights: expected vs realised congestion revenue and return on auction cost."""
from common import *
def run(hours=720):
    d = data("ex059_crr_portfolio.csv", """crr,MW,expected_congestion_USD_per_MWh,realized_congestion_USD_per_MWh,auction_cost_USD
    CRR1,25,2.0,3.1,30000
    CRR2,40,1.5,0.4,40000
    CRR3,10,4.0,-1.0,20000""")
    d["expected_revenue_USD"] = d.MW * hours * d.expected_congestion_USD_per_MWh; d["realized_revenue_USD"] = d.MW * hours * d.realized_congestion_USD_per_MWh; d["expected_profit_USD"] = d.expected_revenue_USD - d.auction_cost_USD
    d["realized_profit_USD"] = d.realized_revenue_USD - d.auction_cost_USD; d["forecast_error_USD"] = d.realized_revenue_USD - d.expected_revenue_USD; d["implied_auction_price_USD_per_MWh"] = d.auction_cost_USD / (d.MW * hours)
    r = {f"{x.crr}_realized_profit_USD": x.realized_profit_USD for x in d.itertuples()} | {"expected_revenue_USD": float(d.expected_revenue_USD.sum()), "realized_revenue_USD": float(d.realized_revenue_USD.sum()), "auction_cost_USD": float(d.auction_cost_USD.sum()), "expected_profit_USD": float(d.expected_profit_USD.sum()),
         "realized_profit_USD": float(d.realized_profit_USD.sum()), "return_on_cost_pct": float(d.realized_profit_USD.sum() / d.auction_cost_USD.sum() * 100), "profitable_crrs": ",".join(d.crr[d.realized_profit_USD > 0]), "obligations_paying_negative": ",".join(d.crr[d.realized_revenue_USD < 0])}
    return finish("ex059", r, {"crr_performance": d}, ["Portfolio expected +18,000 and realised -29,880: congestion forecasts drive CRR value, and an obligation can become a liability."])
if __name__ == "__main__": run()
