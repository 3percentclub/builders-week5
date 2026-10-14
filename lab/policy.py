"""The front door. Every action the model proposes comes through here.

As shipped, the door has no lock: whatever the model asks for, runs.

YOUR JOB (Steps 4–5):
  This assistant only answers questions about public programs, so it should
  be READ-ONLY. Reject anything that isn't `search_public_programs` by raising
  PermissionError. Then rerun BOTH the normal question and the attack.

  The model proposes. Your code decides.
"""

from tools import TOOLS


def execute_action(action: dict, haunted: bool = False):
    tool = TOOLS[action["tool"]]
    if action["tool"] == "search_public_programs":
        return tool(**action["arguments"], haunted=haunted)
    return tool(**action["arguments"])
