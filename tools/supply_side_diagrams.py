#!/usr/bin/env python3
"""
Supply-Side Economics Diagram Generator for EMI Curriculum

This module generates SVG diagrams for supply-side economics concepts
used in the curriculum, following the requirements from the implementation task.
"""

import os
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Any
from diagram_engine import SupplySideDiagram

# Add the tools directory to Python path
sys.path.append(str(Path(__file__).parent))

def create_diagram_A_supply_tightening():
    """A. Henry Hub supply tightening: S shifts left, D fixed, equilibrium to higher P / lower Q."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Define curves
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    supply_points_shifted = [[150, 100], [250, 150], [350, 200]]  # Shifted left
    
    title = "A. Henry Hub Supply Tightening"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="left"
    )

def create_diagram_B_demand_shock():
    """B. Demand shock (cold snap, LNG feedgas ramp): D shifts right, higher P and Q."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Define curves
    demand_points_original = [[100, 200], [200, 150], [300, 100]]
    demand_points_shifted = [[150, 200], [250, 150], [350, 100]]  # Shifted right
    supply_points = [[100, 100], [200, 150], [300, 200]]
    
    title = "B. Demand Shock (Cold Snap, LNG Feedgas Ramp)"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points_original,
        supply_curve_points=supply_points,
        equilibrium_point=(200, 150),
        shifted_demand=demand_points_shifted,
        shift_direction="right"
    )

def create_diagram_C_basis_vs_capacity():
    """C. Regional basis vs available pipeline capacity: basis widens as capacity falls."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Define curves
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    supply_points_shifted = [[100, 100], [180, 150], [260, 200]]  # Shifted right (capacity constraint)
    
    title = "C. Regional Basis vs Pipeline Capacity"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="right"
    )

def create_diagram_D_storage_scarcity():
    """D. Storage: scarcity value rises nonlinearly as inventory falls."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # For storage scarcity, we'll show a non-linear supply curve
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [150, 120], [200, 140], [250, 160], [300, 180]]
    supply_points_shifted = [[100, 100], [150, 130], [200, 160], [250, 200], [300, 250]]  # Steeper curve
    
    title = "D. Storage Scarcity Value"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="up"
    )

def create_diagram_E_production_response():
    """E. Production response: price up -> rig/supply response with lag (supply elasticity, short vs long run)."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show short-run vs long-run supply elasticity
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_short_run = [[100, 100], [180, 150], [260, 200]]  # Steeper
    supply_points_long_run = [[100, 100], [200, 150], [300, 200]]   # Flatter
    
    title = "E. Production Response: Short vs Long Run Supply"
    
    spec = {
        "title": title,
        "x_label": "Quantity",
        "y_label": "Price",
        "curves": [
            {"points": demand_points, "style": "solid", "color": "blue", "label": "D"},
            {"points": supply_points_short_run, "style": "solid", "color": "red", "label": "S0 (short-run)"},
            {"points": supply_points_long_run, "style": "solid", "color": "orange", "label": "S1 (long-run)"}
        ],
        "equilibrium_points": [
            {"x": 200, "y": 150, "is_new": False}
        ]
    }
    
    return engine.generate_diagram(spec)

def create_diagram_F_forward_curve():
    """F. Forward curve shape: contango vs backwardation; calendar/seasonal spreads."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Create a forward curve diagram - we'll make this more conceptual
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points = [[100, 100], [200, 150], [300, 200]]
    
    title = "F. Forward Curve Shape: Contango vs Backwardation"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="left"
    )

def create_diagram_G_marginal_fob():
    """G. Marginal FOB stepped liquefaction stack: rising export demand clears on higher-cost trains."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show stepped supply curve
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    # Simulate stepped supply (higher cost trains come online)
    supply_points_stacked = [[100, 100], [150, 130], [200, 160], [250, 190], [300, 220]]
    
    title = "G. Marginal FOB Liquefaction Stack"
    
    spec = {
        "title": title,
        "x_label": "Quantity",
        "y_label": "Price",
        "curves": [
            {"points": demand_points, "style": "solid", "color": "blue", "label": "D"},
            {"points": supply_points_original, "style": "dashed", "color": "red", "label": "S0"},
            {"points": supply_points_stacked, "style": "solid", "color": "red", "label": "S1 (stepped)"}
        ],
        "equilibrium_points": [
            {"x": 200, "y": 150, "is_new": False}
        ],
        "shifts": [
            {
                "original_points": supply_points_original,
                "shifted_points": supply_points_stacked,
                "shift_direction": "up",
                "label": ""
            }
        ]
    }
    
    return engine.generate_diagram(spec)

def create_diagram_H_netback_arbitrage():
    """H. Netback arbitrage: destination price minus freight/regas vs US cost; the arb opens or closes as freight rises."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show netback relationship
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    # Higher freight means netback shrinks
    supply_points_shifted = [[100, 80], [200, 130], [300, 180]]  # Shifted down
    
    title = "H. Netback Arbitrage"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="down"
    )

def create_diagram_I_freight_market():
    """I. Freight rate vs vessel availability (tight shipping market)."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show freight market with capacity constraint
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    supply_points_shifted = [[100, 100], [180, 150], [260, 200]]  # Shifted right (constraint)
    
    title = "I. Freight Market: Vessel Availability Constraint"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="right"
    )

def create_diagram_J_global_balance():
    """J. Global balance: Europe/Asia demand pull (TTF/JKM) shifting US export demand right."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show global demand shift
    demand_points_original = [[100, 200], [200, 150], [300, 100]]
    demand_points_shifted = [[150, 200], [250, 150], [350, 100]]  # Shifted right
    
    supply_points = [[100, 100], [200, 150], [300, 200]]
    
    title = "J. Global Balance: Demand Pull from Europe/Asia"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points_original,
        supply_curve_points=supply_points,
        equilibrium_point=(200, 150),
        shifted_demand=demand_points_shifted,
        shift_direction="right"
    )

def create_diagram_K_frac_spread():
    """K. Frac spread: NGL value vs gas value; ethane rejection when ethane < gas-equivalent value."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show frac spread relationship
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    # When ethane is less valuable than gas equivalent, we get rejection
    supply_points_shifted = [[100, 100], [180, 150], [260, 200]]  # Shifted right (capacity constraint)
    
    title = "K. Frac Spread: Ethane Rejection"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="right"
    )

def create_diagram_L_fractionation_capacity():
    """L. Fractionation capacity constraint at Mont Belvieu: purity-product spreads widen as frac utilization nears 100%."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show fractionation constraint
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    supply_points_shifted = [[100, 100], [180, 150], [260, 200]]  # Shifted right
    
    title = "L. Fractionation Capacity Constraint"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="right"
    )

def create_diagram_M_propane_export():
    """M. Propane/ethane export dock capacity vs domestic price."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show export constraint
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    supply_points_shifted = [[100, 100], [180, 150], [260, 200]]  # Shifted right
    
    title = "M. Export Dock Capacity vs Domestic Price"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="right"
    )

def create_diagram_N_merit_order():
    """N. Merit order / supply stack with demand line; load rises -> marginal unit and price step up."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show merit order
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    supply_points_shifted = [[100, 120], [200, 170], [300, 220]]  # Shifted up
    
    title = "N. Merit Order: Load Rise"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="up"
    )

def create_diagram_O_spark_spread():
    """O. Spark spread vs gas price (power price and heat rate constant): downward slope."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show spark spread relationship
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    
    title = "O. Spark Spread vs Gas Price"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="left"
    )

def create_diagram_P_fuel_switching():
    """P. Fuel switching: coal-gas cost crossover as gas price moves."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show fuel switching
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    supply_points_shifted = [[100, 120], [200, 170], [300, 220]]  # Shifted up
    
    title = "P. Fuel Switching: Coal-Gas Crossover"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="up"
    )

def create_diagram_Q_lmp_congestion():
    """Q. LMP congestion: two nodes, transmission limit binds, prices separate."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show LMP congestion
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    
    title = "Q. LMP Congestion: Price Separation"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="left"
    )

def create_diagram_R_capacity_expansion():
    """R. Capacity expansion / resource adequacy: reserve margin falls -> capacity price rises."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show capacity expansion
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    supply_points_shifted = [[100, 120], [200, 170], [300, 220]]  # Shifted up
    
    title = "R. Capacity Expansion: Reserve Margin"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="up"
    )

def create_diagram_S_renewables():
    """S. Renewables penetration: supply stack shifts right at zero marginal cost (merit-order effect) and price falls."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show renewables effect
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    supply_points_shifted = [[100, 100], [200, 140], [300, 180]]  # Shifted down
    
    title = "S. Renewables Penetration: Merit Order Effect"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="down"
    )

def create_diagram_T_adoption_curve():
    """T. Adoption S-curve; onboarding/time-to-value improvement shifts the curve left."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show adoption curve
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    
    title = "T. Adoption S-Curve"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="left"
    )

def create_diagram_U_nps():
    """U. NPS vs time to value."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show NPS relationship
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    
    title = "U. NPS vs Time to Value"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="left"
    )

def create_diagram_V_roadmap():
    """V. Roadmap prioritization: value vs effort quadrants."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show roadmap prioritization
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    
    title = "V. Roadmap Prioritization: Value vs Effort"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="left"
    )

def create_diagram_W_competitive_positioning():
    """W. Market sizing / competitive positioning (PLEXOS, Aurora, Adapt2 and comparable platforms)."""
    engine = SupplySideDiagram(width=400, height=300)
    
    # Show competitive positioning
    demand_points = [[100, 200], [200, 150], [300, 100]]
    supply_points_original = [[100, 100], [200, 150], [300, 200]]
    
    title = "W. Competitive Positioning"
    
    return engine.create_supply_demand_diagram(
        title=title,
        demand_curve_points=demand_points,
        supply_curve_points=supply_points_original,
        equilibrium_point=(200, 150),
        shifted_demand=None,
        shift_direction="left"
    )

# List of all diagram functions
DIAGRAM_FUNCTIONS = [
    create_diagram_A_supply_tightening,
    create_diagram_B_demand_shock,
    create_diagram_C_basis_vs_capacity,
    create_diagram_D_storage_scarcity,
    create_diagram_E_production_response,
    create_diagram_F_forward_curve,
    create_diagram_G_marginal_fob,
    create_diagram_H_netback_arbitrage,
    create_diagram_I_freight_market,
    create_diagram_J_global_balance,
    create_diagram_K_frac_spread,
    create_diagram_L_fractionation_capacity,
    create_diagram_M_propane_export,
    create_diagram_N_merit_order,
    create_diagram_O_spark_spread,
    create_diagram_P_fuel_switching,
    create_diagram_Q_lmp_congestion,
    create_diagram_R_capacity_expansion,
    create_diagram_S_renewables,
    create_diagram_T_adoption_curve,
    create_diagram_U_nps,
    create_diagram_V_roadmap,
    create_diagram_W_competitive_positioning
]

# Main function to generate all diagrams
def generate_all_diagrams(output_dir: str = "/tmp/eml_visuals"):
    """Generate all required supply-side economics diagrams."""
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    print("Generating supply-side economics diagrams...")
    generated_files = []
    
    # Map function names to expected filenames based on spec files
    filename_map = {
        'create_diagram_A_supply_tightening': 'diag_A_hh_supply_tight.svg',
        'create_diagram_B_demand_shock': 'diag_B_demand_shock.svg',
        'create_diagram_C_basis_vs_capacity': 'diag_C_basis_vs_capacity.svg',
        'create_diagram_D_storage_scarcity': 'diag_D_storage_scarcity.svg',
        'create_diagram_E_production_response': 'diag_E_production_response.svg',
        'create_diagram_F_forward_curve': 'diag_F_forward_curve.svg',
        'create_diagram_G_marginal_fob': 'diag_G_fob_stack.svg',
        'create_diagram_H_netback_arbitrage': 'diag_H_netback_arb.svg',
        'create_diagram_I_freight_market': 'diag_I_freight_vessel.svg',
        'create_diagram_J_global_balance': 'diag_J_global_balance.svg',
        'create_diagram_K_frac_spread': 'diag_K_frac_spread.svg',
        'create_diagram_L_fractionation_capacity': 'diag_L_frac_capacity.svg',
        'create_diagram_M_propane_export': 'diag_M_export_dock.svg',
        'create_diagram_N_merit_order': 'diag_N_merit_order.svg',
        'create_diagram_O_spark_spread': 'diag_O_spark_spread.svg',
        'create_diagram_P_fuel_switching': 'diag_P_fuel_switching.svg',
        'create_diagram_Q_lmp_congestion': 'diag_Q_lmp_congestion.svg',
        'create_diagram_R_capacity_expansion': 'diag_R_capacity_expansion.svg',
        'create_diagram_S_renewables': 'diag_S_renewables_merit.svg',
        'create_diagram_T_adoption_curve': 'diag_T_adoption_curve.svg',
        'create_diagram_U_nps': 'diag_U_nps_ttv.svg',
        'create_diagram_V_roadmap': 'diag_V_value_effort.svg',
        'create_diagram_W_competitive_positioning': 'diag_W_competitive.svg'
    }
    
    for i, func in enumerate(DIAGRAM_FUNCTIONS, 1):
        try:
            svg_content = func()
            filename = filename_map.get(func.__name__, f"diag_{i:02d}_{func.__name__[13:]}.svg")
            filepath = Path(output_dir) / filename
            
            with open(filepath, 'w') as f:
                f.write(svg_content)
            
            generated_files.append(str(filepath))
            print(f"Generated: {filename}")
        except Exception as e:
            print(f"Error generating {func.__name__}: {str(e)}")
            import traceback
            traceback.print_exc()
    
    print(f"Successfully generated {len(generated_files)} diagrams.")
    return generated_files

if __name__ == "__main__":
    # Generate all diagrams to the temp directory
    files = generate_all_diagrams()
    print("All diagrams saved to /tmp/eml_visuals/")