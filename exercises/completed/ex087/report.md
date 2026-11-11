# ex087 | SYNTHETIC HYPOTHETICAL DATA - not historical market data

dim_location_rows: 12

dim_time_rows: 3

dim_provider_rows: 2

fact_price_rows: 6

orphan_facts: 0

locations_missing_reference_data: none

reference_locations_without_prices: 7

fact_grain: one price per location per timestamp

database: data/processed/warehouse.sqlite

NOTE: Seven reference locations have no price facts yet: coverage gaps are queryable instead of invisible. A priced location missing from reference data would be listed, not dropped.

NOTE: Only the price fact is built; generation, demand, storage and transmission facts follow the same pattern.

