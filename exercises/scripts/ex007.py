"""EX-007 Build the energy-market reference database (hubs, pipelines, power markets, trading locations) from the repo's datasets."""
from common import *
def run():
    PROC.mkdir(exist_ok=True); db = PROC / "reference.sqlite"; con = sqlite3.connect(db)
    gas = pd.DataFrame({"location": ["Henry_Hub", "Waha", "AECO", "Dawn", "Algonquin"], "commodity": "Natural_Gas", "unit": "MMBtu", "role": ["benchmark", "supply_area", "supply_area", "market_area", "market_area"]})
    ngl = pd.DataFrame({"location": ["Mont_Belvieu", "Conway"], "commodity": "NGL", "unit": "gallon", "role": ["primary_hub", "midcontinent_hub"]}); pm = load("power_market_reference.csv")
    pw = pd.DataFrame({"location": pm.market, "commodity": "Electricity", "unit": "MWh", "role": pm.market_type}); loc = pd.concat([gas, ngl, pw], ignore_index=True); loc.insert(0, "location_id", range(1, len(loc) + 1))
    loc.to_sql("dim_location", con, if_exists="replace", index=False); load("gas_network_edges.csv").to_sql("ref_pipeline_segment", con, if_exists="replace", index=False); pm.to_sql("ref_power_market", con, if_exists="replace", index=False)
    s = pd.read_sql_query("SELECT commodity, unit, COUNT(*) AS locations FROM dim_location GROUP BY commodity, unit", con); dup = pd.read_sql_query("SELECT location, COUNT(*) c FROM dim_location GROUP BY location HAVING c>1", con); tabs = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", con); con.close()
    r = {"database": str(db.relative_to(ROOT)), "tables": ",".join(sorted(tabs.name)), "locations": len(loc), "gas_locations": 5, "ngl_locations": 2, "power_markets": len(pw), "duplicate_location_names": len(dup), "units_consistent_within_commodity": bool(loc.groupby("commodity").unit.nunique().max() == 1)}
    return finish("ex007", r, {"dim_location": loc, "summary": s}, ["Location roles are simplified labels; the pipeline segments are the synthetic EX-090 network."])
if __name__ == "__main__": run()
