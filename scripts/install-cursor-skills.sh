#!/usr/bin/env bash
# Symlink plugin skills into ~/.cursor/skills for personal Cursor use.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/plugins/stock-market-mastery/skills"
DEST="${HOME}/.cursor/skills"
mkdir -p "$DEST"
for skill_dir in "$SRC"/*; do
  [ -d "$skill_dir" ] || continue
  name="$(basename "$skill_dir")"
  ln -sfn "$skill_dir" "$DEST/$name"
  echo "linked $DEST/$name"
done
echo "Done. Restart Cursor agent chat or start a new session to pick up skills."
