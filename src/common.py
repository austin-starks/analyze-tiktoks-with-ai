"""Shared paths, data loading and the one LLM call every script uses.

The call goes through the standard `openai` client, so it works with any OpenAI-compatible endpoint:
  LLM_BASE_URL   default https://openrouter.ai/api/v1
  LLM_API_KEY    your key for that endpoint
Every saved answer records the model that actually served it, read from the response.
"""
import csv
import json
import os
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA, PROMPTS, RESULTS = ROOT / "data", ROOT / "prompts", ROOT / "results"
CONFIG = json.loads((ROOT / "models.json").read_text())
CATEGORIES = ["men", "women", "mixed", "debate", "news", "politics", "misc"]
SCHEMA = json.loads((PROMPTS / "schema.json").read_text())


def posts():
    """Every public video: id, upload date (UTC), views, caption."""
    rows = {}
    for r in csv.DictReader((DATA / "posts.csv").open(encoding="utf-8")):
        rows[r["id"]] = r
    return rows


def transcript_input(video_id, caption):
    """The exact user message each model receives: caption plus a timestamped transcript."""
    t = json.loads((DATA / "transcripts" / f"{video_id}.json").read_text(encoding="utf-8"))
    lines = [f"[{int(s['start'])}s] {s['text'].strip()}" for s in t.get("segments", [])]
    return {"caption": caption or "none", "transcript": "\n".join(lines)}


def client():
    from openai import OpenAI
    return OpenAI(base_url=os.environ.get("LLM_BASE_URL", "https://openrouter.ai/api/v1"), api_key=os.environ["LLM_API_KEY"])


def ask(llm, model, system, user, retries=4):
    """One JSON answer that matches the label schema. Returns (label, served_model, usage)."""
    last = None
    for attempt in range(retries):
        try:
            r = llm.chat.completions.create(
                model=model, temperature=CONFIG["temperature"],
                messages=[{"role": "system", "content": system}, {"role": "user", "content": json.dumps(user, ensure_ascii=False)}],
                response_format={"type": "json_schema", "json_schema": {"name": "label", "strict": True, "schema": SCHEMA}})
            label = json.loads(r.choices[0].message.content)
            if label.get("category") not in CATEGORIES:
                raise ValueError(f"unknown category {label.get('category')!r}")
            return label, r.model, (r.usage.model_dump() if r.usage else None)
        except Exception as exc:  # retry transient provider errors, then give up on this video
            last = exc
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"{model}: {last}")


def second_choice(label):
    alt = label.get("alternate_category", "none")
    return alt if label.get("borderline") and alt not in ("none", label["category"]) else ""
