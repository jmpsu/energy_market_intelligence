# 9.9 Scenario analysis and stress testing

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-084 Perform Energy Portfolio Stress Testing (`python3 emi.py run 084`). Full output: `exercises/completed/ex084/report.md`.

## L09.09.1 Scenario design

**Objective.** Explain scenario design and show it in the EX-084 output.

**Prerequisites.** L09.08.5

**Lesson.** A stress scenario is a specific, severe set of price moves. [K]

**Example.** EX-084 (Perform Energy Portfolio Stress Testing) on synthetic North American data: Gas_Collapse_change_USD = -533522.647059 [EX]

**Do.** `python3 emi.py run 084 | grep '^Gas_Collapse_change_USD:'`

**Expect.** `Gas_Collapse_change_USD: -533522.647059`

**On the job.** Evaluate portfolio losses under extreme gas prices, electricity scarcity, pipeline outages, and weather events.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.08.5 | After: L09.09.2

## L09.09.2 Historical stress events

**Objective.** Explain historical stress events and show it in the EX-084 output.

**Prerequisites.** L09.09.1

**Lesson.** Historical stresses replay real events. [K]

**Example.** EX-084 (Perform Energy Portfolio Stress Testing) on synthetic North American data: Mild_Winter_change_USD = -496127.941176 [EX]

**Do.** `python3 emi.py run 084 | grep '^Mild_Winter_change_USD:'`

**Expect.** `Mild_Winter_change_USD: -496127.941176`

**On the job.** Evaluate portfolio losses under extreme gas prices, electricity scarcity, pipeline outages, and weather events.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.09.1 | After: L09.09.3

## L09.09.3 Hypothetical stress

**Objective.** Explain hypothetical stress and show it in the EX-084 output.

**Prerequisites.** L09.09.2

**Lesson.** Hypothetical stresses are designed around the book's weak points. [K]

**Example.** EX-084 (Perform Energy Portfolio Stress Testing) on synthetic North American data: Power_Collapse_change_USD = -416113.235294 [EX]

**Do.** `python3 emi.py run 084 | grep '^Power_Collapse_change_USD:'`

**Expect.** `Power_Collapse_change_USD: -416113.235294`

**On the job.** Evaluate portfolio losses under extreme gas prices, electricity scarcity, pipeline outages, and weather events.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.09.2 | After: L09.09.4

## L09.09.4 Reverse stress testing

**Objective.** Explain reverse stress testing and show it in the EX-084 output.

**Prerequisites.** L09.09.3

**Lesson.** Reverse stress finds the scenario that produces a given loss. [K]

**Example.** EX-084 (Perform Energy Portfolio Stress Testing) on synthetic North American data: Renewable_Drought_Low_Price_change_USD = -256144.294118 [EX]

**Do.** `python3 emi.py run 084 | grep '^Renewable_Drought_Low_Price_change_USD:'`

**Expect.** `Renewable_Drought_Low_Price_change_USD: -256144.294118`

**On the job.** Evaluate portfolio losses under extreme gas prices, electricity scarcity, pipeline outages, and weather events.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.09.3 | After: L09.09.5

## L09.09.5 Stress reporting

**Objective.** Explain stress reporting and show it in the EX-084 output.

**Prerequisites.** L09.09.4

**Lesson.** Stress reports show loss per scenario against limits. [K]

**Example.** EX-084 (Perform Energy Portfolio Stress Testing) on synthetic North American data: Base_change_USD = 0 [EX]

**Do.** `python3 emi.py run 084 | grep '^Base_change_USD:'`

**Expect.** `Base_change_USD: 0`

**On the job.** Evaluate portfolio losses under extreme gas prices, electricity scarcity, pipeline outages, and weather events.

**Product implication.** Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.

Before: L09.09.4 | After: L09.10.1
