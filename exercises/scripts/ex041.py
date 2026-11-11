"""EX-041 Propane seasonality: monthly supply-demand balance, inventory path, days of supply, cold-winter and export scenarios."""
from common import *
def balance(d, opening, mult=1.0, export_shift=0.0, cold=("Dec", "Jan", "Feb")):
    b = d.copy(); b["domestic_demand_MMb_d"] = np.where(b.month.isin(cold), b.domestic_demand_MMb_d * mult, b.domestic_demand_MMb_d); b["exports_MMb_d"] = b.exports_MMb_d + export_shift
    b["net_build_MMbbl"] = (b.production_MMb_d - b.domestic_demand_MMb_d - b.exports_MMb_d) * b.days; b["ending_inventory_MMbbl"] = opening + b.net_build_MMbbl.cumsum()
    b["days_of_supply"] = b.ending_inventory_MMbbl / (b.domestic_demand_MMb_d + b.exports_MMb_d); return b
def run(winter_demand_mult=None, export_shift=0.0):
    d = load("ex041_propane_balance.csv"); p = params("ex041_assumptions.csv"); mult = p["cold_winter_demand_multiplier"] if winter_demand_mult is None else winter_demand_mult
    base, cold = balance(d, p["opening_inventory"], 1.0, export_shift), balance(d, p["opening_inventory"], mult, export_shift); floor = p["minimum_operating_inventory"]
    t = base[["month", "days", "production_MMb_d", "domestic_demand_MMb_d", "exports_MMb_d", "net_build_MMbbl", "ending_inventory_MMbbl", "days_of_supply"]].copy()
    t["cold_winter_inventory_MMbbl"] = cold.ending_inventory_MMbbl; t["cold_winter_below_minimum"] = t.cold_winter_inventory_MMbbl < floor
    chart("ex041", "propane_inventory", t, "month", ["ending_inventory_MMbbl", "cold_winter_inventory_MMbbl"], title="Propane inventory, base vs cold winter")
    r = {"peak_inventory_MMbbl": float(base.ending_inventory_MMbbl.max()), "peak_month": base.loc[base.ending_inventory_MMbbl.idxmax(), "month"], "base_ending_inventory_MMbbl": float(base.ending_inventory_MMbbl.iloc[-1]),
         "base_min_inventory_MMbbl": float(base.ending_inventory_MMbbl.min()), "build_season_injection_MMbbl": float(base.net_build_MMbbl.clip(lower=0).sum()), "winter_draw_MMbbl": float(-base.net_build_MMbbl.clip(upper=0).sum()),
         "export_share_of_production_pct": float(base.exports_MMb_d.mean() / base.production_MMb_d.mean() * 100), "winter_to_summer_demand_ratio": float(base.domestic_demand_MMb_d.max() / base.domestic_demand_MMb_d.min()),
         "cold_winter_min_inventory_MMbbl": float(cold.ending_inventory_MMbbl.min()), "cold_winter_months_below_minimum": ",".join(t.month[t.cold_winter_below_minimum]) or "none", "cold_winter_extra_draw_MMbbl": float(base.ending_inventory_MMbbl.iloc[-1] - cold.ending_inventory_MMbbl.iloc[-1]),
         "min_days_of_supply_base": float(base.days_of_supply.min())}
    return finish("ex041", r, {"propane_balance": t}, ["Exports held flat every month; in practice exports respond to the US-overseas price spread and dock capacity.", "National balance: regional (PADD 2 vs PADD 3) tightness and Conway-Mont Belvieu spreads are not captured (see EX-040).", "No price response to inventory."])
if __name__ == "__main__": run()
