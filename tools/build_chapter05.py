#!/usr/bin/env python3
"""Build Chapter 5 (NGL): 10 section pages, enriched lessons.yaml, 8 lab write-ups with answer keys, sources, and NGL_STUDY_GUIDE.md."""
import yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; CH = ROOT / "curriculum/chapters/chapter_05"
SRC = {"S1": ("EIA, Hydrocarbon gas liquids explained", "https://eia.gov/energyexplained/hydrocarbon-gas-liquids/"),
 "S2": ("EIA, Uses of hydrocarbon gas liquids", "https://www.eia.gov/energyexplained/hydrocarbon-gas-liquids/uses-of-hydrocarbon-gas-liquids.php"),
 "S3": ("EIA, Where do hydrocarbon gas liquids come from", "https://www.eia.gov/energyexplained/hydrocarbon-gas-liquids/where-do-hydrocarbon-gas-liquids-come-from-in-depth.php"),
 "S4": ("EIA, Transporting and storing hydrocarbon gas liquids", "https://www.eia.gov/energyexplained/hydrocarbon-gas-liquids/transporting-and-storing-hydrocarbon-gas-liquids.php"),
 "S5": ("EIA, Imports and exports of hydrocarbon gas liquids", "https://www.eia.gov/energyexplained/hydrocarbon-gas-liquids/imports-and-exports-of-hydrocarbon-gas-liquids.php"),
 "S6": ("EIA Today in Energy, First shipment of ethane from U.S. Gulf Coast arrives in Europe (2016)", "https://www.eia.gov/todayinenergy/detail.php?id=28052"),
 "S7": ("EIA Today in Energy, Ethane production expected to increase (2016)", "https://www.eia.gov/todayinenergy/detail.php?id=25632"),
 "S8": ("EIA Today in Energy, U.S. exports of propane reached records in the first half of 2026", "https://www.eia.gov/todayinenergy/detail.php?id=68244"),
 "S9": ("RBN Energy, The strange relationship between Mont Belvieu and Conway NGLs", "https://rbnenergy.com/daily-posts/blog/strange-relationship-between-mont-belvieu-and-conway-ngls"),
 "S10": ("ICIS, Estimating US ethane rejection (2017)", "https://www.icis.com/resources/news/2017/05/10/10105414/estimating-us-ethane-rejection"),
 "S11": ("Congressional Research Service R45398, Natural Gas Liquids: The Unknown Hydrocarbons (2018)", "https://www.everycrsreport.com/files/20181026_R45398_276b160020ed76497f32ec02b5247abba3e60e99.html"),
 "S12": ("OPIS, Most NGLs exit 2022 at lower levels", "https://www.opis.com/blog/most-ngls-exit-2022-at-lower-levels/"),
 "S13": ("EIA, STEO hydrocarbon gas liquids module", "https://www.eia.gov/analysis/pdfpages/steo_hglindex.php"),
 "S14": ("RBN Energy, The Conway vs. Mont Belvieu propane/NGL differential blowout", "https://rbnenergy.com/daily-posts/blog/conway-vs-mont-belvieu-propanengl-differential-blowout"),
 "S15": ("RBN Energy, The differential between us: what drives big propane price spreads", "https://rbnenergy.com/the-differential-between-us-what-drives-big-propane-price-spreads")}
FIX = [("14% of volume, 20.3 of 28.05 USD... see table; it is the largest value component.", "14% of volume but 8.53 of the 28.05 USD barrel (30.4%), the largest value component."),
 ("Isobutane rows show the widest positive margins after propane on 2026-01-12.", "Isobutane net margin: 0.013 then 0.028 USD/gal."),
 ("Ending inventory rises versus base (48.13): lower exports loosen the balance.", "base_ending_inventory_MMbbl: 84.63 (base 48.13): lower exports loosen the balance."),
 ("Several Mont Belvieu propane price assessments exist (non-TET, TET/LST) [S14][S12].", "Several Mont Belvieu propane price assessments exist (non-TET, TET/LST) [S15][S12]."),
 ("blows out under constraints or cold weather, and can invert [S14][S12].", "blows out under constraints or cold weather, and can invert [S15][S12]."),
 ("Constraints anywhere tend to hit Conway prices harder [S9].", "Constraints tend to hit the smaller Conway hub harder [K]."),
 ("Regional shortages can occur before the national number looks tight [S14].", "Regional shortages can occur before the national number looks tight [K]."),
 ("Inventory builds April to September and draws in winter, driven by heating demand [S5].", "Heating demand drives a seasonal cycle [S5]: inventory builds in the warm months and draws in winter (the month shape here is synthetic).")]
LABS = {"037": ("NGL composition and recovery", "Supply analyst at a gas processor. A 200,000 Mcf/d plant needs a product-by-product liquids forecast and a processing-margin estimate for the monthly commercial review.",
  "How many barrels of each product will the plant make, and what is the gross frac spread?",
  "GPM = mol% x factor. gal/d = inlet x GPM x recovery. bbl = gal / 42. shrink MMBtu = gal x MMBtu/gal. frac spread = NGL value / shrink - gas price.",
  ["python3 emi.py run 037", "python3 emi.py run 037 mode=reject", "python3 emi.py run 037 gas_price=7.5", "cat exercises/completed/ex037/ngl_recovery.csv"],
  [("Ethane is 48.6% of the barrels. What share of the value is it?", "476,416.5 gal x 0.235 = 111,958 USD of 572,848 USD: 19.5%."),
   ("In rejection mode barrels fall to 12,787 bbl/d but the frac spread per MMBtu rises from 3.83 to 5.73. Why?", "The barrels removed are ethane, the lowest-value component per MMBtu. The remaining barrel is richer per MMBtu of shrink. Per-MMBtu spread is not total dollars."),
   ("At gas 7.50 the average frac spread is -0.42. Should the plant stop recovering everything?", "No. Check each component: ethane fuel value 0.499 > 0.235 price (reject); propane fuel value 0.686 < 0.720 (recover). An average hides the component decision."),
   ("Which inputs are assumptions rather than measurements?", "Conversion factors, recovery factors, one price date, no fees. All are flagged in the NOTE lines.")],
  "Edit data/synthetic/ngl_components.csv: set ethane mol_pct to 6.0. Predict theoretical GPM before running (5.3519 - 4.5 x 0.2669 = 4.15085). Run, confirm, restore 10.5."),
 "038": ("Ethane rejection", "Commercial optimiser for the same plant. Ethane is 0.235 USD/gal at Mont Belvieu, gas is 3.25 USD/MMBtu, T&F is 0.08 USD/gal.",
  "Recover or reject ethane this month?",
  "Per gallon: recover if price - fee > gas x 0.0665. Plant level: compare total uplift in each mode, including propane lost in rejection.",
  ["python3 emi.py run 038", "python3 emi.py run 038 gas_price=2", "python3 emi.py run 038 ethane_price=0.30", "cat exercises/completed/ex038/gas_price_grid.csv"],
  [("Why is the plant breakeven (0.2782) below the simple breakeven (0.2961)?", "Rejecting also drops propane recovery from 98% to 90%: 21,992 gal/d of propane uplift (7,535 USD/d) is lost. Recovery earns that back, so ethane can be worth less and still justify recovery."),
   ("At what gas price does the decision flip at today's ethane price?", "2.644 USD/MMBtu. Below it, recover."),
   ("Ethane rallies to 0.30. Decision and value?", "RECOVER, worth 9,164 USD/d over rejection."),
   ("Name two real-world limits the model ignores.", "Residue-gas Btu limits capping rejection; pipeline or fractionator capacity and minimum-volume commitments.")],
  "Edit data/synthetic/ex037_plant.csv: set transport_frac_fee to 0.05. Predict the simple breakeven (0.266125) and plant breakeven (0.246631) and the decision (still REJECT at 0.235). Run, confirm, restore 0.08."),
 "039": ("Fractionation economics", "NGL marketer offered 50,000 bbl of Y-grade at 0.55 USD/gal. Frac fee 0.07 USD/gal. Purity prices are the 2026-01-05 Mont Belvieu table.",
  "Buy the Y-grade?", "Barrel value = 42 x sum(fraction x purity price). Margin = value - 42 x (purchase + fee).",
  ["python3 emi.py run 039", "cat exercises/completed/ex039/barrel_value.csv"],
  [("What is one barrel worth and what is the margin?", "28.0518 USD value, 26.04 USD cost, 2.0118 USD/bbl margin, 100,590 USD on the lot."),
   ("What is the most you can pay for the Y-grade?", "0.5979 USD/gal (weighted purity price 0.6679 less the 0.07 fee)."),
   ("Which component matters most to the margin?", "Natural gasoline: 14% of volume, 30.4% of value. A 10% fall in its price removes 0.85 USD/bbl, 42% of the margin."),
   ("What costs are missing?", "Transport to the fractionator, product loss, storage, and the time between purchase and sale.")],
  "Edit data/synthetic/ex039_ygrade.csv to an ethane-rich barrel (Ethane 0.50, Propane 0.25, Normal_Butane 0.09, Isobutane 0.05, Natural_Gasoline 0.11). Predict the direction of the margin change, run, explain, restore."),
 "040": ("Mont Belvieu vs Conway arbitrage", "NGL marketer long product at Conway. Pipeline 0.045 USD/gal plus terminal handling 0.012 USD/gal to reach Mont Belvieu. Lot size 1,000,000 gal.",
  "Which products should move south on each date?", "Basis = Belvieu - Conway. Net margin = basis - 0.057. Ship when positive.",
  ["python3 emi.py run 040", "cat exercises/completed/ex040/ngl_arbitrage.csv"],
  [("Which product never clears the cost?", "Ethane: basis 0.030 both dates, net -0.027 USD/gal."),
   ("Best shipment?", "Propane on 2026-01-12: 0.090 - 0.057 = 0.033 USD/gal, 33,000 USD."),
   ("Propane basis widened from 0.065 to 0.090. Name two possible causes.", "Stronger Gulf Coast or export pull at Belvieu; surplus or constrained outbound capacity at Conway."),
   ("Why might the arbitrage still fail?", "No pipeline space, timing risk between purchase and sale, quality differences, moving the market with your own volume.")],
  "Without editing files, state the transport cost at which propane on 2026-01-05 stops paying (basis 0.065 - handling 0.012 = 0.053 USD/gal)."),
 "041": ("Propane seasonality", "Supply analyst preparing the pre-winter outlook. Opening inventory 45 MMbbl on 1 April, production 2.90 MMb/d, exports 1.95 MMb/d, operating minimum 30 MMbbl.",
  "Is winter supply adequate, and what breaks it?", "Ending inventory = opening + (production - demand - exports) x days. Days of supply = inventory / (demand + exports).",
  ["python3 emi.py run 041", "python3 emi.py run 041 export_shift=0.10", "python3 emi.py run 041 winter_demand_mult=1.10", "cat exercises/completed/ex041/propane_balance.csv"],
  [("When and how high does inventory peak?", "97.88 MMbbl at end September (October is flat)."),
   ("How much does a 20% colder December to February cost?", "25.23 MMbbl extra draw. Inventory falls to 26.0 MMbbl in February and 22.9 in March, below the 30 MMbbl floor."),
   ("Exports rise 0.10 MMb/d all year. Effect?", "36.5 MMbbl less inventory: ending 11.63 MMbbl and 3.8 days of supply even in a normal winter. Exports matter more than weather in this balance."),
   ("What would happen in a real market that this model does not show?", "Prices would rise, exports would fall and inventory would be rationed by price; regional tightness would appear first.")],
  "Find the winter multiplier at which the floor is first breached. Extra draw per 1% = 25.23 / 20 = 1.2615 MMbbl; headroom at end March is 48.13 - 30 = 18.13 MMbbl; breach at about 14.4%. Confirm with winter_demand_mult=1.14 and 1.15."),
 "042": ("Ethane cracker margin", "Feedstock buyer at an ethylene producer with 3,300 million lb/yr of capacity. Ethylene at a hypothetical 22 c/lb.",
  "How much can the cracker pay for ethane, and would propane be a better feed?", "c/lb feed = USD/gal x 100 / lb per gal. Feed cost per lb ethylene = that / yield. Margin = ethylene - feed cost + co-product credit - conversion.",
  ["python3 emi.py run 042", "python3 emi.py run 042 ethane_price=0.35", "python3 emi.py run 042 ethylene_price=30"],
  [("Ethane feed cost per lb of ethylene?", "23.5 / 2.97 / 0.78 = 10.14 c/lb."),
   ("Margin and annual value?", "8.86 c/lb, about 292 million USD/yr."),
   ("Maximum ethane price before margin is zero?", "0.440 USD/gal."),
   ("Together with EX-038, what band can ethane trade in?", "Floor near the plant recovery breakeven (0.278), ceiling near the cracker breakeven (0.440), under these synthetic assumptions.")],
  "Predict the ethane margin at 0.35 USD/gal by hand (35 / 2.97 / 0.78 = 15.11; 22 - 15.11 + 1 - 4 = 3.89 c/lb). Confirm."),
 "043": ("NGL transport optimisation", "Logistics scheduler moving 60,000 bbl from Conway and 40,000 bbl from the Marcellus to Mont Belvieu (70,000) and an East Coast export dock (30,000).",
  "Which arcs carry which barrels, and what is pipeline capacity worth?", "Minimise sum(cost x volume) subject to supply, demand and arc capacity (linear program).",
  ["python3 emi.py run 043", "python3 emi.py run 043 outage_arc=A5", "python3 emi.py run 043 outage_arc=A1 outage_frac=1", "cat exercises/completed/ex043/shipment_plan.csv"],
  [("Base cost and plan?", "246,500 USD (2.465 USD/bbl): both pipelines full, 15,000 bbl Conway rail, 5,000 bbl Marcellus rail, 10,000 bbl marine. No trucks."),
   ("Half of the Conway pipeline is lost. Cost?", "320,250 USD: +73,750, or 3.28 USD per barrel of lost capacity, and 2,500 bbl go by truck."),
   ("The whole Conway pipeline is lost. What happens?", "Infeasible: remaining Conway outlets total 55,000 bbl, so 5,000 bbl are stranded."),
   ("Why is 3.28 USD/bbl a useful number?", "It is what the lost capacity was worth for the period; compare it with the tariff when deciding on a capacity commitment.")],
  "Predict the cost of losing half of A5 (Marcellus pipeline): 12,500 bbl move from 1.50 to rail at 3.20, +21,250 USD. Confirm with outage_arc=A5."),
 "044": ("Integrated NGL portfolio", "Risk analyst marking a six-position NGL book across two hubs on 2026-01-05 and 2026-01-12.",
  "What did the book make, and from which risk?", "MtM = signed gallons x (mark - trade price). Spread P&L = net gallons x Conway move + Belvieu gallons x basis move.",
  ["python3 emi.py run 044", "cat exercises/completed/ex044/positions_marked.csv", "cat exercises/completed/ex044/by_hub.csv"],
  [("Book MtM on each date and P&L?", "26,500 then 118,000 USD; P&L 91,500."),
   ("Propane made 52,500. How much was outright price?", "2,500 (net long 500,000 gal x 0.005). The other 50,000 was basis: 2,000,000 gal x 0.025."),
   ("Which position lost and why?", "P4, short natural gasoline: price rose 0.03, -15,000. P2, short Conway propane: -7,500."),
   ("What is the book's net position and why is that number weak?", "100,000 bbl long, but it adds gallons of different products with different prices and risks. Report by product and hub.")],
  "By hand, compute the P&L if Conway propane had risen 0.03 like Belvieu (basis unchanged): P2 becomes -45,000, propane total 15,000 = 500,000 x 0.03, all flat price.")}
src = (CH / "lessons_source.txt").read_text()
for a, b in FIX: assert a in src, a; src = src.replace(a, b)
rows = [l.split("|") for l in src.strip().splitlines()]; assert len(rows) == 50 and all(len(r) == 9 for r in rows), [len(r) for r in rows]
LEG = "Evidence tags: [S#] = stated in the linked source (curriculum/chapters/chapter_05/sources.md). [EX] = computed by this repo's exercise on SYNTHETIC data. [K] = general industry knowledge NOT source-checked in this build; verify before relying on it."
guide = ["# NGL study guide (Chapter 5)\n", LEG + "\n", "All prices, volumes and plant data are synthetic and hypothetical unless a sentence carries an [S#] tag.\n",
 "## Order of study\n\n1. Sections 5.1-5.2 + labs 037\n2. Sections 5.3-5.4 + labs 038, 039\n3. Sections 5.5-5.6 + labs 041, 042\n4. Sections 5.7-5.9 + lab 040\n5. Section 5.10 + labs 043, 044, then rerun every completion test unaided\n",
 "## Formula sheet (as used in the code)\n\n| Quantity | Formula |\n|---|---|\n| Barrel | 1 bbl = 42 gal |\n| Richness | GPM = mol% x gal/Mcf-per-mol% factor |\n| Plant liquids | gal/d = inlet Mcf/d x GPM x recovery |\n| Shrink | MMBtu = gal x MMBtu/gal |\n| Fuel value | USD/gal = MMBtu/gal x gas price |\n| Frac spread | NGL value / shrink MMBtu - gas price |\n| Netback | hub price - T&F fee |\n| Ethane rule | recover if price - fee > gas x 0.0665 |\n| Basis | Mont Belvieu - Conway |\n| Arbitrage | basis - transport - handling |\n| Y-grade barrel | 42 x sum(fraction x purity price) |\n| Inventory | opening + (production - demand - exports) x days |\n| Days of supply | inventory / (demand + exports) |\n| Feed cost | c/lb = USD/gal x 100 / lb per gal; per lb ethylene = / yield |\n| Cracker margin | ethylene - feed cost + co-product credit - conversion |\n| MtM | signed gal x (mark - trade price) |\n| Spread P&L | net gal x Conway move + Belvieu gal x basis move |\n",
 "## Factors used (rounded engineering approximations [K]; contracts use GPA Midstream standards)\n\n| Product | gal/Mcf per mol% | MMBtu/gal | lb/gal |\n|---|---|---|---|\n| Ethane | 0.2669 | 0.0665 | 2.97 |\n| Propane | 0.2749 | 0.0915 | 4.22 |\n| Isobutane | 0.3265 | 0.0996 | 4.69 |\n| Normal butane | 0.3146 | 0.1037 | 4.87 |\n| Natural gasoline | 0.3650 | 0.1100 | 5.50 |\n"]
titles = {}
for s in range(1, 11):
    sd = CH / "sections" / f"section_{s:02d}"; y = yaml.safe_load((sd / "lessons.yaml").read_text()); titles[s] = y["title"]
    page = [f"# 5.{s} {y['title']}\n", LEG + "\n"]; sec = [r for r in rows if r[0] == f"5.{s}"]; assert len(sec) == 5
    for les, r in zip(y["lessons"], sec):
        _, n, obj, lesson, example, do, expect, job, prod = r
        les.update(objective=obj, market_lesson=lesson, example=example, terminal_activity=do, expected_result=expect, professional_application=job, product_implication=prod, status="written",
                   builds_on=les["prerequisite"], leads_to=(f"L05.{s:02d}.{int(n)+1}" if int(n) < 5 else (f"L05.{s+1:02d}.1" if s < 10 else "L06.01.1")))
        page.append(f"## {les['id']} {les['title']}\n\n**Objective.** {obj}\n\n**Lesson.** {lesson}\n\n**Example.** {example}\n\n**Do.** `{do}`\n\n**Expect.** {expect}\n\n**On the job.** {job}\n\n**Product implication.** {prod}\n\n**Before:** {les['builds_on']} | **Next:** {les['leads_to']}\n")
    (sd / "lessons.yaml").write_text(yaml.safe_dump(y, sort_keys=False, width=1000, allow_unicode=True)); (sd / "content.md").write_text("\n".join(page)); guide.append("\n".join(page).replace(LEG + "\n", ""))
guide.append("# Labs\n")
for n, (title, scen, dec, model, cmds, qa, test) in LABS.items():
    out = (ROOT / f"exercises/expected_output/ex{n}.txt").read_text().strip()
    lab = [f"## Lab EX-{n}: {title}\n", f"**Scenario.** {scen}\n", f"**Decision.** {dec}\n", f"**Model.** {model}\n", f"**Code.** exercises/scripts/ex{n}.py | **Test.** exercises/tests (python3 emi.py test)\n", "**Run (from the repo root).**\n\n```\n" + "\n".join(cmds) + "\n```\n",
           "**Reference output of the first command (synthetic).**\n\n```\n" + out + "\n```\n", "**Questions.** Answer before reading the key.\n\n" + "\n".join(f"{i}. {q}" for i, (q, _) in enumerate(qa, 1)) + "\n", f"**Completion test.** {test}\n",
           "**Answer key.**\n\n" + "\n".join(f"{i}. {a}" for i, (_, a) in enumerate(qa, 1)) + "\n"]
    (CH / "labs" / f"ex{n}.md").write_text("\n".join(lab)); guide.append("\n".join(lab))
srcmd = "# Chapter 5 sources\n\nRead during the build via web search result excerpts on 2026-11-11; full pages were not fetched.\n\n" + "\n".join(f"- {k}: [{t}]({u})" for k, (t, u) in SRC.items()) + "\n"
(CH / "sources.md").write_text(srcmd); guide.append(srcmd); (ROOT / "NGL_STUDY_GUIDE.md").write_text("\n".join(guide))
m = yaml.safe_load((ROOT / "curriculum/curriculum_master.yaml").read_text())
for c in m["chapters"]:
    if c["chapter"] == 5:
        for s in c["sections"]: s["page_status"] = "written"
(ROOT / "curriculum/curriculum_master.yaml").write_text(yaml.safe_dump(m, sort_keys=False, width=200))
print("sections", len(list(CH.glob("sections/*/content.md"))), "labs", len(list(CH.glob("labs/*.md"))), "guide words", len((ROOT / "NGL_STUDY_GUIDE.md").read_text().split()))
