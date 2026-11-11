# ex077 | SYNTHETIC HYPOTHETICAL DATA - not historical market data

train_rows: 300

test_rows: 99

intercept: 0.270758

coef_lag_price: 0.889493

coef_hdd: 0.004145

model_mae: 0.064202

model_rmse: 0.081947

model_mape_pct: 1.700686

model_bias: 0.00886

naive_mae: 0.063398

naive_rmse: 0.080086

naive_mape_pct: 1.683732

naive_bias: -0.00279

in_sample_rmse: 0.075422

rmse_skill_vs_naive_pct: -2.322766

generating_process: price = 0.9*lag + 0.1*(2.5 + 0.04*HDD) + N(0, 0.08)

NOTE: HDD is used as a known input on the forecast day (perfect weather foresight); a real forecast needs forecast HDD.

NOTE: On this sample the fitted model does NOT beat persistence out of sample (negative skill) even though the data were generated from the same linear form: with 0.9 persistence and noise of 0.08 the HDD signal is too weak to estimate reliably from 300 days.

