#!/usr/bin/env python3
"""Step 1: five independent voters label every video with the same prompt (prompts/voter.md).

Writes results/voters/<voter>/<video id>.json. An answer already on disk is never requested again,
so the run can be stopped and resumed.

  python3 src/classify.py                 # every video
  python3 src/classify.py --set holdout   # only his 30 held-out labeled videos
"""
import argparse
import json
from concurrent.futures import ThreadPoolExecutor

from common import CONFIG, DATA, PROMPTS, RESULTS, ask, client, posts, transcript_input


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", choices=["all", "tune", "holdout"], default="all")
    ap.add_argument("--workers", type=int, default=8, help="calls in flight per model")
    a = ap.parse_args()
    videos = posts()
    split = json.loads((DATA / "split.json").read_text())
    ids = sorted(videos) if a.set == "all" else split[a.set]
    system = (PROMPTS / "voter.md").read_text()
    llm = client()

    def one(job):
        voter, model, vid = job
        out = RESULTS / "voters" / voter / f"{vid}.json"
        if out.exists():
            return
        label, served, usage = ask(llm, model, system, transcript_input(vid, videos[vid]["description"]))
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps({"id": vid, "voter": voter, "model": model, "served_by": served, "label": label, "usage": usage},
                                  ensure_ascii=False, indent=1))

    # One pool per model, all at once: every model works in parallel, each with --workers calls in flight.
    pools = {v: ThreadPoolExecutor(a.workers) for v in CONFIG["voters"]}
    futures = [pools[v].submit(one, (v, m, i)) for i in ids for v, m in CONFIG["voters"].items()]
    for n, f in enumerate(futures, 1):
        f.result()
        if n % 250 == 0:
            print(f"{n}/{len(futures)}", flush=True)
    for pool in pools.values():
        pool.shutdown()
    print(f"done: {len(futures)} answers")


if __name__ == "__main__":
    main()
