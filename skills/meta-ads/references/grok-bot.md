# Running this skill inside Grok Bot

Grok Bot reads the same `SKILL.md` format as Claude, and each bot has its own always-on cloud computer (terminal, files, browser), routines, connectors and messaging (Telegram, WhatsApp, email). That makes it a natural home for the operator loop: the analysis runs on the bot's computer, the daily check is a routine, and the report arrives where the user already reads messages.

## Install

Ask the bot, in a conversation:

```text
Install the meta-ads skill from https://github.com/hoodini/ai-agents-skills:
clone the repo to ~/ai-agents-skills (or git pull if it exists) and run
sh ~/ai-agents-skills/scripts/install-grok-bot.sh --skill meta-ads
```

The script copies `skills/meta-ads/` to `~/agent-data/workflows/meta-ads/` (the library every bot on the account reads) and installs `requests`. Rerun the same two steps to update. Confirm under **Settings > Plugins > Yours**, or in the `/` menu of a conversation.

Run every script from the installed folder: `python3 ~/agent-data/workflows/meta-ads/scripts/<script>.py`.

## Credentials

- Follow `references/setup.md`. A System User token (never expires) suits a bot best; a 60-day user token works but needs a renewal reminder.
- Keep the token out of chat history and out of skill files. If the bot's vault exposes secrets to the shell, use it; otherwise write `~/.config/meta-ads/.env` with `chmod 600` and `set -a; . ~/.config/meta-ads/.env; set +a` before running scripts.
- Run `auth_check.py` right after setup. The bot's computer has open internet, so the sandbox proxy problem in troubleshooting.md doesn't apply.

## Sales-platform data

If the bot has a connector or MCP for the checkout/course platform (e.g. the Schooler MCP, `https://my.schooler.biz/mcp`), add it in the bot's connectors and authorize it once; then follow `references/sales-platform-data.md`. If not, export students from the platform and drop the files on the bot's computer for `segment_students.py`.

## A dedicated analyst bot

Create a bot just for ads (for example "Ads Analyst") with this skill, the Meta credentials and the platform connector. Give it a clear routing name so the main bot hands it anything about campaigns, pixels or sales funnels, and the user can tag it with `@`. Its personal rules:
- Read freely; any change to Meta, the website or the course platform needs the user's explicit "approve" for that specific action (`references/write-actions.md`).
- Report in the user's language, money first, at most two recommendations.

## The daily routine

Use the prompt template in `references/monitoring.md` as the routine prompt, and add this line at the top, because routine approvals expire unanswered (about ten minutes) and the step never runs:

```
This run is unattended. Never request an approval during it. If a step would change anything,
stop there and list it under "waiting for approval" with what and why. Continue with read-only steps.
```

- Schedule: every morning in the user's time zone (confirm the zone back before saving).
- Deliver the report where the user reads (Telegram / WhatsApp / email) and save it to a dated file on the bot's computer, so a silent run and a failed run can be told apart.
- Test the routine once by hand and read the whole output before trusting the schedule.

## Raise a flag, don't wait for the morning

Grok Bot can message the user on its own initiative. Worth an immediate message (from a frequent lightweight check, read-only):
- an ad or ad set rejected, or delivery stopped;
- `check_pixel.py` reports MISSING / SUSPECT on the landing or checkout page;
- spend today passed about one break-even CPA with no checkout;
- a new "signed up but didn't pay" person on the course platform (name only, so the user can reach them the same day).

Everything else waits for the daily report. Keep alerts rare; a bot that pings for noise gets muted.

## What the user approves in a live conversation

Creating campaigns or audiences, activating or pausing, budget changes, creative swaps, sending any mailing, and any write on the course platform. The bot prepares the exact action (dry-run output, preview links, the list and the text), the user replies approve, then it runs.
