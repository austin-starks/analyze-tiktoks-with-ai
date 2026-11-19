#!/usr/bin/env python3
"""Step 0a: list every public video on a TikTok profile and save its metadata to data/posts.csv.

Uses yt-dlp (https://github.com/yt-dlp/yt-dlp), which reads TikTok's public pages. No account or key is needed.

  python3 src/collect.py --handle ilyas.abdulin
"""
import argparse
import csv
import json
import subprocess

from common import DATA

FIELDS = ["id", "url", "timestamp", "duration", "view_count", "like_count", "comment_count", "repost_count", "save_count", "description"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--handle", required=True, help="the profile handle without @")
    a = ap.parse_args()
    out = subprocess.run(["yt-dlp", "--dump-json", "--skip-download", "--ignore-errors", f"https://www.tiktok.com/@{a.handle}"],
                         capture_output=True, text=True).stdout
    rows = []
    for line in out.splitlines():
        v = json.loads(line)
        rows.append({k: v.get(k, "") for k in FIELDS if k not in ("url", "description")} |
                    {"url": v.get("webpage_url", ""), "description": v.get("description") or v.get("title", "")})
    rows.sort(key=lambda r: int(r["timestamp"] or 0))
    DATA.mkdir(exist_ok=True)
    with (DATA / "posts.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} public videos saved to data/posts.csv")


if __name__ == "__main__":
    main()
