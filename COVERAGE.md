# Coverage — what this map does and does not include

As of 2026-10-05. A map that hides its edges invites over-trust; these are ours.

## Included (17)

Claude Code, OpenCode, Codex CLI, Gemini CLI, Aider, Goose, OpenHands, Cline, Roo Code, Qwen Code, Zed, Continue, Kilo Code, GitHub Copilot CLI, Crush, Amazon Q Developer CLI, Vibe.

Selection rule: open-source or openly documented **coding agents with a documented instruction/skill loading surface**, plus the most-cited compatibility targets. Star counts informed the second batch, not the first.

## Deliberately not included

- **Cursor, Windsurf, JetBrains Junie, Amazon Q IDE plugin, GitHub Copilot Chat (IDE).** IDE-bound agents with closed or partially closed distribution: their docs describe settings UI more than file conventions, and several change without public changelogs. Mapping them would produce cells whose evidence is a help-center article that may be rewritten next week. They are candidates for a future batch *if* their docs stabilize around file conventions.
- **Framework-level agent runtimes** (LangGraph, AutoGen, CrewAI). They orchestrate models but do not load repo instruction files; the question this map asks does not apply.
- **One-off or unmaintained CLIs.** A convention loader with two releases and no docs is not a convention.

## Known limits inside the included set

- **Precedence is under-documented** for several harnesses (see PRECEDENCE.md "the undocumented middle"): a ● cell says "loads", not "wins".
- **Enterprise/managed tiers** (managed CLAUDE.md, org-deployed skills) are noted where documented but not matrixed separately; they change who controls the file, which is a governance question, not a loading question.
- **Version skew.** Cells describe the release pinned on each harness page. A harness that adds a loader next month is not wrong today; the map is.

## How to extend

Follow the evidence contract in the sibling atlas ([harness-atlas CONTRIBUTING](https://github.com/Orvii/harness-atlas/blob/main/CONTRIBUTING.md)): fetched URLs per claim, version pin with source, `unknown` over guess. Then `scripts/generate.py` does the rest.
