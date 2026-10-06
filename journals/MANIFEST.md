# Journals — the public source of every page

Sanitized researcher results, one JSON object per line. Regenerate the map:

    python3 scripts/generate.py journals/wf_2ae2253f-8b3.jsonl journals/wf_dfb588e1-caa.jsonl journals/wf_v34-incoming.jsonl

| file | harness results | wave |
|---|---|---|
| [wf_2ae2253f-8b3.jsonl](wf_2ae2253f-8b3.jsonl) | 17 | wave 1 — first seventeen harnesses |
| [wf_dfb588e1-caa.jsonl](wf_dfb538e1-caa.jsonl) | 5 | wave 2 — Cursor, Windsurf, Jules, Kiro, Devin (to twenty-two) |
| [wf_v34-incoming.jsonl](wf_v34-incoming.jsonl) | 5 | wave 3 — Augment Code, Tabnine, Replit Agent, Qodo, Bolt |

Later files win on conflicts (see `scripts/generate.py`).
