"""EX-053 Dispatch economics: marginal cost = fuel price x heat rate + VOM; merit order and coal-gas switching when gas price changes."""
from common import *
from market_models.electricity.dispatch import merit_order
def run(gas_price=3.25, demand_MW=2000):
    d = data("ex053_units.csv", """generator,fuel,fuel_price_USD_per_MMBtu,heat_rate_MMBtu_per_MWh,vom_USD_per_MWh,available_capacity_MW
    NUC,uranium,0.70,10.4,2.0,900
    CC1,gas,3.25,6.8,2.5,600
    CC2,gas,3.25,7.4,3.0,500
    COAL,coal,2.10,10.2,4.5,500
    GT,gas,3.25,10.5,5.0,300""")
    def stack(g):
        s = d.copy(); s.loc[s.fuel == "gas", "fuel_price_USD_per_MMBtu"] = g; s["marginal_cost_USD_per_MWh"] = s.fuel_price_USD_per_MMBtu * s.heat_rate_MMBtu_per_MWh + s.vom_USD_per_MWh; return merit_order(s, demand_MW)
    a, pa, _ = stack(gas_price); b, pb, _ = stack(2.50); a["rank"] = range(1, len(a) + 1); sw = (d.fuel_price_USD_per_MMBtu[3] * d.heat_rate_MMBtu_per_MWh[3] + d.vom_USD_per_MWh[3] - d.vom_USD_per_MWh[2]) / d.heat_rate_MMBtu_per_MWh[2]
    r = {f"{x.generator}_cost": x.marginal_cost_USD_per_MWh for x in a.itertuples()} | {"merit_order": ">".join(a.generator), "clearing_price": pa, "marginal_unit": a[a.dispatch_MW > 0].generator.iloc[-1], "coal_dispatch_MW": float(a.dispatch_MW[a.generator == "COAL"].iloc[0]),
         "merit_order_gas_2_50": ">".join(b.generator), "clearing_price_gas_2_50": pb, "coal_dispatch_MW_gas_2_50": float(b.dispatch_MW[b.generator == "COAL"].iloc[0]), "gas_price_where_CC2_displaces_COAL": float(sw)}
    return finish("ex053", r, {"merit_order": a, "merit_order_low_gas": b}, ["Fuel prices and heat rates synthetic. No start costs, minimum loads or emissions prices."])
if __name__ == "__main__": run()
