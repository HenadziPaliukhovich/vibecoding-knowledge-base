---
name: code-review
description: Use when the user asks to review code, review a diff/PR, check for bugs, or asks "is this code good/safe to merge".
---

# Skill: code-review

Follow the checklist in `artifacts/checklists/ai-code-review.md` as the baseline. This skill adds the review workflow and severity model on top of it.

## Workflow

1. Identify the scope: a specific file, a diff (`git diff`), or a PR. If scope is ambiguous, ask which files/commits to review rather than guessing.
2. Read the full context around changed lines, not just the diff hunks — changed code interacts with surrounding code.
3. Check the changes against every section of `artifacts/checklists/ai-code-review.md` (correctness, security, error handling, tests, readability, performance where relevant).
4. Classify every finding by severity:
   - **Blocker**: bugs, security issues, data loss risk, broken tests — must fix before merge.
   - **Should-fix**: design smells, missing error handling, missing tests for new logic.
   - **Nit**: naming, formatting, minor style — optional, call out but don't block on these alone.
5. Present findings grouped by severity, with file:line references, not as one long undifferentiated list.
6. If everything is clean, say so explicitly — don't invent nitpicks just to have something to say.

## What to flag every time

- Hardcoded secrets, tokens, or credentials.
- Missing input validation on anything user- or network-supplied.
- Silent failure (empty catch blocks, swallowed errors, unchecked return values).
- New logic added without a corresponding test.
- Commands or code that could be destructive (`rm -rf`, force pushes, unbounded loops touching disk/network) — flag as Blocker even if functionally "correct".

## Tone

Be direct and specific. Reference exact lines and explain *why* something is a problem, not just that it is. Prefer showing the fix (a short diff or snippet) over describing it in prose when the fix is small.
