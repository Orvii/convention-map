# Qodo

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `AGENTS.md` | not documented | The overview says to add the Default template to the appropriate agent instruction file; precedence against other instructions is not documented. | [src](https://docs.qodo.ai/agentic-toolbox/agentic-toolbox-overview) |
| `CLAUDE.md` | not documented | The overview names this as an example instruction file for the Default template; precedence against other instructions is not documented. | [src](https://docs.qodo.ai/agentic-toolbox/agentic-toolbox-overview) |
| `Default template (no filesystem path documented)` | not documented | Agents are directed to read the template and add its instructions to the appropriate agent instruction file; conflict ordering is not documented. | [src](https://docs.qodo.ai/agentic-toolbox/agentic-toolbox-overview) |
| `SKILL.md definitions` | not documented | Listed as an input to rule discovery and refinement; ordering or conflict behavior is not documented. | [src](https://docs.qodo.ai/core-concepts/context-engine) |
| `Review Standards (no file path documented)` | workspace | Standards can be workspace-wide or repository-scoped; precedence among rules is not documented. | [src](https://docs.qodo.ai/agentic-toolbox/manage-standards) |
| `.pr_agent.toml` | project (repository/project-group; organization-level settings also documented) | Repository-local settings override project and organization settings; the complete ordering across all sources is not documented. Its applicability to Agentic Toolbox is not specified. | [src](https://docs.qodo.ai/configuration/configuration-file) |

## Skill directories discovered

none documented.

## Learned memory

The Context Engine gathers and reasons over context from repositories, pull requests, organizational rules, and development workflows. The documentation does not specify durable-memory guarantees, retention periods, or memory file paths.

[src](https://docs.qodo.ai/core-concepts/context-engine)

## Compatibility notes

Qodo exposes managed skills to compatible host agents over MCP, and its CLI installer configures skills for supported agent environments, but no filesystem skill-directory paths are documented; local Agentic Toolbox installation is not required for MCP use. The overview directs users to place Qodo instructions in AGENTS.md or CLAUDE.md, but does not define precedence against host instructions. Agentic Toolbox is described as separate from deprecated Qodo Command CLI (@qodo/command) and Qodo Gen CLI; installing it replaces an existing Qodo Command installation, but the docs do not specify affected instruction or skill paths.
