# **EXPANDED EXECUTION DIRECTIVE**

## **Energy Market Intelligence Curriculum: Task 1 and Task 2**

**Execution mode:** Exhaustive, depth-first, sequential, verified-by-execution.

**Target repository:** `/root/energy_market_intelligence`

**Authoritative requirements:** `/root/agent_prompts/emi_curriculum_task.md`, covering Task 1 and Task 2. Its requirements remain unchanged and take precedence over this execution directive.

**Authorization to continue from the Task 1 report into Task 2 without stopping: NO**

This document reorganizes the execution requirements, operating protocol, engineering specification, and verification requirements into a coherent sequence. It does not authorize skipping, reducing, or weakening any requirement.

# **PART I. OPERATING PROTOCOL**

## **1. Work Queue and Resumption Rules**

The authoritative work queue is:

`/root/energy_market_intelligence/AGENT_WORKQUEUE.md`

1. Read the entire work queue before starting, resuming, or continuing after a context summary.
2. Resume at the first unchecked `[ ]` item.
3. Execute work in the order specified by the queue and the phases in this directive.
4. Work on one item at a time.
5. For each item:
   - Read the relevant requirements and source material.
   - Make the required changes.
   - Run the command that proves the changes work.
   - Capture the actual command output.
   - Append the relevant evidence to the corresponding work queue item.
   - Change `[ ]` to `[x]` only after successful verification.
6. Save the work queue after every completed item.
7. If interrupted, use the work queue as the authoritative record of progress.
8. Do not report completion, produce a final completion summary, or mark all work complete while unchecked items remain.
9. The only authorized stopping points are:
   - Task 1 §6, after delivering the Task 1 report.
   - Task 2 §10, after delivering the Task 2 report.
   - A genuinely blocked item, which must be documented precisely.

## **2. Evidence and Verification**

Evidence must consist of actual command output from the VPS.

The following do not constitute evidence:

- `print()` statements claiming success.
- Statements that something should work.
- A file merely existing.
- Successful imports without functional testing.
- A completed TODO list without corresponding execution evidence.
- Tests that were not actually executed.

If a command fails, its corresponding work item remains unchecked.

If an item genuinely cannot be completed:

`[!] BLOCKED: exact reason and actual command output`

Record the reason and continue with the next item.

Every test step must include execution of:

```
cd /root/energy_market_intelligence && python3 emi.py test
```

The project uses unittest through `emi.py`. Pytest is not installed.

## **3. Change Control**

Do not regenerate existing exercise artifacts unless the specific work item requires it.

Protected artifact locations:

- `exercises/completed/`
- `exercises/expected_output/`
- `reports/model_validation/`
- `data/processed/*.sqlite`

If an operation changes these artifacts, list every changed file in the corresponding work queue item.

After changes, inspect:

```
git status --short
git diff --stat
```

Preserve existing working content unless a requirement explicitly calls for its modification.

# **PART II. ENVIRONMENT AND REPOSITORY BOUNDARIES**

## **4. Verified Environment**

The following environment facts were verified during setup.

**Energy Market Intelligence interpreter:**

`/root/.venvs/emi/bin/python3`

Python version: 3.12.

Available packages include:

- pandas
- numpy
- scipy
- matplotlib
- networkx
- pyyaml

Do not create another virtual environment inside the repository.

Pin any newly added package to its exact version and record that version.

**Henry Hub repository interpreter, read-only use:**

`/root/henry_hub_atomic_agents/.venv/bin/python`

**Ollama endpoint:**

`http://127.0.0.1:11434`

Available models:

- `qwen2.5-coder:32b`
- `qwen3:4b`
- `nomic-embed-text`

**Requirements documents:**

Inspect:

- `/root/energy_market_intelligence/*.odt`
- `/root/energy_market_intelligence_source_docs/*.odt`

If the three required ODT documents cannot be found, record the exact search results as a blocked pre-flight item and continue with the remaining work.

## **5. Repository Boundaries**

The target repository is:

`/root/energy_market_intelligence`

The Henry Hub repository is:

`/root/henry_hub_atomic_agents`

Henry Hub must remain read-only throughout this project.

Its components may be examined, reused, and copied into Energy Market Intelligence where appropriate.

Every copied component must include a header comment identifying its original source path.

Never modify Henry Hub source files, configuration, Git state, or generated artifacts.

Before any Energy Market Intelligence edits, save the Henry Hub Git status to:

`/tmp/hh_status_before.txt`

The original before-and-after comparison cannot be reconstructed if this file was not saved before the first modification. Document that limitation accurately rather than manufacturing a baseline.

# **PART III. TASK 1: PROGRESSIVE CURRICULUM**

## **6. Phase 0: Pre-flight**

Complete Task 1 §1 before making changes.

First save:

`/tmp/hh_status_before.txt`

Then execute and record the required pre-flight commands:

- Energy Market Intelligence Git status.
- Git history.
- Repository file tree.
- Repository disk usage.
- README.md.
- STATUS.md.
- Availability and paths of required command-line tools.
- Python dependencies.
- Henry Hub Git status.
- Henry Hub Git history, including the last 15 commits.
- Henry Hub file tree.

Extract and read all available ODT requirements documents.

Record the outputs.

## **7. Phase 1: Baseline and Gap Analysis**

Establish the baseline before modifying curriculum content.

Inspect the execution, testing, and linting commands for:

- `emi.py`
- `init_db.py`
- `tools/`
- `exercises/`
- `trading_simulation/`
- `market_models/`

Run the available baseline commands and save their output to:

`/tmp/eml_baseline_<timestamp>.txt`

Record:

1. Existing test failures.
2. Existing import failures.
3. Existing broken paths and links.
4. Existing database problems.
5. Missing curriculum content.
6. Missing or incomplete exercises.
7. Missing assessments.
8. Existing visual and diagram deficiencies.

Identify the SQLite database using:

```
file sqlite3
```

Write a gap analysis comparing the requirements documents with the actual repository.

Inspect the curriculum build tools before editing lesson pages. Determine whether running the build tools overwrites manually edited content. Record the actual findings in the work queue.

## **8. Phase 2: Henry Hub Reuse Map**

Examine the following Henry Hub components read-only:

`kb_ingest.py`, `literature_kb.py`, `emi_ingest.py`, `emi_alignment.py`, `knowledge_roles.py`, `lng_evidence.py`, `lng_global.py`, `lng_forward.py`, `lng_feedgas.py`, `frac_module.py`, `fundamentals.py`, `metric_docs.py`, `derivation.py`, `chat_service.py`, `agents/retrieval_hub.py`, `agents/quant_commodities.py`, `agents/quant_risk.py`, `web/tooltip.js`, `web/knowledge.html`, `web/knowledge.js`, `web/drill.js`, `docs/`, and `tests/`.

For each component, document:

1. Its existing functionality.
2. What it contributes to the Energy Market Intelligence curriculum.
3. Whether it should be copied, imported, or called.
4. Its destination path in Energy Market Intelligence.
5. Any dependencies or integration requirements.

Write the reuse map into a file in the Energy Market Intelligence repository.

## **9. Phase 3: Full Curriculum Architecture**

The curriculum contains 12 chapters and 120 sections.

Assign every chapter and section to one of six levels:

- L0
- L1
- L2
- L3
- L4
- L5

Every level must contain:

1. Learning objectives.
2. Prerequisites.
3. Readings.
4. Runnable terminal exercises.
5. Visual explanations.
6. Quiz questions.
7. Quiz answer keys.
8. A capstone.
9. A product-management track component.

For each chapter, read its complete `lessons_source.txt` and `sources.md` before generating or auditing its ten sections.

Map every source topic, subtopic, formula, regulatory framework, market convention, and empirical workflow into the appropriate sections.

No source concepts may be silently dropped.

If a chapter lacks source documents, synthesize authoritative primary-source references appropriate to its scope, including EIA, FERC, CFTC, CME/NYMEX, ICE, ISO/RTO tariff manuals, and academic energy finance literature.

## **10. Phase 4: Market Coverage**

Ensure the curriculum covers every market topic specified in Task 1 §3.

**North America**

- Henry Hub.
- Basis.
- Pipelines and takeaway capacity.
- Storage.
- Production.
- Gulf Coast LNG feedgas.
- Liquefaction.
- AECO.
- LNG Canada.
- Mexico exports.
- NGL processing.
- Mont Belvieu fractionation.
- Ethane exports.
- Propane exports.
- All seven ISO/RTOs.
- Locational Marginal Pricing.
- Congestion.
- Dispatch.
- Merit order.
- Spark spreads.
- Fuel switching.
- Resource adequacy.
- Capacity markets.

**Europe**

- TTF.
- NBP.
- Regasification.
- Storage.
- ENTSOG flows.
- Market coupling.

**Asia**

- JKM.
- Oil-indexed LNG contracts.
- Hub-indexed LNG contracts.
- Demand in Japan.
- Demand in Korea.
- Demand in China.
- Demand in India.

**Global linking topics**

- Freight.
- Netbacks.
- Arbitrage.
- Marginal FOB.
- Seasonal balances.
- Forward curves.
- Calendar spreads.
- Risk.

## **11. Phase 5: Product-Management Track**

Include a product-management track at every curriculum level.

Cover:

- Discovery interviews.
- Product adoption.
- Roadmap prioritization.
- Product requirements documents.
- Go-to-market.
- Net Promoter Score.
- Time to value.
- Team leadership.
- PLEXOS product teardown.
- Aurora product teardown.
- Adapt2 product teardown.
- Production-cost simulation.
- Capacity expansion.
- Resource adequacy.
- Portfolio optimization.
- Price forecasting.
- Modeling assumptions.
- Explaining analytical results.
- Managed services.

Product teardowns must cite public sources only. Mark claims that cannot be verified as `UNVERIFIED`.

## **12. Phase 6: Curriculum Entry Point**

Create one authoritative entry point in the README or index.

It must include:

- Complete learning path.
- Level progression.
- Chapter and section navigation.
- Progress tracker.
- Environment setup.
- Required dependencies.
- How to run exercises.
- How to run tests.
- How to run the entire curriculum.
- How to access the visual library.

## **13. Phase 7: Technical Repair and Execution**

Fix:

- Broken code.
- Broken imports.
- Incorrect paths.
- Broken links.
- Database initialization.
- Exercise execution.
- Missing dependencies.
- Incompatible interfaces.

Run every exercise and record its actual pass/fail result.

Run every script created or modified.

Preserve existing generated artifacts unless their modification is explicitly required.

## **14. Phase 8: Task 1 Verification and Report**

Complete Task 1 §5 verification.

Required checks:

1. Rerun the baseline and compare against the original baseline.
2. Confirm no new failures.
3. Run every exercise, notebook, and script created or modified.
4. Check links across all curriculum files.
5. Render every visual to `/tmp/eml_visuals/`.
6. List the rendered visual paths.
7. Compare Henry Hub Git status against `/tmp/hh_status_before.txt`.
8. Confirm Henry Hub remains unchanged.

Then deliver the complete Task 1 §6 report.

Mandatory stop

**STOP after the Task 1 report. Do not begin Task 2 without explicit authorization.**

Do not commit or push changes at this stopping point.

# **PART IV. TASK 2: VISUAL SUPPLY-SIDE ECONOMICS LAYER**

Task 2 begins only after Task 1 is complete and the required authorization is received.

## **15. Phase 9: Task 2 Pre-flight**

Before editing:

1. Record Task 2 as `PENDING` in STATUS.md or the existing tracker.
2. Capture Git status.
3. Save a visual baseline to `/tmp/eml_visual_baseline_<timestamp>.txt`.
4. List the files expected to be touched.
5. Record existing visual assets and their locations.

## **16. Phase 10: Diagram Engine and Library**

Complete Task 2 §§4–7.

Build one metadata-driven diagram engine.

Reuse Henry Hub's renderer and metadata patterns by copying the relevant components and recording their original source paths.

The existing `tools/diagram_engine.py` must be inspected and tested against every drawing requirement before being reused.

Create declarative diagram specifications in YAML, JSON, or Python.

Implement all 23 diagrams, A–W.

Render every diagram to:

`/tmp/eml_visuals/`

Also render the diagrams into the curriculum at the exact paths referenced by the lessons.

Extend the diagrams to every relevant curriculum topic.

If a topic cannot be represented accurately with a simple x-y diagram, document the technical reason.

## **17. Phase 11: Supply-Side Economics Blocks**

Implement the Supply-Side Economics layer across all applicable topics and project areas specified in Task 2 §§2–3.

Applicable areas include:

- Curriculum.
- Exercises.
- Assessments.
- Market models.
- Trading simulation.
- Research.
- Reports.
- Product management.
- NGL_STUDY_GUIDE.md.

Each block must contain:

1. Two to four sentences explaining the supply-side mechanism.
2. A relevant North American market example.
3. Europe and Asia examples where the topic is global.
4. At least one x-y diagram showing the mechanism and direction of the shift.
5. A Predict-the-shift question.
6. An answer diagram showing the correct shift.
7. Text and diagrams describing exactly the same mechanism and direction.
8. Valid image links resolving to actual generated assets.

Each lesson section must contain at least one diagram, and each lesson must contain at least three diagrams.

For the 120 lesson sections, create one work queue item per section.

Each section must be individually implemented, verified, documented, and checked off.

The current state is:

- Two of 120 sections have received partial work.
- Section 6.7 contains a diagram that contradicts its text.
- Section 6.7 lacks a Predict-the-shift question.
- Both existing blocks reference a nonexistent `../../../diagrams/` directory.
- These deficiencies must be corrected before marking the sections complete.

## **18. Phase 12: Diagram Drawing Rules**

Check every diagram against every requirement.

- Short axis labels.
- No numeric ticks.
- No numeric scales.
- No grid lines.
- Original curves dashed.
- New curves solid.
- Directional arrows.
- Other relevant curves remain visible.
- Old equilibrium points marked hollow.
- New equilibrium points marked filled.
- S0/S1-style curve labels.
- No reliance on color alone.
- No legends.
- Every conceptual diagram includes the exact label `Illustrative relationship`.
- Readable at the actual size displayed in the lesson.

Every diagram must identify its evidence classification:

- Observed data.
- Model-derived.
- Illustrative.

Real data must include its source URL and retrieval date.

Shift directions must be economically and physically correct.

## **19. Phase 13: Hands-on Diagram Exercises**

Implement exercises allowing learners to:

1. Change a diagram parameter.
2. Regenerate the diagram.
3. Observe the resulting curve movement.
4. Identify the effect on price, spread, basis, or volume.
5. Verify the result against the expected output.

All exercise commands must execute successfully.

## **20. Phase 14: Coverage Matrix and Testing**

Create a coverage matrix mapping every lesson or topic to:

- Explanation.
- Market example.
- Diagram.
- Correct shift direction.
- Predict-the-shift question.
- Answer diagram.
- Any justified diagram exception.

Implement tests for:

1. Every lesson has a Supply-Side Economics block.
2. Every lesson meets the minimum diagram count.
3. Every diagram specification matches its topic.
4. Every shift direction is correct.
5. Curve styles are correct.
6. Arrow directions are correct.
7. Equilibrium is consistent with the shift.
8. Diagrams contain no ticks.
9. Every conceptual diagram contains `Illustrative relationship`.
10. Every SVG renders.
11. Every image link resolves.
12. Existing content changes only through permitted additions.

Run targeted tests, the full suite, and static checks.

Render all diagrams to `/tmp/eml_visuals/` and inspect representative examples at actual lesson size.

Rerun the baseline and compare it against the original.

Verify that Henry Hub remains unchanged.

## **21. Phase 15: Task 2 Final Report**

Complete Task 2 §10.

Deliver the complete report, including:

- Implemented features.
- Completed diagram inventory.
- Curriculum coverage.
- Exercise execution results.
- Test results.
- Baseline comparison.
- Henry Hub before-and-after comparison.
- Remaining blocked items.
- Actual verification evidence.

Then STOP.

# **PART V. ENGINEERING SPECIFICATION**

The following requirements apply throughout the implementation of Task 1 and Task 2. They supplement the sequential phases above and do not override the authoritative requirements document.

## **22. Repository Discovery and Work Ledger**

Before modifying curriculum content, perform the complete repository discovery.

Create:

`/tmp/emi_audit/`

Create:

`/tmp/emi_sandbox/`

Execute:

```
mkdir -p /tmp/emi_audit /tmp/emi_sandbox

find /root/energy_market_intelligence -maxdepth 5 | sort > /tmp/emi_audit/full_tree.txt

find /root/energy_market_intelligence -type f | sort > /tmp/emi_audit/all_files.txt

find /root/energy_market_intelligence -type f -exec wc -l {} + | sort -n > /tmp/emi_audit/line_counts.txt

wc -l /tmp/emi_audit/all_files.txt

cat /tmp/emi_audit/line_counts.txt
```

Inspect every chapter directory, from `chapter_01` through the highest numbered chapter.

Read every existing `lessons_source.txt` and `sources.md` completely.

Audit the following:

- `assessments/baseline/baseline_assessment.md`
- `assessments/baseline/baseline_answer_key.md`
- `assessments/competency_evidence/scores.csv`
- `assessments/daily/day_01_assessment.md` through `day_12_assessment.md`
- `assessments/daily/day_01_answer_key.md` through `day_12_answer_key.md`
- `assessments/final/final_assessment.md`
- `assessments/final/final_answer_key.md`
- `curriculum/chapters/chapter_XX/chapter_overview.md`
- `curriculum/chapters/chapter_XX/lessons_source.txt`
- `curriculum/chapters/chapter_XX/sources.md`
- `curriculum/chapters/chapter_XX/labs/ex*.md`
- `curriculum/chapters/chapter_XX/sections/section_01` through `section_10`
- Every corresponding `content.md` and `lessons.yaml`.

Create:

`/tmp/emi_audit/work_ledger.json`

Track every file using these statuses:

- `PENDING`
- `GENERATED`
- `AUDITED`
- `TESTED`
- `PASSED`

Update the ledger after every file is completed and tested.

## **23. Chapter Overview Requirements**

Every `chapter_overview.md` must include:

1. Chapter title and executive abstract.
2. Scope and physical/financial market context.
3. Operational relevance.
4. Prerequisites.
5. Required CLI/Python toolchain.
6. Prior chapter dependencies.
7. Comprehensive competency matrix mapping all ten sections to:
   - Quantitative objectives.
   - Mathematical equations.
   - Terminal deliverables.
8. Canonical mathematical reference.
9. Variable definitions.
10. Units and sign conventions.
11. Chapter capstone terminal workflow.

The capstone must provide an end-to-end multi-command workflow connecting all ten sections.

## **24. Section Content Requirements**

Every `content.md` must contain at least:

- 180 lines.
- 1,200 words.

Each section must follow this structure:

1. Section header.
2. Four to six measurable learning objectives.
3. Physical and financial market mechanics.
4. Market-clearing mechanisms.
5. Physical delivery constraints.
6. Contract specifications.
7. Settlement rules.
8. Counterparty and basis mechanics.
9. Mathematical formulation.
10. Full derivations.
11. Units.
12. Edge cases.
13. Boundary conditions.
14. Numerical stability considerations.
15. Worked analytical example.
16. Intermediate calculations.
17. Final numerical results.
18. Common pitfalls.
19. Unit traps.
20. Production edge cases.

Every section must contain at least three complete terminal exercises.

Each exercise must include four subsections.

**Exercise X.Y: Title and Objective**

Explain the quantitative or data-engineering problem.

**Step 1: Deterministic Data Fixture Setup**

Provide an executable, copy-pasteable shell command or inline Python script.

The command must create realistic, domain-accurate local data, including appropriate market time series, forward curves, order books, dispatch stacks, or contract schedules.

Do not rely on external URLs or nonexistent files.

**Step 2: Terminal Challenge Prompt**

Explain exactly what the learner must compute, transform, filter, join, or model.

Use appropriate CLI tools, including:

- awk
- sed
- grep
- sort
- join
- cut
- bc
- jq
- sqlite3
- duckdb
- python3
- numpy
- pandas
- scipy

**Step 3: Reference Solution Command**

Provide the complete command that solves the exercise.

**Step 4: Verified Expected Output**

Provide the exact stdout produced by executing the setup command followed by the reference solution.

## **25. lessons.yaml Requirements**

Every `lessons.yaml` must contain at least 120 lines.

It must be valid YAML and follow this structure:

```
chapter: <int>
section: <int>
title: "<string>"
estimated_minutes: <int>

prerequisites:
  - "<string>"

learning_objectives:
  - id: "LO-<ch>-<sec>-01"
    description: "<string>"
    bloom_level: "<apply|analyze|evaluate|create>"

key_formulas:
  - name: "<string>"
    expression: "<string>"
    variables:
      <var>: "<unit and definition>"

terminal_exercises:
  - id: "EX-<ch>-<sec>-01"
    title: "<string>"
    difficulty: "<foundational|intermediate|advanced>"
    tools_required: ["bash", "python3", "awk"]
    setup_command: |
      <exact runnable bash setup command>
    task_prompt: |
      <detailed terminal prompt for the learner>
    solution_command: |
      <exact runnable bash/python solution command>
    expected_output: |
      <exact verified stdout>
    validation_assertions:
      - "<automated check description>"

review_questions:
  - question: "<string>"
    answer: "<detailed technical answer>"
```

Every YAML file must contain at least three complete terminal exercises.

Each exercise must have nonempty:

- `setup_command`
- `task_prompt`
- `solution_command`
- `expected_output`

## **26. Lab Requirements**

Every lab under:

`curriculum/chapters/chapter_XX/labs/ex*.md`

must contain at least 150 lines.

Each lab must include:

1. Scenario and operational brief.
2. Complete environment description.
3. Synthetic dataset generator.
4. Multi-file deterministic datasets.
5. Five sequential terminal tasks.
6. Explicit CLI constraints for every task.
7. Complete reference solution commands.
8. Exact verified expected output.
9. An automated self-check script.

Each task must build on the artifacts generated by previous tasks.

Examples of suitable datasets include:

- Hourly LMPs.
- Gas hub basis.
- Heat rates.
- Storage inventories.
- Forward curves.
- Pipeline capacity.
- Dispatch stacks.

## **27. Assessment Requirements**

Audit and complete 100% of `assessments/`.

**Baseline assessment**

`baseline_assessment.md` and `baseline_answer_key.md` must contain 15 diagnostic problems covering:

- Energy units and conversions.
- Unix shell data manipulation.
- SQL aggregation.
- Probability and statistics.
- Python numerical computing.

Every answer must include runnable terminal verification commands and exact numerical answers.

**Daily assessments**

Create or audit:

- `day_01_assessment.md` through `day_12_assessment.md`.
- `day_01_answer_key.md` through `day_12_answer_key.md`.

Each daily assessment must contain ten rigorous problems:

- Five conceptual or quantitative derivation problems.
- Five hands-on terminal execution problems with inline data fixtures.

Each answer key must contain complete derivations, runnable CLI/Python commands, and verified stdout.

**Final assessment**

`final_assessment.md` and `final_answer_key.md` must contain 20 comprehensive capstone problems covering:

- Cross-commodity spreads.
- Curve construction.
- Risk metrics.
- Portfolio optimization.
- Automated terminal pipelines.

**Competency evidence**

Ensure `assessments/competency_evidence/scores.csv` has a valid schema containing:

- `assessment_id`
- `chapter_scope`
- `skill_domain`
- `max_score`
- `passing_threshold`
- `terminal_lab_weight`
- `verification_status`

## **28. Prohibited Patterns and Skeleton Files**

The following strings and patterns are prohibited anywhere in the repository, except valid Python ellipsis indexing and regex patterns:

- `TODO`
- `TBD`
- `FIXME`
- `XXX`
- `HACK`
- `COMING SOON`
- `PLACEHOLDER`
- `INSERT HERE`
- `TO BE ADDED`
- Prose truncation using `...`
- `# rest of code`
- `# similar to above`
- `# repeat for`
- `etc.` when used to truncate lists of rules, formulas, or steps.

No skeleton files.

Every file must meet its specified structural, content, and verification requirements.

## **29. Mandatory Sandbox Verification**

All newly authored Bash pipelines, awk/sed/jq expressions, SQL/DuckDB queries, and Python scripts must be tested in:

`/tmp/emi_sandbox/`

Execute them in an isolated environment and confirm:

- Exit code 0.
- Exact stdout parity.
- Correct generated artifacts.
- Expected behavior.

Do not publish an expected output until it has been produced by actual execution.

# **PART VI. FINAL AUTOMATED QUALITY GATE**

## **30. Mandatory Verification Script**

Create:

`/tmp/emi_audit/verify_repo.py`

Execute it and achieve 100% PASS across all six verification checks before reporting Task 2 completion.

### **Check 1: Manifest and Line-Count Floor**

Verify:

- Every repository file appears in the manifest.
- Zero empty files.
- Every `content.md` has at least 180 lines.
- Every `lessons.yaml` has at least 120 lines.
- Every `labs/ex*.md` has at least 150 lines.
- Every assessment has at least 150 lines.
- Every answer key has at least 200 lines.

### **Check 2: Prohibited Placeholder Scan**

Scan the entire repository for prohibited placeholders.

Verify zero matches for:

`TODO|TBD|FIXME|PLACEHOLDER|COMING SOON|INSERT HERE|TO BE ADDED`

Also verify that prose ellipsis truncation, defined as `...` at the end of lines outside code blocks, returns zero matches.

### **Check 3: YAML Schema and Structural Validation**

For every `lessons.yaml`:

- Parse with `yaml.safe_load()`.
- Verify the required fields.
- Verify at least three terminal exercises.
- Verify each exercise has nonempty setup, task, solution, and expected output fields.

### **Check 4: Live Execution of All YAML Exercises**

The verification script must:

1. Iterate through every `lessons.yaml`.
2. Extract every terminal exercise.
3. Create an isolated directory under `/tmp/emi_sandbox/<exercise_id>`.
4. Execute setup commands through `bash -e`.
5. Execute solution commands through `bash -e`.
6. Verify exit code 0.
7. Compare normalized stdout with the documented expected output.

Required result:

**Zero failures across all extracted exercises.**

Any failure must be corrected in the source file and retested immediately.

### **Check 5: Markdown Lab and Answer-Key Execution**

Extract runnable setup and solution code blocks from:

- `content.md`
- `labs/ex*.md`
- `*_answer_key.md`

Execute them in isolated sandbox directories.

Verify:

- Exit code 0.
- Nonempty valid output.
- Output matches the documented expected results.

### **Check 6: Final Verification Report**

The verification script must print a complete summary containing:

- Total chapters processed.
- Total sections processed.
- Total labs processed.
- Total assessments processed.
- Total curriculum and assessment lines written.
- Total YAML exercises executed.
- Total YAML exercises passed.
- Total YAML exercise failures.
- Total Markdown lab and answer-key blocks executed.
- Total Markdown lab and answer-key blocks passed.
- Total Markdown failures.
- Total prohibited placeholder matches.

Required final results:

- 100% PASS.
- Zero failed YAML exercises.
- Zero failed Markdown execution checks.
- Zero prohibited placeholder matches.
- All manifest and structural requirements satisfied.

# **PART VII. EXECUTION ORDER**

The following sequence governs all implementation work.

| Phase | Work                                 | Required stopping condition              |
| ----- | ------------------------------------ | ---------------------------------------- |
| 0     | Task 1 pre-flight                    | Pre-flight evidence recorded             |
| 1     | Baseline and gap analysis            | Baseline saved and failures documented   |
| 2     | Henry Hub reuse map                  | Reuse map written                        |
| 3     | Level and curriculum architecture    | All 12 chapters and 120 sections mapped  |
| 4     | Market coverage                      | All required market topics mapped        |
| 5     | Product-management track             | Every level covered                      |
| 6     | README/index                         | Entry point complete                     |
| 7     | Technical repair and execution       | All required exercises tested            |
| 8     | Task 1 verification and report       | STOP for authorization                   |
| 9     | Task 2 pre-flight                    | Visual baseline and file inventory saved |
| 10    | Diagram engine and A–W library       | All 23 diagrams rendered and verified    |
| 11    | Supply-Side Economics blocks         | All 120 sections individually verified   |
| 12    | Hands-on diagram exercises           | Parameter-change exercises verified      |
| 13    | Coverage matrix and testing          | All targeted and full-suite tests passed |
| 14    | Task 2 final verification and report | STOP                                     |

**Execution rules:**

- Do not skip phases.
- Do not combine unrelated work items merely to accelerate execution.
- Do not mark an item complete without actual evidence.
- Do not regenerate protected artifacts unnecessarily.
- Do not modify Henry Hub.
- Do not commit or push before the Task 1 authorization checkpoint.
- Do not begin Task 2 without explicit authorization.
- Do not report completion while any required work remains unchecked.

**The authoritative work queue remains the persistent record of execution. Every completed item must contain its actual verification evidence.**
