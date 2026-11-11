#!/usr/bin/env python3
"""Energy Market Intelligence CLI.  emi.py list | run <id>|all [key=value ...] | test | status
Overrides (e.g. emi.py run 038 gas_price=5) print a scenario result and save nothing."""
import os, sys, importlib, subprocess, yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parent; S = ROOT / "exercises/scripts"; sys.path.insert(0, str(S))
mods = sorted(p.stem for p in S.glob("ex[0-9]*.py")) + ["ng_001_basis"]
def labs():
    for lab, ops in (("exercise-005", ["validate", "analyze", "report", "test"]), ("exercise-003", [None])):
        for op in ops: subprocess.run([sys.executable, str(ROOT / "exercises/labs" / lab / "run.py")] + ([op] if op else []), check=True, stdout=subprocess.DEVNULL)
        print(f"lab {lab}: OK")
cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
if cmd == "list": print("\n".join(f"{m:14s} {(importlib.import_module(m).__doc__ or '').splitlines()[0]}" for m in mods))
elif cmd == "run":
    kw = {}
    for a in sys.argv[3:]:
        k, v = a.split("=", 1)
        try: kw[k] = float(v)
        except ValueError: kw[k] = v
    if kw: os.environ["EMI_SCENARIO"] = "1"
    for m in (mods if sys.argv[2] == "all" else [sys.argv[2] if sys.argv[2].startswith(("ex", "ng")) else f"ex{int(sys.argv[2]):03d}"]): importlib.import_module(m).run(**kw); print()
    if sys.argv[2] == "all": labs()
elif cmd == "test": sys.exit(subprocess.call([sys.executable, "-m", "unittest", "discover", "-s", str(ROOT / "exercises/tests"), "-v"]))
elif cmd == "status":
    e = yaml.safe_load((ROOT / "curriculum/exercise_delivery_sequence.yaml").read_text())["exercises"]
    for t in (1, 2, 3): print(f"tier {t}: {sum(x['tier']==t and x['status']!='not_started' for x in e)}/{sum(x['tier']==t for x in e)} implemented")
