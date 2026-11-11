"""EX-036 Winter gas supply disruption: daily regional balance with demand surge, freeze-offs, import limits and ratcheted storage."""
from common import *
def run(freeze_off_pct=25.0, storage_max=6.0):
    d = data("ex036_cold_snap.csv", "day,temperature_F,normal_demand_Bcf_d,production_Bcf_d,pipeline_import_cap_Bcf_d\n1,35,18,12,8\n2,22,18,12,8\n3,8,18,12,8\n4,2,18,12,7\n5,5,18,12,7\n6,18,18,12,8\n7,33,18,12,8")
    d["demand_Bcf_d"] = d.normal_demand_Bcf_d + 0.22 * (35 - d.temperature_F).clip(lower=0); d["production_actual"] = d.production_Bcf_d * np.where(d.temperature_F < 15, 1 - freeze_off_pct / 100, 1.0)
    inv, rows = 30.0, []
    for x in d.itertuples():
        need = x.demand_Bcf_d - x.production_actual; imp = min(max(need, 0), x.pipeline_import_cap_Bcf_d); deliver = storage_max * (1.0 if inv > 15 else 0.6); sto = min(max(need - imp, 0), deliver, inv); inv -= sto
        rows.append({"day": x.day, "imports": imp, "storage_withdrawal": sto, "storage_deliverability": deliver, "shortfall_Bcf_d": max(need - imp - sto, 0), "inventory_end_Bcf": inv, "import_utilization_pct": imp / x.pipeline_import_cap_Bcf_d * 100})
    t = d.merge(pd.DataFrame(rows), on="day"); chart("ex036", "cold_snap", t, "day", ["demand_Bcf_d", "production_actual", "imports", "storage_withdrawal", "shortfall_Bcf_d"], title="Cold-snap gas balance")
    r = {"peak_demand_Bcf_d": float(t.demand_Bcf_d.max()), "peak_day": int(t.loc[t.demand_Bcf_d.idxmax(), "day"]), "production_lost_Bcf": float((t.production_Bcf_d - t.production_actual).sum()), "total_shortfall_Bcf": float(t.shortfall_Bcf_d.sum()), "shortfall_days": ",".join(map(str, t.day[t.shortfall_Bcf_d > 1e-9])) or "none",
         "days_imports_at_cap": int((t.import_utilization_pct > 99.9).sum()), "storage_withdrawn_Bcf": float(t.storage_withdrawal.sum()), "peak_day_supply_gap_before_storage": float((t.demand_Bcf_d - t.production_actual - t.imports).max())}
    return finish("ex036", r, {"daily_balance": t}, ["Demand rises and supply falls on the same days: the two effects compound.", "Hypothetical region and numbers; no price formation, no demand curtailment priority."])
if __name__ == "__main__": run()
