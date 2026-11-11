"""EX-055 Spark spread = power price - heat rate x gas price - variable O&M; run when positive."""
from common import *
def run(output_mw=100, heat_rate=None, gas_shift=0.0):
    d = load("generator_spark_spreads.csv"); hr = d.heat_rate_MMBtu_per_MWh if heat_rate is None else heat_rate
    d["fuel_cost_USD_per_MWh"] = (d.gas_price_USD_per_MMBtu + gas_shift) * hr; d["variable_cost_USD_per_MWh"] = d.fuel_cost_USD_per_MWh + d.variable_O_and_M_USD_per_MWh
    d["spark_spread_USD_per_MWh"] = d.electricity_price_USD_per_MWh - d.variable_cost_USD_per_MWh; d["dispatch"] = d.spark_spread_USD_per_MWh > 0
    d["implied_market_heat_rate"] = d.electricity_price_USD_per_MWh / (d.gas_price_USD_per_MMBtu + gas_shift)
    d["gross_margin_USD"] = np.where(d.dispatch, d.spark_spread_USD_per_MWh * output_mw, 0.0)
    chart("ex055", "spark_spread", d, "hour", ["spark_spread_USD_per_MWh"], "bar", "Hourly spark spread")
    r = {f"hour_{x.hour}_spark_USD_per_MWh": x.spark_spread_USD_per_MWh for x in d.itertuples()}
    r |= {"profitable_hours": int(d.dispatch.sum()), "total_gross_margin_USD": float(d.gross_margin_USD.sum()), "lowest_margin_hour": int(d.loc[d.spark_spread_USD_per_MWh.idxmin(), "hour"])}
    return finish("ex055", r, {"spark_spread_report": d}, ["Hour-by-hour rule ignores start cost, minimum run time, ramping and emissions cost."])
if __name__ == "__main__": run()
