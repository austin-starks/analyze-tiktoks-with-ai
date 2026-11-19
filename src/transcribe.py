#!/usr/bin/env python3
"""Step 0b: transcribe every video's audio with Whisper and save data/transcripts/<id>.json.

Downloads only the audio (yt-dlp), sends it to an OpenAI-compatible transcription endpoint and keeps the
timestamped segments, so each label can point at the second where the claim is made.
  TRANSCRIBE_BASE_URL  default https://api.openai.com/v1
  TRANSCRIBE_API_KEY   your OpenAI key (OpenRouter has no audio endpoint)
A transcript already on disk is skipped.

  python3 src/transcribe.py
"""
import csv
import json
import os
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from common import DATA


def main():
    from openai import OpenAI
    llm = OpenAI(base_url=os.environ.get("TRANSCRIBE_BASE_URL", "https://api.openai.com/v1"), api_key=os.environ["TRANSCRIBE_API_KEY"])
    rows = list(csv.DictReader((DATA / "posts.csv").open(encoding="utf-8")))
    (DATA / "transcripts").mkdir(parents=True, exist_ok=True)

    def one(r):
        out = DATA / "transcripts" / f"{r['id']}.json"
        if out.exists():
            return
        with tempfile.TemporaryDirectory() as tmp:
            audio = Path(tmp) / "audio.m4a"
            subprocess.run(["yt-dlp", "-q", "-f", "bestaudio/best", "-x", "--audio-format", "m4a", "-o", str(audio), r["url"]], check=True)
            with audio.open("rb") as fh:
                t = llm.audio.transcriptions.create(model="whisper-1", file=fh, response_format="verbose_json",
                                                   timestamp_granularities=["segment"])
        segments = [{"start": s.start, "end": s.end, "text": s.text} for s in (t.segments or [])]
        out.write_text(json.dumps({"text": t.text, "duration": t.duration, "segments": segments}, ensure_ascii=False))

    with ThreadPoolExecutor(6) as pool:
        list(pool.map(one, rows))
    print(f"{len(list((DATA / 'transcripts').glob('*.json')))} transcripts in data/transcripts")


if __name__ == "__main__":
    main()
