---
description: View or update your MEGA-Code developer profile (language, level, style) to personalise skill extraction.
argument-hint: [--language <lang>] [--level Beginner|Intermediate|Expert] [--style Mentor|Formal|Concise] [--reset]
allowed-tools: Bash, AskUserQuestion
---

# Developer Profile

Set up your developer profile to personalise skill and lesson extraction.
The profile determines which skills are generated and how output is presented.

## Finding the MEGA-Code Directory

```bash
MEGA_DIR="$(cat ~/.local/mega-code/plugin-root 2>/dev/null || echo $HOME/.claude/mega-code)"
```

## Interactive Setup (Recommended)

Ask the user for their profile using `AskUserQuestion` with these fields:

- **language**: Preferred communication language — common options: `English`, `Korean`, `Thai`
  (user can type a custom language via "Other")
- **level**: `Beginner`, `Intermediate`, or `Expert`
  (used to filter out skills too basic for their experience level)
- **style**: `Mentor`, `Formal`, or `Concise`

After collecting answers, save with:

```bash
MEGA_DIR="$(cat ~/.local/mega-code/plugin-root 2>/dev/null || echo $HOME/.claude/mega-code)"
set -a && . "$MEGA_DIR/.env" 2>/dev/null && set +a && \
  uv run --directory "$MEGA_DIR" python -m mega_code.client.cli profile \
    --language "<language>" \
    --level <level> \
    --style <style>
```

## Show Current Profile

```bash
MEGA_DIR="$(cat ~/.local/mega-code/plugin-root 2>/dev/null || echo $HOME/.claude/mega-code)"
set -a && . "$MEGA_DIR/.env" 2>/dev/null && set +a && \
  uv run --directory "$MEGA_DIR" python -m mega_code.client.cli profile
```

## Update Individual Fields

Any subset of fields can be updated — omitted fields keep their existing values:

```bash
MEGA_DIR="$(cat ~/.local/mega-code/plugin-root 2>/dev/null || echo $HOME/.claude/mega-code)"
set -a && . "$MEGA_DIR/.env" 2>/dev/null && set +a && \
  uv run --directory "$MEGA_DIR" python -m mega_code.client.cli profile \
    --level Expert
```

### Field Options

| Field | Options |
|-------|---------|
| `--language` | Any language string, e.g. `English`, `Thai`, `Korean`, `Japanese` |
| `--level` | `Beginner`, `Intermediate`, `Expert` |
| `--style` | `Mentor`, `Formal`, `Concise` |

## Reset Profile

Remove all profile settings and revert to defaults:

```bash
MEGA_DIR="$(cat ~/.local/mega-code/plugin-root 2>/dev/null || echo $HOME/.claude/mega-code)"
set -a && . "$MEGA_DIR/.env" 2>/dev/null && set +a && \
  uv run --directory "$MEGA_DIR" python -m mega_code.client.cli profile --reset
```

## Profile Storage

Profile is stored at: `~/.local/mega-code/profile.json`

Applied automatically during pipeline runs to:
- Filter out skills too basic for the user's experience level
- Personalise generated lessons, skills, and strategies
- Adapt communication language and style
