# 12.6 Transmission and pipeline disruption scenarios

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-060 Simulate Generator Outages (`python3 emi.py run 060`). Full output: `exercises/completed/ex060/report.md`.

## L12.06.1 Transmission outage scenario

**Objective.** Explain transmission outage scenario and show it in the EX-060 output.

**Prerequisites.** L12.05.5

**Lesson.** A transmission outage changes flows and prices. [K]

**Example.** EX-060 (Simulate Generator Outages) on synthetic North American data: Baseline_price_USD_per_MWh = 48 [EX]

**Do.** `python3 emi.py run 060 | grep '^Baseline_price_USD_per_MWh:'`

**Expect.** `Baseline_price_USD_per_MWh: 48`

**On the job.** Remove generation capacity from a simplified power market and recalculate dispatch and market prices.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.05.5 | After: L12.06.2

## L12.06.2 Pipeline outage scenario

**Objective.** Explain pipeline outage scenario and show it in the EX-060 output.

**Prerequisites.** L12.06.1

**Lesson.** A pipeline outage cuts fuel to plants. [K]

**Example.** EX-060 (Simulate Generator Outages) on synthetic North American data: Baseline_available_capacity_MW = 6700 [EX]

**Do.** `python3 emi.py run 060 | grep '^Baseline_available_capacity_MW:'`

**Expect.** `Baseline_available_capacity_MW: 6700`

**On the job.** Remove generation capacity from a simplified power market and recalculate dispatch and market prices.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.06.1 | After: L12.06.3

## L12.06.3 Combined disruption

**Objective.** Explain combined disruption and show it in the EX-060 output.

**Prerequisites.** L12.06.2

**Lesson.** Combined disruptions compound. [K]

**Example.** EX-060 (Simulate Generator Outages) on synthetic North American data: Baseline_reserve_margin_pct = 21.818182 [EX]

**Do.** `python3 emi.py run 060 | grep '^Baseline_reserve_margin_pct:'`

**Expect.** `Baseline_reserve_margin_pct: 21.818182`

**On the job.** Remove generation capacity from a simplified power market and recalculate dispatch and market prices.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.06.2 | After: L12.06.4

## L12.06.4 Impact quantification

**Objective.** Explain impact quantification and show it in the EX-060 output.

**Prerequisites.** L12.06.3

**Lesson.** Quantify impact in MWh, MMBtu and dollars. [K]

**Example.** EX-060 (Simulate Generator Outages) on synthetic North American data: Baseline_unmet_MW = 0 [EX]

**Do.** `python3 emi.py run 060 | grep '^Baseline_unmet_MW:'`

**Expect.** `Baseline_unmet_MW: 0`

**On the job.** Remove generation capacity from a simplified power market and recalculate dispatch and market prices.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.06.3 | After: L12.06.5

## L12.06.5 Mitigation options

**Objective.** Explain mitigation options and show it in the EX-060 output.

**Prerequisites.** L12.06.4

**Lesson.** Mitigations include alternative supply, storage and hedges. [K]

**Example.** EX-060 (Simulate Generator Outages) on synthetic North American data: Baseline_marginal_unit = COAL_01 [EX]

**Do.** `python3 emi.py run 060 | grep '^Baseline_marginal_unit:'`

**Expect.** `Baseline_marginal_unit: COAL_01`

**On the job.** Remove generation capacity from a simplified power market and recalculate dispatch and market prices.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.06.4 | After: L12.07.1
