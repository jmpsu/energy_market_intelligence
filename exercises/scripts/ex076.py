"""EX-076 ETRM data integration: join the trade store (EX-069) to curated market data (EX-070); price coverage, MtM feed, integration breaks."""
from common import *
import ex069, ex070
def run():
    quiet(ex069.run); quiet(ex070.run); tr = sql("trades.sqlite", "SELECT * FROM trade"); px = sql("market_data.sqlite", "SELECT * FROM curated_prices")
    last = px.sort_values("timestamp").groupby(["commodity", "location"], as_index=False).last()[["commodity", "location", "price", "timestamp", "provider"]]; m = tr.merge(last, on=["commodity", "location"], how="left", suffixes=("", "_mark"))
    m["priced"] = m.price_mark.notna(); m["mtm_USD"] = m.signed_volume * (m.price_mark - m.price); feed = m[m.priced][["trade_id", "commodity", "location", "signed_volume", "price", "price_mark", "timestamp", "provider", "mtm_USD"]]; breaks = m[~m.priced][["trade_id", "commodity", "location"]].assign(break_type="no_curated_price_for_location")
    feed.to_csv(ROOT / "trading_simulation/settlements/ex076_risk_feed.csv", index=False)
    r = {"trades_in_store": len(tr), "locations_in_market_data": len(last), "trades_priced": int(m.priced.sum()), "price_coverage_pct": float(m.priced.mean() * 100), "integration_breaks": ",".join(f"{a}:{b}" for a, b in zip(breaks.trade_id, breaks.location)), "mtm_priced_trades_USD": float(feed.mtm_USD.sum()),
         "systems_connected": "trade_capture>market_data>valuation>risk_feed", "unpriced_notional_USD": float(m.notional_USD[~m.priced].sum())}
    return finish("ex076", r, {"risk_feed": feed, "integration_breaks": breaks}, ["A valuation that silently skips unpriced trades understates risk: coverage is reported and breaks are listed. Marks are the latest curated observation, not a forward curve for the delivery month."])
if __name__ == "__main__": run()
