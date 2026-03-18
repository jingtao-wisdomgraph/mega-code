# mega-code plugin

Codex CLI plugin for session collection and skill extraction.
All Python logic lives in `mega_code/`. This directory owns
skills and plugin configuration.

## Structure

```
skills/run/       → $mega-code-run      trigger extraction pipeline
skills/status/    → $mega-code-status   show pending items
skills/profile/   → $mega-code-profile  set language/level/style
skills/login/     → $mega-code-login    OAuth flow
skills/help/      → $mega-code-help     list available commands
scripts/          → codex-bootstrap.sh
```

## Installation

```bash
npx skills add wisdomgraph/mega-code -a codex
```

## MEGA_DIR Setup (required in every skill that calls uv run)

```bash
MEGA_DIR="$(cat ~/.local/share/mega-code/pkg-breadcrumb 2>/dev/null)"
if [ -z "$MEGA_DIR" ] || [ ! -f "$MEGA_DIR/pyproject.toml" ]; then
  MEGA_DIR="$HOME/.local/share/mega-code/pkg"
  if [ ! -f "$MEGA_DIR/pyproject.toml" ]; then
    rm -rf "$MEGA_DIR"
    git clone --depth 1 "${MEGA_CODE_REPO_URL:-https://github.com/wisdomgraph/mega-code.git}" "$MEGA_DIR"
  fi
  bash "$MEGA_DIR/scripts/codex-bootstrap.sh" "$MEGA_DIR"
fi
```

All `uv run` commands must use `--directory "$MEGA_DIR"`.
Before any `uv run`, set the cache dir to avoid sandbox permission issues:

```bash
export UV_CACHE_DIR="${UV_CACHE_DIR:-$MEGA_DIR/.uv-cache}"
```

## Environment Loading

```bash
set -a && . "$MEGA_DIR/.env" 2>/dev/null && set +a
```

Always source `.env` before any Python command. Check `MEGA_CODE_API_KEY` is set
before making server calls.

## Skill Conventions

- Every `SKILL.md` must have `name:`, `description:`, and `allowed-tools:` frontmatter
- Use `disable-model-invocation: true` for skills that only run Bash commands
- Allowed tools should be minimal — prefer `Bash, Read` over unrestricted sets
- All commands in one Bash block so variables stay in scope across steps
