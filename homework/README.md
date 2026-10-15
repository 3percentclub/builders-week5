# Homework: Haunt-Proof Your Hackathon App 🎃

**Due Sun Oct 18, 11:59pm ET** · Submit in Google Classroom (Week 5 topic)

Three tasks. If you're on a hackathon team, do tasks 2 and 3 for that project. No team yet? Use the lab app.

---

## Task 1 · Finish the lab + name one ghost that's still loose

```bash
cd lab
pytest tests/
```

All green? Then open [`remaining-risk.md`](remaining-risk.md) and write down **one** risk your fix does *not* cover. A few ideas to get you started:

- What if a future tool *is* allowed to send messages?
- What if the injection lives in a user's question instead of a document?
- What if the vector index mixes two nonprofits' documents?

**Submit:** a screenshot of the passing tests + your filled-in `remaining-risk.md`.

## Task 2 · Draw your hackathon data map

Copy [`data-map-template.md`](data-map-template.md). One row per component your app touches. Ask the five questions of every box:

1. What data reaches it?
2. Does it store content?
3. How long?
4. Who has access?
5. What should change?

"Unknown" is a fine answer, and it's a finding, so write it down.

**Submit:** the filled template (a photo of a whiteboard drawing is fine too).

## Task 3 · Scan your repo + run the inspection

```bash
# macOS
brew install gitleaks
# everyone else: https://github.com/gitleaks/gitleaks#installing

gitleaks git -v .
```

Fix anything it finds, **rotate any real key it caught** (deleting the line isn't enough: it's still in git history), and turn on GitHub push protection (repo Settings → Code security).

Then go through [`inspection-checklist.md`](inspection-checklist.md). If you already have an AI Citizens partner, do it together on a quick call. No partner yet? Do it solo. That's fine, and you'll review it with your hackathon team on Friday.

**Submit:** the Gitleaks summary line + the filled-in checklist.

---

Stuck? Post in the cohort Discord. Every class starts with a recap, so jump in on Thursday either way.
