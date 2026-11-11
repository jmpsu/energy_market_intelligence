# Capstone presentation (10 minutes)

All figures are from `python3 emi.py run 100` on SYNTHETIC data.

## 1. Decision asked for
Approve the 90-day roadmap in product_management/roadmap/ex095_roadmap_90_day.md.

## 2. Evidence (live output)

```
ex100 | SYNTHETIC HYPOTHETICAL DATA - not historical market data
Base_portfolio_value_USD: 1617201.470588
Gas_Spike_portfolio_value_USD: 2579646.764706
Power_Scarcity_portfolio_value_USD: 3037356.176471
Pipeline_Disruption_portfolio_value_USD: 1947938.058824
Renewable_Shortfall_portfolio_value_USD: 2128587.352941
Combined_Extreme_portfolio_value_USD: 3323248.823529
base_gas_book_value_USD: 1015500
base_gas_unit_margin_USD: 429400
base_renewable_revenue_USD: 141900
base_battery_margin_USD: 30401.470588
worst_scenario: Base
worst_change_USD: 0
base_short_hours: 1
NOTE: Gas positions are treated as long inventory valued at price x volume; a percentage shock applied to the negative Waha price makes it more negative.
NOTE: Battery energy capacity, efficiency and SOC are added assumptions (capstone_assumptions.csv); the brief supplies only 100 MW.
NOTE: Gas book is a stock value, power margin is one day: the sum is a teaching aggregate, not an accounting measure.
NOTE: Every scenario with a power-price rise is a gain for this net-long asset portfolio; the short demand position is reported in MW but not priced.

```

## 3. Storyline
1. Problem: gas, power and NGL exposures are analysed in separate tools.
2. Evidence: the integrated scenario table above changes the ranking of risks versus single-commodity views.
3. Recommendation: build the top-ranked items in product_management/roadmap/ex097_ranked_features.csv.
4. KPIs: product_management/kpis/ex098_kpis.csv.
5. Risks and limits: synthetic data, simplified physics, no vendor capability verified (see competitive_analysis/platform_comparison.md).

## 4. Q&A prep
Re-run with overrides to answer what-ifs live, e.g. `python3 emi.py run 038 gas_price=5`, `python3 emi.py run 017 cut=0.8`.
