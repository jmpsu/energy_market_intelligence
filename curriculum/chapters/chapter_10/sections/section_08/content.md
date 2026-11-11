# 10.8 APIs, ETL/ELT, and ETRM integrations

Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.

Section exercise: EX-088 Develop a Market Data API (`python3 emi.py run 088`). Full output: `exercises/completed/ex088/report.md`.

## L10.08.1 API design

**Objective.** Explain aPI design and show it in the EX-088 output.

**Prerequisites.** L10.07.5

**Lesson.** An API exposes data through documented endpoints. [K]

**Example.** EX-088 (Develop a Market Data API) on synthetic North American data: requests = 7 [EX]

**Do.** `python3 emi.py run 088 | grep '^requests:'`

**Expect.** `requests: 7`

**On the job.** Build an interface that exposes validated market prices and analytical outputs to downstream applications.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.07.5 | After: L10.08.2

## L10.08.2 ETL vs ELT

**Objective.** Explain eTL vs ELT and show it in the EX-088 output.

**Prerequisites.** L10.08.1

**Lesson.** ETL transforms before loading; ELT after. [K]

**Example.** EX-088 (Develop a Market Data API) on synthetic North American data: status_200 = 3 [EX]

**Do.** `python3 emi.py run 088 | grep '^status_200:'`

**Expect.** `status_200: 3`

**On the job.** Build an interface that exposes validated market prices and analytical outputs to downstream applications.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.08.1 | After: L10.08.3

## L10.08.3 ETRM integration points

**Objective.** Explain eTRM integration points and show it in the EX-088 output.

**Prerequisites.** L10.08.2

**Lesson.** ETRM integration points are trades, prices, positions and settlements. [K]

**Example.** EX-088 (Develop a Market Data API) on synthetic North American data: status_404 = 3 [EX]

**Do.** `python3 emi.py run 088 | grep '^status_404:'`

**Expect.** `status_404: 3`

**On the job.** Build an interface that exposes validated market prices and analytical outputs to downstream applications.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.08.2 | After: L10.08.4

## L10.08.4 Data contracts

**Objective.** Explain data contracts and show it in the EX-088 output.

**Prerequisites.** L10.08.3

**Lesson.** A data contract states schema, timing and quality. [K]

**Example.** EX-088 (Develop a Market Data API) on synthetic North American data: status_400 = 1 [EX]

**Do.** `python3 emi.py run 088 | grep '^status_400:'`

**Expect.** `status_400: 1`

**On the job.** Build an interface that exposes validated market prices and analytical outputs to downstream applications.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.08.3 | After: L10.08.5

## L10.08.5 Pipeline orchestration

**Objective.** Explain pipeline orchestration and show it in the EX-088 output.

**Prerequisites.** L10.08.4

**Lesson.** Orchestration runs pipelines in order and reports failures. [K]

**Example.** EX-088 (Develop a Market Data API) on synthetic North American data: waha_observations = 2 [EX]

**Do.** `python3 emi.py run 088 | grep '^waha_observations:'`

**Expect.** `waha_observations: 2`

**On the job.** Build an interface that exposes validated market prices and analytical outputs to downstream applications.

**Product implication.** Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.

Before: L10.08.4 | After: L10.09.1
