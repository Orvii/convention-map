<picture>
  <source media="(prefers-color-scheme: dark)" srcset="hero.svg">
  <img alt="convention-map — which instruction and skill files each harness loads" src="hero.svg">
</picture>

# convention-map

Which instruction, memory and skill files each AI coding harness **loads**, from which paths, with what precedence — measured from official docs, one evidence URL per claim.

The ecosystem converged on a handful of convention files (`CLAUDE.md`, `AGENTS.md`, `SKILL.md`, skill directories) without anyone deciding it. This map is the measurement of that convergence: if you write your project's instructions once, where should they live to be read by the most harnesses?

## How to read it

- [matrix.md](matrix.md) — harness × convention-path grid. `●` = loaded as instruction/context file, `◆` = discovered as a skill directory.
- [harnesses/](harnesses/) — per harness: loaded paths with scope (global/project) and documented precedence, skill directories, learned-memory behavior, compatibility notes.
- [PRECEDENCE.md](PRECEDENCE.md) — the three conflict models (concatenate / first-match / specificity-overrides) for when two instruction files disagree.
- [MEMORY.md](MEMORY.md) — which harnesses write learned memory about you, where it lives, and on-by-default vs opt-in.
- [COVERAGE.md](COVERAGE.md) — what is included, what is deliberately not, and why.
- [SYNTHESIS.md](SYNTHESIS.md) — what the convergence means, and its expiry date.
- Every cell links to the doc page it was read from, fetched during the research run (2026-10-05).

## The short answer

As of this snapshot (27 harnesses): `AGENTS.md` at the project root is read by **23 of 27** — the de-facto instruction interchange. The four holdouts are instructive rather than rebellious: **Aider** predates the format entirely; **Replit Agent** and **Tabnine** read house files (`replit.md`, `.tabnine/guidelines`) instead; and **Bolt** auto-reads lowercase `agents.md` while documenting no `AGENTS.md` at all — the convention spreading as a case-variant. For skills the field splits: `.agents/skills` is discovered by 19, while `.claude/skills` is discovered by 12, several of those purely for Claude-Code compatibility. Practical read: put instructions in `AGENTS.md`; put skills in `.agents/skills` and mirror into `.claude/skills` if you care about the compatibility tail. Read [SYNTHESIS.md](SYNTHESIS.md) for why that is an observation with an expiry date, not a standard.

This repo answers *which file each harness reads*. The two adjacent questions — *what people actually put in those files* (2,303 real ones: testing instructions in 75.9%, security in 14.8%) and *whether the files change what agents do* (four experiments, one of them a null with a stated power bound) — live in [context-file-evidence](https://github.com/Orvii/context-file-evidence). Read together they say: the format converged fast, the content did not, and the payoff is smaller and more content-dependent than either side of the debate claims.

## Regenerating

```bash
python3 scripts/generate.py <journal.jsonl> [...]
```

Same evidence contract as [harness-atlas](https://github.com/Orvii/harness-atlas): no memory answers, dates travel with claims, `unknown` over guess.

## Using the finding: mirror your skills

The map says `.agents/skills` (19/27) and `.claude/skills` (12/27) together cover the field. `scripts/mirror-skills.sh` copies a skill folder into both:

```bash
scripts/mirror-skills.sh path/to/my-skill [repo-root]
```

Copies, not symlinks — several harnesses walk skill directories without following links. Re-run after edits.

---

Orvii — Open, Research, Vision, Innovation & Ideas. The atlas maps capabilities, this maps the files they read.

Part of the Orvii research set: [harness-atlas](https://github.com/Orvii/harness-atlas) · [equivalence-notes](https://github.com/Orvii/equivalence-notes) · [provider-reliability](https://github.com/Orvii/provider-reliability) · [context-file-evidence](https://github.com/Orvii/context-file-evidence) · [retractions](https://github.com/Orvii/retractions) · [svg-instruments](https://github.com/Orvii/svg-instruments) · [bench-notes](https://github.com/Orvii/bench-notes) · [ts-lto-research](https://github.com/Orvii/ts-lto-research).

