import re
from pathlib import Path

from boss import mask, unmask

NOTES = (Path(__file__).parent / "boss_notes.txt").read_text().strip().splitlines()
ALL = "\n".join(NOTES)
SECRETS = [
    "Jordan", "jordan", "Sam", "Riley", "RILEY", "DEMO-4821", "DEMO-5310",
    "555-0147", "555-0199", "sam@example.org", "riley.demo@example.org",
]


def test_nothing_personal_survives():
    masked, _ = mask(ALL)
    for secret in SECRETS:
        assert not re.search(rf"\b{re.escape(secret)}\b", masked), f"{secret!r} leaked: {masked}"


def test_same_person_gets_the_same_token_in_any_case():
    masked, vault = mask(NOTES[0])
    names = re.findall(r"\[NAME_\d+\]", masked)
    assert len(names) == 2 and len(set(names)) == 1, masked
    assert vault[names[0]] in ("Jordan Example", "Jordan")


def test_different_people_get_different_tokens():
    masked, _ = mask(NOTES[2])
    assert len(set(re.findall(r"\[NAME_\d+\]", masked))) == 2, masked


def test_lookalikes_are_left_alone():
    masked, _ = mask(ALL)
    for keep in ["Samsung", "Jordanville", "open since 2019", "300 visits a month"]:
        assert keep in masked, f"{keep!r} was masked by mistake: {masked}"


def test_round_trip_puts_everything_back():
    masked, vault = mask(ALL)
    out = unmask(masked, vault)
    assert "[" not in out, out
    for exact in ["DEMO-4821", "DEMO-5310", "(212) 555-0147", "212-555-0199",
                  "sam@example.org", "riley.demo@example.org", "Samsung", "Jordanville"]:
        assert exact in out, f"{exact!r} didn't come back: {out}"
    assert out.count("Jordan Example") == 2
    assert out.count("Sam Placeholder") == 3
    assert out.count("Riley Demo") == 3


def test_a_model_reply_goes_to_the_right_person():
    masked, vault = mask(NOTES[0])
    name = re.search(r"\[NAME_\d+\]", masked).group()
    phone = re.search(r"\[PHONE_\d+\]", masked).group()
    reply = f"Hi {name}, we'll call you at {phone} tomorrow."
    out = unmask(reply, vault)
    assert "Jordan" in out and "555-01" in out and "[" not in out, out


def test_the_vault_never_leaves_your_code():
    masked, vault = mask(ALL)
    for real in vault.values():
        assert real not in masked
