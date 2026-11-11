"""EX-013 Raw gas processing: split inlet gas into residue gas and NGLs, with shrink, plant fuel and residue heat content. Reuses EX-037."""
from common import *
from ex037 import recover
def run(mode="recover", plant_fuel_pct=1.5, inlet_heat_content=1.25):
    p = params("ex037_plant.csv"); inlet = p["inlet_Mcf_per_d"]; c = recover(load("ngl_components.csv"), inlet, mode); inlet_mmbtu = inlet * inlet_heat_content; shrink = float(c.shrink_MMBtu_per_d.sum()); fuel = inlet_mmbtu * plant_fuel_pct / 100
    vol_removed = float((inlet * c.mol_pct / 100 * c.recovery).sum()); residue_mcf = inlet - vol_removed - inlet * plant_fuel_pct / 100; residue_mmbtu = inlet_mmbtu - shrink - fuel
    r = {"mode": mode, "inlet_Mcf_per_d": inlet, "inlet_MMBtu_per_d": inlet_mmbtu, "ngl_bbl_per_d": float(c.bbl_per_d.sum()), "shrink_MMBtu_per_d": shrink, "plant_fuel_MMBtu_per_d": fuel, "residue_gas_Mcf_per_d": residue_mcf, "residue_gas_MMBtu_per_d": residue_mmbtu,
         "residue_heat_content_MMBtu_per_Mcf": residue_mmbtu / residue_mcf, "volume_shrink_pct": (1 - residue_mcf / inlet) * 100, "energy_balance_residual": inlet_mmbtu - shrink - fuel - residue_mmbtu}
    return finish("ex013", r, {"component_recovery": c}, ["Inlet heat content is an assumption not derived from the composition table; treat residue heat content as indicative.", "Rejection mode leaves ethane in the residue gas and raises its heat content (run mode=reject)."])
if __name__ == "__main__": run()
