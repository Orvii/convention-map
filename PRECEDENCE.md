# Precedence — when two instruction files disagree

As of 2026-10-05. Loading a file is the easy half; what happens when two loaded files contradict is where compatibility actually breaks. Sources: per-harness pages, each cell's precedence note carrying its doc URL.

## The three conflict models

The field splits into exactly three semantics:

**1. Concatenate, never override.** All discovered files load, ordered broadest-first; the model sees everything and resolves conflicts itself.
- Claude Code: managed → user → project, concatenated root-first; `CLAUDE.local.md` appended after `CLAUDE.md` at each level.
- Gemini CLI: global tier first, then workspace and JIT files, concatenated into every prompt.
- Qwen Code: all hits concatenated with origin separators; order inspectable in `/memory`.
- Copilot CLI: combines all applicable user + repo + agent instructions, de-duplicating only.

**2. First match wins.** A priority list; the first file that exists is the only one read at that level.
- Zed: documented priority list, first matching file only (`.rules` beats everything below it).
- Codex CLI (global tier): `AGENTS.override.md` if present else `AGENTS.md`; first non-empty wins.
- OpenCode: per category, any project `AGENTS.md` beats project `CLAUDE.md`; global AGENTS beats `~/.claude/CLAUDE.md`.

**3. Specificity overrides.** Narrower scope wins over broader; later-loaded (closer to cwd) takes priority.
- Aider: home → git root → cwd; last loaded wins; `--config` replaces the search entirely.
- Kilo Code: agent prompt > project config instructions > project AGENTS.md > parent dirs.
- Roo Code / Cline: workspace rules take precedence over global on conflict; Cline additionally gates rules by `paths:` frontmatter globs.

## Why this matters more than loading

Two harnesses reading the *same two files* can behave oppositely: under concatenate, a project file cannot silence a global one — it can only out-argue it in context; under first-match, the global file is invisible once a project file exists. A repo maintained for one harness can therefore misconfigure another without any file changing.

Practical rules for multi-harness repos:
- Keep one source of truth per scope. If a global file and a project file disagree, you have written a harness-dependent repo.
- Prefer imports over duplication where the harness supports them (Claude Code's `@path` syntax pulls a shared file into both house and open conventions).
- Test the conflict case once per harness you support: add a deliberately contradicting line in two scopes and observe which wins. That single experiment documents your repo's behavior under each model better than any table here.

## The undocumented middle

Several harnesses document *loading* but not *conflict resolution* (Goose's glob-merged hints, OpenHands' workspace-vs-root duplication note aside). For those, the matrix says ● and this page says: unknown. Unknown precedence is not neutrality — it is a coin flip your users inherit.
