# Day 3 assessment - Natural Gas Pricing, Trading, and Risk

Pass mark: 8 of 10. Closed notes, terminal open.

1. (L03.01.5 Benchmark limits as a regional proxy) Run `python3 emi.py run 019 | grep '^Henry_Hub_basis_day1:'`. Report the value and explain in one sentence what it means for the desk.
2. (L03.02.5 Basis position P&L) Run `python3 emi.py run 019 | grep '^Henry_Hub_basis_day1:'`. Report the value and explain in one sentence what it means for the desk.
3. (L03.03.5 Index exposure in a book) Run `python3 emi.py run 024 | grep '^residual_risk_after_hh_hedge:'`. Report the value and explain in one sentence what it means for the desk.
4. (L03.04.5 Instrument selection for a hedge) Run `python3 emi.py run 024 | grep '^residual_risk_after_hh_hedge:'`. Report the value and explain in one sentence what it means for the desk.
5. (L03.05.5 Curve shape interpretation) Run `python3 emi.py run 023 | grep '^jan_minus_jul_spread:'`. Report the value and explain in one sentence what it means for the desk.
6. (L03.06.5 Hedge effectiveness) Run `python3 emi.py run 016 | grep '^firm_monthly_margin_USD:'`. Report the value and explain in one sentence what it means for the desk.
7. (L03.07.5 Storage constraint effects on value) Run `python3 emi.py run 025 | grep '^purchase_cost_USD:'`. Report the value and explain in one sentence what it means for the desk.
8. (L03.08.5 Global price pass-through to Henry Hub) Run `python3 emi.py run 033 | grep '^Asia_cargo_margin_USD:'`. Report the value and explain in one sentence what it means for the desk.
9. (L03.09.5 Position limits) Run `python3 emi.py run 027 | grep '^mtm_day1_USD:'`. Report the value and explain in one sentence what it means for the desk.
10. (L03.10.5 Risk reporting for a gas book) Run `python3 emi.py run 027 | grep '^mtm_day1_USD:'`. Report the value and explain in one sentence what it means for the desk.
