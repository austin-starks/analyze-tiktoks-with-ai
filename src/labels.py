#!/usr/bin/env python3
"""Step 3: one final label per video, written to results/labels.csv.

Rule: if at least 4 of the 5 voters give the same first choice, that is the label. Otherwise the adjudicator's call is.
The file also keeps every voter's first and close-second choice, so any other rule can be recomputed from it.

  python3 src/labels.py
"""
import csv
import json
from collections import Counter
from datetime import datetime, timezone

from common import CONFIG, RESULTS, posts, second_choice


def main():
    rows = []
    for vid, p in posts().items():
        votes = {v: json.loads((RESULTS / "voters" / v / f"{vid}.json").read_text())["label"] for v in CONFIG["voters"]}
        top, n = Counter(l["category"] for l in votes.values()).most_common(1)[0]
        adj = RESULTS / "adjudicator" / f"{vid}.json"
        if n >= CONFIG["agreement_needed"]:
            final, source, adj_label = top, f"{n} of 5 voters", None
        else:
            adj_label = json.loads(adj.read_text())["label"]
            final, source = adj_label["category"], "adjudicator"
        row = {"id": vid, "date": datetime.fromtimestamp(int(p["timestamp"]), tz=timezone.utc).date().isoformat(),
               "views": p["view_count"], "final": final, "decided_by": source}
        for v, l in votes.items():
            row[f"{v}_first"], row[f"{v}_second"] = l["category"], second_choice(l)
        row["adjudicator"] = adj_label["category"] if adj_label else ""
        row["adjudicator_reason"] = adj_label["reason"] if adj_label else ""
        row["url"] = p["url"]
        rows.append(row)
    rows.sort(key=lambda r: (r["date"], r["id"]))
    with (RESULTS / "labels.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} videos;", dict(Counter(r["decided_by"] for r in rows)))


if __name__ == "__main__":
    main()
