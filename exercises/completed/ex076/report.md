# ex076 | SYNTHETIC HYPOTHETICAL DATA - not historical market data

trades_in_store: 4

locations_in_market_data: 5

trades_priced: 2

price_coverage_pct: 50

integration_breaks: TR002:Algonquin,TR004:Mont_Belvieu

mtm_priced_trades_USD: 13000

systems_connected: trade_capture>market_data>valuation>risk_feed

unpriced_notional_USD: 1910000

NOTE: A valuation that silently skips unpriced trades understates risk: coverage is reported and breaks are listed. Marks are the latest curated observation, not a forward curve for the delivery month.

