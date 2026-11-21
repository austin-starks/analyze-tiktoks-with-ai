#!/usr/bin/env python3
"""Step 2: when fewer than 4 of the 5 voters agree, the adjudicator makes the final call.

It reads the same caption and transcript plus all five answers (category, close second, claim, reason) and decides
from the transcript and the rules in prompts/adjudicator.md, not by counting votes.
Writes results/adjudicator/<video id>.json.

  python3 src/adjudicate.py
"""
import json
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

import argparse

from common import CONFIG, add_run_arg, ask, client, posts, prompt, results_dir, second_choice, transcript_input


def voter_answers(R, vid):
    out = []
    for n, voter in enumerate(CONFIG["voters"], 1):
        lab = json.loads((R / "voters" / voter / f"{vid}.json").read_text())["label"]
        out.append({"reviewer": n, "category": lab["category"], "close_second": second_choice(lab) or "none",
                    "claim_answered": lab.get("claim_answered", ""), "reason": lab.get("reason", "")})
    return out


def disputed(R, vid):
    answers = voter_answers(R, vid)
    return Counter(x["category"] for x in answers).most_common(1)[0][1] < CONFIG["agreement_needed"], answers


def main():
    ap = argparse.ArgumentParser()
    add_run_arg(ap)
    a = ap.parse_args()
    R = results_dir(a.run)
    videos = posts()
    system = prompt("adjudicator.md", a.run)
    llm = client()
    todo = [(vid, ans) for vid in sorted(videos) for is_disputed, ans in [disputed(R, vid)] if is_disputed]

    def one(job):
        vid, answers = job
        out = R / "adjudicator" / f"{vid}.json"
        if out.exists():
            return
        user = {"video": transcript_input(vid, videos[vid]["description"]), "reviewers": answers}
        label, served, usage = ask(llm, CONFIG["adjudicator"], system, user)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps({"id": vid, "model": CONFIG["adjudicator"], "served_by": served, "label": label,
                                   "reviewers": answers, "usage": usage}, ensure_ascii=False, indent=1))

    with ThreadPoolExecutor(8) as pool:
        list(pool.map(one, todo))
    print(f"adjudicated {len(todo)} of {len(videos)} videos")


if __name__ == "__main__":
    main()
