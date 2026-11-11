# Exercise 003: Natural Gas Supply-Chain Report

## Scenario

A fictional Permian Basin production source supplies 1.000 Bcf of raw
natural gas. All volumes and commercial assumptions are synthetic.

## Executive results

| Metric | Result |
|---|---:|
| Raw wellhead production | 1.000 Bcf |
| Processing plant inlet | 0.990 Bcf |
| Residue gas after processing | 0.910 Bcf |
| Gas available after transmission fuel | 0.895 Bcf |
| Total city gate receipts | 0.875 Bcf |
| End-user delivery | 0.870 Bcf |
| End-user delivery yield | 87.00% |
| Remaining storage inventory | 0.020 Bcf |
| Storage share of city gate receipts | 20.57% |

## Original production volume accounting

| Category | Volume (Bcf) | Share |
|---|---:|---:|
| End-user delivery | 0.870 | 87.00% |
| NGL extraction shrinkage, gas equivalent | 0.070 | 7.00% |
| Fuel and unaccounted-for gas | 0.040 | 4.00% |
| Remaining storage inventory | 0.020 | 2.00% |
| **Total accounted volume** | **1.000** | **100.00%** |

## Storage analysis

The scenario injects 0.200 Bcf and later withdraws
0.180 Bcf. The modeled cohort retains
0.020 Bcf in inventory.

Storage shifts the timing of supply. It does not create additional gas.

## Energy and notional commodity-value equivalents

Assumptions: 1.037 MMBtu/Mcf and $3.25/MMBtu.

| Measure | Energy (MMBtu) | Notional value |
|---|---:|---:|
| Wellhead production | 1,037,000 | $3,370,250.00 |
| End-user delivery | 902,190 | $2,932,117.50 |

These are mathematical equivalents, not actual producer revenue, pipeline
revenue, customer bills, realized prices, or a calculation of economic loss.
The model assigns no separate value to recovered NGLs or storage services.

## Accounting validation

**PASS: all accounting checks reconciled.**

- Gathering balance: PASS
- Processing balance: PASS
- Transmission fuel balance: PASS
- Transmission allocation balance: PASS
- Storage inventory balance: PASS
- City gate receipt balance: PASS
- Distribution balance: PASS
- Overall gas-volume accounting bridge: PASS

## Commercial interpretation

1. The original 1.000 Bcf does not reach end users intact.
2. NGL shrinkage represents gas-volume equivalent associated with recovered
   liquids. It does not mean all associated hydrocarbon value disappears.
3. Gathering, processing, transmission, and distribution consume or account
   for gas before final delivery.
4. Storage inventory must be distinguished from gas already delivered.
5. Wellhead production, residue gas, pipeline receipts, storage inventory,
   city gate receipts, and end-user delivery are different measurement points.

## Model limitations

This simplified exercise does not model pipeline pressure, linepack,
nominations, imbalance penalties, capacity rights, compressor performance,
gas quality, actual network topology, hourly demand, operational constraints,
or real market prices.

The NGL shrinkage entry is a gas-volume-equivalent adjustment, not a full
physical mass balance of all hydrocarbon products. The model assumes a
consistent standard-volume basis. Actual contracts and measurement systems
specify reference conditions and heating-value procedures.
