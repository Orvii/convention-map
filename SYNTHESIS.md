# Synthesis — the interoperability surface, measured

As of 2026-10-05, 22 harnesses. Counts below are harnesses whose docs document loading the marker (●/◆ in [matrix.md](matrix.md)); every cell cites a fetched doc.

## 1. AGENTS.md won the instruction war by absence of opposition

21 of 22 harnesses document reading `AGENTS.md`. The single holdout is **Aider**, whose design predates the format and whose docs document no instruction file at all — not a rejection but an absence. The house-file camps (Crush, Qwen Code) read their own file *and* AGENTS.md, so the count is about defaults, not exclusivity.

The decisive detail is Claude Code's rule: it reads `AGENTS.md` **only when no `CLAUDE.md` exists** in the working directory or above (default `claude-md-or-agents-md`, v2.1.277+). So the ecosystem's most influential harness defers to AGENTS.md precisely when the house file is absent — which is exactly the condition in every repo that adopted the open convention first. A standard won by being the fallback.

## 2. Skills split into two camps, and the split is political

`.agents/skills` (16) vs `.claude/skills` (11). The `.claude/skills` readers include harnesses that document the path explicitly as Claude-Code compatibility (OpenCode gates it behind `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1`; Crush lists it among several discovery roots). The `.agents/skills` readers are the neutral-ground camp.

Practical consequence: mirroring a skill folder into both paths costs nothing and covers ~the union. Treating either as "the standard" costs you the other camp.

## 3. House files persist as opt-outs, not defaults

`GEMINI.md` (6), `.cursorrules` (6), `CRUSH.md` (2), `QWEN.md` (1), `copilot-instructions.md` (3): every vendor house file survives, but mostly as an *additional* source alongside AGENTS.md rather than instead of it. The pattern is accretion: harnesses add the open convention without removing the house one, because removing it would break existing users' repos.

## 4. Precedence is where the compatibility breaks

Loading is the easy half; *which file wins* is undocumented or surprising in most harnesses. Claude Code concatenates (root-first, never overrides) and has a config switch for CLAUDE.md+AGENTS.md coexistence; OpenCode walks up to the git worktree; others are silent. Two harnesses reading the same two files can therefore behave differently on the same repo — interoperability at the file level does not imply interoperability at the semantic level.

## 5. Expiry date

This map is a snapshot of an arms race in slow motion: Claude Code added native AGENTS.md in v2.1.277; Continue shipped Claude-compatible hooks after its end-of-life; Vibe imports four vendors' plugin formats. Re-measure before relying on any count here — the generator and evidence contract exist for exactly that (`scripts/generate.py`, see [harness-atlas CONTRIBUTING](https://github.com/Orvii/harness-atlas/blob/main/CONTRIBUTING.md) for the shared rules).
