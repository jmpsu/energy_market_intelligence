# STATUS

Verified by running, 2026-11-11 11:03 UTC:

- Exercises: 100 of 100 implemented (98 via `emi.py run`, EX-003 and EX-005 as labs) + 4 NGL extensions (101-104). `python3 emi.py status`.
- Tests: Ran 52 tests in 13.543s -> OK. `python3 emi.py test`.
- Section pages: 120 of 120. Lessons with all fields: 600 of 600. Every lesson command in chapters 1-4 and 6-12 was executed and its expected line matched.
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
