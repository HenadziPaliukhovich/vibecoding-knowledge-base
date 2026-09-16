#!/usr/bin/env python3
import json
import sys

payload = json.load(sys.stdin)
file_paths = payload.get("tool_response", {}).get("file_paths") or []
if file_paths:
    changed = ", ".join(file_paths)
    print(f"Edited files: {changed}. Remember to run the relevant checks before committing.")
else:
    print("Files were edited. Remember to run the relevant checks before committing.")
