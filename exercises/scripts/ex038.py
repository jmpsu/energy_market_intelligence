"""EX-038 Ethane rejection: per gallon, recover when (ethane price - T&F fee) > gas price x ethane MMBtu/gal; plant-level decision includes the propane lost in rejection mode."""
from common import *
from ex037 import recover, prices
def plant_uplift(comp, inlet, mode, px, fee, gas):
    c = recover(comp, inlet, mode); c["netback_USD_per_gal"] = c["product"].map(px) - fee; c["fuel_value_USD_per_gal"] = c.MMBtu_per_gal * gas
    c["margin_USD_per_gal"] = c.netback_USD_per_gal - c.fuel_value_USD_per_gal; c["uplift_USD_per_d"] = c.gal_per_d * c.margin_USD_per_gal; return c
def decide(comp, inlet, px, fee, gas):
    a, b = plant_uplift(comp, inlet, "recover", px, fee, gas), plant_uplift(comp, inlet, "reject", px, fee, gas); d = a.set_index("product").gal_per_d - b.set_index("product").gal_per_d
    m = a.set_index("product").margin_USD_per_gal; other = float((d.drop("Ethane") * m.drop("Ethane")).sum()); fuel_c2 = float(a.fuel_value_USD_per_gal[a["product"] == "Ethane"].iloc[0])
    return a, b, {"recover_uplift_USD_per_d": float(a.uplift_USD_per_d.sum()), "reject_uplift_USD_per_d": float(b.uplift_USD_per_d.sum()), "ethane_swing_gal_per_d": float(d["Ethane"]),
                  "propane_lost_in_rejection_gal_per_d": float(d["Propane"]), "ethane_fuel_value_USD_per_gal": fuel_c2, "ethane_netback_USD_per_gal": float(px["Ethane"] - fee),
                  "simple_breakeven_ethane_USD_per_gal": fuel_c2 + fee, "plant_breakeven_ethane_USD_per_gal": fuel_c2 + fee - other / float(d["Ethane"])}
def run(gas_price=None, ethane_price=None):
    p = params("ex037_plant.csv"); comp = load("ngl_components.csv"); px = prices(p["price_date"]).mont_belvieu_USD_per_gallon.copy(); gas = p["gas_price"] if gas_price is None else gas_price
    if ethane_price is not None: px["Ethane"] = ethane_price
    a, b, r = decide(comp, p["inlet_Mcf_per_d"], px, p["transport_frac_fee"], gas); r["rejection_advantage_USD_per_d"] = r["reject_uplift_USD_per_d"] - r["recover_uplift_USD_per_d"]
    r["decision"] = "REJECT" if r["rejection_advantage_USD_per_d"] > 0 else "RECOVER"; r = {"gas_price": gas, "ethane_price": float(px["Ethane"])} | r
    grid = pd.DataFrame([{"gas_price_USD_per_MMBtu": g} | {k: v for k, v in decide(comp, p["inlet_Mcf_per_d"], px, p["transport_frac_fee"], g)[2].items() if "breakeven" in k or "uplift" in k} for g in np.arange(1.5, 5.01, 0.5)])
    grid["decision"] = np.where(grid.reject_uplift_USD_per_d > grid.recover_uplift_USD_per_d, "REJECT", "RECOVER"); adv = lambda g: (lambda u: u["reject_uplift_USD_per_d"] - u["recover_uplift_USD_per_d"])(decide(comp, p["inlet_Mcf_per_d"], px, p["transport_frac_fee"], g)[2])
    r["gas_price_where_decision_flips"] = float(-adv(0.0) / (adv(1.0) - adv(0.0)))      # advantage is linear in gas price
    chart("ex038", "ethane_breakeven", grid, "gas_price_USD_per_MMBtu", ["simple_breakeven_ethane_USD_per_gal", "plant_breakeven_ethane_USD_per_gal"], title="Ethane breakeven vs gas price")
    return finish("ex038", r, {"recover_mode": a, "reject_mode": b, "gas_price_grid": grid}, ["Rejection mode also loses propane recovery, so the plant recovers ethane at a price below the simple per-gallon breakeven.",
                  "Not modeled: residue-gas pipeline Btu limits that cap how much ethane can be rejected, ethane pipeline minimum-volume commitments, and fractionator or pipeline capacity limits that force rejection regardless of price."])
if __name__ == "__main__": run()
