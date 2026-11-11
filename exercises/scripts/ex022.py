"""EX-022 Seasonal gas spreads: winter-summer strips and key calendar spreads versus the cost of storage. Reuses the EX-023 curve."""
from common import *
def run(storage_cost=0.14, fuel_pct=3.0):
    c = load("ex023_hh_forward_quotes.csv").set_index("contract_month").day1_USD_per_MMBtu; m = lambda k: float(c[f"2027-{k:02d}"]); summer = float(np.mean([m(k) for k in range(4, 11)])); winter = float(np.mean([m(k) for k in (11, 12, 1, 2, 3)]))
    pairs = pd.DataFrame([("Mar_minus_Apr", m(3) - m(4)), ("Jan_minus_Jul", m(1) - m(7)), ("Dec_minus_May", m(12) - m(5)), ("Oct_minus_Nov", m(10) - m(11)), ("winter_minus_summer_strip", winter - summer)], columns=["spread", "USD_per_MMBtu"])
    buy, sell = min(range(4, 11), key=m), max((11, 12, 1, 2, 3), key=m); gross = m(sell) - m(buy); cost = storage_cost + fuel_pct / 100 * m(buy)
    r = {r_.spread: r_.USD_per_MMBtu for r_ in pairs.itertuples()} | {"cheapest_injection_month": buy, "richest_withdrawal_month": sell, "best_single_spread": gross, "storage_cost_incl_fuel": cost, "net_storage_margin_USD_per_MMBtu": gross - cost, "storage_in_the_money": bool(gross > cost), "breakeven_storage_cost": gross - fuel_pct / 100 * m(buy)}
    return finish("ex022", r, {"calendar_spreads": pairs}, ["Winter here is Nov, Dec plus the earlier-dated Jan-Mar contracts of the same calendar year: a simplification of a true Nov-Mar strip.", "Intrinsic value only; EX-025 adds capacity and ratchet limits."])
if __name__ == "__main__": run()
