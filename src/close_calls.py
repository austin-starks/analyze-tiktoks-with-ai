#!/usr/bin/env python3
"""The videos where the models disagree about whether it is defending women: watch them and decide for yourself.

A video is a close call when at least 2 of the 5 voters list "women" as a first or close-second choice, but fewer than
4 give it as their first choice. Writes results/close-calls.csv with the link, the claim, every vote, the final label,
the referee's reason, and where to watch: the median of the five voters' timestamps (0 when none gave one).

  python3 src/close_calls.py
"""
import csv
import json

from common import CONFIG, RESULTS, posts


def main():
    p = posts()
    voters = list(CONFIG["voters"])
    out = []
    for r in csv.DictReader((RESULTS / "labels.csv").open(encoding="utf-8")):
        listed = sum("women" in (r[f"{v}_first"], r[f"{v}_second"]) for v in voters)
        first = sum(r[f"{v}_first"] == "women" for v in voters)
        if listed < 2 or first >= 4:
            continue
        answers = [json.loads((RESULTS / "voters" / v / f"{r['id']}.json").read_text())["label"] for v in voters]
        adj = RESULTS / "adjudicator" / f"{r['id']}.json"
        lab = json.loads(adj.read_text())["label"] if adj.exists() else answers[-1]
        # Where to watch: the median of the five voters' timestamps, ignoring 0 (a model's "no single moment").
        seconds = sorted(a["evidence_seconds"] for a in answers if a.get("evidence_seconds"))
        watch_at = seconds[len(seconds) // 2] if seconds else 0
        out.append({"id": r["id"], "date": r["date"], "views": r["views"], "title": p[r["id"]]["description"][:120].replace("\n", " "),
                    "url": r["url"], "watch_at_seconds": watch_at, "claim": lab.get("claim_answered", ""),
                    "final": r["final"], "voters_listing_women": f"{listed} of 5", "voters_first_choice_women": f"{first} of 5",
                    **{v: r[f"{v}_first"] + (f" / {r[f'{v}_second']}" if r[f"{v}_second"] else "") for v in voters},
                    "referee_reason": r["adjudicator_reason"]})
    out.sort(key=lambda x: x["date"])
    with (RESULTS / "close-calls.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    print(f"{len(out)} close calls on defending women -> results/close-calls.csv")


if __name__ == "__main__":
    main()
