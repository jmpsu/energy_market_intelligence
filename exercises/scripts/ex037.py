"""EX-037 NGL composition and recovery: mol% -> GPM -> gallons and barrels per day, shrink, product value, frac spread."""
from common import *
def recover(comp, inlet_mcf_d, mode):
    c = comp.copy(); c["theoretical_gpm"] = c.mol_pct * c.gal_per_Mcf_per_molpct; c["recovery"] = c[f"recovery_{mode}"]
    c["gal_per_d"] = inlet_mcf_d * c.theoretical_gpm * c.recovery; c["bbl_per_d"] = c.gal_per_d / 42; c["shrink_MMBtu_per_d"] = c.gal_per_d * c.MMBtu_per_gal
    return c
def prices(date):
    px = load("ngl_regional_prices.csv"); return px[px.date == date].set_index("product")
def run(mode="recover", gas_price=None, inlet_Mcf_per_d=None):
    p = params("ex037_plant.csv"); gas = p["gas_price"] if gas_price is None else gas_price; inlet = p["inlet_Mcf_per_d"] if inlet_Mcf_per_d is None else inlet_Mcf_per_d
    c = recover(load("ngl_components.csv"), inlet, mode); c["mont_belvieu_USD_per_gal"] = c["product"].map(prices(p["price_date"]).mont_belvieu_USD_per_gallon)
    c["value_USD_per_d"] = c.gal_per_d * c.mont_belvieu_USD_per_gal; c["fuel_value_USD_per_gal"] = c.MMBtu_per_gal * gas; c["barrel_share_pct"] = c.gal_per_d / c.gal_per_d.sum() * 100
    value, shrink = float(c.value_USD_per_d.sum()), float(c.shrink_MMBtu_per_d.sum())
    r = {"mode": mode, "theoretical_gpm": float(c.theoretical_gpm.sum()), "recovered_gpm": float(c.gal_per_d.sum() / inlet), "ngl_gal_per_d": float(c.gal_per_d.sum()), "ngl_bbl_per_d": float(c.bbl_per_d.sum()),
         "shrink_MMBtu_per_d": shrink, "ngl_value_USD_per_d": value, "shrink_cost_USD_per_d": shrink * gas, "gross_frac_spread_USD_per_d": value - shrink * gas,
         "ngl_value_USD_per_MMBtu": value / shrink, "frac_spread_USD_per_MMBtu": value / shrink - gas, "weighted_price_USD_per_gal": value / float(c.gal_per_d.sum())}
    r |= {f"{x.product}_bbl_per_d": x.bbl_per_d for x in c.itertuples()} | {"ethane_barrel_share_pct": float(c.barrel_share_pct[c["product"] == "Ethane"].iloc[0])}
    return finish("ex037", r, {"ngl_recovery": c}, ["Conversion factors (gal/Mcf per mol%, MMBtu/gal, lb/gal) are rounded engineering approximations; contracts use GPA Midstream standards. C5+ uses one factor for the whole pentanes-plus cut.",
                  "Gross frac spread ignores plant fuel, transport and fractionation fees, and the processing contract split (fee, POP, keep-whole)."])
if __name__ == "__main__": run()
