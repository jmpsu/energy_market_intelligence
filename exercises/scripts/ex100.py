"""EX-100 Integrated capstone: gas book + gas unit + wind/solar + battery, revalued across the supplied risk scenarios.
Reuses market_models.optimization.battery (EX-065) and the spark-spread logic of EX-055."""
from common import *
from market_models.optimization.battery import dispatch
def evaluate(s, gas, assets, mkt, a):
    g = lambda k: getattr(s, k) / 100; a_ = assets.set_index("technology")
    power = mkt.market_price_USD_per_MWh * (1 + g("power_price_change_percent")); gasp = mkt.gas_price_USD_per_MMBtu * (1 + g("gas_price_change_percent"))
    ccgt = a_.loc["Natural_Gas_Generator"]; fuel_avail = 1 - max(g("gas_supply_reduction_percent"), g("pipeline_capacity_reduction_percent"))
    spark = power - ccgt.heat_rate_MMBtu_per_MWh * gasp - ccgt.variable_cost_USD_per_MWh; gen = np.where(spark > 0, ccgt.capacity_MW * fuel_avail, 0.0)
    ren = (mkt.solar_generation_MW + mkt.wind_generation_MW) * (1 + g("renewable_generation_change_percent")); bat = a_.loc["Battery"]
    b = dispatch(power, bat.capacity_MW, bat.capacity_MW, a["battery_energy_capacity"], a["battery_min_soc"], a["battery_initial_soc"], a["battery_round_trip_efficiency"], grid_charge=True, var_cost=bat.variable_cost_USD_per_MWh)
    gas_value = float((gas.volume * gas.price_USD_per_unit * (1 + g("gas_price_change_percent"))).sum())
    hourly = pd.DataFrame({"scenario": s.scenario, "hour": mkt.hour, "power_price": power, "spark_spread": spark, "gas_unit_MW": gen, "renewables_MW": ren, "battery_net_MW": b["discharge"] - b["charge"], "demand_MW": mkt.demand_MW})
    hourly["net_position_MW"] = hourly.gas_unit_MW + hourly.renewables_MW + hourly.battery_net_MW - hourly.demand_MW
    return {"scenario": s.scenario, "gas_book_value_USD": gas_value, "gas_unit_margin_USD": float((np.maximum(spark, 0) * ccgt.capacity_MW * fuel_avail).sum()), "gas_unit_run_hours": int((gen > 0).sum()),
            "fuel_burn_MMBtu": float(gen.sum() * ccgt.heat_rate_MMBtu_per_MWh), "renewable_revenue_USD": float(ren @ power), "battery_margin_USD": b["revenue"],
            "short_hours": int((hourly.net_position_MW < 0).sum()), "max_short_MW": float(-min(hourly.net_position_MW.min(), 0))}, hourly
def run():
    gas, assets, mkt, sc, a = load("capstone_gas_positions.csv"), load("capstone_power_assets.csv"), load("capstone_power_market.csv"), load("capstone_risk_scenarios.csv"), params("capstone_assumptions.csv")
    rows, hrs = zip(*[evaluate(s, gas, assets, mkt, a) for s in sc.itertuples()]); t = pd.DataFrame(rows)
    t["power_day_margin_USD"] = t.gas_unit_margin_USD + t.renewable_revenue_USD + t.battery_margin_USD; t["portfolio_value_USD"] = t.gas_book_value_USD + t.power_day_margin_USD
    t["change_vs_base_USD"] = t.portfolio_value_USD - t.portfolio_value_USD.iloc[0]
    t.to_csv(ROOT / "reports/final_capstone/ex100_scenario_valuation.csv", index=False); t.to_csv(ROOT / "trading_simulation/scenarios/ex100_scenario_valuation.csv", index=False)
    chart("ex100", "scenario_value", t, "scenario", ["gas_book_value_USD", "power_day_margin_USD"], "bar", "Portfolio value by scenario")
    r = {f"{x.scenario}_portfolio_value_USD": x.portfolio_value_USD for x in t.itertuples()} | {"base_gas_book_value_USD": t.gas_book_value_USD.iloc[0], "base_gas_unit_margin_USD": t.gas_unit_margin_USD.iloc[0],
         "base_renewable_revenue_USD": t.renewable_revenue_USD.iloc[0], "base_battery_margin_USD": t.battery_margin_USD.iloc[0], "worst_scenario": t.loc[t.change_vs_base_USD.idxmin(), "scenario"], "worst_change_USD": float(t.change_vs_base_USD.min()),
         "base_short_hours": int(t.short_hours.iloc[0])}
    return finish("ex100", r, {"scenario_valuation": t, "hourly_dispatch": pd.concat(hrs)}, ["Gas positions are treated as long inventory valued at price x volume; a percentage shock applied to the negative Waha price makes it more negative.",
                  "Battery energy capacity, efficiency and SOC are added assumptions (capstone_assumptions.csv); the brief supplies only 100 MW.", "Gas book is a stock value, power margin is one day: the sum is a teaching aggregate, not an accounting measure.",
                  "Every scenario with a power-price rise is a gain for this net-long asset portfolio; the short demand position is reported in MW but not priced."])
if __name__ == "__main__": run()
