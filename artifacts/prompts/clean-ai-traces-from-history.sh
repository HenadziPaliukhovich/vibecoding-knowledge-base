#!/usr/bin/env bash
# Rewrites git history to strip AI-tell traces from commit messages:
# - "Co-Authored-By: Claude ..." trailers
# - "Generated with Claude Code" / "🤖 Generated with ..." lines
# - "As an AI..." style lines
# Usage: run from inside the target repo.
#   ./clean-ai-traces-from-history.sh            (rewrite current branch only)
#   ./clean-ai-traces-from-history.sh --all      (rewrite all branches and tags)
#
# DESTRUCTIVE: rewrites commit hashes on every touched commit.
# - Creates a backup branch first (backup/pre-ai-cleanup-<timestamp>).
# - Requires force-push afterwards; anyone else with a clone must re-clone or hard-reset.
# - Do not run this on a shared branch without warning collaborators first.

set -euo pipefail

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Error: not inside a git repository." >&2
  exit 1
 fi

if [[ -n "$(git status --porcelain)" ]]; then
  echo "Error: working tree is not clean. Commit or stash changes first." >&2
  exit 1
fi

SCOPE="${1:-}"
BACKUP_BRANCH="backup/pre-ai-cleanup-$(date +%Y%m%d%H%M%S)"
git branch "$BACKUP_BRANCH"
echo "Backup created: $BACKUP_BRANCH (restore with: git reset --hard $BACKUP_BRANCH)"

MSG_FILTER='sed -E \
  -e "/^Co-Authored-By: .*(Claude|Anthropic|AI).*$/d" \
  -e "/^🤖 ?Generated with.*$/Id" \
  -e "/^Generated with .*(Claude|AI).*$/Id" \
  -e "/^As an AI.*$/Id" \
  -e "/^\[AI\].*$/Id" \
  -e "/^Co-authored-by: .*noreply\.anthropic\.com.*$/Id"'

if command -v git-filter-repo >/dev/null 2>&1; then
  echo "Using git-filter-repo."
  if [[ "$SCOPE" == "--all" ]]; then
    git filter-repo --force --message-callback "
 import re
 patterns = [
     r'^Co-Authored-By:.*(Claude|Anthropic|AI).*$',
     r'^\xf0\x9f\xa4\x96 ?Generated with.*$',
     r'^Generated with .*(Claude|AI).*$',
     r'^As an AI.*$',
     r'^\\[AI\\].*$',
 ]
 lines = message.decode('utf-8', 'ignore').splitlines()
 kept = [l for l in lines if not any(re.match(p, l, re.IGNORECASE) for p in patterns)]
 return ('\n'.join(kept)).strip().encode('utf-8') + b'\n'
"
  else
    CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
    git filter-repo --force --refs "$CURRENT_BRANCH" --message-callback "
 import re
 patterns = [
     r'^Co-Authored-By:.*(Claude|Anthropic|AI).*$',
     r'^\xf0\x9f\xa4\x96 ?Generated with.*$',
     r'^Generated with .*(Claude|AI).*$',
     r'^As an AI.*$',
     r'^\\[AI\\].*$',
 ]
 lines = message.decode('utf-8', 'ignore').splitlines()
 kept = [l for l in lines if not any(re.match(p, l, re.IGNORECASE) for p in patterns)]
 return ('\n'.join(kept)).strip().encode('utf-8') + b'\n'
"
  fi
else
  echo "git-filter-repo not found, falling back to 'git filter-branch' (slower, legacy)."
  echo "Tip: install git-filter-repo for a faster/safer rewrite: brew install git-filter-repo"
  export FILTER_BRANCH_SQUELCH_WARNING=1
  RANGE="--all"
  if [[ "$SCOPE" != "--all" ]]; then
    RANGE="HEAD"
  fi
  git filter-branch --force --msg-filter "$MSG_FILTER" -- "$RANGE"
fi

echo ""
echo "Done. Review the rewritten history:"
echo "  git log --oneline -20"
echo ""
echo "If it looks correct, push it:"
echo "  git push --force-with-lease origin $(git rev-parse --abbrev-ref HEAD)"
echo ""
echo "If something went wrong, restore with:"
echo "  git reset --hard $BACKUP_BRANCH"
