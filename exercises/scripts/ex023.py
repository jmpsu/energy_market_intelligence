"""EX-023 Forward curve shape and position valuation. MtM = sign x volume x (forward - trade price), undiscounted."""
from common import *
def value(trades, curve, col):
    t = trades.merge(curve[["contract_month", col]], on="contract_month", validate="m:1"); t["sign"] = np.where(t.side == "BUY", 1, -1)
    t["mtm_USD"] = t.sign * t.volume_MMBtu * (t[col] - t.price_USD_per_MMBtu); return t
def run():
    c = load("ex023_hh_forward_quotes.csv"); tr = load("ex023_trades.csv"); c["month"] = c.contract_month.str[-2:].astype(int)
    c["month_on_month_spread"] = c.day1_USD_per_MMBtu.diff(); c["season"] = np.where(c.month.isin([11, 12, 1, 2, 3]), "winter", "summer")
    win, summ = c.day1_USD_per_MMBtu[c.season == "winter"].mean(), c.day1_USD_per_MMBtu[c.season == "summer"].mean()
    v = value(tr[tr.trade_day == 1], c, "day1_USD_per_MMBtu"); c.to_csv(ROOT / "trading_simulation/forward_curves/hh_curve.csv", index=False); v.to_csv(ROOT / "trading_simulation/positions/ex023_positions_day1.csv", index=False)
    chart("ex023", "forward_curve", c, "contract_month", ["day1_USD_per_MMBtu"], title="Henry Hub forward curve, day 1")
    r = {"calendar_strip_USD_per_MMBtu": float(c.day1_USD_per_MMBtu.mean()), "winter_strip": float(win), "summer_strip": float(summ), "winter_minus_summer": float(win - summ),
         "jan_minus_jul_spread": float(c.day1_USD_per_MMBtu[c.month == 1].iloc[0] - c.day1_USD_per_MMBtu[c.month == 7].iloc[0]), "lowest_month": c.loc[c.day1_USD_per_MMBtu.idxmin(), "contract_month"]}
    r |= {f"{x.trade_id}_mtm_USD": x.mtm_USD for x in v.itertuples()} | {"book_mtm_day1_USD": float(v.mtm_USD.sum()), "net_position_MMBtu": float((v.sign * v.volume_MMBtu).sum())}
    return finish("ex023", r, {"curve": c, "positions_day1": v}, ["Equal-weighted strips (no day-count weighting), no discounting, quotes treated as mid."])
if __name__ == "__main__": run()
