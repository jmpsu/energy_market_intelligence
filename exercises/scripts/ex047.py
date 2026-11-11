"""EX-047 Day-ahead vs real-time: price spread statistics, two-settlement generator revenue, virtual (INC) trade P&L."""
from common import *
def run(virtual_mw=50):
    d = load("ex047_da_rt.csv"); d["dart_spread"] = d.da_price_USD_per_MWh - d.rt_price_USD_per_MWh; d["deviation_MW"] = d.rt_actual_MW - d.da_award_MW
    d["da_revenue_USD"] = d.da_award_MW * d.da_price_USD_per_MWh; d["rt_settlement_USD"] = d.deviation_MW * d.rt_price_USD_per_MWh; d["total_revenue_USD"] = d.da_revenue_USD + d.rt_settlement_USD
    d["rt_only_revenue_USD"] = d.rt_actual_MW * d.rt_price_USD_per_MWh; d["virtual_inc_pnl_USD"] = virtual_mw * d.dart_spread; d["peak"] = d.hour.between(15, 20)
    chart("ex047", "da_vs_rt", d, "hour", ["da_price_USD_per_MWh", "rt_price_USD_per_MWh"], title="Day-ahead vs real-time price")
    r = {"mean_da_price": float(d.da_price_USD_per_MWh.mean()), "mean_rt_price": float(d.rt_price_USD_per_MWh.mean()), "mean_dart_spread": float(d.dart_spread.mean()), "hours_rt_above_da": int((d.dart_spread < 0).sum()),
         "rt_price_std": float(d.rt_price_USD_per_MWh.std(ddof=1)), "da_price_std": float(d.da_price_USD_per_MWh.std(ddof=1)), "peak_mean_dart_spread": float(d.dart_spread[d.peak].mean()), "offpeak_mean_dart_spread": float(d.dart_spread[~d.peak].mean()),
         "da_revenue_USD": float(d.da_revenue_USD.sum()), "rt_settlement_USD": float(d.rt_settlement_USD.sum()), "two_settlement_revenue_USD": float(d.total_revenue_USD.sum()), "rt_only_revenue_USD": float(d.rt_only_revenue_USD.sum()),
         "outage_buyback_cost_USD": float(-d.rt_settlement_USD[d.deviation_MW < 0].sum()), "da_revenue_lost_equivalent_USD": float((-d.deviation_MW * d.da_price_USD_per_MWh)[d.deviation_MW < 0].sum()), "virtual_inc_pnl_USD": float(d.virtual_inc_pnl_USD.sum())}
    return finish("ex047", r, {"two_settlement": d}, ["One synthetic day; a DA-RT premium needs many days to estimate.", "A unit that trips in a high-price real-time hour buys back its day-ahead award at the real-time price: the buy-back cost exceeds the day-ahead revenue for those MWh."])
if __name__ == "__main__": run()
