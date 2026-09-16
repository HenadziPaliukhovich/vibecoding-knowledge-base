# Vibe Coding Knowledge Base

A static knowledge base for vibe coding: practical guidance, QA checklists, prompt templates, and example `CLAUDE.md` files.

## Site

Once GitHub Pages is enabled, the site is available at:

`https://henadzipaliukhovich.github.io/vibecoding-knowledge-base/`

## Run locally

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000`.

## Updating

```bash
git add .
git commit -m "Update knowledge base"
git push
```

Deployment runs automatically after every push to `main`. To redeploy without changing files: **Actions → Deploy GitHub Pages → Run workflow**.

## Structure

- `index.html` — the site
- `CLAUDE.md` — rules for the AI agent
- `.claude/settings.json` — hooks configuration (deterministic enforcement)
- `artifacts/` — reusable prompts, checklists, and examples
- `.github/workflows/deploy-pages.yml` — automated deployment
