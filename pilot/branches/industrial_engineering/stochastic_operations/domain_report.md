# Stage D Domain Report — Stochastic Operations (Industrial Engineering / OR pilot)

**Status:** COMPLETE — 10/10 templates accepted; Stage D audit **PASS, zero required actions** (2 observations forwarded to the branch Final Report)
**Auditor:** Domain Auditor agent, fresh context (did not author or review any template)
**Date:** 2026-08-06

## 1. Inventory

| # | Template | File | Area | Difficulty | Cycles | Branching |
|---|---|---|---|---|---|---|
| 1 | mm1_time_in_system | queueing_systems.py | S1 | Easy | 1 | – |
| 2 | mmc_waiting_time | queueing_systems.py | S1 | Intermediate | 1 | – (time-unit-mixing template of the area) |
| 3 | server_configuration_selection | queueing_systems.py | S1 | Intermediate | 1 | ✔ winner decision (see §2.3) |
| 4 | mm1k_finite_capacity | queueing_systems.py | S1 | Advanced | 2 (Advanced earned by construction) | (✔) ρ<1 vs ρ≥1 regime commentary, 50/50 |
| 5 | two_state_steady_state | markov_chains.py | S2 | Easy | 1 | – |
| 6 | two_step_transition_probability | markov_chains.py | S2 | Intermediate | 1 | – |
| 7 | absorbing_chain_time_to_failure | markov_chains.py | S2 | Advanced | 1 | – |
| 8 | system_reliability_topology | system_reliability.py | S3 | Easy | 3 (exact-Decimal chain redesign) | ✔ sampled topology: series / parallel / mixed |
| 9 | exponential_mttf_topology | system_reliability.py | S3 | Intermediate | 1 | ✔ series (rate-sum) vs parallel (memoryless staging) formula family |
| 10 | poisson_event_count | poisson_processes.py | S4 | Easy | 2 (v1 terminated early on docstring/phrasing) | – |

Allocation S1/S2/S3/S4 = 4/3/2/1 ✓ (BOOKS.md §1 quotas). Difficulty 4 Easy / 4 Intermediate / 2 Advanced ✓. Branching: 2 strong + 1 medium + 1 regime-commentary (≥3 met; see §2.3).

Audit-side verification (this audit, independent of the frozen harness runs): 200-seed sweep per template — determinism byte-identical, zero assert firings, exactly one `**Answer:**` line per instance, H6-class diversity far exceeded everywhere (minimum: t3 with 17 distinct answers / 21 distinct questions, its full reachable set).

## 2. Diversity audit

### 2.1 Reasoning-chain skeletons (all 10, from source)

| # | Governing relation(s) | Skeleton |
|---|---|---|
| 1 | M/M/1 closed forms; Little | ρ stability check → L = λ/(μ−λ) → W = L/λ → hr→min (4 steps, pure substitution) |
| 2 | Erlang-C chain; Little | min→hr unit conversion → a, ρ check → P0 finite sum (c-dependent expansion) → Lq → Wq → min (6 steps) |
| 3 | M/M/1 W vs M/M/2 L = 2ρ/(1−ρ²); Little | convert both rates → dual stability check → W1 → L2 → W2 → compare & select (6 steps, comparative decision) |
| 4 | Birth–death balance equations, first principles | ρ + stability *argument* (finite state space) → derive p_n = ρⁿp₀ from cut balance → normalize → P_K → λ_eff → L as explicit weighted sum → Little with λ_eff → min (8 steps, distribution constructed before any measure) |
| 5 | Two-state DTMC balance | π₁p = π₂q + normalization → solve → complement check (3 steps) |
| 6 | Chapman–Kolmogorov | decompose over intermediate state → 3 path products → sum → independent row-sum verification (4 steps, sum-over-paths) |
| 7 | First-step (conditioning) analysis, absorbing DTMC | construct 2×2 linear system → solve by substitution (c1, n1, d1) → back-substitute → non-circular re-evaluation check (6 steps, system built then solved) |
| 8 | Structure functions (probability algebra) | identify sampled structure → per-branch: 3-product / complement-product / parallel-reduce-then-series (3 steps; step *content* branches with topology) |
| 9 | Min of exponentials (rate sum) OR memoryless two-phase staging | series: sum rates → invert (3 steps); parallel: phase split → E[first] = θ/2 → survivor good-as-new = θ → add (4 steps; different given-data style per branch) |
| 10 | Poisson pmf, N(t) ~ Poisson(λt) | μ = λt → e^(−μ) factor → pmf evaluation (3 steps) |

**No isomorphic pair found.** Each template's chain differs in governing relation or derivation structure, not just variable names. The two *closest* separations, both acceptable:

- **t1 / t3:** t3's Option 1 embeds t1's M/M/1 time-in-system result as a single closed-form step, but t3's skeleton is a two-model comparative decision (and its Option 2 uses the M/M/2 special-case L, not t2's Erlang-C route). Not a re-skin.
- **t5 / t7:** both solve DTMC linear relations, but t5 is one balance equation with normalization while t7 constructs and solves a first-step *system* for expected absorption times — different equations, different depth.

### 2.2 The three flagged comparisons

**(a) t1 M/M/1 vs t2 M/M/c vs t4 M/M/1/K — DISTINCT.** t1 is direct closed-form substitution (4 steps). t2 inserts a deliberate time-unit conversion and routes through the Erlang P0 finite sum whose expansion changes with c — a qualitatively different computation (6 steps). t4 shares no closed form with either: the steady-state distribution is *derived* from cut-balance equations, normalized, and L is computed as an explicit weighted sum, with Little applied to the effective (unblocked) rate; stability reasoning is inverted (finite state space, ρ ≥ 1 admissible — 609 of 1,949 reachable combos are overloaded). Three genuinely different chains on the same physical family.

**(b) t8 series/parallel reliability vs t9 MTTF — DISTINCT.** t8 is dimensionless probability algebra on structure functions (mission reliabilities in, reliability out; no time dimension, no distribution beyond independence). t9 reasons about *lifetimes* of exponential components: series via the rate-sum property of the minimum, parallel via a memorylessness staging argument; the answer is an expected time in hours. Different governing relations, different mathematical objects, different answer dimensions. The shared series/parallel vocabulary is surface-level only.

**(c) Branching count and quality vs the BOOKS.md §4 plan.** Planned: S1-#3, S3-#8, S3-#9 (+ ρ<1 gates in every S1 template, with S1-#4 the deliberate ρ≥1 exception). Delivered exactly, plus t4's 50/50-sampled regime branch as a bonus:

- **t8 — strong.** Three-way topology branch changes the governing formula *and* the step structure/prose; all three branches confirmed reachable and correctly structured (audit instances).
- **t9 — strong.** The configuration flips the entire formula family (rate-sum vs memoryless staging), the step count (3 vs 4), and the given-data style (rates per 1000 h vs mean life θ).
- **t3 — medium; known observation CONFIRMED.** Independent enumeration of all 21 reachable (tsA, tsB, λ) triples reproduces the R1/harness finding in `template_server_configuration_selection.jsonl`: within every (tsA, tsB) pair the winner is constant across the entire admissible λ range — (2,3)→pair, (2,4)→single, (2,5)→single, (3,4)→pair, (3,5)→pair. The branch driver is the service-time pair, never λ; the branching is coarser than the S1-#3 slate line ("winner is parameter-dependent") suggests, though it *is* parameter-dependent (12 single / 9 pair across the reachable set) and the solver must still compute both options to discover the winner — the decision is never inferable from the stem. t3 is also the domain's instance-space floor (21 questions / 17 answers; passes H6's ≥10 with margin). Assessment: acceptable as the third branching template; logged as an observation, not a defect. If the branch were ever to be strengthened, widening the tsB set or the ρ windows so at least one pair contains a λ-driven flip would do it — **not required**.
- **t4 — supporting.** The regime branch changes the stability *argument* (the pedagogical point of the template) but not the computation chain; counted as reinforcement, not as one of the three.

Verdict on structural diversity: **requirement met** (2 strong + 1 medium parameter-dependent branches ≥ the "at least 3 SHOULD" bar; no near-duplicate chains).

## 3. Coverage audit and blind relabel

Method: labels below were formed from the §2.1 rubric applied to the code's step structure and 3 generated instances per template (seeds 101/202/303), before consulting each docstring's declared label. (Declared labels are physically inside the sources the diversity audit reads; the relabel was formed from rubric criteria and observed step counts, not by adopting the declaration.)

| # | Observed steps | Governing structure (rubric axis) | Blind label | Declared | Match |
|---|---|---|---|---|---|
| 1 | 4 | single principle, direct substitution | Easy | Easy | ✓ |
| 2 | 6 | coupled concepts + non-trivial time-unit reasoning | Intermediate | Intermediate | ✓ |
| 3 | 6 | two models + decision that changes the reported quantity | Intermediate | Intermediate | ✓ |
| 4 | 8 | system constructed from first principles before substitution | Advanced | Advanced | ✓ |
| 5 | 3 | single principle, direct substitution | Easy | Easy | ✓ |
| 6 | 4 | decomposition set-up + multi-path sum + independent verification | Intermediate | Intermediate | ✓ (borderline note below) |
| 7 | 6 | linear system constructed and solved from first principles | Advanced | Advanced | ✓ |
| 8 | 3 | single structure formula per branch, direct substitution | Easy | Easy | ✓ |
| 9 | 3–4 | regime decision changes the applicable formula family | Intermediate | Intermediate | ✓ (note below) |
| 10 | 3 | single formula, direct substitution | Easy | Easy | ✓ |

**All 10 blind relabels concur with the declared labels. Zero mismatches.**

Borderline notes (concurrences, recorded for completeness):
- **t6** sits near the Easy/Intermediate boundary (one governing decomposition, 4 steps). Intermediate is justified: the C-K set-up over the intermediate state is a construction, not a formula lookup, and the row-sum verification requires computing two further independent entries — well beyond direct substitution.
- **t9**'s series branch alone (3 steps, rate sum) would read Easy; the template's Intermediate is carried by the §2.1 "regime decision that changes the applicable formula" clause plus the parallel branch's two-concept memorylessness synthesis. Consistent with how the rubric treats branching templates.

Quota conformance: area allocation 4/3/2/1 = BOOKS.md quotas ✓; difficulty split 4/4/2 ✓ (Easy: 1, 5, 8, 10; Intermediate: 2, 3, 6, 9; Advanced: 4, 7 — exactly the slate's assignment).

## 4. Verdict

**PASS — zero required actions.** No isomorphic pairs; all three flagged comparisons resolve as distinct; branching plan honored (2 strong + 1 medium + 1 supporting); area quotas and 4/4/2 split honored; 10/10 blind difficulty relabels concur.

Observations forwarded to the branch Final Report (not blocking):

1. **t3 branch driver (from R1 cycle-1, confirmed by this audit):** the configuration winner is decided entirely by the (tsA, tsB) service-time pair; λ never flips it within a pair. Parameter-dependent branching is technically satisfied and the solver must compute both options, but the mechanism is coarser than the slate phrasing implies. A human expert reviewing Phase 2/3 promotion may wish to judge whether this counts as full branching credit.
2. **t10 slate simplification:** the BOOKS.md slate line for S4 ("event-count probability + Erlang waiting-time computation") was narrowed to the pmf-only event count at authoring (consistent with the single-final-answer contract R2). The slate is explicitly non-binding; noted so the Final Report inventory describes what was actually built.

## 5. Artifacts

Templates: `pilot/templates/branches/industrial_engineering/stochastic_operations/` (queueing_systems.py, markov_chains.py, system_reliability.py, poisson_processes.py).
Review logs: `pilot/branches/industrial_engineering/review_logs/template_*.jsonl` (10 logs; cycle counts in §1; every acceptance at all-≥4 / zero-blocking / R2-within-tolerance).
Audit evidence: 200-seed determinism/assert/diversity sweep (all 10 pass); exhaustive t3 winner-map enumeration (21 triples); instance generations at seeds 101/202/303 for the blind relabel.
