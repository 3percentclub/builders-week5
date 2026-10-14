# Follow the Footprints · Data Map

**Groups of 3–4 · 10 min work + 5 min debrief · No code**

## The architecture

```
User
  → Web app
  → AI gateway
  → Model provider

Web app
  → Vector database
  → Email tool
  → Observability platform
```

**The twist:** the model provider offers Zero Data Retention (ZDR). The web app logs full request bodies for debugging.

## Interrogate every room

Fill in one row per box. "Unknown" is a valid answer, and unknown retention is a finding.

| Component | What data reaches it? | Stores content? (Yes / No / Unknown) | How long? | Who has access? | What should change? |
|---|---|---|---|---|---|
| Web app | | | | | |
| AI gateway | | | | | |
| Model provider (ZDR) | | | | | |
| Vector database | | | | | |
| Email tool | | | | | |
| Observability platform | | | | | |

## Your three changes

1.
2.
3.

## Debrief question

Where could this person's information still be tomorrow, even if the model provider kept nothing?
