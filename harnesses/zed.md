# Zed

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `~/.config/zed/AGENTS.md` | global | Personal instructions, loaded for every project; project instruction file overrides it when they conflict. Windows equivalent: %APPDATA%\Zed\AGENTS.md. | [src](https://zed.dev/docs/ai/instructions) |
| `<project>/.rules` | project | First entry in the documented priority list; Zed uses the FIRST matching file only, so .rules beats every file below it. | [src](https://zed.dev/docs/ai/instructions) |
| `<project>/.cursorrules` | project | Second in priority list; used only if no .rules exists (first match wins). | [src](https://zed.dev/docs/ai/instructions) |
| `<project>/.windsurfrules` | project | Third in priority list; used only if nothing earlier matches. | [src](https://zed.dev/docs/ai/instructions) |
| `<project>/.clinerules` | project | Fourth in priority list; used only if nothing earlier matches. | [src](https://zed.dev/docs/ai/instructions) |
| `<project>/.github/copilot-instructions.md` | project | Fifth in priority list; loaded as 'compatible project instructions' by Zed Agent. | [src](https://zed.dev/docs/ai/instructions) |
| `<project>/AGENT.md` | project | Sixth in priority list; only used if nothing earlier matches. | [src](https://zed.dev/docs/ai/instructions) |
| `<project>/AGENTS.md` | project | Primary documented file, but only seventh in the first-match priority list — .rules/.cursorrules/.windsurfrules/.clinerules/copilot-instructions/AGENT.md all win over it when present. | [src](https://zed.dev/docs/ai/instructions) |
| `<project>/CLAUDE.md` | project | Eighth in priority list; loaded as compatible project instructions by Zed Agent. Never overrides AGENTS.md. | [src](https://zed.dev/docs/ai/instructions) |
| `<project>/GEMINI.md` | project | Ninth (last) in priority list; used only if none of the other eight project files exist. | [src](https://zed.dev/docs/ai/instructions) |

## Skill directories discovered

- `~/.agents/skills` — [src](https://zed.dev/docs/ai/skills)
- `<project>/.agents/skills` — [src](https://zed.dev/docs/ai/skills)

## Learned memory

None — Zed has no built-in learned/auto memory: agent context comes only from instructions, skills, profiles, and MCP, and persistence is per-thread (archived thread history, auto-compaction summaries, @-mentioning past threads), with no memories directory or cross-session memory store documented anywhere in the docs.

[src](https://zed.dev/docs/ai/agent-panel)

## Compatibility notes

Zed is aggressively compatibility-focused for instructions: the Zed Agent reads six other vendors' project files (.rules, .cursorrules, .windsurfrules, .clinerules, .github/copilot-instructions.md, CLAUDE.md, GEMINI.md) plus AGENT.md/AGENTS.md, but only ONE project file is ever used — the first match in the documented priority order — so e.g. an existing .rules or .cursorrules silently beats AGENTS.md/CLAUDE.md. Skills follow the external agentskills.io spec, not Claude's: loaded ONLY from ~/.agents/skills (global) and <project>/.agents/skills (project-local; flat children only, symlinks allowed, 50KB catalog cap, no custom search paths) — a .claude/skills dir is NOT read; same-name project skill overrides global. No opencode.json/kilo.jsonc/crush file support (MCP lives in Zed's own settings.json). Legacy Rules Library was replaced by Skills + Instructions (project .rules kept as compat); rules have been dropped from new agent requests. All of this applies to Zed's native Zed Agent only — External Agents (Claude Code, Codex, OpenCode etc. over ACP) and Terminal Threads own their native config and are explicitly not controlled by Zed's instruction loader.
