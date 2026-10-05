# Qwen Code

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `QWEN.md (cwd, then each parent dir up to project root identified by .git folder, or up to home dir)` | project | Default context filename #1 (kept for backward compat; listed before AGENTS.md). Hierarchy: more specific files supplement/override general ones; all hits are concatenated with origin separators into the system prompt; exact order inspectable in /memory dialog. | [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/configuration/settings.md) |
| `~/.qwen/QWEN.md (global; QWEN_HOME env var relocates ~/.qwen)` | global | First/most general tier of the hierarchy, loaded for all projects. | [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/features/memory.md) |
| `AGENTS.md (same locations as QWEN.md: ~/.qwen/AGENTS.md, cwd + parent dirs, home dir)` | both | Read by default alongside QWEN.md: the default filename list is ['QWEN.md','AGENTS.md']; loader iterates filenames in that order, so all QWEN.md hits precede AGENTS.md hits; configurable via context.fileName. | [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/packages/core/src/memory/memoryDiscovery.ts) |
| `.qwen/QWEN.local.md (fixed slot at project root = nearest ancestor with .git dir/file)` | project | NOT part of the hierarchical upward search; loaded from a single fixed slot after all other project-level context files so it can supplement or override shared instructions; skipped if no project root; intended to be gitignored. | [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/packages/core/src/utils/memory-constants.ts) |
| `context.fileName setting (string or array) — configurable context filename(s) used at all locations above` | both | When set, overrides the default QWEN.md+AGENTS.md filename list. | [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/configuration/settings.md) |
| `~/.qwen/rules/**/*.md (or $QWEN_HOME/rules/)` | global | Rules: every .md under the dir (incl. subdirs) is discovered; always loaded; rules without paths: frontmatter are baseline (sit in system prompt every turn like context files). | [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/features/rules.md) |
| `<project>/.qwen/rules/**/*.md` | project | Loaded only when the workspace is trusted; rules with paths: globs are injected once on the first matching file read/edit; project rules load after user rules. | [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/features/rules.md) |
| `Extension context file named by extension manifest contextFileName (defaults to a QWEN.md in the extension dir when present) plus the extension's rules/ dir` | both | Extension context files are appended after the workspace QWEN.md/AGENTS.md scan; extension rules must be conditional (a no-paths rule is skipped with a warning), so they never join the always-on context. | [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/extension/introduction.md) |

## Skill directories discovered

- `~/.qwen/skills/` — [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/features/skills.md)
- `~/.agents/skills/` — [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/packages/core/src/config/storage.ts)
- `<project>/.qwen/skills/` — [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/features/skills.md)
- `<project>/.agents/skills/` — [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/packages/core/src/skills/skill-manager.ts)
- `custom directories from the settings `skills.directories` array (discovered at the user level, ~ expanded)` — [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/packages/core/src/config/config.ts)
- `bundled skills shipped inside the package (<bundleDir>/bundled; in the repo: packages/core/src/skills/bundled/)` — [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/packages/core/src/skills/skill-manager.ts)
- `active extensions' skills (no fixed base dir; loaded from active extensions)` — [src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/features/skills.md)

## Learned memory

Built-in learned auto-memory, on by default: after sessions Qwen writes markdown memory files (one file per memory plus a MEMORY.md index) under ~/.qwen/projects/<project>/memory/ — per git checkout, each linked worktree gets its own folder — with an opt-in git-committed team tier at <repo>/.qwen/team-memory/.

[src](https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/features/memory.md)

## Compatibility notes

Compatibility and extras. (1) Gemini CLI fork heritage: it no longer loads GEMINI.md as context — the filename constants are now QWEN.md/AGENTS.md (only deprecated setGeminiMdFilename aliases remain in code); CLAUDE.md and GEMINI.md appear only in permission-classifier prompt text and stale comments, not in any loader. No .cursorrules / CRUSH.md / opencode.json / kilo.jsonc support. (2) Claude Code interop exists but not via convention files: `/import-config` imports MCP servers from ~/.claude.json and .claude/settings.json (packages/cli/src/config/claudeMcpImport.ts); the extension system consumes Claude's `.claude-plugin/marketplace.json` + plugin.json and rewrites `.claude` path references to `.qwen`; subagent frontmatter mirrors `.claude/agents/*.md` verbatim so CC agent files can be copied into `.qwen/agents/` (project, highest precedence) or `~/.qwen/agents/` (user fallback); hooks accept CLAUDE_PROJECT_DIR. It does NOT read ~/.claude/skills/ or .claude/skills/. (3) The shared `.agents` convention is honored for skills only — provider config dirs are ['.qwen','.agents'] at both user and project level; .agents is not used for rules/context. (4) Skills precedence: within a level the first provider dir wins, so .qwen beats .agents; across levels project > user > extension > bundled (documented in skills.md). A skill colliding with a custom command loses on the slash surface (commands load after skills). (5) Other instruction-ish files it loads: .qwen/agents/*.md and ~/.qwen/agents/*.md (subagent definitions), .qwen/commands/*.md and ~/.qwen/commands/*.md (custom slash-command prompts), .qwen/workflows/*.js surfaced as slash commands. Context files support @path/to/file.md imports (Claude-style import processor). (6) context.includeDirectories / context.loadFromIncludeDirectories can extend the QWEN.md scan across extra directories; QWEN_CODE_MEMORY_* env vars relocate/partition auto-memory.
