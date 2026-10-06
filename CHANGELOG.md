# Changelog

## [2026-10-06] - link-rot repair: five moved evidence URLs re-pointed

### Modified
- `journals/wf_v34-incoming.jsonl` and the `journals-incoming/` sources (tracked in this repo) — five vendor doc pages that moved since the research run, re-pointed to their live canonical URLs with each claim re-verified against the new page: Qodo `agentic-toolbox/manage-standards` → `…/manage-standards-skill` (carries the Review Standards wording); Replit `replitai/replit-md` → `features/project-setup/replit-dot-md` (carries "When Agent processes your requests, it automatically reads your `replit.md` file"), `replitai/agent-customization` → `features/agent/agent-customization` (carries "Workspace Settings → Customization"), `replitai/memories` → `chat/memories` (carries the private-by-default and Custom-Instructions-take-priority wording); Bolt `best-practices/manage-project-context` → `best-practices/manage-context` (carries the agents.md auto-read and record-keeping claims).
- `harnesses/{bolt,qodo,replit-agent}.md` regenerated — paths, scopes and precedence notes unchanged, only the citation URLs moved.
- Replit's `replit.md` row needed a source hunt rather than a slug guess: the page is absent from `llms.txt` but documented in full in `llms-full.txt`, which is what surfaced `features/project-setup/replit-dot-md`.

### Removed
- `scripts/__pycache__/` untracked and gitignored — a compiled artifact had been committed.

## [2026-10-06] - enforced reproducibility: regen-check gate + manifest-ordered regeneration

### Added
- `.github/workflows/regen-check.yml` — regenerates every page from `journals/` on data-path pushes and fails if any committed page differs. The evidence contract now has the same mechanical enforcement harness-atlas has: a hand-edited cell cannot land.

### Modified
- `scripts/generate.py` — `main()` orders journals by the wave sequence `journals/MANIFEST.md` declares instead of trusting the caller's argument order. The documented command is `generate.py journals/*.jsonl`, and a shell glob expands alphabetically, not by wave; the sort makes the printed command correct for any file set (the latent form of the bug that bit harness-atlas). Explicit `manifest=` override for CI's /tmp regeneration; `encoding="utf-8"` on every read and write (the documented workflow previously depended on the platform default encoding).
- `README.md` — the Regenerating section prints the safe glob form and states that CI enforces regeneration parity.

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
