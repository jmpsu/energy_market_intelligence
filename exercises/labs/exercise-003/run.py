from pathlib import Path
import math
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
OUT = BASE / "outputs"

FLOW_FILE = DATA / "flow_events.csv"
ASSUMPTIONS_FILE = DATA / "market_assumptions.csv"

OUT.mkdir(parents=True, exist_ok=True)

TOLERANCE = 1e-9
MCF_PER_BCF = 1_000_000


def require_file(path):
    if not path.is_file():
        raise FileNotFoundError(f"Required input file not found: {path}")


def load_inputs():
    require_file(FLOW_FILE)
    require_file(ASSUMPTIONS_FILE)

    flow = pd.read_csv(FLOW_FILE)
    assumptions_df = pd.read_csv(ASSUMPTIONS_FILE)

    required_columns = {
        "event_id", "event_name", "stage",
        "volume_bcf", "classification", "notes"
    }

    missing = required_columns.difference(flow.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    if flow["event_id"].duplicated().any():
        raise ValueError("Duplicate event IDs found.")

    if flow["event_name"].duplicated().any():
        raise ValueError("Duplicate event names found.")

    flow["volume_bcf"] = pd.to_numeric(
        flow["volume_bcf"], errors="raise"
    )

    for value in flow["volume_bcf"]:
        if not math.isfinite(float(value)) or value < 0:
            raise ValueError("Volumes must be finite and nonnegative.")

    if assumptions_df["assumption"].duplicated().any():
        raise ValueError("Duplicate assumptions found.")

    assumptions = {
        str(row.assumption): float(row.value)
        for row in assumptions_df.itertuples()
    }

    required_assumptions = {
        "heat_content_mmbtu_per_mcf",
        "flat_commodity_price_usd_per_mmbtu",
    }

    missing = required_assumptions.difference(assumptions)
    if missing:
        raise ValueError(f"Missing assumptions: {sorted(missing)}")

    for key, value in assumptions.items():
        if not math.isfinite(value) or value <= 0:
            raise ValueError(f"Invalid assumption {key}: {value}")

    return flow, assumptions


def main():
    flow, assumptions = load_inputs()
    volumes = flow.set_index("event_name")["volume_bcf"].to_dict()

    required_events = [
        "Wellhead gas produced",
        "Gathering fuel and metering variance",
        "Gas received at processing plant",
        "NGL extraction shrinkage",
        "Processing plant fuel",
        "Residue gas leaving processing",
        "Transmission compressor fuel",
        "Residue gas available for allocation",
        "Direct delivery to city gate",
        "Storage injection",
        "Storage withdrawal",
        "Storage inventory remaining",
        "Total gas received at city gate",
        "Distribution fuel and unaccounted-for gas",
        "Gas delivered to end users",
    ]

    missing = [name for name in required_events if name not in volumes]
    if missing:
        raise ValueError(f"Missing required events: {missing}")

    def v(name):
        return float(volumes[name])

    raw = v("Wellhead gas produced")
    gathering = v("Gathering fuel and metering variance")
    plant_inlet = v("Gas received at processing plant")
    ngl_shrinkage = v("NGL extraction shrinkage")
    plant_fuel = v("Processing plant fuel")
    residue = v("Residue gas leaving processing")
    transmission_fuel = v("Transmission compressor fuel")
    available = v("Residue gas available for allocation")
    direct_delivery = v("Direct delivery to city gate")
    storage_injection = v("Storage injection")
    storage_withdrawal = v("Storage withdrawal")
    storage_inventory = v("Storage inventory remaining")
    city_gate = v("Total gas received at city gate")
    distribution_use = v("Distribution fuel and unaccounted-for gas")
    end_user_delivery = v("Gas delivered to end users")

    checks = []

    def add_check(name, calculated, reported):
        residual = calculated - reported
        checks.append({
            "check": name,
            "calculated_bcf": calculated,
            "reported_bcf": reported,
            "residual_bcf": residual,
            "passed": abs(residual) <= TOLERANCE,
        })

    add_check("Gathering balance", raw - gathering, plant_inlet)

    add_check(
        "Processing balance",
        plant_inlet - ngl_shrinkage - plant_fuel,
        residue,
    )

    add_check(
        "Transmission fuel balance",
        residue - transmission_fuel,
        available,
    )

    add_check(
        "Transmission allocation balance",
        available,
        direct_delivery + storage_injection,
    )

    add_check(
        "Storage inventory balance",
        storage_injection,
        storage_withdrawal + storage_inventory,
    )

    add_check(
        "City gate receipt balance",
        direct_delivery + storage_withdrawal,
        city_gate,
    )

    add_check(
        "Distribution balance",
        city_gate - distribution_use,
        end_user_delivery,
    )

    fuel_and_uaf = (
        gathering + plant_fuel + transmission_fuel + distribution_use
    )

    accounted_volume = (
        end_user_delivery
        + ngl_shrinkage
        + fuel_and_uaf
        + storage_inventory
    )

    add_check(
        "Overall gas-volume accounting bridge",
        raw,
        accounted_volume,
    )

    checks_df = pd.DataFrame(checks)
    checks_df.to_csv(OUT / "mass_balance_checks.csv", index=False)

    bridge = pd.DataFrame([
        {
            "category": "Gas delivered to end users",
            "volume_bcf": end_user_delivery,
        },
        {
            "category": "NGL extraction shrinkage, gas equivalent",
            "volume_bcf": ngl_shrinkage,
        },
        {
            "category": "Fuel and unaccounted-for gas",
            "volume_bcf": fuel_and_uaf,
        },
        {
            "category": "Remaining storage inventory",
            "volume_bcf": storage_inventory,
        },
    ])

    bridge["share_of_wellhead_production_pct"] = (
        bridge["volume_bcf"] / raw * 100
    )
    bridge.to_csv(OUT / "volume_accounting.csv", index=False)

    process_steps = pd.DataFrame([
        ["Wellhead production", raw],
        ["Processing plant inlet", plant_inlet],
        ["Residue gas after processing", residue],
        ["Gas available after transmission fuel", available],
        ["Direct delivery to city gate", direct_delivery],
        ["Storage injection", storage_injection],
        ["Storage withdrawal", storage_withdrawal],
        ["Total city gate receipts", city_gate],
        ["End-user delivery", end_user_delivery],
    ], columns=["process_step", "volume_bcf"])

    process_steps.to_csv(OUT / "process_steps.csv", index=False)

    heat_content = assumptions["heat_content_mmbtu_per_mcf"]
    price = assumptions["flat_commodity_price_usd_per_mmbtu"]

    energy_rows = []

    for label, volume in [
        ("Wellhead production", raw),
        ("End-user delivery", end_user_delivery),
    ]:
        mcf = volume * MCF_PER_BCF
        mmbtu = mcf * heat_content
        value = mmbtu * price

        energy_rows.append({
            "measure": label,
            "volume_bcf": volume,
            "volume_mcf": mcf,
            "energy_mmbtu": mmbtu,
            "assumed_price_usd_per_mmbtu": price,
            "notional_value_usd": value,
        })

    energy_df = pd.DataFrame(energy_rows)
    energy_df.to_csv(OUT / "energy_value_equivalent.csv", index=False)

    fig, ax = plt.subplots(figsize=(11, 4))
    left = 0.0

    for row in bridge.itertuples():
        width = float(row.volume_bcf)

        ax.barh(
            ["1.000 Bcf produced"],
            [width],
            left=left,
            label=f"{row.category}: {width:.3f} Bcf",
        )

        if width >= 0.035:
            ax.text(
                left + width / 2,
                0,
                f"{width:.3f}",
                ha="center",
                va="center",
            )

        left += width

    ax.set_xlim(0, raw)
    ax.set_xlabel("Bcf, gas-volume equivalent")
    ax.set_title("Where the Original 1.000 Bcf Goes")
    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.25),
        ncol=2,
        frameon=False,
    )

    fig.tight_layout()
    fig.savefig(
        OUT / "volume_accounting.png",
        dpi=160,
        bbox_inches="tight",
    )
    plt.close(fig)

    delivery_yield = end_user_delivery / raw * 100
    storage_withdrawal_share = storage_withdrawal / city_gate * 100

    production_energy = raw * MCF_PER_BCF * heat_content
    delivery_energy = end_user_delivery * MCF_PER_BCF * heat_content

    production_value = production_energy * price
    delivery_value = delivery_energy * price

    passed = int(checks_df["passed"].sum())
    total_checks = len(checks_df)

    failed_checks = checks_df.loc[~checks_df["passed"]]

    check_lines = [
        f"- {row.check}: {'PASS' if row.passed else 'FAIL'}"
        for row in checks_df.itertuples()
    ]

    status = (
        "PASS: all accounting checks reconciled."
        if failed_checks.empty
        else "FAIL: one or more accounting checks did not reconcile."
    )

    report = f"""# Exercise 003: Natural Gas Supply-Chain Report

## Scenario

A fictional Permian Basin production source supplies 1.000 Bcf of raw
natural gas. All volumes and commercial assumptions are synthetic.

## Executive results

| Metric | Result |
|---|---:|
| Raw wellhead production | {raw:.3f} Bcf |
| Processing plant inlet | {plant_inlet:.3f} Bcf |
| Residue gas after processing | {residue:.3f} Bcf |
| Gas available after transmission fuel | {available:.3f} Bcf |
| Total city gate receipts | {city_gate:.3f} Bcf |
| End-user delivery | {end_user_delivery:.3f} Bcf |
| End-user delivery yield | {delivery_yield:.2f}% |
| Remaining storage inventory | {storage_inventory:.3f} Bcf |
| Storage share of city gate receipts | {storage_withdrawal_share:.2f}% |

## Original production volume accounting

| Category | Volume (Bcf) | Share |
|---|---:|---:|
| End-user delivery | {end_user_delivery:.3f} | {end_user_delivery / raw * 100:.2f}% |
| NGL extraction shrinkage, gas equivalent | {ngl_shrinkage:.3f} | {ngl_shrinkage / raw * 100:.2f}% |
| Fuel and unaccounted-for gas | {fuel_and_uaf:.3f} | {fuel_and_uaf / raw * 100:.2f}% |
| Remaining storage inventory | {storage_inventory:.3f} | {storage_inventory / raw * 100:.2f}% |
| **Total accounted volume** | **{accounted_volume:.3f}** | **{accounted_volume / raw * 100:.2f}%** |

## Storage analysis

The scenario injects {storage_injection:.3f} Bcf and later withdraws
{storage_withdrawal:.3f} Bcf. The modeled cohort retains
{storage_inventory:.3f} Bcf in inventory.

Storage shifts the timing of supply. It does not create additional gas.

## Energy and notional commodity-value equivalents

Assumptions: {heat_content:.3f} MMBtu/Mcf and ${price:.2f}/MMBtu.

| Measure | Energy (MMBtu) | Notional value |
|---|---:|---:|
| Wellhead production | {production_energy:,.0f} | ${production_value:,.2f} |
| End-user delivery | {delivery_energy:,.0f} | ${delivery_value:,.2f} |

These are mathematical equivalents, not actual producer revenue, pipeline
revenue, customer bills, realized prices, or a calculation of economic loss.
The model assigns no separate value to recovered NGLs or storage services.

## Accounting validation

**{status}**

{chr(10).join(check_lines)}

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
"""

    (OUT / "comparison_report.md").write_text(report, encoding="utf-8")

    print("\n=== NATURAL GAS SUPPLY-CHAIN ANALYSIS ===")
    print(f"Wellhead production:       {raw:.3f} Bcf")
    print(f"Residue gas:               {residue:.3f} Bcf")
    print(f"City gate receipts:        {city_gate:.3f} Bcf")
    print(f"End-user delivery:         {end_user_delivery:.3f} Bcf")
    print(f"End-user delivery yield:   {delivery_yield:.2f}%")
    print(f"Remaining storage:         {storage_inventory:.3f} Bcf")
    print(f"\nAccounting checks: {passed}/{total_checks} passed")

    if not failed_checks.empty:
        print("\nFAILED CHECKS:")
        print(failed_checks.to_string(index=False))
        raise SystemExit(1)

    print("\nGenerated files:")
    for path in sorted(OUT.iterdir()):
        if path.is_file():
            print(f"  {path.name}")

    print("\nRESULT: All accounting checks passed.")


if __name__ == "__main__":
    main()
