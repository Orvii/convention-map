# Codex CLI

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `$CODEX_HOME/AGENTS.override.md (default ~/.codex/AGENTS.override.md; CODEX_HOME overrides the home)` | global | Global scope is checked first: AGENTS.override.md if present, otherwise AGENTS.md. Only the first non-empty file at this level is used. Global instructions are prepended before the project chain (global first, repo root second, nested override last). | [src](https://developers.openai.com/codex/guides/agents-md) |
| `$CODEX_HOME/AGENTS.md (default ~/.codex/AGENTS.md)` | global | Fallback for the home dir: loader iterates [AGENTS.override.md, AGENTS.md] and returns the first non-empty file; empty override falls through to AGENTS.md. Rebuilt on every run / at start of each TUI session, no cache. | [src](https://github.com/openai/codex/blob/main/codex-rs/codex-home/src/instructions/mod.rs) |
| `<every directory from project root down to CWD>/AGENTS.override.md` | project | Project scope walks from project root (default: dir containing .git; project_root_markers configurable) down to CWD, inclusive; if no project root found only CWD is checked. Per directory the candidate order is AGENTS.override.md, then AGENTS.md, then project_doc_fallback_filenames entries; at most one file per directory (first that exists wins). | [src](https://github.com/openai/codex/blob/main/codex-rs/core/src/agents_md.rs) |
| `<every directory from project root down to CWD>/AGENTS.md` | project | All selected files are concatenated root-to-CWD (joined in the prompt; source uses a "\n\n--- project-doc ---\n\n" separator), so files closer to CWD appear later and override earlier guidance. Combined cap project_doc_max_bytes, default 32 KiB; empty files skipped; file content is truncated at the remaining budget. | [src](https://developers.openai.com/codex/guides/agents-md) |
| `<project directories>/<entries of project_doc_fallback_filenames> (project_doc_fallback_filenames, e.g. ["TEAM_GUIDE.md", ".agents.md"])` | project | Checked per directory only after AGENTS.override.md and AGENTS.md are missing. Default list is empty (config source: Some(Vec::new())), so out of the box only AGENTS.override.md/AGENTS.md load; e.g. adding CLAUDE.md here would make Codex load it like an instructions file. Entries must be plain filenames (entries containing path separators, '.', '..' are ignored with a warning). | [src](https://learn.chatgpt.com/docs/config-file/config-reference) |
| `~/.codex/config.toml (global config layer; CODEX_HOME based)` | global | Base user config layer; key instruction-related knobs live here: project_doc_fallback_filenames, project_doc_max_bytes, project_root_markers, model_instructions_file (replaces built-in base instructions instead of AGENTS.md), [skills.config] enable/disable entries. | [src](https://learn.chatgpt.com/docs/config-file/config-advanced) |
| `<repo dir>/.codex/config.toml (project config layers, plus .codex/hooks.json / inline [hooks])` | project | Codex walks root-to-CWD and loads every .codex/config.toml it finds; on key conflicts the file closest to CWD wins. Loaded only when the project is trusted; if untrusted, project .codex layers (config, hooks, rules) are ignored. Relative paths inside resolve against the containing .codex/ folder. | [src](https://learn.chatgpt.com/docs/config-file/config-advanced) |

## Skill directories discovered

- `<each dir from CWD up to repo root>/.agents/skills (i.e. $CWD/.agents/skills, ancestor dirs, $REPO_ROOT/.agents/skills)` — [src](https://developers.openai.com/codex/skills)
- `~/.agents/skills ($HOME/.agents/skills)` — [src](https://developers.openai.com/codex/skills)
- `/etc/codex/skills (ADMIN scope; system config layer folder for /etc/codex/config.toml)` — [src](https://developers.openai.com/codex/skills)
- `$CODEX_HOME/skills (deprecated user skills location, kept for backward compatibility)` — [src](https://github.com/openai/codex/blob/main/codex-rs/ext/skills/src/host_roots.rs)
- `$CODEX_HOME/skills/.system (SYSTEM scope: bundled OpenAI skills cache; embedded samples copied here)` — [src](https://github.com/openai/codex/blob/main/codex-rs/skills/src/lib.rs)
- `<each project config layer dir>/.codex/skills (REPO scope, one per project layer found between repo root and CWD)` — [src](https://github.com/openai/codex/blob/main/codex-rs/ext/skills/src/host_roots.rs)

## Learned memory

Yes - Codex CLI has built-in learned memory, off by default: enable with [features] memories = true in config.toml (or Settings > Personalization in the desktop app); after enabling, Codex generates local memory files under ~/.codex/memories/ (summaries, durable entries, recent inputs, evidence) in background passes and injects existing memories into future sessions, with per-chat /memories controls and settings like memories.generate_memories / memories.use_memories; docs explicitly say to keep mandatory rules in AGENTS.md, not memory.

[src](https://learn.chatgpt.com/docs/customization/memories)

## Compatibility notes

No runtime compatibility with other vendors' convention files: nothing in the discovery code reads CLAUDE.md, GEMINI.md, CRUSH.md, .cursorrules, .cursor/rules, etc. Out of the box it loads only AGENTS.override.md / AGENTS.md (project_doc_fallback_filenames default = empty). BUT it ships a one-time importer, not a loader: the external-agent-migration crate + TUI "external agent config migration" flow reads Claude Code config (~/.claude dir, CLAUDE.md, settings.json, commands, hooks, sessions, memory/plugins marketplaces) and Cursor config (.cursor dir, .cursorrules, cli.json, hooks.json, cli-config.json) to import/rewrite them into Codex config (source: codex-rs/external-agent-migration/src/source/cla.rs and cur.rs). Other notable context-file mechanics: search for AGENTS.md stops at the project root (git root by default) so files above the repo root are never read; project .codex layers (config.toml, hooks.json, .codex/skills) load only for trusted projects; skills with the same name from different roots are not merged, both appear in selectors; skill folders may be symlinks (followed); skills bundled in plugins are also discovered from installed plugin roots (plugin checkouts under $CODEX_HOME/plugins, marketplace-based); config key "instructions" is reserved/deprecated in favor of model_instructions_file or AGENTS.md.
