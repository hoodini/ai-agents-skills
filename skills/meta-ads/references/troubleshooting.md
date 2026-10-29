# Troubleshooting

Real failure modes observed when running this skill. Read the section that matches your symptom.

If none of these match, re-run `python scripts/auth_check.py` and share the full JSON output with the user - it's usually the fastest path to the root cause.

---

## Auth / token problems

### `auth_check.py` returns `ok: true` but `ad_accounts_visible: 0`

The token is valid, but the identity it resolves to can't see any ad accounts. Two causes:

**Path A (System User token):** the System User hasn't been granted access to any ad accounts yet. Go to Business Settings → Users → System Users → click the user → Add Assets → Ad Accounts tab → tick each account → grant "Manage campaigns" or "Read performance" → Save. Re-run `auth_check.py`.

**Path B (user token):** the FB user who generated the token at Graph Explorer doesn't own or have been granted access to any ad accounts. Two sub-causes:
- You were logged into the wrong FB account in Graph Explorer when you generated the token. Log out, log into the right one, repeat B.1.
- The OAuth popup during B.1 didn't include `ads_read` / `ads_management` / `business_management` scopes. Regenerate with those permissions checked.

### `auth_check.py` returns `ok: false` with code 190

The token is expired or revoked. For Path B: tokens expire after ~60 days - repeat B.1 then B.2 in `setup.md` to get a fresh one. For Path A: System User tokens don't expire, so if you see 190 on one, either it was explicitly revoked in Business Settings or the System User itself was deleted. Regenerate.

### `auth_check.py` returns `ok: false` with code 102 or 4

Session expired / app restriction. Almost always means the App Secret was regenerated or the app was put into "Live" mode without App Review. For personal use, the app should stay in "Development mode" - check App Dashboard → App Mode toggle.

### `exchange_token.py` fails with `(#100) Invalid OAuth access token`

The short-lived token you pasted is already expired (they last ~1-2 hours) or mistyped. Go back to Graph Explorer, click "Generate Access Token" again, paste the fresh one immediately.

### `exchange_token.py` fails with `(#1) Unknown error` or `(#101) Missing client_id parameter`

`META_APP_ID` and/or `META_APP_SECRET` are missing or wrong in `.env`. Re-copy both from your Meta developer app → Settings → Basic. The App Secret needs to be revealed via the "Show" button - make sure you copied the actual secret, not the placeholder dots.

### `(#200) Permissions error` when calling a write endpoint

The token has `ads_read` but not `ads_management`. User tokens inherit only the scopes granted at OAuth time - regenerate with `ads_management` checked. System User tokens need the "Manage campaigns" role on the specific ad account (not just "Read performance").

---

## Network / environment problems

### `requests.exceptions.ProxyError: Tunnel connection failed: 403 Forbidden`

Your execution environment can't reach `graph.facebook.com`. This happens with Claude's Linux sandbox in some configurations - the outbound proxy blocks Meta's Graph domain.

**Fix:** run the scripts from the user's host machine (their Mac/Windows/Linux) instead of the sandbox. On macOS use `/usr/bin/python3`. Install deps on the host first:

```bash
/usr/bin/python3 -m pip install --user requests
```

Then run each script with the host Python:

```bash
/usr/bin/python3 /path/to/skills/meta-ads/scripts/auth_check.py
```

Don't try curl / wget / a different HTTP library - the block is at the proxy layer, not in `requests`.

### `ModuleNotFoundError: No module named 'requests'`

Python doesn't have `requests` installed. Pick the command that matches your OS:

```bash
# macOS
python3 -m pip install --user requests

# Windows (PowerShell or cmd)
python -m pip install --user requests
# or if that fails:
py -m pip install --user requests

# Linux (normal case)
python3 -m pip install --user requests

# Linux with PEP 668 enforcement (Debian/Ubuntu 22+)
python3 -m pip install --user --break-system-packages requests
```

If you installed it but still see the error, you probably have multiple Python versions on your machine. Install against the same interpreter you're running the script with - find it with:
- macOS / Linux: `which python3` then `python3 -m pip show requests`
- Windows: `where python` then `python -m pip show requests`

### `SSLError` / certificate verification failed

Either the host clock is badly wrong (check `date` on macOS/Linux or `Get-Date` in PowerShell) or a corporate proxy is intercepting TLS. For corporate networks, set `REQUESTS_CA_BUNDLE` to point at your org's CA bundle, or run on a personal machine.

---

## Windows-specific issues

### `python` is not recognized as an internal or external command

Python isn't on your PATH. Two fixes:

1. **Re-run the Python installer** from <https://www.python.org/downloads/windows/> and on the first screen tick **"Add python.exe to PATH"**. Close and reopen your terminal after installing.
2. **Use `py` instead.** The Python launcher `py` is installed separately and usually works even when `python` doesn't:
   ```powershell
   py --version
   py scripts/auth_check.py
   py -m pip install --user requests
   ```

### Hebrew, Arabic, or other non-Latin characters show as `?` or garbled in cmd.exe

cmd.exe's default code page is Windows-1252, which can't display Unicode. Switch to UTF-8 for the current session:

```cmd
chcp 65001
```

Then re-run your script. To make UTF-8 the default permanently, set the system locale in **Region settings → Administrative → "Beta: Use Unicode UTF-8 for worldwide language support"** (requires a reboot).

PowerShell and Windows Terminal usually handle UTF-8 correctly without changes.

### Scripts run but `.env` values aren't being picked up

Windows line endings (CRLF) can break the `.env` parser on older tooling, though `meta_client.py`'s loader handles CRLF correctly. If you suspect it's the issue, open `.env` in VS Code and check the bottom-right - if it says "CRLF" click to change to "LF" and save.

### `Copy-Item : Cannot find path` in PowerShell when copying `.env`

You're not in the skill's directory, or the template name is different. Verify:

```powershell
Get-Location           # should end in \skills\meta-ads
Get-ChildItem assets   # should list env.template
```

### PowerShell execution policy prevents running scripts

You shouldn't hit this because the skill only uses `.py` files (not PowerShell scripts), but if you add a `.ps1` wrapper and get "running scripts is disabled on this system", run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### Long path errors when running scripts from deep directories

Windows has a legacy 260-character path limit. If your skill folder is nested very deep (e.g., `C:\Users\you\OneDrive\Documents\Projects\whatever\ai-agents-skills\skills\meta-ads\…`) and you see "file name too long" errors, either move the folder closer to the drive root or enable long paths in Windows:

```powershell
# Run as admin
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1
```

Then reboot.

---

## Ad account discovery problems

### `list_accounts.py` shows an account with `account_status: 3` / `UNSETTLED`

The account has an unpaid balance. Meta still returns it and insights still work, but new campaigns can't be created until payment is resolved. Head to Ads Manager → Billing to clear it. This is not a bug in the script.

### `list_accounts.py` shows `account_status: 7` / `PENDING_RISK_REVIEW`

Meta has flagged the account for manual review. Read-only insights usually still work; writes don't. Appeal via Ads Manager → Account Quality. No API workaround.

### I boosted a post from the Instagram app but `list_accounts.py` doesn't show its ad account

Two possibilities:

1. **You're on a Path A (System User) token.** IG-app boosts typically create a personal ad account attached to your FB profile, not inside any Business Manager - and System User tokens can *only* see BM-owned accounts. No amount of permissions fixes this because the account is structurally outside the BM. Switch to Path B (user token) and you'll see it.
2. **The boost ran under a different FB account** than the one you used at Graph Explorer. Check which FB login owns the Instagram account that did the boost.

### "I added the ad account to the Business Manager, why doesn't the SU token see it?"

Two missing steps, in order:
1. BM owns the ad account → Business Settings → Accounts → Ad Accounts → it should be listed under "Ad Accounts I Own", not "Ad Accounts I Have Access To". If it's the latter, you don't have write access - contact the account owner to transfer it.
2. System User has been granted the ad account as an asset → Business Settings → Users → System Users → click the user → Add Assets → tick the account → save.

After both, regenerate the System User token (the old one's scope is cached at generation time).

### Wrong ID pasted into `META_AD_ACCOUNT_ID`

Common mixup: in Business Settings the System User page shows **the System User's ID** prominently (a 15-digit number). People sometimes paste that into `META_AD_ACCOUNT_ID`. It's not an ad account ID.

Ad Account IDs come from Ads Manager's URL (`act=<digits>`) or from `list_accounts.py` output. The format the API expects is `act_<digits>`.

---

## Insights / data problems

### `(#3018) The start date of the time range cannot be beyond 37 months from the current date`

Meta's insights API only serves data from the last 37 months. Any campaign older than that is invisible to the API. If the user asks about a 2019 campaign in 2026, the answer is literally "the API can't tell you."

Workaround: open Ads Manager → Reports → Archived Reports, run the report in the UI, export CSV. Do not try to construct clever date ranges to sneak past the cap - Meta checks each range's start date against the 37-month wall.

### `(#1815001) Cannot Request for Deleted Objects`

You tried to request `effective_status` values that include `DELETED` on the campaigns endpoint. Meta's campaigns edge doesn't support filtering on DELETED - it returns 1815001 rather than empty. `list_campaigns.py` already excludes DELETED from `--status` choices for this reason.

If you really need to see deleted campaigns, use Ads Manager's UI with the "Deleted" filter. There's no API path.

### `fetch_insights.py` times out on a long date range

Switch to async mode: add `--async` or let the script auto-fall-back. Async insights jobs can run up to 30 minutes server-side; sync calls time out at ~60s.

If `--async` also fails with "Job Failed", your query is likely too broad for Meta's async quota too. Split the date range (e.g., one month at a time) or reduce breakdowns.

### Insights return `spend: "0"` but Ads Manager shows spend

Three common causes:
1. **Attribution window mismatch.** Ads Manager defaults to 7-day-click + 1-day-view. API defaults to a narrower window depending on version. Pass `action_attribution_windows=['7d_click','1d_view']` explicitly in the insights query.
2. **Level mismatch.** You queried `level=account` but the campaign is on a sub-account. Check the `account_id` on the campaign.
3. **Currency confusion.** `spend` is returned in the account's currency (as a decimal string in major units for insights - *unlike* `amount_spent` on the account object, which is minor units). Don't confuse the two.

### Click numbers seem too high

`clicks` includes *every* click anywhere on the ad - reactions, "See more" expansions, profile clicks. For outbound link clicks only, use `inline_link_clicks`. For the metric Ads Manager calls "Link clicks", it's `actions` where `action_type = link_click`.

---

## Display / encoding problems

### Hebrew / Arabic / Chinese campaign names show as `\u05d2\u05dd...` in output

JSON escaping. Scripts output `ensure_ascii=False` so this shouldn't happen when you run them directly. If you see escaped Unicode, you're probably viewing the output through a pipe that doesn't handle UTF-8 - on Windows cmd.exe, run `chcp 65001` first; on macOS/Linux it usually Just Works unless `LANG` is set to `C`.

### `amount_spent` is a weirdly large number like `1691697`

That's minor units (agorot / cents / pence). Divide by 100 for most currencies. For zero-decimal currencies (JPY, KRW, VND, CLP, ISK, UGX, XAF, XOF, TWD) don't divide. `list_accounts.py` already does this conversion and exposes it as `amount_spent_major`. The raw `amount_spent` field is preserved for anyone who needs it.

---

## Write action problems

### `pause_ad.py` or `update_budget.py` returns `ok: true` but the change didn't happen in Ads Manager

Ads Manager's UI caches state for 30-60 seconds. Refresh the browser. If it's still wrong after a minute, pull the ad back via the API - the truth is what the API returns, not the cached UI.

### Budget change rejected with `(#100) Invalid parameter`

Either the new budget is below Meta's minimum for the currency, or above the account's `spend_cap`, or you passed it in the wrong units. Budgets on write are passed in minor units (same as `amount_spent`) - the scripts convert for you, but if you're calling the API directly, pass `daily_budget=500` for ₪5.00, not `daily_budget=5`.

### "I wanted to duplicate an ad, why did the copy show up paused?"

Meta always creates copies in PAUSED status by default - this is intentional so you don't immediately spend money on an unverified copy. Unpause via `pause_ad.py --object-id <new_ad_id> --status ACTIVE` after reviewing the copy in Ads Manager.

### Campaign and ad sets were created, every ad failed with `No Payment Method` (code 100, subcode 1359188)

Meta lets an account with no payment method create campaigns and ad sets, then refuses the ads. `create_campaign.py --confirm` now checks `funding_source_details` first and refuses before writing anything. If you hit it on an old run: add a payment method in Billing, then resume with `--into-adset <adset_id>` so you don't create a second campaign.

### Every creative fails with `Creative should not include standard enhancements`

Meta (v25) deprecated the bundled `degrees_of_freedom_spec.creative_features_spec.standard_enhancements` opt-out. `create_campaign.py` no longer sends it. Review Advantage+ creative toggles per ad in Ads Manager before activating instead.

### Ad account status 9 / 100

- `9` = IN_GRACE_PERIOD: a payment failed and a balance is open. Ads still run for now; the account is disabled if it isn't paid. Tell the user to pay in Billing before launching anything.
- `100` = PENDING_CLOSURE: Meta is closing the account (often after a payment-method change on a personal account, Meta asks for a new one). Anything owned by it, **including a pixel created inside it**, should be treated as going away. Move to the new account and a new or Business-owned pixel.

### The pixel exists but isn't listed when boosting from the Instagram app

The boost flow lists Business-owned pixels only. A pixel created inside a personal ad account (no Business) never appears there, even on the right account. Options: put the account and pixel in a Business Portfolio and connect them, or run the campaign from Ads Manager (recommended for sales anyway). Don't let the user pick "any pixel" from that list: an inactive or unrelated pixel optimizes toward nothing.

### The ad uses an existing Instagram post but shows zero likes

Check `creative.effective_instagram_media_id`. If it differs from `source_instagram_media_id` and the media's `media_product_type` is `AD`, Meta made an ad-only copy because the ad account isn't authorised for that Instagram account through a Business Portfolio. The ad runs, but without the post's social proof, and comment automations on the original post won't see comments on the ad. Fix by connecting the Instagram account and the ad account in the same Business, then recreating the creative.

### Ads Manager shows errors but the API says it's fine

Before debugging the UI with the user, ask the API: `POST /<campaign|adset|ad id>` with `status=ACTIVE` and `execution_options=["validate_only"]` returns `success: true` or the real error, without changing anything. If it validates, activating through the API (with the user's explicit confirmation) avoids the UI entirely.

### The site sends no events even though the pixel code is there

Run `check_pixel.py`. Common causes: the ad account ID pasted as the pixel ID, an old pixel left on one page of the funnel, a CSP header blocking `connect.facebook.net`, or the checkout platform's tracking box saved with a different ID than the site. Lifetime totals also lag by hours: check today's hourly breakdown before concluding events stopped.

---

## When in doubt

1. Run `auth_check.py` - does the token even work?
2. Run `list_accounts.py --with-recent-spend` - do you see the account you expect?
3. Run `list_campaigns.py --account-id act_xxx` - does the campaign list match Ads Manager?
4. If 1-3 all look right but insights are wrong, run the same query in Ads Manager UI and compare - API vs UI discrepancies almost always come down to attribution windows or date ranges.

If you're still stuck, share the full JSON output of whichever script is misbehaving - the errors from Meta are reasonably informative once you can see them.
