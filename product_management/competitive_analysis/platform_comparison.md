# Platform comparison

STATUS: every vendor, category and capability cell below is [K] = general knowledge NOT verified against vendor documentation in this build. Treat nothing here as a product fact. No capability, price or performance claim is asserted.
The 'this repo' column is [EX]: it names the exercise in this repository that reproduces the concept on synthetic data, so you can discuss the workflow without asserting vendor features.

| Platform | Vendor [K] | Category [K] | Concept reproduced in this repo [EX] | Verified from vendor docs? |
|---|---|---|---|---|
| PLEXOS | Energy Exemplar | power/gas market simulation | EX-089 production cost, EX-091 capacity expansion, EX-090 gas network | NO - verify before use |
| PLEXOS Cloud | Energy Exemplar | hosted simulation | EX-092/093 runtime and equivalence | NO - verify before use |
| Aurora | Energy Exemplar | power market forecasting | EX-077 price forecast, EX-049 clearing | NO - verify before use |
| Adapt2 | Energy Exemplar | bid-to-bill / market operations | EX-052 settlements | NO - verify before use |
| Endur | ION (Openlink) | ETRM | EX-069/072/076 trade capture, lifecycle, integration | NO - verify before use |
| PSS/E | Siemens | transmission planning power flow | EX-048/056 DC-OPF, PTDF | NO - verify before use |
| PowerWorld | PowerWorld Corp | power flow / visualisation | EX-056 congestion | NO - verify before use |
| Dayzer | Cambridge Energy Solutions | nodal market simulation | EX-048 LMP, EX-058 FTR | NO - verify before use |
| Enelytix / TARA | Newton Energy Group / PowerGEM | cloud market simulation / transmission analysis | EX-092/093, EX-056 | NO - verify before use |
| Enverus Mosaic | Enverus | power market analytics | EX-009 dashboard, EX-047 DA/RT | NO - verify before use |
| Yes Energy | Yes Energy | ISO market data | EX-070 ingestion, EX-047 | NO - verify before use |
| Bloomberg | Bloomberg | market data terminal | EX-070, EX-023 curves | NO - verify before use |
| ICE | Intercontinental Exchange | exchange, clearing, market data | EX-024 futures/swaps, EX-073 margin | NO - verify before use |
| LSEG | LSEG | market data and analytics | EX-070, EX-088 API | NO - verify before use |
| Snowflake | Snowflake | cloud data warehouse | EX-087 star schema (SQLite) | NO - verify before use |
| Databricks | Databricks | lakehouse / compute | EX-087, EX-093 | NO - verify before use |

## How to verify (do this before your first vendor conversation)

For each platform record in `product_management/competitive_analysis/verification_log.csv`: capability, exact quote, URL, date read. Only quoted rows may be moved from hypothetical to verified.

## Hypothetical integration (proposed, not a vendor feature)

See `product_management/architecture/ex099_architecture.md`: every component there is marked proposed; `vendor_capabilities_asserted = 0` is enforced by a test.
