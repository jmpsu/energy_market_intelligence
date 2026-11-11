"""EX-061 Gas unit commitment over a day: one contiguous run with start cost and minimum run time (exhaustive search) vs the hourly spark-spread rule."""
from common import *
def best_block(margin, cap, start_cost, min_run):
    best = (0.0, None, None)
    for s in range(len(margin)):
        for e in range(s + min_run - 1, len(margin)):
            v = float(margin[s:e + 1].sum() * cap - start_cost)
            if v > best[0]: best = (v, s + 1, e + 1)
    return best
def run(heat_rate=7.2, gas_price=3.25, vom=3.0, capacity_MW=500, start_cost=20000.0, min_run_hours=4):
    d = load("capstone_power_market.csv")[["hour", "market_price_USD_per_MWh"]]; d["margin_USD_per_MWh"] = d.market_price_USD_per_MWh - heat_rate * gas_price - vom; v, s, e = best_block(d.margin_USD_per_MWh.values, capacity_MW, start_cost, int(min_run_hours))
    d["hourly_rule_on"] = d.margin_USD_per_MWh > 0; d["committed_on"] = d.hour.between(s, e) if s else False; naive = float(d.margin_USD_per_MWh[d.hourly_rule_on].sum() * capacity_MW); starts = int((d.hourly_rule_on & ~d.hourly_rule_on.shift(fill_value=False)).sum())
    r = {"marginal_cost_USD_per_MWh": heat_rate * gas_price + vom, "committed_start_hour": s or 0, "committed_end_hour": e or 0, "committed_run_hours": (e - s + 1) if s else 0, "committed_profit_USD": v, "hourly_rule_gross_margin_USD": naive, "hourly_rule_starts": starts,
         "hourly_rule_profit_after_start_costs_USD": naive - starts * start_cost, "loss_making_hours_run_through": int(((d.margin_USD_per_MWh <= 0) & d.committed_on).sum()), "fuel_burn_MMBtu": ((e - s + 1) if s else 0) * capacity_MW * heat_rate}
    return finish("ex061", r, {"commitment": d}, ["Single start, full load when on, perfect foresight. A real unit-commitment model adds minimum load, ramping, multiple starts and minimum down time (mixed-integer)."])
if __name__ == "__main__": run()
