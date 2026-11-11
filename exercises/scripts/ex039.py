"""EX-039 Fractionation economics: value of a Y-grade barrel at Mont Belvieu purity prices vs purchase cost plus frac fee."""
from common import *
def run():
    y = load("ex039_ygrade.csv"); p = params("ex039_frac_assumptions.csv"); px = load("ngl_regional_prices.csv"); px = px[px.date == p["price_date"]]
    y = y.merge(px[["product", "mont_belvieu_USD_per_gallon"]], on="product", validate="1:1"); gpb = p["gallons_per_barrel"]
    y["gallons_per_barrel"] = y.gallon_fraction * gpb; y["value_USD_per_barrel"] = y.gallons_per_barrel * y.mont_belvieu_USD_per_gallon; y["value_share_pct"] = y.value_USD_per_barrel / y.value_USD_per_barrel.sum() * 100
    value = float(y.value_USD_per_barrel.sum()); cost = gpb * (p["ygrade_purchase_price"] + p["fractionation_fee"])
    r = {"composition_sums_to_one": bool(abs(y.gallon_fraction.sum() - 1) < 1e-9), "purity_value_USD_per_barrel": value, "weighted_price_USD_per_gallon": value / gpb, "cost_USD_per_barrel": cost,
         "frac_margin_USD_per_barrel": value - cost, "total_margin_USD": (value - cost) * p["volume"], "breakeven_ygrade_USD_per_gallon": value / gpb - p["fractionation_fee"],
         "largest_value_component": y.loc[y.value_USD_per_barrel.idxmax(), "product"], "ethane_volume_share_pct": float(y.gallon_fraction[y["product"] == "Ethane"].iloc[0] * 100), "ethane_value_share_pct": float(y.value_share_pct[y["product"] == "Ethane"].iloc[0])}
    return finish("ex039", r, {"barrel_value": y}, ["Reuses the EX-040 price table. No transport to the fractionator, no product losses, no storage or timing."])
if __name__ == "__main__": run()
