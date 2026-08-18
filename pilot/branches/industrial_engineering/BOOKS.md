# Stage A — Branch Scoping: Industrial Engineering / Operations Research

**Spec:** docs/pilot_template_authoring_spec.md, Stage A
**Status:** GATE A APPROVED by the user, 2026-08-05 (including §9.2 edition substitutions)
**Prepared by:** Librarian agent (web-verified 2026-08-03; supplied copies verified 2026-08-04)

---

## 1. Domain 1 — Stochastic Operations

### Textbooks

| Role | Book | Justification |
|---|---|---|
| Primary | F.S. Hillier, G.J. Lieberman, *Introduction to Operations Research*, 11th ed. (McGraw-Hill) | "The classic text on operations research" (publisher's own positioning, web-verified): 11 editions since 1967, the dominant OR course adoption worldwide; Hillier received the INFORMS Expository Writing Award for the book and the 2018 Kimball Medal. Queueing Theory is print Ch. 17. |
| Primary | S.M. Ross, *Introduction to Probability Models*, 12th ed. (Academic Press) | The standard applied stochastic-processes text (12 editions); provides the **in-print** grounding for Markov chains (Ch. 4), exponential/Poisson (Ch. 5), queueing (Ch. 8) and reliability (Ch. 9). Needed because H&L 11th ed. moved Markov Chains (Ch. 28), Reliability (Ch. 25) and Application of Queueing Theory (Ch. 26) to **website-supplement chapters** (verified from the 11e front matter). |
| Backup | H.A. Taha, *Operations Research: An Introduction*, 10th ed. (Pearson) | The main alternative OR adoption in US curricula; cross-check for queueing/Markov typologies. |

**Chapter-numbering caveat (verified 2026-08-03; superseded for the supplied copies 2026-08-04):** in H&L **11e** the print book carries Ch. 17 Queueing Theory and Ch. 18 Inventory Theory; Markov chains and reliability exist only as website supplements. The **supplied copy is the 7th ed. (2001)**, whose print TOC (verified from the on-disk PDF outline) carries **Ch. 16 Markov Chains, Ch. 17 Queueing Theory, Ch. 18 The Application of Queueing Theory, Ch. 19 Inventory Theory** — so Markov chains ARE in print in our copy. Ross remains the lead grounding for S2/S3; H&L 7e Ch. 16 is a full in-print secondary.

### Area map (chapters re-anchored to supplied editions: H&L 7e / Ross 11e)

| Area | Chapters | Pedagogical role | Quota |
|---|---|---|---|
| S1. Queueing Systems (birth–death, M/M/1, M/M/c, finite capacity) | H&L Ch. 17 (same number in 7e and 11e); Ross Ch. 8 | Cornerstone | 4 |
| S2. Discrete-Time Markov Chains (steady state, Chapman–Kolmogorov, absorption) | Ross Ch. 4; H&L 7e Ch. 16 (in print; 11e relegates to web Ch. 28) | Core | 3 |
| S3. System Reliability (series/parallel structures, exponential lifetimes) | Ross Ch. 9; NIST/SEMATECH e-Handbook Ch. 8 | Core | 2 |
| S4. Poisson Process & Exponential Distribution | Ross Ch. 5 | Foundational | 1 |

### Suggested template slate (non-binding; final concepts fixed in Stage C)

| # | Concept | Area | Difficulty |
|---|---|---|---|
| 1 | M/M/1 steady-state performance measures (ρ, L, Lq, W, Wq) | S1 | Easy |
| 2 | M/M/c performance: P0 → Lq → Wq chain (Erlang-C form) | S1 | Intermediate |
| 3 | One fast server vs. c slow servers: configuration selection by comparing mean waits [BRANCHING: winner is parameter-dependent] | S1 | Intermediate |
| 4 | M/M/1/K finite-capacity queue: blocking probability, effective arrival rate, L | S1 | Advanced |
| 5 | Two-state Markov chain steady-state probabilities | S2 | Easy |
| 6 | n-step transition probability via Chapman–Kolmogorov (3-state chain) | S2 | Intermediate |
| 7 | Absorbing Markov chain: expected steps to absorption / absorption probability | S2 | Advanced |
| 8 | System reliability from component reliabilities [BRANCHING: sampled series / parallel / mixed topology] | S3 | Easy |
| 9 | MTTF of a system of exponential components [BRANCHING: series (rate-sum) vs. parallel (harmonic-sum) formula family] | S3 | Intermediate |
| 10 | Poisson process: event-count probability + Erlang waiting-time computation | S4 | Easy |

Difficulty split: 4 Easy (1, 5, 8, 10) / 4 Intermediate (2, 3, 6, 9) / 2 Advanced (4, 7). ✓

---

## 2. Domain 2 — Production & Inventory

### Textbooks

| Role | Book | Justification |
|---|---|---|
| Primary | S. Nahmias, T.L. Olsen, *Production and Operations Analysis(/-tics)*, 7th ed. supplied (Waveland; current is 8th ed., retitled *Analytics*) | The preeminent IE production/operations analysis text (8 editions — web-verified). In both editions: inventory with known demand (EOQ family) Ch. 4; uncertain demand (newsvendor, (Q,R)) Ch. 5; S&OP/aggregate planning Ch. 3. Line balancing: supplied 7e Ch. 9 §9.10; 8e moved it into Ch. 11 (facilities chapter eliminated — verified via publisher). |
| Primary | E.A. Silver, D.F. Pyke, D.J. Thomas, *Inventory and Production Management in Supply Chains*, 4th ed. (CRC) | The standard advanced inventory-theory reference; deeper treatment of lot sizing and safety-stock logic for cross-validation. (Chapter mapping to be pinned when the book is on disk.) |
| Backup | Hillier & Lieberman, *Inventory Theory* chapter (supplied 7e: Ch. 19; 11e: Ch. 18) — already on the branch shelf | In-print EOQ variants and the stochastic single-period (newsvendor) model; zero additional acquisition cost. Taha Ch. 13/16 as further cross-check. |

### Area map (chapters re-anchored to the supplied Nahmias/Olsen **7th ed.** — TOC verified visually 2026-08-04)

| Area | Chapters | Pedagogical role | Quota |
|---|---|---|---|
| P1. Deterministic Lot Sizing (EOQ, EPQ, discounts, reorder points) | Nahmias 7e Ch. 4 (§4.5 EOQ incl. order lead time p. 213; §4.6 finite production rate p. 218; §4.7 quantity discounts p. 220); H&L 7e Ch. 19 | Cornerstone | 4 |
| P2. Stochastic Inventory (newsvendor, service levels, (Q,R)) | Nahmias 7e Ch. 5 (§5.3 newsvendor p. 258; §5.4 lot size–reorder point p. 267; §5.5 service levels in (Q,R) p. 274); H&L 7e Ch. 19; Silver et al. (TOC only — see §9) | Core | 3 |
| P3. Production Planning (line balancing, aggregate planning) | Nahmias 7e Ch. 3 (§3.4–3.5 aggregate planning: chase/level/mixed, p. 138 ff.) and Ch. 9 §9.10 Assembly Line Balancing p. 528 (8e note: moved to Ch. 11) | Core | 3 |

### Suggested template slate

| # | Concept | Area | Difficulty |
|---|---|---|---|
| 1 | Basic EOQ: Q*, annual setup+holding cost, cycle time | P1 | Easy |
| 2 | EPQ (finite production rate): Q*, max on-hand inventory | P1 | Easy |
| 3 | All-units quantity discount: candidate Q per price band, regime feasibility, optimal choice [BRANCHING: discount-regime decision] | P1 | Intermediate |
| 4 | Reorder point with lead time [BRANCHING: τ < T vs. τ > T ⇒ R = λ·(τ mod T), per Nahmias Ch. 4] | P1 | Intermediate |
| 5 | Safety stock & reorder point at a given cycle-service level (R = μ_L + z·σ_L) | P2 | Easy |
| 6 | Newsvendor: critical ratio → optimal order quantity (normal demand) | P2 | Intermediate |
| 7 | (Q,R) policy: one full iteration of the Q–R procedure (Q0 = EOQ → R0 → Q1) | P2 | Advanced |
| 8 | Takt time, theoretical minimum workstations, line efficiency / balance delay | P3 | Easy |
| 9 | Assembly-line balancing by a prescribed heuristic (e.g., longest-task-time): resulting station count → balance efficiency | P3 | Intermediate |
| 10 | Aggregate planning: chase vs. level strategy total-cost comparison [BRANCHING: cheaper strategy is parameter-dependent] | P3 | Advanced |

Difficulty split: 4 Easy (1, 2, 5, 8) / 4 Intermediate (3, 4, 6, 9) / 2 Advanced (7, 10). ✓

---

## 3. Domain 3 — Quality & Reliability Control

### Textbooks

| Role | Book | Justification |
|---|---|---|
| Primary | D.C. Montgomery, *Introduction to Statistical Quality Control*, 8th ed. (Wiley) | THE standard SQC course text (8 editions; universally adopted for SPC courses — web-verified). Control charts for variables Ch. 6, attributes Ch. 7, process capability Ch. 8 ("Process and Measurement System Capability Analysis"), acceptance sampling Ch. 15–16. Appendix Table VI is the binding source for control-chart constants (Stage B). |
| Primary | E.L. Grant, R.S. Leavenworth, *Statistical Quality Control*, 7th ed. (McGraw-Hill, 1996) | The classic of the field (1st ed. 1946); historical standard for X̄-R practice and acceptance sampling; cross-validation of constants and typologies. |
| Backup | A. Mitra, *Fundamentals of Quality Control and Improvement*, 4th ed. (Wiley, 2016) | Third common adoption; backup typology source. |

### Area map (chapters per Montgomery — numbering identical in supplied 7th ed. and 8th ed., verified from the on-disk outline)

| Area | Chapters | Pedagogical role | Quota |
|---|---|---|---|
| Q1. Variables Control Charts (X̄-R, X̄-s, OC/ARL) | Ch. 6 (+§6.3 e-Handbook cross-check) | Cornerstone | 4 |
| Q2. Process Capability (Cp, Cpk, fraction nonconforming) | Ch. 8 | Core | 2 |
| Q3. Attributes Control Charts (p, np, c, u) | Ch. 7 | Core | 2 |
| Q4. Acceptance Sampling by Attributes (single plans, OC, AOQ/ATI) | Ch. 15; MIL-STD-105E | Core | 2 |

### Suggested template slate

| # | Concept | Area | Difficulty |
|---|---|---|---|
| 1 | X̄-R chart limits from m subgroups (A2, D3, D4) + σ̂ = R̄/d2 | Q1 | Easy |
| 2 | X̄ chart limits with known σ (3σ limits at subgroup size n) + out-of-control count | Q1 | Easy |
| 3 | Variables chart construction where sampled subgroup size dictates the chart pair [BRANCHING: small n → X̄-R (A2), large n → X̄-s (A3, B3, B4)] | Q1 | Intermediate |
| 4 | β-risk and out-of-control ARL for a specified mean shift (Φ computation → ARL1 = 1/(1−β)) | Q1 | Advanced |
| 5 | Cp and Cpk from spec limits with σ̂ = R̄/d2; capability verdict | Q2 | Easy |
| 6 | Expected fraction nonconforming (ppm) vs. specification [BRANCHING: one-sided vs. two-sided spec] | Q2 | Intermediate |
| 7 | p-chart limits from historical fraction nonconforming [BRANCHING: LCL = max(0, ...) floor] | Q3 | Easy |
| 8 | c-chart limits + out-of-control assessment for defect counts | Q3 | Intermediate |
| 9 | Single sampling plan: P(accept) at a given lot fraction defective (OC-curve point, binomial/Poisson) | Q4 | Intermediate |
| 10 | Rectifying inspection: AOQ and ATI for a single sampling plan | Q4 | Advanced |

Difficulty split: 4 Easy (1, 2, 5, 7) / 4 Intermediate (3, 6, 8, 9) / 2 Advanced (4, 10). ✓

---

## 4. Branching plan (≥3 parameter-dependent branching templates per domain)

| Domain | Branching templates | Mechanism |
|---|---|---|
| Stochastic Operations | S1-#3, S3-#8, S3-#9 (+ ρ<1 steady-state feasibility gate asserted in every S1 template) | Configuration-selection decision; sampled topology changes the governing formula; series vs. parallel MTTF formula families |
| Production & Inventory | P1-#3, P1-#4, P3-#10 | Discount-regime decision; lead-time regime τ vs. T changes the reorder-point formula; chase-vs-level winner depends on sampled costs |
| Quality & Reliability Control | Q1-#3, Q2-#6, Q3-#7 | Subgroup-size-driven chart-type selection (different constants and limit formulas); one-sided vs. two-sided spec; LCL zero-floor logic |

Note on the ρ<1 gate: per AUTHOR_NOTES lesson on feasibility windows, every queueing template samples (λ, μ, c) jointly so that ρ < 1 by construction *and* asserts it; S1-#4 (finite capacity) is the deliberate exception where ρ ≥ 1 is admissible and the solution reasons about it explicitly.

## 5. Authoritative data sources for `constants.py` (Stage B inputs)

| Data | Source |
|---|---|
| Control-chart constants A2, A3, B3, B4, D3, D4, d2, d3, c4 (n = 2…25) | **Montgomery (supplied 7th ed., ON DISK), Appendix Table VI "Factors for Constructing Variables Control Charts"** — located at PDF p. 738 with a **clean text layer** (verified 2026-08-04; spot values A2(2)=1.880, c4(2)=0.7979, d2(5)=2.326 extract correctly). Verbatim transcription per hard rule 2 / lesson 18. Derivation-based provenance check: c4 and d2 are computable from their Γ-function/integral definitions — the same style of check that caught the Terzaghi Nγ incident. Secondary check: NIST/SEMATECH e-Handbook §6.3.2 (on disk; renders factors as MathJax formulas — cross-check only). |
| Acceptance-sampling code letters & single-plan master tables | MIL-STD-105E Tables I / II-A (on disk, `pilot/references/public/mil_std_105e_sampling.pdf`; OCR layer noisy — transcribe from page images). Used for realistic (n, c) plan parameters; OC/AOQ/ATI values are computed, never read from tables. |
| Standard normal CDF Φ and quantiles z | Computed in-template via `math.erf` (deterministic, no table interpolation); solutions display z and Φ(z) at declared precision so a student can follow with a z-table. Spot-check vs. Montgomery Appendix Table II. Convention documented in constants.py. |
| Service-system parameter realism (λ, μ, c ranges; cost/hour ranges) | H&L Ch. 17 / Taha worked-example ranges — realism bounds only, never verbatim numbers |
| Inventory cost conventions (K, h = i·c, p, proportional discounts) | Nahmias Ch. 4–5 conventions and typical ranges — realism bounds only |
| Component reliability ranges (0.90–0.999 class), exponential failure-rate ranges | Ross Ch. 9 conventions; NIST/SEMATECH e-Handbook Ch. 8 (`apr/`) |
| Poisson/exponential/normal distribution conventions (parameterization: rate vs. mean) | Ross Ch. 5 (rate parameterization λ); documented once in constants.py to prevent λ-vs-1/λ ambiguity across templates |

## 6. Unit-system note (Gate A decision point)

Unlike Civil (dual SI / US-customary), this branch is **dimensionally light**: quantities are rates (customers/hour, units/year), counts, probabilities, and currency. There is no meaningful SI-vs-US duality to exercise, so the benchmark's "beyond variable substitution" diversity is carried instead by regime/topology/decision branching (§4) and by time-unit consistency reasoning (e.g., λ per hour vs. μ per minute conversions inside queueing templates — at least one S1 template will deliberately mix time units). **Approver: please confirm this convention.**

## 7. Overlap-avoidance notes (vs. existing branches, checked 2026-08-03)

- Existing Chemical / Electrical / Mechanical branches contain **no** queueing, Markov, reliability, inventory, production-planning, or SPC content (verified against `data/templates/branches/` file inventory).
- Closest touchpoint: `electrical_engineering/digital_communications/deterministic_and_random_signal_analysis.py` computes signal energy/power, mean/variance of a random signal, and autocorrelation — communications-signal reasoning, not stochastic-process modeling. To keep separation clean, S-areas contain **no bare mean/variance computations**: every S-template reasons over a process model (queue, chain, reliability structure, Poisson process).
- Civil branch: zero overlap (entirely different mathematics).
- Within-branch separations: newsvendor lives ONLY in P2 (not duplicated from H&L §18.7 into S-areas); S1 uses continuous-time birth–death steady-state results while S2 is strictly discrete-time chains (Chapman–Kolmogorov, absorption) — distinct reasoning chains; reliability lives ONLY in S3 (Q-areas exclude life-testing entirely).

## 8. Exact bibliographic identifiers (web-verified 2026-08-03)

| Book | Edition / Publisher | ISBN-13 |
|---|---|---|
| Hillier & Lieberman, *Introduction to Operations Research* | 11th ed., McGraw-Hill, 2021 | 978-1-259-87299-0 (ISE: 978-1-260-57587-3) |
| Ross, *Introduction to Probability Models* | 12th ed., Academic Press/Elsevier, 2019 | 978-0-12-814346-9 |
| Nahmias & Olsen, *Production and Operations Analytics* | 8th ed., Waveland Press, 2020 | 978-1-4786-3926-8 |
| Montgomery, *Introduction to Statistical Quality Control* | 8th ed., Wiley, 2020 | 978-1-119-72309-7 (print companion; eText 978-1-119-39930-8; EMEA 978-1-119-65711-8) |
| Taha, *Operations Research: An Introduction* | 10th ed., Pearson, 2016 | 978-0-13-444401-7 |
| Silver, Pyke & Thomas, *Inventory and Production Management in Supply Chains* | 4th ed., CRC Press, 2016 (2021 pbk reprint) | 978-1-4665-5861-8 (pbk: 978-1-032-17932-2) |
| Grant & Leavenworth, *Statistical Quality Control* | 7th ed., McGraw-Hill, 1996 | 978-0-07-043555-1 |
| Mitra, *Fundamentals of Quality Control and Improvement* | 4th ed., Wiley, 2016 | 978-1-118-70514-8 |

## 9. Already on disk

### 9.1 Public references (fetched 2026-08-03)

| Item | Location | Role |
|---|---|---|
| NIST/SEMATECH *e-Handbook of Statistical Methods* (NIST Handbook 151), complete offline copy (official `handbook.zip`, 14,506 files extracted) | `pilot/references/public/nist_sematech_ehandbook/handbook/` | SPC (Ch. 6 `pmc/`), comparisons (Ch. 7 `prc/`), reliability (Ch. 8 `apr/`) — the public-domain anchor for this branch (NAVFAC analog) |
| MIL-STD-105E (10 May 1989, 73 pp., distribution unlimited) | `pilot/references/public/mil_std_105e_sampling.pdf` | Acceptance-sampling plans (Q4) |

### 9.2 As-supplied copies (received 2026-08-04, `pilot/references/public/full_books_industrial_engineering/`; verified 2026-08-04)

| Book | Supplied edition | Text extraction | Stage B/C handling |
|---|---|---|---|
| Hillier & Lieberman | **7th ed.** (2001), not 11th | Full text, clean (`extracted/hillier_lieberman_or_7e.txt`) | Primary anchor. Chapter map re-anchored: Ch. 16 Markov Chains (IN PRINT — better than 11e), Ch. 17 Queueing, Ch. 19 Inventory. Queueing/Markov/inventory fundamentals are edition-stable; Appendix 5 statistical tables available for Φ spot-checks. |
| Ross | **11th ed.** (2014), not 12th | Full text, clean (`extracted/ross_probability_models_11e.txt`) | Primary anchor; chapter numbering identical to 12e (Ch. 4 Markov / Ch. 5 exponential-Poisson / Ch. 8 queueing / Ch. 9 reliability — verified from outline + text). |
| Nahmias & Olsen | **7th ed.** *Production and Operations Analysis* (Waveland), not 8e *Analytics* — file name mislabeled | **Image-only scan** (674 pp., no text layer; pypdf + PyMuPDF both find zero text) | Primary anchor via **targeted visual page reads** (rendered page images are clean — TOC read visually). Chapter map re-anchored to 7e: Ch. 4 / Ch. 5 / Ch. 3 §3.4–3.5 / Ch. 9 §9.10 line balancing. Numeric conventions cross-checked against text-layer H&L Ch. 19 + Silver TOC terms. |
| Montgomery | **7th ed.** (2013), not 8th | Full text, clean (`extracted/montgomery_isqc_7e.txt`) | Primary anchor; chapter numbering identical to 8e (Ch. 6/7/8/15/16 verified from outline). **Appendix Table VI verified on disk with clean text layer (PDF p. 738)** — Stage B constants transcription fully unblocked. |
| Grant & Leavenworth | **3rd ed. (1964)** — copyright page shows 1946/1952/1964; much older than the planned 7th (1996) | **Image-only scan** (620 pp.) | Downgraded to historical typology cross-check via targeted visual reads. Shewhart-chart practice and factor definitions are stable since the 1950s, but NO numeric value may be sourced from it (Montgomery is the binding source anyway). Optional user-side: re-supply the 7th ed. if convenient — not blocking. |
| Silver, Pyke & Thomas | 4th ed., **partial: 81 pp. = front matter + full TOC + Ch. 1–2 (through p. 52)** | Text present for supplied pages (`extracted/silver_pyke_thomas_4e_PARTIAL_ch1-2.txt`) | **Unusable for quantitative grounding** (inventory-math chapters absent; mirrors the Chin situation in Civil). Kept for TOC/terminology alignment only. P2 cross-validation burden shifts to H&L 7e Ch. 19 + Taha Ch. 13/16. Re-source if desired — not blocking. |
| Taha | 10th ed., **Global Edition** (2017) | Full text, clean (`extracted/taha_or_10e_global.txt`) | Backup as planned; Ch. 13 Inventory Modeling, Ch. 16 Probabilistic Inventory Models, Ch. 17 Markov Chains, Ch. 18 Queuing Systems (verified from outline). Global-edition page numbers may differ from US print — cite section numbers, not pages. |
| Mitra | **3rd ed.** (2008), not 4th | Full text, clean (`extracted/mitra_quality_3e.txt`) | Backup as planned; SPC/acceptance-sampling fundamentals edition-stable. |

**Books-first rule status: SATISFIED (2026-08-04).** All four primary anchors are on disk; Stage B is fully unblocked (Montgomery Appendix Table VI has a clean text layer) and Stage C grounding texts are available — pending Gate A approval of this document, including the edition substitutions above.

## 10. Gate A checklist for approver

- [ ] Books are the right anchors per domain (or name replacements)
- [ ] **Edition substitutions accepted as supplied (§9.2):** H&L 7e, Ross 11e, Nahmias 7e (image-only), Montgomery 7e, G&L 1964 3e (cross-check only), Mitra 3e, Silver 4e partial (TOC only), Taha 10e Global
- [ ] Ross + H&L 7e Ch. 16 accepted as the Markov-chain grounding; Ross Ch. 9 for reliability
- [ ] Area maps and quota weights acceptable (chapter maps re-anchored to supplied editions)
- [ ] Suggested slates directionally right (final concepts fixed in Stage C; slate is non-binding)
- [ ] Data-source list acceptable for Stage B curation (Montgomery 7e Appendix Table VI — verified on disk — as the binding control-chart-constant source; MIL-STD-105E for sampling plans; `math.erf` convention for Φ)
- [ ] Unit-light convention (§6) confirmed for this branch — branching diversity in place of dual-unit diversity
