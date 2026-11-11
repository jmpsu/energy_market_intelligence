#!/usr/bin/env python3
"""Scaffold the repo and extract the synthetic datasets + reference labs from the brief.
Usage: python3 tools/bootstrap.py <path-to-brief.txt>"""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
L = Path(sys.argv[1]).read_text().splitlines()
DIRS = """curriculum/assessments curriculum/chapters research/original_papers research/extracted_findings
research/equations research/industry_sources data/raw data/processed data/synthetic data/reference data/schemas
market_models/natural_gas market_models/ngl market_models/electricity market_models/cross_commodity
market_models/optimization trading_simulation/positions trading_simulation/contracts
trading_simulation/forward_curves trading_simulation/dispatch trading_simulation/settlements
trading_simulation/risk trading_simulation/scenarios product_management/customer_workflows
product_management/requirements product_management/architecture product_management/roadmap
product_management/backlog product_management/kpis product_management/capstone exercises/scripts
exercises/tests exercises/expected_output exercises/completed exercises/labs assessments/baseline
assessments/daily assessments/final assessments/competency_evidence reports/daily
reports/model_validation reports/final_capstone""".split()
for d in DIRS: (ROOT / d).mkdir(parents=True, exist_ok=True)

SYN = ROOT / "data/synthetic"
is_csv = lambda s: "," in s and ", " not in s and not s.rstrip().endswith(".")
slug = lambda s: re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")
ex, i, found = None, 555, []
while i < 1139:                       # reference-example region of the brief (lines 556-1139)
    m = re.match(r"Exercise (\d{3})\.", L[i])
    if m: ex = m.group(1)
    if is_csv(L[i]) and not is_csv(L[i - 1]):
        j = i
        while j < len(L) and is_csv(L[j]): j += 1
        head = L[i - 1]
        n = re.search(r"(\w+\.csv)", head)
        name = n.group(1) if n else f"ex{ex}_{slug(head)}.csv"
        (SYN / name).write_text("\n".join(L[i:j]) + "\n"); found.append((ex, name, j - i - 1))
        i = j
    else: i += 1
# normalise the outage scenario table exactly as the brief instructs
(SYN / "ex060_market_demand_assumptions.csv").write_text(
    "scenario,demand_MW,outage_generator,outage_capacity_MW\nBaseline,5500,None,0\nOutage,5500,GAS_02,1200\n")

def block(start_pat, end_pat, frm):
    s = next(k for k in range(frm, len(L)) if re.match(start_pat, L[k]))
    e = next(k for k in range(s + 1, len(L)) if re.match(end_pat, L[k]))
    return "\n".join(L[s + 1:e]) + "\n", e
# reference lab 005 (supplied by the learner) - only BASE is repointed to this repo layout
lab5 = ROOT / "exercises/labs/exercise-005"; (lab5 / "data").mkdir(parents=True, exist_ok=True)
code, e = block(r"cat > exercises/exercise-005/run\.py", r"^PY$", 1180)
code = code.replace('BASE = ROOT / "exercises" / "exercise-005"', "BASE = Path(__file__).resolve().parent")
(lab5 / "run.py").write_text(code)
for f in ("grid_interconnections.csv", "interconnection_interfaces.csv"):
    (lab5 / "data" / f).write_text((SYN / f).read_text())
rd, _ = block(r"cat > exercises/exercise-005/README\.md", r"^EOF$", 1180); (lab5 / "README.md").write_text(rd)
# reference lab 003 (supplied by the learner) - verbatim
lab3 = ROOT / "exercises/labs/exercise-003"; (lab3 / "data").mkdir(parents=True, exist_ok=True)
d, e = block(r"cat > data/flow_events\.csv", r"^CSV$", 2090); (lab3 / "data/flow_events.csv").write_text(d)
d, e = block(r"cat > data/market_assumptions\.csv", r"^CSV$", e); (lab3 / "data/market_assumptions.csv").write_text(d)
d, e = block(r"cat > run\.py", r"^PY$", e); (lab3 / "run.py").write_text(d)
for f in ("flow_events.csv", "market_assumptions.csv"):
    (SYN / f"ex003_{f}").write_text((lab3 / "data" / f).read_text())
for r in found: print(*r)
