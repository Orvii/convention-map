# Goose

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `AGENTS.md` | both | One of the two default context filenames (source default: [".goosehints", "AGENTS.md"]). Read from global ~/.config/goose/AGENTS.md plus ~/.agents/AGENTS.md, and locally from every directory between git root and cwd (root-first order), plus nested dirs as goose touches files in them. Docs: when global and local hints conflict, local wins. No conflict resolution documented between the two files in the same dir; contents are concatenated. | [src](https://goose-docs.ai/docs/guides/context-engineering/using-goosehints) |
| `.goosehints` | both | goose's native hints file. Global: ~/.config/goose/.goosehints (Windows: %APPDATA%\Block\goose\config\.goosehints). Local: .goosehints in the working-dir hierarchy up to the git root, plus nested dirs when accessed. Injected into the system prompt every request as '### Global Hints' then '### Project Hints'; docs state local hints are prioritized over global on conflict. Nested hints stay active for the session; restart to reliably pick up edits. | [src](https://goose-docs.ai/docs/guides/context-engineering/using-goosehints) |
| `filenames listed in $CONTEXT_FILE_NAMES (e.g. CLAUDE.md, .cursorrules)` | both | JSON-array env var that REPLACES the default ['.goosehints','AGENTS.md'] list entirely — to keep .goosehints you must list it. Each configured filename is searched in the global ~/.config/goose/ dir and in the project directory hierarchy with the same nested-loading rules; all found files are combined. CLAUDE.md / .cursorrules / GEMINI.md etc. load only if explicitly listed here; none are defaults. | [src](https://raw.githubusercontent.com/block/goose/main/crates/goose/src/hints/load_hints.rs) |
| `MOIM file via $GOOSE_MOIM_MESSAGE_FILE (e.g. ~/.goose/guardrails.md)` | both | Persistent-instruction file re-read and injected into working memory every turn (with $GOOSE_MOIM_MESSAGE_TEXT concatenated); 64KB UTF-8-safe cap; changes apply without session restart — unlike .goosehints which is loaded at session start. | [src](https://goose-docs.ai/docs/guides/context-engineering/using-persistent-instructions) |

## Skill directories discovered

- `~/.agents/skills/` — [src](https://goose-docs.ai/docs/guides/context-engineering/using-skills)
- `.agents/skills/ (project)` — [src](https://goose-docs.ai/docs/guides/context-engineering/using-skills)
- `~/.agents/plugins/<plugin-name>/ (plugin-provided skills)` — [src](https://goose-docs.ai/docs/guides/context-engineering/using-skills)
- `.agents/plugins/<plugin-name>/ (project-scoped plugin skills)` — [src](https://raw.githubusercontent.com/block/goose/main/crates/goose/src/plugins/mod.rs)
- `~/.config/goose/skills/ (platform config dir; "platform-specific config directories" in docs)` — [src](https://raw.githubusercontent.com/block/goose/main/crates/goose/src/skills/mod.rs)
- `~/.claude/skills/ (backward-compat)` — [src](https://raw.githubusercontent.com/block/goose/main/crates/goose/src/skills/mod.rs)
- `.claude/skills/ (project, backward-compat)` — [src](https://raw.githubusercontent.com/block/goose/main/crates/goose/src/skills/mod.rs)
- `.goose/skills/ (project, backward-compat)` — [src](https://raw.githubusercontent.com/block/goose/main/crates/goose/src/skills/mod.rs)
- `~/.config/agents/skills/ (XDG agents config)` — [src](https://raw.githubusercontent.com/block/goose/main/crates/goose/src/skills/mod.rs)

## Learned memory

Yes — built-in learned memory: the Memory extension (bundled MCP server, toggleable) saves learned facts as files under ~/.config/goose/memory/ (global) and .goose/memory/ (project), and all saved memories are loaded at session start and included in every prompt sent to the LLM (remember_memory/retrieve_memories tools, remember/forget trigger words).

[src](https://goose-docs.ai/docs/mcp/memory-mcp)

## Compatibility notes

Docs moved: https://block.github.io/goose/docs/ now 404s and JS-redirects to https://goose-docs.ai (fetched the redirect page); goose-docs.ai is confirmed official (referenced as http-referer throughout block/goose source). Compatibility: goose natively reads the industry-standard AGENTS.md and is explicitly Claude-compatible — it discovers Agent Skills from .claude/skills/ and ~/.claude/skills/ ("goose skills are compatible with Claude Desktop") and custom agents from .claude/agents/ + .goose/agents/ (project and global), but reads CLAUDE.md only if whitelisted via CONTEXT_FILE_NAMES. No support found for GEMINI.md, CRUSH.md, opencode.json, or kilo.jsonc (checked docs sitemap and repo source). Extra agent-definition dirs (custom agents/subagents): <project>/.agents/agents, .goose/agents, .claude/agents; global ~/.agents/agents, ~/.goose/agents, ~/.claude/agents, plus ~/.config/goose/agents (https://goose-docs.ai/docs/guides/context-engineering/custom-agents and https://raw.githubusercontent.com/block/goose/main/crates/goose/src/sources.rs). Skill precedence per source (crates/goose/src/skills/mod.rs, all_skill_dirs_with_config + scan_skills_from_dir): project dirs scanned before global dirs, first-seen skill name wins (project shadows global); built-ins are appended last and only if not shadowed; docs order files as .agents/skills > .goose/skills > .claude/skills. Hints require goose's Developer extension to be enabled, per the docs page. Hints/load_hints.rs confirms global = Paths::in_config_dir(name) for every configured filename, plus home .agents/AGENTS.md; local = git-root-to-cwd walk, nested subdir hints limited to the working-dir subtree and only for dirs goose accesses via tool args.
