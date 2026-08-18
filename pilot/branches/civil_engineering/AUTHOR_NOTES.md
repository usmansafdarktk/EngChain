# Author style notes — compounded reviewer feedback (Civil Engineering)

Seeded from the spec §3 contract; reviewer lessons append below per cycle.

- Round-then-recompute: gold trace derives ONLY from the question's presented
  values. Assert self-consistency after recomputation, not before.
- Every displayed float uses fixed-format f-strings (`:.2f`, `:.3f`, `:.1f`).
- One final numeric answer; multi-quantity problems make earlier quantities
  intermediate steps.
- Constraint sampling: sample the physically independent variables (e.g.,
  Gs, e, S), derive the dependent ones — never sample values that could
  jointly violate physics.
- Asserts encode the docstring's "Physical bounds" verbatim.

## Lessons from review cycles

(appended chronologically)

### Cycle: phase_relations_degree_of_saturation c1 (2026-08-01)
1. **Joint-corner feasibility:** when a presented value is DERIVED from
   several sampled variables (w = S*e/Gs), compute per-sample feasibility
   bounds for one sampled variable so the derived value can never breach its
   assert — do not rely on independent range choices being jointly safe.
   Stress-test with a 200-seed harness run.
2. **Round-then-recompute applies to EVERY step,** not just the givens: each
   step's result must derive from the previously *displayed* value, so every
   printed equation evaluates exactly as shown.
3. **Condition sampling ranges on the named material** (e range per soil
   type, anchored to Das Table 3.1) — reviewers check that named soils get
   representative values, not just possible ones.
4. **Step justifications must describe the actual operation** ("dividing by
   (1+w)", not "removing the weight of water").

### Cycle: relative_density c1-c2 + borrow_pit c1-c2 (2026-08-01)
5. **Precision must be sized to downstream sensitivity:** when a rounded
   intermediate feeds a difference or a small denominator, its rounding
   error is amplified — carry extra decimals (e at 4dp when divided by
   (e_max - e_min) ~ 0.3) and check worst-case drift analytically.
6. **No unverifiable commentary in the trace:** any claim in the gold trace
   (e.g., a denseness classification) must be derivable from stated
   information, or it doesn't belong. If kept, its scale must come from the
   cited grounding source, not a different textbook's convention.
7. **Avoid min()/max() clamps on sampled values:** clamping creates a
   probability atom at the boundary (R1 measured ~21% of draws at the cap).
   Sample the increment with per-sample bounds instead.
8. **Whole-number rounding of large intermediates (kN-scale) is visible:**
   carry one decimal on quantities whose printed product check would
   otherwise be off by up to half a unit.

### Cycle: B2 area (constant_head, effective_stress, quick_condition) c1 (2026-08-01)
9. **Assert ceilings must dominate the ANALYTIC max of derived quantities**
   — derive the worst-case corner by hand (or Monte Carlo) and record the
   derivation in a comment; a 300-seed harness run cannot see 1e-5 corners.
10. **Test-setup realism has standards, not just physics:** lab-test
    parameters must respect practice (gradient <= ~3 for a constant-head
    test; measurement resolutions matched to instrument reality — whole
    cm^3, not 0.1 cm^3 on litres).
11. **Answer format must be student-anticipatable:** prefer plain decimals
    a student would naturally write; avoid e-notation in the Answer line
    unless the question requests it.
12. **Same-deposit zones must be cross-constrained** (no loosening with
    depth unless the scenario says so) — independence between zone
    parameters is a reviewer-visible inconsistency even when solvability
    is unaffected.

### Cycle: B3 area (consolidation t7 x3 cycles, t8 x2 cycles) (2026-08-01/02)
13. **Index properties carry hidden joint constraints:** LL, e0, Gs jointly
    imply a liquidity state — sample so derived states stay physical
    (w/LL inside [0.55, 0.95] for an NC clay). Check what every sampled
    pair IMPLIES, not just each range.
14. **Loading must respect the failure mode you are not modeling:** a
    consolidation problem's stress increment must stay below the
    undrained-capacity screen, or the scenario contradicts itself. Screen
    sampled loads against the adjacent limit state.
15. **"Advanced" must be earned by construction, not step count:** blind
    relabeling catches linear chains; add genuine synthesis (2:1 stress
    spread, lab-to-field similitude) rather than more substitutions.
16. **Self-containment policy must be uniform across the set:** if one
    question states its empirical relation (Skempton), all must (Tv-U
    fits); reviewers cross-check siblings for policy consistency.
17. **Exclude degenerate parameter values that bypass the reasoning**
    (U = 50% vs a t50 lab reference collapses the similitude ratio to 1).

### Cycle: B4 area (infinite_slope c2, terzaghi_bearing c2) (2026-08-02)
18. **HEADLINE: only primary-source transcription verifies tabulated
    empirical data.** The Terzaghi Ngamma column passed web-based Stage B
    verification with SIX wrong entries (mixed Vesic/Kumbhojkar families);
    R2's derivation-based provenance check + the on-disk Das Table 16.1
    settled it. Every constants table must trace to a page-cited on-disk
    source before templates depend on it.
19. **String serialization is reviewable content:** a mangled soil
    descriptor cost a clarity gate. Proofread rendered questions across
    several seeds, not just the f-string code.
20. **Labels must match the sampled numbers** ("dense sand" cannot draw
    gamma = 16.5 kN/m^3; condition every named property range on the
    label, incl. unit weights — recurrence of lessons 3/12 in new form).

### Cycle: Stage D remediation (branching for t3/t10) (2026-08-02)
21. **Structural diversity is a SET property — plan it at area level:**
    per-template review cannot see a branching shortfall; design >= 3
    branching templates per domain up front, and make each branch change
    the step structure, not just wording.
22. **Decision-driving site data must be internally consistent with every
    other sampled property** (Dr 72-90% forces phi' ~ 35+, not 30): when a
    datum drives a regime decision, cross-check it against the constants
    tables for every co-sampled value.
23. **When a decision rule is stated, make it boundary-safe** (strict vs
    inclusive thresholds spelled out, sampling never landing on the
    boundary) — R3 checks the rule semantics against the trace wording.

### Cycle: structural A2/A3 (t15-t18) (2026-08-02)
24. **Display precision must carry the value's information:** fixed-dp
    formats (%.6f) truncate small magnitudes to 1-2 sig figs; use
    scientific notation for quantities spanning orders of magnitude
    (I in m^4). The round-then-recompute chain must extend THROUGH the
    final unit conversion (the answer derives from the displayed value).
25. **Screens computed pre-rounding need margins sized to the rounding**
    (whole-foot span rounding ate the 0.98 stress-screen margin; 0.96
    holds).
26. **Claimed maxima need proof against alternatives:** R1 position-swept
    the influence-line arrangement to confirm global optimality — when a
    trace asserts "this arrangement governs", the sampling must make it
    true for every instance, and wording must grant the freedom the
    optimum needs ("may travel in either direction").
27. **Idealizations must be licensed in the question** ("members are
    adequately braced, so buckling is not a concern") when sampled
    geometry would otherwise raise the unmodeled failure mode.

### Cycle: water domain (t21-t30, two full cycles) (2026-08-02)
28. **One question, one number:** multi-part asks break Final Answer
    Accuracy; fold subsidiary quantities into required reasoning ("compute
    yc and use it to justify...") and bind the ask to a single value.
29. **If the gold trace depends on a numerical scheme, the QUESTION must
    prescribe it** (trials, update rule, tolerance) — otherwise any valid
    solver produces a different, ungradable step path.
30. **Small differences of near-equal quantities need extra displayed
    digits** (energies before a dz subtraction; conjugate depths before a
    cubed difference) — size display precision to the downstream
    operation's amplification factor, and derive every chain from the
    displayed values through the final unit conversion.
