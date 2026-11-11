# ex079 | SYNTHETIC HYPOTHETICAL DATA - not historical market data

train_days: 150

test_days: 60

base_load_GWh: 298.967157

GWh_per_CDD: 4.11384

GWh_per_HDD: 2.508525

weekend_effect_GWh: -23.869823

model_mape_pct: 1.423928

naive_mape_pct: 6.520203

model_bias_GWh: 1.550732

skill_vs_naive_pct: 78.161298

true_parameters: 300 base, 4.0/CDD, 2.5/HDD, -25 weekend, noise sd 6

NOTE: Actual temperature is used as the input: forecast-temperature error would add to load error. The model form matches the generator, so this is a best case.

