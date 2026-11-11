# Data architecture (as built in this repo)

All data is SYNTHETIC and hypothetical. Everything below is implemented and runnable; nothing describes a vendor system.

| Layer | Location | Built by | Check |
|---|---|---|---|
| Raw synthetic inputs | data/synthetic/*.csv | tools/bootstrap.py, tools/make_synthetic*.py, exercise `data()` helper | files are created once and never overwritten |
| Reference data | data/processed/reference.sqlite (dim_location, ref_pipeline_segment, ref_power_market) | `python3 emi.py run 007` | duplicate_location_names = 0 |
| Ingestion with quality rules | reports/, EX-070 | `python3 emi.py run 070` | rejected rows are logged, not dropped silently |
| Warehouse (star schema) | EX-087 SQLite facts + dimensions | `python3 emi.py run 087` | orphan_facts = 0 |
| API contract | product_management/architecture/ex088_api_contract.md | `python3 emi.py run 088` | status_200 = 3, status_404 = 3 |
| Models | market_models/ (battery, dispatch, dcopf, gas network) | imported by exercises | unit tests in exercises/tests |
| Results | exercises/completed/exNNN/, exercises/expected_output/exNNN.txt | every `emi.py run` | `python3 emi.py test` |
| ETRM integration (proposed) | product_management/architecture/ex099_architecture.md | `python3 emi.py run 099` | vendor_capabilities_asserted = 0 |

Conventions: gas in MMBtu, power in MWh, NGL in gallons; one location name per physical point; scenario runs (`key=value`) print only and save nothing.
Lineage: every number in a lesson page names the command that produces it. Known limits: SQLite stands in for a cloud warehouse; no streaming; no access control.
