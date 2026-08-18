# Stage B — Data Review Log: Civil Engineering

**Target:** `pilot/templates/branches/civil_engineering/constants.py`
**Curator:** Data Curator agent (session of 2026-08-01)
**Reviewer:** independent Data Reviewer agent (fresh context, prompt `pilot/prompts/data_reviewer_v1.md`)
**Reviewer verdict:** PASS — 20 CONFIRMED, 0 DISCREPANCY, 3 UNVERIFIABLE

## Cycle 1 (2026-08-01)

### Coverage
- Universal constants: 100% verified (gravity, γw, ρ, ν — CRC/standard values).
- [ON-DISK] tables: verified at 100% (exceeds the ≥20% spec minimum) against
  the extracted source texts:
  - `MANNINGS_N_CHANNELS` — 12/12 rows vs HDS-4 Table B.2
  - `MANNINGS_N_CONDUITS` — 5/5 rows vs HDS-4 Table B.3
  - `RATIONAL_C` — 16/16 rows vs HEC-22 Table 3-1
  - `SCS_CURVE_NUMBERS` — 25/25 rows vs TR-55 Tables 2-2a/b/c
  - `SCS_IA_RATIO` + runoff equation vs TR-55 Eqs. 2-2/2-3/2-4
- AISC W-shapes: independently re-extracted from the xlsx by the reviewer
  (own script; US + metric column groups) — all 14 shapes × 7 properties ×
  2 unit systems (196 values) + 14 metric labels: zero deviations.
- [VERIFY]-tagged standards entries, via web against named authorities:
  steel E/Fy (AISC/ASTM), concrete Ec coefficients (ACI 318-19 19.2.2.1(b),
  incl. the code-printed 4700 metric coefficient), ASCE 7-22 Table 4.3-1
  live loads (psf and kPa), Terzaghi factors incl. full Kumbhojkar (1993)
  Nγ column, Das Gs/permeability/friction-angle tables, Skempton
  Cc = 0.009(LL−10) undisturbed form — all CONFIRMED.

### Findings and resolutions

| # | Finding | Status | Resolution |
|---|---|---|---|
| 1 | `SATURATED_UNIT_WEIGHTS_KN_M3` endpoints not traceable to a named Das/DM-7 table (anchor values all fall inside; no contradiction) | UNVERIFIABLE | Retagged `[PENDING-TEXTBOOK-VERIFY]`; comment added requiring Stage C templates to state sampled unit weights as given values in the question. Final verification deferred to Das PGE ch. 3 when textbook chapters arrive. |
| 2 | `MOIST_UNIT_WEIGHTS_KN_M3` — same situation | UNVERIFIABLE | Same resolution as #1. |
| 3 | `CV_RANGES_M2_YR` — published low-plasticity values (e.g., glacial lake clays ≈2–2.7 m²/yr) fall below the original 3.0 floor | UNVERIFIABLE | Ranges widened to overlapping (0.3–5.0 / 2.0–30) reflecting the reviewer's evidence; retagged `[PENDING-TEXTBOOK-VERIFY]` for Das ch. 11 / DM-7.01 cv–LL chart. |
| 4 | Cosmetic: HDS-4 Table B.3 sits on doc page B-4, not B-3 | note | Comment corrected. |

## Cycle 2 (2026-08-01) — quarantine resolution after textbook arrival

Das & Sobhan *PGE* (supplied copy: **9th ed.**, full text extracted) resolves
the Cycle 1 quarantine:

- Findings #1/#2 (unit-weight range endpoints): the curated
  `SATURATED_UNIT_WEIGHTS_KN_M3` / `MOIST_UNIT_WEIGHTS_KN_M3` dicts were
  **replaced entirely** by `DAS_NATURAL_STATE_SOILS` — a verbatim transcription
  of Das Table 3.1 (9 soil types; e, w_sat, γd in both unit systems), tagged
  [ON-DISK]. Derived quantities (γ, γsat) are now computed from phase
  relationships inside templates rather than sampled from curated ranges.
  Spot-derivations against the old ranges: loose sand γsat ≈ 18.9 and dense
  sand ≈ 21.0 kN/m³ (inside old ranges), stiff clay ≈ 20.7 (slightly above
  the old 20.5 upper bound) — confirming the replacement was the right call.
- Finding #3 (cv ranges): retagged [POLICY: sampling-only] — Das has no
  general cv table and the DM-7.01 cv–LL chart is image-only; the
  given-values rule (sampled cv always stated verbatim in the question)
  permanently removes endpoint sensitivity.

## Cycle 3 (2026-08-02) — CORRECTION: Terzaghi factor table was wrong

During Stage C review of `template_terzaghi_strip_footing_bearing`, R2's
independent factor-provenance check found that `TERZAGHI_BEARING_FACTORS`
mixed factor families: the Nγ entries at φ ≤ 25° were Vesić values
(2(Nq+1)tanφ — e.g. 5.39 at 20°, 10.88 at 25°), not the Das/Kumbhojkar
tabulation the citation claimed. Adjudicated against the on-disk primary
source (Das PGE 9th ed., **Table 16.1**, text p. 717): **six of nine Nγ
entries were wrong** (φ = 5/10/15/20/25/40), plus a last-digit error in
Nc(10°). Corrected by verbatim transcription; entry retagged [ON-DISK].

**Root-cause note for the Final Report:** the Cycle-1 web-based
verification CONFIRMED the wrong values — secondary web reproductions of
"Das/Kumbhojkar" tables are themselves inconsistent, and the reviewer
anchored on ones matching the curated (wrong) values. Lesson: for tabulated
empirical data, only primary-source transcription counts as verification;
web cross-checks can create false confidence. This defect would have
poisoned every bearing-capacity instance had Stage C's independent
re-derivation check not caught it.

## Cycle 4 (2026-08-02) — additions and a cross-source note

- Added `TERZAGHI_MODIFIED_FACTORS` (local-shear N'c/N'q/N'γ at φ = 20/25/
  30/35), transcribed verbatim from Das & Sivakugan PFE 9th ed. Table 3.2
  (text p. 140) [ON-DISK]; local-shear strip equation per Eq. (3.9).
  Independently re-verified against the book text by a Stage C R2 reviewer.
- Cross-source discrepancy recorded: the two on-disk Das books disagree on
  the general-shear Nγ at φ = 40° (PGE Table 16.1: 116.31; PFE Table 3.1:
  115.31 — likely a typo in one). Our entry follows PGE, the named primary
  for that table. No template samples φ = 40°, so no instance is affected;
  flag for the human-expert phase.

### Gate B status
- Zero discrepancies → **Gate B PASSES** for Stage C purposes, with one
  standing quarantine: the three `[PENDING-TEXTBOOK-VERIFY]` tables may be
  used only as *sampling ranges whose drawn values appear verbatim in the
  question text* (so template correctness never depends on the endpoints).
  Endpoint verification re-opens automatically when the Das chapters land in
  `pilot/references/geotechnical/`.
