"""YOUR JOB: install three locks on the door.

  1. Explicit allowed-tool list (delete_records should not be reachable).
  2. Argument validation: exactly the expected args ("to" and "body"), and the
     recipient must be on an allowed domain.
  3. Approval bound to the EXACT action. `approval` is the action a human
     looked at and said yes to: {"tool": ..., "arguments": {...}}.
     If anything differs from what they approved, reject it.

Raise PermissionError when you reject. Only call the real tool when every
lock passes. Check yourself with `pytest -q`.
"""

from executor import tools

ALLOWED_TOOLS = {"send_email"}
ALLOWED_RECIPIENT_DOMAINS = {"example.org"}


def safe_execute_tool(name: str, args: dict, approval: dict | None = None):
    raise NotImplementedError("Install the three locks here.")
