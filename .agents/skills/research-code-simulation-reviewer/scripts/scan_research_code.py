#!/usr/bin/env python3
"""
Static triage scanner for research code repositories.
This is not a correctness proof. It flags reproducibility and scientific-review cues.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import re
from collections import defaultdict

CODE_EXTS = {'.py', '.m', '.mlx', '.ipynb', '.jl', '.r', '.R', '.yaml', '.yml', '.toml', '.json'}
PATTERNS = {
    'hardcoded_paths': re.compile(r'(/Users/|/home/|C:\\\\|D:\\\\|~/|\\\\\\\\[^\\s]+\\\\)', re.I),
    'randomness': re.compile(r'\b(seed|rng|random|randn?|np\.random|torch\.manual_seed|default_rng)\b', re.I),
    'units_power': re.compile(r'\b(baseMVA|MVA|MVar|MW|kV|pu|p\.u\.|Hz|per[- ]unit)\b', re.I),
    'solver_settings': re.compile(r'\b(tol|tolerance|max_iter|maxiter|solver|converge|convergence|epsilon|threshold)\b', re.I),
    'time_sampling': re.compile(r'\b(dt|timestep|time step|sample|sampling|scan time|latency|delay|rate)\b', re.I),
    'todo_or_fixme': re.compile(r'\b(TODO|FIXME|HACK|XXX)\b', re.I),
    'silent_failure': re.compile(r'\b(pass\s*$|except\s*:\s*$|catch\s+ME)\b', re.I | re.M),
}

def iter_files(root: Path):
    for p in root.rglob('*'):
        if p.is_file() and p.suffix in CODE_EXTS and '.git' not in p.parts:
            yield p

def safe_read(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return ''

def main() -> int:
    parser = argparse.ArgumentParser(description='Static triage scan for research code reproducibility cues.')
    parser.add_argument('path', nargs='?', default='.', help='Repository or directory path')
    args = parser.parse_args()
    root = Path(args.path).resolve()
    if not root.exists():
        raise SystemExit(f'Path does not exist: {root}')

    files = list(iter_files(root))
    hits = defaultdict(list)
    for f in files:
        text = safe_read(f)
        rel = f.relative_to(root)
        for name, pat in PATTERNS.items():
            if pat.search(text):
                hits[name].append(str(rel))

    print('# Research Code Static Triage Report')
    print()
    print(f'- Root: `{root}`')
    print(f'- Files scanned: {len(files)}')
    print()
    for name in PATTERNS:
        vals = hits.get(name, [])
        print(f'## {name}')
        if vals:
            for v in vals[:30]:
                print(f'- {v}')
            if len(vals) > 30:
                print(f'- ... {len(vals) - 30} more')
        else:
            print('- No direct hits found.')
        print()
    print('## Reviewer reminder')
    print('- This scan only flags cues. Manually verify units, assumptions, solver settings, data provenance, and validation tests.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
