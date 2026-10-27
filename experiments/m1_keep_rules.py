"""M1: which keep rule recovers what a curator judged worth loading? Pre-registration: M1-boot-keep-rules.md.

Reads a markdown memory library that is a git repository; prints aggregate numbers only (no file names).
Usage: python m1_keep_rules.py <memory_dir> [K]
"""
import os
import re
import subprocess
import sys
from collections import defaultdict

import numpy as np

MEM = sys.argv[1]
K = int(sys.argv[2]) if len(sys.argv) > 2 else 40
rng = np.random.default_rng(20261027)

PREFIX = {"P": "primitive_", "F": "feedback_", "J": "project_", "U": "user_", "R": "reference_", "O": "protocol_", "M": ""}
MD_LINK = re.compile(r"\]\(([A-Za-z0-9_\-\.]+?)(?:\.md)?\)")
WIKI = re.compile(r"\[\[([^\]\|#]+)(?:[#\|][^\]]*)?\]\]")
TAG = re.compile(r"\[([PFJUROM])·([a-z0-9][a-z0-9\-]*)\]")


def universe():
    out = {}
    for f in os.listdir(MEM):
        if f.endswith(".md") and not f.startswith("_") and f != "MEMORY.md" and not f.startswith("MEMORY_"):
            out[f[:-3]] = os.path.join(MEM, f)
    return out


U = universe()
names = sorted(U)


def resolve(slug):
    slug = slug.strip()
    if slug.endswith(".md"):
        slug = slug[:-3]
    if slug in U:
        return slug
    for p in ("primitive_", "feedback_", "project_", "user_", "reference_", "protocol_"):
        if p + slug in U:
            return p + slug
    return None


def links(text):
    found = set()
    for m in MD_LINK.findall(text):
        r = resolve(m)
        if r:
            found.add(r)
    for m in WIKI.findall(text):
        r = resolve(m)
        if r:
            found.add(r)
    for pre, slug in TAG.findall(text):
        r = resolve(PREFIX[pre] + slug) or resolve(slug)
        if r:
            found.add(r)
    return found


target = links(open(os.path.join(MEM, "MEMORY.md"), encoding="utf-8", errors="ignore").read())

out_edges = {n: links(open(U[n], encoding="utf-8", errors="ignore").read()) - {n} for n in names}
inbound = defaultdict(int)
for src, dsts in out_edges.items():
    for d in dsts:
        inbound[d] += 1

# PageRank: conserved credit, each file splits one unit among its outlinks; dangling mass spread uniformly
idx = {n: i for i, n in enumerate(names)}
N = len(names)
pr = np.full(N, 1.0 / N)
for _ in range(60):
    new = np.full(N, 0.15 / N)
    dangling = 0.0
    for n, dsts in out_edges.items():
        if dsts:
            share = 0.85 * pr[idx[n]] / len(dsts)
            for d in dsts:
                new[idx[d]] += share
        else:
            dangling += pr[idx[n]]
    new += 0.85 * dangling / N
    pr = new

# git dates: first and last commit time per top-level file
log = subprocess.run(["git", "-C", MEM, "log", "--format=@%ct", "--name-only", "--", "*.md"],
                     capture_output=True, text=True, encoding="utf-8", errors="ignore").stdout
first, last = {}, {}
t = None
for line in log.splitlines():
    if line.startswith("@"):
        t = int(line[1:])
    elif line.strip():
        f = os.path.basename(line.strip())
        if f.endswith(".md") and f[:-3] in U and "/" not in line.strip():
            n = f[:-3]
            last[n] = max(last.get(n, t), t)
            first[n] = min(first.get(n, t), t)
size = {n: os.path.getsize(U[n]) for n in names}
fallback = 0  # files with no git history rank as oldest / least recent
feat = {
    "size (smallest first)": {n: -size[n] for n in names},
    "age, newest first": {n: first.get(n, fallback) for n in names},
    "age, oldest first": {n: -first.get(n, 10**12) for n in names},
    "last touch (X2)": {n: last.get(n, fallback) for n in names},
    "inbound links (free credit)": {n: inbound[n] for n in names},
    "PageRank (conserved credit)": {n: pr[idx[n]] for n in names},
}


def expected_hits(score, reps=200):
    """Top-K hits with ties broken uniformly at random, averaged over `reps` tie orders."""
    vals = np.array([score[n] for n in names], dtype=float)
    tgt = np.array([n in target for n in names])
    tot = 0.0
    for _ in range(reps):
        jitter = rng.random(N)
        order = np.lexsort((jitter, -vals))
        tot += tgt[order[:K]].sum()
    return tot / reps


rand = np.array([np.isin(rng.choice(N, K, replace=False), np.where([n in target for n in names])[0]).sum()
                 for _ in range(1000)])
print(f"universe {N} files; target (linked from MEMORY.md) {len(target)}; K = {K}")
print(f"files with git history {len(last)}; distinct last-commit times {len(set(last.values()))}; "
      f"distinct first-commit times {len(set(first.values()))}")
print(f"random: mean {rand.mean():.2f}, 95% band [{np.percentile(rand, 2.5):.0f}, {np.percentile(rand, 97.5):.0f}]")
res = {}
for name, sc in feat.items():
    res[name] = expected_hits(sc)
    print(f"{name:32s} {res[name]:6.2f} of {K}")
a = res["last touch (X2)"] - max(res["age, newest first"], res["age, oldest first"])
b = res["PageRank (conserved credit)"] - res["inbound links (free credit)"]
c_band = res["size (smallest first)"] <= np.percentile(rand, 97.5)
c_below = all(res["size (smallest first)"] <= res[r] - 2 for r in
              ("last touch (X2)", "inbound links (free credit)", "PageRank (conserved credit)"))
print(f"M1-a last touch minus best age rule: {a:+.2f} -> {'HIT' if a >= 2 else 'MISS'}")
print(f"M1-b PageRank minus inbound: {b:+.2f} -> {'HIT' if b >= 2 else 'MISS'}")
print(f"M1-c size within random band: {c_band}; at least 2 below each relational/use rule: {c_below} -> "
      f"{'HIT' if c_band and c_below else 'MISS'}")
