#!/usr/bin/env bash
# Mirror a skill folder into the two widest-discovered skill locations.
# Per convention-map SYNTHESIS (2026-10-05): .agents/skills is discovered by
# 13/17 harnesses, .claude/skills by 8 (several for compatibility). Mirroring
# into both covers the union without picking a side.
#
# Usage: scripts/mirror-skills.sh <skill-dir> [repo-root]
#   <skill-dir>  folder containing SKILL.md (copied, not moved)
#   [repo-root]  defaults to current directory
set -euo pipefail

skill="${1:?usage: mirror-skills.sh <skill-dir> [repo-root]}"
root="${2:-.}"
name="$(basename "$skill")"

[ -f "$skill/SKILL.md" ] || { echo "error: $skill has no SKILL.md"; exit 1; }

for target in ".agents/skills" ".claude/skills"; do
  dest="$root/$target/$name"
  mkdir -p "$dest"
  cp -R "$skill/." "$dest/"
  echo "mirrored -> $dest"
done

cat <<'NOTE'

Note: this copies, it does not symlink — some harnesses walk skill dirs
without following links. Re-run after editing the source skill.
NOTE
