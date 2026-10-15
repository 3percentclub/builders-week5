"""BOSS LEVEL: mask it so you can put it back.

redact() threw the real values away. That's fine for a log, but a real app
has to reply to the right person. The model writes "Tell [NAME_1] to call
back", and your code puts "Jordan Example" back in before the text goes out.

Write two functions:

  mask(text)          -> (masked_text, vault)
  unmask(text, vault) -> text with the real values put back

Rules (the tests check every one):
  1. Numbered tokens: [NAME_1], [EMAIL_1], [PHONE_2], [CASE_ID_1] ...
  2. Same person = same token. "Jordan Example" and later "Jordan" (or
     "jordan") are both [NAME_1]. The model needs to know it's one person.
  3. Don't mask what isn't personal. "Samsung" is not Sam. "Jordanville" is
     not Jordan. "open since 2019" is not a phone number.
  4. The vault stays in YOUR code. It never goes to the model or the log.
  5. unmask() puts emails, phones, and case IDs back exactly, and every
     name back as the person's full name ("jordan" -> "Jordan Example").

No hints this time. Check yourself with `pytest -q test_boss.py`.
"""

PEOPLE = {
    "Jordan Example": ["Jordan"],
    "Sam Placeholder": ["Sam"],
    "Riley Demo": ["Riley"],
}


def mask(text: str) -> tuple[str, dict[str, str]]:
    raise NotImplementedError("Mask with numbered tokens and return the vault.")


def unmask(text: str, vault: dict[str, str]) -> str:
    raise NotImplementedError("Put the real values back.")
