"""EX-103 (NGL extension) Propane export arbitrage: Mont Belvieu price in USD/tonne plus terminal fee and freight versus a delivered Asian price."""
from common import *
def run(mont_belvieu_USD_per_gal=0.72, gal_per_tonne=521.0, terminal_fee_USD_per_gal=0.06, freight_USD_per_tonne=120.0, delivered_asia_USD_per_tonne=560.0, cargo_tonnes=44000.0):
    fob = mont_belvieu_USD_per_gal * gal_per_tonne; term = terminal_fee_USD_per_gal * gal_per_tonne; cost = fob + term + freight_USD_per_tonne; arb = delivered_asia_USD_per_tonne - cost
    t = pd.DataFrame({"item": ["mont_belvieu", "terminal_fee", "freight", "delivered_cost", "delivered_price", "arbitrage"], "USD_per_tonne": [fob, term, freight_USD_per_tonne, cost, delivered_asia_USD_per_tonne, arb]}); t["USD_per_gal"] = t.USD_per_tonne / gal_per_tonne
    r = {"mont_belvieu_USD_per_tonne": fob, "terminal_fee_USD_per_tonne": term, "delivered_cost_USD_per_tonne": cost, "arbitrage_USD_per_tonne": arb, "arbitrage_USD_per_gal": arb / gal_per_tonne, "cargo_margin_USD": arb * cargo_tonnes, "cargo_bbl": cargo_tonnes * gal_per_tonne / 42, "arb_open": bool(arb > 0),
         "breakeven_mont_belvieu_USD_per_gal": (delivered_asia_USD_per_tonne - freight_USD_per_tonne) / gal_per_tonne - terminal_fee_USD_per_gal, "max_terminal_fee_USD_per_gal": (delivered_asia_USD_per_tonne - freight_USD_per_tonne - fob) / gal_per_tonne, "breakeven_freight_USD_per_tonne": delivered_asia_USD_per_tonne - fob - term}
    return finish("ex103", r, {"export_arbitrage": t}, ["521 gal per tonne is a rounded conversion to verify; freight, terminal fee, delivered price and cargo size are synthetic. The arbitrage per gallon is the most a shipper would pay above the terminal fee for dock space."])
if __name__ == "__main__": run()
