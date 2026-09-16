---
name: deploy
description: Use when the user asks to deploy, publish, redeploy, or ship the site to GitHub Pages, or asks why a deployment failed.
---

# Skill: deploy

This project deploys to GitHub Pages via a GitHub Actions workflow at `.github/workflows/deploy-pages.yml`. There is no build step — the repository root is uploaded as the Pages artifact, with `index.html` as the entry point.

## Deployment triggers

- Automatic: every push to `main`.
- Manual: open the repository on GitHub, go to Actions, select "Deploy GitHub Pages", click "Run workflow". Use this to redeploy without a new commit (e.g. after a transient failure, or to re-publish the current `main` state).

## Standard deploy flow

1. Verify working tree is clean: `git status`.
2. Stage and commit changes with a clear message: `git add -A && git commit -m "..."`.
3. Push to `main`: `git push`.
4. Confirm the workflow run succeeded (ask the user to check the Actions tab, or use `gh run list --workflow=deploy-pages.yml` / `gh run watch` if the GitHub CLI is authenticated).
5. Report the live URL: `https://<owner>.github.io/<repo>/`.

## Never do

- Never force-push (`git push --force` / `-f`) to `main`.
- Never push directly to `origin main` without the user's explicit go-ahead for that specific change — the pre-tool-use hook will block it; use a feature branch + PR when in doubt.
- Never edit files inside `.github/workflows/` without explaining the change first — workflow edits affect deploy behavior for everyone.

## Troubleshooting a failed deploy

1. Read the failing job's logs (via `gh run view --log-failed` if CLI is available, otherwise ask the user to paste the Actions log).
2. Common causes: missing `index.html` at repo root, Pages source not set to "GitHub Actions" in Settings → Pages, missing `permissions: pages: write / id-token: write` in the workflow, or a broken relative asset path.
3. Fix the root cause, commit, push, and re-verify — do not just re-run the workflow blindly unless the failure was transient (e.g. a GitHub outage).

## Local preview before deploying

Since this is a static site with no build step, preview by opening `index.html` directly or serving the folder locally, e.g.:

```bash
python3 -m http.server 8000
```

Then check `http://localhost:8000/index.html` at both desktop and mobile widths before pushing.
