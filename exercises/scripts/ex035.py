"""EX-035 US-Canada-Mexico gas balance and two-sided cross-border reconciliation."""
from common import *
def run():
    b = load("north_american_gas_balance.csv"); f = load("cross_border_flows.csv")
    b["supply_Bcf_d"] = b.production_Bcf_d + b.imports_Bcf_d + b.storage_withdrawal_Bcf_d
    b["disposition_Bcf_d"] = b.domestic_consumption_Bcf_d + b.exports_Bcf_d + b.storage_injection_Bcf_d
    b["balance_residual_Bcf_d"] = b.supply_Bcf_d - b.disposition_Bcf_d
    b["flow_imports_Bcf_d"] = b.country.map(f.groupby("destination").flow_Bcf_d.sum()); b["flow_exports_Bcf_d"] = b.country.map(f.groupby("origin").flow_Bcf_d.sum())
    b["import_break_Bcf_d"] = b.imports_Bcf_d - b.flow_imports_Bcf_d; b["export_break_Bcf_d"] = b.exports_Bcf_d - b.flow_exports_Bcf_d
    b["import_dependence_pct"] = b.imports_Bcf_d / b.domestic_consumption_Bcf_d * 100; b["export_share_of_production_pct"] = b.exports_Bcf_d / b.production_Bcf_d * 100
    f["remaining_capacity_Bcf_d"] = f.available_capacity_Bcf_d - f.flow_Bcf_d; f["utilization_pct"] = f.flow_Bcf_d / f.available_capacity_Bcf_d * 100
    key = lambda c: c.replace(" ", "_")
    r = {f"{key(x.country)}_residual_Bcf_d": x.balance_residual_Bcf_d for x in b.itertuples()} | {f"{key(x.country)}_import_break_Bcf_d": x.import_break_Bcf_d for x in b.itertuples()}
    r |= {f"{key(x.country)}_export_break_Bcf_d": x.export_break_Bcf_d for x in b.itertuples()}
    r |= {"countries_fully_reconciled": ",".join(b.country[(b.import_break_Bcf_d.abs() < 1e-9) & (b.export_break_Bcf_d.abs() < 1e-9)]), "total_remaining_capacity_Bcf_d": float(f.remaining_capacity_Bcf_d.sum())}
    return finish("ex035", r, {"country_balance": b, "cross_border_flows": f}, ["Country totals may include LNG or third-country trade that the pipeline flow table omits; the breaks are flagged, not corrected.",
                  "No country balance closes to zero: residuals need a balancing item or a data correction."])
if __name__ == "__main__": run()
