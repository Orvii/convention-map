# Crush

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `.github/copilot-instructions.md` | project | Part of defaultContextPaths, resolved relative to the project working dir and loaded fully; all matching context files are concatenated into the system prompt (no file wins over another). Paths are sorted alphabetically, then deduped; extra paths appended via options.context_paths. No parent-directory walk for context files. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L29-L46) |
| `.cursorrules` | project | Same defaultContextPaths list; loaded in full alongside all other matching context files. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L29-L46) |
| `.cursor/rules/` | project | Directory entry: every file inside is walked recursively and loaded (docs/config/README documents option reset context-path; code walks DirEntry). Loaded in full. | [src](https://github.com/charmbracelet/crush/blob/main/internal/agent/prompt/prompt.go#L111-L140) |
| `CLAUDE.md` | project | Read for Claude Code compatibility; loaded in full alongside the other defaults. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L29-L46) |
| `CLAUDE.local.md` | project | Companion of CLAUDE.md; loaded in full. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L29-L46) |
| `GEMINI.md` | project | Read for Gemini CLI compatibility; loaded in full. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L29-L46) |
| `gemini.md` | project | Lowercase case-variant; loaded in full. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L29-L46) |
| `crush.md` | project | Crush's own convention; loaded in full. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L29-L46) |
| `crush.local.md` | project | Loaded in full. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L29-L46) |
| `Crush.md` | project | Case-variant; loaded in full. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L29-L46) |
| `Crush.local.md` | project | Case-variant; loaded in full. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L29-L46) |
| `CRUSH.md` | project | Case-variant; loaded in full. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L29-L46) |
| `CRUSH.local.md` | project | Case-variant; loaded in full. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L29-L46) |
| `AGENTS.md` | project | Cross-tool standard file; also the default filename Crush writes on project init (initialize_as, default AGENTS.md). Loaded in full. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L26-L46) |
| `agents.md` | project | Case-variant; loaded in full. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L29-L46) |
| `Agents.md` | project | Case-variant; loaded in full. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config.go#L29-L46) |
| `~/.config/crush/CRUSH.md (i.e. <crush config dir>/CRUSH.md; CRUSH_GLOBAL_CONFIG relocates the dir)` | global | Default GlobalContextPaths when unset. Crush-specific personal rules. Both global files are injected into the prompt in a separate 'User context' section (after 'Project-Specific Context'); it does not override project files, both are included. Customizable via option global-context-path (repeatable; directories walked recursively). | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L577-L585) |
| `~/.config/AGENTS.md (parent of the crush config dir)` | global | Default GlobalContextPaths when unset; meant for instructions shared with other agentic tools. Both global files are concatenated into the prompt's user-context section. | [src](https://github.com/charmbracelet/crush/blob/main/README.md#L533-L554) |
| `.crushrc` | project | Config discovery walks up from cwd but stops at the git worktree root. Within a directory: .crushrc > crushrc > .crush.json > crush.json (later-reversed merge makes earliest listed name win). Project config overrides global. New/primary bash-based format (JSON is legacy). | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L942-L985) |
| `crushrc` | project | Second priority within a directory; loses to .crushrc, beats both JSON configs. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L942-L985) |
| `.crush.json` | project | Legacy JSON (deprecated but supported); beats crush.json, loses to crushrc/.crushrc in same directory. Deprecation documented in docs/config/README. | [src](https://github.com/charmbracelet/crush/blob/main/docs/config/README.md#L86-L104) |
| `crush.json` | project | Lowest in-directory priority; everything is merged with project overriding global. | [src](https://github.com/charmbracelet/crush/blob/main/docs/config/README.md#L86-L104) |
| `$XDG_CONFIG_HOME/crush/crushrc (~/.config/crush/crushrc)` | global | Global user config; a crushrc sibling is picked up next to the global crush.json location. Project settings override global ones. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L946-L950) |
| `$XDG_CONFIG_HOME/crush/crush.json (~/.config/crush/crush.json; CRUSH_GLOBAL_CONFIG overrides the directory)` | global | Global user-level config, always included regardless of the git-root boundary. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1211-L1217) |
| `$XDG_DATA_HOME/crush/crush.json (~/.local/share/crush/crush.json; CRUSH_GLOBAL_DATA overrides)` | global | Machine-owned data JSON, merged as config but never executed as Bash; no crushrc is discovered/executed from data dirs. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1257-L1267) |
| `/etc/crush/crush.json (Windows: none)` | global | System-wide config loaded at the lowest priority so user and project configs override it. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/config_unix.go#L5-L7) |
| `<filename set by initialize_as option, default AGENTS.md> (created/updated by crush init, then read as a normal project context file)` | project | Not an extra load source: defines which context file init writes. Init is offered only when NO default context file already exists in the working dir. Option docs: docs/config/README.md. | [src](https://github.com/charmbracelet/crush/blob/main/internal/config/init.go#L44-L85) |

## Skill directories discovered

- `$CRUSH_SKILLS_DIR (env var; if set, it REPLACES all default global skill dirs)` — [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1365-L1368)
- `$XDG_CONFIG_HOME/crush/skills (~/.config/crush/skills)` — [src](https://github.com/charmbracelet/crush/blob/main/README.md#L609-L614)
- `$XDG_CONFIG_HOME/agents/skills (~/.config/agents/skills)` — [src](https://github.com/charmbracelet/crush/blob/main/README.md#L609-L614)
- `~/.agents/skills (per the Agent Skills spec, agentskills.io)` — [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1370-L1376)
- `~/.claude/skills` — [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1370-L1376)
- `%LOCALAPPDATA%\crush\skills (Windows only)` — [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1378-L1389)
- `%LOCALAPPDATA%\agents\skills (Windows only)` — [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1378-L1389)
- `<project working dir>/.agents/skills` — [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1395-L1425)
- `<project working dir>/.crush/skills` — [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1395-L1425)
- `<project working dir>/.claude/skills` — [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1395-L1425)
- `<project working dir>/.cursor/skills` — [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1395-L1425)
- `<git worktree root>/.agents/skills (monorepo-level; working-dir paths come first so local skills take precedence)` — [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1395-L1425)
- `<git worktree root>/.crush/skills (monorepo-level)` — [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1395-L1425)
- `<git worktree root>/.claude/skills (monorepo-level)` — [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1395-L1425)
- `<git worktree root>/.cursor/skills (monorepo-level)` — [src](https://github.com/charmbracelet/crush/blob/main/internal/config/load.go#L1395-L1425)
- `Extra dirs from options.skills_paths / `option skill-path` (docs/config/README documents the four auto-loaded project subdirs needing no option)` — [src](https://github.com/charmbracelet/crush/blob/main/docs/config/README.md#L496-L498)

## Learned memory

None — Crush has no built-in learned/auto memory: no memories directory, no memory-writing tool, and no memory config key; the only "memory" occurrences in the repo are in-process runtime state and a FUTURE.md idea using "memory" to mean session-only, non-persisted config changes.

[src](https://github.com/charmbracelet/crush/blob/main/docs/config/FUTURE.md#L131-L137)

## Compatibility notes

Compatibility: Crush deliberately reads other vendors' convention files — Claude (CLAUDE.md, CLAUDE.local.md, ~/.claude/skills), Cursor (.cursorrules, .cursor/rules/, .cursor/skills), Gemini (GEMINI.md/gemini.md), GitHub Copilot (.github/copilot-instructions.md) — plus its own crush.md/CRUSH.md/*.local.md and the cross-tool AGENTS.md + Agent Skills spec (~/.agents/skills, SKILL.md folders, agentskills.io). Two-tier global context: ~/.config/crush/CRUSH.md for Crush-specific rules, ~/.config/AGENTS.md for instructions shared with other tools. No precedence/override among context files: every matching file is read and concatenated (project files in a "Project-Specific Context" block, global files in a "User context" block of the same system prompt); paths are alphabetically sorted and deduped, dirs under a context path are walked recursively, and ~/env vars are expanded. Context files are only looked up in the working dir (plus explicit context_paths) — unlike config files, which walk up from cwd and stop at the git worktree root so a stray crush.json above the repo is ignored. Config precedence is documented: project overrides global; in a directory .crushrc > crushrc > .crush.json > crush.json; /etc/crush/crush.json is lowest. crush.json is deprecated in favor of executable bash crushrc. `crush init` is only offered when no default context file already exists in the working dir; it writes initialize_as (default AGENTS.md) and then that file is read as a normal project context file. Builtin skills are embedded in the binary (internal/skills/builtin), user skill discovery honors $CRUSH_SKILLS_DIR as a full override of the global default dirs, and skills are deduplicated with working-dir versions taking precedence over git-root ones. Evidence fetched during research from a fresh clone of charmbracelet/crush @ main (commit 8da349060b7df148d209979be0a5e9c9281d1f15, 2026-10-04) and raw.githubusercontent.com URLs verified HTTP 200.
