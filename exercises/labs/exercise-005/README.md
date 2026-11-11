# Exercise 005: North American Grid Interconnections

Scenario:
A power portfolio analyst evaluates the scale, generation mix,
gas-generation dependence, and modeled transfer capabilities
of the Eastern, Western, and ERCOT interconnections.

Data provenance:
All observations are synthetic educational data.

Units:
Peak demand and generation: GW
Interface capacity: MW
Transfer cost: USD/MWh
Generation shares: percent
Transfer capacity relative to destination peak demand: percent

Assumptions:
Generation shares use total modeled generation as the denominator.
Gas-generation dependence uses peak demand as the denominator.
Interface transfer percentages use the receiving interconnection's
peak demand as the denominator.

The interface dataset describes directional transfer capabilities.
It does not establish unrestricted or simultaneous bidirectional
transfers.

The interconnection_transfer_GW field is retained as supplied.
It is not assumed to equal the sum of directional interface capacities.

The network diagram is a logical representation, not a geographic map.
