# Aider

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `.aider.conf.yml (searched at ~/.aider.conf.yml, <git-root>/.aider.conf.yml, ./.aider.conf.yml)` | both | Documented load order: home dir, then git root, then current directory; files loaded last take priority (cwd wins). --config/-c replaces the search entirely and loads only that one file. This YAML is also the mechanism that auto-injects context at startup via its `read:` list (e.g. read: CONVENTIONS.md). Confirmed in source: aider/main.py builds default_config_files = [cwd, git_root, home] then reverses before parsing. | [src](https://aider.chat/docs/config/aider_conf.html) |
| `CONVENTIONS.md (canonical convention file, but any arbitrary path; conventional location: project root)` | project | NOT auto-discovered by filename. It is only loaded when explicitly named: `/read CONVENTIONS.md` in chat, `aider --read CONVENTIONS.md`, or `read: CONVENTIONS.md` (or read: [..]) inside .aider.conf.yml. Loaded read-only and prompt-cacheable. No per-directory discovery, no merge/precedence rules documented (all read files simply join the chat context). | [src](https://aider.chat/docs/usage/conventions.html) |
| `.aider.model.settings.yml (home dir, git root, cwd; overridable via --model-settings-file)` | both | Model configuration only (extra params/known-model settings), not instruction text. Search path built same way as other aider files: home, git root, cwd, plus explicit CLI file. Also .aider.model.metadata.json (default): context-window/cost metadata for unknown models, same search locations (source: aider/main.py generate_search_path_list/register_models). | [src](https://aider.chat/docs/config/options.html) |
| `.aider.model.metadata.json (home dir, git root, cwd; overridable via --model-metadata-file)` | both | Model metadata only, not instructions. Bundled resource metadata is always also loaded; user files add/override entries for unknown models. Same search pattern as .aider.model.settings.yml (source: aider/main.py register_litellm_models). | [src](https://aider.chat/docs/config/options.html) |

## Skill directories discovered

none documented.

## Learned memory

None — Aider has no built-in learned/auto memory: it only writes per-repo chat transcripts (.aider.chat.history.md, .aider.input.history, optional .aider.llm.history) and can manually replay past messages with --restore-chat-history; there is no memory directory, extraction, or cross-session learning.

[src](https://aider.chat/docs/config/options.html)

## Compatibility notes

No native foreign-vendor convention support: grep of current main branch (aider 0.86.3.dev) — aider/main.py, aider/args.py and the whole tree — found zero references to AGENTS.md, CLAUDE.md, GEMINI.md, CRUSH.md, .cursorrules, kilo.jsonc or opencode.json. Aider reads only its own .aider.conf.yml; any other file (e.g. AGENTS.md) reaches context only when explicitly named via /read, --read, or the read: key in .aider.conf.yml (community guidance, e.g. the agents.md FAQ, is exactly `read: AGENTS.md` in .aider.conf.yml — confirming no auto-load). Repo-level grep: https://raw.githubusercontent.com/Aider-AI/aider/main/aider/main.py and https://raw.githubusercontent.com/Aider-AI/aider/main/aider/args.py. Skills: no skill-directory discovery of any kind — no skill concept in the full options reference (https://aider.chat/docs/config/options.html) nor anywhere in the docs index (https://aider.chat/docs/); skill_dirs is empty. Config discovery is exactly three levels (home, git root, cwd) — no subdirectory-level config lookup. Other startup files: .env (git root by default, --env-file override, plus ~/.aider/oauth-keys.env for OAuth creds) and .aiderignore (git root) for ignore rules — neither carries instructions. `--load FILE` executes /commands from a file at launch (could be used to script /read, but is not a convention file itself). Four equivalent option channels confirmed: CLI flags, .aider.conf.yml (home or git root), AIDER_* env vars, .env file (https://aider.chat/docs/config.html); the docs do not spell out env-vs-yml resolution order beyond the file search order above.
