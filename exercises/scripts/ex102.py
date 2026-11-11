"""EX-102 (NGL extension) Processing contract settlement: the same plant day settled under fee, percent-of-proceeds and keep-whole contracts, at two gas prices."""
from common import *
from ex037 import recover, prices
def settle(gas, fee_USD_per_Mcf=0.35, pop_producer_share=0.80, inlet_heat_content=1.25, plant_fuel_pct=2.0):
    p = params("ex037_plant.csv"); c = recover(load("ngl_components.csv"), p["inlet_Mcf_per_d"], "recover"); ngl = float((c.gal_per_d * c["product"].map(prices(p["price_date"]).mont_belvieu_USD_per_gallon)).sum())
    inlet = p["inlet_Mcf_per_d"] * inlet_heat_content; shrink = float(c.shrink_MMBtu_per_d.sum()); fuel = inlet * plant_fuel_pct / 100; residue = (inlet - shrink - fuel) * gas; pool = ngl + residue; fee = fee_USD_per_Mcf * p["inlet_Mcf_per_d"]
    return pd.DataFrame([("fee_based", pool - fee, fee), ("percent_of_proceeds", pool * pop_producer_share, pool * (1 - pop_producer_share)), ("keep_whole", inlet * gas, pool - inlet * gas)], columns=["contract", "producer_USD_per_d", "processor_USD_per_d"]).assign(gas_price=gas, total_USD_per_d=pool)
def run(gas_low=3.25, gas_high=7.50):
    a, b = settle(gas_low), settle(gas_high); t = a.merge(b, on="contract", suffixes=("_low", "_high")); t["processor_change_USD_per_d"] = t.processor_USD_per_d_high - t.processor_USD_per_d_low; t["producer_change_USD_per_d"] = t.producer_USD_per_d_high - t.producer_USD_per_d_low
    r = {f"{x.contract}_processor_low": x.processor_USD_per_d_low for x in t.itertuples()} | {f"{x.contract}_processor_high": x.processor_USD_per_d_high for x in t.itertuples()} | {f"{x.contract}_producer_low": x.producer_USD_per_d_low for x in t.itertuples()}
    r |= {"total_value_low_USD_per_d": float(a.total_USD_per_d.iloc[0]), "contract_most_exposed_to_gas_for_processor": t.loc[t.processor_change_USD_per_d.idxmin(), "contract"], "keep_whole_processor_negative_at_high_gas": bool(t.processor_USD_per_d_high[t.contract == "keep_whole"].iloc[0] < 0), "fee_processor_change": float(t.processor_change_USD_per_d[t.contract == "fee_based"].iloc[0])}
    return finish("ex102", r, {"contract_settlement": t}, ["Same molecules, same prices, three different P&Ls: contract type decides who holds the frac spread. Fee, share and plant-fuel terms are synthetic; real contracts add fixed recoveries, T&F deductions and minimum volumes."])
if __name__ == "__main__": run()
