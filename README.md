# n8n Workflows

Ready-to-import [n8n](https://n8n.io) workflows, each with a complete beginner-friendly setup guide.

Every workflow lives in its own folder with the same layout, so once you've set one up, the rest feel familiar.

## Workflows

| Workflow | What it does | Apps | AI | Guide |
|---|---|---|---|---|
| [Gmail Auto-Labeler](gmail-auto-labeler/) | Labels every new email automatically. Sender rules first (free), AI only for the rest. All settings in a Google Sheet; every success and error logged. | Gmail, Google Sheets, Groq | Yes (free tier) | [SETUP.md](gmail-auto-labeler/SETUP.md) |
| [Nightly n8n → GitHub Backup](github-backup) | Backs up every n8n workflow to a private GitHub repo each night as one commit. Dated snapshots, a `latest/` folder for restoring, secret scan, Telegram alerts. | GitHub, Telegram, n8n API | No | [SETUP.md](github-backup/SETUP.md) |

*More coming.*

## Folder layout

```text
n8n-workflows/
├── README.md                     ← you are here (index of all workflows)
├── _template/                    ← copy this to start a new workflow folder
├── github-backup/                ← nightly backup of all your workflows
├── gmail-auto-labeler/
│   ├── README.md                 ← what it does, at a glance
│   ├── SETUP.md                  ← full step-by-step setup guide
│   ├── CHANGELOG.md              ← version history
│   ├── workflow/                 ← importable n8n JSON files
│   ├── config/                   ← templates (Google Sheet, CSVs)
│   └── images/                   ← screenshots used in the guides
└── scripts/check_workflows.py    ← safety check run on every push
```

## How to use a workflow

1. Open the workflow's folder and read its **README.md** (2 minutes).
2. Follow its **SETUP.md** from top to bottom. Each step has a ✅ checkpoint.
3. In n8n, import the JSON from the `workflow/` folder: create a new workflow → **⋯ → Import from File…**

All workflows are tested on **n8n 2.x** (self-hosted Docker). Guides use `https://n8n.snova.com` as a placeholder for your own n8n address.

## Safety

- **No secrets in this repo.** Exported n8n workflows hold credential *names* only, never passwords, tokens or API keys. Every push runs [`scripts/check_workflows.py`](scripts/check_workflows.py), which fails if anything that looks like a key sneaks in.
- **Nothing destructive by default.** No workflow here deletes, archives or sends anything unless its guide says so and you turn it on.
- **Test before you publish.** Every guide includes a manual test path.

## Adding a new workflow (for maintainers)

1. Copy `_template/` to a new folder named in `kebab-case`, e.g. `github-backup/`.
2. In n8n: open the workflow → **⋯ → Download**. Save it into `workflow/`.
3. Replace personal data (emails, sheet URLs, chat IDs) with placeholders like `you@example.com`.
4. Fill in `README.md`, `SETUP.md` and `CHANGELOG.md` from the template.
5. Add a row to the table above.
6. Run `python scripts/check_workflows.py` before committing.

## License

[MIT](LICENSE). Use, change and share freely.