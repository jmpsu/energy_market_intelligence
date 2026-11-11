"""EX-069 Trade capture: validate trade records against schema and business rules; store accepted trades in SQLite."""
from common import *
COMMODITIES = {"Natural_Gas": "MMBtu", "Electricity": "MWh", "Propane": "gal", "Ethane": "gal"}
def run():
    d = data("ex069_trades.csv", """trade_id,trade_date,commodity,counterparty,location,side,volume,unit,price,start_date,end_date,contract_type
    TR001,2026-01-05,Natural_Gas,Producer_A,Henry_Hub,BUY,100000,MMBtu,3.20,2026-02-01,2026-02-28,physical_fixed
    TR002,2026-01-05,Natural_Gas,Utility_A,Algonquin,SELL,60000,MMBtu,8.50,2026-02-01,2026-02-28,physical_fixed
    TR003,2026-01-05,Electricity,IPP_F,PJM_West,BUY,16000,MWh,45.00,2026-02-01,2026-02-28,financial_swap
    TR004,2026-01-05,Propane,Marketer_I,Mont_Belvieu,BUY,2000000,gal,0.700,2026-02-01,2026-02-28,physical_fixed
    TR005,2026-01-05,Natural_Gas,,Waha,BUY,80000,MMBtu,1.10,2026-02-01,2026-02-28,physical_index
    TR006,2026-01-05,Natural_Gas,Trader_J,Henry_Hub,SELL,-40000,MMBtu,3.15,2026-02-01,2026-02-28,financial_swap
    TR007,2026-01-05,Electricity,IPP_F,ERCOT_North,SELL,8000,MWh,52.00,2026-03-01,2026-02-01,financial_swap
    TR008,2026-01-05,Crude_Oil,Trader_J,Cushing,BUY,1000,bbl,70.00,2026-02-01,2026-02-28,financial_swap
    TR009,2026-01-05,Ethane,Marketer_I,Mont_Belvieu,BUY,3000000,MMBtu,0.240,2026-02-01,2026-02-28,physical_fixed""")
    v = d.copy(); v["reason"] = np.select([v.counterparty.isna(), v.volume <= 0, pd.to_datetime(v.end_date) < pd.to_datetime(v.start_date), ~v.commodity.isin(COMMODITIES), v.unit != v.commodity.map(COMMODITIES), ~v.side.isin(["BUY", "SELL"])],
                                          ["missing_counterparty", "non_positive_volume", "end_before_start", "unknown_commodity", "unit_mismatch", "bad_side"], default="")
    ok, rej = v[v.reason == ""].drop(columns="reason"), v[v.reason != ""]; ok = ok.assign(signed_volume=np.where(ok.side == "BUY", 1, -1) * ok.volume, notional_USD=ok.volume * ok.price)
    PROC.mkdir(exist_ok=True); con = sqlite3.connect(PROC / "trades.sqlite"); ok.to_sql("trade", con, if_exists="replace", index=False); rej.to_sql("trade_reject", con, if_exists="replace", index=False); con.close(); ok.to_csv(ROOT / "trading_simulation/contracts/ex069_accepted_trades.csv", index=False)
    r = {"submitted": len(d), "accepted": len(ok), "rejected": len(rej), "reject_reasons": ",".join(f"{a}:{b}" for a, b in zip(rej.trade_id, rej.reason)), "accepted_notional_USD": float(ok.notional_USD.sum()), "trade_id_unique": bool(d.trade_id.is_unique), "net_gas_MMBtu": float(ok.signed_volume[ok.commodity == "Natural_Gas"].sum())}
    return finish("ex069", r, {"accepted_trades": ok, "rejected_trades": rej}, ["Validation at capture is the cheapest control in the trade lifecycle: every reject here is a break avoided in confirmation, scheduling or settlement."])
if __name__ == "__main__": run()
