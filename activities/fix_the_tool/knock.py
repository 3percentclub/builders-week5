"""Three proposals knock at the door. Watch what gets in.

    python knock.py            # the door with no lock (executor.execute_tool)
    python knock.py --locked   # your locks (locks.safe_execute_tool)

Every proposal is "approved" exactly as written, so only your locks can stop it.
"""

import json
import sys
from pathlib import Path

import executor

PROPOSALS = json.loads((Path(__file__).parent / "proposals.json").read_text())


def main() -> None:
    locked = "--locked" in sys.argv
    if locked:
        from locks import safe_execute_tool

    print("DOOR:", "your locks" if locked else "no lock", "\n")
    for proposal in PROPOSALS:
        name, args = proposal["tool"], proposal["arguments"]
        try:
            if locked:
                result = safe_execute_tool(name, args, approval=proposal)
            else:
                result = executor.execute_tool(name, args)
            print(f"  LET IN   {name} {args} -> {result}")
        except PermissionError as err:
            print(f"  BLOCKED  {name} {args} -> {err}")
        except NotImplementedError as err:
            print(f"  TODO     {err}")
            break

    print("\nclients table:", executor.DATABASE.get("clients", "GONE"))
    print("fake outbox:  ", json.dumps(executor.OUTBOX) if executor.OUTBOX else "(empty)")


if __name__ == "__main__":
    main()
