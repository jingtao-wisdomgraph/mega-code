# MEGA Code 1.0.1-beta

**AI agents that evolve autonomously. Developers that never stop learning.**

MEGA Code automatically captures your real coding sessions and converts them into durable, reusable knowledge — Skills and Strategies — so your AI agent gets smarter every session.

---

## Why MEGA Code

Today's AI coding agents start every session from zero — same errors, same rework, no memory of what worked before.

MEGA Code solves this with **Compound Intelligence**:

- **Skills** — Reusable know-how extracted from real coding sessions that agents can execute again and again, eliminating repeated mistakes.
- **Strategies** — Decision guidance that resurfaces in similar situations, so agents make better choices over time.

The extraction pipeline runs remotely, uses your own LLM key (BYOK), and produces assets that dramatically lower repeated errors across sessions.

---

## Real Work. Real Results.

Measured head-to-head against 5 leading systems on tasks developers actually ship.

<table>
<tr>
<td align="center"><h3>1/5</h3><b>Token Usage</b><br><sub>vs no-skill baseline</sub><br><sub>169K tokens vs 897K baseline</sub></td>
<td align="center"><h3>#1</h3><b>Highest Score</b><br><sub>against 5 competing systems</sub><br><sub>78% combined avg — 4 skills x 2 models</sub></td>
<td align="center"><h3>3x</h3><b>Structural Quality</b><br><sub>vs competitor average</sub><br><sub>16/16 score across 8 structural dimensions</sub></td>
</tr>
</table>

### Token Usage

```
MEGA Code        ████░░░░░░░░░░░░░░░░  169K   ← 81% reduction
HF Upskill       ████████████████░░░░  763K
anthropic-skill  █████████████████░░░  826K
Baseline         ██████████████████░░  897K
skill-factory    ██████████████████████████████  1,448K
```

### Combined Score

```
MEGA Code        ████████████████  78%   ← #1
HF Upskill       ██████████████░░  70%
anthropic-skill  █████████████░░░  65%
Baseline         █████████████░░░  65%
skill-factory    █████████░░░░░░░  43%
```

> [See the full benchmark →](https://www.megacode.ai/performance)

---

## Quick Start

### Step 1 — Install

```bash
npx skills add https://github.com/wisdomgraph/mega-code/tree/codex -a codex
```

### Step 2 — Sign in

```
$mega-code-login
```

Authenticates via GitHub or Google. Your API key is saved automatically.

### Step 3 — Add your own LLM API key

MEGA Code uses a **Bring Your Own Key (BYOK)** model — you supply your own Gemini or OpenAI key.

Visit [console.megacode.ai](https://console.megacode.ai) → **Account → API Keys** to register your key.

### Step 4 — Run in any project

```
$mega-code-run                    # Extract skills from your sessions
$mega-code-status                 # Check results
```

---

## Free to Start

MEGA Code is currently free to use — just bring your own LLM API key (Gemini or OpenAI).
Core learning, exports, and Skills/Strategies capture are available in the current release.

---

## Available Commands

| Command | Description |
|---|---|
| `$mega-code-login` | Sign in via GitHub or Google OAuth |
| `$mega-code-run` | Run skill extraction pipeline |
| `$mega-code-status` | Show pending items and status |
| `$mega-code-profile` | View or update your developer profile (language, level, style) |
| `$mega-code-help` | Show help and reference |

### Example Session

```bash
$mega-code-login                  # Sign in (first time)
$mega-code-profile                # Set your language, level, and style
$mega-code-run --project          # Extract skills from all project sessions
$mega-code-status                 # See what was generated
```

---

## Update

```bash
npx skills add https://github.com/wisdomgraph/mega-code/tree/codex -a codex
```

---

## Configuration

Configuration is stored in `~/.local/share/mega-code/` and persists across sessions.
Use `$mega-code-login` to authenticate, or `mega-code configure` CLI for advanced settings.

## Terms of Service

By using this plugin, you agree to the [Terms of Service](https://megacode.ai/terms).

## License

Apache-2.0
