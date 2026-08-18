# Stage D Domain Report — Water Resources & Hydraulics (Civil pilot)

**Status:** COMPLETE — 10/10 templates accepted; Stage D audit **PASS, zero required actions**
**Date:** 2026-08-02

## 1. Inventory

| # | Template | Area | Difficulty | Cycles | Branching |
|---|---|---|---|---|---|
| 21 | manning_rectangular_discharge | C1 | Easy | 2 | – |
| 22 | manning_trapezoidal_velocity | C1 | Easy | 2 (re-terminated on velocity) | – |
| 23 | best_hydraulic_rectangular_section | C1 | Intermediate | 2 | – |
| 24 | normal_depth_iteration | C1 | Advanced | 2 (secant redesign) | ✔ section shape inside every iteration |
| 25 | critical_depth_froude_classification | C2 | Easy | 2 (single-answer ask) | (regime conclusion) |
| 26 | hydraulic_jump_energy_loss | C2 | Intermediate | 2 (4-dp conjugates) | ✔ known-depth direction |
| 27 | max_hump_height_no_choking | C2 | Intermediate | 2 (bisection floor) | – |
| 28 | rational_method_peak_flow | C3 | Easy | 2 (natural phrasing) | ✔ single vs composite C |
| 29 | scs_curve_number_runoff | C3 | Intermediate | 2 (**redesigned**: mm data, inch-bound core) | – |
| 30 | linear_reservoir_routing_step | C3 | Advanced | 2 (**redesigned**: two intervals) | – |

Allocation 4/3/3; difficulty 4/4/2; all 10 blind relabels match (audit); branching 3 strong + 1 weak (≥3 met).

## 2. Hardening statistics

- **The hardest domain of the branch:** every template took 2 cycles. Cycle 1 produced the pilot's densest defect harvest: a cross-cutting R1 physics failure (erosive velocities on the unlined-earth lining — phys 3 on all four C1 templates), an R3 blocking (t24's iteration scheme absent from the question → gold path irreproducible), three R2 precision blockings (cubed-difference, energy-cancellation, and 2-dp-S amplification), two R1 assert holes (t26/t27), and two R3 difficulty relabels that forced genuine redesigns (t29 → unit-bound mm/inch chain; t30 → derivation + two routing intervals).
- **Harness pre-catches:** 7 joint-corner classes fixed before any reviewer saw them.
- **Verification depth (cycle 2):** exhaustive proofs where sampling can't reach — all 60,726 reachable (yc, y1) combos for t27; 599,518-point lattice for t26; 462,900-point lattice for t30; t24 line-by-line gold-path reproduction from the question's prescribed scheme plus brentq cross-check. Audit: 600/600 parser round-trips, 500-seed stress sweeps, zero assert firings.
- **New defect classes discovered (feeding AUTHOR_NOTES 28–30):** near-cancellation display precision; question-prescribed numerical schemes for iterative gold traces; multi-part asks vs the single-answer contract; lining/land-use realism screens (erosive velocity as the unmodeled failure mode).

## 3. Escalation list

1. Erosive-velocity screens and the Fr ≤ ~0.9 subcritical design convention encode judgment an expert should bless (some codes allow supercritical lined chutes).
2. t22 vs t21 is the branch's weakest structural differentiation (audit: acceptable, "should not be narrowed further").
3. t29's inch-bound-equation framing (SI storm data) should be reviewed by a practicing hydrologist for regional convention fit.

## 4. Artifacts

Templates: `pilot/templates/branches/civil_engineering/water_resources/*.py` (3 files).
Review log: `review_logs/area_C1_C2_C3_water.jsonl` + harness JSONs + instance files (cycles 1–2).
Audit: Stage D agent (PASS, 2026-08-02); this report.
