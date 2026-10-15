"""The two places a case note can leak: the model and the log.

Both are fake (plain Python lists), so nothing really leaves your laptop.
Every note goes through redact() first. That's the whole lesson: one
choke point in code, not a prompt that says "please don't repeat names".
"""

from redact import redact

MODEL_INBOX: list[str] = []
LOG: list[str] = []


def ask_model(note: str) -> str:
    safe = redact(note)
    MODEL_INBOX.append(safe)
    LOG.append(f"sent to model: {safe}")
    return safe
