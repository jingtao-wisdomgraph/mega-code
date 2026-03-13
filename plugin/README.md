# MEGA-Code Plugin

An open-source Claude Code plugin that collects interaction data, extracts
reusable skills, and optimizes AI workflows.

## Install

Install directly from GitHub via Claude Code:

```
/plugin marketplace add https://github.com/wisdomgraph/mega-code.git
/plugin install mega-code@wisdomgraph-mega-code
```

Or add the entry to your Claude Code `marketplace.json` manually:

```json
{
  "plugins": [
    {
      "name": "mega-code",
      "source": "https://github.com/wisdomgraph/mega-code.git"
    }
  ]
}
```

## Quick Start

After installation, configure your API key:

```bash
mega-code login
```

Or set it manually:

```bash
mega-code configure --api-key <your_key>
```

Check status:

```bash
mega-code status
```

## Documentation

Full documentation is available at [megacode.ai](https://megacode.ai).

## License

Apache 2.0 — see [LICENSE](../LICENSE).
