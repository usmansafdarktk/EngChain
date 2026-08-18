# Author style notes — Industrial Engineering / OR branch

**Binding baseline:** ALL 30 lessons in
`pilot/branches/civil_engineering/AUTHOR_NOTES.md` apply from template 1
onward (HANDOFF §5). Re-read that file plus this one before every template.
IE-specific lessons append below per review cycle.

## Standing IE-branch conventions (Stage A/B decisions)

- **Unit-light branch:** rates/counts/probabilities/USD; no SI-vs-US
  duality. Diversity comes from regime/topology/decision branching
  (BOOKS.md §4). At least one S1 template deliberately mixes time units
  (λ per hour vs. μ per minute) — when it does, both units must be stated
  explicitly in the question.
- **ρ < 1 steady-state gate:** every infinite-queue template samples
  (λ, μ, c) jointly so ρ < 1 by construction AND asserts it; the gold trace
  states the steady-state check as a step. M/M/1/K is the deliberate
  exception (ρ ≥ 1 admissible and reasoned about).
- **Given-values rule (from Stage B):** every sampled parameter is stated
  verbatim in the question; [REALISM] ranges screen plausibility only.
- **Φ convention:** statistics.NormalDist for Φ/Φ⁻¹; solutions display z
  and Φ(z) at declared precision so a z-table student can follow.
- **Integer-friendly rates:** where a scenario allows it, sample integer
  per-hour rates — cleaner student arithmetic and exact ρ = λ/μ checks
  (Civil lesson 11 analog).
- **Probability display precision:** probabilities that feed later steps
  (P0, ρ powers, Φ values) carry 4 dp; terminal probabilities may use 3-4
  dp sized to downstream amplification (Civil lessons 5/24/30).

## Lessons from review cycles

(appended chronologically; numbering continues Civil's 1-30)

### Cycle: mm1_time_in_system c1 (2026-08-05) — accepted c1

31. **Steady-state phrasing:** don't both stipulate "in steady state" in the
    stem and ask the solver to "verify steady state" — ask to *verify that a
    steady state exists (rho < 1)*, or drop the stipulation.
32. **Docstring corner lists must be exhaustive over scenarios:** when a
    bound's extremum is realized by more than one scenario window, name them
    all (or say "several scenarios realize this corner").
33. **Realism ceiling on utilization:** rho near 0.92 yields hour-long
    average system times; where the named setting makes persistent
    saturation implausible, cap rho at ~0.85 (also buys precision margin in
    (1-rho)^-2 amplification chains — see lesson 30).

### Cycle: mmc_waiting_time c1 (2026-08-05) — accepted c1

34. **Name the general formula before instantiating it:** when a step prints
    an expanded standard result (P0 sum), first state the general form the
    expansion comes from — the trace should teach which result is applied.
35. **Finite instance spaces collide:** with O(100) reachable instances,
    5-seed review batches can contain duplicates (seeds 101=105 here) and
    Stage E seed sets may too; prefer instance spaces >= a few hundred, or
    accept and note the collision odds in the docstring.
36. **Display phrases must stay inside the constants anchor class:** the
    prose setting ("urgent-care clinic") must be the SAME kind of operation
    the [REALISM] window was anchored to ("hospital emergency room") — R1
    cross-checks prose against the cited anchor, not just the numbers.

### Cycle: server_configuration_selection c1 (2026-08-05) — accepted c1

37. **Never compress a unit conversion into a chained equality:** show the
    "x 60 minutes/hour" operation explicitly (or show the hours value first,
    then the minutes value) — both R2 and R3 flag silent-unit jumps.
38. **Notation must be consistent when instantiating a general formula:**
    if the trace's variables are rho2/L2, the quoted formula must be written
    in those symbols (not generic rho/L).
39. **Assert envelopes should hug the enumerated corners** (small margin for
    the rounding chain only) and the docstring should state the corners
    inline — a 2x-loose envelope draws an R1 finding.
40. **Say which sampled parameter drives a branch:** Stage D audits branch
    QUALITY; if a decision branch is driven by one parameter pair (not the
    obvious one, e.g. service-time pair rather than lambda), the docstring
    should say so explicitly.

### Cycle: mm1k_finite_capacity c1-c2 (2026-08-06) — accepted c2 after relabel-forced revision

41. **R3's blind relabel is a hard gate — recurrence of Civil lesson 15:**
    chaining N standard formulas is Intermediate no matter how many steps;
    Advanced requires the trace to CONSTRUCT something (balance equations →
    distribution → normalize → direct expectation). Design the construction
    in from the start for every Advanced slate slot.
42. **Justify non-obvious substitutions in named laws:** using lam_e (not
    lambda) in Little's formula needs one sentence of why (L counts only
    joining cars); classic student confusion points must be addressed, not
    asserted.
43. **Unroll short inductions:** "p1 = rho p0, p2 = rho^2 p0, ..., hence
    p_n = rho^n p0" — one extra line makes the derivation followable when
    the derivation IS the pedagogical point.
44. **Enumerate corners BEFORE writing docstring bounds** (I violated my own
    lesson 39 twice this template — the bounds are outputs of QA, never
    estimates). Also noted: numbers-only surface variation across instances
    is acceptable (H6 requires distinct strings, not distinct prose) but
    reviewers remark on it; consider light framing variation where cheap.

### Cycle: two_state_steady_state c1 (2026-08-06) — accepted c1

45. **Every framing must carry the memoryless clause IN the scenario**
    ("tomorrow's status depends only on today's"), most of all in settings
    where reality is non-Markovian (machine aging). "Model as a Markov
    chain" imposes the assumption by directive; the scenario should convey
    it.
46. **Verification steps must be non-circular:** checking pi1 + pi2 = 1
    after defining pi2 = 1 - pi1 verifies nothing — check the ORIGINAL
    equation instead (pi1*p vs pi2*q numerically). Also flag rounding at
    the truncation point ("= 0.7083, rounded to four decimals") when the
    question prescribes a precision.
47. **Module-header and docstring citations must agree** (Ross Ex. 4.1/4.3
    vs 4.1/4.8 drew a provenance finding); one source of truth, copied.

### Cycle: two_step_transition_probability c1 (2026-08-06) — accepted c1

48. **Compressed check steps still need one worked constituent:** when a
    verification step reuses a method "the same way", show at least one of
    its constituent products (or say explicitly that the nine products
    repeat Step 2's pattern) so the student can follow without recomputing
    blind. ALSO re-learned lesson 44 the hard way: the draft assert ceiling
    (0.61) sat BELOW the true reachable max (0.6550) — always run the scan
    BEFORE writing the numbers down.

### Cycle: absorbing_chain_time_to_failure c1 (2026-08-06) — accepted c1

49. **Asset scale must match the implied lifetime scale:** transition
    probabilities implying a ~7-week life should name a consumable or
    component (cutting tool, spindle, pump seal), not multi-year capital
    equipment (a CNC machine). Check what the sampled numbers IMPLY about
    the named object before naming it (kin of lessons 13/20).
50. **Name checks honestly:** re-evaluating the original equation with the
    solved values is a *consistency check* (catches arithmetic slips), not
    a "non-circular" verification (it cannot catch a wrong setup). Use the
    accurate term; reviewers audit the claim, not just the arithmetic.

### Cycle: system_reliability_topology c1-c3 (2026-08-06) — accepted c3

51. **Exact-decimal display chains, and name the rounding convention:**
    (a) when inputs are fixed-dp decimals, carry intermediates in exact
    Decimal arithmetic (products of 3-dp values ARE exact at 6 dp) so the
    gold chain equals a full-precision solve; (b) round the FINAL display
    HALF-UP via Decimal — float round() silently disagrees with every
    decimal convention at true ties (R2 found 181 tie points in a 331k
    space); (c) if ties are reachable, the question should state the
    convention. Never round an intermediate that feeds a later product
    unless the rounding is exact.
52. **Gloss specialized terms in the question** ("mission reliability —
    the probability of operating without failure over the run") rather
    than only in the docstring.
53. **Constants must cohere ACROSS an area's templates:** t8's
    reliability classes and t9's failure-rate windows x mission times
    imply each other (R = exp(-lambda*t)); check the implication before
    grounding two templates in the same constants family. Also: remove
    unused numeric givens (run_days) — decoys draw findings; and remove
    unused imports.

### Cycle: exponential_mttf_topology c1 (2026-08-06) — accepted c1

54. **Phrase the rounding convention uniformly across branches** (even when
    one branch is always exact, the asymmetry is visible), and in claims
    about constants windows say "within" rather than "inside" when a
    sampled endpoint coincides with the window boundary.

### Cycle: poisson_event_count authoring (2026-08-06) — harness catch

55. **The Answer line carries exactly ONE number.** Restating the event
    count k ("exactly 2 breakdowns ... is 0.2707") put a second numeric in
    the line and the parser keyed on k — H6 collapsed to 7 distinct
    "answers" (k = 0..6) across 300 seeds. Refer to sampled counts in
    words ("that exact breakdown count"), never digits, anywhere in the
    Answer line. (Sharpens spec R2 and Civil lesson 28.)

### Cycle: basic_eoq c1 (2026-08-06) — R1 major on assert envelope

56. **A big scan is NOT an analytic corner derivation** (lesson 9/44
    recurrence, sharpened): when the extremum is a monotone function of the
    sampled windows, DERIVE the corner draw by hand (R1 did: Q spans
    [100.0, 28284.3], outside my scan-based asserts — a 1-in-250k crash).
    Scans only confirm derivations. Also: measure quoted rates (rejection
    %, combo counts) — never estimate them into comments; and exclusion
    rationales for constants classes must state the ACTUAL disqualifying
    corner, verified per class.

### Cycle: basic_eoq c2 + epq_finite_production c1-c2 (2026-08-06/07)

57. **Display-precision wobble SCALES with the answer's magnitude:**
    rounding an intermediate to d dp perturbs a downstream root/product by
    a RELATIVE amount, so the absolute wobble grows with Q — derive the
    bound AT the envelope maximum, not at a typical scale (0.7 units at
    mid-scale became 2.65 at the fastener corner). Remedies, in order:
    carry the intermediate at more dp; floor the denominator by per-sample
    constraints; coarsen the answer grid (nearest ten) so a screened
    midpoint margin dominates the wobble with real margin. And reuse of a
    display string across templates must re-check the PREMISE it was
    written for ("purchased" component cannot be "produced in-house").

### Cycle: quantity_discount_all_units c1 (2026-08-07) — accepted c1

58. **Decision templates need ECONOMIC decisiveness, not just structural
    branching:** sample the decision-driving quantities around the EXACT
    break-even (solve for it per draw — closed forms that drop terms
    understate it), then verify by sweep that every comparison winner
    holds a real share (>= 15-20%). With naive ranges the deepest
    discount won 26,176/26,176 comparisons — a decision in name only.
    (Extends lessons 21/40 from structure to economics.)
59. **A docstring's dominance argument must be the ACTUAL binding
    constraint:** citing a bound that doesn't quite hold (b2/0.45) while
    a different mechanism (the D cap) makes the assert safe draws an R1
    finding even when the code is correct. State the real reason; QA it.

### Cycle: reorder_point_lead_time c1 (2026-08-07) — accepted c1; Area P1 complete

60. **Unit words must agree in number:** "a constant 1 weeks" (tau = 1)
    drew three findings. Pluralize via a precomputed word ("week" if n == 1
    else "weeks") EVERYWHERE a sampled integer meets a unit noun — check
    every f-string at its extreme values (kin of lesson 19).
61. **When a display chain wobbles but the true answer is exact integer
    arithmetic, bridge with the exact identity in the trace** ("R =
    lambda*tau - k*Q = ... = 105, exactly") — reviewers accept the wobble
    when the trace itself shows why the final value is exact. Design for
    exact-integer answers where the model allows it.

### Cycle: safety_stock_reorder_point c1 (2026-08-07) — accepted c1

62. **Bind a rounding convention to EVERY quantity the question requests,**
    not just the final answer: "state the safety stock" with no precision
    leaves the student's 457.3 vs the gold's 457.28 formally mismatched.
    Either prescribe it ("to two decimals") or drop the request.

### Cycle: newsvendor_normal_demand c1 (2026-08-07) — accepted c1

63. **Cap economic ratios between co-sampled prices:** independent
    sampling of c and p inside class windows admits 15x markups at the
    corners; add a per-sample markup cap (p <= ~4c for retail goods) —
    the numbers must satisfy commercial practice jointly, not just
    per-window (economic recurrence of lessons 12/22).
64. **State the optimality condition that turns economics into a
    quantile:** "P(D <= Q*) = CR, so Q* is the CR-quantile of demand" is
    one sentence and makes the pivotal step justified rather than
    recipe-like. When a 4-dp quantile is required, either give the value
    (t15 pattern) or name the tooling assumption.

### Cycle: qr_policy_one_iteration c1 (2026-08-07) — two blocking flags + relabel

65. **The final answer gets ONE rounding, and boundary screens must
    protect the ACTUAL rounding path:** rounding to 1 dp and then to whole
    units differs from direct whole-unit rounding on the [0.445, 0.49)
    fractional band — 4% of gold answers contradicted the question's own
    prescription while the screen guarded a path the code didn't take.
    Two independent reviewers found it; the 5-instance batch showed
    nothing. Also: use half-up (_hu) for EVERY displayed intermediate the
    question's rounding clause covers — Python round() is half-even.
66. **For Advanced iteration templates, prescribe PRECISIONS, not
    PROCEDURES:** state the coupled optimality system, the definitions,
    the symbol bindings, and the rounding rules — and let the solver
    assemble the iteration order. A fully enumerated recipe is
    Intermediate substitution no matter how many formulas it chains
    (lesson 41's prescribed-scheme corollary; balances lesson 29).

### Cycle: qr_policy_one_iteration c2 (2026-08-07) — blocking tie channel + clause ambiguity

67. **Float-repr half-up FAILS at true decimal ties — lesson 51's full
    generality:** whenever a rounded quantity's operands are exact
    decimals (int * 4-dp, differences of 4-dp values), the exact result
    can land ON a tie and repr-based rounding goes DOWN (6.0750 stored as
    6.074999...). Compute those roundings in Decimal from the displayed
    operand STRINGS. Also: assert that every programmatic str.replace
    patch actually landed — one silent miss shipped a known-broken line
    to my own QA sweep (which caught it: 798 residual violations).
68. **Precision clauses must NAME every quantity they cover:** "the
    normal-function values" defensibly excluded L(z); enumerate — "z,
    phi(z), Phi(z), and L(z) each to four decimals" — and itemize the
    list (a), (b), (c) rather than packing a run-on sentence.

### Cycle: qr_policy_one_iteration c3-c4 (2026-08-07) — accepted c4 (at the cap)

69. **Boundary-difficulty concepts: reconcile by blind-label majority and
    reallocate slots — don't oscillate.** Three R3 instances split
    I/A/I on the same de-scaffolded question; fighting reviewer variance
    with wording tweaks burns cycles. Adopt the majority label, move the
    Advanced quota to a concept whose construction is unambiguous
    (line-balancing station assembly), and record the reconciliation in
    the docstring. The slate is non-binding; the 4/4/2 ledger is what
    must hold.
70. **Check the implied operating regime against the textbook's implicit
    picture:** every t17 instance has cycle < lead time (orders always
    outstanding) — internally valid, but the derivation's usual mental
    model assumes otherwise. When a sampling design pushes ALL instances
    into a regime the grounding text treats as the exception, escalate it
    (kin of lessons 14/22/49).

### Cycle: takt_time_line_efficiency c1 (2026-08-07) — accepted c1

71. **Spell out the denominator of every DEFINED quantity and the reason
    for every integrality operation:** "time capacity of the stations"
    should read "N_min * takt per unit", and a ceiling deserves its
    one-line "stations must be whole, so round up". Exact-integer design
    (divisor-sampled takt) again eliminated the rounding-defect family
    outright — R2's exhaustive sweep found all 1,403 reachable
    percentage ties correctly half-up.

### Cycle: line_balancing_heuristic c1 (2026-08-07) — accepted c1 (Advanced concurs)

72. **Every screen the docstring names must be CODED or restated as a
    proven implication** ("N_min in {n, n-1} follows from the delay cap
    and per-station fit; verified by sweep" — not "screened"). State
    distinctness assumptions in the question when a rule's tie-break is
    otherwise undefined, even if ties are unreachable by construction.
    Validation of lesson 69: reallocating the Advanced slot to authentic
    construction (station assembly) earned a concurring blind label at
    cycle 1 — construction that IS the derivation beats prescription
    depth every time.

### Cycle: chase_vs_level_aggregate c1 (2026-08-07) — accepted c1; DOMAIN 2 COMPLETE

73. **State every zero-default and every integrality requirement
    explicitly** (I0 = 0 was the question's one free assumption; the
    LEVEL clause needed "smallest integer"), and when regime steering
    deliberately hollows out parts of a constants window, say so in the
    docstring rather than citing the full window. Also: prescribing a
    SIMPLIFIED variant of a textbook plan (gross-demand chase) is fine
    when the question says so explicitly — internal coherence beats
    fidelity to an unstated convention.

### Cycle: xbar_r_control_limits c1 (2026-08-07) — R1 physics 2/5; coherence redesign

74. **SPC spread must be DERIVED from a class-window sigma, never sampled
    independently of it:** R-bar = (2-5% of target) implied sigma
    fractions up to 2.4x the class's own cap — 98% of shaft draws
    violated the constants file the template cites (lesson 53's SPC
    recurrence, found by R1 at scale while both math reviewers scored 5).
    Also check what the quoted measurement RESOLUTION implies: micron-
    quoted data with millimetre sigma is gauging-inconsistent. And
    replace vacuous asserts with the real coherence screen — decorative
    asserts imply protection that does not exist.

### Cycle: xbar_r_control_limits c2 (2026-08-07) — accepted c2

75. **Display resolution must match credible GAUGE resolution per class:**
    0.01-micron (10 nm) coating quotes exceed eddy-current instrument
    reality even when statistically harmless — set dp per class from
    instrumentation practice (shaft microns OK, coating tenths of a
    micron). And keep the docstring's assert list in lockstep with the
    code (a listed-but-absent screen drew a finding even though the
    property held by construction).

### Cycle: xbar_known_sigma_classification c1 (2026-08-07) — two blocking flags

76. **Decimal exactness of a division depends on the DIVISOR's prime
    factorization (2^a * 5^b), not on the divisor being a nice integer:**
    sigma/3 never terminates and sigma/4 needs TWO extra digits — my
    "integer sqrt(n) implies exact" assumption shipped self-inconsistent
    printed equations in half the n=16 draws and a boundary-straddling
    gold answer. Derive each division's exact digit requirement; for
    graded ratios, compute in exact Fraction arithmetic and SCREEN the
    result away from every rounding boundary (also defeats the Decimal
    28-digit context misrounding true ties — R2's seed-3820 find).

### Cycle: chart_pair_selection c1 (2026-08-07) — no blocking, but a major

77. **In a BRANCHING template the branch decision must be load-bearing
    for the FINAL answer — screen for wrong-branch coincidence:** with
    R-bar and s-bar derived from one sigma, A2*R-bar and A3*s-bar both
    approximate 3*sigma/sqrt(n), so the WRONG chart pair reproduced the
    identical UCL_x at the prescribed precision in 18% of 20k draws
    (R2 at scale; all five shipped seeds re-solved exactly). A
    final-answer grader would then score wrong-branch solutions correct
    — the very concept the template tests goes unmeasured. Fix: compute
    the wrong-branch answer per draw and reject-and-resample on
    coincidence (lesson 58's decisiveness principle, extended from
    economic comparisons to structural branches). Draw the branch
    OUTSIDE the resample loop or branch-dependent rejection rates skew
    the intended 50/50 mix. Companion finds: sample AWAY from the
    textbook's own ambiguity band (Montgomery's "n > 10 or 12" — n = 12
    satisfies one reading and not the other; large window now starts at
    13, R3), and quote software-reported statistics at software
    precision (R-bar at dp coarsened sigma-coherence cross-checks up to
    9.5% in the dp=1 class; both statistics now at dp+1, R1).

### Cycle: chart_pair_selection c2 (2026-08-07) — accepted c2

78. **A decisiveness screen is only as strong as the GRADING MODEL it
    assumes — state that model in the docstring:** the v2 screen
    guarantees the wrong-branch answer differs, but in ~42% of draws by
    only 1 ulp (all three c2 reviewers converged on this from different
    angles). Under this pipeline's exact-match parser that fully
    discriminates; under any tolerance-based grader it would not. When
    a cheap margin exists, prefer rejecting coincidences AND near-
    coincidences; when the 1-ulp floor is structural (two estimators of
    the same 3*sigma/sqrt(n) quantity), document the exact-match
    assumption so a future tolerance-graded reuse re-screens with a
    margin.

### Cycle: arl_beta_mean_shift c1-c2 (2026-08-07) — redesigned to earn Advanced, accepted c2

79. **Boundary screens silently NARROW the sampled parameter window —
    enumerate the SURVIVING support and document that, not the
    sampling window:** 4 of 11 sampled k values were rejected by the
    Phi/ARL tie screens for EVERY target, so the documented [0.58,
    0.68] window overstated what ships ({0.61, 0.63-0.68}) and two
    reviewer seeds shared identical numeric chains. All three c2
    reviewers independently hit this from different angles. When the
    parameter space is small, run the full enumeration yourself at
    authoring time: it also proves loop-exhaustion impossibility and
    yields the TIGHT realized bands for the docstring (my eyeballed
    band edges were never attained, and a claimed 0.3 band gap was
    actually 0.2 — docstring invariants must be enumerated, not
    estimated). Companion (lesson 41 confirmed): the c1 blind label
    dispute (Intermediate vs declared Advanced) was resolved by
    REDESIGN, not relabel — three full OC evaluations + a margined
    design selection earned a concurring blind Advanced in c2, and
    capping beta via the design windows simultaneously killed the c1
    latent exact-Phi divergence hazard.

### Cycles: ppm_nonconforming c1-c2, p_chart c1 (2026-08-07) — both revised

80. **A prescribed intermediate-rounding chain is a GRADING TRAP unless
    the question pins it AND the generator screens for path agreement:**
    three templates in a row hit the same class — t26 (2-dp z before
    the table read: exact-CDF solver lands up to 689 ppm away in 67%
    of draws), t27 (limits from rounded se: full-precision solver off
    by 1 ulp in 2/5 shipped seeds — R3 scored clarity 3 and the gate
    failed), t29 (sum-of-rounded-terms vs round-of-exact-sum). The
    durable pattern: (a) state the chain explicitly in the question
    ("using this rounded standard error"), AND (b) reject draws where
    the legitimate alternate path rounds to a different displayed
    value, so both paths coincide in every emitted instance. Wording
    alone leaves exact-match grading punishing correct fuller-precision
    work; screening alone leaves the prescription implicit. Also from
    this batch: never introduce a scenario phrase without checking the
    class window against the REAL process range (my v2 'decorative
    anodized layer' at 20-200 um drew a c2 blocking — lesson 75 applies
    to phrase swaps, not just dp choices), and blind difficulty labels
    on boundary templates oscillate (t26 I-then-E): strengthen the
    construction rather than argue the label (lessons 41/69).

### Cycles: t26 c2-c3, t28 c1, t29 c1, t30 c1 (2026-08-08) — the realism-and-paths batch

81. **Claims about SPECIFIC industrial practice must be verified against
    the actual standard, not invented from plausibility:** three
    successive coating phrases died under expert review — 'decorative
    anodized layer' (real: 5-25 um vs the 20-200 um window),
    'two-sided galvanizing spec' (ISO 1461/ASTM A123 are minimum-only,
    AND real hot-dip COV is 15-30%, incompatible with any SPC class
    window here), and 'extra epoxy thickness is not a defect' (SSPC-PA
    2 bounds DFT both ways; over-thick epoxy mud-cracks). Same class of
    kill: a contract 'expecting at most 20000 nonconforming per 20000-
    unit run' (cap allowances at AQL-like fractions of the lot/run).
    When a scenario needs a domain fact, either anchor it to a standard
    the reviewer can check (MIL-A-8625 ranges, declared-content minima,
    grinding cleanup allowances, resistor tolerance bands) or drop the
    scenario. Also from this batch: lesson-80 path screening must cover
    EVERY quantity on the answer path, including the final sum's
    operands (t28: I screened the roots but not the exact revised
    center line carried into the sum — construct intermediates EXACT
    when a grid permits, which beats screening); and model-framing
    words are load-bearing — 'this lot is p% nonconforming' implies
    type-A hypergeometric, 'the process runs at p%' makes type-B
    binomial exact (t29 blocking, N >= 10n violated inside MIL-STD
    code-letter bands).

### Cycle: ppm_nonconforming c4 (2026-08-08) — DISCARDED at the cycle cap

82. **Know the PRINTED precision of every table you prescribe — a 4-dp
    read from a 5-decimal table is a DOUBLE ROUNDING with its own tie
    set:** Montgomery Appendix Table II prints Phi to FIVE decimals;
    prescribing "read the CDF to 4 decimals" makes a table-following
    student compute round4(round5(Phi)), which diverges from
    round4(Phi) exactly where the 5th decimal is a boundary-crossing 5
    (z = 1.58: 0.94295 -> 0.9430 vs 0.9429; z = 1.88). My 0.03e-4
    screen was sized for direct 4-dp ties only — the double-rounding
    tie set needs ~0.055e-4, or the explicit screen
    round4(round5(p)) == round4(p). This killed t26 at the cap (spec
    §5: discard and replace, never force-accept). Immediate follow-ups
    that ARE the lesson: (a) retro-audit every accepted template that
    reads a printed table at reduced precision (t24 audited
    exhaustively over its finite shipping support: clean); (b) when a
    replacement concept exists that avoids the hazardous dependency
    entirely (the t26R sigma-reduction design needs NO normal table),
    prefer eliminating the hazard class to screening it; (c) grounding
    lines must state the table's ACTUAL printed precision. Cap
    post-mortem for the report: 3 of 4 cycles went to invented-realism
    defects (lesson 81) — the numerics were exact from c1.

### Cycle: sigma_reduction_for_cpk (t26 replacement) c1 (2026-08-08) — revised

83. **A DISPLAYED intermediate must be formatted at ITS OWN precision,
    not the precision of the values it came from:** I formatted the
    limiting distance d_min at the SPEC precision (whole microns) when
    it is a difference between a 1-decimal mean and a whole-number
    limit — so 46% of draws printed "d_min = 12" for an exact 11.6 and
    the next line's division was arithmetically false, even though the
    graded answer (computed from the exact value) was right. Both
    reviewers who saw it blocked. Two durable habits: (a) derive each
    display precision from the quantity's OWN construction
    (max over its operands' precisions), and (b) assert that the
    formatted string round-trips to the exact value, then feed the
    DISPLAYED string into the next step — the same round-then-recompute
    discipline lesson 65 applies to answers, extended to every printed
    intermediate. Related: when a docstring says a value is computed
    "from the displayed X", make the code literally do that; the
    doc/code drift was the defect's mechanism, not just its
    description.

### Cycles: t26R c2, t28 c3, t30 c3 (2026-08-08) — the diversity-and-entailment batch

84. **A template's ANSWER space can collapse even when its question
    space looks rich — measure the answers, not the surface:** t28
    emitted 4,671 distinct questions but only 18 distinct answers (top
    three = 55%), because the graded value depended on ONE constructed
    parameter drawn from a small grid, and the path-agreement screen
    then deterministically killed 58% of that grid. Two habits: (a) put
    a distinct-answer count and modal share in the authoring sweep,
    never just H6's >= 10 threshold; (b) when exactness forces a grid,
    pick the parameter whose arithmetic admits the FINEST grid (here
    m-1 = 24 = 8*3 allows eighths, while m-1 in {19, 49} allows only
    integers) and widen the range as far as realism permits.
85. **Every explanatory clause must be ENTAILED by what the generator
    screens, not merely observed to hold:** t30's "most lots at p2 are
    rejected" was true in all 23,509 reachable draws but guaranteed by
    nothing, so any later loosening of an unrelated screen would
    silently ship a false claim — the same failure mode as the c2
    "rising limb" text, one step earlier in its life. Add the screen
    that makes the sentence true by construction. Corollary from the
    same cycle: if a solution step must invoke an assumption to be
    valid, that assumption belongs in the QUESTION (t30 scoped
    rectification to rejected lots, then Step 4 quietly extended it to
    accepted lots' samples — the (N-n)/N factor was underivable from
    the stem as written).

### Round: t26R c3 / t28 c4 / t30 c4 (2026-08-09) — the stale-evidence round

86. **REGENERATE THE REVIEWER EVIDENCE PACK AS PART OF THE PATCH, NEVER
    AS A SEPARATE STEP:** I patched three templates, then launched nine
    reviewers against instance files that two of the three sweeps had
    never rewritten — one sweep died on a parsing regex before its
    write step, the other was an ad-hoc diversity script with no write
    step at all. Six reviewer-runs were spent certifying code that no
    longer existed. Every one of the six detected it (the tell is
    always the same: regenerate the seeds and diff), which is a real
    endorsement of the fresh-context panel, but the cost was a full
    review round. Make instance regeneration the LAST statement of the
    patch script itself, and assert the pack is newer than the source
    file before dispatching reviewers.
87. **When a fix is reverted, record the measurement that killed it:**
    two t26R c4 candidates were tried and backed out — round 5-micron
    drawing callouts (starved the Cp premise screen: the snap moved
    realized ratios more than the screen tolerated) and a dp+1
    sigma_max (collapsed the Cpk* = 1.67 branch from ~33% to 1.3% of
    draws). Both reverts are now documented IN the docstring with their
    numbers. A bare revert invites the next author — or the next
    reviewer — to propose the same change again; a revert with its
    measurement is a closed question.

### Round: t28 accepted c4, t26R c4 (2026-08-09)

88. **A boundary screen must never EXEMPT the exactly-on-grid case — that
    case is the defect, not the safe one:** I wrote both directional
    screens as `if fpart != 0 and fpart < eps: continue`, reasoning that
    a value sitting exactly on the rounding grid needs no protection
    because rounding it is a no-op. The opposite is true: under a
    ceiling instruction, exact-on-grid is precisely where a solver's
    last-bit float error decides the answer. (1 - 2.135/2.44)*100 is
    12.5 exactly in rationals and 12.50000000000001 in float64, so the
    ceiling gives 12.5 or 12.6 depending on arithmetic. 1.478% of draws
    flipped for an ordinary double-precision solver. Screens are now
    two-sided with no exemption, on the floor as well as the ceiling —
    and a pleasant consequence is that the "(rounded up)" annotations
    became true by construction, since no exact value survives.
    Corollary for every future template: after any directional-rounding
    design, RE-SOLVE THE WHOLE TEMPLATE IN FLOAT64 exactly as the
    question instructs and diff against gold. Exact-rational agreement
    is necessary but not sufficient; the grader's arithmetic is what
    ships.
89. **Grounding "typology only" needs a data check, not just a prose
    check:** t28 emitted 100-board inspection units with T = 516 — the
    exact total AND exact unit definition of the source's worked
    example, differing only in m. Prose was original; the DATA was not.
    A one-line exclusion screen fixes it, but the lesson is to diff
    emitted parameter tuples against the worked examples of the cited
    section, not merely to avoid copying sentences.

### Domain 3 complete (2026-08-09): t26R accepted, 10/10

90. **Verify the SECTION NUMBER, not just the book and chapter — and when
    a citation is wrong, grep for the same string across every template
    that shares the source:** both Q2 templates cited Montgomery Sec. 8.2
    for the capability ratios; 8.2 is the histogram/probability-plot
    section, and Cp/Cpk are 8.3.1/8.3.2 (eq. 8.9, with Table 8.3 giving
    exactly the 1.33/1.50/1.67 target set the template uses). The
    substance was right and the reviewers confirmed the development
    verbatim, so nothing a solver sees was wrong — but the grounding line
    is the audit record a human expert will check first, and the SAME
    wrong string had propagated into an already-accepted template
    because I copied the docstring skeleton. Post-acceptance
    documentation remediation is cheap and safe (no emitted text
    changes); a wrong citation discovered by a certifier later is not.

### Stage D audit of Domain 3 (2026-08-09) — FAIL, remediated

91. **A "branching" template only branches if the BRANCH CHANGES THE
    GRADED ANSWER — measure it, don't declare it:** t27 carried a
    [BRANCHING] tag and a genuine regime decision (LCL floored at zero
    or not), and both regimes were narrated correctly — but the graded
    quantity was the UCL, which is computed BEFORE the floor and is
    therefore identical either way. A solver who never notices the
    floor scores full marks. The Stage D auditor measured this over
    2,000 seeds and found the same hole in t30's verdict branch,
    reducing the domain from a declared three branching templates to
    one. Fix: grade a quantity the regimes compute DIFFERENTLY — here
    the width of the working band (floored: UCL - 0; live: 6*se),
    verified answer-invariant in 0 of 20,000 draws afterwards. The
    check is one line and belongs in every branching template's
    authoring sweep: apply the OTHER regime's formula and assert the
    answer moves.
92. **An independent auditor with no stake beats the author's own
    accounting:** I had ruled my stale-evidence round VOID and counted
    four valid cycles for t26R. The auditor rejected that — I had
    folded that panel's code-level findings into the next cycle, so I
    took the benefit while disclaiming the cost, and the honest record
    is five dispatched / four certifying, a cap overrun with cause. It
    kept the template (gate-clean at acceptance, author-side bug) but
    the accounting stands as an overrun. It also found two things every
    reviewer and I had missed: a wrong section citation in t24 and an
    UNDISCLOSED 19-value answer ceiling there — worse than the 69-value
    one I had disclosed in t28. Self-audit finds what you thought to
    look for; that is the argument for the fresh-context Stage D.

### t27 c4 (2026-08-09) — a patch that broke the sentence it was fixing

93. **READ BACK THE EMITTED TEXT AFTER EVERY PATCH — a sweep verifies
    what you thought to check, and a string patch can leave a wreck the
    numbers never see:** my c4 edit replaced only part of the stem
    sentence, leaving "the distance from the lower limit actually in
    force after the zero floor is applied, up to the working lower
    limit up to the upper control limit" in 100% of instances. One
    reviewer called it blocking (the mangled appositive was the ONLY
    definition of an invented term), another major. My 20,000-seed
    sweep passed cleanly the whole time: it checked every number, and
    it even asserted the OLD bad phrase was absent — but nothing
    asserted the NEW phrase read correctly, and I never printed a
    single generated question to look at. Two habits from this: assert
    the exact expected wording after any stem edit, and always dump one
    full question+solution to the terminal and actually read it before
    dispatching reviewers. The cheapest reviewer in the pipeline is
    your own eyes on one instance.
94. **Prefer the source's vocabulary to invented terms:** "working
    band" and "working lower limit" appear nowhere in Montgomery Ch. 7;
    I coined them to make the floor branch answer-load-bearing, which
    forced the stem to define one invented term using another — and put
    the whole item's solvability on a single fragile appositive. Asking
    for "the upper control limit minus the lower control limit after
    the zero floor has been applied" needs no glossary and cannot be
    garbled into circularity.


### t27 c5 (2026-08-10) — a leak that moved twice

95. **A leak closed by giving the regimes different windows does not get
    closed — it MOVES to whatever those windows differ in.** c3 found
    the regime readable off n, so I gave every n a plan on both sides;
    c4 then enumerated the state space and found D alone separated the
    regimes with 100% accuracy, because D = p-bar*m*n and I had handed
    the two regimes disjoint p-bar windows at similar m*n. Same defect,
    new coordinate. The structural fix is to stop pre-labelling: give
    BOTH regimes the same plan set and draw the parameter from a window
    straddling that plan's OWN crossover, so the regime is a
    consequence of where the draw lands rather than a property of the
    window it came from.
96. **Measure the leak instead of arguing about it: enumerate the
    reachable states, weight them for the rejection sampling, and report
    the best single-feature classifier's accuracy as a number.** "The
    regime is not readable off a surface feature" is an assertion; "the
    best threshold rule on D scores 0.679, on p-bar 0.610, on n 0.565,
    against 0.500 for a coin and 1.000 for the previous design" is
    evidence a reviewer can reproduce or refute. The weights are NOT
    uniform per plan: under reject-and-resample a plan's surviving mass
    is proportional to (survivors / window size), so a naive uniform
    enumeration misreports the attack.
97. **Search the feasible design family before claiming a design is
    good, and report where the optimum is.** Seven plan sets x eighteen
    window rules put the floor at 0.678; the shipped design sits at
    0.679. That turns a soft claim into a bounded one, and it surfaced
    WHY the bound exists: exactness (m*n must divide 10^4) with m >= 20
    admits only m in {20, 25, 40, 50}, and the crossover
    D = 9mn/(9+n) ~ 8.4m therefore lands in four m-clusters with no
    admissible plan between them. A constraint imposed for one reason
    (exact decimals) silently bounded something else (how well the
    regime can be hidden) — worth checking whenever a design feels
    stubborn.
98. **Both wider and narrower windows made the leak worse, for
    different reasons.** Wider windows raise the mean separation between
    the regimes' marginals; narrower ones let the decisiveness screen
    (|LCL| >= 0.0005) eat exactly the overlapping middle. A screen that
    removes a band around the branch boundary is removing the region
    where the regimes are indistinguishable — budget for that when
    sizing the window.


### t28 c5 (2026-08-10) — de-scaffolding, and what it paid for

99. **When a template blind-labels Easy but its subject matter is not,
    the problem is usually scaffolding, not content.** t28 was declared
    Intermediate through four cycles and blind-labelled Easy five times.
    The subject — trial limits, an out-of-control assessment, revision
    after removing an assignable cause — is Intermediate material. What
    made it Easy was that the stem pre-decided every judgment in it:
    which unit was out, that its cause was assignable, that no other
    unit was outside. Removing those three sentences, and giving the
    solver only the largest and smallest counts, turned a substitution
    exercise into a decision that selects the answer — without changing
    the physics, the source, or a single formula.
100. **A "structural residual" may be a cost of the scaffolding rather
    than of the exactness discipline you blamed it on.** I had disclosed
    t28's 69-value answer ceiling as the honest price of provable path
    invariance. De-scaffolding took the same template, with the same
    path-invariance screens, to 328 distinct answers (modal 2.5%,
    top-10 20% against the old 7.6% and 49%). The ceiling came from the
    graded answer depending on one sampled scalar — which is the same
    fact that made the early steps skippable. Two symptoms, one cause;
    fixing the difficulty defect dissolved the diversity defect. Worth
    asking, before disclosing any residual as structural, which design
    decision actually produces it.
101. **Not every surface correlation is a leak — check whether the
    attacking feature is a COARSE VERSION OF THE TESTED COMPARISON.**
    t27's old leak was "D <= 178 -> floored": D is an input the concept
    never asks you to compare against anything, so a solver using it had
    understood nothing. t28's residual is c_max/c-bar at 0.746, and the
    true crossover is c_max/c-bar = 1 + 3/sqrt(c-bar) — the ratio rule
    IS the tested judgment with sqrt(c-bar) replaced by a constant, and
    it is wrong a quarter of the time. Same measured number, entirely
    different meaning. Report both the figure and which kind it is;
    a reviewer cannot tell them apart from the number alone.


### t27 c5/c6 (2026-08-10) — the leak that could not be closed

102. **The feature family you sweep IS your claim — so state the family,
    never a universal.** I wrote "NO SURFACE FEATURE REVEALS THE REGIME"
    in capitals on the strength of a sweep over seven features. A
    reviewer then classified the regime at 91.4% from D/m — a ratio of
    the two integers printed in the stem, formed by one division. My
    sweep had included the derived feature m*n, so derived combinations
    were plainly in scope; I just never enumerated them. Sweep ratios,
    products, differences and residues of every stem quantity, and write
    the claim as "the best rule over THIS family scores X", not as an
    absolute.
103. **Before tuning a design against a leak, check whether an invariant
    bounds it.** The regime here is p-bar vs 9/(9 + n); in the units a
    solver most naturally forms (n*p-bar = D/m) the crossover is
    9n/(9 + n), which tends to 9 and never leaves [7.35, 8.84] for ANY
    admissible plan. That is a two-line limit calculation, and it proves
    no plan selection can hide the branch. I spent three review cycles
    moving the leak from n to D to D/m instead of doing it. When a
    branch boundary has a closed form, take the limit FIRST: if the
    boundary is asymptotically constant in some natural coordinate, the
    branch is unhideable in that coordinate and no amount of window
    tuning will help.
104. **An optimality claim resting on an enumeration is only as good as
    the enumeration.** I claimed 67.9% was "the OPTIMUM of the feasible
    family" because "m*n must divide 10^4 with m >= 20 admits only
    mn in {1000, 1250, 2000, 2500, 5000, 10000}". It also admits 500 and
    625, and m up to 250 — and the plan I had missed, (20, 500), sits
    exactly in the gap my argument said was empty. Adding it alone drops
    the figure I called optimal. Enumerate divisors programmatically;
    never by hand, and never inside the argument that depends on them.
105. **Tuning against one metric can move another the opposite way.** I
    measured that both wider and narrower windows raised the D-leak, and
    concluded the window was optimal. Over that same sweep the D/m leak
    fell monotonically as the window narrowed — from 0.971 to 0.879 —
    so I had tuned a two-sided trade against one side of it. Optimise
    against the MAX over the feature family, never against one feature.
106. **Withdrawing a claim is a legitimate fix, and sometimes the best
    one.** t27's branch could not be made honest, so it stopped being
    claimed: the zero floor stays in the trace because it is part of the
    procedure, but it no longer selects the graded answer and the
    template is not counted toward the branching quota. The defect
    disappeared, and so did the constraint the branch machinery had
    imposed — the reachable state space went from 191 to 1,221 and
    distinct answers from 133 to 983. A claim you cannot support is a
    liability twice over: it fails review, and it distorts the design
    that was trying to support it.


### t27/t28 c7-c8 (2026-08-10) — the claims, not the code

107. **The single most reliable defect class in this branch was not bad
    code — it was TRUE-SOUNDING CLAIMS ABOUT code that nobody had
    measured.** Across cycles 5-8, reviewers falsified seven of my
    assertions: "no surface feature reveals the regime" (twice, on two
    templates), "the optimum of the feasible family", "exactly these
    eight plans", "the tell is gone", "c_max is drawn freely", and a
    path-agreement guarantee the screen did not actually enforce. In the
    same cycles, independent re-solves found the ARITHMETIC exact every
    single time — including two exhaustive enumerations of an entire
    reachable support. The lesson is not "check your arithmetic"; it is
    that a docstring sentence asserting a property is a claim requiring
    evidence exactly as much as a number is, and it is far easier to
    write than to verify. Where a claim cannot be cheaply re-measured,
    do not make it.
108. **A fix can open a hole that the property it replaced was hiding.**
    While t28's revised centre line divided exactly, the rounded value
    and the exact quotient were the same number, so a path-agreement
    screen built from the rounded one covered both. The moment c7 pinned
    a rounding instead, those became different numbers and the screen
    silently stopped covering 22% of one regime — with no test failing,
    because the test was written against the old invariant. After
    replacing an exactness guarantee with a pinned rounding, re-derive
    every screen that was relying on the guarantee.
109. **Rejection sampling leaks the branch into the marginal of whatever
    it resamples.** t28 fixed the regime and m outside the loop and
    redrew T inside; because acceptance rates differ by regime, T's
    accepted marginal carried the regime at 0.727 accuracy — 78 of 169
    reachable T values were near-deterministic. Nothing in the sampler
    looked wrong. Whenever a quantity is redrawn inside a loop whose
    acceptance depends on a variable fixed outside it, that quantity
    becomes a tell; measure the marginals per branch, not just the
    screens.
110. **State the mechanism, not the measurement, in anything that has to
    stay true.** I put leak accuracies in a docstring three times and
    they went stale three times — the last within one cycle, because the
    screens I added to fix a different defect moved the number from
    0.727 to 0.549. Mechanisms ("rejection sampling prints the regime
    onto the resampled marginal") survive code changes; percentages do
    not. Percentages belong in the dated cycle record.
111. **Retain dead screens, but LIST them as dead.** Six of t28's
    in-loop filters were provably unreachable over the whole support.
    Deleting them would be wrong — a later widening of any window makes
    them live again, and that is exactly when a quietly-removed guard
    costs something — but presenting them as active protection is a
    false claim of the same family as the rest. Keep them, name them,
    and say which ones cannot currently fire.
