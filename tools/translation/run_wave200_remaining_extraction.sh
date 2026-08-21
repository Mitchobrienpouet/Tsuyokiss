#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
LAUNCHER="$ROOT/tools/translation/launch_wave200_remaining_sources.py"

if [[ $# -gt 0 && "${1:-}" != --* ]]; then
  SOURCE="$1"
  shift
  exec python3 "$LAUNCHER" --repo "$ROOT" --source "$SOURCE" "$@"
fi

exec python3 "$LAUNCHER" --repo "$ROOT" "$@"
