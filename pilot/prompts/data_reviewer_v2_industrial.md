# Data Reviewer — Stage B verification prompt (v2, Industrial Engineering / OR)

Role: independent Data Reviewer per docs/pilot_template_authoring_spec.md,
Stage B. You did NOT author the constants file; verify it adversarially.
Do not edit any files — report findings only.

Target file: pilot/templates/branches/industrial_engineering/constants.py

Branch context (read first): pilot/branches/industrial_engineering/BOOKS.md
(§5 data sources, §9 on-disk copies). Reference locations:
- Montgomery ISQC 7e full text: pilot/references/public/full_books_industrial_engineering/extracted/montgomery_isqc_7e.txt
  (and the source PDF alongside it; Appendix Table VI at PDF p. 738)
- MIL-STD-105E: pilot/references/public/mil_std_105e_sampling.pdf
  (Table I at PDF page index 17, Table II-A at index 18; the OCR text layer
  is unreliable — render the pages yourself with pymupdf at >=170 dpi and
  read the images)
- NIST/SEMATECH e-Handbook: pilot/references/public/nist_sematech_ehandbook/handbook/
- H&L 7e / Ross 11e / Taha 10e extracted texts in the same extracted/ folder.
- Nahmias 7e and Grant & Leavenworth are IMAGE-ONLY PDFs — render pages
  visually when a citation names them.

Verification duties:
1. CONTROL_CHART_FACTORS — 100%, by INDEPENDENT DERIVATION with your own
   code (do not trust the file's comments or any prior script):
   c4(n) = sqrt(2/(n-1)) * Gamma(n/2) / Gamma((n-1)/2);
   d2(n) = integral over x of [1 - PHI(x)^n - (1-PHI(x))^n];
   d3(n) = sqrt(E[R^2] - d2^2) via its double-integral definition;
   then A, A2, A3, B3, B4, B5, B6, D1, D2, D3, D4, 1/c4, 1/d2 from the
   standard identities. Compare every table value at its printed precision
   (allow only final-digit rounding differences). ALSO independently confirm
   transcription fidelity against the Montgomery extracted text (the table
   is machine-readable there).
2. Z_QUANTILES — 100% by derivation (statistics.NormalDist().inv_cdf).
3. MIL_STD_105E_* (code letters GII, sample sizes, single-normal Ac subset
   incl. which cells are None/arrows) — 100% against your own visual reads
   of the rendered Table I / Table II-A pages.
4. [REALISM] entries — spot-check >= 20% (and every entry whose comment
   cites a specific section/page): confirm the cited anchor exists where
   claimed (grep extracted texts; render image-only pages) and that the
   range is consistent with the cited conventions. Realism ranges are
   plausibility screens under the given-values rule — flag DISCREPANCY only
   for a wrong citation or a range clearly contradicting the source; flag
   UNVERIFIABLE where the anchor cannot be located.
5. Sanity-check remaining structural claims in comments (e.g., Montgomery
   chapter/section attributions, "R = Ac + 1" claim) against the sources.

Output format — return ONLY this JSON:
{
  "findings": [
    {"entry": "<constant / table row>",
     "status": "CONFIRMED" | "DISCREPANCY" | "UNVERIFIABLE",
     "source_checked": "<document / page / method>",
     "detail": "<what you compared and what you found; for DISCREPANCY give the correct value>"}
  ],
  "summary": {"confirmed": n, "discrepancies": n, "unverifiable": n},
  "verdict": "PASS" | "FAIL"
}
Verdict is FAIL if any DISCREPANCY exists.
