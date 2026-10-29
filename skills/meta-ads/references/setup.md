# One-time Meta API setup - step by step

This is the only manual part of the skill. Meta's developer console involves real web-UI clicks and decisions only you can make, so we'll go slowly. Expect **15-25 minutes** end to end, mostly waiting for Meta's UI to load.

Works on **macOS, Windows, and Linux**. Per-OS command blocks are shown side by side. You only need to run the commands for the OS you're on.

If anything on screen looks different from what's described below, don't panic - Meta redesigns this console regularly. Look for the same *text labels* even if colors or positions have shifted. If you get truly stuck, jump to `references/troubleshooting.md`.

---

## Before you start: prerequisites

### 1. Python 3 installed on your machine

You need Python 3.8 or newer. Check which version you have:

**macOS (Terminal):**
```bash
/usr/bin/python3 --version
```
If you see `Python 3.x.x` you're good. If you see "command not found", install Python:
```bash
# Easiest: install Homebrew-managed Python
brew install python
# Or download the installer from https://www.python.org/downloads/macos/
```

**Windows (PowerShell or cmd):**
```powershell
python --version
```
If that fails, try `py --version`. If neither works, download the installer from **https://www.python.org/downloads/windows/** and **tick the "Add python.exe to PATH" checkbox** on the first screen of the installer - without it, `python` won't work from the terminal. After install, close and reopen your terminal.

**Linux (Bash):**
```bash
python3 --version
```
If missing: `sudo apt install python3 python3-pip` (Debian/Ubuntu) or your distro's equivalent.

### 2. The `requests` Python library

All scripts use one library: `requests`. Install it once:

**macOS:**
```bash
python3 -m pip install --user requests
```

**Windows (PowerShell or cmd):**
```powershell
python -m pip install --user requests
```
If `python` isn't recognized, try `py -m pip install --user requests`.

**Linux (if you hit "externally-managed-environment"):**
```bash
python3 -m pip install --user --break-system-packages requests
```

Verify it installed:
```bash
python3 -c "import requests; print(requests.__version__)"   # macOS / Linux
python -c "import requests; print(requests.__version__)"    # Windows
```
You should see a version number like `2.31.0` print out.

### 3. A terminal open in the skill's directory

You'll be running scripts from inside the `skills/meta-ads/` folder. Open a terminal there now so you don't have to re-navigate every time:

**macOS (Terminal):**
```bash
cd /path/to/skills/meta-ads
```

**Windows (PowerShell):**
```powershell
cd C:\path\to\skills\meta-ads
```

Every subsequent command in this guide assumes you're in that directory.

---

## Step 0: Which path should you use?

Meta has two token types. Pick one by answering three yes/no questions:

1. **Do you boost Instagram posts directly from the Instagram app?** If yes → **Path B.**
2. **Is the ad account you care about owned by a Meta Business Manager you created?** If no → **Path B.**
3. **Do you want a token that never expires, with all ads running from a single BM?** If yes → **Path A.**

**Still unsure? Pick Path B.** A Path B (user) token sees everything a Path A (System User) token sees *plus* personal ad accounts created by Instagram boosts. You can always switch to Path A later.

Both paths share **Steps 1 and 2** below. Do those first, then follow your chosen path.

---

## Step 1: Create a Meta developer app (both paths)

### 1.1 Open the developer console
Open your browser and go to **https://developers.facebook.com/apps**. Log in with the Facebook account that has access to your ads. If this is your first time there, Meta may ask you to register as a developer - agree to the terms.

### 1.2 Start a new app
Look for a green or blue **"Create App"** button, usually in the top-right corner of the page. Click it.

### 1.3 Choose the use case
You'll land on a page titled **"What do you want your app to do?"** with several tile options. Select **"Other"** (usually in the bottom row). Click **"Next"** at the bottom.

### 1.4 Choose the app type
On the **"Select an app type"** page, pick **"Business"**. Click **"Next"**.

### 1.5 Fill in app details
- **Display name:** something descriptive for you only - e.g., `my-meta-ads-skill`. Nobody else will see this.
- **App contact email:** your email.
- **Business Account (optional):** if you already have a Business Manager, select it from the dropdown. If not, skip - you can attach one later (or never, if you go Path B).

Click **"Create app"**. Meta may ask for your password to confirm.

### 1.6 Land on the app dashboard
After creation you'll be taken to your app's dashboard - a page showing the app name at the top and a list of available products in the main panel. Keep this tab open; you'll come back to it.

---

## Step 2: Add the Marketing API product (both paths)

### 2.1 Find the product list
Still on the app dashboard, scroll down to a section titled **"Add products to your app"** or look in the left-hand sidebar for **"Add product"**.

### 2.2 Add Marketing API
Find the **"Marketing API"** tile. Click **"Set up"** on it. The page reloads and Marketing API appears in the left sidebar.

### 2.3 Note your App ID and App Secret
In the left sidebar, click **"Settings" → "Basic"**. You'll see:
- **App ID** - a 15-digit number at the top.
- **App Secret** - hidden behind a **"Show"** button. Click it; you may need to re-enter your password.

Copy both to a password manager or a scratch file. You'll need the **App ID** in both paths, and the **App Secret** only if you're going Path B.

---

## Path A: System User token (recommended if your ads are in a Business Manager)

Use this path only if you confidently answered "yes" to question 3 in Step 0. If you're unsure, skip down to Path B instead.

### A.1 Make sure your ad account lives inside a Business Manager

1. Go to **https://business.facebook.com/settings** and log in.
2. If you've never created a Business Manager (BM), click **"Create Account"** at **https://business.facebook.com**. Pick a name for the BM, enter your name and email, click **"Submit"**.
3. In the left sidebar: **"Accounts" → "Ad Accounts"**. You should see the ad account listed under **"Ad Accounts I Own"**. If it's listed under **"Ad Accounts I Have Access To"** instead, you don't own it and can't create a System User against it - you'll need to transfer ownership (through the account owner) or switch to Path B.
4. If the ad account isn't listed at all: click **"Add"** (top of the list) → **"Add an ad account"** → enter the ad account ID (format: `1234567890`, the number from Ads Manager's URL).
5. Note your **Business ID** - visible at the top-right of the Business Settings page or in the URL (`business_id=XXXXX`).

### A.2 Create a System User

1. Still in Business Settings, left sidebar: **"Users" → "System Users"**.
2. Click **"Add"** (top-right of the system users list).
3. Name: something like `meta-skill-system-user`. Role: **"Admin"** (required for writes; pick **"Employee"** only if you want read-only). Click **"Create System User"**.
4. You now see the new system user's detail page.

### A.3 Grant the System User access to your ad accounts and app

1. On the system user's detail page, click **"Add Assets"** (usually top-right).
2. A panel opens with tabs: **Pages, Ad Accounts, Apps, Catalogs, Pixels, …**.
3. **Ad Accounts tab:** tick each ad account you want the skill to read/write. Under **"Permissions"**, check **"Manage campaigns"** (gives read + write). For read-only, check **"Read performance"** only. Click **"Save Changes"**.
4. **Apps tab:** tick the app you created in Step 1. Under **"Permissions"**, check **"Manage app"** (or **"Develop app"** - both work). Click **"Save Changes"**.

### A.4 Generate the System User token

1. Still on the system user's page, click **"Generate New Token"**.
2. **Select App:** the one you created in Step 1.
3. **Permissions:** tick `ads_read`, `ads_management`, and `business_management`.
4. **Token expiration:** **"Never"**. (This is the whole point of a System User token.)
5. Click **"Generate Token"**.
6. The token appears once - a long string starting with `EAAB...` or `EAA...`. **Copy it immediately into a password manager.** If you close this dialog without copying, you'll have to regenerate.

### A.5 Find your ad account ID

Open **Ads Manager** in another tab (**https://adsmanager.facebook.com**). The URL contains `act=1234567890`. That `1234567890` is your ad account ID. The format the API expects is with an `act_` prefix: **`act_1234567890`**.

### A.6 Write the `.env` file

Inside the `skills/meta-ads/` folder, copy the template:

**macOS / Linux:**
```bash
cp assets/env.template .env
```

**Windows (PowerShell):**
```powershell
Copy-Item assets\env.template .env
```

**Windows (cmd.exe):**
```
copy assets\env.template .env
```

Now open `.env` in your editor (TextEdit / Notepad / VS Code / whatever) and fill in:
```
META_ACCESS_TOKEN=EAAB...your_system_user_token...
META_AD_ACCOUNT_ID=act_1234567890
META_API_VERSION=v25.0
```
You can leave `META_APP_ID` and `META_APP_SECRET` blank for Path A. Save the file.

### A.7 Verify everything works

**macOS / Linux:**
```bash
python3 scripts/auth_check.py
python3 scripts/list_accounts.py --with-recent-spend
```

**Windows:**
```powershell
python scripts/auth_check.py
python scripts/list_accounts.py --with-recent-spend
```

Expected output:
- `auth_check.py` prints `"ok": true`, your identity as the System User, and at least one ad account.
- `list_accounts.py` lists the accounts the System User can reach, sorted by recent spend. Find yours in the list and confirm it's the one you want.

If `ok: false` or no accounts appear, see the "Ad account discovery problems" section in `references/troubleshooting.md`.

You're done with Path A. Skip ahead to **"What to put in your password manager"**.

---

## Path B: Long-lived user token (for personal ad accounts or Instagram-app boosts)

### B.1 Get a short-lived user token from Graph Explorer

1. In your browser, go to **https://developers.facebook.com/tools/explorer**. Make sure you're logged into the **personal Facebook account** that owns the ads or Instagram account you want to analyze.
2. Top-right, find the **"Meta App"** dropdown. Click it and select the app you created in Step 1.
3. Next dropdown, **"User or Page"**: pick **"User Token"**.
4. Click the **"Permissions"** dropdown/button. A popup opens with a long list of scopes. Tick:
   - `ads_read`
   - `ads_management`
   - `business_management`
   - `pages_show_list` (needed if any boosted content came from a Page)
   
   Close the permissions popup.
5. Click **"Generate Access Token"**. A Facebook OAuth popup appears asking you to confirm. If it lists specific Pages, pick the ones associated with your Instagram account. Click **"Continue"** through the prompts.
6. The token now appears in the big text field at the top of Graph Explorer (long string starting with `EAAB...`). Copy it somewhere safe - a scratch file is fine.

> **This token only lasts ~1-2 hours.** You're about to swap it for a 60-day one in step B.2. Don't dawdle.

### B.2 Exchange for a 60-day long-lived token

1. First, fill in your App ID and App Secret (from Step 2.3) in `.env`. If `.env` doesn't exist yet, copy it:
   
   **macOS / Linux:**
   ```bash
   cp assets/env.template .env
   ```
   
   **Windows (PowerShell):**
   ```powershell
   Copy-Item assets\env.template .env
   ```
   
   **Windows (cmd.exe):**
   ```
   copy assets\env.template .env
   ```
   
   Open `.env` and set:
   ```
   META_APP_ID=1234567890
   META_APP_SECRET=abcdef1234567890abcdef1234567890
   ```
   Save.

2. Now run the exchange script. It will prompt you for the short-lived token and write the resulting 60-day token into `.env` automatically.
   
   **macOS / Linux:**
   ```bash
   python3 scripts/exchange_token.py --write-env
   ```
   
   **Windows:**
   ```powershell
   python scripts/exchange_token.py --write-env
   ```
   
3. When prompted, paste the short-lived token from step B.1 and press Enter. Your input is hidden (no dots or characters appear) - that's intentional, paste and press Enter.

4. On success you'll see `"ok": true`, the expiration (~59.5 days in seconds), and `META_ACCESS_TOKEN` will be set in your `.env`.

5. The short-lived token is now useless - delete it from wherever you pasted it.

### B.3 Discover your ad accounts

**macOS / Linux:**
```bash
python3 scripts/auth_check.py
python3 scripts/list_accounts.py --with-recent-spend
```

**Windows:**
```powershell
python scripts/auth_check.py
python scripts/list_accounts.py --with-recent-spend
```

`list_accounts.py` returns every ad account your Facebook user can see, sorted by last-30-day spend. Find the one with the activity you care about and copy its `id` value (format `act_1234567890`).

### B.4 Pin the default ad account

Open `.env` and add or update:
```
META_AD_ACCOUNT_ID=act_1234567890
```
Save. Now every script will default to this account without needing `--account-id` each time.

### B.5 Re-verify

Run `auth_check.py` one more time:

**macOS / Linux:** `python3 scripts/auth_check.py`
**Windows:** `python scripts/auth_check.py`

It should print `"ok": true` with your identity (your Facebook display name) and a list of visible accounts.

### B.6 The 60-day rotation

Long-lived user tokens expire after ~60 days. Meta emails you a warning ~10 days out, but don't rely on it - set a calendar reminder for 55 days from now. When the token expires:
1. Repeat step B.1 (get a fresh short-lived token from Graph Explorer).
2. Run `exchange_token.py --write-env` again. Same flow, same outcome.

Your App ID and App Secret don't change, so `.env` just needs the new `META_ACCESS_TOKEN`.

---

## App Review (you probably don't need this)

Your app will stay in **"Development mode"** - that's fine. Development mode means *only you* (and anyone you explicitly added as admin/developer of the app) can use the token to hit the API. For a personal-use skill, that's exactly what you want.

App Review is only required if you want *other* Meta users (not you, not your System User) to sign into your app and use it against *their* accounts. If that's your use case, this skill isn't the right shape - each user should run their own setup with their own app.

---

## What to put in your password manager

Save these somewhere safe (1Password, Bitwarden, iCloud Keychain, etc.):

- **App ID**
- **App Secret** (only if you went Path B)
- **Access token** (System User token for Path A, 60-day user token for Path B)
- **Business Manager ID** (Path A only)
- **Ad Account ID(s)** (`act_…` format)

These are the keys to your ad kingdom. Anyone with your token can spend money on your ads and read your ad data - treat the token like a credit card number.

**Do not commit `.env` to git.** If you're copying this skill into a repo of your own, add `.env` to your `.gitignore` before your first commit.

---

## Troubleshooting

If any step failed or produced unexpected output, head to **`references/troubleshooting.md`** for the real-world failure modes we've already seen. The top ones:

- `auth_check.py` returns `ok: true` but `ad_accounts_visible: 0` - token works but sees nothing. Fix in troubleshooting.md.
- `(#3018) start date cannot be beyond 37 months` - Meta only serves data from the last 37 months. Older campaigns are invisible via API; check Ads Manager's archived reports UI instead.
- `ProxyError: Tunnel connection failed: 403` - your environment can't reach `graph.facebook.com`. Run the scripts on your own machine instead of a sandbox.
- `ModuleNotFoundError: No module named 'requests'` - install it with the command from the "prerequisites" section above.
- `(#200) Permissions error` on a write call - your token doesn't have `ads_management` scope (Path B) or the System User doesn't have "Manage campaigns" (Path A).

If none of those match, share the full JSON output of the failing script with the assistant - the error messages Meta returns are usually actionable.
