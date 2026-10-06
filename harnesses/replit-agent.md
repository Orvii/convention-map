# Replit Agent

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `replit.md (project root)` | project | Automatically read when Agent handles requests; precedence versus Workspace Custom Instructions is not documented. | [src](https://docs.replit.com/features/project-setup/replit-dot-md) |
| `Workspace Settings -> Customization (Custom Instructions)` | team | Loads on every message across Workspace Projects. Explicit requests and Custom Instructions take priority over Memories; conflict ordering versus replit.md is not documented. | [src](https://docs.replit.com/features/agent/agent-customization) |

## Skill directories discovered

- `/.agents/skills` — [src](https://docs.replit.com/features/agent/skills-directory)
- `.local/secondary_skills/` — [src](https://docs.replit.com/features/agent/skills-directory)

## Learned memory

Replit can write and maintain Memories during work: user memory captures durable preferences and working style for one builder and workspace, while project memory stores conventions, gotchas, and fixes for one Project and is retrieved when relevant. Memories exclude personal or sensitive information, including sensitive traits, third-party personal data, credentials, and project-confidential facts; they are private by default, with collaborator sharing off by default. Explicit requests and Custom Instructions take priority over memory.

[src](https://docs.replit.com/chat/memories)

## Compatibility notes

Replit says skills follow the Agent Skills specification, but does not promise cross-agent compatibility. The docs specify that Custom Instructions outrank Memories but leave conflicts between Custom Instructions and replit.md undocumented. The .replit documentation describes app behavior configuration, not an Agent instruction carrier. AGENTS.md and GitHub skill import are not documented in the checked instruction and skills pages.
