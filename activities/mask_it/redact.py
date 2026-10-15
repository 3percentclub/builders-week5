"""YOUR JOB: write redact() so nothing personal leaves your code.

Before a case note goes to a model (or into a log), swap every piece of
personal info for a label:

  emails          -> [EMAIL]
  phone numbers   -> [PHONE]     (every format in the notes: (212) 555-0147,
                                  212-555-0199, 212.555.0123, +1 212 555 0100)
  case IDs        -> [CASE_ID]   (they look like DEMO-4821)
  client names    -> [NAME]      (use KNOWN_NAMES: you can't regex a name,
                                  but you DO know who's in your own database)

Keep everything else, so the model can still help ("needs housing support"
must survive). Check yourself with `pytest -q`.

Hints: `import re`. Do emails BEFORE phones. Replace longer names before
shorter ones ("Jordan Example" before "Jordan").
"""

import re  # noqa: F401  (you'll want this)

KNOWN_NAMES = ["Jordan Example", "Sam Placeholder", "Riley Demo", "Jordan", "Sam", "Riley"]


def redact(text: str) -> str:
    raise NotImplementedError("Mask the emails, phones, case IDs, and names here.")
