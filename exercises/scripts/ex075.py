"""EX-075 Reconcile contracted, scheduled and delivered gas volumes and mark the positions to settlement price."""
from common import *
def run(tolerance_pct=1.0):
    d = load("gas_position_reconciliation.csv")
    d["side"] = np.where(d.counterparty.str.startswith("Utility"), "SELL", "BUY"); sign = np.where(d.side == "BUY", 1, -1)   # assumption: producers/traders supply us, utilities buy from us
    d["contract_vs_scheduled_MMBtu"] = d.contracted_MMBtu - d.scheduled_MMBtu; d["scheduled_vs_delivered_MMBtu"] = d.scheduled_MMBtu - d.delivered_MMBtu
    d["delivery_imbalance_pct"] = d.scheduled_vs_delivered_MMBtu / d.scheduled_MMBtu * 100
    d["mtm_USD"] = sign * (d.settlement_price_USD_per_MMBtu - d.contract_price_USD_per_MMBtu) * d.contracted_MMBtu
    d["delivered_value_USD"] = d.delivered_MMBtu * d.settlement_price_USD_per_MMBtu; d["signed_physical_MMBtu"] = sign * d.delivered_MMBtu
    d["exception"] = (d.contract_vs_scheduled_MMBtu != 0) | (d.delivery_imbalance_pct.abs() > tolerance_pct)
    loc = d.groupby("location", as_index=False).agg(contracted_MMBtu=("contracted_MMBtu", "sum"), net_physical_MMBtu=("signed_physical_MMBtu", "sum"), mtm_USD=("mtm_USD", "sum"))
    r = {f"{x.trade_id}_mtm_USD": x.mtm_USD for x in d.itertuples()} | {"total_mtm_USD": float(d.mtm_USD.sum()), "net_physical_position_MMBtu": float(d.signed_physical_MMBtu.sum()),
         "total_abs_delivery_imbalance_MMBtu": float(d.scheduled_vs_delivered_MMBtu.abs().sum()), "exception_trades": ",".join(d.trade_id[d.exception]),
         "largest_counterparty_by_volume": d.loc[d.contracted_MMBtu.idxmax(), "counterparty"], "largest_location_by_volume": loc.loc[loc.contracted_MMBtu.idxmax(), "location"]}
    return finish("ex075", r, {"position_ledger": d, "location_summary": loc, "exception_log": d[d.exception]}, ["Trade direction is not in the source data; BUY/SELL is inferred from counterparty type and must be confirmed.",
                  "MtM uses contracted volume; delivered-volume differences are operational exposure reported separately."])
if __name__ == "__main__": run()
