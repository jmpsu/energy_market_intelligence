# EX-095 Product requirements (SYNTHETIC HYPOTHETICAL DATA - not historical market data)

Score = customer value / engineering person-weeks x (6 - technical risk) / 5. Single-interview evidence per persona: treat as hypotheses.

## REQ-01 Automated basis monitoring
- Persona: Gas_Trader (C001); problem: Regional_basis_analysis; 416 h/yr; stated impact $250,000/yr
- Requirement: the product shall provide basis by hub vs Henry Hub refreshed within 5 minutes of each curated price load; alert when basis moves beyond a user-set threshold.
- Acceptance test: automated check on the reference dataset passes for the stated condition.
- Success KPI: analyst hours on basis analysis per week.
- Score 25,000; effort 8 person-weeks; risk 2/5

## REQ-02 Unified risk dashboard
- Persona: Portfolio_Manager (C003); problem: Portfolio_risk_visibility; 520 h/yr; stated impact $650,000/yr
- Requirement: the product shall provide one view of position, MtM, VaR and stress loss by book, reconciling to the position ledger to the dollar.
- Acceptance test: automated check on the reference dataset passes for the stated condition.
- Success KPI: share of books covered; time to produce the daily risk pack.
- Score 24,375; effort 16 person-weeks; risk 3/5

## REQ-03 Automated nomination reconciliation
- Persona: Gas_Scheduler (C004); problem: Pipeline_capacity_reconciliation; 312 h/yr; stated impact $180,000/yr
- Requirement: the product shall provide contracted, scheduled and delivered volumes matched per trade with every break above tolerance listed with a reason code.
- Acceptance test: automated check on the reference dataset passes for the stated condition.
- Success KPI: breaks found before invoice issue; scheduler hours per week.
- Score 12,000; effort 12 person-weeks; risk 2/5

## REQ-04 Integrated dispatch simulation
- Persona: Power_Analyst (C002); problem: Generation_dispatch_analysis; 624 h/yr; stated impact $400,000/yr
- Requirement: the product shall provide dispatch run for a gas unit plus storage reproduces an independent benchmark within 0.1 percent of objective value.
- Acceptance test: automated check on the reference dataset passes for the stated condition.
- Success KPI: simulations run per user per week.
- Score 6,667; effort 24 person-weeks; risk 4/5

## REQ-05 Simulation performance optimization
- Persona: Quant_Analyst (C005); problem: Slow_model_execution; 780 h/yr; stated impact $500,000/yr
- Requirement: the product shall provide runtime on the reference study reduced with identical objective value (relative difference below 1e-6) and zero constraint violations.
- Acceptance test: automated check on the reference dataset passes for the stated condition.
- Success KPI: median study runtime; scenarios per study.
- Score 5,000; effort 20 person-weeks; risk 5/5
