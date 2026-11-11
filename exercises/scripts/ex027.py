"""EX-027 Regional gas trading portfolio: exposure by hub, Henry Hub equivalent vs basis exposure, and P&L. Uses the EX-019 prices."""
from common import *
import ex019
def run():
    ex019.run() if not (SYN / "ex019_hub_prices.csv").exists() else None; px = load("ex019_hub_prices.csv").set_index("hub")
    p = data("ex027_positions.csv", "position_id,hub,position_MMBtu,trade_price\nR1,Henry_Hub,300000,3.20\nR2,Waha,150000,1.00\nR3,Algonquin,-80000,8.50\nR4,Dawn,-100000,2.85\nR5,AECO,120000,2.20\nR6,Henry_Hub,-350000,3.30")
    p["mark1"] = p.hub.map(px.price_day1); p["mark2"] = p.hub.map(px.price_day2); p["mtm_day1"] = p.position_MMBtu * (p.mark1 - p.trade_price); p["pnl"] = p.position_MMBtu * (p.mark2 - p.mark1)
    hh = px.loc["Henry_Hub"]; p["hh_pnl"] = p.position_MMBtu * (hh.price_day2 - hh.price_day1); p["basis_pnl"] = p.pnl - p.hh_pnl; h = p.groupby("hub", as_index=False).agg(net_MMBtu=("position_MMBtu", "sum"), pnl=("pnl", "sum"))
    r = {"net_position_MMBtu": float(p.position_MMBtu.sum()), "gross_position_MMBtu": float(p.position_MMBtu.abs().sum()), "henry_hub_equivalent_MMBtu": float(p.position_MMBtu.sum()), "basis_exposure_MMBtu": float(p.position_MMBtu[p.hub != "Henry_Hub"].abs().sum()), "mtm_day1_USD": float(p.mtm_day1.sum()),
         "pnl_USD": float(p.pnl.sum()), "hh_price_pnl_USD": float(p.hh_pnl.sum()), "basis_pnl_USD": float(p.basis_pnl.sum()), "largest_loss_hub": h.loc[h.pnl.idxmin(), "hub"], "largest_gain_hub": h.loc[h.pnl.idxmax(), "hub"]}
    return finish("ex027", r, {"positions": p, "by_hub": h}, ["Net position is small but gross basis exposure is large: a flat-looking book can still lose on basis."])
if __name__ == "__main__": run()
