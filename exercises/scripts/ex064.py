"""EX-064 Dunkelflaute: multi-day low wind and solar; thermal and long-duration storage cover, unserved energy and required storage duration."""
from common import *
def run(demand_MWh_d=9600.0, renewables_normal_MWh_d=4800.0, thermal_max_MWh_d=6000.0, storage_MWh=5000.0, storage_power_MW=250.0, lull_days=(4, 5, 6, 7, 8), lull_factor=0.10, voll=5000.0):
    soc, rows = storage_MWh, []
    for day in range(1, 11):
        ren = renewables_normal_MWh_d * (lull_factor if day in lull_days else 1.0); resid = demand_MWh_d - ren; th = min(resid, thermal_max_MWh_d); gap = resid - th; dis = min(gap, soc, storage_power_MW * 24); soc -= dis
        surplus = thermal_max_MWh_d - th; ch = min(surplus, storage_MWh - soc, storage_power_MW * 24) if gap == 0 else 0.0; soc += ch; rows.append({"day": day, "renewables_MWh": ren, "thermal_MWh": th + ch, "storage_discharge_MWh": dis, "storage_charge_MWh": ch, "storage_soc_MWh": soc, "unserved_MWh": gap - dis})
    t = pd.DataFrame(rows); gap_total = (demand_MWh_d - renewables_normal_MWh_d * lull_factor - thermal_max_MWh_d) * len(lull_days)
    r = {"daily_gap_in_lull_MWh": gap_total / len(lull_days), "lull_energy_gap_MWh": gap_total, "storage_discharged_MWh": float(t.storage_discharge_MWh.sum()), "unserved_MWh": float(t.unserved_MWh.sum()), "unserved_days": int((t.unserved_MWh > 0).sum()), "scarcity_cost_USD": float(t.unserved_MWh.sum() * voll),
         "storage_needed_MWh": gap_total, "storage_duration_needed_hours": gap_total / storage_power_MW, "storage_duration_installed_hours": storage_MWh / storage_power_MW, "first_unserved_day": int(t.day[t.unserved_MWh > 0].iloc[0]) if (t.unserved_MWh > 0).any() else 0}
    return finish("ex064", r, {"dunkelflaute": t}, ["Daily energy balance, not hourly: it shows the energy shortfall, not the peak-MW shortfall. A 20-hour store covers under two of five lull days."])
if __name__ == "__main__": run()
