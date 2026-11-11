"""EX-101 (NGL extension) Propane forward curve: seasonal shape, summer-fill storage trade, hedge of a winter purchase."""
from common import *
def run(storage_fee_USD_per_gal_month=0.005, financing_rate=0.06, volume_gal=4200000):
    c = data("ex101_propane_forwards.csv", """contract_month,mont_belvieu_USD_per_gal
    2027-04,0.700
    2027-05,0.690
    2027-06,0.685
    2027-07,0.690
    2027-08,0.705
    2027-09,0.725
    2027-10,0.750
    2027-11,0.775
    2027-12,0.795
    2028-01,0.805
    2028-02,0.790
    2028-03,0.750""")
    c["month_index"] = range(len(c)); buy = c.loc[c.mont_belvieu_USD_per_gal.idxmin()]; sell = c.loc[c.mont_belvieu_USD_per_gal.idxmax()]; months = int(sell.month_index - buy.month_index); spread = float(sell.mont_belvieu_USD_per_gal - buy.mont_belvieu_USD_per_gal)
    carry = storage_fee_USD_per_gal_month * months + buy.mont_belvieu_USD_per_gal * financing_rate * months / 12; c["carry_adjusted_vs_buy_month"] = c.mont_belvieu_USD_per_gal - buy.mont_belvieu_USD_per_gal - (storage_fee_USD_per_gal_month + buy.mont_belvieu_USD_per_gal * financing_rate / 12) * (c.month_index - buy.month_index)
    chart("ex101", "propane_curve", c, "contract_month", ["mont_belvieu_USD_per_gal"], title="Propane forward curve")
    r = {"cheapest_month": buy.contract_month, "dearest_month": sell.contract_month, "gross_spread_USD_per_gal": spread, "months_held": months, "carry_cost_USD_per_gal": float(carry), "net_storage_margin_USD_per_gal": spread - float(carry), "net_storage_margin_USD": (spread - float(carry)) * volume_gal, "volume_bbl": volume_gal / 42,
         "summer_strip": float(c.mont_belvieu_USD_per_gal.iloc[:6].mean()), "winter_strip": float(c.mont_belvieu_USD_per_gal.iloc[6:].mean()), "locked_january_cost_USD": float(sell.mont_belvieu_USD_per_gal) * volume_gal, "breakeven_storage_fee_USD_per_gal_month": (spread - buy.mont_belvieu_USD_per_gal * financing_rate * months / 12) / months}
    return finish("ex101", r, {"propane_curve": c}, ["Synthetic curve. The storage trade locks the spread only if both legs are hedged on trade date; physical storage also needs cavern space and pipeline access."])
if __name__ == "__main__": run()
