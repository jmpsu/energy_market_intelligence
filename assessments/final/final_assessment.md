# Final assessment

Part A: 24 knowledge questions (pass 20). Part B: 6 practical tasks (pass 5). Part C: capstone presentation (reports/final_capstone/capstone_presentation.md).

## Part A

1. (L01.01.1 Upstream, midstream, downstream segments) Run `python3 emi.py run 001 | grep '^nodes:'`. Report the value and explain in one sentence what it means for the desk.
2. (L01.10.4 Integrated gas-power modeling rationale) Run `python3 emi.py run 009 | grep '^corr_hdd_storage_change:'`. Report the value and explain in one sentence what it means for the desk.
3. (L02.01.1 Shale basin geography) Run `python3 emi.py run 010 | grep '^Appalachian_netback_USD_per_MMBtu:'`. Report the value and explain in one sentence what it means for the desk.
4. (L02.10.4 Realized price at the delivery point) Run `python3 emi.py run 012 | grep '^blended_netback_USD_per_MMBtu:'`. Report the value and explain in one sentence what it means for the desk.
5. (L03.01.1 Henry Hub as benchmark) Run `python3 emi.py run 019 | grep '^Waha_basis_day1:'`. Report the value and explain in one sentence what it means for the desk.
6. (L03.10.4 Market price risk and liquidity) Run `python3 emi.py run 027 | grep '^basis_exposure_MMBtu:'`. Report the value and explain in one sentence what it means for the desk.
7. (L04.01.1 Network representation: nodes and edges) Run `python3 emi.py run 018 | grep '^nodes:'`. Report the value and explain in one sentence what it means for the desk.
8. (L04.10.4 Price and basis impacts) Run `python3 emi.py run 036 | grep '^total_shortfall_Bcf:'`. Report the value and explain in one sentence what it means for the desk.
9. (L05.01.1 NGL component properties) Run `cat data/synthetic/ngl_components.csv`. Report the value and explain in one sentence what it means for the desk.
10. (L05.10.4 Portfolio exposure) Run `python3 emi.py run 044`. Report the value and explain in one sentence what it means for the desk.
11. (L06.01.1 Regulated vs restructured states) Run `python3 emi.py run 045 | grep '^markets:'`. Report the value and explain in one sentence what it means for the desk.
12. (L06.10.4 Settlement statements) Run `python3 emi.py run 050 | grep '^all_energy_USD_per_h:'`. Report the value and explain in one sentence what it means for the desk.
13. (L07.01.1 Thermal technologies) Run `python3 emi.py run 053 | grep '^NUC_cost:'`. Report the value and explain in one sentence what it means for the desk.
14. (L07.10.4 Constraint interactions) Run `python3 emi.py run 065 | grep '^energy_charged_MWh:'`. Report the value and explain in one sentence what it means for the desk.
15. (L08.01.1 Front-office functions) Run `python3 emi.py run 072 | grep '^events:'`. Report the value and explain in one sentence what it means for the desk.
16. (L08.10.4 Endur as an enterprise ETRM example) Run `python3 emi.py run 076 | grep '^price_coverage_pct:'`. Report the value and explain in one sentence what it means for the desk.
17. (L09.01.1 Price series properties) Run `python3 emi.py run 078 | grep '^observations:'`. Report the value and explain in one sentence what it means for the desk.
18. (L09.10.4 Weather derivatives) Run `python3 emi.py run 085 | grep '^payout_USD:'`. Report the value and explain in one sentence what it means for the desk.
19. (L10.01.1 Optimization problem structure) Run `python3 emi.py run 090 | grep '^base_transport_cost_USD_per_d:'`. Report the value and explain in one sentence what it means for the desk.
20. (L10.10.4 Result-equivalence validation) Run `python3 emi.py run 093 | grep '^reduced_resolution_objective_error_pct:'`. Report the value and explain in one sentence what it means for the desk.
21. (L11.01.1 Segment taxonomy) Run `python3 emi.py run 095 | grep '^rank_1:'`. Report the value and explain in one sentence what it means for the desk.
22. (L11.10.4 Managing trade-offs) Run `python3 emi.py run 100 | grep '^Pipeline_Disruption_portfolio_value_USD:'`. Report the value and explain in one sentence what it means for the desk.
23. (L12.01.1 Gas-power coupling) Run `python3 emi.py run 066 | grep '^fuel_needed_MMBtu_per_h:'`. Report the value and explain in one sentence what it means for the desk.
24. (L12.10.4 Q&A preparation) Run `python3 emi.py run 100 | grep '^Pipeline_Disruption_portfolio_value_USD:'`. Report the value and explain in one sentence what it means for the desk.

## Part B

1. Run `python3 emi.py run 038 gas_price=5` and state the ethane decision and why.
2. Run `python3 emi.py run 017 edge=P001 cut=0.5` and name the node that goes short.
3. Run `python3 emi.py run 027` and split the P&L into Henry Hub and basis parts.
4. Run `python3 emi.py run 081` and `python3 emi.py run 082`; explain why Expected Shortfall exceeds VaR.
5. Run `python3 emi.py run 100` and present the capstone scenario table in two minutes.
6. Run `python3 emi.py test` and report the number of tests and the result.
