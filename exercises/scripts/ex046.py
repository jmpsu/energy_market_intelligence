"""EX-046 ISO/RTO vs bilateral: the same 100 MW x 16 h sale settled at nodal prices, bilaterally with wheeling, and with a contract for differences."""
from common import *
def run(mw=100, hours=16, lmp_gen=42.0, lmp_load=48.0, contract=45.0, wheeling=4.0, loss=0.03):
    mwh = mw * hours; rows = [("iso_spot", lmp_gen, lmp_load, "both exposed to spot; congestion 6 between nodes"), ("bilateral_physical_with_wheeling", contract, (contract + wheeling) / (1 - loss), "price fixed; buyer pays wheeling and losses"),
                              ("iso_plus_cfd_at_gen_node", contract, lmp_load + (contract - lmp_gen), "seller fixed; buyer keeps node-to-node basis"), ("iso_plus_cfd_at_load_node", lmp_gen + (contract - lmp_load), contract, "buyer fixed; seller keeps node-to-node basis")]
    t = pd.DataFrame(rows, columns=["structure", "seller_USD_per_MWh", "buyer_USD_per_MWh", "risk_allocation"]); t["seller_revenue_USD"] = t.seller_USD_per_MWh * mwh; t["buyer_cost_USD"] = t.buyer_USD_per_MWh * mwh; t["gap_USD_per_MWh"] = t.buyer_USD_per_MWh - t.seller_USD_per_MWh
    r = {f"{x.structure}_seller": x.seller_USD_per_MWh for x in t.itertuples()} | {f"{x.structure}_buyer": x.buyer_USD_per_MWh for x in t.itertuples()} | {"congestion_USD_per_MWh": lmp_load - lmp_gen, "congestion_total_USD": (lmp_load - lmp_gen) * mwh, "MWh": mwh}
    return finish("ex046", r, {"structures": t}, ["In every ISO structure someone holds the 6 USD/MWh node-to-node difference; an FTR is the instrument that hedges it (EX-056, EX-058)."])
if __name__ == "__main__": run()
