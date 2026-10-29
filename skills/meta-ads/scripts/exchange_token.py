#!/usr/bin/env python3
"""Exchange a short-lived Meta user access token for a 60-day long-lived one.

This is the Path B workflow from references/setup.md. Graph API Explorer
hands you a short-lived user token (~1-2 hours); you exchange it here for
a 60-day token that's safe to put in .env.

Requires META_APP_ID and META_APP_SECRET to be set (in .env or exported).
Those come from your Meta developer app dashboard → Settings → Basic.

Usage:
  # Reads the short-lived token interactively (doesn't echo) and writes
  # the long-lived token to stdout as JSON.
  python scripts/exchange_token.py

  # Or pass the short-lived token as an arg (less safe - shows in shell history):
  python scripts/exchange_token.py --short-token EAAxxx...

  # Write the exchanged token into .env automatically (replaces META_ACCESS_TOKEN):
  python scripts/exchange_token.py --write-env

Exit code 0 on success, 1 on failure.
"""

from __future__ import annotations

import argparse
import getpass
import os
import sys
from pathlib import Path

import requests

from meta_client import DEFAULT_VERSION, GRAPH_BASE, _load_dotenv, print_json


def exchange(app_id: str, app_secret: str, short_token: str, version: str) -> dict:
    """Call Meta's oauth/access_token endpoint. Returns parsed JSON."""
    url = f"{GRAPH_BASE}/{version}/oauth/access_token"
    params = {
        "grant_type": "fb_exchange_token",
        "client_id": app_id,
        "client_secret": app_secret,
        "fb_exchange_token": short_token,
    }
    resp = requests.get(url, params=params, timeout=30)
    body = resp.json() if resp.content else {}
    if not resp.ok:
        raise RuntimeError(
            f"Token exchange failed (HTTP {resp.status_code}): {body.get('error', body)}"
        )
    return body


def write_env(env_path: Path, token: str) -> None:
    """Replace or append META_ACCESS_TOKEN in the .env file."""
    lines = env_path.read_text().splitlines() if env_path.exists() else []
    out_lines = []
    replaced = False
    for line in lines:
        if line.strip().startswith("META_ACCESS_TOKEN="):
            out_lines.append(f"META_ACCESS_TOKEN={token}")
            replaced = True
        else:
            out_lines.append(line)
    if not replaced:
        out_lines.append(f"META_ACCESS_TOKEN={token}")
    env_path.write_text("\n".join(out_lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--short-token",
        help="Short-lived user token. If omitted, you'll be prompted (hidden input).",
    )
    parser.add_argument(
        "--app-id",
        help="Meta app ID. Defaults to $META_APP_ID.",
    )
    parser.add_argument(
        "--app-secret",
        help="Meta app secret. Defaults to $META_APP_SECRET. Avoid passing via CLI.",
    )
    parser.add_argument(
        "--write-env",
        action="store_true",
        help="Write the long-lived token into .env (replaces META_ACCESS_TOKEN).",
    )
    parser.add_argument(
        "--env-path",
        default=".env",
        help="Path to .env file. Default: .env in the current directory.",
    )
    args = parser.parse_args()

    _load_dotenv()

    app_id = args.app_id or os.environ.get("META_APP_ID")
    app_secret = args.app_secret or os.environ.get("META_APP_SECRET")
    version = os.environ.get("META_API_VERSION", DEFAULT_VERSION)

    if not app_id or not app_secret:
        print_json(
            {
                "ok": False,
                "error": (
                    "Missing META_APP_ID and/or META_APP_SECRET. Add them to .env "
                    "or pass --app-id and --app-secret. Find them in your Meta developer "
                    "app dashboard → Settings → Basic."
                ),
            }
        )
        return 1

    short = args.short_token
    if not short:
        short = getpass.getpass("Paste short-lived token (input hidden): ").strip()
        if not short:
            print_json({"ok": False, "error": "No short token provided."})
            return 1

    try:
        resp = exchange(app_id, app_secret, short, version)
    except Exception as e:
        print_json({"ok": False, "error": str(e)})
        return 1

    long_token = resp.get("access_token")
    expires_in = resp.get("expires_in")
    if not long_token:
        print_json({"ok": False, "error": "Exchange succeeded but no access_token returned.", "raw": resp})
        return 1

    days = expires_in / 86400 if expires_in else None

    if args.write_env:
        env_path = Path(args.env_path)
        write_env(env_path, long_token)
        env_action = f"Wrote META_ACCESS_TOKEN to {env_path.resolve()}"
    else:
        env_action = "Not written to .env (pass --write-env to do so)."

    print_json(
        {
            "ok": True,
            "long_lived_token": long_token,
            "expires_in_seconds": expires_in,
            "expires_in_days": round(days, 1) if days else None,
            "env_action": env_action,
            "reminder": (
                "Delete the short-lived token from wherever you pasted it. "
                "The long-lived token is good for ~60 days - set a calendar "
                "reminder to regenerate."
            ),
        }
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
