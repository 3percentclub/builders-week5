"""The Door With No Lock.

A model proposes tool calls as JSON. This file decides what actually runs.
Everything is fake: the outbox is a list and the "database" is a dict.
"""

OUTBOX: list[dict] = []
DATABASE: dict[str, list[str]] = {"clients": ["Jordan Example", "Sam Placeholder"], "volunteers": ["Riley Demo"]}


def send_email(to: str, body: str) -> str:
    OUTBOX.append({"to": to, "body": body})
    return f"queued email to {to}"


def delete_records(table: str) -> str:
    DATABASE.pop(table, None)
    return f"deleted every row in {table}"


tools = {"send_email": send_email, "delete_records": delete_records}


def execute_tool(name, args):
    """As shipped: runs whatever the model asks for, with whatever arguments."""
    return tools[name](**args)


# ---------------------------------------------------------------------------
# YOUR JOB: install three locks.
#
#   1. Explicit allowed-tool list (delete_records should not be reachable).
#   2. Argument validation: exactly the expected args, and the recipient
#      must be on an allowed domain.
#   3. Approval bound to the EXACT action. `approval` is the action a human
#      looked at and said yes to: {"tool": ..., "arguments": {...}}.
#      If anything differs from what they approved, reject it.
#
# Raise PermissionError when you reject. Only call the real tool when every
# lock passes. Run `pytest -q` to check yourself.
# ---------------------------------------------------------------------------

ALLOWED_TOOLS = {"send_email"}
ALLOWED_RECIPIENT_DOMAINS = {"example.org"}


def safe_execute_tool(name: str, args: dict, approval: dict | None = None):
    raise NotImplementedError("Install the three locks here.")
