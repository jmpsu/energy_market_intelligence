# 7.9 Long-duration and seasonal storage

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-064 Analyze Dunkelflaute Conditions (`python3 emi.py run 064`). Full output: `exercises/completed/ex064/report.md`.

## L07.09.1 Long-duration storage technologies

**Objective.** Explain long-duration storage technologies and show it in the EX-064 output.

**Prerequisites.** L07.08.5

**Lesson.** Long-duration storage includes pumped hydro and other multi-hour to multi-day technologies. [K]

**Example.** EX-064 (Analyze Dunkelflaute Conditions) on synthetic North American data: daily_gap_in_lull_MWh = 3120 [EX]

**Do.** `python3 emi.py run 064 | grep '^daily_gap_in_lull_MWh:'`

**Expect.** `daily_gap_in_lull_MWh: 3120`

**On the job.** Simulate prolonged periods of low wind and solar generation and quantify the resulting scarcity exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.08.5 | After: L07.09.2

## L07.09.2 Seasonal balancing

**Objective.** Explain seasonal balancing and show it in the EX-064 output.

**Prerequisites.** L07.09.1

**Lesson.** Seasonal balancing needs far more energy than daily shifting. [K]

**Example.** EX-064 (Analyze Dunkelflaute Conditions) on synthetic North American data: lull_energy_gap_MWh = 15600 [EX]

**Do.** `python3 emi.py run 064 | grep '^lull_energy_gap_MWh:'`

**Expect.** `lull_energy_gap_MWh: 15600`

**On the job.** Simulate prolonged periods of low wind and solar generation and quantify the resulting scarcity exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.09.1 | After: L07.09.3

## L07.09.3 Dunkelflaute exposure

**Objective.** Explain dunkelflaute exposure and show it in the EX-064 output.

**Prerequisites.** L07.09.2

**Lesson.** A dunkelflaute is a multi-day stretch of low wind and solar. [K]

**Example.** EX-064 (Analyze Dunkelflaute Conditions) on synthetic North American data: storage_discharged_MWh = 5000 [EX]

**Do.** `python3 emi.py run 064 | grep '^storage_discharged_MWh:'`

**Expect.** `storage_discharged_MWh: 5000`

**On the job.** Simulate prolonged periods of low wind and solar generation and quantify the resulting scarcity exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.09.2 | After: L07.09.4

## L07.09.4 Duration valuation

**Objective.** Explain duration valuation and show it in the EX-064 output.

**Prerequisites.** L07.09.3

**Lesson.** Each added hour of duration earns less than the one before. [K]

**Example.** EX-064 (Analyze Dunkelflaute Conditions) on synthetic North American data: unserved_MWh = 10600 [EX]

**Do.** `python3 emi.py run 064 | grep '^unserved_MWh:'`

**Expect.** `unserved_MWh: 10600`

**On the job.** Simulate prolonged periods of low wind and solar generation and quantify the resulting scarcity exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.09.3 | After: L07.09.5

## L07.09.5 Storage adequacy contribution

**Objective.** Explain storage adequacy contribution and show it in the EX-064 output.

**Prerequisites.** L07.09.4

**Lesson.** Storage counts toward adequacy only for as long as it can discharge. [K]

**Example.** EX-064 (Analyze Dunkelflaute Conditions) on synthetic North American data: unserved_days = 4 [EX]

**Do.** `python3 emi.py run 064 | grep '^unserved_days:'`

**Expect.** `unserved_days: 4`

**On the job.** Simulate prolonged periods of low wind and solar generation and quantify the resulting scarcity exposure.

**Product implication.** Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.

Before: L07.09.4 | After: L07.10.1
