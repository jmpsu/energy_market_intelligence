"""EX-031 Storage operations: inventory, ratcheted withdrawal rates and remaining deliverability over a withdrawal run."""
from common import *
def run(days=40, start_inventory=9000000, daily_demand=300000):
    p = {"working_gas": 10000000, "max_withdrawal": 250000, "max_injection": 120000}; ra = data("ex031_ratchets.csv", "inventory_pct_above,withdrawal_pct_of_max\n60,100\n40,80\n20,60\n0,40")
    inv, rows = float(start_inventory), []
    for d in range(1, days + 1):
        pct = inv / p["working_gas"] * 100; rate = p["max_withdrawal"] * float(ra.withdrawal_pct_of_max[ra.inventory_pct_above <= pct].iloc[0]) / 100; w = min(rate, inv, daily_demand); inv -= w
        rows.append({"day": d, "inventory_start_pct": pct, "deliverability_MMBtu_d": rate, "withdrawn_MMBtu": w, "unserved_MMBtu": daily_demand - w, "inventory_end_MMBtu": inv})
    t = pd.DataFrame(rows); chart("ex031", "deliverability", t, "day", ["deliverability_MMBtu_d", "withdrawn_MMBtu"], title="Storage deliverability under ratchets")
    r = {"start_inventory_pct": start_inventory / p["working_gas"] * 100, "end_inventory_pct": inv / p["working_gas"] * 100, "total_withdrawn_MMBtu": float(t.withdrawn_MMBtu.sum()), "first_ratchet_day": int(t.day[t.deliverability_MMBtu_d < p["max_withdrawal"]].iloc[0]) if (t.deliverability_MMBtu_d < p["max_withdrawal"]).any() else 0,
         "end_deliverability_MMBtu_d": float(t.deliverability_MMBtu_d.iloc[-1]), "total_unserved_MMBtu": float(t.unserved_MMBtu.sum()), "days_with_shortfall": int((t.unserved_MMBtu > 0).sum()), "inventory_left_but_undeliverable_at_demand_rate": bool(inv > 0 and t.unserved_MMBtu.iloc[-1] > 0)}
    return finish("ex031", r, {"withdrawal_run": t}, ["Deliverability falls as inventory falls: late-winter gas in the ground cannot all be delivered on the peak day.", "Step ratchets are a simplification of pressure-driven deliverability curves."])
if __name__ == "__main__": run()
