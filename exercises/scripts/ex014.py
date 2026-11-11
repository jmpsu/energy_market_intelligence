"""EX-014 Pipeline capacity measures: nameplate, operational, contracted, scheduled, available, utilisation."""
from common import *
def run():
    d = data("ex014_segments.csv", "segment,nameplate_MMBtu_d,operational_MMBtu_d,contracted_firm_MMBtu_d,scheduled_MMBtu_d\nPermian_to_Gulf,2000000,1850000,1850000,1840000\nAppalachia_to_NE,1500000,1500000,1450000,1180000\nMidcon_to_Chicago,1200000,1000000,820000,640000\nRockies_to_West,900000,900000,900000,905000")
    d["operational_derate_pct"] = (1 - d.operational_MMBtu_d / d.nameplate_MMBtu_d) * 100; d["unsubscribed_MMBtu_d"] = d.operational_MMBtu_d - d.contracted_firm_MMBtu_d; d["operationally_available_MMBtu_d"] = d.operational_MMBtu_d - d.scheduled_MMBtu_d
    d["utilization_pct"] = d.scheduled_MMBtu_d / d.operational_MMBtu_d * 100; d["contracted_but_unused_MMBtu_d"] = (d.contracted_firm_MMBtu_d - d.scheduled_MMBtu_d).clip(lower=0); d["status"] = np.select([d.scheduled_MMBtu_d > d.operational_MMBtu_d, d.utilization_pct >= 98], ["DATA_ERROR_overscheduled", "constrained"], "open")
    r = {f"{x.segment}_utilization_pct": x.utilization_pct for x in d.itertuples()} | {"constrained_segments": ",".join(d.segment[d.status == "constrained"]), "data_errors": ",".join(d.segment[d.status.str.startswith("DATA")]), "fully_subscribed_but_underused": ",".join(d.segment[(d.unsubscribed_MMBtu_d == 0) & (d.utilization_pct < 98)]) or "none",
          "total_release_candidate_MMBtu_d": float(d.contracted_but_unused_MMBtu_d.sum())}
    return finish("ex014", r, {"capacity_measures": d}, ["Sold-out is not the same as full: contracted-but-unused capacity is what the secondary market trades.", "One segment is scheduled above operational capacity on purpose: a data-quality check."])
if __name__ == "__main__": run()
