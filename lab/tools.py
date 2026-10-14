"""The rooms in the house. Every tool is fake: nothing leaves your laptop."""

import json
from pathlib import Path

FIXTURES = Path(__file__).parent / "fixtures"
CASE_NOTES = json.loads((FIXTURES / "case_notes.json").read_text())

OUTBOX: list[dict] = []


def load_documents(haunted: bool = False) -> dict[str, str]:
    docs = {p.name: p.read_text() for p in FIXTURES.glob("*.txt")}
    if haunted:
        docs.update({p.name: p.read_text() for p in (FIXTURES / "haunted").glob("*.txt")})
    return docs


def search_public_programs(query: str, haunted: bool = False) -> list[str]:
    """Tiny keyword retrieval: returns documents ranked by word overlap."""
    words = {w.strip("?.,!").lower() for w in query.split() if len(w) > 3}
    scored = []
    for text in load_documents(haunted).values():
        score = sum(1 for w in words if w in text.lower())
        if score:
            scored.append((score, text))
    return [text for _, text in sorted(scored, key=lambda pair: pair[0], reverse=True)]


def get_case_note(case_id: str) -> str:
    return CASE_NOTES[case_id]["note"]


def send_message(to: str, body: str) -> str:
    OUTBOX.append({"to": to, "body": body})
    return f"sent to {to}"


TOOLS = {
    "search_public_programs": search_public_programs,
    "send_message": send_message,
}
