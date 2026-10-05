# GitHub Copilot CLI

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `$HOME/.copilot/copilot-instructions.md (or $COPILOT_HOME/copilot-instructions.md)` | global | User-level instructions, applied across repositories/all sessions. COPILOT_HOME replaces ~/.copilot for both user-level instruction locations. No general precedence order is defined between instruction files: CLI combines all applicable user-level + repository + agent instructions and only de-duplicates identical copies; /instructions lists what was loaded and can disable files. | [src](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) |
| `$HOME/.copilot/instructions/**/*.instructions.md` | global | Modular user-level instruction files; loaded alongside copilot-instructions.md, apply to all sessions. | [src](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) |
| `.github/copilot-instructions.md` | project | Repository-wide instructions, discovered in the standard locations: repo root, current working directory, intermediate directories between them, and directories nested in the path of a file the CLI is working on. Supports @-relative-path imports of other in-repo files. | [src](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) |
| `.github/instructions/**/*.instructions.md` | project | Path-specific modular instructions: included only when the file's frontmatter applyTo glob matches a file Copilot CLI is working with. Discovered in standard locations but NOT intermediate directories. Not expanded for @-imports. excludeAgent frontmatter can hide them from cloud agent / code review. | [src](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) |
| `AGENTS.md` | project | Agent instructions, discovered in the standard locations (repo root, cwd, intermediate dirs, dirs nested in the path of a file it works on). Supports @-relative-path imports. | [src](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) |
| `CLAUDE.md (and .claude/CLAUDE.md)` | project | Anthropic-format agent instructions read first-class, discovered in the standard locations; Copilot CLI additionally uses .claude/CLAUDE.md. Supports @-relative-path imports. | [src](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) |
| `GEMINI.md` | project | Google-format agent instructions read first-class, discovered in the standard locations. @-file references are NOT expanded in GEMINI.md. | [src](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) |
| `Directories listed in COPILOT_CUSTOM_INSTRUCTIONS_DIRS (additional AGENTS.md and *.instructions.md files)` | both | Env var (comma-separated dirs) adds extra locations for AGENTS.md and *.instructions.md beyond the standard discovery locations. | [src](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) |

## Skill directories discovered

- `.github/skills/<skill-name>/SKILL.md` — [src](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
- `.claude/skills/<skill-name>/SKILL.md` — [src](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
- `.agents/skills/<skill-name>/SKILL.md` — [src](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
- `~/.copilot/skills/<skill-name>/SKILL.md` — [src](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference)
- `~/.agents/skills/<skill-name>/SKILL.md` — [src](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
- `Additional directories configured via the skillDirectories setting (plus /skills add and copilot skill add)` — [src](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference)

## Learned memory

Built-in learned memory exists: "Copilot Memory" (public preview, paid plans) server-side remembers repository-level facts and user-level preferences across features, managed in Copilot CLI via the /memory on|off|show command with memory writes gated by a "memory" permission kind; unused entries auto-delete after 28 days. No local memories directory is documented.

[src](https://docs.github.com/en/copilot/concepts/agents/copilot-memory)

## Compatibility notes

Compatibility: reads other vendors' agent files first-class — CLAUDE.md (incl. .claude/CLAUDE.md), GEMINI.md, and the open AGENTS.md standard; project skills are discovered from .claude/skills too, so Claude Code repo skills are picked up automatically, and the CLI also reads .claude/settings.json / .claude/settings.local.json for a shared cross-tool subset (companyAnnouncements, disableAllHooks, enabledPlugins, extraKnownMarketplaces, hooks). It does NOT document loading Cursor/Windsurf/opencode/kilo conventions (.cursorrules, opencode.json, kilo.jsonc): the supported-locations table in the add-custom-instructions doc is the definitive list. Precedence: no general order between instruction files (combined, identical duplicates removed; avoid conflicts), while for skills project-level takes precedence over personal-level on same name. Instruction edits need a new/resumed session; /instructions and /skills list what loaded. Adjacent loaded artifacts not counted as instruction files: custom agents at .github/agents/*.agent.md (project, takes precedence) and ~/.copilot/agents/*.agent.md (personal), MCP configs (.mcp.json, .github/mcp.json, ~/.copilot/mcp-config.json), hooks (.github/hooks/, ~/.copilot/hooks/, settings hooks key), and settings files .github/copilot/settings.json + settings.local.json + ~/.copilot/settings.json.
