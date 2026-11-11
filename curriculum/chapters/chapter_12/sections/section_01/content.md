# 12.1 Integrated gas and power market fundamentals

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-066 Model Gas-Electric Coordination (`python3 emi.py run 066`). Full output: `exercises/completed/ex066/report.md`.

## L12.01.1 Gas-power coupling

**Objective.** Explain gas-power coupling and show it in the EX-066 output.

**Prerequisites.** L11.10.5

**Lesson.** Gas plants link the gas and power markets. [K]

**Example.** EX-066 (Model Gas-Electric Coordination) on synthetic North American data: fuel_needed_MMBtu_per_h = 7200 [EX]

**Do.** `python3 emi.py run 066 | grep '^fuel_needed_MMBtu_per_h:'`

**Expect.** `fuel_needed_MMBtu_per_h: 7200`

**On the job.** Simulate how gas pipeline constraints affect the availability and dispatch of gas-fired power generators.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L11.10.5 | After: L12.01.2

## L12.01.2 Fuel-driven price formation

**Objective.** Explain fuel-driven price formation and show it in the EX-066 output.

**Prerequisites.** L12.01.1

**Lesson.** When gas is marginal, power price follows gas price times heat rate. [K]

**Example.** EX-066 (Model Gas-Electric Coordination) on synthetic North American data: fuel_available_MMBtu_per_h = 5000 [EX]

**Do.** `python3 emi.py run 066 | grep '^fuel_available_MMBtu_per_h:'`

**Expect.** `fuel_available_MMBtu_per_h: 5000`

**On the job.** Simulate how gas pipeline constraints affect the availability and dispatch of gas-fired power generators.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.01.1 | After: L12.01.3

## L12.01.3 Weather as joint driver

**Objective.** Explain weather as joint driver and show it in the EX-066 output.

**Prerequisites.** L12.01.2

**Lesson.** Cold or heat raises gas and power demand together. [K]

**Example.** EX-066 (Model Gas-Electric Coordination) on synthetic North American data: fuel_shortfall_pct = 30.555556 [EX]

**Do.** `python3 emi.py run 066 | grep '^fuel_shortfall_pct:'`

**Expect.** `fuel_shortfall_pct: 30.555556`

**On the job.** Simulate how gas pipeline constraints affect the availability and dispatch of gas-fired power generators.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.01.2 | After: L12.01.4

## L12.01.4 Integrated balance

**Objective.** Explain integrated balance and show it in the EX-066 output.

**Prerequisites.** L12.01.3

**Lesson.** An integrated balance tracks both commodities. [K]

**Example.** EX-066 (Model Gas-Electric Coordination) on synthetic North American data: output_MW = 675 [EX]

**Do.** `python3 emi.py run 066 | grep '^output_MW:'`

**Expect.** `output_MW: 675`

**On the job.** Simulate how gas pipeline constraints affect the availability and dispatch of gas-fired power generators.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.01.3 | After: L12.01.5

## L12.01.5 Fundamentals briefing

**Objective.** Explain fundamentals briefing and show it in the EX-066 output.

**Prerequisites.** L12.01.4

**Lesson.** A fundamentals briefing states drivers, balance and risks. [K]

**Example.** EX-066 (Model Gas-Electric Coordination) on synthetic North American data: lost_MW = 225 [EX]

**Do.** `python3 emi.py run 066 | grep '^lost_MW:'`

**Expect.** `lost_MW: 225`

**On the job.** Simulate how gas pipeline constraints affect the availability and dispatch of gas-fired power generators.

**Product implication.** Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters.

Before: L12.01.4 | After: L12.02.1
