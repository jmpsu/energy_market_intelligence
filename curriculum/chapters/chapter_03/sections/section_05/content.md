# 3.5 Forward curves and calendar spreads

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-023 Build a Natural Gas Forward Curve (`python3 emi.py run 023`). Full output: `exercises/completed/ex023/report.md`.

## L03.05.1 Curve construction from quotes

**Objective.** Explain curve construction from quotes and show it in the EX-023 output.

**Prerequisites.** L03.04.5

**Lesson.** A forward curve is built from quoted contract prices by delivery month. [K]

**Example.** EX-023 (Build a Natural Gas Forward Curve) on synthetic North American data: calendar_strip_USD_per_MMBtu = 3.25 [EX]

**Do.** `python3 emi.py run 023 | grep '^calendar_strip_USD_per_MMBtu:'`

**Expect.** `calendar_strip_USD_per_MMBtu: 3.25`

**On the job.** Construct a forward price curve from monthly market observations and calculate its shape.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.04.5 | After: L03.05.2

## L03.05.2 Contango, backwardation, seasonality

**Objective.** Explain contango, backwardation, seasonality and show it in the EX-023 output.

**Prerequisites.** L03.05.1

**Lesson.** Contango means later months cost more; backwardation the reverse; gas adds a winter premium. [K]

**Example.** EX-023 (Build a Natural Gas Forward Curve) on synthetic North American data: winter_strip = 3.52 [EX]

**Do.** `python3 emi.py run 023 | grep '^winter_strip:'`

**Expect.** `winter_strip: 3.52`

**On the job.** Construct a forward price curve from monthly market observations and calculate its shape.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.05.1 | After: L03.05.3

## L03.05.3 Calendar spreads

**Objective.** Explain calendar spreads and show it in the EX-023 output.

**Prerequisites.** L03.05.2

**Lesson.** A calendar spread is the price difference between two delivery months. [K]

**Example.** EX-023 (Build a Natural Gas Forward Curve) on synthetic North American data: summer_strip = 3.057143 [EX]

**Do.** `python3 emi.py run 023 | grep '^summer_strip:'`

**Expect.** `summer_strip: 3.057143`

**On the job.** Construct a forward price curve from monthly market observations and calculate its shape.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.05.2 | After: L03.05.4

## L03.05.4 Strip and seasonal pricing

**Objective.** Explain strip and seasonal pricing and show it in the EX-023 output.

**Prerequisites.** L03.05.3

**Lesson.** A strip is the average over consecutive months, such as a winter or summer strip. [K]

**Example.** EX-023 (Build a Natural Gas Forward Curve) on synthetic North American data: winter_minus_summer = 0.462857 [EX]

**Do.** `python3 emi.py run 023 | grep '^winter_minus_summer:'`

**Expect.** `winter_minus_summer: 0.462857`

**On the job.** Construct a forward price curve from monthly market observations and calculate its shape.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.05.3 | After: L03.05.5

## L03.05.5 Curve shape interpretation

**Objective.** Explain curve shape interpretation and show it in the EX-023 output.

**Prerequisites.** L03.05.4

**Lesson.** Curve shape tells you what the market pays to store, and where it expects tightness. [K]

**Example.** EX-023 (Build a Natural Gas Forward Curve) on synthetic North American data: jan_minus_jul_spread = 0.5 [EX]

**Do.** `python3 emi.py run 023 | grep '^jan_minus_jul_spread:'`

**Expect.** `jan_minus_jul_spread: 0.5`

**On the job.** Construct a forward price curve from monthly market observations and calculate its shape.

**Product implication.** Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.

Before: L03.05.4 | After: L03.06.1
