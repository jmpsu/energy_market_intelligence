"""EX-008 Same price shock, different participants: P&L effect of a gas price rise on producer, pipeline, generator, utility and trader."""
from common import *
def run(gas_shock=2.0, power_pass_through=0.5):
    d = data("ex008_participants.csv", "participant,gas_position_MMBtu_per_d,power_position_MWh_per_d,hedged_fraction,note\nProducer,500000,0,0.6,long gas production\nPipeline,0,0,0,fee based\nGas_Generator,-168000,24000,0.0,burns gas at 7.0 heat rate and sells power\nRegulated_Utility,-300000,0,0.0,buys gas and recovers cost later through rates\nTrader,-100000,0,0.0,short gas position")
    hr_power = 7.0 * gas_shock * power_pass_through; d["gas_pnl_USD_per_d"] = d.gas_position_MMBtu_per_d * gas_shock * (1 - d.hedged_fraction); d["power_pnl_USD_per_d"] = d.power_position_MWh_per_d * hr_power
    d["immediate_pnl_USD_per_d"] = d.gas_pnl_USD_per_d + d.power_pnl_USD_per_d; d["eventual_pnl_USD_per_d"] = np.where(d.participant == "Regulated_Utility", 0.0, d.immediate_pnl_USD_per_d); d["response"] = ["drill and hedge more", "none (volumes may rise)", "run less unless power follows", "file for cost recovery; cash strain meanwhile", "cover short or cut position"]
    r = {f"{x.participant}_immediate_pnl_USD_per_d": x.immediate_pnl_USD_per_d for x in d.itertuples()} | {"power_price_rise_USD_per_MWh": hr_power, "generator_breakeven_pass_through": 1.0, "winners": ",".join(d.participant[d.immediate_pnl_USD_per_d > 0]), "losers": ",".join(d.participant[d.immediate_pnl_USD_per_d < 0])}
    return finish("ex008", r, {"incentives": d}, ["Generator keeps its margin only if power rises by heat rate x gas move (pass-through = 1.0).", "Positions and hedge ratios are synthetic."])
if __name__ == "__main__": run()
