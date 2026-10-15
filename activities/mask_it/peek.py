"""Run me: python peek.py   (shows what the model would see)."""

from pathlib import Path

import pipeline

for note in (Path(__file__).parent / "notes.txt").read_text().strip().splitlines():
    print("BEFORE:", note)
    try:
        print("MODEL SEES:", pipeline.ask_model(note), "\n")
    except NotImplementedError:
        print("MODEL SEES: (redact() isn't written yet, so this would go out as-is)\n")
