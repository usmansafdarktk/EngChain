# Stage B — Data Review Log: Industrial Engineering / Operations Research

**Target:** `pilot/templates/branches/industrial_engineering/constants.py`
**Curator:** Data Curator agent (session of 2026-08-05)
**Reviewer:** independent Data Reviewer agents (fresh contexts, prompt `pilot/prompts/data_reviewer_v2_industrial.md`)
**Final verdict:** PASS — Cycle 2: 6 CONFIRMED, 0 DISCREPANCY, 0 UNVERIFIABLE (Cycle 1: 22 CONFIRMED, 1 DISCREPANCY, 2 UNVERIFIABLE — all resolved)

## Cycle 1 (2026-08-05)

### Coverage

- `CONTROL_CHART_FACTORS` (n = 2–25, 16 columns, **384 cells**): verified at
  **100% by independent derivation** — reviewer's own code computed c4 from
  its Γ-function definition, d2 by deterministic quadrature (converged to
  7 dp), d3 via the E[R²] double integral (500×500 Gauss–Legendre), and all
  remaining columns from the standard identities. Every cell matches at its
  printed precision (353/384 round exactly; the other 31 are final-digit
  rounding artifacts of the printed source, each reproduced exactly by the
  table's own rounding conventions — no transcription errors).
  **Transcription fidelity separately confirmed token-by-token against the
  on-disk Montgomery 7e text (Appendix Table VI, text p. 720 / PDF p. 738):
  384/384 byte-identical.** This is the derivation-based provenance check
  promised in BOOKS.md §5 (Terzaghi lesson applied preemptively).
- `Z_QUANTILES`: 100% by derivation (`NormalDist.inv_cdf`), exact at 4 dp;
  cross-references located in Montgomery Appendix Table II and H&L 7e App. 5.
- `MIL_STD_105E_*`: 100% against the reviewer's own page renders —
  Table I GII column (15/15 bands incl. skipped letter I), Table II-A sample
  sizes (16/16), and all 75 Ac-subset cells including every None/arrow cell
  and the Re = Ac + 1 claim.
- `[REALISM]` entries: reviewed above the ≥20% minimum — every entry citing
  a specific section/page was checked (grep of extracted texts; visual
  renders of the image-only Nahmias 7e pp. 138, 204–205, 213, 218, 220–221,
  258, 274, 528–533).

### Findings and resolutions

| # | Finding | Status | Resolution |
|---|---|---|---|
| 1 | Code-letter comment cited the default-level provision as §4.9.2; it is §4.9.1 "Inspection Level" ("Normally, Inspection Level II is used.") | DISCREPANCY (comment-only; no numeric value affected) | Citation corrected to §4.9.1 with the verbatim provision quoted. |
| 2 | `COMPONENT_RELIABILITY_CLASSES` claimed Ross 11e Ch. 9 examples quote "component reliabilities in the 0.9+ range" — chapter works symbolically (p_i); no such numerics exist | UNVERIFIABLE | Comment rewritten: Ross grounds typology only; retagged `[REALISM][POLICY: sampling-only]` (given-values rule ⇒ correctness-neutral); added to the human-expert escalation list. |
| 3 | `FAILURE_RATE_PER_HR` cited e-Handbook §8.1.2/8.1.10 as a magnitude anchor — those sections define rates / Bayesian methodology but tabulate no per-family magnitude bands (curator re-check of the suggested alternates apr164/apr171/apr221 found no bands either) | UNVERIFIABLE | False anchor withdrawn explicitly in the comment; retagged `[REALISM][POLICY: sampling-only]`; escalation-listed. |
| 4 | Cosmetic (within a CONFIRMED entry): "Taha 10e §18.9?" uncertainty marker — reviewer resolved §18.9 = "Queuing Decision Models", §18.9.1 = "Cost Models" | note | Citation made definite. |
| 5 | Cosmetic (within a CONFIRMED entry): holding-rate comment claimed "worked examples use i in the 0.15–0.35/yr band", but the §4.4 flagship illustration builds I = 0.37 (28+2+6+1%); problems use ≈0.22 | note | Window widened to (0.15, 0.40); comment now states both anchors precisely. |
| 6 | Cosmetic (within a CONFIRMED entry): subgroup-size guidance attributed to §6.2.3/§6.3; the efficiency guidance lives in §6.3 | note | Attribution corrected to §6.3 with the verbatim "n > 10 or 12" quote. |

## Cycle 2 (2026-08-05) — fresh reviewer, scope = the six revised entries

All six re-verified CONFIRMED against the reviewer's own renders/greps
(MIL-STD-105E §4.9.1 text + Table I caption; Taha/H&L titles; Ross Ch. 9
full-chapter scan; e-Handbook apr/ full-chapter scan; Nahmias pp. 204–205
h = Ic and the 37% build-up, problem rates 20–25%; Montgomery §6.3 verbatim
quote). **0 discrepancies, 0 unverifiable → Gate B PASS.**

## Escalation list (for eventual human experts)

- `COMPONENT_RELIABILITY_CLASSES` and `FAILURE_RATE_PER_HR` windows have no
  primary-source numeric anchor (judgment screens under the given-values
  rule). A reliability-engineering expert should bless or adjust the bands
  (e.g., against MIL-HDBK-217F or vendor FIT data, neither on disk).
- Montgomery 7e Ch. 7's flagship p-chart example baseline (p̄ = 0.231,
  out-of-control startup) sits above `P_CHART_PBAR = (0.01, 0.15)`; the
  window intentionally models in-control historical baselines — flagged so
  humans confirm the policy.

## Method note

Curator-side pre-review sanity check (internal identities A = 3/√n,
A2 = 3/(d2√n), A3 = 3/(c4√n), B3–B6, D1–D4 from c4/d2/d3, zero-floors) ran
clean before Cycle 1; it is recorded here because it is NOT a substitute for
the reviewer's independent derivation, only a transcription-typo screen.
