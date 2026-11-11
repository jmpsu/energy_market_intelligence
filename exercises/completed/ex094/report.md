# ex094 | SYNTHETIC HYPOTHETICAL DATA - not historical market data

hours: 48

energy_balance_all_hours: True

model_prices_are_stack_costs: True

validation_mae_raw: 6.674167

validation_bias_raw: -5.136667

validation_corr_raw: 0.94848

high_load_bias_raw: -19.787143

normal_load_bias_raw: 0.895882

raw_model_passes: False

calibrated_scarcity_adder_USD_per_MWh_per_MW: 0.048415

validation_mae_calibrated: 1.549857

validation_bias_calibrated: 0.729596

calibrated_model_passes: True

mae_threshold: 3

high_load_hours_in_validation: 7

NOTE: Diagnosis: error is concentrated in high-load hours (structural: the stack has no scarcity pricing), not spread evenly (which would suggest a cost-level calibration error).

NOTE: Calibrated on hours 0-23, validated on hours 24-47; the synthetic observed series was generated with an adder of 0.05 USD/MWh per MW above 5200 MW plus noise (sd 2).

NOTE: Passing a backcast does not validate the model for conditions outside the sample (outages, new capacity, fuel price changes).

