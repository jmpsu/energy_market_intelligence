"""Expected-output tests for the NGL exercises (037-044) and tier 1 exercises 047, 056, 063, 081, 082, 084, 094. Expected values are hand-derived inline."""
import csv, math, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT / "exercises/tests"))
from test_exercises import Base, run, rows, DONE, SYN
GPM = {"C2": 10.5 * 0.2669, "C3": 5.0 * 0.2749, "iC4": 0.7 * 0.3265, "nC4": 1.5 * 0.3146, "C5": 1.3 * 0.3650}
class TestNGL(Base):
    def test_037(self):
        r = run("ex037"); gal = 200000 * (GPM["C2"] * 0.85 + GPM["C3"] * 0.98 + GPM["iC4"] * 0.99 + GPM["nC4"] * 0.99 + GPM["C5"] * 1.0); self.near(r["theoretical_gpm"], sum(GPM.values())); self.near(r["ngl_gal_per_d"], gal, 1e-3); self.near(r["ngl_bbl_per_d"], gal / 42, 1e-4)
        shr = 200000 * (GPM["C2"] * 0.85 * 0.0665 + GPM["C3"] * 0.98 * 0.0915 + GPM["iC4"] * 0.99 * 0.0996 + GPM["nC4"] * 0.99 * 0.1037 + GPM["C5"] * 0.1100); self.near(r["shrink_MMBtu_per_d"], shr, 1e-3)
        val = 200000 * (GPM["C2"] * 0.85 * 0.235 + GPM["C3"] * 0.98 * 0.720 + GPM["iC4"] * 0.99 * 1.020 + GPM["nC4"] * 0.99 * 0.890 + GPM["C5"] * 1.450); self.near(r["frac_spread_USD_per_MMBtu"], val / shr - 3.25, 1e-6)
        self.assertLess(run("ex037", mode="reject")["ngl_bbl_per_d"], r["ngl_bbl_per_d"]); run("ex037")
    def test_038(self):
        r = run("ex038"); swing, lost = 200000 * GPM["C2"] * (0.85 - 0.10), 200000 * GPM["C3"] * (0.98 - 0.90); adv = swing * (0.0665 * 3.25 - (0.235 - 0.08)) - lost * (0.720 - 0.08 - 0.0915 * 3.25)
        self.near(r["rejection_advantage_USD_per_d"], adv, 1e-3); self.assertEqual(r["decision"], "REJECT"); self.near(r["simple_breakeven_ethane_USD_per_gal"], 0.0665 * 3.25 + 0.08); self.assertLess(r["plant_breakeven_ethane_USD_per_gal"], r["simple_breakeven_ethane_USD_per_gal"])
        self.assertEqual(run("ex038", ethane_price=0.30)["decision"], "RECOVER"); self.near(run("ex038", ethane_price=r["plant_breakeven_ethane_USD_per_gal"])["rejection_advantage_USD_per_d"], 0, 1e-3)
        self.near(run("ex038", gas_price=r["gas_price_where_decision_flips"])["rejection_advantage_USD_per_d"], 0, 1e-3); self.near(r["gas_price_where_decision_flips"], (0.155 + lost * 0.64 / swing) / (0.0665 + lost * 0.0915 / swing), 1e-6); run("ex038")
    def test_041(self):
        r = run("ex041"); inv = cold = 45.0; path, cpath = [], []
        for x in rows(SYN / "ex041_propane_balance.csv"):
            p, d, e, n = float(x["production_MMb_d"]), float(x["domestic_demand_MMb_d"]), float(x["exports_MMb_d"]), int(x["days"]); inv += (p - d - e) * n; cold += (p - d * (1.2 if x["month"] in ("Dec", "Jan", "Feb") else 1) - e) * n; path.append(inv); cpath.append(cold)
        self.near(r["peak_inventory_MMbbl"], max(path)); self.near(r["base_ending_inventory_MMbbl"], path[-1]); self.near(r["cold_winter_min_inventory_MMbbl"], min(cpath)); self.assertEqual(r["cold_winter_months_below_minimum"], "Feb,Mar")
        self.assertEqual(run("ex041", winter_demand_mult=1.0)["cold_winter_months_below_minimum"], "none"); run("ex041")
    def test_042(self):
        r = run("ex042"); cost = 23.5 / 2.97 / 0.78; self.near(r["Ethane_feed_cost_c_per_lb_ethylene"], cost); self.near(r["Ethane_margin_c_per_lb_ethylene"], 22.0 - (cost - 1.0 + 4.0)); self.near(r["Propane_margin_c_per_lb_ethylene"], 22.0 - (72.0 / 4.22 / 0.42 - 20.0 + 5.0))
        self.near(run("ex042", ethane_price=r["Ethane_breakeven_feed_price_USD_per_gal"])["Ethane_margin_c_per_lb_ethylene"], 0); run("ex042")
    def test_043(self):
        r = run("ex043"); self.near(r["base_total_cost_USD"], 25000 * 1.5 + 45000 * 1.9 + 5000 * 3.2 + 10000 * 4.0 + 15000 * 4.5, 1e-3); self.assertGreaterEqual(r["outage_total_cost_USD"], r["base_total_cost_USD"])
        p = rows(DONE / "ex043/shipment_plan.csv"); self.assertTrue(all(float(x["shipped_bbl_base"]) <= float(x["capacity_bbl_base"]) + 1e-6 and float(x["shipped_bbl_outage"]) <= float(x["capacity_bbl_outage"]) + 1e-6 for x in p))
        for k in ("base", "outage"): self.near(sum(float(x[f"shipped_bbl_{k}"]) for x in p if x["destination"] == "Mont_Belvieu"), 70000, 1e-3); self.near(sum(float(x[f"shipped_bbl_{k}"]) for x in p if x["origin"] == "Conway"), 60000, 1e-3)
        self.near(run("ex043", outage_frac=0.0)["outage_cost_increase_USD"], 0, 1e-3); run("ex043")
    def test_044(self):
        r = run("ex044"); self.near(r["mtm_day1_USD"], 2e6 * .020 - 1.5e6 * .005 - 3e6 * .005 + .5e6 * .010 - .8e6 * .005 + .4e6 * .020); self.near(r["weekly_pnl_USD"], 2e6 * .030 - 1.5e6 * .005 + 3e6 * .010 - .5e6 * .030 + .8e6 * .015 + .4e6 * .030)
        self.near(r["propane_flat_price_pnl_USD"] + r["propane_basis_pnl_USD"], r["propane_total_pnl_USD"]); self.near(r["propane_basis_pnl_USD"], 2e6 * ((0.750 - 0.660) - (0.720 - 0.655))); self.near(r["net_position_bbl"], 4.2e6 / 42)
class TestTier1Remaining(Base):
    def test_047(self):
        r = run("ex047"); d = rows(SYN / "ex047_da_rt.csv"); da = [float(x["da_price_USD_per_MWh"]) for x in d]; rt = [float(x["rt_price_USD_per_MWh"]) for x in d]
        self.near(r["da_revenue_USD"], 300 * sum(da)); self.near(r["rt_settlement_USD"], -100 * (rt[16] + rt[17])); self.near(r["two_settlement_revenue_USD"], 300 * sum(da) - 100 * (rt[16] + rt[17])); self.near(r["virtual_inc_pnl_USD"], 50 * (sum(da) - sum(rt)))
        self.assertGreater(r["outage_buyback_cost_USD"], r["da_revenue_lost_equivalent_USD"])
    def test_056(self):
        r = run("ex056"); self.near(r["lmp_bus_1"], 20); self.near(r["lmp_bus_2"], 50); self.near(r["lmp_bus_3"], -20 + 2 * 50); self.near(r["gen_bus_1_MW"], 150); self.near(r["dispatch_cost_USD_per_h"], 150 * 20 + 150 * 50)
        self.near(r["congestion_rent_USD_per_h"], 300 * 80 - 150 * 20 - 150 * 50); self.near(r["ftr_payout_USD_per_h"], 100 * (80 - 20) + 50 * (80 - 50)); self.near(abs(r["flow_L13_MW"]), 150)
        pt = {x["line"]: x for x in rows(DONE / "ex056/ptdf.csv")}; self.near(float(pt["L13"]["bus_1"]), 2 / 3, 1e-5); self.near(float(pt["L13"]["bus_2"]), 1 / 3, 1e-5); u = run("ex056", l13_limit=1000); self.near(u["lmp_bus_3"], 20); self.near(u["congestion_rent_USD_per_h"], 0); run("ex056")
    def test_063(self):
        r = run("ex063"); rule = 50 * 0.9 * (135 + 120 + 110) - 50 * (15 + 18 + 18); self.near(r["rule_of_thumb_revenue_USD"], rule); self.assertGreaterEqual(r["lp_revenue_USD"], rule); soc = 50.0; rev = 0.0
        for x in rows(DONE / "ex063/battery_dispatch.csv"):
            c, d, s, p = (float(x[k]) for k in ("charge_MW", "discharge_MW", "soc_MWh", "electricity_price_USD_per_MWh")); soc += 0.9 * c - d; rev += (d - c) * p; self.near(s, soc, 1e-4); self.assertTrue(-1e-6 <= c <= 50 + 1e-6 and -1e-6 <= d <= 50 + 1e-6 and 10 - 1e-6 <= s <= 200 + 1e-6)
        self.near(rev, r["lp_revenue_USD"], 1e-2); self.assertGreaterEqual(soc, 50 - 1e-4)
    def test_081_082(self):
        r = run("ex081"); d = rows(SYN / "ex081_price_changes.csv"); pnl = [500000 * float(x["henry_hub_USD_per_MMBtu"]) - 200000 * float(x["waha_USD_per_MMBtu"]) + 20000 * float(x["pjm_west_USD_per_MWh"]) for x in d]
        m = sum(pnl) / len(pnl); sd = math.sqrt(sum((v - m) ** 2 for v in pnl) / (len(pnl) - 1)); self.near(r["portfolio_daily_vol_USD"], sd, 1e-3); self.near(r["parametric_var95_USD"], 1.6448536269514722 * sd, 1e-2); self.near(r["parametric_var99_USD"], 2.3263478740408408 * sd, 1e-2)
        self.near(r["component_var_henry_hub_USD_per_MMBtu"] + r["component_var_waha_USD_per_MMBtu"] + r["component_var_pjm_west_USD_per_MWh"], r["parametric_var95_USD"], 1e-3); self.near(r["worst_day_loss_USD"], -min(pnl), 1e-3)
        s = sorted(pnl); self.assertTrue(-s[25] <= r["historical_var95_USD"] <= -s[24]); self.assertGreater(r["diversification_benefit_USD"], 0)
        e = run("ex082"); self.near(e["historical_es99_USD"], -sum(s[:5]) / 5, 1e-3); self.near(e["historical_es95_USD"], -sum(s[:25]) / 25, 1e-3); self.assertEqual((e["tail_observations_95"], e["tail_observations_99"]), (25, 5))
        z = 2.3263478740408408; self.near(e["normal_es99_USD"], sd * math.exp(-z * z / 2) / math.sqrt(2 * math.pi) / 0.01, 1e-2); self.assertTrue(e["historical_es99_USD"] >= e["historical_var99_USD"] and e["historical_es95_USD"] >= e["historical_var95_USD"])
    def test_084(self):
        r = run("ex084"); px = [35, 32, 30, 28, 25, 30, 40, 55, 65, 70, 68, 60, 55, 58, 75, 95, 125, 150, 115, 85, 65, 50, 42, 38]; gu = 500 * sum(max(.5 * p - 26.4, 0) - max(p - 26.4, 0) for p in px); ren = -0.5 * 141900
        self.assertLessEqual(r["Power_Collapse_change_USD"], gu + ren + 1e-6); self.assertGreaterEqual(r["Power_Collapse_change_USD"], gu + ren - 30401.48); self.assertEqual(r["scenarios_breaching_limit"], "Gas_Collapse,Mild_Winter,Power_Collapse"); self.near(r["Base_change_USD"], 0)
        t = {x["scenario"]: x for x in rows(DONE / "ex084/stress_results.csv")}; self.near(float(t["Mild_Winter"]["gas_book_value_change_USD"]), -0.3 * 1015500, 1e-3); self.assertEqual(run("ex084", limit=-1e9)["scenarios_breaching_limit"], "none"); run("ex084")
    def test_094(self):
        r = run("ex094"); self.assertTrue(r["energy_balance_all_hours"] and r["model_prices_are_stack_costs"] and not r["raw_model_passes"] and r["calibrated_model_passes"]); self.assertTrue(0.03 < r["calibrated_scarcity_adder_USD_per_MWh_per_MW"] < 0.07)
        self.assertLess(r["high_load_bias_raw"], -10); self.assertLess(abs(r["normal_load_bias_raw"]), 2); self.assertLess(r["validation_mae_calibrated"], r["validation_mae_raw"])
if __name__ == "__main__": unittest.main()
