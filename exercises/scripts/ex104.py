"""EX-104 (NGL extension) Product specification check: sample compositions tested against specification limits; off-spec volume and discount exposure."""
from common import *
def run(offspec_discount_USD_per_gal=0.05):
    spec = data("ex104_spec_limits.csv", """product,component,limit_type,limit_liquid_vol_pct
    Propane,propane,min,90.0
    Propane,ethane,max,5.0
    Propane,butanes_plus,max,2.5
    Ethane,ethane,min,95.0
    Ethane,methane,max,1.5
    Ethane,propane,max,3.5""")
    s = data("ex104_samples.csv", """sample_id,product,volume_gal,methane,ethane,propane,butanes_plus
    S1,Propane,500000,0.0,2.1,96.4,1.5
    S2,Propane,400000,0.0,6.2,92.0,1.8
    S3,Propane,300000,0.0,1.0,95.6,3.4
    S4,Ethane,800000,0.9,96.1,3.0,0.0
    S5,Ethane,600000,2.2,94.3,3.5,0.0""")
    m = s.melt(id_vars=["sample_id", "product", "volume_gal"], var_name="component", value_name="measured").merge(spec, on=["product", "component"]); m["pass"] = np.where(m.limit_type == "min", m.measured >= m.limit_liquid_vol_pct, m.measured <= m.limit_liquid_vol_pct)
    s["composition_sum"] = s[["methane", "ethane", "propane", "butanes_plus"]].sum(axis=1); fails = m[~m["pass"]]; s["on_spec"] = ~s.sample_id.isin(fails.sample_id); s["failed_tests"] = s.sample_id.map(fails.groupby("sample_id").component.agg(",".join)).fillna("")
    r = {"samples": len(s), "on_spec_samples": int(s.on_spec.sum()), "off_spec_samples": ",".join(s.sample_id[~s.on_spec]), "off_spec_volume_gal": float(s.volume_gal[~s.on_spec].sum()), "off_spec_pct_of_volume": float(s.volume_gal[~s.on_spec].sum() / s.volume_gal.sum() * 100), "discount_exposure_USD": float(s.volume_gal[~s.on_spec].sum() * offspec_discount_USD_per_gal),
         "tests_run": len(m), "tests_failed": len(fails), "compositions_sum_to_100": bool(np.allclose(s.composition_sum, 100))} | {f"{x.sample_id}_failed": x.failed_tests or "none" for x in s.itertuples()}
    return finish("ex104", r, {"sample_results": s, "test_detail": m}, ["Specification limits here are invented for the exercise; actual limits come from the pipeline, fractionator or industry specification named in the contract."])
if __name__ == "__main__": run()
