# Stage D Domain Report — Structural Analysis (Civil pilot)

**Status:** COMPLETE — 10/10 templates accepted; Stage D audit **PASS on first attempt** (zero required actions)
**Date:** 2026-08-02
**Spec:** docs/pilot_template_authoring_spec.md

## 1. Inventory

| # | Template | Area | Difficulty | Cycles | Branching |
|---|---|---|---|---|---|
| 11 | beam_support_reactions | A1 | Easy | 1 (+polish) | ✔ load-type (weakest; audit counts 5 without it) |
| 12 | truss_method_of_joints | A1 | Easy | 1 (+polish) | – |
| 13 | beam_internal_moment | A1 | Easy | 1 (+polish) | ✔ section-side |
| 14 | truss_method_of_sections | A1 | Intermediate | 1 (+polish) | ✔ 3-way member selection |
| 15 | influence_line_max_reaction | A2 | Intermediate | 1 (+polish) | – (arrangement decision) |
| 16 | beam_deflection_formula | A3 | Easy | 2 | ✔✔ dual-unit × load-case |
| 17 | virtual_work_truss_deflection | A3 | Intermediate | 2 | – |
| 18 | cantilever_double_integration | A3 | Intermediate | 2 | ✔ load-case (rewrites the integration) |
| 19 | force_method_continuous_beam | A4 | Advanced | 1 (+polish) | ✔ load-case (changes released-beam analysis) |
| 20 | slope_deflection_end_moment | A4 | Advanced | 1 (+polish) | – |

Allocation 4/1/3/2 per BOOKS.md; difficulty 4/4/2; **all 10 blind relabels match** (audit); **branching count 6** (≥3 required — planned at area level per lesson 21, vs geotech's post-hoc remediation).

## 2. Hardening statistics

- **Cycles:** 13 template-review cycles + 1 audit pass. Seven accepted on cycle 1 (A1 all four with *zero blocking findings* — first such area); three needed cycle 2 (t16/t18 I-display defect; t17 band closure).
- **Gate failures:** 3 (t16 + t18 R3 clarity gates on the shared `%.6f` display-truncation defect; t17 R1 band-closure major).
- **Harness/author catches pre-review:** t18 delta-ceiling corner; t20 near-cancellation floor; t19 author-self-caught 8× coefficient error; t20 w-ceiling corner (R1).
- **Verification depth:** R2 re-solved all 50 instances — including **independent Euler–Bernoulli stiffness-matrix solutions** for the indeterminate templates with sign-convention benchmarks, full joint-equilibrium matrix solves for both trusses, and sympy verification of the double-integration closed forms. R1 *proved* claimed optima (influence-line arrangement position-swept; t17 verified by exhaustive 13,776-combo sweep; t19/t20 exhaustive sweeps of 2,604/24,074 cases + 2M-draw MC). Audit re-verified 600 instances end-to-end incl. parser round-trip (600/600).
- **Style-guide growth:** lessons 24–27 added (display precision carries information; rounding-sized screen margins; proving claimed maxima; licensing idealizations).

## 3. Evidence of compounding (geotech → structural)

| Metric | Geotech | Structural |
|---|---|---|
| Cycle-1 acceptance | 6/10 | 7/10 (incl. one 4-template zero-blocking area) |
| Stage D verdict | FAIL → remediate → PASS | **PASS first attempt** |
| Branching | 1 planned, 3 after remediation | 6 planned up front |
| Blind-relabel mismatches | 3 | 0 |

New defect classes still emerged (display-precision truncation; unclosed derived-quantity bands; unproven optimality claims) — evidence that review remains load-bearing even as authoring improves.

## 4. Escalation list (for the human-expert phase)

1. t18's difficulty sits on the Intermediate/Advanced boundary (satisfies two Advanced clauses literally; single-concept canonical integration) — an expert should bless the label policy for integration-based templates.
2. t19/t20 are Advanced with 4–5 steps (construction criterion met, step-count guideline not) — same policy question.
3. Serviceability/stress screens (L/240, ~180 MPa working stress) encode design judgment an expert should confirm.

## 5. Artifacts

Templates: `pilot/templates/branches/civil_engineering/structural_analysis/*.py` (4 files).
Review logs: `pilot/branches/civil_engineering/review_logs/area_A1_*.jsonl`, `area_A2_A3_*.jsonl`, `area_A4_*.jsonl` + harness JSONs + instance files.
Audit: Stage D agent (PASS, 2026-08-02); this report.
