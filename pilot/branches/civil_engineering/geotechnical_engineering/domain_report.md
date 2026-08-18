# Stage D Domain Report — Geotechnical Engineering (Civil pilot)

**Status:** COMPLETE — 10/10 templates accepted; Stage D audit **PASS** (after one FAIL→remediation cycle)
**Dates:** 2026-08-01 → 2026-08-02
**Spec:** docs/pilot_template_authoring_spec.md

## 1. Inventory

| # | Template | Area | Difficulty | Cycles | Branching |
|---|---|---|---|---|---|
| 1 | phase_relations_degree_of_saturation | B1 | Easy | 1 (+polish) | – |
| 2 | relative_density_of_sand | B1 | Easy | 2 | – |
| 3 | borrow_pit_fill_volume | B1 | Intermediate | 3 | ✔ input-form (moist vs void-ratio) |
| 4 | constant_head_permeability | B2 | Easy | 1 (+polish) | – |
| 5 | effective_stress_profile | B2 | Intermediate | 1 (+polish) | – |
| 6 | upward_seepage_quick_condition | B2 | Intermediate | 1 (+polish) | – |
| 7 | primary_consolidation_settlement | B3 | Advanced | 3 | – |
| 8 | time_rate_of_consolidation | B3 | Advanced | 2 (+polish) | ✔✔ drainage path × Tv regime |
| 9 | infinite_slope_factor_of_safety | B4 | Easy | 2 (+polish) | – |
| 10 | terzaghi_strip_footing_bearing | B4 | Intermediate | 3 | ✔ general vs local shear |

Allocation 3/3/2/2 per BOOKS.md; difficulty 4 Easy / 4 Intermediate / 2 Advanced (audit-confirmed by blind relabel, all 10 concur).

## 2. Hardening statistics (the "is it worth it?" evidence)

- **Review cycles:** 10 templates → 19 template-review cycles + 2 Stage D audit passes. 6 templates accepted on cycle 1; 3 needed 2 cycles; 2 needed 3 (t7 twice on R1 physics; t10 constants + branching redesign).
- **Gate failures (real, non-cosmetic):** 6 — precision-amplification drift (t2, R2); liquidity-index inconsistency (t7, R1); undrained-capacity violation (t7, R1); self-containment violation (t8, R3 blocking); serialization/clarity failure (t9, R3); wrong factor family in constants (t10, R2). Plus one **set-level Stage D FAIL** (branching shortfall + t10 relabel).
- **Harness catches before any review:** 3 joint-corner crash bugs (t1-class fixed at author time, t4 volume corner, t10 low-qu corner).
- **Constants-layer corrections adjudicated against on-disk books:** Terzaghi Table 16.1 (6 of 9 Nγ entries were wrong and had *passed web verification*); Das Table 3.1 natural-state soils (replaced curated ranges); modified factors added from PFE Table 3.2. One **cross-source discrepancy between the two Das books** (Nγ at 40°: 116.31 PGE vs 115.31 PFE) logged for the human-expert phase.
- **Verification depth:** every accepted template independently re-solved from question text alone (R2, 5/5 seeds each, plus the auditor's 120-instance sweep per template); Monte-Carlo joint-space audits of 120k–1M draws on physics-critical templates; final answers reproduce within display quantization everywhere.
- **Compounded style guide:** 23 lessons in AUTHOR_NOTES.md; later templates demonstrably avoided earlier defect classes (B2/B4 cycle-1 acceptance rate after B1's lessons).

## 3. Defect-class catalog (what reviewers actually catch)

| Class | Caught by | Instances |
|---|---|---|
| Joint-corner generator crashes | Harness + R1 MC | 5 |
| Precision/rounding chain drift | R2 | 2 |
| Physical-regime violations (capacity, liquidity) | R1 | 2 |
| Wrong/mixed source data in constants | R2 provenance check | 1 (6 values) |
| Self-containment/policy violations | R3 | 2 |
| Difficulty misclassification | R3 blind relabel | 3 |
| Label-vs-value inconsistency | R1 | 3 |
| Serialization/wording defects | R3 (+R1/R2) | 2 |
| Set-level diversity shortfall | Stage D audit | 1 |

## 4. Escalation list (needs a human domain expert eventually)

1. Nγ(40°) cross-source discrepancy between Das PGE Table 16.1 and Das PFE Table 3.1 (unused by templates; likely a typo in one book).
2. Values verified by web only (not on-disk primary): ASCE 7-22 live loads, ACI 318 Ec coefficients, AISC steel properties (official DB on disk covers shapes but not Fy/E prose), CRC water properties — all standard, low risk.
3. t7's undrained-capacity screen uses su ≈ 0.22–0.25·σ'v0 (Skempton-type correlation) as the plausibility bound — an expert should bless the screen itself.

## 5. Artifacts

Templates: `pilot/templates/branches/civil_engineering/geotechnical_engineering/*.py` (4 files) + `constants.py`.
Per-template review logs: `pilot/branches/civil_engineering/review_logs/*.jsonl` (10 files + harness JSONs + instance files).
Audit: Stage D agent transcript (FAIL 2026-08-02 → remediation → PASS 2026-08-02); this report.
