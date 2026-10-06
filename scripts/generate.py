#!/usr/bin/env python3
"""Regenerate matrix.md + harnesses/*.md from convention-map research journals.

Usage: python3 scripts/generate.py <journal.jsonl> [more...]
Journal lines: {"type":"result","result":{harness, instruction_files[], skill_dirs[], memory, ...}}
"""
import json
import re
import sys
from pathlib import Path


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


INSTR_VOCAB = [
    "CLAUDE.md", "CLAUDE.local.md", "AGENTS.md", "GEMINI.md", "CRUSH.md",
    "QWEN.md", ".cursorrules", "copilot-instructions.md", "opencode.json",
    "kilo.jsonc", ".continue/", "rules/",
]
SKILL_VOCAB = [
    ".claude/skills", ".agents/skills", ".cursor/skills", ".continue/skills",
    ".opencode/skills", ".kilo/skills", ".qwen/skills", ".goose/skills",
    ".github/copilot", "plugins/",
]


def match_vocab(text: str, vocab):
    """Free-form doc prose -> set of known convention markers it mentions.

    Case-sensitive on purpose: Bolt documents lowercase `agents.md` and does
    NOT document `AGENTS.md`; a case-insensitive match would credit it with
    the standard it never claims. Verified against waves 1-2: identical hits.
    """
    return {v for v in vocab if v in text}


def manifest_order(journals, manifest):
    """Order journal files by the wave order MANIFEST.md declares.

    "Later waves win on conflicts" is load-bearing and is NOT the alphabetical
    order a shell glob produces: `journals/*.jsonl` would apply whichever wave
    sorts last as the winner, regardless of when it actually ran. The README and
    MANIFEST both print the glob form, so sort here by the manifest's declared
    order; files the manifest does not list go last (newest, alphabetical among
    themselves — the incoming-journal convention).
    """
    if not manifest.exists():
        return list(journals)
    text = manifest.read_text(encoding="utf-8")
    declared = []
    for name in re.findall(r"\((wf_[A-Za-z0-9._-]+\.jsonl)\)", text):
        if name not in declared:
            declared.append(name)
    rank = {name: i for i, name in enumerate(declared)}
    return sorted(
        journals,
        key=lambda j: (rank.get(Path(j).name, len(rank)), Path(j).name),
    )


def load(journals):
    merged = {}
    for j in journals:
        for line in Path(j).read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            m = json.loads(line)
            r = m.get("result")
            if m.get("type") != "result" or not isinstance(r, dict) or "harness" not in r:
                continue
            merged[slug(r["harness"])] = r
    return sorted(merged.values(), key=lambda r: slug(r["harness"]))


def main(journals, out: Path, manifest: Path = None):
    # Order by MANIFEST.md's wave sequence, not the order the shell expanded:
    # later waves must win on conflicts (see manifest_order's docstring). The
    # caller passes the repo root as `out`, so the manifest sits beside the
    # journals it describes; an explicit path overrides it (CI regenerates
    # into /tmp from the same checkout).
    if manifest is None:
        candidate = Path(out) / "journals" / "MANIFEST.md"
        manifest = candidate if candidate.exists() else None
    if manifest is not None:
        journals = manifest_order(journals, manifest)
    rows = load(journals)
    if not rows:
        sys.exit("no results")

    # union of vocabulary markers mentioned across all entries
    files = []
    for r in rows:
        for f in r.get("instruction_files", []):
            for v in match_vocab(f["path"], INSTR_VOCAB):
                if v not in files:
                    files.append(v)
        for d in r.get("skill_dirs", []):
            for v in match_vocab(d["path"], SKILL_VOCAB):
                if v not in files:
                    files.append(v)
    files.sort()

    (out / "harnesses").mkdir(exist_ok=True)
    for r in rows:
        s = slug(r["harness"])
        lines = [f"# {r['harness']}", "", "## Instruction files loaded", ""]
        if r.get("instruction_files"):
            lines += ["| path | scope | precedence | evidence |", "|---|---|---|---|"]
            for f in r["instruction_files"]:
                prec = (f.get("precedence_note") or "—").replace("|", "\\|")
                lines.append(f"| `{f['path']}` | {f['scope']} | {prec} | [src]({f['evidence_url']}) |")
        else:
            lines.append("none documented.")
        lines += ["", "## Skill directories discovered", ""]
        if r.get("skill_dirs"):
            lines += [f"- `{d['path']}` — [src]({d['evidence_url']})" for d in r["skill_dirs"]]
        else:
            lines.append("none documented.")
        lines += ["", "## Learned memory", "", r.get("memory", "—")]
        if r.get("memory_evidence_url"):
            lines += ["", f"[src]({r['memory_evidence_url']})"]
        if r.get("notes"):
            lines += ["", "## Compatibility notes", "", r["notes"]]
        (out / "harnesses" / f"{s}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # matrix: harness x file, mark loads
    md = ["# Convention-file load matrix", "",
          "Cell = harness loads that path (●) or discovers it as a skill dir (◆). Evidence on each harness page.", ""]
    md.append("| harness | " + " | ".join(f"`{p}`" for p in files) + " |")
    md.append("|---|" + "---|" * len(files))
    for r in rows:
        instr = set()
        for f in r.get("instruction_files", []):
            instr |= match_vocab(f["path"], INSTR_VOCAB)
        skills = set()
        for d in r.get("skill_dirs", []):
            skills |= match_vocab(d["path"], SKILL_VOCAB)
        s = slug(r["harness"])
        cells = []
        for p in files:
            mark = "●" if p in instr else ""
            if not mark and p in SKILL_VOCAB and p in skills:
                mark = "◆"
            cells.append(f"[{mark}](harnesses/{s}.md)" if mark else "·")
        md.append(f"| [{r['harness']}](harnesses/{s}.md) | " + " | ".join(cells) + " |")
    (out / "matrix.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"wrote {len(rows)} pages + matrix.md over {len(files)} convention paths")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:], Path(__file__).resolve().parent.parent)
