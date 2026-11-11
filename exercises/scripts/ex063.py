"""EX-063 Battery energy arbitrage with grid charging: LP optimum vs a three-cheapest / three-dearest-hours rule."""
from common import *
from market_models.optimization.battery import dispatch
def run(rte=None, power_mw=None):
    d = load("renewable_storage_dispatch.csv"); p = params("ex065_battery_assumptions.csv"); eff = p["round_trip_efficiency"] if rte is None else rte; pw = p["battery_max_charge_power"] if power_mw is None else power_mw
    px = d.electricity_price_USD_per_MWh; o = dispatch(px, pw, pw, p["maximum_state_of_charge"], p["minimum_state_of_charge"], p["initial_state_of_charge"], eff, grid_charge=True)
    d = d[["hour", "electricity_price_USD_per_MWh"]].assign(charge_MW=o["charge"].round(6), discharge_MW=o["discharge"].round(6), soc_MWh=o["soc"].round(6)); d["net_revenue_USD"] = (d.discharge_MW - d.charge_MW) * px
    lo, hi = px.nsmallest(3), px.nlargest(3); rule = float(pw * eff * hi.sum() - pw * lo.sum()) if lo.index.max() < hi.index.min() else float("nan"); ch, dis = d[d.charge_MW > 1e-6], d[d.discharge_MW > 1e-6]
    chart("ex063", "battery_soc", d, "hour", ["soc_MWh", "electricity_price_USD_per_MWh"], title="Battery arbitrage SOC and price")
    r = {"lp_revenue_USD": o["revenue"], "rule_of_thumb_revenue_USD": rule, "lp_gain_over_rule_USD": o["revenue"] - rule, "energy_charged_MWh": float(o["charge"].sum()), "energy_discharged_MWh": float(o["discharge"].sum()),
         "equivalent_cycles": float(o["discharge"].sum() / p["battery_energy_capacity"]), "avg_charge_price": float((ch.charge_MW * ch.electricity_price_USD_per_MWh).sum() / ch.charge_MW.sum()), "avg_discharge_price": float((dis.discharge_MW * dis.electricity_price_USD_per_MWh).sum() / dis.discharge_MW.sum()),
         "breakeven_price_ratio": 1 / eff, "max_soc_MWh": float(o["soc"].max()), "final_soc_MWh": float(o["soc"][-1]), "revenue_USD_per_MW_day": o["revenue"] / pw}
    return finish("ex063", r, {"battery_dispatch": d}, ["Perfect foresight of prices; price-taker; no degradation cost, no ancillary services, losses applied on charge.", "A charge-discharge pair is only worth doing when the discharge price exceeds the charge price divided by round-trip efficiency."])
if __name__ == "__main__": run()
