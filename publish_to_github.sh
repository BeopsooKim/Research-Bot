#!/usr/bin/env bash
set -euo pipefail

REPO_OWNER="BeopsooKim"
REPO_NAME="Research-Bot"
RELEASE_VERSION="v1.0.0"
DESCRIPTION="Research Bot: Korean/English ECE Codex Skill suite for methodology review, data troubleshooting, critical thinking, artifact review, code/simulation review, literature scouting, ethics, and research roadmaps."

if ! command -v git >/dev/null 2>&1; then
  echo "git is required." >&2
  exit 1
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required. Install it first, then run: gh auth login" >&2
  exit 1
fi

if [ -d .git ]; then
  echo "Existing git repository detected. Continuing."
else
  git init
fi

git add .
if git diff --cached --quiet; then
  echo "No staged changes to commit."
else
  git commit -m "Initial public release v1.0.0"
fi

if gh repo view "$REPO_OWNER/$REPO_NAME" >/dev/null 2>&1; then
  echo "Repository $REPO_OWNER/$REPO_NAME already exists."
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "https://github.com/$REPO_OWNER/$REPO_NAME.git"
  fi
  git push -u origin HEAD
else
  gh repo create "$REPO_OWNER/$REPO_NAME" --public --description "$DESCRIPTION" --source=. --remote=origin --push
fi

if git rev-parse "$RELEASE_VERSION" >/dev/null 2>&1; then
  echo "Tag $RELEASE_VERSION already exists."
else
  git tag "$RELEASE_VERSION"
fi

git push origin "$RELEASE_VERSION"

echo "Published $REPO_OWNER/$REPO_NAME at $RELEASE_VERSION"
