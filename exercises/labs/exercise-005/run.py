#!/usr/bin/env python3

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
OUT = BASE / "outputs"

GENERATION_COLUMNS = [
    "gas_generation_GW",
    "coal_generation_GW",
    "nuclear_generation_GW",
    "renewables_generation_GW",
    "other_generation_GW",
]

REQUIRED_GRID_COLUMNS = [
    "interconnection",
    "peak_demand_GW",
    *GENERATION_COLUMNS,
    "interconnection_transfer_GW",
]

REQUIRED_INTERFACE_COLUMNS = [
    "interface",
    "from_interconnection",
    "to_interconnection",
    "transfer_capacity_MW",
    "available_capacity_MW",
    "transfer_cost_per_MWh",
]


def load_data():
    grid = pd.read_csv(DATA / "grid_interconnections.csv")
    interfaces = pd.read_csv(DATA / "interconnection_interfaces.csv")
    return grid, interfaces


def validate():
    grid, interfaces = load_data()

    missing_grid = set(REQUIRED_GRID_COLUMNS) - set(grid.columns)
    missing_interfaces = set(REQUIRED_INTERFACE_COLUMNS) - set(interfaces.columns)

    if missing_grid:
        raise ValueError(f"Missing grid columns: {sorted(missing_grid)}")

    if missing_interfaces:
        raise ValueError(f"Missing interface columns: {sorted(missing_interfaces)}")

    if grid["interconnection"].duplicated().any():
        raise ValueError("Duplicate interconnection identifiers")

    if interfaces["interface"].duplicated().any():
        raise ValueError("Duplicate interface identifiers")

    numeric_grid = [
        "peak_demand_GW",
        *GENERATION_COLUMNS,
        "interconnection_transfer_GW",
    ]

    numeric_interfaces = [
        "transfer_capacity_MW",
        "available_capacity_MW",
        "transfer_cost_per_MWh",
    ]

    if grid[numeric_grid].isna().any().any():
        raise ValueError("Missing numeric grid observations")

    if interfaces[numeric_interfaces].isna().any().any():
        raise ValueError("Missing numeric interface observations")

    if (grid[numeric_grid] < 0).any().any():
        raise ValueError("Negative values found in nonnegative grid fields")

    if (interfaces[numeric_interfaces] < 0).any().any():
        raise ValueError("Negative interface values found")

    if (
        interfaces["available_capacity_MW"]
        > interfaces["transfer_capacity_MW"]
    ).any():
        raise ValueError("Available capacity exceeds interface capacity")

    known_nodes = set(grid["interconnection"])

    endpoints = (
        set(interfaces["from_interconnection"])
        | set(interfaces["to_interconnection"])
    )

    unknown_nodes = endpoints - known_nodes

    if unknown_nodes:
        raise ValueError(f"Unknown interconnection endpoints: {unknown_nodes}")

    print("VALIDATION PASSED")
    print(f"Interconnections: {len(grid)}")
    print(f"Directional interfaces: {len(interfaces)}")
    print("All required columns are present.")
    print("All numerical observations are valid.")
    print("Available interface capacity does not exceed nameplate capacity.")
    print("All interface endpoints match known interconnections.")


def inspect():
    grid, interfaces = load_data()

    print("\n=== GRID INTERCONNECTIONS ===")
    print(grid.to_string(index=False))

    print("\n=== DIRECTIONAL INTERFACES ===")
    print(interfaces.to_string(index=False))

    print("\n=== DATASET DIMENSIONS ===")
    print(f"Grid records: {len(grid)}")
    print(f"Interface records: {len(interfaces)}")


def analyze():
    grid, interfaces = load_data()

    grid["total_generation_GW"] = grid[GENERATION_COLUMNS].sum(axis=1)

    for column in GENERATION_COLUMNS:
        technology = column.replace("_generation_GW", "")
        grid[f"{technology}_share_pct"] = (
            grid[column] / grid["total_generation_GW"] * 100
        )

    grid["gas_to_peak_demand_pct"] = (
        grid["gas_generation_GW"] / grid["peak_demand_GW"] * 100
    )

    shares = [
        f"{column.replace('_generation_GW', '')}_share_pct"
        for column in GENERATION_COLUMNS
    ]

    generation_output = grid[
        [
            "interconnection",
            "peak_demand_GW",
            "total_generation_GW",
            *shares,
            "gas_to_peak_demand_pct",
        ]
    ].copy()

    generation_output.to_csv(
        OUT / "generation_mix.csv", index=False
    )

    peak_demand = grid.set_index("interconnection")["peak_demand_GW"]

    interfaces["nameplate_capacity_GW"] = (
        interfaces["transfer_capacity_MW"] / 1000
    )

    interfaces["available_capacity_GW"] = (
        interfaces["available_capacity_MW"] / 1000
    )

    interfaces["capacity_utilization_pct"] = (
        interfaces["available_capacity_MW"]
        / interfaces["transfer_capacity_MW"]
        * 100
    )

    interfaces["destination_peak_demand_GW"] = (
        interfaces["to_interconnection"].map(peak_demand)
    )

    interfaces["available_capacity_pct_destination_peak"] = (
        interfaces["available_capacity_GW"]
        / interfaces["destination_peak_demand_GW"]
        * 100
    )

    interfaces.to_csv(
        OUT / "interface_capacity_analysis.csv", index=False
    )

    outgoing = (
        interfaces.groupby("from_interconnection")["available_capacity_GW"]
        .sum()
        .rename("outgoing_available_GW")
    )

    incoming = (
        interfaces.groupby("to_interconnection")["available_capacity_GW"]
        .sum()
        .rename("incoming_available_GW")
    )

    comparison = grid[
        [
            "interconnection",
            "peak_demand_GW",
            "total_generation_GW",
            "gas_to_peak_demand_pct",
            "interconnection_transfer_GW",
        ]
    ].set_index("interconnection")

    comparison = comparison.join(outgoing).join(incoming).fillna(0)

    comparison["incoming_capacity_pct_peak"] = (
        comparison["incoming_available_GW"]
        / comparison["peak_demand_GW"]
        * 100
    )

    comparison["outgoing_capacity_pct_peak"] = (
        comparison["outgoing_available_GW"]
        / comparison["peak_demand_GW"]
        * 100
    )

    comparison = comparison.reset_index()

    comparison.to_csv(
        OUT / "interconnection_comparison.csv", index=False
    )

    print("\nGENERATION MIX AND GAS DEPENDENCE")
    print(generation_output.round(3).to_string(index=False))

    print("\nDIRECTIONAL INTERFACE CAPACITY")
    print(
        interfaces[
            [
                "interface",
                "from_interconnection",
                "to_interconnection",
                "available_capacity_GW",
                "available_capacity_pct_destination_peak",
            ]
        ].round(4).to_string(index=False)
    )

    print("\nINTERCONNECTION COMPARISON")
    print(comparison.round(4).to_string(index=False))

    print("\nANALYSIS FILES CREATED")
    print(OUT / "generation_mix.csv")
    print(OUT / "interface_capacity_analysis.csv")
    print(OUT / "interconnection_comparison.csv")


def report():
    analyze()

    grid, interfaces = load_data()
    generation = pd.read_csv(OUT / "generation_mix.csv")
    comparison = pd.read_csv(OUT / "interconnection_comparison.csv")
    interface_results = pd.read_csv(
        OUT / "interface_capacity_analysis.csv"
    )

    OUT.mkdir(parents=True, exist_ok=True)

    technologies = [
        "gas",
        "coal",
        "nuclear",
        "renewables",
        "other",
    ]

    ax = generation.set_index("interconnection")[
        [f"{technology}_share_pct" for technology in technologies]
    ].plot(
        kind="bar",
        stacked=True,
        figsize=(10, 6),
    )

    ax.set_title("Synthetic Generation Mix by Interconnection")
    ax.set_ylabel("Share of modeled generation (%)")
    ax.set_xlabel("Interconnection")
    ax.legend(
        [technology.replace("_share_pct", "").title()
         for technology in ax.get_legend_handles_labels()[1]],
        title="Technology",
    )
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(OUT / "generation_mix.png", dpi=160)
    plt.close()

    graph = nx.DiGraph()

    for _, row in grid.iterrows():
        graph.add_node(
            row["interconnection"],
            peak=row["peak_demand_GW"],
        )

    for _, row in interface_results.iterrows():
        source = row["from_interconnection"]
        destination = row["to_interconnection"]

        if graph.has_edge(source, destination):
            graph[source][destination]["available_GW"] += (
                row["available_capacity_GW"]
            )
            graph[source][destination]["interfaces"].append(
                row["interface"]
            )
        else:
            graph.add_edge(
                source,
                destination,
                available_GW=row["available_capacity_GW"],
                interfaces=[row["interface"]],
            )

    positions = {
        "Eastern": (1, 0),
        "Western": (-1, 0),
        "ERCOT": (0, -1),
    }

    plt.figure(figsize=(10, 7))

    nx.draw_networkx_nodes(
        graph,
        positions,
        node_size=3500,
    )

    labels = {
        node: f"{node}\nPeak: {graph.nodes[node]['peak']} GW"
        for node in graph.nodes
    }

    nx.draw_networkx_labels(
        graph,
        positions,
        labels=labels,
        font_size=9,
    )

    nx.draw_networkx_edges(
        graph,
        positions,
        arrows=True,
        arrowsize=22,
        connectionstyle="arc3,rad=0.12",
        width=2,
    )

    edge_labels = {
        (source, destination): (
            f"{data['available_GW']:.2f} GW available"
        )
        for source, destination, data in graph.edges(data=True)
    }

    nx.draw_networkx_edge_labels(
        graph,
        positions,
        edge_labels=edge_labels,
        font_size=8,
        label_pos=0.5,
    )

    plt.title("Synthetic Directional Interconnection Interfaces")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(OUT / "interconnection_network.png", dpi=160)
    plt.close()

    highest_gas = comparison.loc[
        comparison["gas_to_peak_demand_pct"].idxmax()
    ]

    total_nameplate = interfaces["transfer_capacity_MW"].sum()
    total_available = interfaces["available_capacity_MW"].sum()

    report_text = f"""# Exercise 005: Interconnection Comparison

## Scenario

A portfolio analyst evaluates modeled generation and directional
transfer capabilities across three North American interconnections.

## Results

Total modeled generation equals supplied peak demand in each
interconnection. This is a synthetic dataset property, not a
general property of electricity systems.

The highest gas-generation-to-peak-demand ratio is
{highest_gas['interconnection']} at
{highest_gas['gas_to_peak_demand_pct']:.2f} percent.

Total interface nameplate capacity across the supplied records:
{total_nameplate / 1000:.2f} GW.

Total available directional interface capacity across the supplied
records:
{total_available / 1000:.2f} GW.

The individual interface capacities are directional. They must not
be interpreted as unrestricted or simultaneously interchangeable
transfer capability.

## Important data discrepancy

The supplied interconnection_transfer_GW field does not consistently
match the interface dataset.

Eastern reports {comparison.loc[comparison.interconnection == 'Eastern', 'interconnection_transfer_GW'].iloc[0]:.2f} GW,
while its supplied outgoing available interfaces total
{comparison.loc[comparison.interconnection == 'Eastern', 'outgoing_available_GW'].iloc[0]:.2f} GW.

Western reports {comparison.loc[comparison.interconnection == 'Western', 'interconnection_transfer_GW'].iloc[0]:.2f} GW,
while its supplied outgoing available interfaces total
{comparison.loc[comparison.interconnection == 'Western', 'outgoing_available_GW'].iloc[0]:.2f} GW.

ERCOT reports {comparison.loc[comparison.interconnection == 'ERCOT', 'interconnection_transfer_GW'].iloc[0]:.2f} GW,
while its supplied outgoing available interface totals
{comparison.loc[comparison.interconnection == 'ERCOT', 'outgoing_available_GW'].iloc[0]:.2f} GW.

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
"""

    (OUT / "comparison_report.md").write_text(report_text)

    print("\nREPORT AND CHARTS CREATED")
    for filename in [
        "generation_mix.png",
        "interconnection_network.png",
        "comparison_report.md",
    ]:
        print(OUT / filename)


def test():
    generation = pd.read_csv(OUT / "generation_mix.csv")
    interfaces = pd.read_csv(OUT / "interface_capacity_analysis.csv")
    comparison = pd.read_csv(OUT / "interconnection_comparison.csv")

    expected_generation = {
        "Eastern": 620,
        "Western": 165,
        "ERCOT": 85,
    }

    for name, expected in expected_generation.items():
        actual = generation.loc[
            generation["interconnection"] == name,
            "total_generation_GW",
        ].iloc[0]

        assert abs(actual - expected) < 1e-9, (
            f"{name} generation total incorrect"
        )

    expected_gas_dependence = {
        "Eastern": 190 / 620 * 100,
        "Western": 38 / 165 * 100,
        "ERCOT": 42 / 85 * 100,
    }

    for name, expected in expected_gas_dependence.items():
        actual = comparison.loc[
            comparison["interconnection"] == name,
            "gas_to_peak_demand_pct",
        ].iloc[0]

        assert abs(actual - expected) < 1e-8, (
            f"{name} gas dependence incorrect"
        )

    assert abs(interfaces["available_capacity_MW"].sum() - 3000) < 1e-9
    assert abs(interfaces["transfer_capacity_MW"].sum() - 4000) < 1e-9

    western_incoming = comparison.loc[
        comparison["interconnection"] == "Western",
        "incoming_available_GW",
    ].iloc[0]

    assert abs(western_incoming - 1.7) < 1e-9

    ercot_gas = comparison.loc[
        comparison["interconnection"] == "ERCOT",
        "gas_to_peak_demand_pct",
    ].iloc[0]

    assert ercot_gas > expected_gas_dependence["Eastern"]
    assert ercot_gas > expected_gas_dependence["Western"]

    print("ALL EXERCISE 005 TESTS PASSED")
    print("Generation totals verified.")
    print("Gas-generation dependence verified.")
    print("Directional transfer totals verified.")
    print("ERCOT has the highest modeled gas dependence.")


def main():
    parser = argparse.ArgumentParser(
        description="Exercise 005: North American Grid Interconnections"
    )

    parser.add_argument(
        "operation",
        choices=["inspect", "validate", "analyze", "report", "test"],
    )

    args = parser.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)

    operations = {
        "inspect": inspect,
        "validate": validate,
        "analyze": analyze,
        "report": report,
        "test": test,
    }

    operations[args.operation]()


if __name__ == "__main__":
    main()
