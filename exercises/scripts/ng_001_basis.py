"""NG-001 Basis and long-basis P&L. Basis = hub price - Henry Hub. Long-basis P&L = position x (basis_2 - basis_1)."""
from common import *
def run():
    d = load("ng_001_basis_prices.csv"); d["basis_USD_per_MMBtu"] = d.hub_price_USD_per_MMBtu - d.henry_hub_USD_per_MMBtu
    rows = []
    for loc, g in d.groupby("location", sort=False):
        g = g.sort_values("period"); b1, b2 = g.basis_USD_per_MMBtu.iloc[0], g.basis_USD_per_MMBtu.iloc[-1]
        rows.append({"location": loc, "basis_period_1_USD_per_MMBtu": round(b1, 4), "basis_period_2_USD_per_MMBtu": round(b2, 4),
                     "basis_movement_USD_per_MMBtu": round(b2 - b1, 4), "position_MMBtu": g.long_basis_position_MMBtu.iloc[0],
                     "long_basis_pnl_USD": round((b2 - b1) * g.long_basis_position_MMBtu.iloc[0], 2), "data_classification": "synthetic"})
    out = pd.DataFrame(rows); out.to_csv(DONE / "ng_001_basis.csv", index=False)
    text = f"ng_001_basis | {LABEL}\n" + out.to_string(index=False) + "\n"; (EXP / "ng_001_basis.txt").write_text(text); print(text, end=""); return out
if __name__ == "__main__": run()
