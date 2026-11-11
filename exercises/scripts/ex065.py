"""EX-065 Solar-plus-storage LP: charge from solar only, maximise market revenue under SOC, power and efficiency limits."""
from common import *
from market_models.optimization.battery import dispatch
def run(rte=None):
    d = load("renewable_storage_dispatch.csv"); p = params("ex065_battery_assumptions.csv")
    o = dispatch(d.electricity_price_USD_per_MWh, p["battery_max_charge_power"], p["battery_max_discharge_power"], p["maximum_state_of_charge"], p["minimum_state_of_charge"],
                 p["initial_state_of_charge"], p["round_trip_efficiency"] if rte is None else rte, solar=d.solar_generation_MW)
    for k in ("charge", "discharge", "soc", "sales"): d[f"{k}_MW" if k != "soc" else "soc_MWh"] = o[k].round(6)
    direct = float(d.solar_generation_MW @ d.electricity_price_USD_per_MWh)
    chart("ex065", "state_of_charge", d, "hour", ["soc_MWh", "electricity_price_USD_per_MWh"], title="Battery SOC and price")
    r = {"direct_solar_revenue_USD": direct, "solar_plus_storage_revenue_USD": o["revenue"], "storage_uplift_USD": o["revenue"] - direct, "energy_charged_MWh": float(o["charge"].sum()),
         "energy_discharged_MWh": float(o["discharge"].sum()), "equivalent_cycles": float(o["discharge"].sum() / p["battery_energy_capacity"]), "energy_sold_MWh": float(o["sales"].sum()),
         "direct_energy_sold_MWh": float(d.solar_generation_MW.sum()), "final_soc_MWh": float(o["soc"][-1])}
    return finish("ex065", r, {"hourly_dispatch": d}, ["Efficiency loss applied on charge; terminal SOC >= initial SOC; perfect price foresight; demand_MW column is not used (merchant sale assumption).",
                  "Storage sells fewer MWh than direct solar yet earns more: value depends on when energy is sold."])
if __name__ == "__main__": run()
