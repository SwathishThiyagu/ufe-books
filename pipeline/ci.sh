#!/usr/bin/env bash
# Runs inside GitHub Actions: write each requested unit on its own branch free/<unit>-book.
# A request line is "<unit> [output path]"; the output path defaults to the unit's path in queue.json.
set -u
git config user.name "ufe-free-books"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git checkout -q main
if [ -n "${UNITS:-}" ]; then
  reqs=$(echo "$UNITS" | tr ' ,' '\n\n' | sed '/^$/d')
else
  reqs=$(grep -v '^[[:space:]]*#' pipeline/requests.txt | sed '/^[[:space:]]*$/d')
fi
[ -z "$reqs" ] && { echo "nothing requested"; exit 0; }
echo "$reqs" | while read -r unit out; do
  br="free/${unit}-book"
  echo "::group::$unit"
  if git ls-remote --exit-code --heads origin "$br" >/dev/null 2>&1; then
    git fetch -q origin "$br"
    if git show "origin/$br:.free/$unit/status.json" 2>/dev/null | grep -q '"state": "ok"'; then
      echo "$unit is already done on $br"; echo "::endgroup::"; continue
    fi
    git checkout -q -B "$br" "origin/$br"
    git merge -q --no-edit -X theirs main || { git merge --abort; git checkout -q -B "$br" main; }
  else
    git checkout -q -B "$br" main
  fi
  if [ -n "${out:-}" ]; then python pipeline/run_unit.py "$unit" --out "$out"; else python pipeline/run_unit.py "$unit"; fi
  code=$?
  for p in .free books pilot; do [ -e "$p" ] && git add -A "$p"; done
  git commit -q -m "$unit: free-model book (exit $code)" || true
  git push -q origin "$br" || echo "push failed for $br"
  git checkout -q main
  echo "::endgroup::"
  if [ "$code" = "75" ]; then echo "The free quota is used up for today; the rest waits for the next run."; break; fi
done
