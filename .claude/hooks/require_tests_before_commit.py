#!/usr/bin/env python3
import json
import re
import subprocess
import sys

payload = json.load(sys.stdin)
command = payload.get("tool_input", {}).get("command", "")
normalized = " ".join(command.strip().split())

if not re.search(r"\bgit\s+commit\b", normalized):
    sys.exit(0)

try:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        capture_output=True,
        text=True,
        timeout=5,
    )
    staged_files = [f for f in result.stdout.splitlines() if f.strip()]
except Exception:
    # If git is unavailable for any reason, do not block the commit.
    sys.exit(0)

if not staged_files:
    sys.exit(0)

# Files that count as "logic" changes and should be backed by tests.
logic_pattern = re.compile(r"\.(js|ts|py|jsx|tsx)$", re.IGNORECASE)
html_pattern = re.compile(r"\.html?$", re.IGNORECASE)

# Files that count as evidence that tests were written or updated.
test_pattern = re.compile(r"(^tests?/|[._-](test|spec)s?\.[a-z]+$)", re.IGNORECASE)

logic_changed = [f for f in staged_files if logic_pattern.search(f)]
html_changed = [f for f in staged_files if html_pattern.search(f)]
tests_changed = any(test_pattern.search(f) for f in staged_files)

if (logic_changed or html_changed) and not tests_changed:
    changed = ", ".join(logic_changed + html_changed)
    print(
        "STOP: Staged changes touch behavior-carrying file(s) "
        f"({changed}) but no test file is staged in this commit.\n"
        "Per CLAUDE.md, every new/changed function or flow needs a test "
        "covering happy path, one edge case, and one failure case.\n"
        "Before committing, either:\n"
        "  1) add/update the corresponding test(s) and stage them, or\n"
        "  2) confirm explicitly this change is logic-free content/copy "
        "with no behavior change, then re-run the commit.",
        file=sys.stderr,
    )
    sys.exit(2)

sys.exit(0)
