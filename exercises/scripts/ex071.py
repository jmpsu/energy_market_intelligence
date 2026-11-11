"""EX-071 Daily P&L and attribution: day-over-day MtM change split into price move on existing trades and new-deal P&L."""
from common import *
from ex023 import value
def run():
    c = load("ex023_hh_forward_quotes.csv"); tr = load("ex023_trades.csv"); old, new = tr[tr.trade_day == 1], tr[tr.trade_day == 2]
    v1, v2old, v2new = value(old, c, "day1_USD_per_MMBtu"), value(old, c, "day2_USD_per_MMBtu"), value(new, c, "day2_USD_per_MMBtu")
    a = v1[["trade_id", "contract_month", "sign", "volume_MMBtu"]].copy(); a["mtm_day1_USD"], a["mtm_day2_USD"] = v1.mtm_USD.values, v2old.mtm_USD.values
    a["curve_move"] = (v2old.day2_USD_per_MMBtu - v1.day1_USD_per_MMBtu).values; a["price_pnl_USD"] = a.sign * a.volume_MMBtu * a.curve_move
    price, newdeal = float(a.price_pnl_USD.sum()), float(v2new.mtm_USD.sum()); total = float(v2old.mtm_USD.sum() + v2new.mtm_USD.sum() - v1.mtm_USD.sum())
    a.to_csv(ROOT / "trading_simulation/risk/ex071_pnl_attribution.csv", index=False)
    r = {"mtm_day1_USD": float(v1.mtm_USD.sum()), "mtm_day2_USD": float(v2old.mtm_USD.sum() + v2new.mtm_USD.sum()), "daily_pnl_USD": total, "price_pnl_USD": price, "new_deal_pnl_USD": newdeal, "unexplained_USD": round(total - price - newdeal, 6) + 0.0}
    r |= {f"{x.trade_id}_price_pnl_USD": x.price_pnl_USD for x in a.itertuples()}
    return finish("ex071", r, {"pnl_attribution": a, "new_deals": v2new}, ["Linear book, so price P&L explains everything; options, discounting and roll-off would add gamma, vega, theta and carry buckets."])
if __name__ == "__main__": run()
