#!/usr/bin/env python3
import json
import re
import shutil
import subprocess
import sys

payload = json.load(sys.stdin)
command = payload.get("tool_input", {}).get("command", "")
normalized = " ".join(command.strip().split())

if not re.search(r"\bgit\s+commit\b", normalized):
    sys.exit(0)

if not shutil.which("npx"):
    # No Node/npx available on this machine — do not block the commit.
    sys.exit(0)

try:
    staged = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        capture_output=True,
        text=True,
        timeout=5,
    ).stdout.splitlines()
except Exception:
    sys.exit(0)

staged = [f.strip() for f in staged if f.strip()]
lint_pattern = re.compile(r"\.(html?|js|jsx|ts|tsx)$", re.IGNORECASE)
format_pattern = re.compile(r"\.(html?|css|js|jsx|ts|tsx|json|md)$", re.IGNORECASE)

lint_targets = [f for f in staged if lint_pattern.search(f)]
format_targets = [f for f in staged if format_pattern.search(f)]

if not lint_targets and not format_targets:
    sys.exit(0)

failures = []

if lint_targets:
    try:
        eslint = subprocess.run(
            [
                "npx", "--yes", "-p", "eslint", "-p", "eslint-plugin-html",
                "eslint", "--config", "eslint.config.js", *lint_targets,
            ],
            capture_output=True,
            text=True,
            timeout=90,
        )
        if eslint.returncode != 0:
            failures.append("ESLint:\n" + (eslint.stdout + eslint.stderr).strip())
    except Exception as exc:
        print(f"WARNING: could not run eslint ({exc}); not blocking on lint.", file=sys.stderr)

if format_targets:
    try:
        prettier = subprocess.run(
            ["npx", "--yes", "prettier", "--check", *format_targets],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if prettier.returncode != 0:
            failures.append("Prettier:\n" + (prettier.stdout + prettier.stderr).strip())
    except Exception as exc:
        print(f"WARNING: could not run prettier ({exc}); not blocking on format.", file=sys.stderr)

if failures:
    print(
        "STOP: Lint/format checks failed on staged file(s).\n\n"
        + "\n\n".join(failures)
        + "\n\nFix before committing:\n"
        f"  npx --yes prettier --write {' '.join(format_targets) or '<files>'}\n"
        f"  npx --yes -p eslint -p eslint-plugin-html eslint --config eslint.config.js --fix {' '.join(lint_targets) or '<files>'}\n"
        "Then re-stage the files and re-run the commit.",
        file=sys.stderr,
    )
    sys.exit(2)

sys.exit(0)
