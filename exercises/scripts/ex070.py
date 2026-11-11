"""EX-070 Market data ingestion: raw staging -> validation -> provider-priority de-duplication -> curated table (SQLite)."""
from common import *
PRIORITY = ["Provider_A", "Provider_B"]; UNITS = {"Natural_Gas": "MMBtu", "Electricity": "MWh"}
def run():
    raw = pd.read_csv(SYN / "raw_market_prices.csv", dtype=str, keep_default_na=False); raw.insert(0, "raw_id", range(1, len(raw) + 1))
    v = raw.copy(); v["ts"] = pd.to_datetime(v.timestamp, errors="coerce"); v["price_num"] = pd.to_numeric(v.price, errors="coerce")
    reason = np.select([v.price == "", v.price_num.isna(), v.ts.isna(), v.unit != v.commodity.map(UNITS), v.currency != "USD"],
                       ["missing_price", "non_numeric_price", "bad_timestamp", "unit_mismatch", "bad_currency"], default="")
    v["reject_reason"] = reason; rejected = v[v.reject_reason != ""]; ok = v[v.reject_reason == ""].copy()
    ok["prio"] = ok.provider.map({p: i for i, p in enumerate(PRIORITY)}); key = ["ts", "commodity", "location"]
    ok = ok.sort_values(key + ["prio"]); dup = ok[ok.duplicated(key, keep="first")]; cur = ok.drop_duplicates(key, keep="first")
    curated = cur.assign(timestamp=cur.ts.dt.strftime("%Y-%m-%dT%H:%M:00"), price=cur.price_num)[["timestamp", "commodity", "location", "price", "unit", "currency", "provider", "raw_id"]]
    PROC.mkdir(exist_ok=True); con = sqlite3.connect(PROC / "market_data.sqlite")
    raw.to_sql("raw_prices", con, if_exists="replace", index=False); curated.to_sql("curated_prices", con, if_exists="replace", index=False)
    rejected[list(raw.columns) + ["reject_reason"]].to_sql("rejected_prices", con, if_exists="replace", index=False); con.close()
    r = {"raw_rows": len(raw), "rejected_rows": len(rejected), "reject_reasons": ",".join(sorted(rejected.reject_reason)), "duplicate_rows_superseded": len(dup),
         "curated_rows": len(curated), "negative_prices_preserved": int((curated.price < 0).sum()), "provider_priority": ">".join(PRIORITY),
         "max_provider_disagreement": float(ok.groupby(key).price_num.agg(lambda s: s.max() - s.min()).max()), "completeness_pct": len(curated) / raw[["timestamp", "commodity", "location"]].drop_duplicates().shape[0] * 100}
    return finish("ex070", r, {"curated_prices": curated, "rejected_records": rejected[list(raw.columns) + ["reject_reason"]], "superseded_duplicates": dup[list(raw.columns)]},
                  ["Henry Hub 10:00 has no valid observation from any provider: a gap the curated layer must expose, not fill."])
if __name__ == "__main__": run()
