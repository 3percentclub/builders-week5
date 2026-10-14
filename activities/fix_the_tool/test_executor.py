import json
from pathlib import Path

import pytest

import executor
from locks import safe_execute_tool

PROPOSALS = json.loads((Path(__file__).parent / "proposals.json").read_text())
REMINDER, DELETE_ALL, EXFILTRATE = PROPOSALS


@pytest.fixture(autouse=True)
def fresh_house():
    executor.OUTBOX.clear()
    executor.DATABASE.update({"clients": ["Jordan Example", "Sam Placeholder"], "volunteers": ["Riley Demo"]})
    yield


def test_unknown_tool_is_rejected():
    with pytest.raises(PermissionError):
        safe_execute_tool(DELETE_ALL["tool"], DELETE_ALL["arguments"], approval=DELETE_ALL)
    assert "clients" in executor.DATABASE


def test_extra_argument_is_rejected():
    args = {**REMINDER["arguments"], "bcc": "outside@example.invalid"}
    with pytest.raises(PermissionError):
        safe_execute_tool("send_email", args, approval={"tool": "send_email", "arguments": args})
    assert executor.OUTBOX == []


def test_unapproved_recipient_is_rejected():
    with pytest.raises(PermissionError):
        safe_execute_tool(EXFILTRATE["tool"], EXFILTRATE["arguments"], approval=EXFILTRATE)
    assert executor.OUTBOX == []


def test_denied_approval_sends_nothing():
    with pytest.raises(PermissionError):
        safe_execute_tool(REMINDER["tool"], REMINDER["arguments"], approval=None)
    assert executor.OUTBOX == []


def test_recipient_changed_after_approval_is_rejected():
    tampered = {**REMINDER["arguments"], "to": "someone-else@example.org"}
    with pytest.raises(PermissionError):
        safe_execute_tool("send_email", tampered, approval=REMINDER)
    assert executor.OUTBOX == []


def test_valid_approved_reminder_sends_exactly_once():
    safe_execute_tool(REMINDER["tool"], REMINDER["arguments"], approval=REMINDER)
    assert executor.OUTBOX == [REMINDER["arguments"]]
