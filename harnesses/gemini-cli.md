# Gemini CLI

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `~/.gemini/GEMINI.md` | global | Global tier loaded first, then concatenated with workspace and JIT files and sent to the model with every prompt — tiers concatenate, nothing overrides. | [src](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/gemini-md.md) |
| `GEMINI.md in the workspace directories and their parent directories` | project | Loaded after global; upward traversal stops at first directory containing a boundary marker (context.memoryBoundaryMarkers, default [".git"]); context.discoveryMaxDirs default 200. Docs define load order (global → workspace → JIT) but contents are concatenated, no winner-takes-all. | [src](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/gemini-md.md) |
| `GEMINI.md in any directory a tool accesses (just-in-time, dir + ancestors up to trusted root)` | project | JIT tier appended when the model touches that directory; discovers component-specific instructions only when needed. | [src](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/gemini-md.md) |
| `Any filename(s) set in settings.json context.fileName (string | string[]; default undefined → GEMINI.md), e.g. ["AGENTS.md", "CONTEXT.md", "GEMINI.md"]` | both | Replaces the default GEMINI.md name at every tier; this is the only way AGENTS.md / other vendors' files are read — they are NOT in the default list. | [src](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/reference/configuration.md) |
| `@path.md imports referenced inside any context file (relative or absolute paths)` | both | Inlined via the Memory Import Processor (docs/reference/memport.md); lets a GEMINI.md pull arbitrary markdown files, including outside the workspace. | [src](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/gemini-md.md) |
| `<extension dir>/<contextFileName declared in gemini-extension.json> (default GEMINI.md at extension root)` | global | Extension context is an additive read-only layer, loaded in every session where the extension is active; extensions are not a write target for memories. | [src](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/extensions/writing-extensions.md) |
| `settings.json files: system defaults, ~/.gemini/settings.json (user), .gemini/settings.json (project), /etc/gemini-cli/settings.json (Linux) | C:\ProgramData\gemini-cli\settings.json (Windows) | /Library/Application Support/GeminiCli/settings.json (macOS)` | both | Config layers, low→high: defaults < system defaults file < user settings < project settings < system override settings < env vars (.env) < CLI args. | [src](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/reference/configuration.md) |

## Skill directories discovered

- `.gemini/skills/ (workspace; SKILL.md at dir root or one level deep; only discovered when workspace is trusted)` — [src](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/skills.md)
- `.agents/skills/ (workspace alias; takes precedence over .gemini/skills within the workspace tier)` — [src](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/skills.md)
- `~/.gemini/skills/ (user scope, available across all projects)` — [src](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/skills.md)
- `~/.agents/skills/ (user alias; takes precedence over ~/.gemini/skills within the user tier)` — [src](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/skills.md)
- `<extension dir>/skills/<skill-name>/SKILL.md (skills bundled in installed extensions)` — [src](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/extensions/writing-extensions.md)
- `built-in skills shipped with the CLI (no user directory)` — [src](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/skills.md)

## Learned memory

Yes — the agent persists durable facts by editing Markdown memory files (shared project instructions → repo GEMINI.md, private project notes → the per-project private memory folder, cross-project preferences → ~/.gemini/GEMINI.md), and the experimental Auto Memory feature (experimental.autoMemory, off by default) mines past session transcripts from ~/.gemini/tmp/<project>/chats/ and drafts memory .patch files plus SKILL.md candidates into a project-local inbox reviewed via /memory inbox, never applying anything without approval.

[src](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/auto-memory.md)

## Compatibility notes

Compatibility: default context filename is GEMINI.md only — AGENTS.md, CLAUDE.md, .cursorrules, CRUSH.md etc. are NOT read by default; AGENTS.md/any other vendor file works only when listed in settings context.fileName (request to add AGENTS.md to defaults is still open, issue #12345, Oct 2025). The `.agents/skills/` alias is Gemini CLI's explicit cross-tool interop path (Agent Skills open standard, originally Anthropic's format); within a tier the .agents alias beats .gemini/skills. Skill discovery precedence low→high: built-in < extension < user < workspace; workspace skills only load in trusted folders; only name+description are injected at session start, the SKILL.md body loads on activation after a user consent prompt. Context files are concatenated (never merged/overridden) and support @file.md imports; /memory show, /memory reload, /memory inbox manage them. Config lives in settings.json (four layers, precedence documented above) — this is Gemini's analogue of opencode.json/kilo.jsonc, not an instruction source. Note: geminicli.com banner announces Gemini CLI is being replaced by Antigravity CLI for unpaid/Google One tiers on June 18 (per https://geminicli.com/docs/cli/skills fetched this session).
