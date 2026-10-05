# Kilo Code

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `AGENTS.md` | project | Primary instruction file. Auto-discovered at project root and in parent dirs via findUp; also loaded per-subdirectory on demand when the Read tool touches a file there (injected as context tags). Documented priority order: 1 agent prompt > 2 project kilo.jsonc `instructions` > 3 project AGENTS.md > 4 global kilo.jsonc `instructions`. Always loaded if present — cannot be individually disabled. | [src](https://kilocode.ai/docs/customize/agents-md) |
| `AGENT.md` | project | Singular fallback filename, lower precedence than AGENTS.md. Both are write-protected (agent needs approval to edit). Uppercase required. | [src](https://kilocode.ai/docs/customize/agents-md) |
| `CLAUDE.md` | project | Read for Claude Code compatibility; project-level CLAUDE.md keeps working permanently (unaffected by Claude Code Migration). | [src](https://kilocode.ai/docs/customize/custom-instructions) |
| `~/.claude/CLAUDE.md` | global | Claude-compatible global fallback, loaded until Claude Code Migration (Settings -> Experimental, off by default) has been attempted. Migration imports it into ~/.config/kilo/AGENTS.md; after the attempt Kilo stops loading global Claude instructions. | [src](https://kilocode.ai/docs/customize/custom-instructions) |
| `~/.config/kilo/AGENTS.md` | global | Global instructions file. Project-level instructions are loaded before global and take precedence for conflicting directives. | [src](https://kilocode.ai/docs/customize/custom-instructions) |
| `CONTEXT.md` | project | Listed as an additional auto-discovered project context file alongside AGENTS.md and CLAUDE.md. | [src](https://kilocode.ai/docs/customize/custom-instructions) |
| `kilo.jsonc (project root) or .kilo/kilo.jsonc` | project | Its `instructions` array (file paths, globs, URLs) defines project rules; documented priority 2 — outranks AGENTS.md. `.kilo/kilo.jsonc` takes priority if both exist. Files matched by globs load in filesystem order. Config may also be .kilo/agents/*.md and .kilo/command/*.md territory — those are separate features. | [src](https://kilocode.ai/docs/customize/custom-rules) |
| `~/.config/kilo/kilo.jsonc` | global | Global `instructions` array; documented priority 4. Rules load in array order: global first, then project; on conflicting directives project-level wins. | [src](https://kilocode.ai/docs/customize/custom-rules) |
| `.kilo/rules/*.md, .kilo/rules-{mode}/*.md (e.g. rules-code, rules-debug, rules-ask)` | project | Conventional rule directory; mode-specific subdirs scope rules to a mode. Current docs reference these files through the `instructions` key (e.g. ".kilo/rules/*.md"); the VSCode-era docs treat placement in .kilo/rules/ as auto-applied. | [src](https://kilocode.ai/docs/getting-started/migrating) |
| `~/.kilo/rules/*.md` | global | Global rules stored as files in home folder (global equivalents of .kilo/rules/). | [src](https://kilocode.ai/docs/getting-started/migrating) |
| `.kilocode/rules/ (incl. .kilocode/rules/memory-bank/ and .kilo/rules/memory-bank/)` | project | Legacy VSCode-extension rules dir; contents automatically included for backward compatibility. Deprecated memory-bank rule files under it still load, but memory bank is deprecated in favor of AGENTS.md. | [src](https://kilocode.ai/docs/customize/custom-rules) |
| `~/.kilocode/rules/` | global | Legacy global rules dir of the old VSCode extension; loaded first, project rules take precedence on conflict. | [src](https://github.com/Kilo-Org/kilocode-legacy/blob/main/docs/legacy-ides/customize/custom-rules.md) |
| `.kilocoderules` | project | Legacy single-file rules from the VSCode extension; still loaded via auto-migration. | [src](https://kilocode.ai/docs/customize/custom-instructions) |
| `.roorules, .clinerules` | project | Legacy fallback rule files (Roo Code / Cline heritage), lowest priority after global and project rule dirs. | [src](https://github.com/Kilo-Org/kilocode-legacy/blob/main/docs/legacy-ides/customize/custom-rules.md) |
| `opencode.json, opencode.jsonc, config.json, kilo.json (same global and project locations)` | both | If present in ~/.config/kilo/ or project, Kilo reads and deep-merges them alongside kilo.jsonc (opencode heritage: CLI is a fork of opencode). But .opencode/ directories are no longer read — config must live in ~/.config/kilo/ and ./.kilo/. | [src](https://kilocode.ai/docs/getting-started/settings) |

## Skill directories discovered

- `.kilo/skills/<name>/SKILL.md` — [src](https://kilocode.ai/docs/customize/skills)
- `~/.kilo/skills/<name>/SKILL.md (Windows: \Users\<user>\.kilo\skills\<name>\SKILL.md)` — [src](https://kilocode.ai/docs/customize/skills)
- `.agents/skills/ (project)` — [src](https://kilocode.ai/docs/customize/skills)
- `~/.agents/skills/ (user-level; discovered by default, no config needed)` — [src](https://kilocode.ai/docs/customize/skills)
- `.claude/skills/ (project)` — [src](https://kilocode.ai/docs/customize/skills)
- `~/.claude/skills/ (user-level)` — [src](https://kilocode.ai/docs/customize/skills)
- `skills.paths entries in kilo.jsonc (absolute, ~/-relative, or project-relative paths)` — [src](https://kilocode.ai/docs/customize/skills)
- `skills.urls remote skill directories (must serve index.json manifest)` — [src](https://kilocode.ai/docs/customize/skills)

## Learned memory

Kilo has built-in opt-in project memory ("Kilo Memory"): disabled by default, enabled per project, stored outside the repo at ~/.local/share/kilo/memory/<project>/ as project.md, environment.md, corrections.md plus saved session digests (auto-save on by default, extractable via kilo_memory_save/kilo_memory_recall and /memory commands); the older rule-file Memory Bank (.kilo/rules/memory-bank/) is deprecated in favor of AGENTS.md.

[src](https://kilocode.ai/docs/customize/context/memory)

## Compatibility notes

Compatibility-heavy harness. Reads other vendors' files: project CLAUDE.md and CONTEXT.md, plus .claude/ and .agents/ directories (Claude Code and open-agent standard compat). Legacy support kept: .kilocoderules, .roorules, .clinerules rule files and .kilocode/rules/ dirs (auto-included). opencode config files (opencode.json/opencode.jsonc/config.json) are still deep-merged, but the .opencode directories themselves are no longer read. Does NOT auto-load GEMINI.md, CRUSH.md, .cursorrules or .windsurfrules — cursor/windsurf migration docs instruct users to copy those files into .kilo/rules/ manually. Two doc generations coexist on the site: the file-scan rules model (.kilo/rules/ dirs, mode dirs, ~/.kilo/rules/) and the newer config-driven model (instructions key in kilo.jsonc); documented precedence in both: agent prompt > project instructions > project AGENTS.md > global instructions, project beats global on conflicts, AGENTS.md unsuppressable. External skill dirs (.claude/skills, .agents/skills) can be disabled with KILO_DISABLE_EXTERNAL_SKILLS=true; .claude/skills loads only when Claude Code Compatibility is enabled. Skill name conflicts: project .kilo/skills wins over ~/.kilo/skills. Claude Code Migration (off by default) imports ~/.claude/CLAUDE.md, standalone ~/.claude/skills SKILL.md dirs, and MCP servers from ~/.claude.json once, then stops the global Claude fallback.
