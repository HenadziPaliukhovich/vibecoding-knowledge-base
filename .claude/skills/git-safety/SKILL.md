---
name: git-safety
description: Use when the user asks to save progress, commit, undo, revert, cancel changes, or when a logical step is finished and needs to be safely checkpointed.
---

# Skill: git-safety

Act as the user's Git assistant. They do not want to run git commands manually — you run them, on request, following this strict workflow.

## Before committing (the review)

1. Run `git status` and `git diff --staged` (or `git diff` if nothing is staged yet).
2. Summarize the changes in 1-2 plain-language sentences — no raw diff dumps.
3. Ask: "Shall I commit these changes?" Wait for explicit approval before staging or committing.

## When committing (the execution)

1. On approval, stage the relevant files (`git add`) — never `git add -A` blindly if unrelated files are also dirty.
2. Use Conventional Commits format for the message: `feat: ...`, `fix: ...`, `test: ...`, `docs: ...`, `refactor: ...`, `chore: ...`.
3. Do not commit if tests or linters are currently failing. Fix them first, or tell the user explicitly why you cannot commit yet.
4. After committing, report the commit hash and a one-line summary of what was saved.

## When undoing (the panic button)

If the user says "undo", "revert", or "cancel changes":

1. Run `git status` first to see what is uncommitted.
2. Show the user exactly what will be lost before doing anything destructive.
3. On confirmation, run `git restore .` (unstaged/tracked changes) and `git clean -fd` (untracked files) to return to the last committed state.
4. Confirm afterward that the working tree is clean (`git status` again).

## Never do

- Never force-push (`git push --force` / `-f`).
- Never run `git restore .` or `git clean -fd` without the user's explicit confirmation — these are destructive and cannot be undone.
- Never commit secrets, `.env` contents, or files matched by `.gitignore`.
