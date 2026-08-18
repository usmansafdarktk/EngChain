"""
Stage E — build the pilot mini-testset (5 instances per template) in the
exact schema of the real EngTrace testset, so run_inference.py and the
evaluation framework consume it unchanged.

Usage: python pilot/harness/build_mini_testset.py <branch_snake_case>
"""

import importlib.util
import inspect
import json
import random
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

SEEDS = [201, 202, 203, 204, 205]      # distinct from review seeds 101-105


def main(branch):
    tpl_root = REPO_ROOT / "pilot" / "templates" / "branches" / branch
    out_root = REPO_ROOT / "pilot" / "testset_preview" / branch
    out_root.mkdir(parents=True, exist_ok=True)

    total = 0
    # skip __pycache__ and any other private directory: without this the
    # builder emits an empty <dir>.jsonl alongside the real domains
    for domain_dir in sorted(p for p in tpl_root.iterdir()
                             if p.is_dir() and not p.name.startswith("_")):
        domain = domain_dir.name
        records = []
        for py in sorted(domain_dir.glob("*.py")):
            spec = importlib.util.spec_from_file_location(py.stem, py)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            funcs = [(n, o) for n, o in inspect.getmembers(mod, inspect.isfunction)
                     if n.startswith("template_") and o.__module__ == mod.__name__]
            for name, func in sorted(funcs):
                doc = inspect.getdoc(func) or ""
                m = re.search(r"Difficulty:\s*(\w+)", doc)
                level = m.group(1) if m else "Unknown"
                for seed in SEEDS:
                    random.seed(seed)
                    q, s = func()
                    records.append({
                        "id": f"{name}_{seed}",
                        "seed": seed,
                        "branch": branch,
                        "domain": domain,
                        "area": py.stem,
                        "level": level,
                        "question": q,
                        "solution": s,
                    })
        out = out_root / f"{domain}.jsonl"
        with out.open("w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec) + "\n")
        print(f"{domain}: {len(records)} records -> {out}")
        total += len(records)
    print(f"TOTAL: {total} records")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "civil_engineering")
