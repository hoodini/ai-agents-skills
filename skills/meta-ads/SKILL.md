---
name: meta-ads
description: Run Meta ads end to end like a PPC specialist: install and verify the pixel on a funnel, launch Sales campaigns, read the data, find where the funnel leaks, fix campaigns live, build stage-by-stage remarketing, and monitor daily. Pull, analyze, manage, and CREATE Meta ads (Facebook, Instagram, Messenger, Threads, Click-to-WhatsApp) via the Marketing API. Use when the user mentions Meta/FB/IG ads, Ads Manager, ROAS, CPA, CPM, CTR, ad spend, campaign or ad set performance, creative fatigue, frequency, CTWA, audience/placement breakdowns, A/B ad tests, or wants to pause an ad, change a budget, duplicate a winner, or launch a new campaign from scratch, install or debug a Meta pixel (פיקסל), set up remarketing (רימרקטינג, קהלים מותאמים, מי שביקר ולא קנה), or wants ongoing monitoring of a live campaign. Also covers reconciling ads with real sales from the checkout/course platform (Schooler MCP, סקולר, רב מסר) and turning past buyers, sign-ups that didn't pay and non-starters into cross-sell and recovery campaigns. Runs in Claude and in Grok Bot (גרוק בוט): install into a bot, run the daily check as a routine, alert on Telegram/WhatsApp. Trigger on Hebrew terms like פרסום בפייסבוק/באינסטגרם, פרסומות מטא, ביצועי קמפיין, פרסומות, צור קמפיין, השק קמפיין, A/B טסט. Trigger on questions like how are my ads doing, which creative is winning, is my ad fatigued, what's my CPA, drop a 30-day report, launch an A/B test for my course, build a campaign with these 3 angles. Trigger even if auth isn't set up - the skill walks through one-time setup. Do NOT use for organic Instagram analytics, Reels view counts on non-promoted posts, or organic Threads engagement; those need the Instagram Graph API.
---

# Meta Ads (Marketing API)

Pull ad performance data from Meta (Facebook, Instagram, Messenger, Click-to-WhatsApp, Threads), run analyses, and, with explicit confirmation, write changes back (pause, budget change, duplicate, full campaign creation with images, copy or existing Instagram posts).

Beyond reporting, this skill is meant to act as the user's **PPC operator**: get the pixel right on every page of the funnel, launch a Sales campaign that can actually learn, read the numbers stage by stage, change things rarely and for a reason, and keep watching. The operator loop below is the main workflow for anyone who sells something online.

## When to consult this skill

Any question about Meta ad performance, creative health, audience/placement mix, or campaign management. If the user asks "how are my ads doing" without specifying a platform, ask whether they mean Meta or Google before defaulting.

## Three things to internalize before touching any script

**1. Where the scripts run matters.** The scripts call `graph.facebook.com` over the open internet. Some execution environments (including Claude's Linux sandbox in certain configurations) block this endpoint via proxy. If you hit a `ProxyError` / `Tunnel connection failed: 403` on the first call, run the scripts from the **user's host machine** - macOS, Windows, or Linux - using that machine's Python. Per-OS commands:
- **macOS:** `python3 scripts/auth_check.py`, deps via `python3 -m pip install --user requests`
- **Windows:** `python scripts/auth_check.py` (or `py scripts/auth_check.py` if `python` isn't on PATH), deps via `python -m pip install --user requests`
- **Linux:** `python3 scripts/auth_check.py`, deps via `python3 -m pip install --user requests` (add `--break-system-packages` on Debian/Ubuntu 22+)

The scripts themselves are pure Python with one dependency (`requests`) and no shell/OS assumptions, so they run identically everywhere once dependencies are installed.

**2. WhatsApp is not a separate ad surface.** Click-to-WhatsApp ads run on Facebook and Instagram placements. They show up in the Marketing API as regular ads with `destination_type=WHATSAPP` and conversion events under `actions` (look for `onsite_conversion.messaging_conversation_started_7d` and similar). Don't promise the user a "WhatsApp ads dashboard" - there isn't one.

**3. Read is safe, write is not.** Insights endpoints (GET) are idempotent and harmless. Pause / budget / duplicate (POST) actions touch real money. The write rules in `references/write-actions.md` are non-negotiable - read that file before any write call.

## The operator loop (the main workflow for selling)

When the user wants sales, not just a report, run these phases in order. Each has its reference file; read it when you reach that phase. **The system that ties them together is `references/full-funnel-system.md`**: signal inventory, the intent ladder (who is at which stage and what stops them), audiences per rung with exclusions, campaign architecture (prospecting / re-engage / close), creative per rung, the testing order and the keep/kill/scale/shift rules. Read it before designing audiences or campaigns, and again whenever you analyse results.

1. **Map the funnel and settle the account** (`references/pixel-setup.md` steps 0-1). Where does each step happen (landing page, checkout platform, payment)? Which ad account pays, does it have a payment method, is it in a Business? Decide ONE ad account and ONE pixel before anything else; switching later costs a re-install everywhere and resets learning.
2. **Install the pixel and verify it in three layers** (`references/pixel-setup.md`): installed on every page (`check_pixel.py`), calls made, events received in Test events, then a real ~99%-coupon purchase. Find out what events the checkout platform already sends by reading its JS, and give every funnel step a unique standard event.
3. **Write down the economics** (`references/ppc-operator-playbook.md`): price, break-even CPA, target CPA. Every later recommendation is phrased against them.
4. **Launch** with `create_campaign.py` (`references/campaign-creation.md`): Sales objective, optimization event chosen by volume, Facebook + Instagram placements (`"placements": "fb_ig_all"`), CBO with 3-5 creatives, UTM tags, everything PAUSED, dry-run validated by Meta, preview links sent to the user, activation as a separate confirmed write.
5. **Day 0 structural check**: after the first ~50 in spend run `funnel_report.py --breakdowns placement,age`. Fix structural leaks now (e.g. Audience Network eating the budget) while a learning reset is cheap.
6. **Days 1-3: hands off.** Daily read-only check; fix only what's broken.
7. **Day 4+: decide by the table** in the playbook: scale in 20-30% steps, swap the weakest creative, or fix the leaking funnel stage (`rates_pct` in `funnel_report.py`).
8. **Cover every rung of the intent ladder** (`references/full-funnel-system.md`, `references/funnel-remarketing.md`): instrument the gaps (landing-page engagement events, the checkout platform's registration URL, customer lists), build mutually exclusive audiences from video viewers to checkout abandoners, give each rung its own message and creative (write the text, brief the user on what to film), and run re-engage and close campaigns with their own budgets. Then test one variable at a time and move money by marginal CPA.
9. **Reconcile with the sales platform and sell to warm segments** (`references/sales-platform-data.md`): pull real enrollments (e.g. Schooler MCP), compare with Meta's attributed purchases, and build segments: signed up but didn't pay, bought A but not B, paid but never started. These are the cheapest sales in the business.
10. **Monitor proactively** (`references/monitoring.md`): a scheduled daily read-only report against break-even, with at most two recommended actions.

If the user needs money urgently, say plainly that paid prospecting is the slowest revenue and put the warm levers first (past buyers, hand-raisers within the platform's messaging rules, a higher-ticket offer); see "Money-now levers" in the playbook.

## Where it runs: Claude and Grok Bot

The skill is plain `SKILL.md` + Python scripts, so it runs anywhere an agent has a shell and internet: Claude Code, the Claude apps, and **Grok Bot**, where a dedicated analyst bot can own the whole loop (daily check as a routine, alerts on Telegram/WhatsApp, approvals in a live conversation). Install into Grok Bot with `sh scripts/install-grok-bot.sh --skill meta-ads` from a clone of the repo (it copies the skill to `~/agent-data/workflows/meta-ads/`). Details, credentials, routine rules and alert thresholds: `references/grok-bot.md`.

## The 37-month data wall

Meta's insights API only serves data from the last **37 months**. Any campaign older than that returns error `3018` and is effectively invisible. If the user asks "what was my best campaign ever" and their activity predates the window, the answer is "the API can't tell you - check Ads Manager's archived reports UI." Surface this before starting a query that's going to fail.

## Before anything else: check setup + discover accounts

The first three calls are always the same:

1. `python scripts/auth_check.py` - is the token alive, what identity does it resolve to, how many ad accounts does it see?
2. `python scripts/list_accounts.py --with-recent-spend` - which accounts are actually running ads right now? (Sorted by last-30-day spend, then lifetime spend.) This tells you which account to pin as `META_AD_ACCOUNT_ID`.
3. `python scripts/list_campaigns.py` - once you have the right account, what campaigns are on it?

If any of these fail, stop and walk the user through `references/setup.md`. Don't try to be clever and guess credentials.

### How to guide a user through setup (first-timers)

`references/setup.md` is written as a click-by-click walkthrough. When a user has no credentials yet:

1. **One step at a time.** Don't dump the whole document. Ask them which OS they're on, then give them the prerequisites block for that OS. Wait for them to report "done" before moving on.
2. **Confirm the path choice.** Walk through the Step 0 decision questions with them in chat. Don't assume - especially "do you boost from Instagram?" is easy to misjudge.
3. **Read back what they paste.** When they share a token, App ID, or ad account ID, echo it back (redact tokens to the first 8 chars) and confirm you have it right before you move on. This catches the #1 setup bug: pasting the System User's ID where the Ad Account ID should go.
4. **Verify before moving on.** After they fill in `.env`, run `auth_check.py` immediately. Don't let them run analysis commands until the verification returns `ok: true` - every "the report is empty" issue traces back to a half-broken `.env`.
5. **Match their OS in every command.** If they said "I'm on Windows," don't tell them to run `python3` - tell them `python` or `py`. If they said "Mac", use `python3`. The setup.md has per-OS blocks; copy the matching one into chat.

Required env vars (user provides these once during setup):
- `META_ACCESS_TOKEN` - either a long-lived user token (Path B, 60 days) or System User token (Path A, never expires). See the decision tree below.
- `META_AD_ACCOUNT_ID` - default ad account, format `act_1234567890` (scripts accept `--account-id` to override per call).
- `META_API_VERSION` - defaults to `v25.0` (current as of early 2026; v26.0 expected ~Sep 2026).

The user puts these in a `.env` file at the working directory or exports them in the shell. Scripts auto-load `.env` if present. See `assets/env.template`.

## Path A vs Path B: which token type?

This is the single most common failure mode. Get it right up front.

**Use Path A (System User token) when:**
- Ads run inside a Meta Business Manager you control.
- The ad accounts you want to analyze are owned by that BM.
- You want a token that never expires.

**Use Path B (long-lived user token) when:**
- You boost posts from the Instagram app (these often create a personal ad account outside any BM - invisible to System User tokens no matter what permissions you grant).
- Your ad account is attached to your personal Facebook profile, not a BM.
- You want to see every ad account your personal FB login can access (typically the broadest view).

**Can't tell which?** Start with Path B. It sees a strict superset of what Path A sees. Once you've identified the important accounts, you can optionally move them into a BM and switch to Path A for permanence.

Full setup steps for both paths: `references/setup.md`.

## Workflow: read operations

For any read request, follow this loop:

1. **Pick the right script.** Don't reinvent. The bundled scripts cover the common cases:
   - `auth_check.py` - verify token, list visible accounts briefly
   - `list_accounts.py` - discover all ad accounts, decode status, show lifetime + optional recent spend
   - `list_campaigns.py` - campaigns under an account, with status filters
   - `fetch_insights.py` - the workhorse. Date ranges, breakdowns (publisher_platform, age, gender, country, placement, device_platform), level (account/campaign/adset/ad), custom field lists. Read its `--help` before calling.
   - `creative_fatigue.py` - frequency + CTR decay analysis at the ad level
   - `anomaly_detect.py` - compares a date range against the prior equivalent range, flags significant changes
   - `exchange_token.py` - Path B only: swap short-lived user token for 60-day long-lived token
   - `funnel_report.py` - one campaign's status, review issues and pixel funnel (clicks → landing → view content → add to cart → checkout → purchase) with stage-to-stage rates, lifetime/yesterday/today, per ad, plus optional breakdowns (placement, age, gender, hour, device). The daily-check workhorse.
   - `segment_students.py` - turns course-platform student exports (e.g. Schooler MCP `list_course_students` results saved to files) into counts and CSV segments: signed up but didn't pay, paid but not started, bought A without B
   - `check_pixel.py` - which pixel IDs actually load on each funnel URL; flags missing pixels, leftover pixels and the ad-account-ID-pasted-as-pixel mistake

   Write scripts (pause/budget/duplicate/create - read `write-actions.md` first):
   - `pause_ad.py` - pause/resume a single campaign, ad set, or ad
   - `update_budget.py` - modify daily or lifetime budget with 2×-per-call safety cap
   - `duplicate_ad.py` - clone an ad, ad set, or entire campaign into a new copy
   - `create_campaign.py` - build a whole campaign (campaign + ad sets + creatives + ads) from a spec JSON: image ads or existing Instagram posts, CBO, pixel-event optimization, placement presets, UTM tags. Meta-validated dry-run, payment-method guard, partial state on failure, `--into-adset` resume. See `references/campaign-creation.md`.
   - `rollback_creation.py` - pause or delete every object from a `create_campaign.py` run using its state file

2. **Run it, capture JSON output.** Every script outputs structured JSON to stdout. Don't try to parse human-readable text - there isn't any. Pipe to a file if the user wants to keep the raw data: `python scripts/fetch_insights.py ... > insights.json`.

3. **Analyze with the playbooks.** Once you have the data, consult `references/analysis-playbooks.md` for the relevant pattern (fatigue, funnel, audience mix, anomalies). The playbook tells you what thresholds matter and what to recommend.

4. **Present in the user's preferred language.** If the user writes in Hebrew, respond in Hebrew. Keep metric names in English (`CTR`, `CPA`, `ROAS`) so they cross-reference cleanly with Ads Manager. If asked for a doc/dashboard, follow whatever design system skill they've set up.

## Workflow: write operations (pause, budget, duplicate)

These are the dangerous ones. Follow this protocol every time, no shortcuts:

1. **Surface the action and the impact in plain language before calling.** Example: "Pause ad `Campaign_v3` (ID 120214...). This ad spent ₪47 in the last 7 days with 0.8% CTR. Confirm?"
2. **Wait for explicit `yes` / `confirm` / the user's language equivalent in chat.** A previous "go ahead" in the conversation does not carry over. Each write needs its own confirmation.
3. **One action at a time by default.** If the user wants to bulk-pause 12 ads, present a numbered list and confirm the whole batch in one explicit message ("pause all 12") - but log each call separately.
4. **Always do a dry-run first when the script supports it** (`--dry-run` flag prints what would change without calling the API).
5. **Never auto-shift budgets above +50% in one call.** If the user wants a 3x increase, do it in steps with confirmation each time. Meta's learning phase resets on big budget changes anyway.

Full rules and edge cases in `references/write-actions.md`. Read it before calling any of: `pause_ad.py`, `update_budget.py`, `duplicate_ad.py`, `create_campaign.py`.

## Workflow: creating a campaign from scratch

Use `create_campaign.py` to build a full campaign tree (campaign → ad sets → creatives → ads) in one shot from a spec JSON. Good for A/B flights where you want the exact same structure with disciplined naming and auditable creation history.

Before you touch the script:

1. **Check if the user has a pixel, and that it really works** (`references/pixel-setup.md`). No pixel → force `objective: OUTCOME_TRAFFIC` and `optimization_goal: LINK_CLICKS`. Don't build a conversions campaign against an account that can't measure conversions; you'd be paying Meta to optimize toward an event it never sees. Surface this to the user and let them decide whether to wait for pixel install or launch blind on traffic.
2. **Check the account balance and payment method.** Status code 3 (`UNSETTLED`) means objects can be created but nothing will deliver until balance clears; 9 (`IN_GRACE_PERIOD`) means a failed payment is open; 100 (`PENDING_CLOSURE`) means the account is going away. With no payment method at all, Meta rejects the ads themselves; `create_campaign.py --confirm` refuses up front.
3. **Discover the right page + Instagram identity.** Users often own multiple pages. Query `/me/accounts` and `/act_.../promote_pages` and match against which page ran their historical winning ads (fetch a handful of recent ads, pull `creative.effective_object_story_id` to see the page ID in the prefix).
4. **Default everything to PAUSED.** The campaign, ad sets, and ads should all be `PAUSED` at creation. The user flips ACTIVE themselves in Ads Manager once they've eyeballed the creative. This is the last safety net.
5. **Dry-run first, always.** `create_campaign.py --spec foo.json --dry-run` prints the full plan with resolved interest IDs, currency-corrected budgets, and targeting summary. Walk the dry-run back to the user in plain language before asking for `--confirm`.

Per `write-actions.md`, a fresh explicit confirmation is required for `--confirm` even if the user approved the plan earlier in the same session. That confirmation must name the action (e.g. "confirm create", "בצע יצירה") - not a generic "ok".

Full spec format, field reference, currency handling, interest resolution, state file and rollback details: `references/campaign-creation.md`.

### When NOT to use `create_campaign.py`

- **Single ad addition to existing ad set** - just call the ads endpoint directly or use the UI. Overkill to spec-and-run for one ad.
- **Duplicating a winner** - `duplicate_ad.py` is faster and preserves learning signals.
- **Dynamic creative, catalog ads, collection ads** - not supported. The script handles single-image link ads and existing Instagram posts. Extend it or build a sibling script if needed.

## Gotchas the scripts already handle for you

- **Currency minor units.** `amount_spent`, `balance`, `spend_cap`, `daily_budget`, `lifetime_budget` are returned by Meta as strings of minor units (agorot/cents/pence). `list_accounts.py` and `list_campaigns.py` convert these to major units in a `_major` or plain decimal field. Zero-decimal currencies (JPY, KRW, VND, ISK, TWD, etc.) are not divided.
- **Account status codes.** Scripts decode 1→ACTIVE, 2→DISABLED, 3→UNSETTLED, 7→PENDING_RISK_REVIEW, etc.
- **Pagination.** All scripts auto-paginate via `meta_client.paginate()`.
- **Rate limits.** `meta_client._request()` backs off on subcodes 1487742 / 2446079 / 1487390 and retries.
- **Async insights.** `fetch_insights.py` auto-falls-back to async jobs when sync queries would time out (or you can force with `--async`).
- **DELETED campaigns.** Meta's campaigns endpoint returns error 1815001 when you request DELETED. The script's `--status` choices deliberately exclude DELETED. To see deleted campaigns, use Ads Manager UI.

## What the bundled scripts don't handle

- Initial auth / token generation (manual, see `references/setup.md`).
- Pixel installation itself (it's site code: `references/pixel-setup.md` walks through it, `check_pixel.py` verifies it) and Conversions API ingestion (separate API).
- Dynamic creative / catalog / collection ad formats (image ads and existing Instagram posts only).
- Custom Audience creation has no bundled script yet: `references/funnel-remarketing.md` has the exact API rule shape for website audiences, and engagement audiences are simpler in the Ads Manager UI.
- Editing an already-live creative in place (you create new creatives via `create_campaign.py`; editing an existing one is a different API shape).

If the user needs something the scripts don't cover, extend the skill in a writeable copy and re-package - see `references/campaign-creation.md` for the pattern `create_campaign.py` establishes for write scripts. Don't fork separate one-off scripts in the user's working directory; consolidate into the skill so the next run benefits.

## Reference files

Read these on demand, not all upfront.

- `references/setup.md` - One-time setup: decision tree Path A vs Path B, how to create the app, get tokens, find account IDs. Read this when the user has no credentials, or when `auth_check.py` fails.
- `references/insights-fields.md` - Field glossary, breakdown options, common metric definitions, gotchas (attribution windows, action_attribution, deduplication). Read this when constructing a custom insights query.
- `references/analysis-playbooks.md` - Patterns for creative fatigue, audience analysis, funnel diagnosis, anomaly response. Read this when the user asks for analysis, not just data.
- `references/write-actions.md` - Mandatory before any write call. Confirmation flow, safety thresholds, rollback patterns - including the campaign-creation section before using `create_campaign.py`.
- `references/campaign-creation.md` - Spec format, field reference, currency handling, interest resolution, state file and rollback details for `create_campaign.py`. Read this when the user asks to launch a campaign, A/B test, or new ad flight from scratch.
- `references/full-funnel-system.md` - The doctrine: every signal Meta and the stack can capture, the intent ladder (L0 cold to L8 buyer, with video-depth and engagement rungs), audience recipes and exclusions, lookalikes, campaign architecture and budget split, creative per rung and hooks, the testing order and minimum data, keep/kill/iterate/scale/shift rules, weekly rhythm. Read before designing any funnel.
- `references/pixel-setup.md` - From zero to a verified funnel: account/pixel ownership decisions, Pixel vs CAPI, event naming per funnel step, reading a checkout platform's real events, the three-layer verification and the real test purchase. Read before any conversion campaign.
- `references/ppc-operator-playbook.md` - The live operating loop: economics, launch checklist, day-by-day rules, decision table, stage-leak diagnosis, known traps (Audience Network, age stretch, reporting lag, IG post copies), money-now levers, how to report.
- `references/funnel-remarketing.md` - Stage-by-stage remarketing: audiences, exclusions, sizing limits, structure, API rule shape, creative per stage.
- `references/sales-platform-data.md` - Ground truth from the checkout/course platform: connecting the Schooler MCP, what each tool returns, reconciling real sales with Meta, the six questions it answers, turning segments into mailing campaigns (signed-up-minus-paid, cross-sell, activation, reminder sequences), privacy.
- `references/grok-bot.md` - Running the skill inside Grok Bot: install/update, credentials, a dedicated analyst bot, the unattended daily routine, which events deserve an immediate alert, what needs approval in a live conversation.
- `references/monitoring.md` - Setting up a scheduled daily read-only check, with a prompt template.
- `references/troubleshooting.md` - Common failure modes (sandbox proxy, IG boost invisible to SU tokens, missing requests module, encoding issues, 37-month cap, etc.). Read this when any script returns `ok: false` or something unexpected.

## Scaling beyond personal use

This skill is built for one user, one set of credentials, a handful of ad accounts. Multi-tenant / client-agency use (one operator managing dozens of client BMs) is a different build:
- Per-client credential storage (not everyone's tokens in one .env).
- Each client issues their own System User token from their own BM.
- Audit log of every write action, who triggered it, against which account.

Don't try to retrofit the personal skill for multi-tenant use. Tell the user it's a different build.
