# Learned memory — who writes notes about you, and where

As of 2026-10-06, 27 harnesses. "Learned memory" here means: the agent *writes* durable notes about the user/project without being asked, and reloads them later. Instruction files you author are not memory; they are input. Sources: per-harness pages.

## The split

**Built-in learned memory (15):**

| Harness | Default | Where it writes |
|---|---|---|
| Claude Code | on (local sessions) | `~/.claude/projects/<project>/memory/`, index `MEMORY.md` |
| Qwen Code | on | `~/.qwen/projects/<project>/memory/`, index `MEMORY.md` |
| Goose | extension, toggleable | `~/.config/goose/memory/` + `.goose/memory/` |
| Gemini CLI | on | repo `GEMINI.md` (shared) + per-project private folder |
| Codex CLI | **off** | config-gated (`[features] memories = true`) |
| Kilo Code | **off**, per-project opt-in | `~/.local/share/kilo/memory/<project>/project.md` |
| Copilot CLI | preview, paid plans | server-side ("Copilot Memory"), not local files |
| Cursor | on (cloud automations) | per-automation `MEMORIES.md`, outside the agent filesystem; UI-managed |
| Windsurf | on (legacy Cascade) | `~/.codeium/windsurf/memories/`, workspace-scoped; successor Devin Local persists none |
| Google Jules | per-repo toggle | server-side "Jules Memory for Repositories"; no file path documented |
| Amazon Kiro | on (Kiro Web) | account-level automatic memory; open-source Kiro Crew adds a six-layer local store |
| Devin | on (cloud) | account Knowledge (deprecated, migrating to skills) + Automations scratchpad |
| Augment Code | on (Cosmos Experts) | Markdown memory in the Expert's directory on the shared virtual filesystem |
| Replit Agent | on | user + Project memories; sensitive categories excluded, private by default |
| Bolt | on (project knowledge) | persists through context clears; account knowledge spans projects |

**No learned memory (12):** OpenCode, Aider, Cline, Roo Code, Zed, OpenHands, Crush, Amazon Q CLI, Vibe, Continue, Tabnine (checkpointing is session rollback — not memory), Qodo (Context Engine retention undocumented). Their persistence is what you author (rules, transcripts, thread history) — nothing self-writes.

## What the split says

1. **The MEMORY.md index convention traveled.** Claude Code and Qwen Code write the same shape (one file per memory + `MEMORY.md` index) — another instance of the compatibility chain ([SYNTHESIS §6](SYNTHESIS.md)): the file layout became the interface before anyone standardized it.
2. **Defaults disagree, and defaults are policy.** On-by-default memory (Claude Code, Qwen, Gemini) means the agent records observations about you unless you opt out; off-by-default (Codex, Kilo) treats that recording as a choice. Neither is neutral; the matrix records which choice each made.
3. **Server-side memory is a different animal.** Copilot's lives on their servers, not your disk — deletable via their UI, not via `rm`. Anyone auditing what an agent remembers must first ask *where the memory lives*, because the answer decides who can read, export, or delete it.
4. **"Memory Bank" is not memory.** Cline and Roo Code document a *user-implemented* markdown methodology under that name. It appears in searches for memory and is not learned memory at all — a naming collision worth knowing before citing either.

5. **The cloud cluster moved memory off the disk entirely.** Cursor's per-automation memories, Jules' per-repo memory, Kiro Web's account memory and Devin's Knowledge all live in the vendor's account, not the user's filesystem. Point 3's audit question — *where does the memory live?* — now has a third answer beyond local files and one vendor server: *in an account scope you can only reach through a settings UI*, with migration paths (Devin Knowledge → skills) that can move your notes without touching your disk.

## Practical rules for multi-harness users

- If two harnesses with on-by-default memory share a repo, two note-takers write about the same project into different directories. Decide which one is authoritative; the other's notes are a fork of your project's folklore.
- Memory files are context: they load into prompts. Review them like code — a stale note ("we use library X") steers every future session.
- For shared machines, memory directories are per-user state with project names in the path; treat them as mildly sensitive.
