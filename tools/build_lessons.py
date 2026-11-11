#!/usr/bin/env python3
"""Build section pages + full lesson fields for chapters 1-4 and 6-12 from curriculum/lesson_src/*.txt (sec|exercise|5 lesson sentences).
Example/expected values are read from exercises/expected_output/exNNN.txt (produced by running the exercise). Chapter 5 is built by build_chapter05.py."""
import yaml, re
from pathlib import Path
R = Path(__file__).resolve().parents[1]; C = R / "curriculum"
titles = {l.split("|")[0]: l.strip().split("|")[1:] for l in (C / "lesson_titles.txt").read_text().splitlines() if l.strip()}
master = yaml.safe_load((C / "curriculum_master.yaml").read_text()); ex = {x["id"][3:]: x for x in yaml.safe_load((C / "exercise_delivery_sequence.yaml").read_text())["exercises"]}
PROD = {1: "A market-intelligence product needs one reference model of participants, locations and units before any analytics.", 2: "Physical gas data (capacity, storage, nominations) is the raw input customers expect a product to load and reconcile.",
 3: "Basis, curves and position views are the core screens of a gas trading product; every number must trace to a price source.", 4: "Network and scenario features sell when users can change one constraint and see flows and basis respond.",
 6: "Power-market products are judged on nodal price accuracy and on explaining congestion, not on averages.", 7: "Asset models must respect operating constraints or customers will not trust dispatch and margin outputs.",
 8: "ETRM integration is where products succeed or fail: trade, price and position interfaces need explicit data contracts.", 9: "Risk features need transparent methods and reproducible numbers; a black-box VaR is not accepted by a middle office.",
 10: "Simulation speed and result equivalence are product features: faster runs only count if the answers are proven unchanged.", 11: "Every roadmap item should cite customer evidence and a measurable KPI.", 12: "Integrated gas-power-NGL scenarios are the differentiator for a cross-commodity product; they depend on all earlier chapters."}
def results(n):
    f = R / f"exercises/expected_output/ex{n}.txt"; out = []
    for l in f.read_text().splitlines():
        m = re.match(r"^([A-Za-z0-9_.\-]+): (.+)$", l)
        if m and m.group(1) != "NOTE" and not re.search(r"speedup|seconds|runtime|_ms$|elapsed|database", m.group(1)): out.append(m.groups())
    return out
rows = {}
for f in sorted((C / "lesson_src").glob("*.txt")):
    for l in f.read_text().splitlines():
        p = l.split("|"); rows[p[0]] = (p[1], p[2:])
ids = [f"L{int(s.split('.')[0]):02d}.{int(s.split('.')[1]):02d}.{n}" for s in titles for n in range(1, 6)]
count = 0
for ch in master["chapters"]:
    c = ch["chapter"]
    if c == 5: continue
    for sec in ch["sections"]:
        s = sec["section"]; n, sent = rows[s]; res = results(n); e = ex[n]; d = C / f"chapters/chapter_{c:02d}/sections/section_{int(s.split('.')[1]):02d}"; d.mkdir(parents=True, exist_ok=True)
        md = [f"# {s} {sec['title']}", "", "Evidence tags: [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it.", "",
              f"Section exercise: EX-{n} {e['title']} (`python3 emi.py run {n}`). Full output: `exercises/completed/ex{n}/report.md`.", ""]; ls = []
        for i, (t, txt) in enumerate(zip(titles[s], sent), 1):
            lid = f"L{c:02d}.{int(s.split('.')[1]):02d}.{i}"; k = ids.index(lid); key, val = res[(i - 1) % len(res)]
            L = {"id": lid, "title": t, "objective": f"Explain {t[0].lower() + t[1:]} and show it in the EX-{n} output.", "prerequisites": [ids[k - 1]] if k else [], "market_lesson": txt + " [K]",
                 "north_american_example": f"EX-{n} ({e['title']}) on synthetic North American data: {key} = {val} [EX]", "terminal_activity": f"python3 emi.py run {n} | grep '^{key}:'", "expected_result": f"{key}: {val}",
                 "professional_application": e["task"], "product_implication": PROD[c], "before": ids[k - 1] if k else None, "after": ids[k + 1] if k + 1 < len(ids) else None, "status": "written_command_verified"}
            ls.append(L); count += 1
            md += [f"## {lid} {t}", "", f"**Objective.** {L['objective']}", "", f"**Prerequisites.** {L['prerequisites'][0] if k else 'none'}", "", f"**Lesson.** {L['market_lesson']}", "", f"**Example.** {L['north_american_example']}", "",
                   f"**Do.** `{L['terminal_activity']}`", "", f"**Expect.** `{L['expected_result']}`", "", f"**On the job.** {L['professional_application']}", "", f"**Product implication.** {L['product_implication']}", "", f"Before: {L['before']} | After: {L['after']}", ""]
        (d / "content.md").write_text("\n".join(md)); (d / "lessons.yaml").write_text(yaml.safe_dump({"section": s, "title": sec["title"], "exercise": f"EX-{n}", "lessons": ls}, sort_keys=False, width=1000)); sec["page_status"] = "written"
(C / "curriculum_master.yaml").write_text(yaml.safe_dump(master, sort_keys=False, width=1000)); print(count, "lessons written")
