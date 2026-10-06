# Augment Code

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `/path/to/custom-rules.md` | project | CLI lists custom rules first and says they are appended to automatically loaded workspace guidelines; the file's scope is not documented. | [src](https://docs.augmentcode.com/cli/rules) |
| `CLAUDE.md` | project | CLI lists it above AGENTS.md; also discovered hierarchically up to the workspace root. | [src](https://docs.augmentcode.com/cli/rules) |
| `AGENTS.md` | project | CLI lists it below CLAUDE.md; also discovered hierarchically up to the workspace root. | [src](https://docs.augmentcode.com/cli/rules) |
| `<workspace_root>/.augment-guidelines` | project | CLI ranks below AGENTS.md and workspace rules; IDE lists it last when applying rules under the character limit. | [src](https://docs.augmentcode.com/setup-augment/guidelines) |
| `<workspace_root>/.augment/rules/` | project | CLI ranks below workspace guidelines; IDE rules support Always, Manual, and Auto types. | [src](https://docs.augmentcode.com/cli/rules) |
| `~/.augment/rules/` | user | CLI ranks below workspace rules; IDE user rules are always included. | [src](https://docs.augmentcode.com/setup-augment/guidelines) |
| `~/.augment/user-guidelines.md` | user | IDE user guidelines apply to future chats in that IDE; ordering against other sources is not documented. | [src](https://docs.augmentcode.com/setup-augment/guidelines) |
| `*.md` | project | Can be imported as workspace rules; general precedence is not documented. | [src](https://docs.augmentcode.com/setup-augment/guidelines) |
| `*.mdx` | project | Can be imported as workspace rules; general precedence is not documented. | [src](https://docs.augmentcode.com/setup-augment/guidelines) |

## Skill directories discovered

- `~/.augment/skills/` — [src](https://docs.augmentcode.com/cli/skills)
- `<workspace>/.augment/skills/` — [src](https://docs.augmentcode.com/cli/skills)
- `~/.claude/skills/` — [src](https://docs.augmentcode.com/cli/skills)
- `<workspace>/.claude/skills/` — [src](https://docs.augmentcode.com/cli/skills)
- `~/.agents/skills/` — [src](https://docs.augmentcode.com/cli/skills)
- `<workspace>/.agents/skills/` — [src](https://docs.augmentcode.com/cli/skills)
- `cosmos/files/organization/.augment/skills/` — [src](https://docs.augmentcode.com/cosmos/config-skills)
- `cosmos/files/user/.augment/skills/` — [src](https://docs.augmentcode.com/cosmos/config-skills)
- `<repo>/<workspace>/.claude/skills/` — [src](https://docs.augmentcode.com/cosmos/config-skills)
- `<repo>/<workspace>/.agents/skills/` — [src](https://docs.augmentcode.com/cosmos/config-skills)
- `plugins/hello-commands/` — [src](https://docs.augmentcode.com/cli/plugins)
- `agents/` — [src](https://docs.augmentcode.com/cli/plugins)
- `skills/` — [src](https://docs.augmentcode.com/cli/plugins)

## Learned memory

Cosmos Experts retain useful context across sessions as readable Markdown in the Expert's directory in the shared virtual filesystem. Memory is enabled for all Template Experts; custom Experts created with Cosmos Advisor get lightweight memory by default unless omitted. Experts can save trusted feedback directly and build evidence before promoting noisier signals.

[src](https://docs.augmentcode.com/cosmos/experts-memory)

## Compatibility notes

Auggie and the IDE support Claude- and Agents-style skill directories, including .claude/skills/ and .agents/skills/. CLI rules have a listed order, but the docs do not define a general conflict-resolution algorithm; the IDE's order applies to limit handling. IDE documentation says hierarchical AGENTS.md and CLAUDE.md files are combined, while CLI lists CLAUDE.md above AGENTS.md. Cosmos skill paths and memory are documented, but Cosmos instruction-file paths and team/enterprise instruction-file scopes are not documented.
