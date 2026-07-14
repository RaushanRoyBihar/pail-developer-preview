#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

blocked_files="$(find . -type f \( -name '*.tar' -o -name '*.tar.gz' -o -name '*.tgz' -o -name '*.zip' -o -name '*.whl' -o -name '*.sqlite*' -o -name '*.db' -o -name '*.psnd*' -o -name '*.wav' -o -name '*.pem' -o -name '*.key' \) -print)"
if [[ -n "$blocked_files" ]]; then
  printf 'Blocked public artifacts:\n%s\n' "$blocked_files" >&2
  exit 1
fi

blocked_paths="$(find . -type d \( -name 'panani_core_layers' -o -name 'sutra_pool' -o -name 'private_runtime' -o -name 'frequency_maps' -o -name 'memory_state' \) -print)"
if [[ -n "$blocked_paths" ]]; then
  printf 'Blocked private paths:\n%s\n' "$blocked_paths" >&2
  exit 1
fi

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  credential_scan=(git grep -IEn 'gh[pousr]_[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----' -- . ':!scripts/public-safety-check.sh')
else
  credential_scan=(grep -RIE --exclude='public-safety-check.sh' 'gh[pousr]_[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----' .)
fi

if "${credential_scan[@]}"; then
  echo 'Potential credential material detected.' >&2
  exit 1
fi

echo 'Public safety check passed.'
