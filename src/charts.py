#!/usr/bin/env python3
"""Draw the README charts from results/labels.csv and results/summary-since-2026-04-01.json into assets/.

  python3 src/charts.py
"""
import csv
import json
from datetime import date

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from common import CATEGORIES, RESULTS, ROOT  # noqa: E402

INK, PAPER, MUTED = "#1b2923", "#f6f3e8", "#8a948e"
COLOR = {"men": "#bd3b2f", "women": "#24704c", "mixed": "#c9a85a", "debate": "#c9a85a", "news": "#68736d", "politics": "#68736d", "misc": "#a9b0ab"}
NAME = {"men": "Defending men", "women": "Defending women", "mixed": "Mixed", "debate": "Debates",
        "news": "News", "politics": "Politics", "misc": "Miscellaneous"}
ASSETS = ROOT / "assets"


def style(ax, title, sub):
    ax.set_facecolor(PAPER)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(colors=INK, labelsize=11)
    ax.set_title(title, loc="left", fontsize=17, fontweight="bold", color=INK, pad=26)
    ax.text(0, 1.02, sub, transform=ax.transAxes, fontsize=11, color=MUTED)


def bars(summary, key, fmt, title, sub, name):
    data = summary["one_label"]
    order = sorted(CATEGORIES, key=lambda c: data[c][key])
    fig, ax = plt.subplots(figsize=(10, 5.2), facecolor=PAPER)
    vals = [data[c][key] for c in order]
    ax.barh([NAME[c] for c in order], vals, color=[COLOR[c] for c in order], height=.62)
    for i, (c, v) in enumerate(zip(order, vals)):
        ax.text(v + max(vals) * .01, i, fmt(v, data[c]), va="center", fontsize=11, color=INK, fontweight="bold" if c == "women" else None)
    ax.set_xlim(0, max(vals) * 1.18)
    ax.set_xticks([])
    style(ax, title, sub)
    fig.tight_layout()
    fig.savefig(ASSETS / name, dpi=160, facecolor=PAPER)


def timeline(rows):
    fig, ax = plt.subplots(figsize=(10, 4.2), facecolor=PAPER)
    xs = [date.fromisoformat(r["date"]) for r in rows]
    ys = [int(r["views"]) / 1e6 for r in rows]
    ax.bar(xs, ys, width=1.4, color=[COLOR["men"] if x >= date(2026, 4, 1) else MUTED for x in xs])
    ax.axvline(date(2026, 4, 1), color=INK, ls="--", lw=1.4)
    ax.text(date(2026, 4, 1), max(ys) * .95, "  April 1, 2026: views take off", color=INK, fontsize=11)
    ax.set_ylabel("views (millions)", color=INK)
    style(ax, "Views per video, in upload order", f"{len(rows)} public videos")
    fig.tight_layout()
    fig.savefig(ASSETS / "timeline.png", dpi=160, facecolor=PAPER)


def main():
    ASSETS.mkdir(exist_ok=True)
    summary = json.loads((RESULTS / "summary-since-2026-04-01.json").read_text())
    rows = list(csv.DictReader((RESULTS / "labels.csv").open(encoding="utf-8")))
    n = summary["videos"]
    bars(summary, "videos", lambda v, d: f"{v}  ({d['share']}%)", "What he posts: videos per category",
         f"Since April 1, 2026 · {n} videos · one label per video", "categories.png")
    bars(summary, "view_share", lambda v, d: f"{v}%", "What gets watched: share of all views",
         f"Since April 1, 2026 · {summary['views'] / 1e6:.0f}M views", "views.png")
    timeline(rows)
    print("charts written to assets/")


if __name__ == "__main__":
    main()
