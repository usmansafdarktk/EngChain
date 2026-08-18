# EngTrace Pilot — Session Handoff (written 2026-08-02)

Read this fully before doing anything. It is the authoritative context for
continuing the template-authoring pilot. The governing process document is
`docs/pilot_template_authoring_spec.md` — follow it exactly.

## 1. Project context

- This repo implements the **EngTrace** paper (symbolic benchmark for
  verifiable process supervision of engineering reasoning; full extracted
  text at `docs/_ARR_May__EngTrace.txt`). 90 expert-authored Python
  templates × 15 seeds = 1,350 instances across Chemical/Electrical/
  Mechanical; two-stage evaluation (Tier-1 symbolic step matching + AI
  Tribunal); 27 models evaluated.
- Rejected twice at ACL for **limited branch scope**. Decision: add
  branches in priority order **Civil → Industrial/OR → Aerospace**.
- Before committing human experts, the user's supervisor approved an
  **agentic Phase-1 pilot**: AI agents author and harden 30 templates per
  branch (10 per domain, 4 Easy/4 Intermediate/2 Advanced), following the
  original paper's methodology (textbook grounding, authoritative
  constants, multi-cycle independent review). Phases 2/3 (AI Tribunal,
  human certification) are explicitly OUT of pilot scope; pilot templates
  live under `pilot/` and never enter `data/templates/` or the paper
  without the real validation pipeline.

## 2. State: CIVIL ENGINEERING BRANCH COMPLETE (verdict: GO)

All stages done (2026-07-31 → 2026-08-02):
- Gate A approved; Stage B constants curated and independently verified
  (`pilot/templates/branches/civil_engineering/constants.py`, page-cited).
- **30 templates accepted** across geotechnical_engineering (Stage D:
  FAIL→remediated→PASS), structural_analysis (PASS first attempt),
  water_resources (PASS, zero actions). ~50 review cycles, 15 genuine gate
  failures caught and fixed, 0 forced acceptances.
- Stage E: **150-record mini-testset** at
  `pilot/testset_preview/civil_engineering/*.jsonl` (seeds 201–205; exact
  real-testset schema: id/seed/branch/domain/area/level/question/solution;
  150/150 verified through `evaluation/engineering_parser.py`).
- Branch final report: `pilot/reports/civil_engineering_final_report.md`.
- Headline integrity event: the Terzaghi Nγ constants passed WEB
  verification with six wrong values (mixed Vesić/Kumbhojkar families);
  caught by R2's derivation-based provenance check and corrected by
  verbatim transcription from the on-disk Das book (see
  `pilot/branches/civil_engineering/data_review_log.md`, Cycles 3–4; the
  two Das books also disagree at Nγ(40°): 116.31 PGE vs 115.31 PFE —
  logged for human experts).

## 3. Key artifacts (read as needed, not all up front)

- `docs/pilot_template_authoring_spec.md` — stages A–E, template contract
  (§3), reviewer protocol (§5), harness checks H1–H7 (§6), layout (§7).
- `pilot/branches/civil_engineering/AUTHOR_NOTES.md` — **30 compounded
  lessons; re-read before authoring ANY template** (per-step
  round-then-recompute; per-sample joint-corner feasibility windows;
  primary-source-only verification of tabulated data; single final
  numeric answer; question-prescribed iteration schemes; display precision
  sized to downstream amplification; label-value consistency; branching
  planned at area level; etc.).
- `pilot/harness/check_template.py` (run at 300 seeds; must pass before
  any review) and `pilot/harness/build_mini_testset.py` (Stage E).
- `pilot/prompts/*.md` — versioned agent prompts (author, R1 physics, R2
  math re-solve, R3 clarity, data reviewer). Reviewers are FRESH-context
  subagents; review instances use seeds 101–105 via the gen_instances
  scratchpad pattern.
- Per-domain: `BOOKS.md` (Stage A, needs the user's Gate A approval),
  `data_review_log.md`, `review_logs/*.jsonl`, `domain_report.md`s.
- References: `pilot/references/public/` (public-domain gov docs I fetched
  + MANIFEST.md) and `pilot/references/public/full_books/` (user-supplied
  licensed textbooks with `extracted/*.txt` full texts). All gitignored.

## 4. Hard process rules (non-negotiable, learned or user-set)

1. **Books first**: no Stage C authoring until the branch's primary
   textbooks are on disk and extracted. NEVER download copyrighted books
   (user supplies via licensed channels); public-domain US-government
   documents MAY be fetched directly.
2. **Primary-source transcription is the only valid verification for
   tabulated empirical data** — web cross-checks create false confidence
   (Terzaghi incident).
3. **Gate A is a human checkpoint**: the user approves BOOKS.md before
   Stage B. Stage D domain audits and per-template gates are agent-run.
4. Templates: exact `**Step X:**`/`**Answer:**` format; ONE final numeric
   answer; stdlib `random` only; asserts encode docstring Physical bounds;
   every printed equation must reproduce from its displayed operands.
5. Gate = every reviewer ≥4 on every dimension, zero blocking flags, R2
   independent re-solve within 0.1% (quantization distinguished); max 4
   cycles then discard-and-replace; Stage D needs ≥3 branching templates
   per domain and blind difficulty relabels to concur.
6. Report to the user at milestones (area/domain), not per template. The
   user sometimes sends stray keystrokes mid-turn ("ecd", "02") — ignore
   politely. The user approves with short messages ("continue",
   "approved").

## 5. NEXT TASK: Industrial Engineering / Operations Research branch

Decision confirmed by the user (2026-08-02). Execute the spec end-to-end,
one stage at a time, exactly as done for Civil:

- **Stage A (start here)**: domains = Stochastic Operations (queueing
  M/M/1 vs M/M/c, reliability series/parallel, Markov chains) /
  Production & Inventory (EOQ, quantity-discount regime, newsvendor,
  line balancing) / Quality & Reliability Control (X̄-R charts, Cp/Cpk,
  acceptance sampling). Candidate books to web-verify: Hillier &
  Lieberman *Introduction to Operations Research*; Ross *Introduction to
  Probability Models*; Nahmias *Production and Operations Analysis*;
  Montgomery *Introduction to Statistical Quality Control*. Public-domain
  anchor to FETCH into `pilot/references/public/`: **NIST/SEMATECH
  e-Handbook of Statistical Methods** (SPC, reliability — the NAVFAC
  analog for this branch). Produce `pilot/branches/industrial_engineering/
  BOOKS.md` (books+ISBNs, area maps with chapters, 10-template slates at
  4/4/2, data-source table, branching plan ≥3 per domain: ρ<1 steady-state
  gates, M/M/1-vs-M/M/c selection, discount-regime decision, chart-type
  selection, series-vs-parallel topology) → STOP for Gate A.
- **Stage B**: constants.py — control-chart constants (A2, D3, D4, c4,
  d2) MUST be transcribed from Montgomery's appendix tables once on disk
  (lesson 18); distribution conventions; standard sampling plans.
- **Stages C–E**: per spec, with all 30 AUTHOR_NOTES lessons applied from
  the start. New-branch layout:
  `pilot/templates/branches/industrial_engineering/<domain>/<area>.py`.
- User-side pending: acquiring the IE textbooks (chapter PDFs into
  `pilot/references/public/full_books/` or a new branch folder — follow
  wherever the user drops them); optionally running the Civil mini-testset
  model pilot (`evaluation/run_inference.py` consumes it unchanged).

## 6. Parked items (do not lose)

- Aerospace = branch 3 (Gas Dynamics / Orbital Mechanics / Propulsion;
  Anderson, Curtis, Sutton; US Standard Atmosphere public-domain).
- Escalation lists for eventual human experts: in each domain report +
  data_review_log (judgment screens, Das-vs-Das Nγ(40°), difficulty
  policy for construction-heavy sub-6-step Advanced templates).
- Paper-side observations from the original repo review (user aware):
  error-analysis "Annotators A/B/C" are LLM scripts while §5.4 says
  "human domain experts"; testset + generator gitignored (release gap);
  EngChain naming remnants.
