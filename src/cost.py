#!/usr/bin/env python3
"""What a run cost: every saved answer's token usage x the model's current OpenRouter price.

Prices are read from https://openrouter.ai/api/v1/models at the time you run this and saved with the date, so the
receipt says which prices it used. Writes results/cost.json (or results/runs/<run>/cost.json).

  python3 src/cost.py
  python3 src/cost.py --run fair
"""
import argparse
import json
import urllib.request
from datetime import date

from common import CONFIG, add_run_arg, results_dir


def main():
    ap = argparse.ArgumentParser()
    add_run_arg(ap)
    R = results_dir(ap.parse_args().run)
    with urllib.request.urlopen("https://openrouter.ai/api/v1/models", timeout=60) as r:
        price = {m["id"]: m["pricing"] for m in json.load(r)["data"]}
    rows = []
    for key, model in [*CONFIG["voters"].items(), ("referee", CONFIG["adjudicator"])]:
        files = sorted((R / "adjudicator").glob("*.json") if key == "referee" else (R / "voters" / key).glob("*.json"))
        tin = tout = 0
        for f in files:
            u = json.loads(f.read_text()).get("usage") or {}
            tin += u.get("prompt_tokens") or 0
            tout += u.get("completion_tokens") or 0
        pin, pout = float(price[model]["prompt"]) * 1e6, float(price[model]["completion"]) * 1e6
        rows.append({"role": key, "model": model, "calls": len(files), "input_tokens": tin, "output_tokens": tout,
                     "usd_per_million_input": pin, "usd_per_million_output": pout, "usd": round(tin * pin / 1e6 + tout * pout / 1e6, 2)})
    out = {"prices_from": "https://openrouter.ai/api/v1/models", "prices_date": date.today().isoformat(), "models": rows,
           "total_usd": round(sum(r["usd"] for r in rows), 2)}
    (R / "cost.json").write_text(json.dumps(out, indent=1))
    for r in rows:
        print(f"{r['role']:20} {r['calls']:4} calls  {r['input_tokens'] / 1e6:5.2f}M in x ${r['usd_per_million_input']:.3f}"
              f"  {r['output_tokens'] / 1e6:5.2f}M out x ${r['usd_per_million_output']:.3f}  = ${r['usd']:.2f}")
    print(f"total ${out['total_usd']:.2f} at {out['prices_date']} prices")


if __name__ == "__main__":
    main()
