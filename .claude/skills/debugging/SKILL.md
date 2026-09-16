---
name: debugging
description: Use when the user reports a bug, error, crash, unexpected behavior, or asks to fix something that is broken.
---

# Skill: debugging

A systematic, evidence-first process for fixing bugs — avoid guessing at fixes before understanding the failure.

## Process

1. **Reproduce first.** Get (or construct) the exact steps, input, or command that triggers the bug. If you cannot reproduce it, say so explicitly and ask for more detail (exact error text, stack trace, browser/OS, steps) instead of guessing at a fix.
2. **Read the actual error.** Capture the full error message and stack trace — not a paraphrase. Identify the exact file and line where it originates, not just where it surfaces.
3. **Form a hypothesis.** State in one sentence what you think is causing the bug, based on the code and the error — before editing anything.
4. **Verify the hypothesis** with the smallest possible check: a targeted log/print, a quick script, reading the relevant function, or a minimal repro — before writing the real fix.
5. **Fix the root cause, not the symptom.** Prefer a fix that addresses why the bug happened over one that only suppresses the visible error (e.g. don't wrap a broken call in try/except just to stop the crash).
6. **Verify the fix** by re-running the original repro steps and confirming the bug no longer occurs.
7. **Check for regressions.** Run existing tests if present; consider whether the fix could affect other call sites of the changed code.

## Never do

- Never claim a bug is fixed without having reproduced and re-verified it.
- Never silently swallow an error (bare `except: pass`, empty `catch {}`) as the "fix".
- Never make broad, unrelated changes while chasing a bug — keep the diff scoped to the root cause.

## When stuck

If reproduction fails after reasonable attempts, or the root cause is unclear after investigation, say so explicitly and lay out what was tried and what additional information (logs, exact repro steps, environment) is needed — rather than shipping a speculative fix.
