# Stage D Domain Report — Industrial Engineering / OR, Domain 2: Production & Inventory

**Spec:** docs/pilot_template_authoring_spec.md, Stage D
**Auditor:** Domain Auditor agent (fresh context; did not author or review any of these templates)
**Date:** 2026-08-07
**Inputs:** 10 accepted template sources (`pilot/templates/branches/industrial_engineering/production_and_inventory/`), BOOKS.md §2/§4, review logs (`pilot/branches/industrial_engineering/review_logs/`), 3 fresh instances per template (seeds 201–203, `random.seed` from repo root with `sys.path.insert(0, ".")`), plus targeted 500-seed sweeps (seeds 1–500) for branch/regime/winner mixes.

**VERDICT: PASS** (no isomorphic pairs; zero relabel mismatches; t17 reconciliation judged sound; branching plan exceeded — 3 planned + 1 bonus regime template). Two advisory notes, no required actions.

---

## 1. Inventory

| # | Template | File | Area | Frozen difficulty | Reasoning-chain skeleton (one line) |
|---|---|---|---|---|---|
| t11 | `template_basic_eoq` | deterministic_lot_sizing.py | P1 | Easy | Derive h = i·c → closed-form sqrt EOQ → round + ordering-frequency sanity check (3 steps) |
| t12 | `template_epq_finite_production` | deterministic_lot_sizing.py | P1 | Easy | Derive h → effective-parameter reduction h' = h(1 − D/P) with its physical justification → sqrt EPQ → grid round → peak inventory H (4 steps) |
| t13 | `template_quantity_discount_all_units` | deterministic_lot_sizing.py | P1 | Intermediate | Multi-candidate optimization: tier EOQs → realizability regime classification (3 classes) → total-cost comparison at candidates → argmin (4–7 steps) |
| t14 | `template_reorder_point_lead_time` | deterministic_lot_sizing.py | P1 | Intermediate | Regime comparison τ vs T → (over-regime) modular reduction of lead time by whole cycles → exact integer R (4–5 steps) |
| t15 | `template_safety_stock_reorder_point` | stochastic_inventory.py | P2 | Easy | Given z-quantile for stated service level → SS = z·σ_L → R = μ_L + SS (3 steps) |
| t16 | `template_newsvendor_normal_demand` | stochastic_inventory.py | P2 | Intermediate | Economic derivation cu/co from prices → critical fractile CR → invert Φ for z → Q* = μ + zσ (4 steps) |
| t17 | `template_qr_policy_one_iteration` | stochastic_inventory.py | P2 | Intermediate (reconciled) | Coupled-system one-iteration update: EOQ seed → stockout probability from optimality condition → quantile/R0 → unit normal loss → expected shortage → updated Q1 (7 steps) |
| t18 | `template_takt_time_line_efficiency` | production_planning.py | P3 | Easy | takt = A·60/D (exact integer) → N_min ceiling → efficiency ratio (3 steps) |
| t19 | `template_line_balancing_heuristic` | production_planning.py | P3 | Advanced | Algorithm execution over precedence state: station-by-station construction under the longest-eligible-task rule → n vs N_min → balance delay (5–6 numbered steps + per-station decision sub-chains) |
| t20 | `template_chase_vs_level_aggregate` | production_planning.py | P3 | Advanced | Construct two complete multi-period plans (chase workforce path + inventories; level max-over-prefixes workforce + inventories) → cost both → regime-dependent comparison (6 steps) |

All 10 conform to the §3 contract on inspection: `**Step X:**` markers, single `**Answer:**` line whose final number is the asked quantity, stdlib `random` only, constants.py-sourced parameter windows, embedded physical-bounds assertions, self-contained questions. Determinism spot-checked (t11, t17: same seed → identical output).

---

## 2. Diversity audit

### 2.1 Explicitly assessed pairs

**(a) t11 EOQ vs t12 EPQ — DISTINCT (nearest pair in the domain).**
Both terminate in Q* = sqrt(2KD/h_eff) and share the h = i·c opening. They are not step-isomorphic: t12 inserts a structurally new step — deriving and justifying the effective holding cost h' = h(1 − D/P) from the inventory-buildup mechanism (build rate P − D, peak H = Q(1 − D/P)) — and closes with the maximum on-hand inventory, which t11 has no analogue of (t11 closes with an ordering-frequency check). The physical scenario also differs (purchased lot delivered at once vs in-house gradual production), and the textbook treats them as separate models (Nahmias §4.5 vs §4.6). This is the canonical EOQ/EPQ pedagogical pair, not a re-skin; flagged as the domain's closest pair and judged acceptable.

**(b) t15 safety stock vs t16 newsvendor — DISTINCT.**
Both end in a single μ + z·σ substitution, but the provenance of z — the intellectual content of each template — is entirely different. In t15, z is *given* in the question for a stated cycle-service level; the reasoning is interpreting the service level as a quantile requirement. In t16, z must be *derived*: underage/overage costs from the price structure (cu = p − c, co = c − s), the critical ratio cu/(cu+co) from the optimality argument, then an inverse-CDF evaluation. t16's chain contains an economic optimization concept absent from t15; the shared final line is one substitution step out of four. Not isomorphic.

**(c) t18 takt/efficiency vs t19 line balancing — DISTINCT.**
Shared vocabulary (takt/cycle time, N_min ceiling, an idle/efficiency ratio) but qualitatively different chains: t18 is a three-step exact-integer formula chain (takt from demand and available time → ceiling → ratio); t19 never computes takt (CT is given) and its core is the *execution of a stateful assignment algorithm* over a precedence network — eligibility sets recomputed after every assignment, fit decisions, station closures — before the closing delay ratio. One is substitution, the other is construction. Note t18's efficiency = W/(N_min·takt) and t19's balance delay = 1 − Σt/(n·CT) are complements of the same metric family; since the metric is the closing one-liner in both, not the reasoning body, this does not create isomorphism.

**(d) Branching quality (BOOKS.md §4 plan: P1-#3, P1-#4, P3-#10 — ≥3 required).**
Verified live by 500-seed sweep (seeds 1–500), not just claimed:

| Template | Mechanism | Attained mix (500 seeds) | Assessment |
|---|---|---|---|
| t13 | Discount-regime decision: which tier EOQs are realizable changes the candidate set and step count (4/6/7 steps) | branch a 231 / b 144 / c 125; within comparisons, EOQ vs breakpoint winners: b 60/84, c 33/92 | Genuine 3-way regime branching AND a live decision inside each comparison branch (small 2–3.5% discount steps keep the comparison non-degenerate — a documented cycle-1 fix) |
| t14 | Lead-time regime τ < T vs τ > T switches the formula (R = λτ vs R = λτ − kQ with whole-cycle reduction) | under 254 / over 246 (over-regime k ∈ {1, 2}) | Genuine formula-family switch, ~50/50 |
| t20 | Cost regime (churn-heavy vs holding-heavy) steers which plan wins | chase 230 / level 270 | Genuine parameter-dependent winner; both outcomes well-represented |
| t17 | (not a branching template) | — | Materiality screen forces Q1/Q0 ≥ 1.14 (iteration visibly matters) and the r0 window [0.02, 0.25] is regime-realism-constrained; this is decisiveness engineering, not reasoning-path branching — correctly NOT counted toward the §3 branching quota |

Additionally t19's station count n ∈ {3, 4} (269/231) and heuristic-matches-N_min vs exceeds-it (both observed in the seed-201–203 instances) vary the trace structure parameter-dependently. The domain carries 3 formal branching templates plus this structural variation — the §3 "at least 3" requirement is met with margin.

### 2.2 Full-domain skeleton scan

The ten skeletons (inventory table above) partition into clearly different derivation structures: closed-form substitution (t11, t15, t18), substitution with a derived effective parameter (t12), fractile-inversion economics (t16), regime-switched exact arithmetic (t14), candidate-set optimization with regime logic (t13), coupled-system iteration (t17), algorithm execution over evolving state (t19), and dual multi-period plan construction with comparison (t20). No pair is step-isomorphic.

One family-level observation (advisory, not a violation): the EOQ root sqrt(2KD/h) appears in four templates — as the entire answer (t11), with an effective parameter (t12), as the per-tier candidate generator inside an optimization (t13), and as the iteration seed inside a coupled system (t17). Each use is embedded in a different superstructure, which is exactly the "same tool, different reasoning chain" pattern the spec permits; but any future P1/P2 replacement should avoid adding a fifth sqrt-family member.

---

## 3. Coverage audit

### 3.1 Area allocation and difficulty split (FROZEN)

| Area | Quota (BOOKS.md §2) | Delivered | Templates |
|---|---|---|---|
| P1 Deterministic Lot Sizing | 4 | 4 | t11 E, t12 E, t13 I, t14 I |
| P2 Stochastic Inventory | 3 | 3 | t15 E, t16 I, t17 I |
| P3 Production Planning | 3 | 3 | t18 E, t19 A, t20 A |

Split: 4 Easy (t11, t12, t15, t18) / 4 Intermediate (t13, t14, t16, t17) / 2 Advanced (t19, t20) — **confirmed 4/4/2**. Docstring labels match the frozen assignment in all 10 sources. The delivered slate deviates from the BOOKS.md suggested slate only in the t17↔t19 Advanced/Intermediate swap (slate explicitly non-binding; see §4).

### 3.2 Blind re-label against §2.1

Method: 3 fresh instances per template (seeds 201–203) generated from repo root; labels assigned from the rubric axes (governing principles, regime decisions, step counts, construction-before-substitution) before comparing with the frozen labels.

| # | Frozen | Auditor blind label | Rationale (§2.1) | Match |
|---|---|---|---|---|
| t11 | Easy | Easy | Single principle (EOQ); direct substitution; 3 steps | YES |
| t12 | Easy | Easy | Single principle with one derived parameter; direct substitution; 4 steps | YES |
| t13 | Intermediate | Intermediate | Regime decision changes the applicable candidate set/formula path; 4–7 steps | YES |
| t14 | Intermediate | Intermediate | Regime decision (τ vs T) changes the formula; 4–5 steps | YES |
| t15 | Easy | Easy | Single principle; direct substitution; 3 steps | YES |
| t16 | Intermediate | Intermediate | Two coupled concepts (cost economics → normal fractile); 4 steps | YES |
| t17 | Intermediate | Intermediate (high) | Multi-concept but fully guided: the question states the coupled system, the iteration order, and an itemized precision scheme, so the solver substitutes through a prescribed 7-step chain rather than constructing it; top of the Intermediate band | YES |
| t18 | Easy | Easy | Single chain; exact integer arithmetic; 3 steps | YES |
| t19 | Advanced | Advanced (boundary) | The station structure must be iteratively constructed over changing eligibility state before any final substitution — §2.1's "construction ... before numeric substitution"; n=3 draws show 5 numbered steps (below the "≥6 steps" guide), but each station step contains a multi-decision sub-chain, so procedural depth is adequate | YES |
| t20 | Advanced | Advanced | Two complete multi-period plans built from first principles (incl. the max-over-prefixes feasibility argument) before the comparison; 6 steps; regime-dependent outcome | YES |

**Mismatches: 0 of 10.** Two boundary observations recorded (t17 sits at the top of Intermediate; t19's n=3 draws are formally one numbered step short of the Advanced step guide) — both consistent with the frozen labels and both already surfaced by R3 in the review logs.

---

## 4. Assessment of the t17 label reconciliation

**History** (review_logs/template_qr_policy_one_iteration.jsonl, 4 cycles): R3's blind labels ran Intermediate (v1, fully scaffolded) → Advanced (v2, de-scaffolded question) → Intermediate (v3, iteration-order clause restored) → Intermediate (v4, accepted). Cycle-4 arbiter reconciled the label to Intermediate by blind-label majority and moved the domain's second Advanced slot to t19 (line balancing), which was then accepted at cycle 1 with an independent blind Advanced label.

**Judgment: SOUND**, on four grounds:

1. **The majority tracks the accepted artifact, not just a vote count.** The single Advanced label (c2) was attached to a version whose question deliberately withheld the iteration order; v3/v4 restored the explicit "determine R0 from the second condition, then Q1 from the first" clause plus the itemized precision list (a)–(f). The version actually frozen is a guided substitution chain — the construction §2.1 demands of Advanced is done *for* the solver. Both blind reads of the accepted form (c3, c4) said Intermediate, and this audit's independent blind read concurs.
2. **The rubric supports Intermediate for v4.** Seven steps, multi-concept (EOQ, optimality condition, normal quantile, loss function), but no regime decision and no system construction: "two coupled concepts ... 4–7 steps" fits; "construction of a system of equations/iteration from first principles before any numeric substitution" does not, because the system and the iteration recipe are stated in the question.
3. **The receiving template genuinely earns the slot.** t19's station-by-station assembly over evolving eligibility state is authentic construction; its cycle-1 acceptance with an unprompted blind Advanced label (and R2's 200k-seed full-assignment equality check) validates the reallocation rather than merely papering over the 4/4/2 arithmetic. The residual weakness — n=3 draws with 5 numbered steps against the "≥6 steps" guide — was disclosed by R3 and is mitigated by the multi-decision content of each station step.
4. **Process integrity.** The slate is explicitly non-binding (BOOKS.md §10); the 4/4/2 stratification was preserved; the reconciliation was logged with a lesson (IE-69: reconcile boundary-difficulty concepts by blind-label majority + slot reallocation rather than oscillating) rather than force-labeling to fit the plan. This is the intended use of Stage D's "mismatches are reconciled" clause.

Minor residue, correctly handled: the c4 R1 observation that all t17 instances run in the multi-outstanding-order regime was escalated to the human-expert list rather than silently absorbed — appropriate under §5.3.

---

## 5. Verdict and actions

**PASS.**

- Diversity: no isomorphic pairs among the 10; the three explicitly-questioned pairs (t11/t12, t15/t16, t18/t19) are each distinct in reasoning structure; branching quota met (t13, t14, t20) and verified live by 500-seed sweeps.
- Coverage: P1/P2/P3 = 4/3/3 as planned; difficulty split 4/4/2 confirmed; blind relabel 10/10 concordant.
- t17 reconciliation: sound; t19 slot reallocation validated.

**Required actions: none.** Advisory notes for Stage E / future maintenance:

1. (Advisory) The sqrt(2KD/h) family appears in 4 of 10 templates (t11, t12, t13, t17) in structurally different roles; acceptable now, but do not add a fifth member if any P1/P2 template is ever replaced.
2. (Advisory) t19's n=3 draws produce 5 numbered steps, formally below the Advanced "≥6 steps" guide; the per-station decision sub-chains carry the depth. If the Phase 2 Tribunal applies the step count mechanically, consider counting station sub-decisions or constraining to n=4 draws.
3. (Carried forward) The t17 multi-outstanding-order regime note remains on the branch escalation list for the human expert (already logged at cycle 4; no Stage D action).
