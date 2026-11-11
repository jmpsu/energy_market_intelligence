"""EX-088 Market data API: a request handler over the warehouse (EX-087) returning JSON with status codes; exercised in-process."""
from common import *
import json, ex087
def handle(path, con):
    parts = [p for p in path.strip("/").split("/") if p]
    if parts[:2] == ["v1", "locations"] and len(parts) == 2: return 200, {"locations": [r[0] for r in con.execute("SELECT location FROM dim_location ORDER BY location")]}
    if parts[:2] == ["v1", "prices"] and len(parts) in (3, 4):
        if not con.execute("SELECT 1 FROM dim_location WHERE location=?", (parts[2],)).fetchone(): return 404, {"error": "unknown location", "location": parts[2]}
        q = "SELECT t.timestamp, f.price, f.unit, f.currency, p.provider FROM fact_price f JOIN dim_location l USING(location_key) JOIN dim_time t USING(time_key) JOIN dim_provider p USING(provider_key) WHERE l.location=?"
        rows = con.execute(q + (" AND t.timestamp=?" if len(parts) == 4 else "") + " ORDER BY t.timestamp", tuple(parts[2:])).fetchall()
        if not rows: return 404, {"error": "no validated price", "location": parts[2]}
        return 200, {"location": parts[2], "data_classification": "synthetic", "observations": [dict(zip(["timestamp", "price", "unit", "currency", "provider"], r)) for r in rows]}
    return 400, {"error": "bad request", "path": path}
def run():
    quiet(ex087.run); con = sqlite3.connect(PROC / "warehouse.sqlite"); calls = ["/v1/locations", "/v1/prices/Waha", "/v1/prices/Henry_Hub/2026-01-05T08:00:00", "/v1/prices/Henry_Hub/2026-01-05T10:00:00", "/v1/prices/Nowhere", "/v1/prices/Mont_Belvieu", "/v2/anything"]
    out = [(c,) + handle(c, con) for c in calls]; con.close(); t = pd.DataFrame([{"request": c, "status": s, "body": json.dumps(b)} for c, s, b in out]); by = dict((c, (s, b)) for c, s, b in out)
    (ROOT / "product_management/architecture/ex088_api_contract.md").write_text(f"# EX-088 market data API contract ({LABEL})\n\nGET /v1/locations -> 200 list\nGET /v1/prices/<location> -> 200 observations | 404 unknown location | 404 no validated price\nGET /v1/prices/<location>/<timestamp> -> 200 | 404\nanything else -> 400\n\nEvery 200 price response carries unit, currency, provider and data_classification.\n")
    r = {"requests": len(calls), "status_200": int((t.status == 200).sum()), "status_404": int((t.status == 404).sum()), "status_400": int((t.status == 400).sum()), "waha_observations": len(by["/v1/prices/Waha"][1]["observations"]), "waha_negative_price_served": bool(min(o["price"] for o in by["/v1/prices/Waha"][1]["observations"]) < 0),
         "henry_hub_0800_price": by["/v1/prices/Henry_Hub/2026-01-05T08:00:00"][1]["observations"][0]["price"], "henry_hub_1000_status": by["/v1/prices/Henry_Hub/2026-01-05T10:00:00"][0], "locations_listed": len(by["/v1/locations"][1]["locations"])}
    return finish("ex088", r, {"api_calls": t}, ["Handler logic only, called in-process: no HTTP server, authentication, pagination or rate limiting. A missing price returns 404, never a filled or stale value."])
if __name__ == "__main__": run()
