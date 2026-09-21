# Vibe Coding Flow

A focused three-step guide for turning an idea into a deployed product with Claude Code.

## The flow

1. Create a project folder and start Claude Code.
2. Copy one prompt to create the project's `CLAUDE.md` working rules.
3. Describe the idea; Claude clarifies, plans, tests, implements, reviews, commits, and deploys.

## Run locally

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000`.

## Deploy

GitHub Pages deploys automatically after a push to `main`:

`https://henadzipaliukhovich.github.io/vibecoding-knowledge-base/`

## Files

- `index.html` — the complete site
- `CLAUDE.md` — project rules for Claude
- `.claude/settings.json` — deterministic hooks configuration
