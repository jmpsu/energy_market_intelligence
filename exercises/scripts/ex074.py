"""EX-074 Physical gas scheduling: connect purchases, a transport contract with fuel retention, nominations and sales; find the delivery shortfall."""
from common import *
def run(supply_MMBtu=60000.0, sales_MMBtu=55000.0, mdq_receipt_MMBtu=50000.0, fuel_pct=2.0, receipt_price=3.00, delivery_price=3.60):
    f = fuel_pct / 100; need_receipt = sales_MMBtu / (1 - f); nom_receipt = min(supply_MMBtu, mdq_receipt_MMBtu, need_receipt); delivered = nom_receipt * (1 - f); short = sales_MMBtu - delivered; excess = supply_MMBtu - nom_receipt
    t = pd.DataFrame({"step": ["supply_purchased", "receipt_needed_for_sales", "transport_MDQ", "receipt_nominated", "fuel_retained", "delivered", "sales_obligation", "delivery_shortfall", "excess_supply_at_receipt"],
                      "MMBtu": [supply_MMBtu, need_receipt, mdq_receipt_MMBtu, nom_receipt, nom_receipt * f, delivered, sales_MMBtu, short, excess]})
    r = {"receipt_needed_MMBtu": need_receipt, "receipt_nominated_MMBtu": nom_receipt, "fuel_retained_MMBtu": nom_receipt * f, "delivered_MMBtu": delivered, "delivery_shortfall_MMBtu": short, "excess_supply_MMBtu": excess, "binding_constraint": "transport_MDQ" if nom_receipt == mdq_receipt_MMBtu else "supply" if nom_receipt == supply_MMBtu else "sales",
         "cost_to_cover_shortfall_at_delivery_USD": short * delivery_price, "proceeds_from_excess_at_receipt_USD": excess * receipt_price, "locational_loss_USD": short * delivery_price - excess * receipt_price, "MDQ_needed_MMBtu": need_receipt}
    return finish("ex074", r, {"scheduling_chain": t}, ["Long 60,000 at the receipt point and short 55,000 at the delivery point is not a flat position: the transport contract limits how much of one can become the other."])
if __name__ == "__main__": run()
