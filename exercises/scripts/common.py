"""Shared helpers for all exercise scripts. All inputs under data/synthetic are SYNTHETIC, hypothetical data."""
import os, sys, sqlite3
from pathlib import Path
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0, str(ROOT))
SYN, DONE, EXP, PROC = ROOT / "data/synthetic", ROOT / "exercises/completed", ROOT / "exercises/expected_output", ROOT / "data/processed"
MMBTU_PER_BCF = 1_000_000   # simplification: 1 Mcf = 1 MMBtu (EX-003 uses 1.037)
LABEL = "SYNTHETIC HYPOTHETICAL DATA - not historical market data"

def load(name): return pd.read_csv(SYN / name)

def params(name):
    out = {}
    for k, v in load(name).set_index("parameter")["value"].items():
        try: out[k] = float(v)
        except ValueError: out[k] = v
    return out

def chart(ex, name, df, x, ys, kind="line", title=""):
    if os.environ.get("EMI_SCENARIO"): return
    ax = df.plot(x=x, y=ys, kind=kind, figsize=(9, 4.5), title=f"{title} ({LABEL.split(' - ')[0].title()})")
    ax.figure.tight_layout(); d = DONE / ex; d.mkdir(parents=True, exist_ok=True); ax.figure.savefig(d / f"{name}.png", dpi=130); plt.close(ax.figure)

def finish(ex, results, frames=None, notes=()):
    """Persist artifacts: completed/<ex>/*.csv, completed/<ex>/report.md, expected_output/<ex>.txt; print the result block."""
    scenario = bool(os.environ.get("EMI_SCENARIO")); d = DONE / ex; d.mkdir(parents=True, exist_ok=True)
    for n, f in ({} if scenario else (frames or {})).items(): f.to_csv(d / f"{n}.csv", index=False)
    fmt = lambda v: f"{v:.6f}".rstrip("0").rstrip(".") if isinstance(v, (float, np.floating)) else str(v)
    lines = [f"{ex} | {LABEL}"] + [f"{k}: {fmt(v)}" for k, v in results.items()] + [f"NOTE: {n}" for n in notes]
    text = "\n".join(lines) + "\n"
    if scenario: print("[SCENARIO RUN - nothing saved]\n" + text, end=""); return results
    (EXP / f"{ex}.txt").write_text(text); (d / "report.md").write_text("# " + text.replace("\n", "\n\n"))
    print(text, end=""); return results

def data(name, text):
    """Inline SYNTHETIC dataset: written to data/synthetic/<name> on first use so it persists and can be edited, then read back."""
    p = SYN / name
    if not p.exists(): p.write_text("\n".join(l.strip() for l in text.strip().splitlines()) + "\n")
    return pd.read_csv(p)

def quiet(fn, *a, **k):
    import contextlib, io
    with contextlib.redirect_stdout(io.StringIO()): return fn(*a, **k)

def sql(db, query):
    con = sqlite3.connect(PROC / db)
    try: return pd.read_sql_query(query, con)
    finally: con.close()

def data(name, text):
    """Create a SYNTHETIC dataset under data/synthetic on first use (so it is persistent and editable) and load it."""
    p = SYN / name
    if not p.exists(): p.write_text(text.strip() + "\n")
    return pd.read_csv(p)
