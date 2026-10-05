# Vibe

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `$VIBE_HOME/AGENTS.md (default ~/.vibe/AGENTS.md; VIBE_HOME is env-overridable)` | global | User-level instructions, injected in the system prompt as '## User instructions'. Documented instruction hierarchy (system-prompt template) ranks repo AGENTS.md files (level 3) above the user's AGENTS.md (level 4), so project files win on conflict. Loaded only while the 'user' source is enabled — CLI, app-server and ACP all init with ('user', 'project'). | [src](https://github.com/mistralai/mistral-vibe/blob/main/vibe/core/config/harness_files/_harness_manager.py#L220-L228) |
| `<project root>/…/AGENTS.md — every AGENTS.md from each open project root (trusted cwd, or --add-dir roots) up to its trust root` | project | All files on the chain are active and rendered outermost-first (later entry = higher priority); closer to the task wins on conflict; project instructions take priority over ~/.vibe/AGENTS.md. Loaded only for trusted folders — trust root comes from trusted_folders.toml and falls back to the root itself; results deduped by resolved directory across roots. | [src](https://github.com/mistralai/mistral-vibe/blob/main/vibe/core/config/harness_files/_harness_manager.py#L281-L298) |
| `<project>/**/AGENTS.md — subdirectory docs, discovered lazily` | project | Not in the startup prompt: when read_file reads a file below an open project root, AGENTS.md files between that file's parent and the project root are appended to the tool result once per directory per session (same closer-wins semantics). The Unified Harness (Rust core) never loads AGENTS.md itself — the host composes the startup section and a builtin post-tool hook restores lazy discovery for unified sessions. | [src](https://github.com/mistralai/mistral-vibe/blob/main/vibe/core/tools/builtins/read_file.py#L120-L140) |
| `<project root>/.vibe/prompts/<id>.md and ~/.vibe/prompts/<id>.md — custom system prompt override (id from config system_prompt_id, default 'cli')` | both | Completely replaces the default system prompt when the file exists. Search order in load_prompt: project .vibe/prompts/ dirs first, then ~/.vibe/prompts/, then bundled builtin prompts; first hit wins. | [src](https://github.com/mistralai/mistral-vibe/blob/main/vibe/core/prompts/__init__.py#L79-L96) |

## Skill directories discovered

- `~/.vibe/skills/ ($VIBE_HOME/skills — one subdirectory per skill, SKILL.md inside; user scope)` — [src](https://github.com/mistralai/mistral-vibe/blob/main/vibe/core/config/harness_files/_paths.py#L5-L6)
- `~/.agents/skills/ (AGENTS_HOME = ~/.agents; Agent Skills standard location, user scope)` — [src](https://github.com/mistralai/mistral-vibe/blob/main/vibe/core/config/harness_files/_paths.py#L13)
- `<project root>/.vibe/skills/ (root-level only, trusted folders only, project scope)` — [src](https://github.com/mistralai/mistral-vibe/blob/main/vibe/core/paths/_local_config_files.py#L73-L75)
- `<project root>/.agents/skills/ (root-level only, trusted folders only, project scope)` — [src](https://github.com/mistralai/mistral-vibe/blob/main/vibe/core/paths/_local_config_files.py#L94-L97)
- `custom dirs from config skill_paths (absolute or cwd-relative; treated as GLOBAL scope)` — [src](https://github.com/mistralai/mistral-vibe/blob/main/vibe/core/skills/manager.py#L86-L97)
- `~/.vibe/plugins/<plugin>/skills/<name>/SKILL.md and <root>/.vibe/plugins/<plugin>/skills/<name>/SKILL.md (plugin-provided skills; foreign Claude Code/Codex/Kimi/OpenCode plugin trees adapted to skills + MCP only)` — [src](https://github.com/mistralai/mistral-vibe/blob/main/vibe/core/skills/builtins/vibe.py#L1100-L1124)
- `~/.vibe/skills-registry-cache/store/<skill-id>/<version>/SKILL.md (experimental skills registry cache; off by default)` — [src](https://github.com/mistralai/mistral-vibe/blob/main/vibe/core/skills/registry/_store.py#L24-L30)

## Learned memory

None — no built-in learned/auto memory: repo-wide search finds no memories directory or auto-memory feature; ~/.vibe holds config, hooks, history, session logs and plans (sessions persist for resume, but nothing is auto-learned), and the only knowledge artifact is plugin-bundled static KNOWLEDGE.md files.

[src](https://github.com/mistralai/mistral-vibe/blob/main/vibe/core/skills/builtins/vibe.py#L19-L46)

## Compatibility notes

Repo is mistralai/mistral-vibe ("Minimal CLI coding agent by Mistral"); all evidence fetched from main @ 7c19608af06f6c61d63f8f7a5c3430da73fba2ab (tarball + raw URLs, verified 200).

Foreign-vendor compatibility: no reads of CLAUDE.md, GEMINI.md, CRUSH.md, .cursorrules, .windsurfrules, .clinerules or kilo.jsonc anywhere (repo-wide grep clean). Claude Code compatibility is plugin-format only: a plugin directory under ~/.vibe/plugins/ or .vibe/plugins/ whose manifest is .claude-plugin/plugin.json is adapted (skills + MCP servers only; hooks/knowledge/agents/libraries/connectors are native-only, executable JS/TS refused) — see https://github.com/mistralai/mistral-vibe/blob/main/vibe/core/plugins/_compatibility.py and vibe/core/plugins/_claude.py. Same for Codex (.codex-plugin/plugin.json), Kimi (.kimi.plugin.json or .kimi-plugin/plugin.json) and OpenCode (.opencode/plugins/, .opencode/skills/*/SKILL.md, opencode.json/opencode.jsonc inside the plugin root). Vibe also reads OpenAI Codex per-skill metadata agents/openai.yaml (allow_implicit_invocation policy) in any skill dir — vibe/core/skills/parser.py#L12-L21.

Own conventions beyond AGENTS.md: config files are ~/.vibe/config.toml (user) and <root>/.vibe/config.toml (project, trusted only, wins per field; discovered on nearest ancestor up to VIBE_HOME.parent), plus hooks.toml (~/.vibe/hooks.toml + <root>/.vibe/hooks.toml); layering per docs/adr/0005: defaults < discovered < user TOML < project TOML < VIBE_* env < session overrides < admin (admin always highest). Registry manifests: <root>/.vibe/skills.toml and ~/.vibe/skills.toml (experimental). Bundled builtin skills ship in the package (worktree, vibe, skill-creator, create-plugin), not on disk. The repo itself dogfoods: AGENTS.md + .agents/skills/ + .vibe/skills/.

Instruction hierarchy template text lives at harness/runtimes/python/python/mistralai_vibe_local_harness/vibe/_system_instructions.py#L13-L26 (critical > user messages > repo AGENTS.md > user AGENTS.md > overridable defaults > skills/MCP > external data); the AGENTS_DOC utility prompt states project-over-user and closer-file-wins: vibe/core/prompts/agents_doc.md. README sections corroborate: Skill Discovery README.md#L435-L445, Custom System Prompts README.md#L545-L558. Unified Harness core (Rust) never loads AGENTS.md itself — host composes startup prompt, builtin post-tool hook handles lazy subdir injection (vibe/app_server/_agents_md_hooks.py#L1-L11).
