#!/usr/bin/env python3
import json
import re
import sys

payload = json.load(sys.stdin)
command = payload.get("tool_input", {}).get("command", "")
normalized = " ".join(command.strip().split())

if re.search(r"\bgit\s+commit\b", normalized):
    # Check that ruff and mypy are not actively failing by inspecting the command.
    # Advisory reminder — agent must confirm checks pass before proceeding.
    print(
        "STOP: Before committing, confirm that ruff check and mypy (for Python projects) "
        "and all other relevant linters/tests currently pass. "
        "Do not commit with failing checks — fix them first, then commit.",
        file=sys.stderr,
    )
    sys.exit(2)

sys.exit(0)
