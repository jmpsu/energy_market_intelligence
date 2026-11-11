"""EX-019 Regional gas basis: each hub versus Henry Hub, ranked and classified."""
from common import *
def run():
    d = data("ex019_hub_prices.csv", "hub,region,price_day1,price_day2\nHenry_Hub,Gulf,3.25,3.25\nWaha,Permian,1.10,-0.40\nAECO,Alberta,2.15,2.05\nDawn,Ontario,2.80,3.10\nChicago,Midwest,3.10,3.30\nAlgonquin,New_England,8.75,10.25\nSoCal,California,3.95,4.40")
    hh = d.set_index("hub").loc["Henry_Hub"]; d["basis_day1"] = d.price_day1 - hh.price_day1; d["basis_day2"] = d.price_day2 - hh.price_day2; d["basis_change"] = d.basis_day2 - d.basis_day1
    d["type"] = np.select([d.hub == "Henry_Hub", d.basis_day1 < -0.05, d.basis_day1 > 0.05], ["benchmark", "supply_area_discount", "market_area_premium"], "near_flat"); d = d.sort_values("basis_day1").reset_index(drop=True)
    r = {f"{x.hub}_basis_day1": x.basis_day1 for x in d.itertuples()} | {"widest_discount": d.hub.iloc[0], "widest_premium": d.hub.iloc[-1], "largest_basis_move_hub": d.loc[d.basis_change.abs().idxmax(), "hub"], "largest_basis_move": float(d.basis_change[d.basis_change.abs().idxmax()]), "max_spread_between_hubs_day2": float(d.price_day2.max() - d.price_day2.min()), "negative_priced_hubs_day2": ",".join(d.hub[d.price_day2 < 0])}
    return finish("ex019", r, {"basis_table": d}, ["Synthetic prices (Waha and Algonquin match NG-001). Henry Hub flat both days: every price move here is basis."])
if __name__ == "__main__": run()
