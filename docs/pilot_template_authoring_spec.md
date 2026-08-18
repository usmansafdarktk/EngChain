# Implementation Spec — Agentic Pilot Authoring of EngTrace Templates (Phase 1 Only)

**Version:** 1.0
**Status:** Draft for supervisor review
**Scope:** Template authoring (Phase 1) for new engineering branches, executed by AI agents, one branch at a time.
**Out of scope:** AI Tribunal pre-screening (Phase 2), human expert certification (Phase 3), full 15-seed testset instantiation (Phase 4). These run later, with human experts, only if the pilot justifies the investment.

---

## 1. Purpose

Before recruiting human domain experts (costly, slow), produce a **pilot template set** for each new branch that:

1. follows the *same rigorous methodology* used for the original 90 templates — textbook grounding, authoritative data sources, physically constrained parameterization, computed gold traces;
2. is hardened through **multiple independent AI review cycles** per template (a stand-in for, not a replacement of, the Tribunal + human certification);
3. is directly runnable through the **existing, unmodified EngTrace inference and evaluation pipeline**, so sample models can be evaluated on it and expected outcomes understood.

The pilot answers one question: *is authoring high-quality symbolic templates in these branches feasible and worth full human-expert validation?*

**Integrity boundary:** pilot templates MUST NOT be merged into `data/templates/` (the certified benchmark) and MUST NOT be reported in the paper unless they later pass the real Phase 2 (AI Tribunal) and Phase 3 (human certification) pipeline.

---

## 2. Branches, domains, and quotas

Branches are executed **strictly one at a time**, in priority order. A branch starts only after the previous branch's Final Report (§9) is delivered.

| Priority | Branch | Domain 1 | Domain 2 | Domain 3 |
|---|---|---|---|---|
| 1 | Civil Engineering | Structural Analysis | Geotechnical Engineering | Water Resources & Hydraulics |
| 2 | Industrial Engineering / OR | Stochastic Operations | Production & Inventory | Quality & Reliability Control |
| 3 | Aerospace Engineering | Gas Dynamics & Compressible Flow | Orbital Mechanics | Propulsion |

Per-domain quota: **10 templates, stratified 4 Easy / 4 Intermediate / 2 Advanced** (mirrors the benchmark's ≈75% foundational / 25% advanced weighting, §3.4 / Table 9 of the paper). Per branch: **30 templates**.

Domain names above are the working taxonomy (derived from ABET curricula and professional-society standards: ASCE, IISE, AIAA). Stage A (§4) may refine *areas within* a domain, but MUST NOT change the three domains without explicit human sign-off.

### 2.1 Difficulty rubric (binding definition)

Aligned to the paper's three axes (Conceptual Complexity, Mathematical Sophistication, Procedural Depth):

- **Easy:** single governing principle; direct algebraic substitution; 3–4 solution steps. (Exemplar: `template_basic_stress_strain`.)
- **Intermediate:** two coupled concepts OR a regime decision that changes the applicable formula OR non-trivial unit-system reasoning; 4–7 steps. (Exemplar: `template_aliased_frequency_identification`.)
- **Advanced:** multi-concept synthesis requiring construction of a system of equations / integration / iteration from first principles before any numeric substitution; ≥6 steps. (Exemplar: `template_statically_indeterminate`.)

---

## 3. The template contract (what every template MUST be)

Every template is a Python function reproducing the exact anatomy of the existing 90 (see `data/templates/branches/.../mole_balances.py` for reference style):

```python
def template_<snake_case_name>():
    """
    <Title>

    Scenario:
        <2–5 sentences: the physical setup, the governing equation(s) shown
        explicitly, and what is being solved for.>

    Difficulty: <Easy | Intermediate | Advanced>
    Grounding: <Book, edition, chapter/section that inspired the problem typology>
    Physical bounds: <the ranges/constraints that guarantee physical realism>

    Returns:
        tuple(str, str): (question, solution)
    """
    # 1. Parameterize inputs  — sample ONLY from branch constants.py and
    #    physically constrained ranges; constraints must encode physics,
    #    not just bounds.
    # 2. Core computation     — compute the ground truth by executing the real
    #    engineering calculation (math/scipy allowed; must be deterministic).
    # 3. Serialize            — f-string question + step-by-step gold solution.
    return question, solution
```

**Hard formatting requirements** (these are what the downstream parser and Tier-1 verifier key on — violations are automatic rejection):

- R1. Solution steps formatted exactly `**Step X:** <text>` starting on a new line; `**Given:**` block first is encouraged.
- R2. Solution ends with exactly one line `**Answer:** ... <value> <units>`, and the final numeric value in that line is the quantity being asked for. **Single final numeric answer per template** (avoid multi-part a)/b) answers — the parser takes the last number; multi-part answers make Final Answer Accuracy ill-defined).
- R3. Every step that produces a quantity embeds the computed intermediate value in the step text (this is what makes the trace verifiable step-by-step).
- R4. Randomness uses ONLY the stdlib `random` module (no `numpy.random`, no time/uuid), so `random.seed(s)` before the call makes output fully reproducible.
- R5. All numeric display values rounded to a declared precision; no raw float artifacts (`0.30000000000000004`).
- R6. Question is self-contained: solvable with only the stated values plus universal constants; no reference to figures/tables/diagrams.
- R7. Parameterization pulls named physical data (materials, fluids, media, distributions, code values) from the branch `constants.py`, never inlined magic values.

**Structural-diversity requirement:** within a domain, each template MUST introduce a *qualitatively distinct reasoning chain* (different governing equation, regime logic, or derivation structure) — not a re-skin of another template with different variable names. At least 3 of the 10 templates per domain SHOULD have parameter-dependent branching that changes the reasoning path (unit system, geometry, physical regime), mirroring the benchmark's "beyond variable substitution" claim.

**Copyright/plagiarism rule:** templates take *problem typologies* from the textbooks — never verbatim problem statements or verbatim numbers from worked examples. All wording is original; all parameters are sampled.

---

## 4. Pipeline stages (per branch)

### Stage A — Branch scoping (agent: **Librarian**)

Inputs: branch name, the three fixed domains.
Tasks:
1. For each domain, identify the **2 most-adopted, most-cited undergraduate/graduate textbooks** plus 1 backup, with evidence of authority (standard curricular adoption, edition count, professional-society endorsement). Web search REQUIRED; do not rely on memory alone.
2. For each domain, extract a **chapter-level area map**: 3–4 fundamental areas (chapter-scale pedagogical units) with the book chapters they correspond to, and allocate the 10-template quota across areas (weighted toward cornerstone areas, per the Pedagogical Significance principle).
3. Identify the **authoritative data sources** for parameterization (handbooks, standards, government data — e.g., ACI 318 / AISC Manual / Manning's n tables for Civil; control-chart constants and standard-distribution tables for IE; US Standard Atmosphere 1976 / JPL planetary constants for Aerospace).

Output: `pilot/branches/<branch>/BOOKS.md` — books with justifications, area map with chapter mapping, quota allocation, data-source list.
Gate A: a human (you) skims BOOKS.md and approves before Stage B. This is the one cheap human checkpoint that anchors everything downstream.

### Stage B — Constants curation (agents: **Data Curator**, then **Data Reviewer**)

1. Curator authors `pilot/templates/branches/<branch_snake_case>/constants.py` in the style of the existing branch constants files: named lists/dicts of real materials, fluids, soils, distributions, dimensionless constants, etc. **Every entry carries an inline comment citing its source** (handbook + table/section).
2. Data Reviewer (fresh agent, no access to Curator's session) spot-verifies ≥20% of entries (and 100% of universal constants) against the cited sources via web search; flags discrepancies; Curator fixes. Loop until zero discrepancies.

Output: cited `constants.py` + `pilot/branches/<branch>/data_review_log.md`.
Gate B: review log shows all flags resolved.

### Stage C — Per-template authoring + hardening loop (agents: **Author**, **R1–R3 Reviewers**, orchestrated per §5)

For each planned template (from the Stage A allocation), sequentially:

1. **Author** writes the template per the §3 contract, grounded in the assigned book chapter.
2. **Automated harness** (§6) runs. Any failure → Author revises. Reviewers never see a template that fails the harness.
3. **Independent review cycle** (§5): three reviewer agents score it; Author revises against consolidated feedback; loop until the acceptance gate passes or the cycle cap is hit.
4. On acceptance: template + its review log are frozen. On cap-out: template is **discarded and replaced** with a new concept from the same area (never force-accepted); the failure is logged.

### Stage D — Domain wrap-up (agent: **Domain Auditor**, fresh context)

After 10 templates are accepted for a domain:
1. **Diversity audit:** verify the structural-diversity requirement across the 10 (no near-duplicate reasoning chains; flag pairs whose solution skeletons are isomorphic). Any violation → replace the weaker template via Stage C.
2. **Coverage audit:** confirm area allocation and the 4/4/2 difficulty split were honored; confirm each difficulty label against §2.1 (auditor re-labels blind, mismatches are reconciled).
3. Emit `pilot/branches/<branch>/<domain>/domain_report.md`.

### Stage E — Branch wrap-up (orchestrator)

1. Regenerate and re-run the full harness over all 30 templates from a clean process.
2. Generate the **pilot mini-testset**: 5 instances per template (documented seeds) → 150 JSONL records in the exact schema of the real testset (`id`, `seed`, `branch`, `domain`, `area`, `level`, `question`, `solution`) so `evaluation/run_inference.py` and the evaluation framework run **unchanged**.
3. Emit the branch Final Report (§9).

---

## 5. Review protocol (the hardening loop)

### 5.1 Reviewer roles

Each reviewer is a **separate agent instance with a fresh context**. Reviewers receive ONLY: the template source code, 5 generated instances (fixed seeds 101–105), the domain's BOOKS.md excerpt, and the rubric. They never see the Author's reasoning, other reviewers' outputs, or prior cycle scores (each cycle is blind).

- **R1 — Physical Plausibility Auditor** (domain-expert persona): are scenarios physically real across all sampled instances? Are ranges realistic for the named materials/systems? Does any parameter combination violate the stated regime (e.g., laminar formula at turbulent Re, steady-state queue at ρ ≥ 1, subsonic relation at M > 1)? MUST actively search for a breaking parameter combination by reading the sampling logic, not just the 5 instances.
- **R2 — Mathematical Correctness Verifier**: independently **re-solves 3 of the 5 instances numerically with its own code** (not by eyeballing the trace) and compares every intermediate value and the final answer. Also checks unit consistency symbolically at every step.
- **R3 — Pedagogical Clarity & Solvability Reviewer**: is the question unambiguous and solvable from stated information alone; are all symbols defined; is the gold trace a faithful, complete derivation a student could follow; is the difficulty label consistent with §2.1?

### 5.2 Scoring and acceptance gate

Each reviewer returns the Tribunal rubric JSON (identical dimensions to Appendix H, for continuity):
`physical_plausibility_score`, `mathematical_correctness_score`, `pedagogical_clarity_score` (1–5), `confidence_score`, `blocking_flag` (bool), `findings` (list of specific, actionable defects with the offending code line or instance excerpt).

**Acceptance gate (all conditions):**
- every reviewer scores **≥ 4 on every dimension**;
- **zero** `blocking_flag`s;
- R2's independent recomputation matches all checked intermediates and the final answer within 0.1% relative.

This is deliberately stricter than the Tribunal's median-≥4 rule: the pilot has no human safety net behind it.

### 5.3 Revision loop policy

- After each cycle, an **Arbiter** step consolidates the three reviews into a deduplicated defect list; the Author revises against it.
- **Cycle cap: 4 review cycles per template.** Not converged by cycle 4 → discard and replace (§4 Stage C.4). Log the discarded template and the unresolved defects — these logs are evidence for the feasibility question.
- A template revised for *any* reason re-runs the full harness before re-review.
- Reviewer findings that dispute the *physics* (not the code) and survive one full cycle unresolved are escalated to the human checkpoint list in the Final Report rather than silently overridden.

---

## 6. Automated verification harness (runs before every review cycle)

A single script, `pilot/harness/check_template.py`, executed per template. All checks MUST pass:

| # | Check | Pass condition |
|---|---|---|
| H1 | Execution | 25 seeded runs (`random.seed(s)` for s in 1..25), zero exceptions, < 5 s per instance |
| H2 | Determinism | same seed twice → byte-identical `(question, solution)` |
| H3 | Format | R1/R2 of §3 hold: step markers parse, exactly one `**Answer:**` line |
| H4 | Parser round-trip | `evaluation.engineering_parser.extract_steps(solution)` yields ≥ 3 steps and a non-None final answer **equal to the template's internally computed value** (rel. err < 1e-6) |
| H5 | Numeric hygiene | no NaN/Inf anywhere; all displayed floats respect declared precision; no float artifacts |
| H6 | Instance diversity | across the 25 runs: ≥ 10 distinct final answers and ≥ 10 distinct question strings |
| H7 | Bounds conformance | values asserted against the docstring's declared "Physical bounds" (each template embeds these as assertions in its own code; harness verifies assertions exist and none fire across 25 runs) |

Harness output is appended to the template's review log.

---

## 7. Artifacts and directory layout

```
pilot/
  harness/check_template.py
  branches/<branch>/
    BOOKS.md                      # Stage A output (human-approved)
    data_review_log.md            # Stage B output
    <domain>/domain_report.md     # Stage D output
    review_logs/<template>.jsonl  # one record per review cycle: harness result,
                                  # 3 reviews, arbiter summary, author changelog
  templates/branches/<branch_snake_case>/
    constants.py
    <domain_snake_case>/<area_snake_case>.py   # mirrors data/templates layout
  testset_preview/<branch>/*.jsonl             # Stage E mini-testset (5 seeds/template)
  reports/<branch>_final_report.md
```

The `pilot/templates/branches/` tree intentionally mirrors `data/templates/branches/` so that promotion after real Phase 2/3 validation is a file move, and so `template_loader`-style discovery works against it.

---

## 8. Agent execution rules

- **One branch at a time; within a branch, domains sequential; within a domain, templates sequential.** (Review cycles for template *n* may not overlap with authoring of template *n+1* — reviewer feedback on early templates is folded into an `AUTHOR_NOTES.md` style guide that the Author re-reads before each new template, so quality compounds.)
- Author, Reviewers, Data Curator/Reviewer, and Domain Auditor are **distinct agent instances**; a reviewer never reviews its own authoring, and fresh contexts are mandatory for every review cycle.
- Every agent that asserts a real-world fact (book adoption, constant value, code provision, material property) MUST ground it via web search or the cited source, and record the citation in the relevant log.
- All agent prompts are stored under `pilot/prompts/` and versioned; a change to a prompt mid-branch is recorded in the Final Report (it is a methodological change).

---

## 9. Final Report (per branch) — the "is it worth it?" deliverable

`pilot/reports/<branch>_final_report.md` MUST contain:

1. Inventory: 30 accepted templates (name, area, difficulty, grounding book/chapter, one-line reasoning-chain description).
2. Hardening statistics: review cycles per template (distribution), discard/replace count with reasons, most common defect categories caught by R1/R2/R3 — this is the direct evidence of where human experts will/won't be needed.
3. Escalation list: unresolved physics disputes and any judgment calls needing a human domain expert.
4. Model-pilot readiness: confirmation the mini-testset runs through `run_inference.py` + the evaluation framework unchanged, with one worked example.
5. Recommendation: go / no-go / revise for full human-expert Phase 2–3 on this branch.

---

## Appendix — Stage A starting candidates (Librarian must verify, may extend)

**Civil:** Hibbeler *Structural Analysis*; Kassimali *Structural Analysis* (alt) · Das *Principles of Geotechnical Engineering*; Craig's *Soil Mechanics* (alt) · Chow *Open-Channel Hydraulics*; Mays *Water Resources Engineering* (alt). Data: ACI 318, AISC Steel Construction Manual, ASCE 7, Manning roughness tables, standard soil property tables.

**Industrial/OR:** Hillier & Lieberman *Introduction to Operations Research*; Ross *Introduction to Probability Models* · Nahmias *Production and Operations Analysis* · Montgomery *Introduction to Statistical Quality Control*. Data: control-chart constant tables (A2, D3, D4, c4), standard normal/Poisson/exponential parameter conventions, standard acceptance-sampling plans.

**Aerospace:** Anderson *Modern Compressible Flow*; Anderson *Fundamentals of Aerodynamics* (alt) · Curtis *Orbital Mechanics for Engineering Students*; Vallado (alt) · Sutton *Rocket Propulsion Elements*; Hill & Peterson *Mechanics and Thermodynamics of Propulsion* (alt). Data: US Standard Atmosphere 1976, isentropic/normal-shock relations (γ = 1.4), JPL planetary constants, standard propellant property tables.
