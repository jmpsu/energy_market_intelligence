"""EX-052 Load-serving entity settlement: day-ahead purchase, real-time deviation, ancillary charge, and a shadow-settlement check against the ISO statement."""
from common import *
def run(statement_total=23715.0, tolerance=1.0):
    p = {"da_MWh": 500.0, "da_price": 42.0, "actual_MWh": 530.0, "rt_price": 60.0, "ancillary_rate": 1.5}
    lines = [("day_ahead_energy", p["da_MWh"] * p["da_price"]), ("real_time_deviation", (p["actual_MWh"] - p["da_MWh"]) * p["rt_price"]), ("ancillary_services", p["actual_MWh"] * p["ancillary_rate"])]
    t = pd.DataFrame(lines, columns=["charge", "shadow_USD"]); total = float(t.shadow_USD.sum()); diff = statement_total - total
    r = {x.charge + "_USD": x.shadow_USD for x in t.itertuples()} | {"shadow_total_USD": total, "average_cost_USD_per_MWh": total / p["actual_MWh"], "statement_total_USD": statement_total, "difference_USD": diff, "dispute": bool(abs(diff) > tolerance),
         "underforecast_cost_USD": (p["actual_MWh"] - p["da_MWh"]) * (p["rt_price"] - p["da_price"]), "cost_if_perfect_da_forecast_USD": p["actual_MWh"] * p["da_price"] + p["actual_MWh"] * p["ancillary_rate"]}
    return finish("ex052", r, {"shadow_settlement": t}, ["The supplied statement is 120 above the shadow calculation: the kind of break a settlements analyst disputes. Real statements carry dozens of charge codes."])
if __name__ == "__main__": run()
