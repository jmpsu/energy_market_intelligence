"""EX-086 Risk attribution engine: explain a day's P&L by factor (price, basis, volatility, time, volume) and report the unexplained residual."""
from common import *
def run(actual_pnl_USD=27500.0, unexplained_threshold_pct=10.0):
    d = data("ex086_factor_sensitivities.csv", """factor,bucket,sensitivity,sensitivity_unit,factor_move
    henry_hub_delta,price,500000,USD_per_1.00_USD_per_MMBtu,0.10
    waha_basis_delta,basis,200000,USD_per_1.00_USD_per_MMBtu,-0.15
    pjm_power_delta,price,20000,USD_per_1.00_USD_per_MWh,2.00
    gas_option_vega,volatility,15000,USD_per_vol_point,-2.00
    option_theta,time,-1200,USD_per_day,1.00
    volume_variance,volume,0.50,USD_margin_per_MMBtu,-5000""")
    d["pnl_USD"] = d.sensitivity * d.factor_move; b = d.groupby("bucket", as_index=False).pnl_USD.sum(); explained = float(d.pnl_USD.sum()); un = actual_pnl_USD - explained
    r = {f"{x.bucket}_pnl_USD": x.pnl_USD for x in b.itertuples()} | {"explained_pnl_USD": explained, "actual_pnl_USD": actual_pnl_USD, "unexplained_USD": un, "unexplained_pct_of_actual": abs(un) / abs(actual_pnl_USD) * 100, "within_threshold": bool(abs(un) / abs(actual_pnl_USD) * 100 <= unexplained_threshold_pct),
         "largest_factor": d.loc[d.pnl_USD.abs().idxmax(), "factor"], "gross_factor_pnl_USD": float(d.pnl_USD.abs().sum())}
    return finish("ex086", r, {"factor_pnl": d, "bucket_pnl": b}, ["First-order (delta, vega, theta) explain: the residual holds gamma, cross effects, new deals and data errors. A small net P&L can hide large offsetting factor P&Ls (gross 151,700)."])
if __name__ == "__main__": run()
