#!/usr/bin/env python3
"""Every model's reasoning in one sheet: one row per video per model, plus the referee's call where there was one.

The answers live in one JSON file each under results/voters/ and results/adjudicator/. This flattens them so you can
filter by video and read why each model labeled it the way it did. Writes results/reasons.csv.

  python3 src/reasons.py
  python3 src/reasons.py --run fair       # results/runs/fair/reasons.csv
"""
import argparse
import csv
import json

from common import CONFIG, add_run_arg, posts, results_dir, second_choice


def main():
    ap = argparse.ArgumentParser()
    add_run_arg(ap)
    R = results_dir(ap.parse_args().run)
    p = posts()
    final = {r["id"]: r for r in csv.DictReader((R / "labels.csv").open(encoding="utf-8"))}
    rows = []
    for vid in sorted(final, key=lambda i: (final[i]["date"], i)):
        base = {"id": vid, "date": final[vid]["date"], "url": p[vid]["url"], "title": p[vid]["description"][:120].replace("\n", " "),
                "final": final[vid]["final"], "decided_by": final[vid]["decided_by"]}
        answers = [(v, json.loads((R / "voters" / v / f"{vid}.json").read_text())) for v in CONFIG["voters"]]
        adj = R / "adjudicator" / f"{vid}.json"
        if adj.exists():
            answers.append(("referee", json.loads(adj.read_text())))
        for who, a in answers:
            lab = a["label"]
            rows.append({**base, "model": who, "served_by": a.get("served_by", ""), "category": lab["category"],
                         "second_choice": second_choice(lab), "claim_answered": lab.get("claim_answered", ""),
                         "reason": lab.get("reason", ""), "evidence_seconds": lab.get("evidence_seconds", 0)})
    with (R / "reasons.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} answers for {len(final)} videos -> {R / 'reasons.csv'}")


if __name__ == "__main__":
    main()
