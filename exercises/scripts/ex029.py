"""EX-029 Pipeline imbalances: scheduled vs actual, tolerance, and tiered monthly cash-out."""
from common import *
def run(index_price=3.25):
    d = data("ex029_month.csv", "shipper,scheduled_MMBtu,actual_takes_MMBtu\nAlpha,3000000,3045000\nBeta,2400000,2280000\nGamma,1800000,1998000\nDelta,2700000,2700000")
    tiers = data("ex029_cashout_tiers.csv", "tier,from_pct,to_pct,shipper_owes_pipeline_multiplier,pipeline_owes_shipper_multiplier\n1,0,5,1.00,1.00\n2,5,10,1.10,0.90\n3,10,100,1.25,0.75")
    d["imbalance_MMBtu"] = d.actual_takes_MMBtu - d.scheduled_MMBtu; d["imbalance_pct"] = d.imbalance_MMBtu / d.scheduled_MMBtu * 100
    def cash(x):
        tot, a = 0.0, abs(x.imbalance_pct)
        for t in tiers.itertuples():
            q = max(min(a, t.to_pct) - t.from_pct, 0) / 100 * x.scheduled_MMBtu; tot += q * index_price * (t.shipper_owes_pipeline_multiplier if x.imbalance_MMBtu > 0 else -t.pipeline_owes_shipper_multiplier)
        return tot
    d["cashout_USD_shipper_pays"] = d.apply(cash, axis=1); d["at_index_USD"] = d.imbalance_MMBtu * index_price; d["penalty_USD"] = d.cashout_USD_shipper_pays - d.at_index_USD
    r = {f"{x.shipper}_imbalance_pct": x.imbalance_pct for x in d.itertuples()} | {f"{x.shipper}_cashout_USD": x.cashout_USD_shipper_pays for x in d.itertuples()} | {"total_penalty_vs_index_USD": float(d.penalty_USD.sum()), "largest_penalty_shipper": d.loc[d.penalty_USD.idxmax(), "shipper"], "system_net_imbalance_MMBtu": float(d.imbalance_MMBtu.sum())}
    return finish("ex029", r, {"imbalance_cashout": d}, ["Positive imbalance = shipper took more than scheduled and buys the excess at index times a premium; negative = sells at a discount. Both directions lose money beyond tier 1.", "Synthetic tier table; each tariff defines its own."])
if __name__ == "__main__": run()
