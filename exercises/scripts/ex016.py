"""EX-016 Firm vs interruptible transport: cost by load factor, breakeven, and value against the locational spread."""
from common import *
def run(spread=0.80, it_available_pct=70.0):
    p = data("ex016_rates.csv", "parameter,value,unit\nfirm_reservation,0.45,USD_per_MMBtu_per_day_of_MDQ\nfirm_commodity,0.02,USD_per_MMBtu\nfuel_pct,1.5,percent\nit_rate,0.55,USD_per_MMBtu\nmdq,50000,MMBtu_per_day\ndays,30,days\ndownstream_price,3.60,USD_per_MMBtu").set_index("parameter").value
    lf = np.arange(0.1, 1.01, 0.1); t = pd.DataFrame({"load_factor": lf}); t["firm_unit_cost"] = p.firm_reservation / lf + p.firm_commodity; t["it_unit_cost"] = p.it_rate; t["cheaper"] = np.where(t.firm_unit_cost < t.it_unit_cost, "firm", "interruptible")
    be = p.firm_reservation / (p.it_rate - p.firm_commodity); fuel = p.fuel_pct / 100 * p.downstream_price; vol = p.mdq * p.days
    firm_margin = vol * (spread - p.firm_commodity - fuel) - p.firm_reservation * vol; it_margin = vol * it_available_pct / 100 * max(spread - p.it_rate - fuel, 0)
    r = {"breakeven_load_factor": be, "firm_unit_cost_at_100pct": p.firm_reservation + p.firm_commodity, "firm_unit_cost_at_50pct": p.firm_reservation / 0.5 + p.firm_commodity, "spread": spread, "firm_monthly_margin_USD": firm_margin, "it_monthly_margin_USD": it_margin,
         "firm_fixed_cost_USD": p.firm_reservation * vol, "spread_where_firm_breaks_even": p.firm_reservation + p.firm_commodity + fuel, "preferred": "firm" if firm_margin > it_margin else "interruptible"}
    return finish("ex016", r, {"cost_by_load_factor": t}, ["Interruptible is cut first: on the days the spread is widest it may not flow at all (it_available_pct).", "Reservation charge is owed whether or not gas flows."])
if __name__ == "__main__": run()
