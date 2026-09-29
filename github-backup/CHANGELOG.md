# Changelog

## 1.0 — First version
- Schedule Trigger (02:00) and Manual Trigger run the same chain; the Config node detects which fired.
- One commit per run via GitHub's Git Data API (blobs → tree → commit → update ref), instead of the GitHub node's one-file-per-commit Contents API.
- Dated snapshots in `backups/YYYY-MM-DD/` plus a mirrored `latest/` folder and a `_manifest.json` index.
- Same-day reruns replace that day's folder, including deletions, using tree entries with `sha: null`.
- Secret scan over every node halts the run before upload and names the workflow and node.
- Safety guards: refuses to run on 0 workflows, on a >50% drop versus `latest/`, on a truncated GitHub file list, and on any path outside today's folder and `latest/`.
- Telegram alert on every run; eight nodes route their error output to one failure message, which reports the failed step via `$prevNode.name`.
- Separate error workflow for crashes, with de-duplication so one failure never sends two messages.
- Test mode: 2 workflows into a `test/` prefix.