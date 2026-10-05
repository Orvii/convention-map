# Cursor

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `AGENTS.md` | project (repository root) | Nested AGENTS.md files in subdirectories are combined with parent directories, with more specific (deeper) instructions taking precedence. Docs call AGENTS.md a simpler alternative to .cursor/rules; no precedence is documented between AGENTS.md and .cursor/rules when both exist. | [src](https://cursor.com/docs/rules) |
| `<subdirectory>/AGENTS.md` | project (any subdirectory of the repository) | Automatically applied when working with files in that directory or its children; combined with parent directories, more specific instructions win. | [src](https://cursor.com/docs/rules) |
| `.cursor/rules/*.mdc` | project (version-controlled) | Rules are applied in order Team Rules -> Project Rules -> User Rules; all applicable rules are merged and earlier sources take precedence when guidance conflicts. Project rules must use the .mdc extension; plain .md files in .cursor/rules are ignored. | [src](https://cursor.com/docs/rules) |
| `User Rules (not stored on the file system; defined in Customize -> Rules)` | user (global across all projects) | Lowest of the rule sources (Team -> Project -> User). Used by Agent (Chat); not applied to Inline Edit (Cmd/Ctrl+K). | [src](https://cursor.com/docs/rules) |
| `Team Rules (not file-based; created from the Cursor dashboard)` | team (Team and Enterprise plans) | Take precedence over Project Rules and User Rules; enforced rules cannot be disabled by members. | [src](https://cursor.com/docs/rules) |
| `<project-root>/.cursor/hooks.json` | project | Hook response merging priority (highest to lowest): Enterprise -> Team -> Project -> User. Deny wins over ask; ask wins over allow regardless of source. | [src](https://cursor.com/docs/hooks) |
| `~/.cursor/hooks.json` | user (global on the local machine) | Lowest in hook priority order; not available to Cloud Agents (cloud VMs have no access to the local home directory). | [src](https://cursor.com/docs/hooks) |
| `/Library/Application Support/Cursor/hooks.json (macOS); /etc/cursor/hooks.json (Linux/WSL); C:\ProgramData\Cursor\hooks.json (Windows)` | enterprise (MDM-managed, system-wide) | Highest priority hook source. | [src](https://cursor.com/docs/hooks) |
| `Team hooks (not file-based; configured in the web dashboard, cloud-distributed to members)` | enterprise/team | Second in priority order, above Project and User hooks. | [src](https://cursor.com/docs/hooks) |
| `.cursor/agents/*.md (custom subagents)` | project | Project subagents take precedence over user subagents when names conflict; .cursor/ takes precedence over .claude/ or .codex/ for same-named agents. | [src](https://cursor.com/docs/subagents) |
| `.claude/agents/ (custom subagents, Claude compatibility)` | project | Lower precedence than .cursor/agents/ for same-named subagents. | [src](https://cursor.com/docs/subagents) |
| `.codex/agents/ (custom subagents, Codex compatibility)` | project | Lower precedence than .cursor/agents/ for same-named subagents. | [src](https://cursor.com/docs/subagents) |
| `~/.cursor/agents/ (custom subagents)` | user (all projects for current user) | Project subagents take precedence when names conflict. | [src](https://cursor.com/docs/subagents) |
| `~/.claude/agents/ (custom subagents, Claude compatibility)` | user | Project subagents take precedence when names conflict. | [src](https://cursor.com/docs/subagents) |
| `~/.codex/agents/ (custom subagents, Codex compatibility)` | user | Project subagents take precedence when names conflict. | [src](https://cursor.com/docs/subagents) |
| `.cursor/mcp.json` | project | — | [src](https://cursor.com/docs/mcp) |
| `~/.cursor/mcp.json` | user (global) | — | [src](https://cursor.com/docs/mcp) |
| `.cursor-plugin/plugin.json (Cursor Plugin manifest)` | plugin (installed via Cursor Marketplace or team marketplaces; components apply at user/team/workspace level) | Manifest component paths (rules/agents/skills/commands/hooks/mcpServers) replace folder-based discovery for that component when specified. | [src](https://cursor.com/docs/reference/plugins) |
| `plugin.json (Agent Plugins open-standard manifest at plugin root)` | plugin | Defines portable skills and MCP servers only; Cursor Plugins format supports the full component set (rules, agents, commands, hooks). | [src](https://cursor.com/docs/reference/plugins) |
| `.cursor-plugin/marketplace.json (multi-plugin repository manifest, repo root)` | plugin (marketplace) | Per-plugin manifest values take precedence when merged with a marketplace entry. | [src](https://cursor.com/docs/reference/plugins) |
| `rules/ (inside a Cursor Plugin; .md, .mdc, or .markdown files)` | plugin | Installed plugin rules appear in Customize alongside other rules; no precedence versus file-based rules is documented. | [src](https://cursor.com/docs/reference/plugins) |
| `agents/ (inside a Cursor Plugin; .md, .mdc, or .markdown files)` | plugin | — | [src](https://cursor.com/docs/reference/plugins) |
| `commands/ (inside a Cursor Plugin; .md, .mdc, .markdown, or .txt files)` | plugin | — | [src](https://cursor.com/docs/reference/plugins) |
| `hooks/hooks.json (inside a Cursor Plugin)` | plugin | — | [src](https://cursor.com/docs/reference/plugins) |
| `mcp.json (at plugin root)` | plugin | — | [src](https://cursor.com/docs/reference/plugins) |

## Skill directories discovered

- `.agents/skills/` — [src](https://cursor.com/docs/skills)
- `.cursor/skills/` — [src](https://cursor.com/docs/skills)
- `~/.agents/skills/` — [src](https://cursor.com/docs/skills)
- `~/.cursor/skills/` — [src](https://cursor.com/docs/skills)
- `.claude/skills/` — [src](https://cursor.com/docs/skills)
- `.codex/skills/` — [src](https://cursor.com/docs/skills)
- `~/.claude/skills/` — [src](https://cursor.com/docs/skills)
- `~/.codex/skills/` — [src](https://cursor.com/docs/skills)
- `<anywhere-in-repo>/.cursor/skills/ or <anywhere-in-repo>/.agents/skills/ (nested skill directories; Cursor walks the skills root recursively for SKILL.md)` — [src](https://cursor.com/docs/skills)
- `skills/ (inside a plugin; each subdirectory containing a SKILL.md)` — [src](https://cursor.com/docs/reference/plugins)
- `SKILL.md at plugin root (single-skill plugin, only if no skills/ dir and no manifest skills field)` — [src](https://cursor.com/docs/reference/plugins)

## Learned memory

The only persistent cross-session agent memory Cursor documents is for Cloud Agent automations: each automation gets "Memories", where the agent can read and write persistent notes across runs. A memory is stored as a named entry (MEMORIES.md by default) that exists outside the agent's working filesystem, is enabled by default and can be disabled, and can be viewed, edited, or deleted from the automation's tool configuration UI. Memories are per-automation and persist across runs. For the IDE/CLI Agent, no cross-session memory store or memory file is documented (not documented).

[src](https://cursor.com/docs/cloud-agent/automations)

## Compatibility notes

Cursor's documented convention surface spans four rule types (Project Rules, User Rules, Team Rules, AGENTS.md), Agent Skills, subagents, hooks, plugins, and MCP. The built-in system prompt itself is not file-configurable: the context breakdown describes "System prompt" as Cursor's built-in instructions, while rules, skills, MCP, and subagents are separate injected categories (https://cursor.com/docs/agent/prompting). CLAUDE.md as an instruction file is not documented anywhere in the docs; Claude compatibility appears only as read directories (.claude/skills/, .claude/agents/, ~/.claude/skills/, ~/.claude/agents/), the CLAUDE_PLUGIN_ROOT variable in plugin MCP configs, and the CLAUDE_PROJECT_DIR hook environment alias.

Cloud sessions vs local surfaces. Cloud Agents read AGENTS.md from the repository (docs recommend a "Cursor Cloud specific instructions" section), and read rules from all three levels (user, team, repo .cursor/rules/*.mdc). Project skills committed to the repo are available to cloud agents; personal skills in ~/.cursor/skills/ reach the cloud only when "Sync Skills for Cloud Agents" is enabled (only ~/.cursor/skills/ syncs - project skills, ~/.agents/skills/, and other local files stay on the machine), and self-hosted workers use project skills or skills baked into the worker image. Cloud agents run command-based hooks from <project-root>/.cursor/hooks.json plus, on Enterprise, team and enterprise-managed hooks; user-level ~/.cursor/hooks.json is not available in cloud agents, Tab hooks and workspaceOpen do not apply, and sessionEnd/sessionStart semantics differ. Docs state subagents are usable in the editor, CLI, and Cloud Agents, but which custom subagent directories cloud sessions pick up is not documented. User-level skills sync is admin-gated: Team/Enterprise admins can disable "Sync Skills for Cloud Agents" for everyone. Skills can be published to a team marketplace, which stores a Cursor-hosted copy separate from the local sync.

Precedence across categories: rules use Team -> Project -> User; hooks merge Enterprise -> Team -> Project -> User; subagents resolve project-over-user and .cursor/ over .claude//.codex/; precedence among skill directories (e.g., .cursor/skills vs .agents/skills, or project vs user skills) is not documented, and plugin-provided rules have no documented rank versus file-based rules. Also not documented: a user-level AGENTS.md (docs limit AGENTS.md to project root and subdirectories), any legacy .cursorrules support, a standalone filesystem path for user/workspace slash commands (command files are documented only inside plugins at commands/), and a memory file for the IDE/CLI agent. CLI configuration (~/.cursor/cli-config.json globally, <project>/.cursor/cli.json for permissions only) holds settings and permissions rather than instructions, so it is listed here only for completeness (https://cursor.com/docs/cli/reference/configuration). Plugins ship as git repositories discovered through .cursor-plugin/marketplace.json or the Cursor Marketplace; Cursor expands ${CURSOR_PLUGIN_ROOT} and ${CLAUDE_PLUGIN_ROOT} but not the Agent Plugins ${PLUGIN_ROOT}/${PLUGIN_DATA} variables.
