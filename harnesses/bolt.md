# Bolt

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `agents.md` | project | Bolt starts with agents.md, then follows links or references; main instructions must be in agents.md. Precedence against other instruction sources is not documented. | [src](https://support.bolt.new/best-practices/manage-context) |
| `record-keeping .md files (exact paths not documented)` | project | Read into context on every prompt; ordering or conflict handling is not documented. | [src](https://support.bolt.new/best-practices/manage-context) |

## Skill directories discovered

none documented.

## Learned memory

Project knowledge remains available after context is cleared, although recent chat history does not; Bolt retains access to project code and files. Account knowledge applies across projects, while project knowledge is limited to one project. Saved custom prompts are tied to the account and available across workspaces, including team workspaces, but are not shared with teammates by default.

[src](https://support.bolt.new/best-practices/manage-context)

## Compatibility notes

Bolt documents lowercase agents.md as its project instruction entry point; recognition of AGENTS.md is not documented. Project skills override workspace skills with the same name, but broader conflict handling among instructions and knowledge sources is not documented. Skills are considered from the current project, enabled workspace skills, and enabled Bolt-curated skills, but no discovery directory paths are specified. The Prompt Library is account-scoped, not documented as file-backed, and prompts are not shared by default. skill discovery names three sources (current project, enabled workspace skills, Bolt-curated) without directory paths.
