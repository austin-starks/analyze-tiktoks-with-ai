#!/usr/bin/env python3
"""How often the labels match Ilyas's OWN labels for his latest 60 videos (data/his-labels.json).

His 60 were split 30/30 before any model ran (data/split.json). The prompts were tuned on `tune` only and frozen;
`holdout` was scored once afterwards. Prints each voter, the plurality of the 5, and the final label.

  python3 src/score.py --set holdout
"""
import argparse
import csv
import json
from collections import Counter

from common import CONFIG, DATA, RESULTS


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", choices=["tune", "holdout", "all"], default="holdout")
    a = ap.parse_args()
    his = {r["id"]: r["his"] for r in json.loads((DATA / "his-labels.json").read_text())}
    split = json.loads((DATA / "split.json").read_text())
    ids = split["tune"] + split["holdout"] if a.set == "all" else split[a.set]
    rows = {r["id"]: r for r in csv.DictReader((RESULTS / "labels.csv").open(encoding="utf-8"))}
    score = Counter()
    for vid in ids:
        r, truth = rows[vid], his[vid]
        for v in CONFIG["voters"]:
            score[v] += r[f"{v}_first"] == truth
        ranked = Counter(r[f"{v}_first"] for v in CONFIG["voters"]).most_common()
        plurality = ranked[0][0] if len(ranked) == 1 or ranked[0][1] > ranked[1][1] else "tie"
        score["plurality of 5"] += plurality == truth
        score["final label"] += r["final"] == truth
    print(f"Agreement with his own labels, {a.set} ({len(ids)} videos):")
    for k, v in score.most_common():
        print(f"  {k:22} {v:>3}/{len(ids)}  {100 * v / len(ids):.0f}%")


if __name__ == "__main__":
    main()
