# EX-088 market data API contract (SYNTHETIC HYPOTHETICAL DATA - not historical market data)

GET /v1/locations -> 200 list
GET /v1/prices/<location> -> 200 observations | 404 unknown location | 404 no validated price
GET /v1/prices/<location>/<timestamp> -> 200 | 404
anything else -> 400

Every 200 price response carries unit, currency, provider and data_classification.
