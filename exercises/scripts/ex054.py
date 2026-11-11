"""EX-054 Heat rates: average vs incremental heat rate from an input-output curve, and efficiency."""
from common import *
def run():
    d = data("ex054_input_output.csv", """output_MW,fuel_input_MMBtu_per_h
    200,1700
    300,2300
    400,2900
    500,3500""")
    d["average_heat_rate_MMBtu_per_MWh"] = d.fuel_input_MMBtu_per_h / d.output_MW; d["incremental_heat_rate_MMBtu_per_MWh"] = d.fuel_input_MMBtu_per_h.diff() / d.output_MW.diff(); d["efficiency_pct"] = 3.412 / d.average_heat_rate_MMBtu_per_MWh * 100
    d["average_heat_rate_Btu_per_kWh"] = d.average_heat_rate_MMBtu_per_MWh * 1000; no_load = float(d.fuel_input_MMBtu_per_h.iloc[0] - d.incremental_heat_rate_MMBtu_per_MWh.iloc[1] * d.output_MW.iloc[0])
    r = {"full_load_heat_rate": float(d.average_heat_rate_MMBtu_per_MWh.iloc[-1]), "min_load_heat_rate": float(d.average_heat_rate_MMBtu_per_MWh.iloc[0]), "incremental_heat_rate_400_to_500": float(d.incremental_heat_rate_MMBtu_per_MWh.iloc[-1]), "full_load_efficiency_pct": float(d.efficiency_pct.iloc[-1]),
         "full_load_Btu_per_kWh": float(d.average_heat_rate_Btu_per_kWh.iloc[-1]), "no_load_fuel_MMBtu_per_h": no_load, "incremental_cost_at_gas_3_25": 3.25 * float(d.incremental_heat_rate_MMBtu_per_MWh.iloc[-1]), "average_cost_at_gas_3_25_full_load": 3.25 * float(d.average_heat_rate_MMBtu_per_MWh.iloc[-1])}
    return finish("ex054", r, {"heat_rate_curve": d}, ["Dispatch uses the incremental heat rate (6.0), not the average (7.0): the no-load fuel is sunk once the unit is on. Linear synthetic curve."])
if __name__ == "__main__": run()
