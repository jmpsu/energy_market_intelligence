"""Expected-output tests for the remaining 59 exercises and the four NGL extensions. Expected values are hand-derived inline (right-hand side of each row)."""
import math, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT / "exercises/tests"))
from test_exercises import Base, run, rows, DONE, SYN
from test_exercises_2 import GPM
SHRINK = 200000 * (GPM["C2"] * 0.85 * 0.0665 + GPM["C3"] * 0.98 * 0.0915 + GPM["iC4"] * 0.99 * 0.0996 + GPM["nC4"] * 0.99 * 0.1037 + GPM["C5"] * 0.1100)
NGLVAL = 200000 * (GPM["C2"] * 0.85 * 0.235 + GPM["C3"] * 0.98 * 0.720 + GPM["iC4"] * 0.99 * 1.020 + GPM["nC4"] * 0.99 * 0.890 + GPM["C5"] * 1.450)
PX = [35, 32, 30, 28, 25, 30, 40, 55, 65, 70, 68, 60, 55, 58, 75, 95, 125, 150, 115, 85, 65, 50, 42, 38]
NUM = [  # (exercise, result key, hand-derived expected value, tolerance)
 ("ex001", "nodes", 16, 0), ("ex001", "edges", 15, 0), ("ex001", "paths_Permian_to_Houston_Load", 2, 0), ("ex002", "participants", 12, 0), ("ex002", "rate_regulated", 5, 0),
 ("ex004", "delivered_MWh", 100000 / 7 * 0.975 * 0.98 * 0.96, 1e-6), ("ex004", "fuel_cost_USD_per_gross_MWh", 3.25 * 7, 1e-9), ("ex006", "retail_cost_USD_per_MWh", 45 * 1.05 + 8 + 2 + 55 + 6, 1e-9), ("ex006", "retail_increase_pct", 45 * 0.5 * 1.05 / 118.25 * 100, 1e-9),
 ("ex007", "natural_gas_locations", 5, 0), ("ex007", "ngl_locations", 2, 0), ("ex007", "CA_locations", 2, 0), ("ex007", "gas_distinct_units", 2, 0),
 ("ex008", "Producer_pnl_USD_per_d", 200000 * 0.5, 1e-9), ("ex008", "Generator_pnl_USD_per_d", -70000 * 0.7 * 0.4, 1e-9), ("ex008", "Utility_pnl_USD_per_d", 0, 1e-9), ("ex008", "Trader_pnl_USD_per_d", 20000, 1e-9),
 ("ex011", "total_growth_pct", (18.6 / 18.0 - 1) * 100, 1e-9), ("ex011", "Montney_share_2026_pct", 11.2 / 18.6 * 100, 1e-9), ("ex012", "realized_wellhead_USD_per_MMBtu", 3.25 * 0.97 - (0.25 + 0.20 + 0.45 + 0.03), 1e-9), ("ex012", "hub_price_for_zero_netback", 0.93 / 0.97, 1e-9),
 ("ex013", "residue_MMBtu_per_d", 200000 * 1.25 * 0.98 - SHRINK, 1e-3), ("ex014", "unsubscribed_firm_Bcf_d", 1.85 - 1.70, 1e-9), ("ex014", "utilization_of_operational_pct", 1.58 / 1.85 * 100, 1e-9), ("ex016", "breakeven_load_factor", 0.40 / (0.55 - 0.02), 1e-9), ("ex016", "firm_cost_at_50pct", 0.82, 1e-9),
 ("ex017", "outage_unmet_Bcf_d", 5 + (25 - (10 + 5 + 5)), 1e-6), ("ex017", "additional_unmet_Bcf_d", 5, 1e-6), ("ex018", "max_flow_to_LNG_Bcf_d", 6 + 1, 1e-9), ("ex018", "stranded_upstream_Bcf_d", 1, 1e-9), ("ex019", "Waha_basis", 1.10 - 3.25, 1e-9), ("ex019", "Algonquin_Citygate_basis", 8.75 - 3.25, 1e-9),
 ("ex022", "winter_minus_summer", (3.6 + 3.5 + 3.2 + 3.45 + 3.85) / 5 - (3.0 + 2.95 + 3.0 + 3.1 + 3.12 + 3.08 + 3.15) / 7, 1e-9), ("ex022", "Jan_minus_Jul", 0.5, 1e-9), ("ex024", "physical_index_plus_swap_pay_fixed", 3.30, 1e-9), ("ex024", "waha_index_plus_HH_swap_only", 3.60 - 0.60 - 0.30, 1e-9),
 ("ex024", "waha_index_plus_HH_swap_plus_basis_swap", 3.30 - 0.40, 1e-9), ("ex026", "combined_change", -0.30 * 1.5 + 0.25 * 2 + 0.02 * 10 - 0.0015 * 150, 1e-9), ("ex027", "flat_price_pnl_USD", 130000 * 0.20, 1e-6), ("ex027", "total_pnl_USD", 26000 - 40000 - 60000 + 2500 + 2000, 1e-6),
 ("ex028", "Gamma_scheduled_MMBtu", 100000 - 40000 - 25000, 1e-6), ("ex028", "confirmation_cuts", 5000, 1e-6), ("ex029", "X_cashout_USD", 2000 * 3.25 + 1000 * 3.25 * 1.2, 1e-6), ("ex029", "Y_cashout_USD", -1000 * 3.25, 1e-6), ("ex029", "Z_cashout_USD", -(1750 * 3.25 + 2250 * 3.25 * 0.8), 1e-6),
 ("ex031", "total_withdrawn_MMcf", 5 * 200 + 21 * 120 + 4 * 60, 0), ("ex031", "ending_inventory_MMcf", 6000 - 3760, 0), ("ex032", "total_feedgas_Bcf_d", (2.4 * 0.9 + 4.5 * 0.95 + 2.1 * 0.6) * 1.1, 1e-9), ("ex032", "outage_feedgas_lost_Bcf_d", 4.5 * 0.95 * 1.1, 1e-9),
 ("ex034", "mean_ttf_minus_hh", (125.6 - 39.2) / 12, 1e-9), ("ex034", "months_asia_preferred", 6, 0), ("ex036", "total_unmet_Bcf", 5 + 14 + 17 + 8 + 6, 1e-9), ("ex036", "first_unmet_day", 3, 0), ("ex036", "storage_withdrawn_Bcf", 60, 1e-9),
 ("ex046", "bilateral_physical_with_wheeling_buyer", (45 + 4) / 0.97, 1e-9), ("ex046", "iso_plus_cfd_at_gen_node_buyer", 48 + 3, 1e-9), ("ex049", "clearing_price_USD_per_MWh", 42, 1e-9), ("ex049", "producer_surplus_USD_per_h", 1200 * 42 + 800 * 30 + 1500 * 7, 1e-6),
 ("ex050", "energy_plus_regulation_USD_per_h", 180 * 10 + 20 * 12, 1e-9), ("ex050", "regulation_requirement_MW", 50, 1e-9), ("ex051", "accredited_MW", 475 + 60 + 60 + 54, 1e-9), ("ex051", "annual_capacity_revenue_USD", 649 * 150 * 365, 1e-3), ("ex051", "cost_to_cover_short_USD", (690 - 649) * 150 * 365, 1e-3),
 ("ex052", "shadow_total_USD", 500 * 42 + 30 * 60 + 530 * 1.5, 1e-9), ("ex052", "difference_USD", 120, 1e-9), ("ex053", "clearing_price", 2.10 * 10.2 + 4.5, 1e-9), ("ex053", "gas_price_where_CC2_displaces_COAL", (2.10 * 10.2 + 4.5 - 3.0) / 7.4, 1e-9), ("ex053", "coal_dispatch_MW_gas_2_50", 0, 1e-9),
 ("ex054", "full_load_heat_rate", 7.0, 1e-9), ("ex054", "incremental_heat_rate_400_to_500", 6.0, 1e-9), ("ex054", "no_load_fuel_MMBtu_per_h", 500, 1e-9), ("ex057", "zonal_load_payment_USD_per_h", 300 * 20 + 4500, 1e-6), ("ex057", "nodal_load_payment_USD_per_h", 300 * 80, 1e-6),
 ("ex058", "obligation_payout_USD", 50 * (5 + 10 + 20 + 35 + 15 + 5 - 8), 1e-9), ("ex058", "option_payout_USD", 50 * 90, 1e-9), ("ex059", "realized_profit_USD", 25 * 720 * 3.1 + 40 * 720 * 0.4 - 10 * 720 * 1.0 - 90000, 1e-6), ("ex059", "expected_profit_USD", 36000 + 43200 + 28800 - 90000, 1e-6),
 ("ex064", "unserved_MWh", 5 * (9600 - 480 - 6000) - 5000, 1e-6), ("ex064", "storage_duration_needed_hours", 15600 / 250, 1e-9), ("ex066", "lost_MW", 900 - 400 - 2200 / 8, 1e-9), ("ex066", "lost_margin_USD_per_h", 25 * (80 - 48) + 200 * (80 - 60), 1e-9),
 ("ex067", "energy_cost_USD", 24000 * (55 * 60 + 9000 * (58 + 48 + 50 + 58)), 1e-3), ("ex067", "unserved_GWh", (4 + 22 + 18 + 2) * 24, 1e-9), ("ex069", "accepted", 4, 0), ("ex069", "rejected", 5, 0), ("ex072", "rejected_events", 2, 0), ("ex072", "settled_trades", 1, 0),
 ("ex073", "total_exposure_USD", 600000 + 150000 + 400000 + 150000, 1e-6), ("ex073", "collateral_calls_USD", 100000 + 100000, 1e-6), ("ex074", "delivery_shortfall_MMBtu", 55000 - 50000 * 0.98, 1e-6), ("ex074", "receipt_needed_MMBtu", 55000 / 0.98, 1e-6),
 ("ex076", "price_coverage_pct", 50, 1e-9), ("ex076", "mtm_priced_trades_USD", 100000 * (3.25 - 3.20) + 16000 * (45.50 - 45.00), 1e-6), ("ex086", "explained_pnl_USD", 50000 - 30000 + 40000 - 30000 - 1200 - 2500, 1e-6), ("ex086", "unexplained_USD", 1200, 1e-6),
 ("ex087", "fact_price_rows", 6, 0), ("ex087", "orphan_facts", 0, 0), ("ex087", "reference_locations_without_prices", 12 - 5, 0), ("ex088", "status_200", 3, 0), ("ex088", "status_404", 3, 0), ("ex088", "henry_hub_0800_price", 3.25, 1e-9), ("ex089", "unserved_MWh", 0, 1e-9),
 ("ex091", "total_cost_USD_per_yr", 1000 * (300000 + 8 * 8760) + 600 * (120000 + 30 * 4000) + 400 * (60000 + 60 * 500), 1e-2), ("ex091", "crossover_hours_CT_vs_CC", 60000 / 30, 1e-9), ("ex091", "crossover_hours_CC_vs_Baseload", 180000 / 22, 1e-9),
 ("ex096", "requirements", 8, 0), ("ex096", "requirements_with_working_exercise", 8, 0), ("ex096", "requirements_with_automated_test", 8, 0), ("ex097", "top_score_balanced", (7 + 5 + 9 - 2) / 4, 1e-9), ("ex098", "net_revenue_retention_pct", 1130 / 1250 * 100, 1e-9), ("ex098", "gross_revenue_retention_pct", 1040 / 1250 * 100, 1e-9),
 ("ex099", "components", 13, 0), ("ex099", "orphan_components", 0, 0), ("ex099", "vendor_capabilities_asserted", 0, 0), ("ex101", "net_storage_margin_USD_per_gal", 0.12 - (0.005 * 7 + 0.685 * 0.06 * 7 / 12), 1e-9),
 ("ex102", "fee_based_processor_low", 0.35 * 200000, 1e-6), ("ex102", "keep_whole_processor_low", NGLVAL - SHRINK * 3.25 - 5000 * 3.25, 1e-3), ("ex102", "keep_whole_processor_high", NGLVAL - SHRINK * 7.5 - 5000 * 7.5, 1e-3),
 ("ex103", "arbitrage_USD_per_tonne", 560 - 0.72 * 521 - 0.06 * 521 - 120, 1e-9), ("ex104", "off_spec_volume_gal", 400000 + 300000 + 600000, 1e-9), ("ex104", "discount_exposure_USD", 1300000 * 0.05, 1e-9)]
TXT = [("ex001", "most_central_node", "Henry_Hub"), ("ex008", "indifferent", "Pipeline,Utility"), ("ex017", "most_affected_node", "HUB_EAST"), ("ex019", "weakest_hub", "Waha"), ("ex028", "shippers_cut", "Beta,Gamma"), ("ex050", "best_option", "energy_plus_regulation"),
       ("ex053", "merit_order", "NUC>CC1>COAL>CC2>GT"), ("ex053", "merit_order_gas_2_50", "NUC>CC1>CC2>COAL>GT"), ("ex073", "breaches", "CP_A,CP_C"), ("ex074", "binding_constraint", "transport_MDQ"), ("ex076", "integration_breaks", "TR002:Algonquin,TR004:Mont_Belvieu"),
       ("ex091", "screening_choice_by_block", "Baseload>Combined_Cycle>Combustion_Turbine"), ("ex097", "rank_1", "Basis_monitor"), ("ex102", "contract_most_exposed_to_gas_for_processor", "keep_whole"), ("ex104", "off_spec_samples", "S2,S3,S5"), ("ex087", "locations_missing_reference_data", "none")]
B1 = {"ex001","ex002","ex004","ex006","ex007","ex008","ex011","ex012","ex013","ex014","ex016","ex017","ex018","ex019","ex022","ex024","ex026","ex027","ex028","ex029","ex031","ex032","ex034","ex036"}
NUM = [x for x in NUM if x[0] not in B1] + [("ex001", "nodes", 18, 0), ("ex001", "links", 19, 0), ("ex001", "path_handoffs", 7, 0), ("ex002", "participant_types", 12, 0),
 ("ex004", "delivered_MWh", 1e6 * 1.037 / 7 * 0.975 * 0.98 * 0.96, 1e-6), ("ex004", "fuel_cost_USD_per_delivered_MWh", 3.25 * 7 / (0.975 * 0.98 * 0.96), 1e-9), ("ex006", "retail_cost_USD_per_MWh", 45 + 2.7 + 9 + 2 + 14 + 5 + 38 + 6, 1e-9), ("ex006", "retail_cost_change_pct", 47.7 * 0.5 / 121.7 * 100, 1e-9),
 ("ex007", "gas_locations", 5, 0), ("ex007", "ngl_locations", 2, 0), ("ex007", "duplicate_location_names", 0, 0), ("ex008", "Producer_immediate_pnl_USD_per_d", 500000 * 2 * 0.4, 1e-9), ("ex008", "Gas_Generator_immediate_pnl_USD_per_d", -168000 * 2 + 24000 * 7 * 2 * 0.5, 1e-9),
 ("ex008", "Pipeline_immediate_pnl_USD_per_d", 0, 1e-9), ("ex008", "Trader_immediate_pnl_USD_per_d", -200000, 1e-9), ("ex011", "total_growth_pct", (19.0 / 18.5 - 1) * 100, 1e-9), ("ex011", "Montney_share_pct", 10.9 / 19.0 * 100, 1e-9), ("ex011", "Montney_netback", 2.15 - 0.35 - 1.45 + 0.90, 1e-9),
 ("ex012", "Firm_to_Gulf_Coast_netback", 3.15 * 0.98 - 0.60 - 0.40, 1e-9), ("ex012", "blended_netback_USD_per_MMBtu", (30000 * (3.60 * 0.965 - 1.25) + 60000 * (3.15 * 0.98 - 1.0) + 10000 * 0.70) / 100000, 1e-9), ("ex013", "energy_balance_residual", 0, 1e-6), ("ex013", "residue_gas_MMBtu_per_d", 200000 * 1.25 * 0.985 - SHRINK, 1e-3),
 ("ex014", "Permian_to_Gulf_utilization_pct", 1840 / 1850 * 100, 1e-9), ("ex014", "total_release_candidate_MMBtu_d", 10000 + 270000 + 180000, 1e-9), ("ex016", "breakeven_load_factor", 0.45 / (0.55 - 0.02), 1e-9), ("ex016", "firm_unit_cost_at_50pct", 0.92, 1e-9), ("ex017", "extra_unmet_Bcf_d", 5, 1e-6),
 ("ex019", "Waha_basis_day1", 1.10 - 3.25, 1e-9), ("ex019", "Algonquin_basis_day1", 8.75 - 3.25, 1e-9), ("ex019", "largest_basis_move", -1.5, 1e-9), ("ex022", "winter_minus_summer_strip", (3.6 + 3.5 + 3.2 + 3.45 + 3.85) / 5 - (3.0 + 2.95 + 3.0 + 3.1 + 3.12 + 3.08 + 3.15) / 7, 1e-9), ("ex022", "Jan_minus_Jul", 0.5, 1e-9),
 ("ex024", "locked_all_in_price", 3.40 - 0.90, 1e-9), ("ex024", "unhedged_cost_range_USD", 310000 * (4.60 - 1.20), 1e-6), ("ex024", "hh_hedged_cost_range_USD", 310000 * ((4.60 - 1.50) - (1.20 + 1.00)), 1e-6), ("ex026", "Cold_winter_price", 3.25 * (114 / 110) ** 4, 1e-9), ("ex026", "price_per_1_Bcf_d_tightening", 3.25 * ((111 / 110) ** 4 - 1), 1e-9),
 ("ex027", "pnl_USD", 150000 * -1.5 - 80000 * 1.5 - 100000 * 0.3 + 120000 * -0.1, 1e-6), ("ex027", "mtm_day1_USD", 15000 + 15000 - 20000 + 5000 - 6000 + 17500, 1e-6), ("ex027", "hh_price_pnl_USD", 0, 1e-9), ("ex028", "confirmed_MMBtu", 490000, 1e-6), ("ex028", "confirmation_cuts_MMBtu", 20000, 1e-6), ("ex028", "capacity_cuts_MMBtu", 70000, 1e-6),
 ("ex029", "Alpha_cashout_USD", 45000 * 3.25, 1e-6), ("ex029", "Beta_cashout_USD", -120000 * 3.25, 1e-6), ("ex029", "Gamma_cashout_USD", 90000 * 3.25 + 90000 * 3.25 * 1.10 + 18000 * 3.25 * 1.25, 1e-6), ("ex029", "total_penalty_vs_index_USD", 90000 * 3.25 * 0.10 + 18000 * 3.25 * 0.25, 1e-6),
 ("ex031", "days_with_shortfall", 40, 0), ("ex032", "feed_gas_Bcf_d", (4.5 * 0.92 + 3 * 0.95 + 5 * 0.88 + 2.5 * 0.4 + 0.8 * 0.9) * 1.1, 1e-9), ("ex032", "feed_gas_at_full_utilization_Bcf_d", 15.8 * 1.1, 1e-9), ("ex034", "months", 36, 0),
 ("ex036", "total_shortfall_Bcf", 0.94 + 3.26 + 2.6, 1e-9), ("ex036", "storage_withdrawn_Bcf", 0.86 + 6 + 6 + 6 + 1.74, 1e-9), ("ex036", "peak_day", 4, 0)]
TXT = [x for x in TXT if x[0] not in B1] + [("ex001", "most_connected_node", "Interstate_Pipeline"), ("ex002", "rate_regulated", "Interstate_Pipeline,LDC_Gas_Utility,Vertically_Integrated_Utility,ISO_RTO"), ("ex008", "winners", "Producer"), ("ex014", "data_errors", "Rockies_to_West"),
 ("ex019", "widest_discount", "Waha"), ("ex027", "largest_loss_hub", "Waha"), ("ex028", "shippers_cut", "Beta,Delta,Echo"), ("ex036", "shortfall_days", "3,4,5")]
class TestRemaining(Base):
    @classmethod
    def setUpClass(cls): cls.R = {m: run(m) for m in sorted({x[0] for x in NUM + TXT} | {"ex009", "ex061", "ex062", "ex068", "ex078", "ex079", "ex083", "ex093"})}
    def test_numeric_expectations(self):
        for m, k, v, tol in NUM:
            with self.subTest(exercise=m, key=k): self.near(float(self.R[m][k]), v, max(tol, 1e-9))
    def test_text_expectations(self):
        for m, k, v in TXT:
            with self.subTest(exercise=m, key=k): self.assertEqual(self.R[m][k], v)
    def test_009_078_recomputed_from_csv(self):
        d = rows(SYN / "ex009_daily_market.csv"); self.near(self.R["ex009"]["mean_implied_heat_rate"], sum(float(x["power_price"]) / float(x["henry_hub"]) for x in d) / len(d), 1e-9)
        p = [float(x["henry_hub_USD_per_MMBtu"]) for x in rows(SYN / "ex077_hh_daily_synthetic.csv")]; lr = [math.log(b / a) for a, b in zip(p, p[1:])]; m = sum(lr) / len(lr); self.near(self.R["ex078"]["annualised_vol"], math.sqrt(sum((v - m) ** 2 for v in lr) / (len(lr) - 1) * 252), 1e-9)
    def test_061_independent_search(self):
        mg = [p - 7.2 * 3.25 - 3 for p in PX]; best = max([(sum(mg[s:e + 1]) * 500 - 20000, s + 1, e + 1) for s in range(24) for e in range(s + 3, 24)] + [(0.0, 0, 0)]); r = self.R["ex061"]
        self.near(r["committed_profit_USD"], best[0], 1e-6); self.assertEqual((r["committed_start_hour"], r["committed_end_hour"]), best[1:]); self.near(r["hourly_rule_gross_margin_USD"], 500 * sum(max(v, 0) for v in mg), 1e-6)
    def test_062_settlement_identity(self):
        d = rows(DONE / "ex062/forecast_settlement.csv"); rev = sum(float(x["forecast_MW"]) * float(x["da_price"]) + (float(x["actual_MW"]) - float(x["forecast_MW"])) * float(x["rt_price"]) for x in d); self.near(self.R["ex062"]["revenue_USD"], rev, 1e-6)
        self.near(self.R["ex062"]["imbalance_cost_USD"], sum((float(x["actual_MW"]) - float(x["forecast_MW"])) * (float(x["da_price"]) - float(x["rt_price"])) for x in d), 1e-6)
    def test_068_greedy_equals_lp(self):
        mg = sorted((p - 7.2 * 3.25 - 3 for p in PX), reverse=True); left = 40000 / 7.2; tot = 0.0
        for v in mg:
            q = min(500, left); tot += max(v, 0) * q; left -= q
        self.near(self.R["ex068"]["gas_unit_margin_USD"], tot, 1e-4); self.near(self.R["ex068"]["gas_burn_MMBtu"], 40000, 1e-4); self.assertEqual(self.R["ex068"]["full_load_hours"], 11)
    def test_079_083_089_093_invariants(self):
        f = self.R["ex079"]; self.assertLess(f["model_mape_pct"], f["naive_mape_pct"]); self.near(f["GWh_per_CDD"], 4.0, 0.5); self.near(f["GWh_per_HDD"], 2.5, 0.5); self.near(f["weekend_effect_GWh"], -25, 4)
        p = self.R["ex083"]; self.near(p["pfe_at_maturity_USD"], 0, 1e-9); self.assertTrue(2 <= p["peak_pfe_month"] <= 9 and p["peak_pfe_USD"] > p["peak_expected_exposure_USD"] > 0); self.near(run("ex083")["peak_pfe_USD"], p["peak_pfe_USD"], 1e-9)
        s = self.R["ex089"]; self.near(sum(v for k, v in s.items() if k.endswith("_share_pct")), 100, 1e-6); self.assertGreaterEqual(s["load_weighted_price_USD_per_MWh"], s["average_cost_USD_per_MWh"]); self.assertGreater(run("ex089", gas_cost_scale=2.0)["total_production_cost_USD"], s["total_production_cost_USD"]); run("ex089")
        o = self.R["ex093"]; self.assertTrue(o["parallel_results_equivalent"]); self.assertFalse(o["reduced_resolution_equivalent"]); self.assertGreater(o["reduced_resolution_objective_error_pct"], 0)
    def test_scenarios(self):
        self.near(run("ex012", volume_MMBtu_d=30000)["blended_netback_USD_per_MMBtu"], 3.60 * 0.965 - 1.25, 1e-9); self.near(run("ex103", mont_belvieu_USD_per_gal=self.R["ex103"]["breakeven_mont_belvieu_USD_per_gal"])["arbitrage_USD_per_tonne"], 0, 1e-9)
        self.near(run("ex036", storage_max=100)["total_shortfall_Bcf"], 0, 1e-9); r31 = self.R["ex031"]; self.near(r31["total_withdrawn_MMBtu"] + r31["end_inventory_pct"] * 1e5, 9e6, 1e-3); self.assertLessEqual(run("ex018")["max_flow_to_LNG_GULF_Bcf_d"], 12); self.assertEqual(run("ex038", gas_price=7.5)["decision"], "REJECT")
        for m in ("ex012", "ex103", "ex036", "ex038"): run(m)
if __name__ == "__main__": unittest.main()
