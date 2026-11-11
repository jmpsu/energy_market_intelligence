"""EX-058 Financial transmission rights: obligation vs option payout from hourly congestion, against auction cost."""
from common import *
def run(mw=50, auction_cost=3000.0):
    cong = [0, 0, -4, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 20, 35, 15, 5, 0, 0, 0, 0]; d = pd.DataFrame({"hour": range(1, 25), "sink_minus_source_USD_per_MWh": cong})
    d["obligation_payout_USD"] = d.sink_minus_source_USD_per_MWh * mw; d["option_payout_USD"] = d.sink_minus_source_USD_per_MWh.clip(lower=0) * mw; ob, op = float(d.obligation_payout_USD.sum()), float(d.option_payout_USD.sum())
    r = {"obligation_payout_USD": ob, "option_payout_USD": op, "option_value_over_obligation_USD": op - ob, "auction_cost_USD": auction_cost, "obligation_profit_USD": ob - auction_cost, "breakeven_avg_congestion_USD_per_MWh": auction_cost / (mw * 24),
         "realized_avg_congestion_USD_per_MWh": float(d.sink_minus_source_USD_per_MWh.mean()), "counterflow_hours": int((d.sink_minus_source_USD_per_MWh < 0).sum()), "physical_hedge_net_congestion_USD": 0.0}
    return finish("ex058", r, {"ftr_settlement": d}, ["An obligation pays negative in counterflow hours; an option does not. A 50 MW physical schedule on the same path pays exactly the congestion the obligation returns: net zero."])
if __name__ == "__main__": run()
