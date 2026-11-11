"""EX-091 Capacity expansion: least-cost technology mix for a three-block load duration curve (LP), checked against the screening-curve rule."""
from common import *
from scipy.optimize import linprog
def run():
    tech = data("ex091_technologies.csv", """technology,fixed_cost_USD_per_MW_yr,variable_cost_USD_per_MWh
    Baseload,300000,8
    Combined_Cycle,120000,30
    Combustion_Turbine,60000,60""")
    blk = data("ex091_load_blocks.csv", """block,MW,hours
    base,1000,8760
    intermediate,600,4000
    peak,400,500""")
    T, B = len(tech), len(blk); c = np.concatenate([tech.fixed_cost_USD_per_MW_yr.values, np.repeat(tech.variable_cost_USD_per_MWh.values, B) * np.tile(blk.hours.values, T)])       # vars: capacity[T], MW serving block[T x B]
    Aeq = np.zeros((B, T + T * B)); Aub = np.zeros((T, T + T * B))
    for i in range(T):
        Aub[i, i] = -1
        for j in range(B): Aeq[j, T + i * B + j] = 1; Aub[i, T + i * B + j] = 1
    res = linprog(c, A_ub=Aub, b_ub=np.zeros(T), A_eq=Aeq, b_eq=blk.MW.values, bounds=[(0, None)] * (T + T * B), method="highs"); tech["capacity_MW"] = res.x[:T].round(4); serve = res.x[T:].reshape(T, B)
    tech["energy_MWh"] = (serve * blk.hours.values).sum(axis=1); tech["capacity_factor_pct"] = (tech.energy_MWh / (tech.capacity_MW.where(tech.capacity_MW > 0) * 8760) * 100).fillna(0); tech["total_cost_USD"] = tech.capacity_MW * tech.fixed_cost_USD_per_MW_yr + tech.energy_MWh * tech.variable_cost_USD_per_MWh
    screen = [min(tech.itertuples(), key=lambda x: x.fixed_cost_USD_per_MW_yr + x.variable_cost_USD_per_MWh * h).technology for h in blk.hours]; f, v = tech.fixed_cost_USD_per_MW_yr.values, tech.variable_cost_USD_per_MWh.values
    r = {"total_cost_USD_per_yr": float(res.fun), "average_cost_USD_per_MWh": float(res.fun / (blk.MW * blk.hours).sum())} | {f"{x.technology}_MW": x.capacity_MW for x in tech.itertuples()} | {"screening_choice_by_block": ">".join(screen), "total_capacity_MW": float(tech.capacity_MW.sum()),
         "crossover_hours_CT_vs_CC": float((f[1] - f[2]) / (v[2] - v[1])), "crossover_hours_CC_vs_Baseload": float((f[0] - f[1]) / (v[1] - v[0]))}
    return finish("ex091", r, {"expansion_plan": tech}, ["Greenfield, single year, no reserve margin, no existing fleet, no renewables or storage, no lumpiness: the textbook screening-curve problem that capacity-expansion tools generalise."])
if __name__ == "__main__": run()
