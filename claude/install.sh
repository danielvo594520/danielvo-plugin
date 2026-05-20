#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLAUDE_HOME="${CLAUDE_HOME:-$HOME/.claude}"

mkdir -p "$CLAUDE_HOME/skills" "$CLAUDE_HOME/agents"

link_path() {
  local source_path="$1"
  local target_path="$2"

  if [ -e "$target_path" ] && [ ! -L "$target_path" ]; then
    echo "Refusing to replace existing non-symlink: $target_path" >&2
    exit 1
  fi

  ln -sfn "$source_path" "$target_path"
}

link_path "$ROOT/plugins/danielvo-dev/skills/dev-workflow" "$CLAUDE_HOME/skills/dev-workflow"
link_path "$ROOT/plugins/danielvo-dev/skills/plugin-maintainer" "$CLAUDE_HOME/skills/plugin-maintainer"
link_path "$ROOT/plugins/danielvo-dev/agents/danielvo-reviewer.md" "$CLAUDE_HOME/agents/danielvo-reviewer.md"
link_path "$ROOT/plugins/danielvo-dev/agents/danielvo-plugin-maintainer.md" "$CLAUDE_HOME/agents/danielvo-plugin-maintainer.md"

echo "Installed Danielvo Claude Code skills and agents into $CLAUDE_HOME"
