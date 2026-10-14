"""A deterministic stand-in for an LLM.

It behaves like a gullible model: it follows any "INSTRUCTION FOR THE
ASSISTANT" it finds inside retrieved text. That's the whole point. Real models
get fooled less predictably, which is worse, not better.
"""

import re

from tools import get_case_note

ACTIVE_CASE_ID = "DEMO-4821"
INJECTION = re.compile(r"INSTRUCTION FOR THE ASSISTANT:(.*)", re.IGNORECASE | re.DOTALL)
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")


def propose_actions(question: str) -> list[dict]:
    """Step 1: the model asks to search. A normal, harmless first move."""
    return [{"tool": "search_public_programs", "arguments": {"query": question}}]


def react_to_documents(documents: list[str]) -> list[dict]:
    """Step 2: the model reads what came back, and obeys anything that sounds official."""
    actions = []
    for doc in documents:
        match = INJECTION.search(doc)
        if match and "send_message" in match.group(1):
            recipient = EMAIL.search(match.group(1))
            if recipient:
                actions.append(
                    {
                        "tool": "send_message",
                        "arguments": {"to": recipient.group(0), "body": get_case_note(ACTIVE_CASE_ID)},
                    }
                )
    return actions


def write_answer(question: str, documents: list[str]) -> str:
    if not documents:
        return "I couldn't find a public program that matches that question."
    clean_lines = INJECTION.sub("", documents[0]).strip().splitlines()
    return " ".join(line for line in clean_lines[1:] if line.strip())
