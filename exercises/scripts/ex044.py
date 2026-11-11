"""EX-044 Integrated NGL portfolio: mark positions by product and hub, weekly P&L, flat-price vs Belvieu-Conway basis attribution."""
from common import *
def mark(pos, px, date):
    q = px[px.date == date].melt(id_vars=["date", "product"], var_name="hub", value_name="mark"); q["hub"] = q.hub.str.replace("_USD_per_gallon", "")
    m = pos.merge(q[["product", "hub", "mark"]], on=["product", "hub"], validate="m:1"); m["sign"] = np.where(m.side == "BUY", 1, -1); m["signed_gal"] = m.sign * m.volume_gal; m["mtm_USD"] = m.signed_gal * (m.mark - m.trade_price_USD_per_gal); return m
def run():
    pos, px = load("ex044_ngl_positions.csv"), load("ngl_regional_prices.csv"); d1, d2 = sorted(px.date.unique()); a, b = mark(pos, px, d1), mark(pos, px, d2)
    t = a[["position_id", "side", "product", "hub", "signed_gal", "trade_price_USD_per_gal"]].copy(); t["mark_day1"], t["mark_day2"], t["mtm_day1_USD"], t["mtm_day2_USD"] = a.mark.values, b.mark.values, a.mtm_USD.values, b.mtm_USD.values
    t["pnl_USD"] = t.mtm_day2_USD - t.mtm_day1_USD; t["signed_bbl"] = t.signed_gal / 42; t["notional_day2_USD"] = t.signed_gal * t.mark_day2
    prod = t.groupby("product", as_index=False).agg(net_gal=("signed_gal", "sum"), pnl_USD=("pnl_USD", "sum")); hub = t.groupby("hub", as_index=False).agg(net_gal=("signed_gal", "sum"), pnl_USD=("pnl_USD", "sum"))
    p = px[px["product"] == "Propane"].set_index("date"); d_con = float(p.conway_USD_per_gallon[d2] - p.conway_USD_per_gallon[d1]); d_basis = float((p.mont_belvieu_USD_per_gallon[d2] - p.conway_USD_per_gallon[d2]) - (p.mont_belvieu_USD_per_gallon[d1] - p.conway_USD_per_gallon[d1]))
    pp = t[t["product"] == "Propane"]; net, mb = float(pp.signed_gal.sum()), float(pp.signed_gal[pp.hub == "mont_belvieu"].sum())
    r = {"mtm_day1_USD": float(t.mtm_day1_USD.sum()), "mtm_day2_USD": float(t.mtm_day2_USD.sum()), "weekly_pnl_USD": float(t.pnl_USD.sum())} | {f"{x.position_id}_pnl_USD": x.pnl_USD for x in t.itertuples()}
    r |= {"net_position_gal": float(t.signed_gal.sum()), "net_position_bbl": float(t.signed_bbl.sum()), "gross_notional_USD": float(t.notional_day2_USD.abs().sum()), "largest_pnl_product": prod.loc[prod.pnl_USD.abs().idxmax(), "product"],
          "propane_net_gal": net, "propane_flat_price_pnl_USD": net * d_con, "propane_basis_pnl_USD": mb * d_basis, "propane_total_pnl_USD": float(pp.pnl_USD.sum()), "propane_basis_move_USD_per_gal": d_basis}
    t.to_csv(ROOT / "trading_simulation/positions/ex044_ngl_positions_marked.csv", index=False)
    return finish("ex044", r, {"positions_marked": t, "by_product": prod, "by_hub": hub}, ["Propane P&L = net gallons x Conway move + Belvieu gallons x basis move: the spread leg, not outright price, drives the result.", "Two price dates only; no VaR, no forward tenor, no physical logistics or storage costs."])
if __name__ == "__main__": run()
