"""EX-001 Map the North American energy system as a logical network from wellhead to end use."""
from common import *
import networkx as nx
def run():
    e = data("ex001_system_edges.csv", """
from_node,to_node,from_type,to_type,link
Gas_Basin,Gathering,production,gathering,gathering_line
Gathering,Processing_Plant,gathering,processing,gathering_line
Processing_Plant,Interstate_Pipeline,processing,gas_transmission,residue_gas
Processing_Plant,NGL_Pipeline,processing,ngl_transport,y_grade
NGL_Pipeline,Fractionator,ngl_transport,fractionation,y_grade
Fractionator,Petrochemical_Plant,fractionation,end_use,purity_products
Fractionator,Export_Dock,fractionation,export,purity_products
Interstate_Pipeline,Gas_Storage,gas_transmission,storage,injection
Gas_Storage,Interstate_Pipeline,storage,gas_transmission,withdrawal
Interstate_Pipeline,LNG_Terminal,gas_transmission,export,feed_gas
Interstate_Pipeline,Gas_Utility_LDC,gas_transmission,distribution,city_gate
Interstate_Pipeline,Gas_Power_Plant,gas_transmission,generation,fuel
Gas_Utility_LDC,Gas_Customers,distribution,end_use,retail_gas
Gas_Power_Plant,Transmission_Grid,generation,power_transmission,electricity
Wind_Solar,Transmission_Grid,generation,power_transmission,electricity
Battery,Transmission_Grid,storage,power_transmission,discharge
Transmission_Grid,Battery,power_transmission,storage,charge
Transmission_Grid,Electric_Utility,power_transmission,distribution,wholesale_power
Electric_Utility,Power_Customers,distribution,end_use,retail_power""")
    g = nx.from_pandas_edgelist(e, "from_node", "to_node", edge_attr="link", create_using=nx.DiGraph); path = nx.shortest_path(g, "Gas_Basin", "Power_Customers")
    types = pd.concat([e[["from_node", "from_type"]].set_axis(["node", "type"], axis=1), e[["to_node", "to_type"]].set_axis(["node", "type"], axis=1)]).drop_duplicates()
    reach = pd.DataFrame([{"node": n, "reachable_from_gas_basin": nx.has_path(g, "Gas_Basin", n), "in_degree": g.in_degree(n), "out_degree": g.out_degree(n)} for n in g]).merge(types, on="node")
    if not os.environ.get("EMI_SCENARIO"):
        plt.figure(figsize=(12, 7)); nx.draw(g, nx.spring_layout(g, seed=3), with_labels=True, node_size=1800, font_size=6, node_color="lightgrey"); plt.title("Logical energy system map (synthetic)"); (DONE / "ex001").mkdir(exist_ok=True); plt.savefig(DONE / "ex001/system_map.png", dpi=130); plt.close()
    r = {"nodes": g.number_of_nodes(), "links": g.number_of_edges(), "gas_to_power_customer_path": " > ".join(path), "path_handoffs": len(path) - 1, "most_connected_node": max(g, key=g.degree), "end_use_nodes": int((types.type == "end_use").sum()),
         "nodes_not_fed_by_gas": ",".join(reach.node[~reach.reachable_from_gas_basin]) or "none", "gas_power_coupling_node": "Gas_Power_Plant"}
    return finish("ex001", r, {"edges": e, "nodes": reach}, ["Logical map, not geographic; one node per asset class."])
if __name__ == "__main__": run()
