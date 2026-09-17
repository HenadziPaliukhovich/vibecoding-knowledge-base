#!/usr/bin/env python3
import json
import re
import sys

payload = json.load(sys.stdin)
command = payload.get("tool_input", {}).get("command", "")
normalized = " ".join(command.strip().split())

if re.search(r"\bgit\s+commit\b", normalized):
    print(
        "Before committing: confirm tests and linters currently pass. "
        "Do not commit with failing checks \u2014 fix them first, then commit.",
        file=sys.stderr,
    )

sys.exit(0)
