#!/usr/bin/env python3
"""Step 4: how many videos, and how many views, fall in each category.

Counts one label per video (results/labels.csv `final`), the way his own chart counts. As a check it also counts
multi-label: a video counts in every category that at least 3 of the 5 voters list as a first or close-second choice.
Prints the table and writes results/summary.json.

  python3 src/count.py                    # since April 1, 2026 (when his views took off)
  python3 src/count.py --since 2025-01-01 # his whole channel
"""
import argparse
import csv
import json

from common import CATEGORIES, CONFIG, add_run_arg, results_dir

MILLION = 1_000_000


def table(rows, has):
    total, views = len(rows), sum(int(r["views"]) for r in rows)
    out = {}
    for c in CATEGORIES:
        hit = [r for r in rows if has(r, c)]
        out[c] = {"videos": len(hit), "share": round(100 * len(hit) / total, 1),
                  "views": sum(int(r["views"]) for r in hit), "view_share": round(100 * sum(int(r["views"]) for r in hit) / views, 1),
                  "million_view_videos": sum(int(r["views"]) >= MILLION for r in hit)}
    for c in CATEGORIES:
        out[c]["rank"] = 1 + sum(out[o]["videos"] > out[c]["videos"] for o in CATEGORIES)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="2026-04-01")
    add_run_arg(ap)
    a = ap.parse_args()
    R = results_dir(a.run)
    rows = [r for r in csv.DictReader((R / "labels.csv").open(encoding="utf-8")) if r["date"] >= a.since]
    voters = list(CONFIG["voters"])
    one = table(rows, lambda r, c: r["final"] == c)
    multi = table(rows, lambda r, c: sum(c in (r[f"{v}_first"], r[f"{v}_second"]) for v in voters) >= 3)
    summary = {"since": a.since, "videos": len(rows), "views": sum(int(r["views"]) for r in rows),
               "million_view_videos": sum(int(r["views"]) >= MILLION for r in rows), "one_label": one, "multi_label_check": multi}
    (R / f"summary-since-{a.since}.json").write_text(json.dumps(summary, indent=1))
    print(f"Since {a.since}: {len(rows)} videos, {summary['views'] / 1e6:.1f}M views, {summary['million_view_videos']} with 1M+")
    print(f"{'category':10}{'videos':>8}{'share':>8}{'views':>9}{'of views':>10}{'1M+':>6}{'rank':>6}   multi-label videos / rank")
    for c in sorted(CATEGORIES, key=lambda c: one[c]["rank"]):
        o, m = one[c], multi[c]
        print(f"{c:10}{o['videos']:>8}{o['share']:>7}%{o['views'] / 1e6:>8.1f}M{o['view_share']:>9}%{o['million_view_videos']:>6}{o['rank']:>6}"
              f"   {m['videos']:>4} / {m['rank']}")


if __name__ == "__main__":
    main()
