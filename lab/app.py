"""Public-programs helper for a fictional nonprofit.

    python app.py "What should I bring to my housing appointment?"
    python app.py --haunted "What should I bring to my housing appointment?"
"""

import argparse
import json

import mock_model
from policy import execute_action
from tools import OUTBOX


def run(question: str, haunted: bool = False) -> dict:
    OUTBOX.clear()
    proposed, blocked, documents = [], [], []

    for action in mock_model.propose_actions(question):
        proposed.append(action)
        documents = execute_action(action, haunted=haunted)

    for action in mock_model.react_to_documents(documents):
        proposed.append(action)
        try:
            execute_action(action, haunted=haunted)
        except PermissionError as err:
            blocked.append({"action": action, "reason": str(err)})

    return {
        "answer": mock_model.write_answer(question, documents),
        "proposed": proposed,
        "blocked": blocked,
        "outbox": list(OUTBOX),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("question")
    parser.add_argument("--haunted", action="store_true", help="put the haunted document on the shelf")
    parser.add_argument("--mock", action="store_true", help="kept for the slides; mock mode is the only mode")
    args = parser.parse_args()

    result = run(args.question, haunted=args.haunted)

    print("\n[model proposed actions]")
    print(json.dumps(result["proposed"], indent=2))
    if result["blocked"]:
        print("\n[blocked by policy.py]")
        for item in result["blocked"]:
            print(f"  {item['action']['tool']}: {item['reason']}")
    print("\n[fake outbox]")
    print(json.dumps(result["outbox"], indent=2) if result["outbox"] else "  (empty)")
    print("\n[answer]")
    print(f"  {result['answer']}\n")


if __name__ == "__main__":
    main()
