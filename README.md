# Who Let the Ghost In? 👻

**3percentclub AI Builders · Week 5: Secure AI (keep your app's data private)**

Tonight our agent is a haunted house. Every tool, memory, and search index we added in Weeks 1–4 is a room, and every room is one more door a ghost can float through. We find the doors, then lock them **in code, not in a prompt.**

> The rule of the house: **the model proposes. Your code decides.**

## Start here (no install, no key)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/3percentclub/builders-week5/blob/main/lab.ipynb)

Click the button, then press play on each gray box from top to bottom. You don't need an API key and you don't need to sign up for anything.

Everything here is fake on purpose: synthetic case notes, a mock model, and a fake outbox (just a Python list). No API key. Nothing really sends.

**Provider-agnostic.** There's no AI SDK in this repo: just the Python standard library plus `pytest`. `lab/mock_model.py` stands in for the model (`propose_actions`, `react_to_documents`, `write_answer`) and returns plain JSON tool calls. The security layer (`activities/fix_the_tool/locks.py`, `lab/policy.py`) sits outside the model, so it works with any provider you plug in later (AI Gateway, OpenRouter, Ollama, anything with tool calling). Swap the model, keep the locks.

---

## Setup (2 minutes)

```bash
git clone https://github.com/3percentclub/builders-week5.git
cd builders-week5
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

You only need Python 3.10+ and `pytest`.

---

## What's in the house

| Room | Folder | When |
|---|---|---|
| Follow the Footprints | `activities/trace_it/` | In class (solo, no code) |
| The Door With No Lock | `activities/fix_the_tool/` | In class (solo, no LLM needed) |
| Mask the Names (+ Boss Level) | `activities/mask_it/` | In class (solo, no LLM needed) |
| Plant a Ghost, Then Bust It | `lab/` | Final lab (solo) |
| Homework | `homework/` | Due **Sun Oct 18, 11:59pm ET** |

---

## Room 1 · Follow the Footprints (no code)

Open `activities/trace_it/data-map.md`. For every box in the architecture, answer the five questions. "Unknown" counts as an answer, and an important one: unknown retention is a finding.

## Room 2 · The Door With No Lock

```bash
cd activities/fix_the_tool
pytest -q          # fails until you write safe_execute_tool()
```

`executor.py` runs whatever the model asks for. Three proposals knock at the door (`proposals.json`). All three are valid JSON. Only one is a friendly trick-or-treater. Install three locks:

1. An explicit allowed-tool list
2. Argument validation + allowed destinations
3. Approval bound to the **exact** action (if the recipient changes after approval, it fails)

## Room 2.5 · Mask the Names

```bash
cd activities/mask_it
python peek.py            # see what the model and the log would get right now
pytest -q test_redact.py  # warm-up: fails until you write redact()
pytest -q test_boss.py    # boss level: fails until you write mask() + unmask()
```

Case notes are full of names, phones, emails, and case IDs. Every note goes through one choke point in code before it reaches the model or the log. A prompt saying "please don't repeat names" is not a lock.

- **Warm-up (`redact.py`):** swap personal info for labels like `[NAME]` and `[PHONE]`. The hints are in the file.
- **Boss level (`boss.py`):** use numbered tokens you can reverse, so the model's reply can go back to the right person. Same person = same token (even "jordan" in lowercase), "Samsung" is not Sam, and the vault never leaves your code. No hints.

## Room 3 · Plant a Ghost, Then Bust It (final lab)

One ghost (attacker), one ghostbuster (defender). Switch halfway.

```bash
cd lab

# 1. A normal question against the clean document (your baseline)
python app.py "What documents should someone bring to the housing-support appointment?"

# 2. Same question, but the haunted document is on the shelf
python app.py --haunted "What documents should someone bring to the housing-support appointment?"
```

Look at the proposed action and the fake outbox. The case note escaped. The model thought it was being compliant.

Now open `policy.py` and bolt the door. Then:

```bash
pytest tests/      # 2 fail until the door is bolted
```

**Done when:**
- The normal program question still works.
- The malicious action is rejected even when the model proposes it.
- No synthetic case note appears in the fake outbox.

**Done early?** Add schema validation, a PII redaction step before the "model" sees the docs, or a cross-org test (org_a can't read org_b's docs).

---

## Homework

See [`homework/README.md`](homework/README.md). Three parts, built for your hackathon project.

## Key dates

- **Thu Oct 22** · Week 6: Evals, guardrails & system architecture
- **Fri Oct 23 – Sat Oct 24** · Spooky Civic AI Hackathon: Build Weekend
- **Sun Oct 25, 2–5pm ET** · Demo Day

Questions? Ask in the cohort Discord.
