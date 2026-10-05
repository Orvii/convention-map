# Google Jules

## Instruction files loaded

| path | scope | precedence | evidence |
|---|---|---|---|
| `AGENTS.md` | project (repository root; read automatically for Jules sessions on that repository) | No precedence rules are documented. The docs describe a single file looked up automatically in the repository root ("Jules now automatically looks for a file named AGENTS.md in the root of your repository") and are silent on which file wins when multiple AGENTS.md files or other instruction sources exist. First announced June 20, 2025: "Jules reads from AGENTS.md if it's in your repo." | [src](https://jules.google/docs/#include-agentsmd-file) |
| `README.md` | project (repository root; used only as environment-setup hints) | Docs mention README.md alongside AGENTS.md only as a source of setup hints ("Jules will also refer to agents.md or your readme.md file for hints to setup an environment on the fly"); no precedence between the two is stated. | [src](https://jules.google/docs/environment/) |

## Skill directories discovered

none documented.

## Learned memory

Jules has persistent cross-session memory at the repository level. \"Jules Memory for Repositories\" (announced September 30, 2025) captures preferences, nudges, and corrections during tasks, and the next time a task runs in that repository Jules consults the saved memory to anticipate the user's needs and patterns. It is a server-side cloud feature: no file path or storage location is documented. It can be toggled per repository in the repo settings page under \"Knowledge\" (default on/off state is not documented), and its scope is explicitly per repository — the docs say memory is referenced for \"the same or a similar task in that specific repository,\" with no cross-repository carry-over described. The Gemini 3 Pro changelog entry (November 19, 2025) later refers to \"Agentic Memories,\" described as Jules using context more effectively to adapt to coding preferences over time.

[src](https://jules.google/docs/changelog/2025-09-30)

## Compatibility notes

Everything above was verified from the official Jules documentation, which currently lives at https://jules.google/docs; the URL https://developers.google.com/jules returns HTTP 404 as fetched. The docs publish a machine-readable index at https://jules.google/docs/llms.txt and a .md variant of every page.

Cloud vs local: Jules is a cloud autonomous agent — each task runs in a fresh Google-hosted virtual machine that clones the repository, and AGENTS.md is read from the repository root inside that cloud session. Jules Tools, the command-line surface, is a client for the same cloud service; the docs describe no local convention-file loading for it (no user-level ~/.jules/AGENTS.md, no local instruction config).

Not documented: nested or subdirectory AGENTS.md files (only the repository-root file is described); precedence when multiple instruction sources exist; any user-level or enterprise-level instruction/context files; compatibility with other agents' convention files — CLAUDE.md, GEMINI.md, .cursor/rules, .cursor/skills, or skill directories of any kind are not mentioned anywhere in the docs, and AGENTS.md (plus README.md as a setup-hints fallback) is the only convention file Jules documents. The docs are likewise silent on the exact spelling beyond describing it as AGENTS.md (the environment page uses lowercase "agents.md").

Other context configured through the UI rather than files: environment setup scripts and per-repository environment variables are entered in repository settings, and MCP server connections are added per account on the Jules Settings page; none of these have documented config-file paths.
