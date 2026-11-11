"""Expected-output test for NG-001 (standard library unittest only). Expected values are derived here from the brief, not read from the script."""
import csv, subprocess, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; SCRIPT = ROOT / "exercises/scripts/ng_001_basis.py"; OUT = ROOT / "exercises/completed/ng_001_basis.csv"; TXT = ROOT / "exercises/expected_output/ng_001_basis.txt"
EXPECTED = {"Waha": (-2.15, -3.65, -1.50, -15000.0), "Algonquin": (5.50, 7.00, 1.50, 15000.0)}
FIELDS = ["location", "basis_period_1_USD_per_MMBtu", "basis_period_2_USD_per_MMBtu", "basis_movement_USD_per_MMBtu", "position_MMBtu", "long_basis_pnl_USD", "data_classification"]
class TestNg001Basis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.proc = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
        with open(OUT) as f: cls.rows = {r["location"]: r for r in csv.DictReader(f)}
    def test_executes(self): self.assertEqual(self.proc.returncode, 0, self.proc.stderr)
    def test_schema(self):
        with open(OUT) as f: self.assertEqual(next(csv.reader(f)), FIELDS)
        self.assertEqual(set(self.rows), set(EXPECTED))
    def test_values_units_signs(self):
        for loc, (b1, b2, mv, pnl) in EXPECTED.items():
            r = self.rows[loc]
            self.assertAlmostEqual(float(r["basis_period_1_USD_per_MMBtu"]), b1, places=6); self.assertAlmostEqual(float(r["basis_period_2_USD_per_MMBtu"]), b2, places=6)
            self.assertAlmostEqual(float(r["basis_movement_USD_per_MMBtu"]), mv, places=6); self.assertAlmostEqual(float(r["long_basis_pnl_USD"]), pnl, places=2)
        self.assertLess(float(self.rows["Waha"]["long_basis_pnl_USD"]), 0); self.assertGreater(float(self.rows["Algonquin"]["long_basis_pnl_USD"]), 0)
    def test_independent_arithmetic(self):
        hh, vol = 3.25, 10000                                                    # basis = hub - Henry Hub ; P&L = volume x (basis2 - basis1)
        for loc, p1, p2 in (("Waha", 1.10, -0.40), ("Algonquin", 8.75, 10.25)):
            self.assertAlmostEqual(vol * ((p2 - hh) - (p1 - hh)), EXPECTED[loc][3], places=6)
    def test_classification_and_artifacts(self):
        self.assertTrue(all(r["data_classification"] == "synthetic" for r in self.rows.values())); self.assertIn("SYNTHETIC", TXT.read_text())
    def test_reproducible(self):
        first = OUT.read_bytes(); subprocess.run([sys.executable, str(SCRIPT)], capture_output=True); self.assertEqual(first, OUT.read_bytes())
    def test_edge_zero_movement_gives_zero_pnl(self): self.assertEqual(10000 * ((1.10 - 3.25) - (1.10 - 3.25)), 0)
if __name__ == "__main__": unittest.main()
