#!/usr/bin/env python3
"""Safety check for n8n workflow exports.

Fails (exit code 1) if:
  - any workflow/*.json file is not valid JSON or not an n8n workflow
  - any file looks like it contains a secret (API keys, tokens, private keys)
  - a workflow folder is missing README.md or SETUP.md

Run locally:  python scripts/check_workflows.py
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SECRET_PATTERNS = {
    "Groq API key": r"gsk_[A-Za-z0-9]{20,}",
    "OpenAI API key": r"sk-[A-Za-z0-9_-]{20,}",
    "GitHub token": r"(ghp|gho|ghu|ghs|github_pat)_[A-Za-z0-9_]{20,}",
    "Google API key": r"AIza[0-9A-Za-z_-]{30,}",
    "Slack token": r"xox[abprs]-[A-Za-z0-9-]{10,}",
    "Telegram bot token": r"\b\d{8,10}:[A-Za-z0-9_-]{35}\b",
    "Private key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    "Google OAuth client secret": r"GOCSPX-[A-Za-z0-9_-]{20,}",
}
TEXT_SUFFIXES = {".json", ".md", ".csv", ".txt", ".yml", ".yaml", ".py", ".js"}

problems = []

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.suffix not in TEXT_SUFFIXES:
        continue
    if path.name == "check_workflows.py":
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    rel = path.relative_to(ROOT)
    for name, pattern in SECRET_PATTERNS.items():
        if re.search(pattern, text):
            problems.append(f"{rel}: looks like it contains a {name}")
    if path.suffix == ".json" and path.parent.name == "workflow":
        try:
            data = json.loads(text)
        except json.JSONDecodeError as exc:
            problems.append(f"{rel}: invalid JSON ({exc})")
            continue
        if not isinstance(data, dict) or "nodes" not in data or "connections" not in data:
            problems.append(f"{rel}: not an n8n workflow export (missing nodes/connections)")

for folder in ROOT.iterdir():
    if folder.is_dir() and (folder / "workflow").is_dir() and not folder.name.startswith("_"):
        for required in ("README.md", "SETUP.md"):
            if not (folder / required).exists():
                problems.append(f"{folder.name}/: missing {required}")

if problems:
    print("❌ Check failed:\n" + "\n".join(f"  - {p}" for p in problems))
    sys.exit(1)
print("✅ All workflow folders look safe and valid.")
