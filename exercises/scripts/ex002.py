"""EX-002 Classify market participants by commercial role, regulation and price-risk exposure (SQLite)."""
from common import *
def run():
    d = data("ex002_participants.csv", """
participant_type,segment,commodity,rate_regulated,takes_price_risk,earns_from,typical_systems
Producer,upstream,gas_ngl,No,Yes,commodity_price,production_accounting
Gas_Processor,midstream,gas_ngl,No,Depends_on_contract,fees_or_frac_spread,plant_accounting
Interstate_Pipeline,midstream,gas,Yes,No,tariff,scheduling_EBB
Storage_Operator,midstream,gas,Mixed,No,storage_fees,scheduling
NGL_Fractionator,midstream,ngl,No,No,fractionation_fee,terminal_accounting
LDC_Gas_Utility,downstream,gas,Yes,No,regulated_return,gas_supply_planning
Independent_Power_Producer,generation,power,No,Yes,energy_capacity_ancillary,ETRM_bidding
Vertically_Integrated_Utility,generation_delivery,power,Yes,Limited,regulated_return,ETRM_planning_models
ISO_RTO,market_operator,power,Yes,No,administrative_fees,market_clearing
Marketer_Trader,trading,all,No,Yes,spreads_and_optimization,ETRM_risk
Financial_Counterparty,trading,all,No,Yes,spreads,risk_systems
Regulator,oversight,all,n_a,No,n_a,filings""")
    con = sqlite3.connect(":memory:"); d.to_sql("p", con, index=False)
    s = pd.read_sql_query("SELECT segment, COUNT(*) AS types, SUM(takes_price_risk='Yes') AS price_risk_takers, SUM(rate_regulated='Yes') AS regulated FROM p GROUP BY segment ORDER BY types DESC", con); con.close()
    r = {"participant_types": len(d), "full_price_risk_takers": ",".join(d.participant_type[d.takes_price_risk == "Yes"]), "rate_regulated": ",".join(d.participant_type[d.rate_regulated == "Yes"]),
         "fee_earners_without_price_risk": ",".join(d.participant_type[(d.takes_price_risk == "No") & d.earns_from.str.contains("fee|tariff")]), "etrm_users": ",".join(d.participant_type[d.typical_systems.str.contains("ETRM")])}
    return finish("ex002", r, {"participants": d, "segment_summary": s}, ["Generic participant types, not named companies; attributes are simplified."])
if __name__ == "__main__": run()
