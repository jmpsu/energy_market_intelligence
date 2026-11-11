"""EX-004 Trace the electricity supply chain: 1 Bcf of gas to delivered MWh through generation, transmission and distribution losses."""
from common import *
def run(heat_rate=7.0, gas_bcf=1.0):
    p = data("ex004_assumptions.csv", "parameter,value,unit\nheat_content,1.037,MMBtu_per_Mcf\nstation_service_pct,2.5,percent\ntransmission_loss_pct,2.0,percent\ndistribution_loss_pct,4.0,percent\ngas_price,3.25,USD_per_MMBtu\nretail_rate,140,USD_per_MWh").set_index("parameter").value
    mmbtu = gas_bcf * 1e6 * p.heat_content; gross = mmbtu / heat_rate; net = gross * (1 - p.station_service_pct / 100); bulk = net * (1 - p.transmission_loss_pct / 100); deliv = bulk * (1 - p.distribution_loss_pct / 100)
    t = pd.DataFrame({"stage": ["fuel_energy_MWh_thermal", "gross_generation", "net_generation", "delivered_to_distribution", "delivered_to_customers"], "MWh": [mmbtu / 3.412, gross, net, bulk, deliv]}); t["pct_of_fuel_energy"] = t.MWh / t.MWh.iloc[0] * 100
    r = {"fuel_MMBtu": mmbtu, "gross_MWh": gross, "delivered_MWh": deliv, "thermal_efficiency_pct": 3.412 / heat_rate * 100, "fuel_to_customer_efficiency_pct": deliv / (mmbtu / 3.412) * 100, "fuel_cost_USD": mmbtu * p.gas_price,
         "fuel_cost_USD_per_delivered_MWh": mmbtu * p.gas_price / deliv, "fuel_share_of_retail_rate_pct": mmbtu * p.gas_price / deliv / p.retail_rate * 100, "homes_for_a_year_at_10.5_MWh": deliv / 10.5}
    return finish("ex004", r, {"energy_chain": t}, ["3.412 MMBtu = 1 MWh. Loss percentages and the retail rate are synthetic assumptions."])
if __name__ == "__main__": run()
