# Changelog

## [2026-10-06] - wave 3: 27 harnesses, and the journals go public

### Added
- `journals/` — the research journals behind every page (waves 1-2 exported from the original runs, wave 3 from five independent researchers); regeneration is `python3 scripts/generate.py journals/*.jsonl`.
- Five rows: Augment Code (rules hierarchy incl. CLAUDE.md above AGENTS.md, six skill roots incl. .claude/skills and .agents/skills), Tabnine (guidelines at user/project/enterprise scopes; skills in .agents/skills aliases; CLI in maintenance mode), Replit Agent (replit.md + workspace Custom Instructions; /.agents/skills + .local/secondary_skills), Qodo (instructions live in the HOST agent's AGENTS.md/CLAUDE.md by design; standards at workspace scope), Bolt (lowercase agents.md auto-read; AGENTS.md not documented).
- `scripts/check-counts.sh` + CI count-gate (added earlier today) now guards every count in this repo.

### Modified
- `scripts/generate.py` — vocabulary matching is case-sensitive: Bolt's lowercase `agents.md` is a distinct convention from `AGENTS.md`, and counting it as compliance would be the survey's own lie. Verified identical hits on waves 1-2 before switching.
- README/SYNTHESIS/MEMORY counts: AGENTS.md 23 of 27 (holdouts: Aider, Replit, Tabnine, Bolt-as-case-variant); .agents/skills 19, .claude/skills 12; memory split 15/12.

## [2026-10-06] - 22 harnesses: memory split updated for the cloud-autonomous cluster

### Modified
- `MEMORY.md` — the learned-memory split now covers all 22 harness pages: Cursor, Windsurf (legacy Cascade), Google Jules, Amazon Kiro and Devin join the built-in-memory column (12 vs 10), each with where its notes live; new point 5 on account-scoped cloud memory and vendor-side migration paths.

## [2026-10-05] - Initial release: 17 harnesses, four views

### Added
- Research run wf_2ae2253f: one focused researcher per harness — instruction files, skill dirs, learned memory, precedence, each with fetched evidence URLs
- `matrix.md` — vocabulary-matched load grid (21 markers); `harnesses/*.md` — full per-harness detail
- `SYNTHESIS.md` — AGENTS.md won by being the fallback; skills split .agents (13) vs .claude (8); house files accrete; precedence is the real break
- `PRECEDENCE.md` — three conflict models: concatenate, first-match, specificity-overrides
- `MEMORY.md` — learned-memory map: 7 write notes about you (defaults differ), 10 do not
- `scripts/generate.py` — journal-to-pages generator; `scripts/mirror-skills.sh` — copy a skill into both wide-discovery locations
- `hero.svg`, `README.md`, `CONTRIBUTING`-grade evidence contract shared with harness-atlas
