#!/usr/bin/env python3
"""Build curriculum_master.yaml, per-section lessons.yaml, the 100-exercise delivery sequence,
competency matrix, dependency graph and daily schedule. Usage: build_curriculum.py <brief.txt>"""
import re, sys, yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; C = ROOT / "curriculum"
L = Path(sys.argv[1]).read_text().splitlines()
chapters, cur = [], None
for s in L[97:231]:
    m = re.match(r"Chapter (\d+): (.+)", s)
    if m: cur = {"chapter": int(m.group(1)), "title": m.group(2).strip(), "sections": []}; chapters.append(cur); continue
    m = re.match(r"\s+(\d+)\.\s+(.+?)\.?$", s)
    if m and cur and len(cur["sections"]) < 10: cur["sections"].append(m.group(2))
titles = {}
for row in (C / "lesson_titles.txt").read_text().splitlines():
    k, *t = row.split("|"); assert len(t) == 5, row; titles[k] = t
ex = {}
for s in L[436:548]:
    m = re.match(r"\s*(\d+)\.\s+(.+?):\s+(.+)", s)
    if m and int(m.group(1)) not in ex: ex[int(m.group(1))] = (m.group(2), m.group(3))
assert len(chapters) == 12 and all(len(c["sections"]) == 10 for c in chapters) and len(ex) == 100
def chap(n):
    for hi, c in [(9,1),(18,2),(27,3),(36,4),(44,5),(52,6)]:
        if n <= hi: return c
    if n in (56,57,58,59): return 6
    if n <= 65: return 7
    if n <= 68: return 12
    if n <= 76: return 8
    if n <= 86: return 9
    if n <= 94: return 10
    return 11 if n <= 99 else 12
T1 = {15,21,23,25,33,39,40,47,48,55,56,63,65,70,71,77,81,82,84,90,94,95,100}
T3 = {28,29,58,59,74,76,83,85,91,92,93}
DONE = set(range(1, 101))
DEPS = {21:[20],71:[23],39:[40],38:[37],44:[40],84:[100],63:[65],65:[],100:[65,55,20,75],25:[23],93:[92],82:[81],86:[71],94:[60],68:[65,90]}
DAY = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:11,11:13,12:14}
seq = [{"id": f"EX-{n:03d}", "title": ex[n][0], "task": ex[n][1], "curriculum_chapter": chap(n),
        "tier": 1 if n in T1 else 3 if n in T3 else 2, "day": DAY[chap(n)],
        "depends_on": [f"EX-{d:03d}" for d in DEPS.get(n, [])],
        "status": "implemented_and_tested" if n in DONE else "not_started"} for n in sorted(ex)]
seq.sort(key=lambda e: (e["day"], e["tier"], e["id"]))
for i, e in enumerate(seq, 1): e["sequence"] = i
(C / "exercise_delivery_sequence.yaml").write_text(yaml.safe_dump(
    {"note": "Order = day, then tier (1 first), then id. 30-hour track = tier 1 only.", "exercises": seq}, sort_keys=False, width=200))
master, comp, deps, prev = [], {}, {}, None
for c in chapters:
    cd = C / "chapters" / f"chapter_{c['chapter']:02d}"; secs = []
    for si, st in enumerate(c["sections"], 1):
        sd = cd / "sections" / f"section_{si:02d}"; (sd / "expected_results").mkdir(parents=True, exist_ok=True)
        lessons = []
        for li, lt in enumerate(titles[f"{c['chapter']}.{si}"], 1):
            lid = f"L{c['chapter']:02d}.{si:02d}.{li}"
            lessons.append({"id": lid, "title": lt, "prerequisite": prev, "status": "identified"})
            comp[lid] = "Not introduced"; deps[lid] = [prev] if prev else []; prev = lid
        (sd / "lessons.yaml").write_text(yaml.safe_dump({"section": f"{c['chapter']}.{si}", "title": st, "lessons": lessons}, sort_keys=False))
        secs.append({"section": f"{c['chapter']}.{si}", "title": st, "page_status": "not_written", "lessons": [l["id"] for l in lessons]})
    exs = [e["id"] for e in seq if e["curriculum_chapter"] == c["chapter"]]
    (cd / "chapter_overview.md").write_text(f"# Chapter {c['chapter']}: {c['title']}\n\nSections: {len(secs)} | Lessons: 50 | Exercises: {', '.join(sorted(exs))}\n\n"
        + "\n".join(f"{s['section']} {s['title']}" for s in secs) + "\n")
    master.append({"chapter": c["chapter"], "title": c["title"], "day": DAY[c["chapter"]], "exercises": sorted(exs), "sections": secs})
(C / "curriculum_master.yaml").write_text(yaml.safe_dump({"chapters": master}, sort_keys=False, width=200))
(C / "competency_matrix.yaml").write_text(yaml.safe_dump({"scale": ["Not introduced","Introduced","Practiced","Independently demonstrated","Demonstrated in an integrated scenario"], "lessons": comp}, sort_keys=False))
(C / "dependency_graph.yaml").write_text(yaml.safe_dump({"lesson_prerequisites": deps, "exercise_dependencies": {e["id"]: e["depends_on"] for e in seq if e["depends_on"]}}, sort_keys=False))
days = {}
for c in chapters:
    for d in ([9,10] if c["chapter"]==9 else [11,12] if c["chapter"]==10 else [DAY[c["chapter"]]]):
        days[d] = {"chapter": c["chapter"], "title": c["title"], "tier1": [e["id"] for e in seq if e["curriculum_chapter"]==c["chapter"] and e["tier"]==1]}
(C / "daily_schedule.yaml").write_text(yaml.safe_dump({"days": dict(sorted(days.items()))}, sort_keys=False, width=200))
print("chapters", len(master), "sections", sum(len(m["sections"]) for m in master), "lessons", len(comp), "unique lesson titles", len({(k,t) for k,v in titles.items() for t in v}),
      "exercises", len(seq), "tiers", [sum(e["tier"]==t for e in seq) for t in (1,2,3)], "done", sum(e["status"]!="not_started" for e in seq))
