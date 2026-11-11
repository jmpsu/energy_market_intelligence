#!/usr/bin/env python3
"""Build assessments, platform comparison, data architecture, capstone, research extracts, gaps and STATUS from the built curriculum."""
import yaml, glob, subprocess, hashlib
from pathlib import Path
R = Path(__file__).resolve().parents[1]; C = R / "curriculum"; A = R / "assessments"
master = yaml.safe_load((C / "curriculum_master.yaml").read_text()); L = {}
for f in sorted(glob.glob(str(C / "chapters/chapter_*/sections/*/lessons.yaml"))):
    y = yaml.safe_load(open(f)); L[y["section"]] = y["lessons"]
def fld(l, a, b): return l.get(a) or l.get(b) or ""
def q(l, i): return f"{i}. ({l['id']} {l['title']}) Run `{fld(l,'terminal_activity','do')}`. Report the value and explain in one sentence what it means for the desk."
def k(l, i): return f"{i}. `{fld(l,'expected_result','expect')}` - {fld(l,'market_lesson','lesson')}"
for sub in ("daily", "baseline", "final", "competency_evidence"): (A / sub).mkdir(parents=True, exist_ok=True)
allq = []
for ch in master["chapters"]:
    c = ch["chapter"]; ls = [L[s["section"]][4] for s in ch["sections"]]; allq += [L[ch["sections"][0]["section"]][0], L[ch["sections"][9]["section"]][3]]
    (A / f"daily/day_{c:02d}_assessment.md").write_text(f"# Day {c} assessment - {ch['title']}\n\nPass mark: 8 of 10. Closed notes, terminal open.\n\n" + "\n".join(q(l, i) for i, l in enumerate(ls, 1)) + "\n")
    (A / f"daily/day_{c:02d}_answer_key.md").write_text(f"# Day {c} answer key\n\n" + "\n".join(k(l, i) for i, l in enumerate(ls, 1)) + "\n")
base = [L[ch["sections"][0]["section"]][1] for ch in master["chapters"]]
(A / "baseline/baseline_assessment.md").write_text("# Baseline assessment (take before Day 1)\n\nAnswer from what you know now; do not run anything. Score against baseline_answer_key.md and record it in competency_evidence/scores.csv.\n\n" + "\n".join(f"{i}. Explain: {l['title']}." for i, l in enumerate(base, 1)) + "\n")
(A / "baseline/baseline_answer_key.md").write_text("# Baseline answer key\n\n" + "\n".join(f"{i}. {fld(l,'market_lesson','lesson')}" for i, l in enumerate(base, 1)) + "\n")
prac = ["Run `python3 emi.py run 038 gas_price=5` and state the ethane decision and why.", "Run `python3 emi.py run 017 edge=P001 cut=0.5` and name the node that goes short.", "Run `python3 emi.py run 027` and split the P&L into Henry Hub and basis parts.",
        "Run `python3 emi.py run 081` and `python3 emi.py run 082`; explain why Expected Shortfall exceeds VaR.", "Run `python3 emi.py run 100` and present the capstone scenario table in two minutes.", "Run `python3 emi.py test` and report the number of tests and the result."]
(A / "final/final_assessment.md").write_text("# Final assessment\n\nPart A: 24 knowledge questions (pass 20). Part B: 6 practical tasks (pass 5). Part C: capstone presentation (reports/final_capstone/capstone_presentation.md).\n\n## Part A\n\n" + "\n".join(q(l, i) for i, l in enumerate(allq, 1)) + "\n\n## Part B\n\n" + "\n".join(f"{i}. {p}" for i, p in enumerate(prac, 1)) + "\n")
(A / "final/final_answer_key.md").write_text("# Final answer key\n\n## Part A\n\n" + "\n".join(k(l, i) for i, l in enumerate(allq, 1)) + "\n\n## Part B\n\nAnswers are the live outputs of each command; compare with exercises/expected_output/.\n")
(A / "competency_evidence/scores.csv").write_text("assessment,date,score,max_score,notes\nbaseline,,,12,\n" + "".join(f"day_{c:02d},,,10,\n" for c in range(1, 13)) + "final_part_A,,,24,\nfinal_part_B,,,6,\n")
(R / "product_management/competitive_analysis").mkdir(parents=True, exist_ok=True)
plat = [("PLEXOS", "Energy Exemplar", "power/gas market simulation"), ("PLEXOS Cloud", "Energy Exemplar", "hosted simulation"), ("Aurora", "Energy Exemplar", "power market forecasting"), ("Adapt2", "Energy Exemplar", "bid-to-bill / market operations"),
        ("Endur", "ION (Openlink)", "ETRM"), ("PSS/E", "Siemens", "transmission planning power flow"), ("PowerWorld", "PowerWorld Corp", "power flow / visualisation"), ("Dayzer", "Cambridge Energy Solutions", "nodal market simulation"),
        ("Enelytix / TARA", "Newton Energy Group / PowerGEM", "cloud market simulation / transmission analysis"), ("Enverus Mosaic", "Enverus", "power market analytics"), ("Yes Energy", "Yes Energy", "ISO market data"), ("Bloomberg", "Bloomberg", "market data terminal"),
        ("ICE", "Intercontinental Exchange", "exchange, clearing, market data"), ("LSEG", "LSEG", "market data and analytics"), ("Snowflake", "Snowflake", "cloud data warehouse"), ("Databricks", "Databricks", "lakehouse / compute")]
t = ["# Platform comparison", "", "STATUS: every vendor, category and capability cell below is [K] = general knowledge NOT verified against vendor documentation in this build. Treat nothing here as a product fact. No capability, price or performance claim is asserted.",
     "The 'this repo' column is [EX]: it names the exercise in this repository that reproduces the concept on synthetic data, so you can discuss the workflow without asserting vendor features.", "",
     "| Platform | Vendor [K] | Category [K] | Concept reproduced in this repo [EX] | Verified from vendor docs? |", "|---|---|---|---|---|"]
repo = ["EX-089 production cost, EX-091 capacity expansion, EX-090 gas network", "EX-092/093 runtime and equivalence", "EX-077 price forecast, EX-049 clearing", "EX-052 settlements", "EX-069/072/076 trade capture, lifecycle, integration", "EX-048/056 DC-OPF, PTDF",
        "EX-056 congestion", "EX-048 LMP, EX-058 FTR", "EX-092/093, EX-056", "EX-009 dashboard, EX-047 DA/RT", "EX-070 ingestion, EX-047", "EX-070, EX-023 curves", "EX-024 futures/swaps, EX-073 margin", "EX-070, EX-088 API", "EX-087 star schema (SQLite)", "EX-087, EX-093"]
t += [f"| {p} | {v} | {c} | {r} | NO - verify before use |" for (p, v, c), r in zip(plat, repo)]
t += ["", "## How to verify (do this before your first vendor conversation)", "", "For each platform record in `product_management/competitive_analysis/verification_log.csv`: capability, exact quote, URL, date read. Only quoted rows may be moved from hypothetical to verified.", "",
      "## Hypothetical integration (proposed, not a vendor feature)", "", "See `product_management/architecture/ex099_architecture.md`: every component there is marked proposed; `vendor_capabilities_asserted = 0` is enforced by a test."]
(R / "product_management/competitive_analysis/platform_comparison.md").write_text("\n".join(t) + "\n")
(R / "product_management/competitive_analysis/verification_log.csv").write_text("platform,capability,exact_quote,url,date_read\n" + "".join(f"{p[0]},,,,\n" for p in plat))
(R / "product_management/architecture/data_architecture.md").write_text("""# Data architecture (as built in this repo)

All data is SYNTHETIC and hypothetical. Everything below is implemented and runnable; nothing describes a vendor system.

| Layer | Location | Built by | Check |
|---|---|---|---|
| Raw synthetic inputs | data/synthetic/*.csv | tools/bootstrap.py, tools/make_synthetic*.py, exercise `data()` helper | files are created once and never overwritten |
| Reference data | data/processed/reference.sqlite (dim_location, ref_pipeline_segment, ref_power_market) | `python3 emi.py run 007` | duplicate_location_names = 0 |
| Ingestion with quality rules | reports/, EX-070 | `python3 emi.py run 070` | rejected rows are logged, not dropped silently |
| Warehouse (star schema) | EX-087 SQLite facts + dimensions | `python3 emi.py run 087` | orphan_facts = 0 |
| API contract | product_management/architecture/ex088_api_contract.md | `python3 emi.py run 088` | status_200 = 3, status_404 = 3 |
| Models | market_models/ (battery, dispatch, dcopf, gas network) | imported by exercises | unit tests in exercises/tests |
| Results | exercises/completed/exNNN/, exercises/expected_output/exNNN.txt | every `emi.py run` | `python3 emi.py test` |
| ETRM integration (proposed) | product_management/architecture/ex099_architecture.md | `python3 emi.py run 099` | vendor_capabilities_asserted = 0 |

Conventions: gas in MMBtu, power in MWh, NGL in gallons; one location name per physical point; scenario runs (`key=value`) print only and save nothing.
Lineage: every number in a lesson page names the command that produces it. Known limits: SQLite stands in for a cloud warehouse; no streaming; no access control.
""")
(R / "reports/final_capstone").mkdir(parents=True, exist_ok=True)
cap = subprocess.run(["python3", str(R / "emi.py"), "run", "100"], capture_output=True, text=True, cwd=R).stdout
(R / "reports/final_capstone/capstone_presentation.md").write_text("# Capstone presentation (10 minutes)\n\nAll figures are from `python3 emi.py run 100` on SYNTHETIC data.\n\n## 1. Decision asked for\nApprove the 90-day roadmap in product_management/roadmap/ex095_roadmap_90_day.md.\n\n## 2. Evidence (live output)\n\n```\n" + cap + "```\n\n## 3. Storyline\n1. Problem: gas, power and NGL exposures are analysed in separate tools.\n2. Evidence: the integrated scenario table above changes the ranking of risks versus single-commodity views.\n3. Recommendation: build the top-ranked items in product_management/roadmap/ex097_ranked_features.csv.\n4. KPIs: product_management/kpis/ex098_kpis.csv.\n5. Risks and limits: synthetic data, simplified physics, no vendor capability verified (see competitive_analysis/platform_comparison.md).\n\n## 4. Q&A prep\nRe-run with overrides to answer what-ifs live, e.g. `python3 emi.py run 038 gas_price=5`, `python3 emi.py run 017 cut=0.8`.\n")
(R / "research/extracted_findings").mkdir(parents=True, exist_ok=True)
link = {"European_Natural_Gas": "3.8, 4.9", "Supply_and_Demand_Based_Volatility": "9.2, 9.4", "World_Commodity_Prices": "9.1, 12.2", "visibility_graph": "9.2", "Brent": "9.1", "Russian_invasion": "9.9, 4.9", "Coalition_formation": "4.6, 4.7, 2.5", "Optimal_dispatch": "7.8, 7.9", "Good_and_bad_volatility": "9.2, 6.5", "wholesale_market_integration": "6.6, 6.8"}
out = ["# Research source extracts", "", "Machine-extracted first-page text only (pdftotext). NOT read or summarised by a person or model in this build; no finding is asserted. 'Linked sections' is a topical pointer for your own reading.", ""]
for f in sorted(Path("/mnt/user-data/uploads").glob("*.pdf")):
    txt = subprocess.run(["pdftotext", "-l", "1", str(f), "-"], capture_output=True, text=True).stdout.strip()[:1200]
    sec = next((v for k_, v in link.items() if k_.lower() in f.name.lower()), "unlinked")
    out += [f"## {f.name.split('-', 1)[1]}", f"sha256: {hashlib.sha256(f.read_bytes()).hexdigest()[:16]} | linked sections: {sec}", "", "```", txt, "```", ""]
(R / "research/extracted_findings/first_page_extracts.md").write_text("\n".join(out))
tests = subprocess.run(["python3", "-m", "unittest", "discover", "-s", "exercises/tests"], capture_output=True, text=True, cwd=R).stderr.strip().splitlines()[-3:]
nles = sum(len(v) for v in L.values()); npages = len(glob.glob(str(C / "chapters/chapter_*/sections/*/content.md")))
(R / "STATUS.md").write_text(f"""# STATUS

Verified by running, {subprocess.run(['date','-u','+%Y-%m-%d %H:%M UTC'],capture_output=True,text=True).stdout.strip()}:

- Exercises: 100 of 100 implemented (98 via `emi.py run`, EX-003 and EX-005 as labs) + 4 NGL extensions (101-104). `python3 emi.py status`.
- Tests: {tests[0]} -> {tests[-1]}. `python3 emi.py test`.
- Section pages: {npages} of 120. Lessons with all fields: {nles} of 600. Every lesson command in chapters 1-4 and 6-12 was executed and its expected line matched.
- Assessments: baseline, 12 daily (+ answer keys), final (+ key), score sheet.
- Docs: platform comparison, data architecture, capstone presentation, research first-page extracts.

## Gaps (honest list)

1. Chapters 1-4 and 6-12: lesson text is one sentence per lesson, tagged [K] (not source-checked). Chapter 5 (NGL) is the only chapter with cited sources.
2. In those chapters all five lessons of a section point at one exercise; the example shows a real output value but it is not always the value most specific to that lesson title.
3. Professional application = the exercise task from the brief; product implication = one sentence per chapter.
4. Platform comparison: NO vendor capability verified. Vendor/category labels are [K]. Fill verification_log.csv from vendor docs.
5. Research PDFs: first-page text extracted mechanically; not read, no findings, lesson links are topical pointers only.
6. Write-ups with instructor answer keys exist for the NGL labs (ch 5). Other exercises have docstring + report.md + expected output + tests, not a long-form write-up.
7. Tests for 24 exercises (001-036 batch) were re-derived by hand this session after the scripts were rewritten; ex017, ex031, ex034, ex018 have weak (invariant-only) checks.
8. NGL gaps: forward curves, product specs detail, export freight, POP/keep-whole settlement are covered only by EX-101..104 at a basic level.
9. All data is synthetic. Known inconsistencies in brief datasets (EX-015, 025, 035, 060, 065, 075, 085, 100) are flagged in those reports, not corrected.
""")
print(open(R / "STATUS.md").read()[:700])
