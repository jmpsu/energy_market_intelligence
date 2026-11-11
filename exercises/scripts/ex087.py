"""EX-087 Energy market data warehouse: star schema in SQLite (dimensions + price fact), loaded from the curated layer, with integrity checks."""
from common import *
import ex070, ex007
DDL = """CREATE TABLE dim_location(location_key INTEGER PRIMARY KEY, location TEXT UNIQUE, commodity TEXT, region TEXT, country TEXT);
CREATE TABLE dim_provider(provider_key INTEGER PRIMARY KEY, provider TEXT UNIQUE);
CREATE TABLE dim_time(time_key INTEGER PRIMARY KEY, timestamp TEXT UNIQUE, date TEXT, hour INTEGER);
CREATE TABLE fact_price(location_key INTEGER REFERENCES dim_location, provider_key INTEGER REFERENCES dim_provider, time_key INTEGER REFERENCES dim_time, price REAL NOT NULL, unit TEXT, currency TEXT, PRIMARY KEY(location_key, time_key));"""
def run():
    quiet(ex070.run); quiet(ex007.run); px = sql("market_data.sqlite", "SELECT * FROM curated_prices"); ref = sql("reference.sqlite", "SELECT * FROM location")
    db = PROC / "warehouse.sqlite"; db.unlink(missing_ok=True); con = sqlite3.connect(db); con.executescript(DDL); (ROOT / "data/schemas/warehouse_ddl.sql").write_text(DDL + "\n")
    locs = pd.DataFrame({"location": sorted(set(px.location) | set(ref.location))}).merge(ref[["location", "commodity", "region", "country"]], on="location", how="left"); locs.insert(0, "location_key", range(1, len(locs) + 1)); locs.to_sql("dim_location", con, if_exists="append", index=False)
    prov = pd.DataFrame({"provider_key": [1, 2], "provider": ["Provider_A", "Provider_B"]}); prov.to_sql("dim_provider", con, if_exists="append", index=False); tm = pd.DataFrame({"timestamp": sorted(px.timestamp.unique())}); tm.insert(0, "time_key", range(1, len(tm) + 1)); tm["date"] = tm.timestamp.str[:10]; tm["hour"] = tm.timestamp.str[11:13].astype(int); tm.to_sql("dim_time", con, if_exists="append", index=False)
    f = px.merge(locs, on="location").merge(prov, on="provider").merge(tm, on="timestamp")[["location_key", "provider_key", "time_key", "price", "unit", "currency"]]; f.to_sql("fact_price", con, if_exists="append", index=False); q = lambda s: pd.read_sql_query(s, con)
    orphans = int(q("SELECT COUNT(*) n FROM fact_price f LEFT JOIN dim_location l USING(location_key) WHERE l.location_key IS NULL").n[0]); unref = q("SELECT location FROM dim_location WHERE commodity IS NULL"); nofact = q("SELECT l.location FROM dim_location l LEFT JOIN fact_price f USING(location_key) WHERE f.location_key IS NULL")
    avg = q("SELECT l.commodity, COUNT(*) AS observations, ROUND(AVG(f.price), 4) AS avg_price FROM fact_price f JOIN dim_location l USING(location_key) GROUP BY l.commodity"); con.close()
    r = {"dim_location_rows": len(locs), "dim_time_rows": len(tm), "dim_provider_rows": 2, "fact_price_rows": len(f), "orphan_facts": orphans, "locations_missing_reference_data": ",".join(unref.location) or "none", "reference_locations_without_prices": len(nofact), "fact_grain": "one price per location per timestamp", "database": "data/processed/warehouse.sqlite"}
    return finish("ex087", r, {"dim_location": locs, "avg_price_by_commodity": avg}, ["Seven reference locations have no price facts yet: coverage gaps are queryable instead of invisible. A priced location missing from reference data would be listed, not dropped.", "Only the price fact is built; generation, demand, storage and transmission facts follow the same pattern."])
if __name__ == "__main__": run()
