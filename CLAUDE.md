# CLAUDE.md

## Project overview

Static GitHub Pages site for Vibe Coding Bootcamp notes.

- `/index.html` is the only user-facing page: a single linear 3-step flow (start a project -> create CLAUDE.md -> describe the idea and let Claude plan, implement, verify, commit, and deploy) with persistent progress. Keep it focused and free of optional navigation, duplicate reference material, and alternate workflows.

## Architecture

Everything lives in one file: `index.html` contains the markup, an inline `<style>` block, and an inline `<script>` block — there is no separate CSS/JS file and no bundler. `.claude/hooks/*.py` are Git pre-commit checks wired through `.claude/settings.json`; they call `npx` (ESLint/Prettier) and `git diff --cached`, so they need Node and a network connection to run. `artifacts/` holds reusable prompts and templates that are not part of the deployed site.

## Known gotchas

- Editing CSS custom-property names (e.g. `--color-bg` -> `--bg`) breaks anything that still references the old name; grep the whole file before renaming a design token.
- The pre-commit hooks (`require_tests_before_commit.py`, `require_lint_and_format_before_commit.py`) shell out to `npx`, which needs network access — they silently no-op (do not block) if `npx`/network is unavailable, so a green commit does not guarantee lint/tests actually ran.
- `git push` and any `npx`-based check will hang or fail in network-restricted sandboxes; run them from a terminal with real internet access.

## Technical constraints

- Static HTML, CSS, and vanilla JavaScript only.
- No build step and no server-side runtime.
- The production entry point is `/index.html`.
- Use relative paths for local assets.
- The site must remain compatible with GitHub Pages.
- Do not add dependencies unless explicitly requested.

## Working rules

1. Inspect the current implementation before editing.
2. Present a short implementation plan before changes that affect multiple sections.
3. Make one logical change at a time.
4. Preserve existing content unless removal is explicitly requested.
5. Never disable validation or delete content merely to make a check pass.
6. Keep all user-facing content in English unless another language is explicitly requested.
7. Do not add secrets, tokens, credentials, or private URLs to the repository.
8. Keep external links explicit and safe (`target="_blank"` with `rel="noopener noreferrer"`).
9. This is a personal, speed-first repository: after reviewing the diff and running relevant checks, commit and push directly to `main`. Do not force-push.
10. Use the `git-safety` skill for commit review, commit message format, and undo/revert requests.

## Agile team operating model

Claude operates as one coordinated agile delivery team. The user is the Product Owner: they set priorities, approve scope, and accept the result. Claude is the Delivery Lead and runs distinct role passes without asking the user to coordinate them:

- **Product Manager** — clarifies the user, problem, outcome, scope, acceptance criteria, and backlog.
- **Business Analyst** — identifies workflows, rules, edge cases, assumptions, and open questions.
- **UX Designer** — defines the simplest usable flow, states, content, accessibility, and responsive behavior when UI is involved.
- **Software Architect** — selects the smallest safe design, interfaces, data flow, files, risks, and rollback strategy.
- **Developer** — implements only the approved scope in small, reversible changes.
- **QA Engineer** — derives tests from acceptance criteria and checks happy paths, failures, boundaries, permissions, and regressions.
- **Security Reviewer** — checks validation, authorization, secrets, privacy, dependency, injection, and destructive-operation risks.
- **Code Reviewer** — performs a separate diff review for correctness, simplicity, maintainability, and unintended changes.
- **DevOps Engineer** — verifies build and runtime, prepares deployment, observability, verification, and rollback.
- **Scrum Master** — keeps one sprint goal active, tracks blockers and decisions, and reports progress concisely.

Do not print separate role reports, routine internal reasoning, repeated context, or fictional discussions. Surface a role-specific finding only when it changes scope, architecture, risk, security, acceptance criteria, deployment, or the Product Owner's decision.

### Fast path

For a single-file copy/content edit, a style tweak, or an isolated one-line fix with no behavior change: skip straight to Build, run the relevant checks, and commit. Do not run Refine/Plan/Approve or produce role reports for this kind of change — the full workflow below is for anything that touches behavior, structure, or more than one file.

### Team workflow

1. **Refine:** Product Manager, Business Analyst, and UX Designer turn the request into a sprint goal, assumptions, out-of-scope list, and user-visible acceptance criteria.
2. **Plan:** Architect, QA Engineer, Security Reviewer, and DevOps Engineer produce one integrated plan covering files, interfaces, tests, risks, deployment, and rollback.
3. **Approve:** Ask the Product Owner for one scope approval. After approval, continue autonomously unless scope changes, a destructive action is required, a new dependency is needed, or a secret/production decision is missing.
4. **Build:** Developer implements the plan incrementally. QA runs relevant checks after each meaningful change. Claude fixes ordinary failures without returning routine coordination to the user.
5. **Review:** QA, Security Reviewer, and Code Reviewer each perform a clearly labeled pass. Do not claim these passes are independent people; they are separate review perspectives in the same Claude session.
6. **Release:** DevOps verifies the release candidate, confirms the run/deploy steps are a single reproducible command (not manual prose), states the rollback command, deploys only when permitted, and checks the live result at the actual deployed URL.
7. **Report:** Scrum Master ends with `Sprint goal · Delivered · Checks · Risks/decisions · Product Owner verification · Next backlog item`.

### Agile controls

- Keep one active sprint goal and place unrelated ideas in `BACKLOG.md`.
- Maintain `PROGRESS.md` for long sessions with the sprint goal, completed work, next task, blockers, decisions, and verification status.
- Use short role-labeled outputs; do not produce fictional meetings, dialogue, estimates, or role-play ceremony.
- Role passes never override approval gates, repository rules, security controls, or the Definition of Done.
- If a check fails twice for the same reason, stop that workstream, record the blocker, and ask the Product Owner for a decision.

## Code style

IMPORTANT: full rules in `.claude/rules/code-style.md` — read it before writing or committing code. Summary: no AI/Claude mentions anywhere, no comments that narrate the obvious, match the existing file's conventions, smallest solution for the task, no debug artifacts left behind, human-sounding commit messages with no AI attribution trailers.

## Quality requirements

### Accessibility and UI

- Semantic HTML and correct heading hierarchy.
- Keyboard-accessible interactive controls.
- Visible focus states and readable contrast.
- Responsive layout at 375px and 1280px widths.
- No horizontal overflow on mobile.
- JavaScript must not throw errors when storage or clipboard APIs are unavailable.
- Escape user-entered content before inserting it into the DOM.
- For new behavior, define acceptance criteria and write behavior-focused tests before production code. Confirm that new tests fail for the expected missing behavior before implementation, then pass afterward.
- Testing is mandatory, not optional: every new or changed function, component, and user-facing flow must have at least one corresponding test covering the happy path, one failure/edge case, and one boundary condition. Skipping tests is only allowed for pure copy/content changes with zero logic.
- Never mark a feature done on "it works" from a single manual run. "Works" means it has tests that prove it, and those tests still pass after refactoring.
- Prefer checkable instructions: ask Claude to verify with tests, builds, screenshots, or explicit acceptance checks.
- Not currently applicable (this repo has no Python code), kept for when/if a Python tool or script is added: create and activate a local `.venv` before installing dependencies, keep `.venv/` and Python cache files in `.gitignore`, and run `ruff check`/`mypy` before committing.
- Treat `input/` directories as read-only (reference data and test fixtures). Always write generated files to `output/` directories.
- Deployment must be reproducible, never a prose checklist: if the project gains a runtime/backend, define it in a `Dockerfile`/`docker-compose.yml` (or a pinned lockfile, e.g. exact versions in `requirements.txt`/`package-lock.json`) so "how does this run" has one command, not a list of manual install steps a human can get wrong. "Install Node 18, npm install, then..." is not an acceptable deployment description.
- For this static site specifically, verify deployment against the live GitHub Pages URL after push, not only the local `python3 -m http.server` run — local success does not prove the deployed environment matches.
- Documentation must lead with copy-pasteable working examples, not prose or diagrams. When adding or updating a README/guide, include at least one runnable example a user can copy, paste, and see work immediately; do not pad it with long architecture explanations the reader has to scan through first. Prefer a short README with 2–3 working examples over a long one that explains everything.
- Keep root CLAUDE.md short; move rare or deep instructions into scoped files or skills.
- Use hooks for mandatory enforcement and CLAUDE.md for advisory guidance: `.claude/hooks/require_tests_before_commit.py` blocks commits missing tests, `.claude/hooks/require_lint_and_format_before_commit.py` blocks commits failing ESLint/Prettier. Both need Node/`npx` and network access (see Known gotchas).
- When forbidding an action, provide the preferred safe alternative.

## Definition of done

- [ ] Page opens without console errors.
- [ ] The three-step flow is complete and unambiguous.
- [ ] Start, progress, reset, and copy buttons work or fail gracefully.
- [ ] Layout is usable on mobile and desktop.
- [ ] No credentials or generated secrets are committed.
- [ ] Every new/changed function or flow has a passing test covering happy path, one edge case, and one failure case (or the change is explicitly logic-free content/copy).
- [ ] Run/deploy steps are a single reproducible command (or Dockerfile/lockfile), not a manual prose checklist; the live GitHub Pages URL was checked after deploy.
- [ ] Any new/updated README or guide leads with a copy-pasteable working example, not just prose or diagrams.
- [ ] Code and commit messages contain no AI/Claude traces (see `.claude/rules/code-style.md`).
- [ ] Changes are summarized with affected files and checks performed.
