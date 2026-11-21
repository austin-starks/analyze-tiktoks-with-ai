#!/usr/bin/env python3
"""Every video whose final label differs between the published run and another run, with all the votes behind both.

Writes results/runs/<run>/changes.csv.

  python3 src/changes.py --run fair
"""
import argparse
import csv

from common import CONFIG, RESULTS, posts, results_dir


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="the run to compare with the published labels")
    a = ap.parse_args()
    R = results_dir(a.run)
    old = {r["id"]: r for r in csv.DictReader((RESULTS / "labels.csv").open(encoding="utf-8"))}
    new = {r["id"]: r for r in csv.DictReader((R / "labels.csv").open(encoding="utf-8"))}
    p = posts()
    voters = list(CONFIG["voters"])
    vote = lambda r, v: r[f"{v}_first"] + (f" / {r[f'{v}_second']}" if r[f"{v}_second"] else "")
    rows = []
    for vid in sorted(old, key=lambda i: (old[i]["date"], i)):
        o, n = old[vid], new[vid]
        if o["final"] == n["final"]:
            continue
        rows.append({"id": vid, "date": o["date"], "views": o["views"], "title": p[vid]["description"][:120].replace("\n", " "), "url": o["url"],
                     "published": o["final"], a.run: n["final"], f"{a.run}_decided_by": n["decided_by"],
                     **{f"published_{v}": vote(o, v) for v in voters}, **{f"{a.run}_{v}": vote(n, v) for v in voters},
                     "published_referee_reason": o["adjudicator_reason"], f"{a.run}_referee_reason": n["adjudicator_reason"]})
    with (R / "changes.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} of {len(old)} videos changed -> {R / 'changes.csv'}")


if __name__ == "__main__":
    main()
