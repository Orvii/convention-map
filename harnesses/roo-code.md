# Roo Code

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `.roo/rules/** (directory, recursive)` | project | Project rules; recursive read, files sorted alphabetically by basename (case-insensitive), cache/system files skipped. Loaded for all modes; takes precedence over global rules when they conflict. | [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code-Docs/main/docs/features/custom-instructions.md) |
| `.roo/rules-{modeSlug}/** (directory)` | project | Mode-specific project rules; loaded before generic .roo/rules. If no files in any rules-{mode} dir, falls back to .roorules-{mode}, then .clinerules-{mode}. | [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code-Docs/main/docs/features/custom-instructions.md) |
| `~/.roo/rules/** (directory, recursive)` | global | Global rules dir, fixed at ~/.roo (Windows %USERPROFILE%\.roo). Aggregated with project .roo/rules (both read, not either-or); workspace rules win on conflict. | [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code-Docs/main/docs/features/custom-instructions.md) |
| `~/.roo/rules-{modeSlug}/** (directory)` | global | Global mode-specific rules; loaded before generic ~/.roo/rules; complements rather than replaces them. | [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code-Docs/main/docs/features/custom-instructions.md) |
| `AGENTS.md (workspace root, + subfolders with .roo dirs when enableSubfolderRules)` | project | Loaded by default (roo-cline.useAgentRules, default true). Position in prompt: after mode-specific rules and .rooignore, before generic rules from ~/.roo/rules and .roo/rules. AGENTS.md preferred over AGENT.md. | [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/src/core/prompts/sections/custom-instructions.ts) |
| `AGENT.md (workspace root)` | project | Alternative filename, loaded only if AGENTS.md is absent/empty. | [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/src/core/prompts/sections/custom-instructions.ts) |
| `AGENTS.local.md (workspace root, + subfolders)` | project | Personal overrides for AGENTS.md (not version-controlled); loaded even if AGENTS.md does not exist. Source-only feature, not yet in the docs page. | [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/src/core/prompts/sections/custom-instructions.ts) |
| `.roorules (workspace root, single file)` | project | Legacy generic fallback: used only when no .roo/rules/ directory content was loaded; checked before .clinerules. | [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code-Docs/main/docs/features/custom-instructions.md) |
| `.roorules-{modeSlug} (workspace root, single file)` | project | Legacy mode fallback when no rules-{mode} directory has files; checked before .clinerules-{mode}. | [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code-Docs/main/docs/features/custom-instructions.md) |
| `.clinerules (workspace root, single file)` | project | Cline compatibility; same legacy fallback slot as .roorules for generic rules (checked after it, so .roorules wins if both exist). Only the single root file is read - no .clinerules/ directory scan. | [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/src/core/prompts/sections/custom-instructions.ts) |
| `.clinerules-{modeSlug} (workspace root, single file)` | project | Cline mode compatibility fallback, checked after .roorules-{mode}. | [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/src/core/prompts/sections/custom-instructions.ts) |
| `<subfolder>/.roo/rules/** and <subfolder>/AGENTS.md (monorepo)` | project | Opt-in via enableSubfolderRules setting (default false): recursively discovers any subfolder .roo dirs and loads their rules/AGENTS.md, root first then subfolders alphabetically. | [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/src/services/roo-config/index.ts) |
| `.rooignore (instructions section)` | project | Ignore-list file; its generated instructions are injected between mode-specific rules and AGENTS.md in the prompt. | [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/src/core/prompts/sections/custom-instructions.ts) |

## Skill directories discovered

- `.roo/skills-{modeSlug}/{skill-name}/SKILL.md` — [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code-Docs/main/docs/features/skills.mdx)
- `.roo/skills/{skill-name}/SKILL.md` — [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code-Docs/main/docs/features/skills.mdx)
- `.agents/skills-{modeSlug}/{skill-name}/SKILL.md` — [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code-Docs/main/docs/features/skills.mdx)
- `.agents/skills/{skill-name}/SKILL.md` — [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code-Docs/main/docs/features/skills.mdx)
- `~/.roo/skills-{modeSlug}/{skill-name}/SKILL.md` — [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/src/services/skills/SkillsManager.ts)
- `~/.roo/skills/{skill-name}/SKILL.md` — [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code-Docs/main/docs/features/skills.mdx)
- `~/.agents/skills-{modeSlug}/{skill-name}/SKILL.md` — [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/src/services/skills/SkillsManager.ts)
- `~/.agents/skills/{skill-name}/SKILL.md` — [src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code-Docs/main/docs/features/skills.mdx)

## Learned memory

None - Roo Code has no built-in learned/auto memory and no memories directory; persistent context comes only from rule files and skills, and "Memory Bank" is a community pattern users build out of custom instructions (docs mention it only once, in a v3.3.6 release note, as a user workflow).

[src](https://raw.githubusercontent.com/RooCodeInc/Roo-Code-Docs/main/docs/features/custom-instructions.md)

## Compatibility notes

Skill priority (highest to lowest): project .roo mode-specific > project .roo generic > project .agents mode > project .agents generic > global .roo mode > global .roo generic > global .agents mode > global .agents generic. Project overrides global; .roo overrides .agents at same level; symlinked skill dirs supported; frontmatter name must equal dir name.

Compatibility: only foreign conventions read are AGENTS.md/AGENT.md/AGENTS.local.md (cross-agent standard) and Cline's legacy .clinerules/.clinerules-{mode}. Loader source (src/core/prompts/sections/custom-instructions.ts) and full docs repo grep show ZERO references to CLAUDE.md, GEMINI.md, CRUSH.md, .cursorrules, .cursor/rules, opencode.json, kilo.jsonc - not loaded.

Exact prompt assembly order: Language Preference -> Global Instructions (Prompts tab) -> Mode-specific Instructions (Prompts tab) -> mode rules dirs -> mode fallback file -> .rooignore -> AGENTS.md family -> generic rules dirs -> generic fallback file. Directory rules from ALL locations are aggregated (global + project), not first-match; file fallbacks only used when no directory content exists.

Skills use progressive disclosure: at startup only SKILL.md frontmatter (name+description) is indexed; full body loaded on demand via read_file; mode filter applies (skills-{mode}).

Docs site URLs: https://docs.roocode.com/features/custom-instructions and https://docs.roocode.com/features/skills (both 301 to roocodeinc.github.io/Roo-Code). Evidence fetched this session from raw repo files at the URLs above.
