# EX-096 Integrated gas, NGL and power analytics: product specification (SYNTHETIC HYPOTHETICAL DATA - not historical market data)

Hypothetical product. Each requirement is traceable to a working exercise and an automated test in this repository.

## R01 basis by hub vs benchmark with alerts
- User: Gas_Trader | Workflow: morning basis review
- Data required: hub prices
- Acceptance: basis equals hub minus benchmark to 1e-6 on the reference set
- Evidence: EX-019 (exists: True, automated test: True)

## R02 hub-to-hub netback by product
- User: NGL_Marketer | Workflow: daily arbitrage screen
- Data required: NGL hub prices and logistics costs
- Acceptance: net margin equals basis minus logistics cost for every product and date
- Evidence: EX-040 (exists: True, automated test: True)

## R03 recover or reject with plant-level breakeven
- User: Plant_Optimiser | Workflow: monthly ethane decision
- Data required: composition recovery fees gas and NGL prices
- Acceptance: decision flips exactly at the reported breakeven price
- Evidence: EX-038 (exists: True, automated test: True)

## R04 nodal prices with congestion component
- User: Power_Analyst | Workflow: congestion study
- Data required: network topology limits offers
- Acceptance: LMPs match the hand-solved three-bus case
- Evidence: EX-056 (exists: True, automated test: True)

## R05 VaR ES and stress losses against limits
- User: Risk_Manager | Workflow: daily risk pack
- Data required: positions and factor history
- Acceptance: component VaR sums to portfolio VaR
- Evidence: EX-081 (exists: True, automated test: True)

## R06 contracted scheduled delivered break report
- User: Scheduler | Workflow: volume reconciliation
- Data required: trades nominations actuals
- Acceptance: every break above tolerance is listed
- Evidence: EX-075 (exists: True, automated test: True)

## R07 faster runs with proven identical results
- User: Quant_Analyst | Workflow: study turnaround
- Data required: model inputs and baseline outputs
- Acceptance: relative objective difference below 1e-6 and zero constraint violation
- Evidence: EX-092 (exists: True, automated test: True)

## R08 validated curated prices with lineage
- User: Data_Engineer | Workflow: market data onboarding
- Data required: raw vendor files
- Acceptance: rejected and superseded records are retained with reasons
- Evidence: EX-070 (exists: True, automated test: True)
