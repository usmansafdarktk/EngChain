# Author — Stage C authoring procedure (v1)

The Author (main-loop agent) writes one template at a time, following
docs/pilot_template_authoring_spec.md §3 (template contract) exactly.

Per template:
1. Re-read `pilot/branches/civil_engineering/AUTHOR_NOTES.md` (compounded
   reviewer feedback) before writing.
2. Ground the problem typology in the assigned book chapter (BOOKS.md area
   map); record book + section in the docstring `Grounding:` field. Never
   copy a worked example's wording or numbers.
3. Sample parameters only from `constants.py` entries and physically
   constrained ranges; encode the physics as constraints and `assert`s.
4. **Round-then-recompute rule:** every value shown in the question is
   rounded for presentation FIRST, and the entire gold trace is recomputed
   from those presented values — never from the unrounded internals — so a
   solver using the question's numbers reproduces the gold chain exactly.
5. Single final numeric answer (`**Answer:**` line); intermediate steps each
   carry their computed value; all displayed floats use fixed-format
   f-strings.
6. Run the harness (`pilot/harness/check_template.py`) and fix all failures
   BEFORE requesting review.
7. After each review cycle: apply the arbiter's consolidated defect list,
   append lessons to AUTHOR_NOTES.md, re-run the harness, resubmit.
