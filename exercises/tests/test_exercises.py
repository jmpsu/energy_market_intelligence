"""Expected-output tests. Expected numbers are hand-derived from the input data (formulas shown inline), not copied from script output."""
import contextlib, csv, io, sqlite3, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT / "exercises/scripts"))
import yaml
DONE, SYN = ROOT / "exercises/completed", ROOT / "data/synthetic"
def run(mod, **kw):
    with contextlib.redirect_stdout(io.StringIO()): return __import__(mod).run(**kw)
def rows(path):
    with open(path) as f: return list(csv.DictReader(f))
class Base(unittest.TestCase):
    def near(self, a, b, tol=1e-6): self.assertLessEqual(abs(a - b), tol, f"{a} != {b}")
class TestGas(Base):
    def test_010(self):
        r = run("ex010"); self.near(r["Appalachian_netback_USD_per_MMBtu"], 2.65 - 1.10 - 0.35 - 0.65); self.near(r["Permian_netback_USD_per_MMBtu"], 2.10 - 1.25 - 0.40 - 0.90)
        self.near(r["Haynesville_netback_USD_per_MMBtu"], 3.05 - 1.45 - 0.30 - 0.45); self.near(r["Permian_growth_pct"], (24.5 / 23.0 - 1) * 100); self.assertEqual(r["best_netback"], "Haynesville")
    def test_015(self):
        r = run("ex015"); self.near(r["total_unscheduled_MMBtu"], 5000 + 15000 + 25000 + 20000 + 10000); self.near(r["lost_transport_value_USD"], 75000 * (4.75 - 3.25 - 0.30))
        self.assertEqual(r["constrained_hours"], "3,4,5,6,7"); self.near(run("ex015", capacity_scale=2.0)["total_unscheduled_MMBtu"], 0); run("ex015")
    def test_020(self):
        r = run("ex020"); [self.near(r[f"Period_{i}_basis"], b) for i, b in enumerate([1.10 - 3.25, -0.40 - 3.25, -1.25 - 3.40, 0.25 - 3.10], 1)]
        [self.near(r[f"Period_{i}_surplus_Bcf_d"], s) for i, s in enumerate([0.5, 3.0, 4.5, 1.0], 1)]; self.assertLess(r["corr_surplus_basis"], 0); self.assertEqual(r["negative_price_periods"], 2)
    def test_023_071(self):
        r = run("ex023"); self.near(r["book_mtm_day1_USD"], 310000 * (3.60 - 3.40) - 280000 * (3.50 - 3.55) + 300000 * (3.10 - 3.00) - 310000 * (3.85 - 3.70)); self.near(r["calendar_strip_USD_per_MMBtu"], 39.0 / 12)
        p = run("ex071"); self.near(p["price_pnl_USD"], 310000 * 0.10 - 280000 * 0.10 + 300000 * -0.05 - 310000 * -0.05); self.near(p["new_deal_pnl_USD"], 150000 * (3.30 - 3.25))
        self.near(p["daily_pnl_USD"], 11000); self.near(p["unexplained_USD"], 0); self.near(p["mtm_day2_USD"] - p["mtm_day1_USD"], p["daily_pnl_USD"])
    def test_025(self):
        r = run("ex025"); buy = (20000 * (2.80 + 2.60 + 2.70 + 2.90) + 10000 * 3.20) / 0.98; sell = 0.99 * (20000 * (5.20 + 4.10 + 4.70 + 5.50) + 10000 * 3.80)
        self.near(r["net_margin_USD"], sell - buy - 90000 * 0.08 - 90000 * 0.06, 1e-4); self.assertTrue(r["all_months_within_limits"]); self.assertGreaterEqual(r["lp_optimal_net_margin_USD"], r["net_margin_USD"] - 1e-6)
        s = rows(DONE / "ex025/storage_schedule.csv"); inv = [float(x["optimal_inventory_MMBtu"]) for x in s]; self.assertTrue(all(-1e-6 <= v <= 150000 + 1e-6 for v in inv)); self.near(inv[-1], 80000, 1e-3)
        self.assertTrue(all(float(x["optimal_injection_MMBtu"]) <= float(x["injection_capacity_MMBtu"]) + 1e-6 and float(x["optimal_withdrawal_MMBtu"]) <= float(x["withdrawal_capacity_MMBtu"]) + 1e-6 for x in s))
    def test_030(self):
        r = run("ex030"); self.near(r["total_penalty_USD"], 5 * ((7000 - 2000) + (6000 - 1600) + (5000 - 1200) + (5000 - 1800))); self.near(r["Beta_imbalance_MMBtu"], 76000 - 82000)
        self.near(sum(float(x["allocated_capacity_MMBtu"]) for x in rows(DONE / "ex030/ofo_compliance.csv")), 320000, 1e-4)
    def test_033(self):
        r = run("ex033"); cost = 1.15 * 3.25 + 2.50; self.near(r["Europe_margin_USD_per_MMBtu"], 11.00 - 0.40 - 0.90 - cost); self.near(r["Asia_margin_USD_per_MMBtu"], 12.50 - 0.40 - 1.90 - cost)
        self.near(run("ex033", hh=r["Europe_breakeven_HH"])["Europe_margin_USD_per_MMBtu"], 0); run("ex033")
    def test_035(self):
        r = run("ex035"); self.near(r["United_States_residual_Bcf_d"], 108 + 8 + 2 - 82 - 25 - 3); self.near(r["Canada_residual_Bcf_d"], 18 + 2 + 0.2 - 10.5 - 8 - 0.5); self.near(r["United_States_export_break_Bcf_d"], 25 - (5 + 25))
        self.assertEqual(r["countries_fully_reconciled"], "Mexico")
    def test_075(self):
        r = run("ex075"); self.near(r["total_mtm_USD"], 100000 * 0.05 + 80000 * (-0.40 - 1.10) - 60000 * (10.25 - 8.50) - 50000 * (3.10 - 2.80) + 40000 * 0.10); self.assertEqual(r["exception_trades"], "T001,T002,T003,T004")
    def test_090(self):
        r = run("ex090"); self.near(r["base_transport_cost_USD_per_d"], (15 * .25 + 10 * .30 + 20 * .35 + 5 * .20 + 10 * .50) * 1e6, 1); self.near(r["base_unmet_Bcf_d"], 15 - 10); self.assertGreaterEqual(r["disrupted_transport_cost_USD_per_d"], r["base_transport_cost_USD_per_d"] - 1)
        f = rows(DONE / "ex090/flow_comparison.csv"); self.assertTrue(all(float(x["flow_Bcf_d_base"]) <= float(x["capacity_Bcf_d_base"]) + 1e-9 and float(x["flow_Bcf_d_disrupted"]) <= float(x["capacity_Bcf_d_disrupted"]) + 1e-9 for x in f))
        sto = sum(float(x["flow_Bcf_d_base"]) * ((x["to_node"] == "STORAGE_A") - (x["from_node"] == "STORAGE_A")) for x in f); self.near(sto, 0)
class TestNglPower(Base):
    def test_039_040(self):
        r = run("ex040"); self.near(r["2026-01-12_Propane_profit_USD"], (0.750 - 0.660 - 0.045 - 0.012) * 1e6); self.near(r["2026-01-05_Ethane_profit_USD"], (0.235 - 0.205 - 0.057) * 1e6); self.assertEqual(r["products_never_positive"], "Ethane")
        v = 42 * (0.40 * 0.235 + 0.28 * 0.720 + 0.11 * 0.890 + 0.07 * 1.020 + 0.14 * 1.450); g = run("ex039"); self.near(g["purity_value_USD_per_barrel"], v); self.near(g["frac_margin_USD_per_barrel"], v - 42 * (0.55 + 0.07))
    def test_045(self):
        r = run("ex045"); self.assertEqual((r["highest_rt_price_market"], r["largest_rt_minus_da_market"], r["markets"]), ("ISO_NE", "ERCOT", 7)); self.near(r["largest_rt_minus_da_USD_per_MWh"], 44 - 37)
        con = sqlite3.connect(ROOT / "data/processed/power_markets.sqlite"); self.assertEqual(con.execute("SELECT COUNT(*) FROM market_reference r JOIN market_activity a USING(market)").fetchone()[0], 7); con.close()
    def test_048(self):
        r = run("ex048"); self.near(r["constrained_lmp_A"], 30); self.near(r["constrained_lmp_B"], 60); self.near(r["constrained_congestion_rent_USD_per_h"], 250 * 30); self.near(r["constrained_cost_USD_per_h"], 350 * 30 + 150 * 60)
        self.near(r["constrained_load_payment_USD_per_h"] - r["constrained_generator_revenue_USD_per_h"], r["constrained_congestion_rent_USD_per_h"]); self.near(run("ex048", limit=400)["constrained_congestion_component_B"], 0); run("ex048")
    def test_055(self):
        r = run("ex055"); self.near(r["hour_8_spark_USD_per_MWh"], 35 - 7 * 4.5 - 3); self.near(r["total_gross_margin_USD"], 100 * sum(p - 7 * g - 3 for p, g in [(45, 3), (55, 3.25), (65, 3.5), (75, 3.75), (40, 4), (90, 5), (120, 6), (35, 4.5)]))
        self.assertEqual(run("ex055", gas_shift=1.0)["profitable_hours"], 7); run("ex055")
    def test_060(self):
        r = run("ex060"); self.near(r["Baseline_price_USD_per_MWh"], 48); self.near(r["Outage_price_USD_per_MWh"], 65); self.near(r["Baseline_reserve_margin_pct"], (6700 - 5500) / 5500 * 100); self.near(r["Outage_reserve_margin_pct"], 0); self.near(r["Outage_unmet_MW"], 0)
        self.near(r["Baseline_production_cost_USD_per_h"], 800 * 12 + 1500 * 35 + 1200 * 42 + 800 * 48)
    def test_065(self):
        r = run("ex065"); d = rows(DONE / "ex065/hourly_dispatch.csv"); direct = sum(float(x["solar_generation_MW"]) * float(x["electricity_price_USD_per_MWh"]) for x in rows(SYN / "renewable_storage_dispatch.csv"))
        self.near(r["direct_solar_revenue_USD"], direct); self.assertGreaterEqual(r["solar_plus_storage_revenue_USD"], direct); soc = 50.0
        for x in d:
            c, dis, s, sol = (float(x[k]) for k in ("charge_MW", "discharge_MW", "soc_MWh", "solar_generation_MW")); soc += 0.9 * c - dis
            self.near(s, soc, 1e-4); self.assertTrue(-1e-6 <= c <= min(50, sol) + 1e-6 and -1e-6 <= dis <= 50 + 1e-6 and 10 - 1e-6 <= s <= 200 + 1e-6)
        self.assertGreaterEqual(soc, 50 - 1e-4); self.near(run("ex065")["solar_plus_storage_revenue_USD"], r["solar_plus_storage_revenue_USD"]); self.near(run("ex065", rte=1.0)["energy_charged_MWh"], run("ex065", rte=1.0)["energy_discharged_MWh"], 1e-4); run("ex065")
class TestSystemsQuantProduct(Base):
    def test_070(self):
        r = run("ex070"); self.assertEqual((r["raw_rows"], r["rejected_rows"], r["duplicate_rows_superseded"], r["curated_rows"], r["negative_prices_preserved"]), (10, 2, 2, 6, 1)); self.near(r["completeness_pct"], 6 / 7 * 100)
        con = sqlite3.connect(ROOT / "data/processed/market_data.sqlite"); self.assertEqual(con.execute("SELECT COUNT(*) FROM curated_prices WHERE price IS NULL OR provider<>'Provider_A'").fetchone()[0], 0)
        self.near(con.execute("SELECT price FROM curated_prices WHERE location='Waha' AND timestamp LIKE '%T10:00%'").fetchone()[0], -0.40); con.close()
    def test_077(self):
        r = run("ex077"); d = rows(SYN / "ex077_hh_daily_synthetic.csv"); p = [float(x["henry_hub_USD_per_MMBtu"]) for x in d]; e = [p[i] - p[i - 1] for i in range(301, 400)]
        self.near(r["naive_rmse"], (sum(v * v for v in e) / len(e)) ** 0.5, 1e-9); self.assertEqual(r["train_rows"] + r["test_rows"], 399); self.near(run("ex077")["model_rmse"], r["model_rmse"], 1e-12)
    def test_080(self):
        r = run("ex080"); self.near(r["terminal_mean"], r["analytic_mean"], 0.03); self.assertTrue(r["es95_USD"] >= r["var95_USD"] > 0 and r["es99_USD"] >= r["var99_USD"] >= r["var95_USD"] and r["min_simulated_price"] > 0)
        self.near(run("ex080")["var95_USD"], r["var95_USD"], 1e-9); self.assertEqual(len(rows(DONE / "ex080/terminal_distribution.csv")), 10000)
    def test_085(self):
        r = run("ex085"); hdd = sum(max(0, 65 - t) for t in [35, 38, 42, 28, 31, 45, 40, 33, 29, 36, 41, 44, 30, 34, 39]); self.near(r["cumulative_HDD"], hdd); self.near(r["payout_USD"], (450 - hdd) * 10000)
        self.near(r["payout_shift_+15F_USD"], 2_000_000); self.near(r["payout_shift_-5F_USD"], 0); self.near(r["payout_shift_+3F_USD"], (450 - (hdd - 45)) * 10000); self.assertEqual(r["hdd_rows_verified"], 15)
    def test_092(self):
        r = run("ex092"); self.assertTrue(r["results_equivalent"] and r["constraints_satisfied"]); self.assertLess(r["max_relative_objective_difference"], 1e-6)
    def test_095(self):
        r = run("ex095"); self.assertTrue(r["rank_1"].startswith("Automated_basis_monitoring") and r["rank_2"].startswith("Unified_risk_dashboard") and r["rank_5"].startswith("Simulation_performance"))
        self.near(float(r["rank_2"].split("=")[1]), 650000 / 16 * (6 - 3) / 5, 0.1); self.assertEqual((ROOT / "product_management/requirements/ex095_requirements.md").read_text().count("## REQ-"), 5)
    def test_100(self):
        r = run("ex100"); px = [35, 32, 30, 28, 25, 30, 40, 55, 65, 70, 68, 60, 55, 58, 75, 95, 125, 150, 115, 85, 65, 50, 42, 38]; ren = [40, 45, 50, 55, 70, 100, 140, 190, 215, 225, 225, 210, 190, 160, 125, 80, 45, 25, 20, 25, 30, 35, 40, 45]
        self.near(r["base_gas_book_value_USD"], 100000 * 3.25 + 80000 * -0.40 + 60000 * 10.25 + 50000 * 2.15); self.near(r["base_gas_unit_margin_USD"], 500 * sum(max(p - 7.2 * 3.25 - 3, 0) for p in px), 1e-4)
        self.near(r["base_renewable_revenue_USD"], sum(p * q for p, q in zip(px, ren))); self.assertGreater(r["base_battery_margin_USD"], 0)
        t = {x["scenario"]: x for x in rows(DONE / "ex100/scenario_valuation.csv")}; self.assertEqual(len(t), 6); self.near(float(t["Pipeline_Disruption"]["fuel_burn_MMBtu"]) / max(float(t["Pipeline_Disruption"]["gas_unit_run_hours"]), 1), 500 * 0.6 * 7.2, 1e-6)
class TestRepository(Base):
    def test_curriculum_architecture(self):
        m = yaml.safe_load((ROOT / "curriculum/curriculum_master.yaml").read_text())["chapters"]; ids = [l for c in m for s in c["sections"] for l in s["lessons"]]
        self.assertEqual((len(m), sum(len(c["sections"]) for c in m), len(ids), len(set(ids))), (12, 120, 600, 600)); e = yaml.safe_load((ROOT / "curriculum/exercise_delivery_sequence.yaml").read_text())["exercises"]; self.assertEqual(len({x["id"] for x in e}), 100)
        self.assertEqual(len(list((ROOT / "curriculum/chapters").glob("chapter_*/sections/section_*/lessons.yaml"))), 120)
    def test_artifacts_and_labels(self):
        for x in yaml.safe_load((ROOT / "curriculum/exercise_delivery_sequence.yaml").read_text())["exercises"]:
            n = x["id"][-3:]
            if x["status"] == "not_started" or n in ("003", "005", "021"): continue
            self.assertIn("SYNTHETIC", (ROOT / f"exercises/expected_output/ex{n}.txt").read_text(), n); self.assertTrue((DONE / f"ex{n}/report.md").exists(), n)
        self.assertTrue((ROOT / "exercises/labs/exercise-003/outputs/mass_balance_checks.csv").exists() and (ROOT / "exercises/labs/exercise-005/outputs/interconnection_network.png").exists())
if __name__ == "__main__": unittest.main()
