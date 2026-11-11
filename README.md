# energy_market_intelligence

All data under data/synthetic is SYNTHETIC and hypothetical. None of it is historical market data.

    python3 tools/bootstrap.py <brief.txt>        # scaffold + extract datasets + reference labs from the brief
    python3 tools/make_synthetic.py               # extra synthetic datasets
    python3 tools/build_curriculum.py <brief.txt> # 12 chapters / 120 sections / 600 lessons / 100-exercise sequence
    python3 emi.py list | run all | run 048 | test | status

Requires: python3, pandas, numpy, scipy, matplotlib, networkx, pyyaml.

Layout: curriculum/ (architecture), data/synthetic (inputs), market_models/ (reusable models), exercises/scripts (one file per
exercise), exercises/labs (the two supplied reference labs 005 and 003), exercises/tests (unittest), exercises/completed and
exercises/expected_output (artifacts), product_management/, reports/, trading_simulation/. See STATUS.md for what exists and what does not.
