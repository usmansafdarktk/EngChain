# Data Reviewer — Stage B verification prompt (v1)

Role: independent Data Reviewer per docs/pilot_template_authoring_spec.md,
Stage B. You did NOT author the constants file; verify it adversarially.
Do not edit any files — report findings only.

Target file: pilot/templates/branches/civil_engineering/constants.py

Verification duties:
1. 100% of universal constants (gravity, water unit weight/density/viscosity).
2. 100% of entries tagged [VERIFY: ...] — check against the named authority
   via web search (Terzaghi/Kumbhojkar factors, Das typical ranges, ASCE 7-22
   live loads, ACI 318-19 Ec expressions, AISC steel properties, CRC water
   properties, Skempton correlation).
3. >= 20% spot-check of every [ON-DISK] table against the extracted source
   texts in pilot/references/public/extracted/:
   - SCS curve numbers -> nrcs_tr55_urban_hydrology.txt (Tables 2-2a/b/c)
   - Rational C -> fhwa_hec22_urban_drainage.txt (Table 3-1, ~line 2429)
   - Manning's n -> fhwa_hds4_highway_hydraulics.txt (Tables B.2/B.3,
     ~lines 8600-8865)
4. Independently re-check >= 3 AISC W-shapes against
   pilot/references/public/aisc_shapes_database_v16.xlsx (write your own
   extraction script; do not trust any prior extraction).

Output format — return ONLY this JSON:
{
  "findings": [
    {"entry": "<constant / table row>",
     "status": "CONFIRMED" | "DISCREPANCY" | "UNVERIFIABLE",
     "source_checked": "<document / URL>",
     "detail": "<what you compared and what you found; for DISCREPANCY give the correct value>"}
  ],
  "summary": {"confirmed": n, "discrepancies": n, "unverifiable": n},
  "verdict": "PASS" | "FAIL"
}
Verdict is FAIL if any DISCREPANCY exists.
