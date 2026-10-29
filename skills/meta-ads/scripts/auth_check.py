#!/usr/bin/env python3
"""Verify Meta API credentials work.

Outputs JSON with token info and a count of accessible ad accounts.
Exits non-zero if anything is broken so calling code can detect failure.

Usage: python scripts/auth_check.py
"""

from __future__ import annotations

import argparse
import sys

from meta_client import MetaAPIError, get, get_token, get_version, print_json


# Keep in sync with list_accounts.py
STATUS_NAMES = {
    1: "ACTIVE",
    2: "DISABLED",
    3: "UNSETTLED",
    7: "PENDING_RISK_REVIEW",
    8: "PENDING_SETTLEMENT",
    9: "IN_GRACE_PERIOD",
    100: "PENDING_CLOSURE",
    101: "CLOSED",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.parse_args()  # No args needed; this exists so --help works.

    try:
        token = get_token()
    except RuntimeError as e:
        print_json({"ok": False, "stage": "load_token", "error": str(e)})
        return 1

    # Hit /me to confirm the token is alive and get the user/system-user identity.
    try:
        me = get("me", params={"fields": "id,name"})
    except MetaAPIError as e:
        print_json(
            {
                "ok": False,
                "stage": "verify_token",
                "error": str(e),
                "meta_error": e.body.get("error"),
            }
        )
        return 1

    # Check what ad accounts this token can read.
    try:
        accounts = get(
            "me/adaccounts",
            params={"fields": "id,name,account_status,currency,timezone_name", "limit": 100},
        )
    except MetaAPIError as e:
        print_json(
            {
                "ok": False,
                "stage": "list_adaccounts",
                "error": str(e),
                "meta_error": e.body.get("error"),
                "hint": (
                    "Token is valid but can't read ad accounts. "
                    "Make sure 'ads_read' (and 'ads_management' for write) "
                    "permissions were granted. If you're using a System User token, "
                    "the System User must also be granted access to each ad account "
                    "in Business Settings. If your ads are Instagram boosts on a "
                    "personal ad account outside any BM, switch to a user token "
                    "(Path B in references/setup.md)."
                ),
            }
        )
        return 1

    ad_accounts = accounts.get("data", [])

    # Flag accounts that might surprise the user.
    surprises = []
    status_codes = [a.get("account_status") for a in ad_accounts]
    if 3 in status_codes:
        surprises.append(
            "One or more accounts have status UNSETTLED (unpaid balance). "
            "Reads work; you can't launch new campaigns until billing is cleared."
        )
    if 2 in status_codes:
        surprises.append(
            "One or more accounts are DISABLED (likely policy issues). Insights may still read."
        )
    if len(ad_accounts) == 0:
        surprises.append(
            "Token is valid but sees zero ad accounts. "
            "If you boost from the Instagram app, your account is probably personal - "
            "use a user token (Path B) instead of a System User token."
        )

    print_json(
        {
            "ok": True,
            "api_version": get_version(),
            "identity": me,
            "ad_accounts_visible": len(ad_accounts),
            "ad_accounts": [
                {
                    "id": a.get("id"),
                    "name": a.get("name"),
                    "status_code": a.get("account_status"),
                    "status": STATUS_NAMES.get(
                        a.get("account_status"), f"UNKNOWN({a.get('account_status')})"
                    ),
                    "currency": a.get("currency"),
                    "timezone": a.get("timezone_name"),
                }
                for a in ad_accounts
            ],
            "token_length": len(token),
            "warnings": surprises,
            "next_step": (
                "Run `python scripts/list_accounts.py --with-recent-spend` to see "
                "lifetime + recent spend per account and pick the right one for "
                "META_AD_ACCOUNT_ID in your .env."
            ),
        }
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
