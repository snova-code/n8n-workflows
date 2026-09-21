# Changelog

## 4.1 — Nested labels
- Label paths are cleaned (`Dev / GitHub` → `Dev/GitHub`).
- AI short answers (`PRs` for `Dev/GitHub/PRs`) accepted when unique.
- New `apply_parents` setting adds parent labels too.
- Parent labels created before children.

## 4.0 — Google Sheets config and reporting
- All settings moved to a Google Sheet: Settings, Categories, Rules.
- Sender rules run before the AI; `skip_ai` per rule.
- Log tab for successes, Errors tab for failures.
- Instant alert for sync/sheet problems, daily summary email, separate crash error handler.

## 3.3 — Rate-limit tolerant
- AI node: Retry On Fail off (it re-ran the whole batch), On Error → Continue.
- Failed AI calls are logged and retried next run.
- Marker label renamed to `n8n-p` and hidden from the message list.

## 3.2 — No repeats
- Hidden marker label on every handled email; triggers exclude it, so backlog runs move forward.

## 3.1 — Pacing
- Basic LLM Chain batch size 5 → 1 with a 20 s delay (the default of 5 exceeded Groq's per-minute limit).

## 3.0 — Label sync, multiple labels
- Missing labels created automatically; alert for labels not in config.
- Several labels per email, plus STARRED and IMPORTANT.

## 2.0 — Dynamic labels
- Categories kept in one config node; one Add Label node instead of one per category.

## 1.0 — First version
- Gmail Trigger → Text Classifier (Groq) → one Add Label node per category.
