"""EX-045 Power market reference database in SQLite with SQL coverage queries."""
from common import *
def run():
    PROC.mkdir(exist_ok=True); db = PROC / "power_markets.sqlite"; con = sqlite3.connect(db)
    load("power_market_reference.csv").to_sql("market_reference", con, if_exists="replace", index=False); load("market_activity.csv").to_sql("market_activity", con, if_exists="replace", index=False)
    q = lambda s: pd.read_sql_query(s, con)
    spread = q("""SELECT r.market, r.market_type, r.capacity_market, a.average_day_ahead_price_USD_per_MWh AS da, a.average_real_time_price_USD_per_MWh AS rt,
                  a.average_real_time_price_USD_per_MWh - a.average_day_ahead_price_USD_per_MWh AS rt_minus_da, a.renewable_share_percent,
                  RANK() OVER (ORDER BY a.average_real_time_price_USD_per_MWh DESC) AS rt_price_rank
                  FROM market_reference r JOIN market_activity a USING (market) ORDER BY rt_price_rank""")
    by_type = q("SELECT market_type, COUNT(*) AS markets, SUM(capacity_market='Yes') AS with_capacity_market FROM market_reference GROUP BY market_type")
    con.close()
    r = {"markets": len(spread), "highest_rt_price_market": spread.market.iloc[0], "largest_rt_minus_da_market": spread.loc[spread.rt_minus_da.idxmax(), "market"],
         "largest_rt_minus_da_USD_per_MWh": float(spread.rt_minus_da.max()), "highest_renewable_share_market": spread.loc[spread.renewable_share_percent.idxmax(), "market"],
         "markets_without_capacity_market": ",".join(sorted(spread.market[spread.capacity_market == "No"])), "database": str(db.relative_to(ROOT))}
    return finish("ex045", r, {"da_rt_spread": spread, "market_type_summary": by_type}, ["Reference attributes are the brief's supplied synthetic table; verify each market's design against ISO documentation before product use."])
if __name__ == "__main__": run()
