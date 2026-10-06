#!/usr/bin/env bash
# Count gate: every stated harness count in the repo must equal the number
# of harness pages on disk. Counts rot silently; this fails loudly.
set -euo pipefail
cd "$(dirname "$0")/.."

N=$(ls harnesses/*.md | wc -l | tr -d ' ')
fail=0

# README adoption claims: "read by **21 of 22**"
grep -oE '\*\*[0-9]+ of [0-9]+\*\*' README.md | tr -d '*' | while read -r claim; do
  total=${claim##* of }
  if [ "$total" != "$N" ]; then
    echo "README claims '$claim' but harnesses/ holds $N pages" >&2
    exit 1
  fi
done || fail=1

# MEMORY.md scope line: "As of <date>, <N> harnesses."
mem=$(grep -oE 'As of [0-9-]+, [0-9]+ harnesses' MEMORY.md | grep -oE '[0-9]+ harnesses' | head -1 | cut -d' ' -f1)
if [ "${mem:-}" != "$N" ]; then
  echo "MEMORY.md scope says ${mem:-none} harnesses but harnesses/ holds $N" >&2
  fail=1
fi

# MEMORY.md split: built-in table rows + no-memory list names == N
builtin=$(awk '/Built-in learned memory/{f=1;next} f&&/^\| Harness/{next} f&&/^\|---/{next} f&&/^\| /{c++} f&&!/^\| /&&NF{exit} END{print c+0}' MEMORY.md)
nolist=$(grep -oE '\*\*No learned memory \([0-9]+\):\*\*[^.]*\.' MEMORY.md | sed 's/^[^:]*: \*\*//' | tr -d '.' | awk -F', ' '{print NF}')
nolist_declared=$(grep -oE 'No learned memory \([0-9]+\)' MEMORY.md | grep -oE '[0-9]+')
if [ "$builtin" != "${builtin:-0}" ] || [ $((builtin + nolist)) != "$N" ]; then
  echo "MEMORY.md split: $builtin built-in + $nolist none = $((builtin + nolist)) != $N pages" >&2
  fail=1
fi
if [ "$nolist" != "$nolist_declared" ]; then
  echo "MEMORY.md no-memory list holds $nolist names but declares ($nolist_declared)" >&2
  fail=1
fi

if [ "$fail" = 0 ]; then
  echo "counts consistent: $N harness pages, README + MEMORY.md agree"
fi
exit $fail
