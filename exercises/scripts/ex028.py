"""EX-028 Daily gas nominations: nominated -> confirmed (lesser of upstream and downstream) -> scheduled after a priority-based capacity cut."""
from common import *
def run(capacity=420000):
    d = data("ex028_nominations.csv", "nom_id,shipper,service,nominated_MMBtu,upstream_confirmed_MMBtu,downstream_confirmed_MMBtu\nN1,Alpha,primary_firm,150000,150000,150000\nN2,Beta,primary_firm,120000,120000,110000\nN3,Gamma,secondary_firm,100000,100000,100000\nN4,Delta,interruptible,80000,80000,80000\nN5,Echo,interruptible,60000,50000,60000")
    d["confirmed_MMBtu"] = d[["nominated_MMBtu", "upstream_confirmed_MMBtu", "downstream_confirmed_MMBtu"]].min(axis=1); d["confirmation_cut"] = d.nominated_MMBtu - d.confirmed_MMBtu; d["priority"] = d.service.map({"primary_firm": 1, "secondary_firm": 2, "interruptible": 3}); left = capacity; d["scheduled_MMBtu"] = 0.0
    for pr in (1, 2, 3):
        m = d.priority == pr; need = d.confirmed_MMBtu[m].sum(); f = min(1.0, left / need) if need else 0; d.loc[m, "scheduled_MMBtu"] = d.confirmed_MMBtu[m] * f; left -= need * f
    d["capacity_cut"] = d.confirmed_MMBtu - d.scheduled_MMBtu; d["total_cut_pct"] = (1 - d.scheduled_MMBtu / d.nominated_MMBtu) * 100
    r = {"nominated_MMBtu": float(d.nominated_MMBtu.sum()), "confirmed_MMBtu": float(d.confirmed_MMBtu.sum()), "scheduled_MMBtu": float(d.scheduled_MMBtu.sum()), "confirmation_cuts_MMBtu": float(d.confirmation_cut.sum()), "capacity_cuts_MMBtu": float(d.capacity_cut.sum()),
         "interruptible_scheduled_pct": float(d.scheduled_MMBtu[d.priority == 3].sum() / d.confirmed_MMBtu[d.priority == 3].sum() * 100), "firm_cut_MMBtu": float(d.capacity_cut[d.priority < 3].sum()), "shippers_cut": ",".join(d.shipper[d.total_cut_pct > 0])}
    return finish("ex028", r, {"nomination_schedule": d}, ["Two different cuts: confirmation cuts come from a counterparty mismatch, capacity cuts from the pipeline. They need different fixes.", "One cycle only; real pipelines run several nomination cycles per gas day."])
if __name__ == "__main__": run()
