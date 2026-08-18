# Civil Engineering Pilot — Branch Final Report (Stage E)

**Spec:** docs/pilot_template_authoring_spec.md · **Dates:** 2026-07-31 → 2026-08-02
**Verdict up front: GO** — agentic Phase-1 authoring of EngTrace-grade templates is feasible, and the pilot quantifies exactly where human experts remain necessary.

## 1. What was produced

**30 templates, all accepted; all three domains Stage-D audit-PASSED; 150-instance mini-testset generated and 150/150 parser-verified against the existing EngTrace pipeline.**

| Domain | Templates | Difficulty | Branching | Stage D |
|---|---|---|---|---|
| Geotechnical | 10 | 4E/4I/2A | 3 | FAIL → remediate → PASS |
| Structural | 10 | 4E/4I/2A | 6 | **PASS first attempt** |
| Water Resources | 10 | 4E/4I/2A | 4 | **PASS, zero actions** |

Supporting artifacts: page-cited `constants.py` (verified against on-disk primary sources), the H1–H7 harness, versioned agent prompts, per-template JSONL review logs, three domain reports, a 30-lesson compounded style guide (AUTHOR_NOTES.md), and `pilot/testset_preview/civil_engineering/*.jsonl` in the exact schema of the real testset (`id, seed, branch, domain, area, level, question, solution`; seeds 201–205, disjoint from review seeds).

## 2. Hardening statistics — the evidence base

- **Review cycles:** ~50 template-review cycles across 30 templates + 4 Stage D audit passes. Cycle-1 acceptance improved monotonically as lessons compounded: geotech 6/10 → structural 7/10 (incl. a 4-template zero-blocking area) → water 0/10 *by design severity* (the domain that stress-tested every new defect class), all accepted at cycle 2.
- **Genuine gate failures caught and fixed: 15** — spanning nine distinct defect classes: physical-regime violations (liquidity, undrained capacity, erosive velocity), precision-amplification (small denominators, cubed differences, near-cancellation), self-containment violations, difficulty misgrades, serialization defects, assert-safety holes, wrong source data, set-level diversity shortfall, and irreproducible gold paths.
- **Harness pre-catches:** ~15 joint-corner crash classes fixed before any reviewer spent tokens.
- **The headline data-integrity event:** the Terzaghi Nγ column passed web-based Stage-B verification with **six wrong values** (mixed Vesić/Kumbhojkar families); R2's derivation-based provenance check plus the on-disk Das book caught and corrected it — and the two on-disk Das books themselves disagree at Nγ(40°) (116.31 vs 115.31), now logged. **Conclusion: only page-cited primary-source transcription counts as verification for tabulated empirical data.** This single finding justifies the user's books-first policy.
- **Verification depth reached:** independent re-solving of all 150 review instances from question text alone (including full stiffness-matrix and joint-equilibrium solves, sympy symbolic checks, brentq root-finds); Monte-Carlo joint-space sweeps of 0.3–2M draws; and *exhaustive* enumerations where spaces were finite (13,776 / 60,726 / 63,882 / 75,020 / 599,518 combos). Every accepted template's printed arithmetic reproduces exactly from its displayed operands.

## 3. What the pilot proves about the division of labor

**Agents are strong at:** arithmetic-exact gold traces; joint-parameter-space safety (at scales no human would attempt); adversarial cross-checking (three independent lenses caught non-overlapping defect classes throughout); compounding style discipline; and set-level structural auditing.

**Humans remain necessary for** (the escalation lists, consolidated):
1. **Blessing engineering-judgment screens** — undrained-capacity margins, erosive-velocity limits, serviceability conventions (L/240, ~180 MPa), Fr ≤ 0.9 design practice.
2. **Adjudicating cross-source data conflicts** — the Das-vs-Das Nγ(40°) discrepancy is unresolvable without an authority.
3. **Difficulty-policy edge cases** — integration-based and construction-heavy templates that satisfy Advanced criteria with sub-6 step counts.
4. **Regional/convention fit** — e.g., the inch-bound SCS equation posed with SI storm data.
5. **Phase 2/3 certification itself** — this pilot deliberately did NOT run the AI Tribunal or human certification; nothing here enters the paper without them.

## 4. Cost profile (approximate, from this run)

Per domain: ~1 authoring day-equivalent of agent time; 6–13 reviewer-agent invocations (each with its own MC/solver work); 1 audit agent. The dominant human cost was two checkpoints: Gate A approval and supplying licensed textbook PDFs. The expensive human step this pilot *replaces* is template drafting and first-pass QA — not final certification.

## 5. Model-pilot readiness

`pilot/testset_preview/civil_engineering/` (150 records) is directly consumable: point `evaluation/run_inference.py` at it (it walks a directory of .jsonl with `question` fields) and run the evaluation framework unchanged — schema and formatting verified via 150/150 `engineering_parser` round-trips. Suggested first experiment: run 2–3 models spanning capability tiers and compare FAC/Reasoning-F1 profiles against the paper's existing branches to see whether Civil behaves like a "new Mechanical" (accessible) or "new Chemical" (hard) — directly relevant to the branch-difficulty narrative in the revision.

## 6. Recommendation

**GO** for the full human-expert pipeline on Civil (Phase 2 AI Tribunal → Phase 3 certification), and **GO** for repeating this Phase-1 process on Industrial/OR and Aerospace — with the process improvements now encoded: branching planned at area level (lesson 21), primary-source-only data verification (lesson 18), per-step round-then-recompute with sensitivity-sized precision (lessons 2/5/24), and question-prescribed schemes for iterative traces (water-domain lesson).
