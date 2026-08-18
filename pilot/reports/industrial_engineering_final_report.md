# Industrial Engineering / Operations Research Pilot — Branch Final Report (Stage E)

**Spec:** docs/pilot_template_authoring_spec.md · **Dates:** 2026-08-05 → 2026-08-10
**Verdict up front: GO, with a short remediation list.** Thirty templates were authored, hardened and audited; the mini-testset is generated and parser-verified. The branch also produced the pilot's most useful negative result, in §3.

## 1. What was produced

**30 templates across 3 domains; 150-record mini-testset generated, 150/150 parser-verified.**

| Domain | Templates | Difficulty | Answer-affecting branching | Cycles logged | Stage D |
|---|---|---|---|---|---|
| Production & Inventory | 10 | 4E/4I/2A | 3 | 15 | PASS |
| Stochastic Operations | 10 | 4E/4I/2A | 3 | 14 | PASS |
| Quality & Reliability Control | 10 | 4E/4I/2A | 3 | 36 | FAIL→remediate→**re-audit FAIL-remediable**, actions applied |
| **Branch** | **30** | **12E/12I/6A** | **9** | **65** | — |

Every domain meets the mandated 4/4/2 split and the BOOKS.md §4 branching plan of three. One template was correctly discarded at the cycle cap (`template_ppm_nonconforming_spec`, a Φ-table provenance defect) and replaced.

Supporting artifacts: page-cited `constants.py`; the H1–H7 harness; per-template JSONL review logs (65 cycle records); four domain audit reports; a 111-lesson compounded style guide (`AUTHOR_NOTES.md`); and `pilot/testset_preview/industrial_engineering/*.jsonl` in the exact schema of the real testset (`id, seed, branch, domain, area, level, question, solution`; seeds 201–205, disjoint from review seeds).

## 2. Hardening statistics — the evidence base

- **65 logged review cycles** across 30 templates, plus 4 Stage D audit passes. Domains 1 and 2 converged in 14–15 cycles each. Domain 3 consumed **36** — see §3.
- **Verification depth:** independent re-solving of every shipped instance from question text alone; sweeps of 20k–40k seeds as standard; and, on the two most contested templates, **exhaustive enumeration of the entire reachable state space** (1,224 and 24,009 tuples), making their divergence figures proofs rather than estimates. One reviewer constructed an explicit witness multiset for all 30,000 draws to prove a data-realizability condition.
- **Two cycle-cap overruns**, both documented with cause and neither force-accepted: `template_sigma_reduction_for_cpk` (**5 dispatched / 4 certifying**) and the two Q3 templates (7 and 8 cycles). Recorded as overruns, never as "4 cycles" and never as voids.
- **Two cycles shipped without a reviewer panel** (t27 c7, t28 c8), an operator-approved deviation; the Stage D re-audit judged it sound and discharged it for those two templates only.

## 3. The headline finding: the code was right, the claims were not

Domain 3 ran to 36 cycles because two templates were reopened by audit and then repeatedly failed on a defect class worth naming, because it is specific to agentic authoring and the pilot is the only place it would have surfaced.

Across cycles 5–8, independent reviewers verified the **arithmetic** of those templates as exact every single time — six solver paths, zero divergence, twice by exhaustive enumeration. Over the same cycles they falsified **eight of the author's claims about that arithmetic**:

| Claim | Reality |
|---|---|
| "No surface feature reveals the regime" (t27) | `D/m` classified it at 91.4% |
| "The optimum of the feasible family" (t27) | rested on a hand enumeration that omitted admissible plans |
| "Exactly these eight plans" (t27) | nine qualified |
| "No surface feature reveals the regime" (t28) | a fitted 2-parameter curve: zero errors on 30,000 held-out draws |
| "The (T,m) tell is gone" (t28) | reduced to 86.3%, not removed |
| "c_max is drawn freely" (t28) | support had collapsed to 78 backbones |
| Path-agreement guarantee (t28) | screen built from the rounded value; 22.45% of one regime uncovered |
| Realized ARL bands (t24) | quoted values unreachable under the template's own screens |

**Every one was a claim about a search, an enumeration, or a guarantee that had not actually been run.** Prose asserting a *property* is a claim requiring evidence exactly as much as a number is — but it costs nothing to write and no test checks it. Two mechanisms generalise beyond this branch and are recorded as lessons 108–109: replacing an exactness guarantee with a pinned rounding silently voids screens that relied on the old invariant; and rejection sampling prints the branch onto the marginal of whatever it resamples.

**A structural result also came out of it.** A branch whose regime is a threshold on continuous inputs *cannot* be made unpredictable — the boundary is a smooth curve, so a fitted curve recovers it. After three cycles chasing that leak, t27's branching claim was **withdrawn** rather than force-accepted, and t28's was rewritten to the defensible narrower claim: the branch changes the graded answer and the full computation is still required. Withdrawing the claim also removed the constraint it had imposed, taking t27 from 191 reachable states to 1,195.

## 4. Division of labor

**Agents were strong at:** arithmetic-exact gold traces; adversarial verification at scales no human would attempt (exhaustive state-space enumeration, 16-feature leak attacks with held-out splits, order-statistic plausibility screens); catching each other's defects — the three reviewer lenses found non-overlapping classes throughout; and compounding style discipline across 111 lessons.

**Humans remain necessary for:**
1. **Adjudicating realism-versus-design tradeoffs.** Complying with the curated c̄ ceiling cost t28 a rise from 0.716 to 0.909 on a cheap-ratio attack. Realism was chosen; an expert should confirm.
2. **Blessing engineering-judgment screens** — Poisson order-statistic thresholds, metrology floors, the n·p̄ ≥ 3 design floor.
3. **Verifying data against standards not on disk.** t26R's IEC 60063 and MIL-A-8625 values are moved to `constants.py` but flagged **UNVERIFIED** under the branch's primary-source-only rule.
4. **A live physics escalation:** t26R prints σ_max below its own declared 1.5 µm coating-metrology floor in **35.3%** of anodize draws.
5. **Phase 2/3 certification**, which this pilot deliberately did not run.

## 5. Escalation list (carried to the human checkpoint)

1. **Testset defect, new at Stage E:** `template_server_configuration_selection` yields only 17 distinct answers over 20,000 draws and just **3 distinct questions across seeds 201–205**, putting **two duplicate question pairs** in the shipped set — 148 distinct problems in 150 records. Both domain audits missed it because both measured answer diversity over large sweeps rather than checking the shipped pack for identical questions. **Fix before Phase 2.**
2. **Answer-space ceilings** (disclosed in-docstring): t24 19 values; t28 152 (modal 3.2%, P(duplicate in a 5-pack) ≈ 9.5%); t25 121; t22 240. Comfortable at 5 instances, re-examine before any larger instantiation.
3. **t26R:** σ_max below the metrology floor in 35.3% of anodize draws; unverified standards data; **5 dispatched / 4 certifying** cycle accounting.
4. **Two cycle-cap overruns and two unpanelled cycles**, all documented with cause.
5. **Branching allocation differs from the Gate-A slot plan**: delivered t23 (Q1), t28 (Q3), t24 (Q1, unplanned); Q2 carries none after the Q2-#6 discard.
6. **Dead curated constants** (`XBAR_R_SUBGROUP_N`, `XBAR_S_SUBGROUP_N`) read by no template — drift hazard.
7. **Orchestration finding:** two stale-instance-pack incidents cost two full reviewer rounds; the packaging step must regenerate evidence in the same script as the code snapshot (lesson 86).

## 6. Model-pilot readiness

`pilot/testset_preview/industrial_engineering/` (150 records) is directly consumable: point `evaluation/run_inference.py` at it and run the framework unchanged — schema and formatting verified via 150/150 `engineering_parser` round-trips, with `extract_steps` returning a non-empty trace for every record. Suggested first experiment: run 2–3 models spanning capability tiers and compare FAC / Reasoning-F1 against the paper's existing branches. Domain 3 is the interesting probe — its Q3 templates are the most heavily hardened artifacts in the pilot, and t28 in particular grades a *decision* (revise or not) rather than a substitution.

## 7. Recommendation

**GO** for the full human-expert pipeline on Industrial/OR (Phase 2 → Phase 3), conditional on the §5 escalation list, with item 1 fixed first.

**GO** for repeating this Phase-1 process on further branches, with one process change that this branch paid to learn: **require every property claim in a docstring to name the measurement that supports it, or not be made.** A claim with no reproducible measurement behind it is where the defects concentrated — not in the mathematics, which independent verification found correct every time.
