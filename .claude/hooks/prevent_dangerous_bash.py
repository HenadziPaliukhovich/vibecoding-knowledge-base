#!/usr/bin/env python3
import json
import re
import sys

payload = json.load(sys.stdin)
command = payload.get("tool_input", {}).get("command", "")
normalized = " ".join(command.strip().split())

blocked_patterns = [
    (r"\bgit\s+push\b.*\borigin\s+main\b", "Direct pushes to origin main are blocked. Push to a feature branch or open a PR."),
    (r"\brm\s+-rf\b", "rm -rf is blocked. Move files to Trash or inspect the target first."),
]

for pattern, message in blocked_patterns:
    if re.search(pattern, normalized):
        print(message, file=sys.stderr)
        sys.exit(2)

sys.exit(0)
