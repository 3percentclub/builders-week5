import re
from pathlib import Path

import pytest

import pipeline
from redact import KNOWN_NAMES, redact

NOTES = (Path(__file__).parent / "notes.txt").read_text().strip().splitlines()
ALL = "\n".join(NOTES)


@pytest.fixture(autouse=True)
def fresh_sinks():
    pipeline.MODEL_INBOX.clear()
    pipeline.LOG.clear()
    yield


def test_emails_are_masked():
    out = redact(ALL)
    assert "@" not in out
    assert out.count("[EMAIL]") == 2


def test_every_phone_format_is_masked():
    out = redact(ALL)
    assert not re.search(r"\d{3}\D{0,2}\d{4}", out), out
    assert out.count("[PHONE]") == 4


def test_case_ids_are_masked():
    out = redact(ALL)
    assert "DEMO-" not in out
    assert out.count("[CASE_ID]") == 2


def test_names_are_masked_even_first_names_alone():
    out = redact(ALL)
    for name in KNOWN_NAMES:
        assert not re.search(rf"\b{name}\b", out), f"{name!r} leaked: {out}"
    assert "[NAME]" in out


def test_the_useful_part_survives():
    out = redact(NOTES[0])
    assert "needs housing support" in out
    assert "staying with a friend" in out


def test_nothing_personal_reaches_the_model_or_the_log():
    for note in NOTES:
        pipeline.ask_model(note)
    leaked = "\n".join(pipeline.MODEL_INBOX + pipeline.LOG)
    for secret in ["jordan@example.org", "555-0147", "DEMO-4821", "Sam Placeholder", "Riley"]:
        assert secret not in leaked, f"{secret!r} reached the model or the log"
    assert len(pipeline.MODEL_INBOX) == 3
