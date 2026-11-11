# EX-NNN: <title>            Tier <1|2|3> | Chapter <n> | Lessons <Lcc.ss.n, ...> | Depends on <EX-...>

1. Commercial scenario - role, organisation, business problem, the decision to be made
2. What you will build - directory tree of inputs, code, outputs
3. Data - every input file, units, identifiers, provenance class (synthetic | public | licensed)
4. Analytical model - equations, sign conventions, algorithm, stated assumptions
5. Implementation - code location (exercises/scripts/exNNN.py, market_models/...), what is reused
6. Execution - exact commands from the repo root, in order
7. Expected results - numbers with tolerances, each with its hand derivation; automated test name
8. Interpretation - what the result says about the market mechanism; when the model misleads
9. Professional workflow - who does this, when, in which system, handing off to whom
10. Product-management connection - capability, data requirement, acceptance criterion, KPI
11. Deliverables - artifacts written, and which later exercises consume them
12. Completion test - a changed input or new scenario the learner must run and explain unaided
13. Instructor answer key - separate from the learner section

Output contract (enforced by exercises/scripts/common.finish):
- exercises/completed/exNNN/*.csv, report.md, *.png
- exercises/expected_output/exNNN.txt, first line carries the SYNTHETIC label
- run(**overrides) returns a dict of named results; tests in exercises/tests assert against hand-derived values
