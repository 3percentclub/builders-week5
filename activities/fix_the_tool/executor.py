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


# The locks live in locks.py. That's the file you edit.
