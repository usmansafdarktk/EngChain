# Stage D Domain Report v2 — Industrial Engineering / OR, Domain 3: Quality & Reliability Control

**Spec:** `docs/pilot_template_authoring_spec.md`, Stage D
**Auditor:** Domain Auditor agent (fresh context; did not author or review any of these templates, and did not write the v1 report)
**Date:** 2026-08-14
**Supersedes:** `domain_report_superseded_2026-08-09.md` (verdict FAIL-remediable) **in full.** That document's body was treated here as dated evidence, not as truth; every one of its findings was independently re-measured.

**Inputs:** 10 accepted template sources; `constants.py`; BOOKS.md §3/§4/§5; the 11 relevant review logs (10 accepted + `template_ppm_nonconforming_spec.jsonl`, the discard); the on-disk Montgomery ISQC 7e text layer; `evaluation/engineering_parser.py`.

**Evidence generated independently by this audit:**
blind instances at seeds 301–303 for all 10 templates, with all difficulty labels formed and written down **before any template source or docstring was opened**; a 2,000-seed sweep per template measuring distinct answers, distinct questions, modal share, top-10 concentration and P(duplicate answer in a random 5-instance pack) at 200,000 Monte-Carlo packs each; exhaustive enumeration of t24's entire reachable answer space and per-candidate ARL bands; branch-mix sweeps for all five candidate branching mechanisms; a 5,000-seed assertion-conformance run per template (50,000 draws total); harness re-run on all four files from a clean process; Stage E pack verification at seeds 201–205 through `evaluation/engineering_parser.py` using the harness-identical call; pairwise lexical-overlap measurement across all 45 template pairs; and grounding checks located line-by-line in `extracted/montgomery_isqc_7e.txt`.

---

## VERDICT: FAIL — remediable

**Everything the v1 report blocked on has been closed, and I confirm each closure by measurement:**

| v1 required action | Status | This audit's independent measurement |
|---|---|---|
| 1. Restore the 4/4/2 split without force-labelling | **CLOSED** | Blind relabel at seeds 301–303 returns **4E/4I/2A with 0 mismatches in 10** (§3.2). t28 earned Intermediate by de-scaffolding, not by relabelling. |
| 2. Restore a third answer-affecting branching template | **CLOSED** | **3 of 3** measured answer-affecting: t23, t28, t24 (§2.4). t27's branching claim correctly withdrawn. |
| 3. Correct t24's grounding citation | **CLOSED** | t24 now cites Sec. 6.2.6 / 6.2.7; both located in the on-disk source. **10/10 citations verified, 0 defects** (§4). |
| 4. Disclose t24's 19-value answer ceiling | **CLOSED (partially defective)** | Exhaustive enumeration confirms **exactly 19**; the disclosed modal ~10% and P(dup)~50% match my measured 9.95% and 50.7%. But the same disclosure paragraph carries a **falsified band claim** — see Finding A. |
| 5. Back-fill missing review-log records | **CLOSED** | Every cycle now has a record; all four back-filled records carry `reconstructed: true` and an honest note, two of them explicitly stating that unpreserved score vectors are **null, not reconstructed from memory** (§8). |
| 6. Report t26R as 5 dispatched / 4 certifying, not a void | **NOT CARRIED FORWARD** | The ruling survives only in the superseded v1 report. See Finding D. |

**What still blocks.** No correctness, realism, format or determinism defect was found anywhere in this audit: 10/10 harness pass, 0 assertion fires in 50,000 draws, 10/10 grounding citations confirmed, no isomorphic pair, area quotas exact, Stage E clean. The blocking items are three, and all are of the class this branch has repeatedly produced — **claims and conformance, not code**:

- **A. t24's docstring states a measurably false "enumerated" result** and contradicts itself within the same paragraph (§7.2).
- **B. t28's answer-space disclosure has been deleted outright** and the code now carries a dangling cross-reference to the removed note (§7.3).
- **C. t26R violates spec R7**: its named physical data (IEC 60063 E12/E24 preferred-value series, resistor tolerance classes, the MIL-A-8625 Type III thickness envelope) are inlined module literals, not `constants.py` entries, and were therefore never seen by the Stage B Data Reviewer (§6). Spec §3 lists R7 among the requirements whose violation is "automatic rejection".

A single Stage C documentation-and-refactor cycle clears all three. **Stage E must not start until they clear.**

---

## 1. Inventory

| # | Template | File | Area | Declared difficulty | Cycles (rounds / panel-dispatched / certifying) | Reasoning-chain skeleton |
|---|---|---|---|---|---|---|
| t21 | `template_xbar_r_control_limits` | variables_control_charts.py:37 | Q1 | Easy | 2 / 2 / 2 | R̄ → D4/D3 range limits → A2 x̄ limits → σ̂ = R̄/d2 (3 steps, tabulated-constant substitution) |
| t22 | `template_xbar_known_sigma_classification` | variables_control_charts.py:183 | Q1 | Easy | 2 / 2 / 2 | Known σ → σ_x̄ = σ/√n → 3σ limits → scan 8 plotted means, count outside → standardize the extreme (4 steps) |
| t23 | `template_chart_pair_selection` | variables_control_charts.py:376 | Q1 | Intermediate | 2 / 2 / 2 | **n-driven chart-pair selection** → spread-chart limits from the chosen statistic → x̄ limits from the matching constant → σ̂ from the matching divisor (4 steps) |
| t24 | `template_arl_beta_mean_shift` | variables_control_charts.py:622 | Q1 | Advanced | 2 / 2 / 2 (+1 post-acceptance audit record) | z(n) = 3 − k√n for three candidates + far-tail negligibility → β per candidate → ARL₁ per candidate → **margined design selection** → geometric P(detect by sample 2) (5 steps, ~11 embedded values) |
| t25 | `template_cp_cpk_from_specs` | process_capability.py:25 | Q2 | Easy | 1 / 1 / 1 | σ̂ = R̄/d2 → Cp → Cpu, Cpl → Cpk = min + benchmark verdict (4 steps) |
| t26R | `template_sigma_reduction_for_cpk` | process_capability.py:248 | Q2 | Intermediate | **5 / 5 / 4 — documented cap overrun, see §8.3** | Current ratios → Cp-as-ceiling feasibility argument → identify binding d_min → **invert** Cpk = d_min/(3σ) for σ_max → percentage reduction with directional rounding (5 steps, inverse design) |
| t27 | `template_p_chart_limits_floor` | attributes_control_charts.py:63 | Q3 | Easy | **7 / 6 / 6 — cap overrun, c7 not dispatched (§8.2)** | p̄ = D/(mn) → binomial standard error → 3σ limits with the max(0,·) floor reported but not answer-determining (3 steps) |
| t28 | `template_c_chart_revision` | attributes_control_charts.py:305 | Q3 | Intermediate | **8 / 7 / 7 — cap overrun, c8 not dispatched (§8.2)** | c̄ = T/m → trial limits from √c̄ → **solver decides whether any unit is out of control** → if so revise from (T−c_max)/(m−1) and adopt the revised UCL, else adopt the trial UCL (4 or 5 steps) |
| t29 | `template_single_sampling_oc_point` | acceptance_sampling.py:32 | Q4 | Intermediate | 2 / 2 / 2 | Quoted MIL-STD plan → model X ~ Bin(n,p), accept iff X ≤ Ac → evaluate Ac+1 terms → sum (4 steps) |
| t30 | `template_aoq_ati_rectifying` | acceptance_sampling.py:234 | Q4 | Advanced | 4 / 4 / 4 | Quoted plan → Pa at p₁ → Pa at p₂ → **derive** AOQ from the rectification policy, evaluate both, resolve the non-monotone verdict → **derive** and evaluate ATI (5 steps) |

Discarded and replaced during Stage C: `template_ppm_nonconforming_spec` (Q2, Intermediate, 4 cycles, capped out on a Φ table-provenance defect) → replaced by t26R. Correctly executed per §5.3: never force-accepted, unresolved defect logged as feasibility evidence.

**§3 contract conformance.** All 10 emit `**Step X:**` markers, exactly one `**Answer:**` line whose final number is the asked quantity, stdlib `random` only, embedded physical-bounds assertions, and self-contained questions. R7 conformance is the exception — see §6. Copyright rule verified: t27 explicitly screens Montgomery Example 7.1's data (m = 30, n = 50, D = 347), and I confirmed those exact values in the source at `montgomery_isqc_7e.txt:37111` ("30 samples of n = 50 cans", "347 nonconforming cans", p̄ = 0.2313).

---

## 2. Diversity audit — measured, not asserted

### 2.1 Method

Two independent measures, rather than assertion: (i) the printed step-headline skeleton of each template, and (ii) pairwise **Jaccard similarity of high-frequency solution tokens** (identifiers appearing ≥ 100 times across 200 instances per template), over all 45 pairs.

### 2.2 Result: no isomorphic pair

The ten skeletons partition into ten distinct chains: tabulated-constant substitution (t21); known-parameter limits plus a classification/standardization terminal (t22); regime-selected constants family (t23); multi-candidate OC evaluation with margined design selection (t24); forward capability-ratio evaluation (t25); forward-then-**inverse** design with a feasibility argument (t26R); binomial-proportion limits with a domain-boundary floor (t27); Poisson limits with a **trial-versus-revise decision** (t28); cumulative-binomial OC evaluation (t29); two OC evaluations plus two **derived** expectation models and a comparative argument (t30).

**Measured closest pairs (Jaccard on solution tokens):**

| Rank | Pair | J | Resolution |
|---|---|---|---|
| 1 | **t21 / t23** | **0.494** | **DISTINCT — and this, not t25/t26R, is the domain's closest pair on measurement.** In the small-n branch (measured 1,004 / 2,000) t23's Steps 2–4 run t21's constants family in t21's order. Two things separate them and both are load-bearing: t23's Step 1 selection is enforced by a decisiveness screen (`variables_control_charts.py:476`) that rejects any draw where the wrong pair quantizes to the same UCL, so the choice changes the graded answer in **every** instance; and in the other 996 draws the chain runs on an entirely different family (A3/B3/B4/c4) against a different spread statistic. t21 contains no selection at all. |
| 2 | t29 / t30 | 0.271 | DISTINCT. t30's Steps 2–3 are two copies of t29's OC block, but t30 then withholds both result formulas from the stem and requires AOQ = Pa·p·(N−n)/N and ATI = n + (1−Pa)(N−n) to be constructed from the stated policy, plus a non-monotone comparison. Two new expectation models on a shared evaluation block is not a re-skin. |
| 3 | t22 / t27 | 0.253 | DISTINCT. Shared "centre line ± 3 × spread" vocabulary only; different spread estimator, different terminal (standardized z vs. a domain-floored limit). |
| 3= | t21 / t25 | 0.253 | DISTINCT. Shared σ̂ = R̄/d2 opener; t25's whole content is capability ratios against specification limits, which t21 does not contain. |
| — | **t25 / t26R** | **< 0.202** | **DISTINCT, and measurably NOT the closest pair** — contrary to v1 §2.2(a), which named it the domain's closest without measuring. It does not appear in the top eight. t26R's back half (Cp-as-ceiling feasibility argument, binding-side identification, inversion of Cpk = d_min/(3σ), directional-rounding discipline) has no analogue in t25, and the graded quantity is a design percentage, not a capability index. |

**No isomorphic pair found; the structural-diversity MUST is satisfied.**

### 2.3 Family-level observation (advisory, unchanged from v1 and re-confirmed)

The Shewhart move — centre line ± 3 × (spread statistic) — terminates **5 of 10** templates (t21, t22, t23, t27, t28), each with a different spread estimator (A2R̄, σ/√n, A3s̄, √(p̄(1−p̄)/n), √c̄) and a different superstructure. Not a violation; intrinsic to a domain whose Q1 and Q3 areas are both control-chart areas. Do not add a sixth if any Q1/Q3 template is ever replaced.

### 2.4 Branching — MEASURED (2,000-seed sweep per template)

| Template | Declared | Mechanism | Measured mix | Does the branch change the **graded** answer? | Credit |
|---|---|---|---|---|---|
| **t23** | ✔ | Subgroup size selects the constants family: A2/D3/D4/d2 + R̄ + σ̂=R̄/d2 vs A3/B3/B4/c4 + s̄ + σ̂=s̄/c4 | X̄-R 1,004 / X̄-s 996 | **YES — in 100% of instances.** Both candidate UCLs are computed and `assert ucl_x != ucl_alt` (`variables_control_charts.py:511`) makes the wrong pair give a different graded value by construction. | **STRONG** |
| **t28** | ✔ | The solver's own out-of-control assessment decides whether the chart is revised, and therefore which UCL is adopted | revise 1,004 / in-control 996 | **YES — in 100% of instances.** `assert (ans3 == ucl3) == (branch == "in_control")` and `assert uclr3 < ucl3` (`attributes_control_charts.py:611–616`) make the two regimes yield different graded UCLs by construction. Step counts differ too (5 vs 4), confirmed at seeds 201–205. | **STRONG** |
| **t24** | ✔ (docstring §Scenario) | Margined selection of the smallest adequate subgroup size among {9, 16, 25} | n=9 1,003 / n=16 832 / n=25 165 | **YES.** The graded answer is the selected candidate's ARL₁, and the three candidate bands are **pairwise disjoint by exhaustive enumeration**: [5.9, 8.3] / [2.6, 3.5] / [1.5, 1.9], with realized within-instance separations ≥ 3.3 (9 vs 16) and ≥ 1.1 (16 vs 25) — both figures reproduced exactly from the docstring's claim. | **MEDIUM–STRONG** |
| t27 | withdrawn | Sign of the computed LCL drives the max(0,·) floor | floor 617 / positive 1,383 | **NO** — `ucl4 = pb4 + k*se4` (`attributes_control_charts.py:191`) is computed identically before the branch; only Step 3's prose and the reported LCL differ. | TRACE-ONLY (correctly not claimed) |
| t30 | not claimed | Which quality level yields the worse AOQ (non-monotone AOQ curve) | p₂ 1,692 / p₁ 308 | **NO** — the graded ATI is computed at p₁ regardless. | TRACE-ONLY (correctly not claimed) |
| t26R | not claimed | Two scenario classes (hard-anodize / thick-film resistor) with identical chains | anodize 1,125 / resistor 875 | No | NONE (correctly not claimed) |

**Finding — the branching quota is MET.** **3 answer-affecting branching templates** against BOOKS.md §4's Gate-A-approved plan of three. Every branching claim the domain now makes (t23, t28, t24) survives measurement, and both withdrawn/unclaimed branches (t27, t30) are honestly labelled trace-only. This is the first time in this domain's history that the declared branching set and the measured branching set coincide.

**Caveat on allocation, not count (advisory).** BOOKS.md §4 named the three slots as Q1-#3, Q2-#6, Q3-#7. Delivered: Q1-#3 (t23) as planned; Q3 delivers via #8/t28 rather than #7/t27; Q1 supplies a second branching template (t24) that was not in the plan; and **Q2 carries no branching template at all** following the Q2-#6 discard. The count is met and the spec's ≥3 clause is a SHOULD, so this is not blocking — but the Final Report should describe the allocation accurately rather than implying the Gate-A slot plan was delivered as written.

---

## 3. Coverage audit

### 3.1 Area allocation — exact

| Area | Quota (BOOKS.md §3) | Delivered | Templates |
|---|---|---|---|
| Q1 Variables Control Charts | 4 | **4** | t21 E, t22 E, t23 I, t24 A |
| Q2 Process Capability | 2 | **2** | t25 E, t26R I |
| Q3 Attributes Control Charts | 2 | **2** | t27 E, t28 I |
| Q4 Acceptance Sampling | 2 | **2** | t29 I, t30 A |

**Area allocation matches the BOOKS.md §3 quotas exactly**, with the single documented substitution of Q2-#6 → t26R.

### 3.2 Blind re-label against §2.1 — **0 mismatches in 10**

**Method (auditable).** Three instances per template were generated at seeds 301–303 by a script that wrote **only the question and solution strings** to disk — never a docstring, never source. I read that file, formed and recorded a label for each template from the §2.1 axes (number of governing principles; presence of a regime decision that changes the applicable formula; whether a model must be constructed before substitution; step count), and only then opened the sources. Declared labels were read afterwards, from `grep "Difficulty:"`.

| # | **Auditor blind label** | Declared | Match | Rationale against §2.1 |
|---|---|---|---|---|
| t21 | Easy | Easy | ✓ | One principle (tabulated three-sigma factors); all four constants supplied in the stem; pure substitution; 3 steps. |
| t22 | Easy | Easy | ✓ | One principle (the sampling distribution of x̄ governs both the limits and the z); the 8-point scan is a comparison, not a second concept; 4 steps. |
| t23 | Intermediate | Intermediate | ✓ | Squarely §2.1's "regime decision that changes the applicable formula" — the whole constants family and the spread statistic switch on n; 4 steps. |
| t24 | Advanced (boundary) | Advanced | ✓ | Three distinct probability concepts (β from the shifted sampling distribution, ARL₁ as a geometric mean, the geometric two-sample tail) synthesized before a margined design search; β is not supplied and must be constructed. 5 numbered steps against the "≥6" guide, but Steps 1–3 each carry three parallel candidate evaluations (~11 embedded values). |
| t25 | Easy | Easy | ✓ | One principle (capability ratios); direct substitution; 4 steps. |
| t26R | Intermediate | Intermediate | ✓ | Two-plus coupled concepts (ratio algebra, a feasibility argument, an inversion) with no system construction; 5 steps — the middle of the band. |
| t27 | Easy | Easy | ✓ | One principle (binomial-proportion limits); the floor is a one-line domain check that does not change the graded quantity; 3 steps. |
| **t28** | **Intermediate** | Intermediate | ✓ | **The de-scaffolding worked, and I reached this independently.** At seeds 301 and 302 no unit is outside and the trial UCL is adopted (4 steps); at seed 303 the largest count exceeds the trial UCL, the chart is revised, and the revised UCL is adopted (5 steps). The solver must compute the trial limits, compare, and *decide* — a regime decision that changes which formula produces the graded answer, which is exactly §2.1's Intermediate criterion. Steps 1–3 are now load-bearing: skipping them leaves no way to know which limit to report. This is a substantive change from the pre-decided version v1 blind-labelled Easy. |
| t29 | Intermediate (low) | Intermediate | ✓ | A modelling step (map the acceptance event {X ≤ Ac} onto a cumulative binomial) plus a multi-term distributional evaluation — beyond "direct algebraic substitution" on the Mathematical Sophistication axis; 4 steps. Bottom of the band. |
| t30 | Advanced | Advanced | ✓ | Both result formulas (AOQ, ATI) are withheld from the stem and must be constructed from the stated rectification policy before any substitution, on top of two full OC evaluations plus a comparative argument; 5 numbered steps, same boundary allowance as t24. |

**Blind split: 4 Easy / 4 Intermediate / 2 Advanced. Declared split: 4E/4I/2A. Mismatches: 0 of 10.** The §2 quota is met, and it was reached by de-scaffolding t28 so it genuinely earns the slot — not by relabelling to fit the plan. This is the correct resolution of the v1 dispute, and it holds up under a fresh blind pass.

---

## 4. Grounding audit — 10/10, zero defects

Each citation was located line-by-line in `pilot/references/public/full_books_industrial_engineering/extracted/montgomery_isqc_7e.txt` (no fragment longer than a clause is quoted here; the file is never redistributed).

| # | Cited | Covers the content? | Located at |
|---|---|---|---|
| t21 | Ch. 6, Sec. 6.2 (X̄ and R charts) + App. Table VI | ✓ | Sec. 6.2 body; factors transcribed and derivation-verified in `constants.py:213–239` |
| t22 | Sec. 6.2.3, charts based on standard values | ✓ exact | heading at `:28413–28414` |
| t23 | Sec. 6.3, X̄ and s preferable when n is moderately large | ✓ **verbatim** | the "n > 10 or 12" guidance at `:29278` |
| t24 | **Sec. 6.2.6** (OC function) and **Sec. 6.2.7** (ARL) | ✓ **v1's miscitation is fixed** | "The Operating-Characteristic Function" at `:28718`; "The Average Run Length for the …" at `:29091`. The v1 report's Sec. 6.2.2 citation is gone. |
| t25 | Ch. 8, Sec. 8.3 / 8.3.1 / 8.3.2, eq. 8.9 | ✓ | "PROCESS CAPABILITY RATIOS" `:44580`, 8.3.1 `:44582`, off-centre 8.3.2 `:45512`; **eq. (8.9) located at `:45548`**, inside the Cpk = min development |
| t26R | as t25 | ✓ | as above |
| t27 | Ch. 7, Sec. 7.2.1 "Development and Operation of the Control Chart"; the LCL = max(0,·) convention; the np > 3.00 design floor | ✓ **all three, verbatim** | heading `:36873`; the LCL convention at `:36982`; "λ = np must exceed 3.00" at `:38197`, which I confirmed sits inside 7.2.1 (the only intervening heading is 7.2.1's own subsection "Design of the Fraction Nonconforming Control Chart") |
| t28 | Sec. 7.3 / 7.3.1 (c chart) **and** Sec. 6.2.2 (the preliminary-data / trial-limits / discard-and-revise workflow) | ✓ both | 7.3 `:39430`, 7.3.1 `:39528`; the assignable-cause / revise-limits workflow confirmed inside Sec. 6.2.2 (`:26754`–`:28413`). The second citation is unusual but correct: the revision workflow genuinely lives in Ch. 6, not Ch. 7. |
| t29 | MIL-STD-105E Tables I/II-A + Montgomery Sec. 15.2 / 15.2.2 type-B OC | ✓ | "The OC Curve" `:85925`; tables transcribed in `constants.py:261–310` with page citations |
| t30 | Sec. 15.2.4 Rectifying Inspection, AOQ eq. 15.4, ATI eq. 15.6 | ✓ **including both equation numbers** | 15.2.4 body `:85931`; **eq. (15.4) AOQ** and **eq. (15.6) ATI** both located inside that body; the non-monotonicity development that is t30's design point ("the AOQ curve rises, passes through a maximum, and descends") is present verbatim |

**Grounding defects: 0.** The v1 sweep for the same citation-class error was completed across all ten templates; nothing further was found.

---

## 5. Harness

`python pilot/harness/check_template.py <file>`, run from a clean process by this audit on all four files:

| File | Functions | `all_passed` | H1–H7 |
|---|---|---|---|
| variables_control_charts.py | t21, t22, t23, t24 | **true** | all clean |
| process_capability.py | t25, t26R | **true** | all clean |
| attributes_control_charts.py | t27, t28 | **true** | all clean |
| acceptance_sampling.py | t29, t30 | **true** | all clean |

**10/10 pass all seven checks.** Independently, I ran **5,000 seeds per template (50,000 draws)** outside the harness: **zero exceptions and zero assertion fires**, which is direct evidence for H7 far beyond the harness's 25-seed window and confirms every declared physical bound holds across the reachable support.

---

## 6. Constants and spec R7

### 6.1 Curated-window conformance — clean

Every drawn parameter lies inside its curated window, verified both by the templates' own post-loop guards and by my 50,000-draw run with zero fires:

| Template | Curated windows used | Verified |
|---|---|---|
| t21, t22, t23, t25 | `CONTROL_CHART_FACTORS` / `chart_factor()`, `SPC_CHARACTERISTICS[...]["target"]` | ✓ |
| t27 | `P_CHART_PBAR` (0.01, 0.15), `P_CHART_SUBGROUP_N` (50, 400), `SPC_NUM_SUBGROUPS` (20, 30), `SHEWHART_K_SIGMA` | ✓ — and the `(m, n)` plan table is **enumerated in code** from those windows (`_t27_admissible_plans`, `attributes_control_charts.py:45`) rather than hand-listed, so it cannot drift. I re-derived it: `[(20,100),(20,125),(20,250),(25,80),(25,100),(25,200),(25,400)]`. Two docstring claims about this table are **confirmed by measurement**: n = 50 is dropped, and the `SPC_NUM_SUBGROUPS` ceiling of 30 is genuinely unreachable (only m ∈ {20, 25} survive). Mean p̄ measured **0.0874** against the docstring's "about 8.7%". |
| t28 | `C_CHART_CBAR` (2.0, 25.0), `SPC_NUM_SUBGROUPS`, `SHEWHART_K_SIGMA` | ✓ — c̄ confined to [10.0, 25.0]; the 10.0 floor is a hardcoded design bound and is **disclosed as such**. m ∈ {20, 25} is correctly justified (the only values in `SPC_NUM_SUBGROUPS` dividing 100); the 3:1 weighting is disclosed at "measured 74.9%" and I measure **74.7%** over 5,000 seeds. |
| t29, t30 | `MIL_STD_105E_CODE_LETTERS_GII`, `MIL_STD_105E_SAMPLE_SIZE`, `MIL_STD_105E_SINGLE_NORMAL_AC` | ✓ — plan lists **derived at import time** from the transcribed tables (`acceptance_sampling.py:16–22`), never re-keyed; per-draw asserts re-check `n` against the table. Arrow cells (`None`) are correctly excluded. This is the strongest R7 pattern in the domain. |

The v1 report noted that t27 and t28 had been refactored for R7 and that the other eight had not been checked. **I checked all ten.** t29 and t30 are exemplary. t21–t25 are conformant on the data that matters (chart factors, characteristic windows). The problems are in t26R and in two dead curated constants.

### 6.2 **VIOLATION — t26R inlines named physical data (spec R7)**

Spec §3 R7: *"Parameterization pulls named physical data (materials, fluids, media, distributions, code values) from the branch `constants.py`, never inlined magic values."* Spec §3 lists R1–R7 violations as "automatic rejection".

t26R (`process_capability.py:229–244`) sources its **entire physical parameterization** from module-level literals:

- `_T26R_E24_5PCT` and `_T26R_E12_10PCT` — the **IEC 60063 E24 and E12 preferred-value series**, 32 and 16 nominal resistances, hand-listed;
- the tolerance classes `random.choice([5, 10])` and the E24↔5% / E12↔10% pairing rule (`:382`);
- `_T26R_ANODIZE["tsub"] = (48, 88)` and the `20 ≤ LSL, USL ≤ 110` micron band screen (`:424`) — the **MIL-A-8625 Type III producible envelope**;
- the 1.5-micron metrology floor (`:410`), attributed to ASTM B244/B487;
- `"sf": (0.005, 0.03)` for the resistor class, which is a **verbatim duplicate** of `SPC_CHARACTERISTICS["resistor resistance (ohm)"]["sigma_frac"]` in `constants.py:321`, copied rather than imported.

These are named standards data with real-world provenance — precisely what R7 exists to route through `constants.py`. `constants.py` contains **no** E-series entry and **no** MIL-A-8625 entry. Consequences:

1. **The Stage B Data Reviewer never saw them.** `data_review_log.md` covers `constants.py`; t26R was authored later as the Q2 replacement, so its standards data bypassed the §4 Stage B verification loop entirely. The citations exist only as code comments written by the Author.
2. **Drift hazard.** The resistor σ-fraction window is now stored in two places; a change to `constants.py` would silently leave t26R on the old value.
3. It is the only template in the domain in this position. t29/t30 show the correct pattern for exactly this kind of standards table.

**This is the audit's one hard-requirement violation.** The fix is mechanical: move the E12/E24 series, the tolerance-class pairing, the MIL-A-8625 envelope and the metrology floor into `constants.py` with inline source citations in the house style, import them, and have the Data Reviewer spot-verify per Stage B.

### 6.3 Dead curated constants (advisory, R7-adjacent)

`constants.py:332–337` defines `XBAR_R_SUBGROUP_N = (2, 10)` and `XBAR_S_SUBGROUP_N = (11, 25)` with a comment stating explicitly that they exist for *"the chart-type-selection branching template (Q1-#3)"* — i.e. for t23. **t23 does not import them.** It inlines `(4, 8)` and `(13, 20)` (`variables_control_charts.py:446–447`). I grepped the whole branch: **neither constant is referenced by any template in any domain.** The inlined windows are well-justified in t23's docstring (13 rather than 11, so every draw clears both readings of Montgomery's "n > 10 or 12"), so the *values* are right — but a curated constant that no template reads is an unverifiable artifact, and the divergence between the constant and the shipped window is undocumented on the `constants.py` side.

Similarly, t21/t22/t23/t25 each inline a per-class `sf` sigma-fraction sub-window; for the bottle-fill and coating classes these are **verbatim copies** of `SPC_CHARACTERISTICS[...]["sigma_frac"]` rather than reads of it (the shaft class is a documented deliberate narrowing). Same drift hazard, lower severity.

---

## 7. Structural residuals — every disclosure checked against measurement

2,000 seeds per template; P(duplicate) from 200,000 Monte-Carlo 5-instance packs.

| # | Distinct answers | Distinct questions | Modal share | Top-10 conc. | P(dup answer in a 5-pack) | Disclosed? |
|---|---|---|---|---|---|---|
| t21 | 1,981 | 2,000 | 0.10% | 1.0% | 0.5% | n/a |
| t22 | 240 | 2,000 | 1.1% | 9.5% | 5.4% | no (not needed) |
| t23 | 1,998 | 2,000 | 0.10% | 0.6% | 0.5% | n/a |
| **t24** | **19** | **631** | **9.95%** | **73.1%** | **50.7%** | **yes — see 7.2** |
| t25 | 121 | 2,000 | 2.1% | 17.1% | 11.0% | no |
| t26R | 433 | 1,949 | 0.9% | 7.5% | 3.3% | n/a |
| t27 | 724 | **1,388** | 0.65% | 5.6% | 2.1% | n/a |
| **t28** | **152** | 1,928 | 3.35% | 21.2% | 9.9% | **no — see 7.3** |
| t29 | 795 | 1,991 | 0.5% | 3.8% | 1.7% | n/a |
| t30 | 814 | 1,988 | 0.65% | 5.3% | 2.1% | n/a |

### 7.1 The domain-wide picture

t24 remains the tightest instance space by a wide margin on every measure. Everything else is comfortable at 5-instance scale: the second-worst P(duplicate) is t25's 11.0%, and the worst question-surface is t27's 1,388 distinct questions in 2,000 seeds (P(duplicate *question*) in a 5-pack = 0.9%, negligible). No template comes close to failing H6.

### 7.2 t24 — the ceiling is disclosed and correct; **one claim in the same paragraph is false (BLOCKING, Finding A)**

**What is right, and verified by exhaustive enumeration of the full reachable support:**
- The shipping k support is exactly `{0.61, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68}` — **7 values, exactly as documented**, with 0.58/0.59/0.60/0.62 permanently rejected by the Φ and ARL boundary screens.
- The answer space is **exactly 19 values**: {1.5, 1.6, 1.7, 1.8, 1.9, 2.6, 2.7, 2.8, 2.9, 3.0, 3.2, 3.5, 5.9, 6.2, 6.5, 6.8, 7.1, 7.5, 8.3}.
- Disclosed "modal share ~10%" vs **measured 9.95%**; disclosed "P(duplicate answer in a 5-instance set) ~50%" vs **measured 50.7%**. Accurate.
- Disclosed "REALIZED within-instance separations ≥ 3.3 (9 vs 16) and ≥ 1.1 (16 vs 25)" — **exactly reproduced** by my per-k enumeration (minima 3.3 and 1.1, both at k = 0.68).

**Finding A — the band claim is falsified.** The docstring (`variables_control_charts.py:682–684`) states:

> *"Realized 1-dp ARL bands (enumerated) [5.9, 9.6] / [2.6, 4.0] / [1.5, 2.2]"*

**Exhaustive enumeration over the shipping support gives [5.9, 8.3] / [2.6, 3.5] / [1.5, 1.9].** No reachable draw produces 9.6, 4.0 or 2.2. I traced the source of the error: those three upper bounds are the ARLs at **k = 0.58** — the value that the *same docstring*, sixteen lines earlier, documents as permanently rejected by the screens ("the SHIPPING support is {0.61, 0.63..0.68} (7 values; verified by full enumeration)"). The band figures were computed over the *sampled* window [0.58, 0.68] and never re-run after the screens narrowed it, so the paragraph contradicts itself.

**Severity.** Documentation-only: no emitted text changes, and the assert bands `(5.9, 9.7) / (2.5, 4.1) / (1.4, 2.3)` at `variables_control_charts.py:777` are supersets of the true realized bands and never fire in 50,000 draws. But it is a claim labelled "(enumerated)" that was not enumerated against the shipping code — the exact failure mode this branch has produced repeatedly, and it is the *only* remaining instance of it that I could find. It must be corrected, and the corrected figures must be the ones the Final Report quotes.

**Judgment on the 19-value ceiling itself: acceptable for a 5-instance testset, with the v1 conditions retained.** The ceiling is structural (the Φ/ARL tie screens fix the k support, and widening k re-opens the table-rounding hazards those screens close), it is now disclosed, and seeds 201–205 yield 5/5 distinct answers (§9). It must stay on the branch Final Report escalation list and be re-examined before any 15-seed Phase 4 instantiation.

### 7.3 t28 — the disclosure was **deleted** (BLOCKING, Finding B)

The residual **improved substantially**: v1 measured and the docstring then disclosed a 69-value ceiling with modal 7.6%, top-10 48.9%, P(dup) 27.3%. I now measure **152 distinct answers, modal 3.35%, top-10 21.2%, P(dup) 9.9%** — roughly a 2.7× widening, produced as a side effect of pinning the revised centre line's rounding, which freed T and c_max from the exact-division grid. The c8 log records `distinct_answers: 152, modal 3.14%, top10 20.1%` over a larger sweep; **my independent figures agree**, so the *log* is honest.

**Finding B — but the docstring now discloses nothing.** The answer-space note has been removed entirely in favour of a blanket policy ("Figures live in the review log, not here, so they cannot drift against the code", `attributes_control_charts.py:435–436`). The policy is defensible for volatile leak accuracies. It is **not** defensible for the structural residual: a reader of the source has no way to learn that this template's answer space is bounded at all. And the deletion left a **dangling cross-reference**: `attributes_control_charts.py:527` still reads *"see the docstring's support-collapse note"* — a note that no longer exists anywhere in the file (grep confirms zero other occurrences of "support-collapse"). The domain's headline residual disclosure has gone from naming the less severe of two ceilings (v1's finding) to naming neither in-source.

**Required:** restore a one-line structural disclosure to t28's docstring stating the measured ceiling and its date/sweep size, and repair or delete the dangling reference at line 527.

### 7.4 Undisclosed but acceptable (advisory)

t25 (121 answers, P(dup) 11.0%) and t22 (240 answers, P(dup) 5.4%) carry no disclosure. Both are far from binding at 5 instances, and both are structurally explained (Cpk on a 2-dp grid inside an asserted band; z on a 2-dp grid inside [3.2, 4.6]). Worth a line each in the Final Report for completeness, not worth a Stage C cycle.

---

## 8. The cycle record (§7)

### 8.1 Completeness — now clean

§7 requires one log record per cycle. **Every cycle in the domain now has a record**, and every back-filled record is marked:

| Log | Records | Reconstructed |
|---|---|---|
| t21, t22, t23, t29 | c1–c2 | none |
| t24 | c1–c2 + one `post_acceptance_audit` record (no cycle number) | none |
| t25 | c1 | none |
| t26R | c1–c5 | **c2** (`reconstructed: true`) |
| t27 | c1–c7 | **c2, c3, c4** (`reconstructed: true`) |
| t28 | c1–c8 | **c2** (`reconstructed: true`) |
| t30 | c1–c4 | none |
| ppm (discard) | c1–c4 | none |

v1's action 5 is closed. The reconstruction notes are candid and, in the t27 c3/c4 cases, **exemplary**: they state that findings were transcribed from the arbitration of record and that *"Score vectors that were not preserved are null — NOT reconstructed from memory. Treat as a secondary source."* That is the right standard. The t24 post-acceptance audit record (2026-08-08) is likewise a model of the genre: it records a hazard imported from another template's finding, an exhaustive 42-value re-check, a null result, and "no code change required".

### 8.2 The two undispatched cycles — **I judge the deviation SOUND, and I discharge it**

Cycles t27-c7 and t28-c8 were not sent to reviewer panels. Both records state this explicitly and name my audit as the intended substitute:

- t27 c7 `panel`: *"NOT DISPATCHED — operator decision to spend the remaining review budget on t28 (which carried the blocking findings) and let the Stage D re-audit serve as the independent check on this template. Recorded as a deviation from the §5 per-cycle panel requirement."*
- t28 c8 `panel`: *"NOT DISPATCHED — operator-approved: the c7 panel returned no blocking finding and every c8 change is either a screen that makes an existing claim true or a correction to a false claim. The Stage D re-audit is the independent check."*

**Judgment: the deviation was correctly scoped, correctly disclosed, and is now discharged — with one exception.** Grounds:

1. **The precondition held in both cases.** The preceding panel (c6 for t27, c7 for t28) returned no blocking flag in either template. Neither round was force-accepted through a blocking finding.
2. **The changes were of the right character.** t27's c7 change is structural in the safest direction — deriving the `(m, n)` plan table in code from the curated windows so it cannot drift — and I re-derived that table independently and confirmed both of its documented consequences. t28's c8 changes are screens that make previously-false claims true, plus withdrawals of claims that were false. Neither round introduced new modelling.
3. **The substitute check was performed and is real.** I have now done, with fresh context, what a panel would have done: re-derived the enumerations, re-measured every quantitative claim, re-verified the grounding line-by-line, and re-run the harness plus 50,000 draws. R2's role (independent numerical re-solve) is covered by the harness's H4 parser round-trip plus my exhaustive t24 enumeration and per-k ARL reconstruction; R3's role (blind difficulty label) is covered by §3.2, which was formed before any source was opened; R1's role (breaking parameter combination) is covered by the 50,000-draw assertion run and the branch-mix sweeps.
4. **It found something.** The substitute check was not a rubber stamp: Findings A, B and C above are exactly what an independent pass is for, and two of the three (A, B) sit in the very cycles that skipped a panel — A in t24 was untouched by c7/c8, but B is a direct artifact of c8's docstring rewrite. That is evidence the deviation carried real risk, and that the compensating control caught it.

**The exception.** The deviation is discharged for t27 and t28 *only*. It must not become precedent: two consecutive undispatched cycles on the same two templates is the maximum this compensating control can carry, and any further cycle on either template must go to a panel.

### 8.3 The two cap overruns — **the accounting is honest**

Both records carry an identical, unflinching `cycle_cap_note`:

> *"CYCLE-CAP OVERRUN, DOCUMENTED WITH CAUSE. Spec §5 caps review at 4 cycles. Cycles 3+ exist because a Stage D audit reopened an already-accepted template, and several later defects were introduced by the author's own remediation patches rather than by the template failing to converge. No round was force-accepted. Flagged for the human checkpoint."*

**I accept this accounting.** It is accurate on the facts, it does not hide the overrun behind a recount, it correctly identifies the author's own remediation patches as a cause rather than blaming the templates, and it escalates rather than self-absolves. t27 ran 7 rounds and t28 ran 8 against a cap of 4; the cap was blown by a factor of two, and the record says so in plain terms. That is the behaviour the spec's logging requirement exists to produce.

**On t28's voided c4 dispatch:** the log's `evidence_note` records a stale-instance-pack incident, a void, and a re-dispatch **as the same cycle 4** with no cycle-number advance. That is a clean void, correctly executed.

### 8.4 **Finding D — t26R's accounting ruling was not carried forward**

v1's action 6 required t26R to be reported as **"5 dispatched / 4 certifying — cap overrun with cause"**, explicitly *not* as four cycles and *not* as a void. That ruling now exists nowhere in the live artifacts. The t26R log still carries the author's original characterization at c5 — *"the third was VOID (stale evidence, my packaging error) so this is the fourth VALID cycle"* — and the c4 `cycle_accounting` note still frames it as a void while recording the counter-reading.

**I re-affirm the v1 ruling, on independent reasoning.** A round is void only if nothing from it is carried forward. All three c3 reviewers ran verification **directly against the correct on-disk c3 code** and their code-level findings drove the c4 revision (including the directional-rounding defect). A round whose findings advance the artifact must be charged to its budget. **The honest count is 5 dispatched / 4 certifying.** I also re-affirm that this is *not* grounds for discard: the overrun was an author-side packaging bug, the artifact met the full §5.2 gate at the final round, and t26R is itself already a replacement.

The frozen log records need not be rewritten — they correctly record what was decided at the time and explicitly preserve the counter-reading for the human. But the **Final Report §9.2 hardening statistics must state "5 dispatched / 4 certifying — cap overrun with cause"**, and the ruling must be carried on the human checkpoint list. Since v1 is superseded, this report is now the only place it lives.

### 8.5 Live escalation carried forward (physics, unresolved)

t26R's c5 acceptance escalated four items to the Final Report. One is a **physics/realism dispute that survived acceptance unresolved** and therefore belongs on the §9.3 human-expert list under spec §5.3:

> *"sigma_max below the stated metrology floor in 35.7% of anodize draws"*

**I re-measured it: 1,015 of 2,875 anodize draws (35.3%) print a σ_max below the 1.5-micron coating-metrology floor that the template itself asserts as a realism bound on σ.** The claim is accurate and still live. The template asks the solver to compute a target spread that is below the measurement repeatability the same template declares — internally consistent as algebra, questionable as engineering. The process here was correct (escalated, not silently overridden), and it needs a human coating-metrology judgment, not another Stage C cycle. The other three escalations (direction-dependent resistor re-centring justification; the dominant wrong-answer mode; non-round anodize callouts) also stand.

### 8.6 Two stale-instance-pack incidents

t26R c3 and t28 c4 both consumed a reviewer round on stale evidence. The author recorded the lesson (regenerate the pack in the same script as the code snapshot, "lesson 86") and the c4 QA line confirms it was applied. This should appear in the Final Report as an **orchestration** finding — it cost two full reviewer rounds — not as a template defect.

---

## 9. Stage E readiness

**Seed pack 201–205, all 10 templates, 50 instances.**

| # | Distinct answers in the 5-pack | Parsed steps (seeds 201–205) | Final answer extracted | Intermediate step carries a value |
|---|---|---|---|---|
| t21 | **5 / 5** | 3, 3, 3, 3, 3 | ✓ | ✓ |
| t22 | **5 / 5** | 4, 4, 4, 4, 4 | ✓ | ✓ |
| t23 | **5 / 5** | 4, 4, 4, 4, 4 | ✓ | ✓ |
| t24 | **5 / 5** | 5, 5, 5, 5, 5 | ✓ | ✓ |
| t25 | **5 / 5** | 4, 4, 4, 4, 4 | ✓ | ✓ |
| t26R | **5 / 5** | 5, 5, 5, 5, 5 | ✓ | ✓ |
| t27 | **5 / 5** | 3, 3, 3, 3, 3 | ✓ | ✓ |
| t28 | **5 / 5** | **5, 4, 5, 4, 4** | ✓ | ✓ |
| t29 | **5 / 5** | 4, 4, 4, 4, 4 | ✓ | ✓ |
| t30 | **5 / 5** | 5, 5, 5, 5, 5 | ✓ | ✓ |

**All 50 instances parse through `evaluation/engineering_parser.py` using the harness-identical `extract_steps` call; all 10 packs yield 5 distinct final answers; every instance clears the ≥ 3-step minimum and carries an extractable intermediate.** t28's mixed 5/4/5/4/4 step counts are the branching working as designed — three revise draws and two in-control draws in a single pack, which is a favourable draw for trace diversity.

Two notes for the Stage E operator:
- **The pack choice matters and 201–205 is the right one.** v1 recorded that seeds 1–5 contain a t24 duplicate and 301–305 a t28 duplicate; I confirm 201–205 is clean for all ten. Do not substitute another pack without re-running this check.
- t21 and t27 sit exactly at the harness's 3-step floor. Any future edit that merges a step would fail H4.

---

## 10. Required actions and advisory items

### REQUIRED (blocking — Stage E must not start until these clear)

1. **Correct t24's falsified ARL-band claim.** `variables_control_charts.py:682–684` states realized 1-dp ARL bands `[5.9, 9.6] / [2.6, 4.0] / [1.5, 2.2]`. Exhaustive enumeration over the documented 7-value shipping k support gives **`[5.9, 8.3] / [2.6, 3.5] / [1.5, 1.9]`**. The quoted upper bounds are the k = 0.58 values, which the same docstring documents as permanently screened out — the paragraph contradicts itself. Replace with the enumerated figures, state that they are computed over the shipping support (not the sampled window), and quote the corrected bands in the Final Report. Documentation-only; no emitted text changes; re-run the harness to confirm. (§7.2, Finding A)

2. **Restore t28's structural-residual disclosure and repair the dangling reference.** The docstring no longer discloses any answer-space bound; the measured figures are **152 distinct answers, modal 3.35%, top-10 21.2%, P(duplicate in a 5-pack) 9.9%** (concordant with the c8 log's 152 / 3.14% / 20.1%). Add a one-line disclosure with the sweep size and date. Separately, `attributes_control_charts.py:527` refers to *"the docstring's support-collapse note"*, which no longer exists — repair or delete it. (§7.3, Finding B)

3. **Fix t26R's spec R7 violation.** Move the IEC 60063 E24/E12 preferred-value series, the E24↔5% / E12↔10% tolerance pairing, the MIL-A-8625 Type III thickness envelope `(20, 110)` microns and the ASTM B244/B487 1.5-micron metrology floor from `process_capability.py:229–244` and `:410, :424` into `constants.py`, each with an inline source citation in the house style; import them; and delete the verbatim duplicate of `SPC_CHARACTERISTICS["resistor resistance (ohm)"]["sigma_frac"]`. **Have the Stage B Data Reviewer spot-verify the new entries** — these are the only named physical data in the domain that never passed Stage B, because t26R was authored after it. Re-run the harness and confirm byte-identical output for a fixed seed set. (§6.2, Finding C)

4. **Record the t26R cycle-accounting ruling in the Final Report.** §9.2 hardening statistics must state **"5 dispatched / 4 certifying — cap overrun with cause"**, never "4 cycles" and never "a void", and the accounting question must be carried on the human checkpoint list. This ruling currently survives only in the superseded v1 report. Do **not** discard t26R. (§8.4, Finding D)

5. **Carry t26R's live physics escalation to the human checkpoint list.** σ_max prints below the template's own declared 1.5-micron coating-metrology floor in **35.3% of anodize draws** (re-measured; the c5 escalation said 35.7%). Per §5.3 this is a physics dispute that survived acceptance unresolved and needs a human coating-metrology judgment, not another Stage C cycle. Carry the other three t26R c5 escalations alongside it. (§8.5)

### ADVISORY (non-blocking)

1. **The branching allocation differs from the Gate-A plan even though the count is met.** BOOKS.md §4 named Q1-#3, Q2-#6, Q3-#7; delivered are t23 (Q1), t28 (Q3-#8, not #7) and t24 (Q1, unplanned), with **Q2 carrying no branching template** after the Q2-#6 discard. Describe this accurately in the Final Report rather than implying the slot plan was delivered as written. (§2.4)
2. **t21/t23 is the domain's closest pair on measurement (Jaccard 0.494), not t25/t26R (< 0.202).** v1 named t25/t26R the closest without measuring. Both pairs resolve as distinct, but the Final Report should name the right one. (§2.2)
3. **`XBAR_R_SUBGROUP_N` and `XBAR_S_SUBGROUP_N` are dead constants** — `constants.py:332–337` says they exist for t23, and no template in any domain reads them. Either wire t23 to them (documenting the deliberate 13-not-11 narrowing on the `constants.py` side) or delete them. Same drift hazard, lower severity, for the `sf` sigma-fraction windows duplicated verbatim in t21/t22/t23/t25. (§6.3)
4. **The Shewhart "CL ± 3 × spread" move terminates 5 of 10 templates.** Intrinsic to an SPC domain with two control-chart areas; do not add a sixth if any Q1/Q3 template is ever replaced. (§2.3)
5. **t24 and t30 both carry 5 numbered steps against the Advanced "≥ 6 steps" guide**, with depth carried by parallel sub-evaluations within steps. If the Phase 2 Tribunal applies the step count mechanically, both will need the defence recorded here and in the P&I report for t19. (§3.2)
6. **t25 (121 answers, P(dup) 11.0%) and t22 (240, 5.4%) carry no residual disclosure.** Comfortable at 5 instances; worth a line each in the Final Report for completeness, not worth a cycle. (§7.4)
7. **Two stale-instance-pack incidents (t26R c3, t28 c4) cost two full reviewer rounds.** Report as an orchestration finding; the author already recorded and applied the fix (lesson 86). (§8.6)
8. **The undispatched-panel deviation is discharged for t27 and t28 only** and must not become precedent. Any further cycle on either template goes to a panel. (§8.2)
9. **t21 and t27 sit exactly at the harness's 3-step H4 floor.** Any future edit merging a step will fail the harness. (§9)
10. **Do not substitute the Stage E seed pack.** 201–205 is verified clean for all ten; seeds 1–5 (t24) and 301–305 (t28) each contain a duplicate answer. (§9)

---

## 11. Artifacts

**Templates:** `pilot/templates/branches/industrial_engineering/quality_and_reliability_control/` — `variables_control_charts.py`, `process_capability.py`, `attributes_control_charts.py`, `acceptance_sampling.py`.
**Constants:** `pilot/templates/branches/industrial_engineering/constants.py`.
**Review logs:** `pilot/branches/industrial_engineering/review_logs/` — 10 accepted (37 cycle records total) plus `template_ppm_nonconforming_spec.jsonl` (the discard, 4 cycles). Four records are marked `reconstructed: true`; two cycles (t27 c7, t28 c8) are marked as not dispatched to panels; two templates carry documented cycle-cap overruns.
**Grounding source:** `pilot/references/public/full_books_industrial_engineering/extracted/montgomery_isqc_7e.txt` (never redistributed; only short fragments quoted); MIL-STD-105E transcriptions in `constants.py`.
**Audit evidence generated here:** blind instances at seeds 301–303 (all 10, labels formed before any source was opened); 2,000-seed diversity/branch/concentration sweep with 200,000-pack duplicate estimates (all 10); exhaustive enumeration of t24's k support, per-candidate ARL bands, within-instance separations and full answer space; 5,000-seed assertion-conformance run per template (50,000 draws, zero fires); pairwise lexical-overlap measurement over all 45 pairs; harness re-run on all four files from a clean process; Stage E pack verification at seeds 201–205 through `evaluation/engineering_parser.py`; line-located grounding checks for all 10 citations.
