# Exercise 005: Interconnection Comparison

## Scenario

A portfolio analyst evaluates modeled generation and directional
transfer capabilities across three North American interconnections.

## Results

Total modeled generation equals supplied peak demand in each
interconnection. This is a synthetic dataset property, not a
general property of electricity systems.

The highest gas-generation-to-peak-demand ratio is
ERCOT at
49.41 percent.

Total interface nameplate capacity across the supplied records:
4.00 GW.

Total available directional interface capacity across the supplied
records:
3.00 GW.

The individual interface capacities are directional. They must not
be interpreted as unrestricted or simultaneously interchangeable
transfer capability.

## Important data discrepancy

The supplied interconnection_transfer_GW field does not consistently
match the interface dataset.

Eastern reports 1.50 GW,
while its supplied outgoing available interfaces total
1.70 GW.

Western reports 1.20 GW,
while its supplied outgoing available interfaces total
0.90 GW.

ERCOT reports 0.00 GW,
while its supplied outgoing available interface totals
0.40 GW.

These fields have not been silently reconciled.

## Commercial interpretation

A trading portfolio cannot assume that electricity can move freely
between the three interconnections. Transfer capability depends on
the specific interface, direction, operating conditions, and
applicable market and reliability rules.

The supplied network diagram represents only the interfaces in
the synthetic dataset. It does not establish complete geographic
or electrical connectivity.

## Model limitations

This exercise does not model transmission power flow, contingency
analysis, losses, congestion pricing, reserves, ramping, or
synchronization constraints. Interface capacity is not equivalent
to firm commercial transmission rights.
