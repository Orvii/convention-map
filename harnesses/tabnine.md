# Tabnine

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `/.tabnine/guidelines/` | user | Organization guidelines override personal guidelines; precedence against project guidelines is not documented. | [src](https://docs.tabnine.com/main/getting-started/tabnine-agent/guidelines.md) |
| `$PROJECT_FOLDER/.tabnine/guidelines/appguidelines.md` | project | Project-guideline precedence is not documented. | [src](https://docs.tabnine.com/main/getting-started/tabnine-agent/guidelines.md) |
| `Admin Console -> Agent Guidelines -> General Guideline` | enterprise | Applies to organization users and projects; overrides personal guidelines. | [src](https://docs.tabnine.com/main/getting-started/tabnine-agent/guidelines.md) |
| `Organization instructions (CLI; no local file path documented)` | enterprise | Fetched into the authenticated CLI session; ordering against other instruction sources is not documented. | [src](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/agent-guidelines-cli.md) |
| `Service-account instructions (CLI; no local file path documented)` | team | Fetched when configured for the authenticated service account; scope classification and ordering are not documented. | [src](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/agent-guidelines-cli.md) |
| `Coaching Guidelines tool (CLI; no file path documented)` | team | Provides language-specific rules when enabled and supported; ordering is not documented. | [src](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/agent-guidelines-cli.md) |

## Skill directories discovered

- `~/.tabnine/agent/skills/<name>/` — [src](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/agent-skills.md)
- `~/.agents/skills/<name>/` — [src](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/agent-skills.md)
- `<project>/.tabnine/agent/skills/<name>/` — [src](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/agent-skills.md)
- `<project>/.agents/skills/<name>/` — [src](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/agent-skills.md)
- `~/.tabnine/extensions/<extension-name>/ (extension install location; skill discovery path not documented)` — [src](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/extensions.md)

## Learned memory

Learned memory or persistent user preferences are not documented. When enabled, CLI checkpointing saves project-file snapshots in a shadow Git repository and conversation and pending-tool-call JSON in the project's temporary checkpoints directory; exact directory paths are not documented. Checkpointing is disabled by default, and checkpoints are removed when a new session starts, making this session rollback state rather than cross-session memory.

[src](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/checkpointing.md)

## Compatibility notes

The CLI discovers skills in .agents/skills aliases as well as Tabnine-specific skill directories; IDE guideline documentation only compares its guidelines with lowercase agents.md and does not document loading AGENTS.md or CLAUDE.md. Skill precedence is documented across built-in, extension, user, and workspace sources, while guideline precedence only specifies organization over personal; project ordering is not documented. The guidelines page labels /.tabnine/guidelines/ as the home-directory location; it does not show a ~ or $HOME form. Extension documentation says guides may be mirrored into TABNINE.md as a reference but does not specify automatic loading or extension discovery paths; the CLI is in maintenance mode, with critical updates planned through December 31, 2026, followed by deprecation.
