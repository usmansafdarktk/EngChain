"""
EngTrace pilot — automated template verification harness.

Implements checks H1-H7 of docs/pilot_template_authoring_spec.md (section 6).
Runs BEFORE every review cycle; a template that fails any check is returned
to the Author without reviewer involvement.

Usage:
    python pilot/harness/check_template.py <template_file.py> [--function NAME] [--seeds N] [--json OUT.json]

Exit code 0 iff every discovered (or named) template function passes all checks.
"""

import argparse
import importlib.util
import inspect
import json
import random
import re
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

DEFAULT_SEEDS = 25
MAX_SECONDS_PER_INSTANCE = 5.0
MIN_DISTINCT = 10          # H6: distinct answers / questions across seeds
MIN_STEPS = 3              # H4: minimum parsed steps
REL_TOL = 1e-6             # H4: answer-line vs parsed-final agreement
FLOAT_ARTIFACT_RE = re.compile(r"\d\.\d{7,}")          # H5: long decimal tails
STEP_MARKER_RE = re.compile(r"^\s*\*\*Step\s*\d+\s*:?\*\*", re.IGNORECASE | re.MULTILINE)
ANSWER_LINE_RE = re.compile(r"^\s*\*\*Answer:\*\*", re.IGNORECASE | re.MULTILINE)
NUMBER_RE = re.compile(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?")


def _load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_parser():
    parser_path = REPO_ROOT / "evaluation" / "engineering_parser.py"
    spec = importlib.util.spec_from_file_location("engineering_parser", parser_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_function(func, parser, n_seeds: int) -> dict:
    """Run H1-H7 for one template function. Returns a result dict."""
    checks = {}
    instances = {}

    # ---- H1: execution across seeds, with timing --------------------------
    h1_failures = []
    for seed in range(1, n_seeds + 1):
        random.seed(seed)
        t0 = time.monotonic()
        try:
            q, s = func()
            elapsed = time.monotonic() - t0
            if not isinstance(q, str) or not isinstance(s, str):
                h1_failures.append(f"seed {seed}: return is not (str, str)")
                continue
            if elapsed > MAX_SECONDS_PER_INSTANCE:
                h1_failures.append(f"seed {seed}: took {elapsed:.1f}s > {MAX_SECONDS_PER_INSTANCE}s")
            instances[seed] = (q, s)
        except AssertionError as e:
            h1_failures.append(f"seed {seed}: bounds assertion fired: {e}")
        except Exception as e:
            h1_failures.append(f"seed {seed}: {type(e).__name__}: {e}")
    checks["H1_execution"] = {"passed": not h1_failures, "detail": h1_failures[:10]}

    # ---- H2: determinism ---------------------------------------------------
    h2_failures = []
    for seed in (1, max(1, n_seeds // 2), n_seeds):
        if seed not in instances:
            continue
        random.seed(seed)
        try:
            again = func()
        except Exception as e:
            h2_failures.append(f"seed {seed}: re-run raised {type(e).__name__}")
            continue
        if again != instances[seed]:
            h2_failures.append(f"seed {seed}: output not byte-identical on re-run")
    checks["H2_determinism"] = {"passed": not h2_failures, "detail": h2_failures}

    # ---- H3: format --------------------------------------------------------
    h3_failures = []
    for seed, (q, s) in instances.items():
        n_steps = len(STEP_MARKER_RE.findall(s))
        n_answers = len(ANSWER_LINE_RE.findall(s))
        if n_steps < MIN_STEPS:
            h3_failures.append(f"seed {seed}: only {n_steps} '**Step X:**' markers (< {MIN_STEPS})")
        if n_answers != 1:
            h3_failures.append(f"seed {seed}: {n_answers} '**Answer:**' lines (must be exactly 1)")
    checks["H3_format"] = {"passed": not h3_failures, "detail": h3_failures[:10]}

    # ---- H4: parser round-trip --------------------------------------------
    h4_failures = []
    for seed, (q, s) in instances.items():
        steps, step_vals, final = parser.extract_steps(s)
        if len(steps) < MIN_STEPS:
            h4_failures.append(f"seed {seed}: parser extracted {len(steps)} steps (< {MIN_STEPS})")
        if final is None:
            h4_failures.append(f"seed {seed}: parser found no final answer")
            continue
        # The number in the **Answer:** line must equal the parsed final value.
        m = ANSWER_LINE_RE.search(s)
        if m:
            tail = s[m.end():].splitlines()[0] if s[m.end():] else ""
            nums = NUMBER_RE.findall(tail.replace(",", ""))
            if nums:
                declared = float(nums[0])
                denom = abs(declared) if abs(declared) > 1e-12 else 1.0
                if abs(declared - final) / denom > REL_TOL:
                    h4_failures.append(
                        f"seed {seed}: answer-line value {declared} != parsed final {final}")
            else:
                h4_failures.append(f"seed {seed}: no numeric value on the '**Answer:**' line")
        if not any(v is not None for v in step_vals[:-1]):
            h4_failures.append(f"seed {seed}: no intermediate step carries an extractable value")
    checks["H4_parser_roundtrip"] = {"passed": not h4_failures, "detail": h4_failures[:10]}

    # ---- H5: numeric hygiene ----------------------------------------------
    h5_failures = []
    for seed, (q, s) in instances.items():
        blob = q + "\n" + s
        if re.search(r"\b(nan|inf)\b", blob, re.IGNORECASE):
            h5_failures.append(f"seed {seed}: NaN/Inf appears in output")
        artifact = FLOAT_ARTIFACT_RE.search(blob)
        if artifact:
            h5_failures.append(f"seed {seed}: float artifact '{artifact.group(0)[:24]}'")
    checks["H5_numeric_hygiene"] = {"passed": not h5_failures, "detail": h5_failures[:10]}

    # ---- H6: instance diversity -------------------------------------------
    finals, questions = set(), set()
    for seed, (q, s) in instances.items():
        questions.add(q)
        _, _, final = parser.extract_steps(s)
        if final is not None:
            finals.add(round(final, 10))
    h6_ok = len(finals) >= MIN_DISTINCT and len(questions) >= MIN_DISTINCT
    checks["H6_diversity"] = {
        "passed": h6_ok,
        "detail": [] if h6_ok else [
            f"{len(finals)} distinct final answers, {len(questions)} distinct questions "
            f"across {len(instances)} seeds (need >= {MIN_DISTINCT} of each)"],
    }

    # ---- H7: declared bounds + assertions ---------------------------------
    h7_failures = []
    source = inspect.getsource(func)
    doc = inspect.getdoc(func) or ""
    if "Physical bounds" not in doc:
        h7_failures.append("docstring missing a 'Physical bounds:' declaration")
    if not re.search(r"^\s*assert\b", source, re.MULTILINE):
        h7_failures.append("function contains no bounds assertions")
    # (assertion firing is caught in H1)
    checks["H7_bounds"] = {"passed": not h7_failures, "detail": h7_failures}

    return {
        "function": func.__name__,
        "seeds_run": len(instances),
        "passed": all(c["passed"] for c in checks.values()),
        "checks": checks,
    }


def main():
    ap = argparse.ArgumentParser(description="EngTrace pilot template harness (H1-H7)")
    ap.add_argument("template_file", type=Path)
    ap.add_argument("--function", help="check only this template function")
    ap.add_argument("--seeds", type=int, default=DEFAULT_SEEDS)
    ap.add_argument("--json", type=Path, help="also write the report to this path")
    args = ap.parse_args()

    module = _load_module(args.template_file.resolve())
    parser = _load_parser()

    funcs = [
        obj for name, obj in inspect.getmembers(module, inspect.isfunction)
        if name.startswith("template_") and obj.__module__ == module.__name__
    ]
    if args.function:
        funcs = [f for f in funcs if f.__name__ == args.function]
    if not funcs:
        print(f"No template_* functions found in {args.template_file}", file=sys.stderr)
        sys.exit(2)

    report = {
        "file": str(args.template_file),
        "seeds": args.seeds,
        "results": [check_function(f, parser, args.seeds) for f in funcs],
    }
    report["all_passed"] = all(r["passed"] for r in report["results"])

    print(json.dumps(report, indent=2))
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, indent=2), encoding="utf-8")

    sys.exit(0 if report["all_passed"] else 1)


if __name__ == "__main__":
    main()
