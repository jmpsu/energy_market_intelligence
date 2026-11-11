"""EX-099 Conceptual integration architecture: components and interfaces as a graph, with every capability labelled demonstrated-here or proposed. No vendor product capability is asserted."""
from common import *
import networkx as nx
def run():
    c = data("ex099_components.csv", """component,layer,status,evidence
    Vendor_price_feeds,source,proposed,none
    Raw_staging,data,demonstrated_here,EX-070
    Curated_market_data,data,demonstrated_here,EX-070
    Reference_master_data,data,demonstrated_here,EX-007
    Warehouse,data,demonstrated_here,EX-087
    Market_data_API,service,demonstrated_here,EX-088
    Trade_store,data,demonstrated_here,EX-069
    Valuation_and_risk,analytics,demonstrated_here,EX-076
    Dispatch_and_network_simulation,simulation,demonstrated_here,EX-089
    Simulation_orchestrator,simulation,proposed,none
    External_simulation_engine,simulation,proposed,none
    Validation_service,analytics,demonstrated_here,EX-094
    User_workflows_and_reports,presentation,proposed,none""")
    e = data("ex099_interfaces.csv", """source,target,payload
    Vendor_price_feeds,Raw_staging,raw price files
    Raw_staging,Curated_market_data,validated prices
    Reference_master_data,Warehouse,locations and units
    Curated_market_data,Warehouse,price facts
    Warehouse,Market_data_API,query results
    Market_data_API,Valuation_and_risk,marks
    Trade_store,Valuation_and_risk,positions
    Market_data_API,Simulation_orchestrator,model inputs
    Simulation_orchestrator,Dispatch_and_network_simulation,scenario runs
    Simulation_orchestrator,External_simulation_engine,scenario runs
    Dispatch_and_network_simulation,Validation_service,model outputs
    External_simulation_engine,Validation_service,model outputs
    Validation_service,User_workflows_and_reports,validated results
    Valuation_and_risk,User_workflows_and_reports,risk reports""")
    g = nx.from_pandas_edgelist(e, "source", "target", create_using=nx.DiGraph); c["in_graph"] = c.component.isin(g.nodes); c["reaches_users"] = [n == "User_workflows_and_reports" or nx.has_path(g, n, "User_workflows_and_reports") for n in c.component]; st = c.set_index("component").status
    e["interface_status"] = np.where((e.source.map(st) == "demonstrated_here") & (e.target.map(st) == "demonstrated_here"), "demonstrated_here", "proposed")
    (ROOT / "product_management/architecture/ex099_architecture.md").write_text(f"# EX-099 conceptual integration architecture ({LABEL})\n\nNo capability of any commercial product is asserted. External_simulation_engine is a placeholder for a licensed engine; its interfaces are proposals to verify against vendor documentation.\n\n" + "\n".join(f"- {x.source} -> {x.target}: {x.payload} [{x.interface_status}]" for x in e.itertuples()) + "\n")
    r = {"components": len(c), "interfaces": len(e), "demonstrated_components": int((c.status == "demonstrated_here").sum()), "proposed_components": int((c.status == "proposed").sum()), "demonstrated_interfaces": int((e.interface_status == "demonstrated_here").sum()), "orphan_components": int((~c.in_graph).sum()),
         "components_not_reaching_users": ",".join(c.component[~c.reaches_users]) or "none", "is_acyclic": nx.is_directed_acyclic_graph(g), "vendor_capabilities_asserted": 0}
    return finish("ex099", r, {"components": c, "interfaces": e}, ["Verified vendor capability claims: none. Mapping any box to PLEXOS, Aurora, Adapt2 or another product requires that vendor's documentation, which this build has not read."])
if __name__ == "__main__": run()
