#!/usr/bin/env python3
"""Discover every ad account the current token can see.

This is the FIRST script to run after auth_check - it's the answer to
"which ad account should I use?" when the user has many.

By default, returns ALL accounts (ACTIVE, UNSETTLED, DISABLED, CLOSED, etc.)
sorted by lifetime spend (desc). Use --active-only to filter to ACTIVE
accounts only. Use --with-recent-spend to additionally pull last-30-day
spend per account so you can see which accounts are currently running
(takes one extra API call per account, slower).

Usage:
  python scripts/list_accounts.py
  python scripts/list_accounts.py --active-only
  python scripts/list_accounts.py --with-recent-spend
  python scripts/list_accounts.py --currency ILS
"""

from __future__ import annotations

import argparse
import sys

from meta_client import MetaAPIError, get, paginate, print_json


# Account status codes per Meta docs:
# https://developers.facebook.com/docs/marketing-api/reference/ad-account
STATUS_NAMES = {
    1: "ACTIVE",
    2: "DISABLED",
    3: "UNSETTLED",  # outstanding unpaid balance - reads still work, no new spend
    7: "PENDING_RISK_REVIEW",
    8: "PENDING_SETTLEMENT",
    9: "IN_GRACE_PERIOD",
    100: "PENDING_CLOSURE",
    101: "CLOSED",
    201: "ANY_ACTIVE",
    202: "ANY_CLOSED",
}

# Currencies Meta returns amount_spent in minor units (hundredths).
# JPY, KRW, VND etc. are returned in whole units - no divide.
# Full list: https://developers.facebook.com/docs/marketing-api/currencies
ZERO_DECIMAL_CURRENCIES = {"JPY", "KRW", "VND", "CLP", "ISK", "UGX", "XAF", "XOF", "TWD"}


def to_major(amount_minor: str | None, currency: str | None) -> float | None:
    """Convert 'amount_spent' string from minor units to the friendly amount.

    Meta returns amount_spent as a string of MINOR units for most currencies
    (agorot, cents, pence). Divide by 100 unless zero-decimal currency.
    """
    if amount_minor is None:
        return None
    try:
        n = int(amount_minor)
    except (ValueError, TypeError):
        return None
    if currency and currency.upper() in ZERO_DECIMAL_CURRENCIES:
        return float(n)
    return n / 100.0


def fetch_recent_spend(account_id: str) -> dict:
    """Fetch last-30-day spend + last-7-day spend for a single account.

    Returns {"last_30d_spend": float, "last_7d_spend": float} in major units.
    Returns zeros on error (some accounts reject insights queries - skip quietly).
    """
    out = {"last_30d_spend": 0.0, "last_7d_spend": 0.0}
    for preset, key in [("last_30d", "last_30d_spend"), ("last_7d", "last_7d_spend")]:
        try:
            r = get(
                f"{account_id}/insights",
                params={"fields": "spend", "date_preset": preset, "level": "account"},
            )
            data = r.get("data", [])
            if data:
                out[key] = float(data[0].get("spend", 0) or 0)
        except MetaAPIError:
            pass  # best-effort; account may not allow insights reads
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--active-only",
        action="store_true",
        help="Only return accounts with account_status=1 (ACTIVE). Default: show all.",
    )
    parser.add_argument(
        "--with-recent-spend",
        action="store_true",
        help=(
            "Fetch last-30-day and last-7-day spend for each account. "
            "One extra API call per account - slower but tells you which "
            "accounts are actually running right now."
        ),
    )
    parser.add_argument(
        "--currency",
        help="Filter to accounts with this currency (e.g. USD, ILS, EUR).",
    )
    args = parser.parse_args()

    fields = ",".join(
        [
            "id",
            "name",
            "account_status",
            "currency",
            "timezone_name",
            "amount_spent",
            "balance",
            "spend_cap",
            "business",
            "business_name",
            "disable_reason",
            "created_time",
        ]
    )

    accounts = []
    try:
        for acc in paginate("me/adaccounts", {"fields": fields, "limit": 100}):
            status_code = acc.get("account_status")
            if args.active_only and status_code != 1:
                continue
            currency = acc.get("currency")
            if args.currency and currency and currency.upper() != args.currency.upper():
                continue

            business = acc.get("business") or {}
            row = {
                "id": acc.get("id"),
                "name": acc.get("name"),
                "status_code": status_code,
                "status": STATUS_NAMES.get(status_code, f"UNKNOWN({status_code})"),
                "currency": currency,
                "timezone": acc.get("timezone_name"),
                "business_id": business.get("id"),
                "business_name": business.get("name") or acc.get("business_name"),
                "amount_spent_raw": acc.get("amount_spent"),
                "amount_spent": to_major(acc.get("amount_spent"), currency),
                "balance": to_major(acc.get("balance"), currency),
                "spend_cap": to_major(acc.get("spend_cap"), currency),
                "disable_reason": acc.get("disable_reason"),
                "created_time": acc.get("created_time"),
            }

            if args.with_recent_spend:
                row.update(fetch_recent_spend(row["id"]))

            accounts.append(row)
    except MetaAPIError as e:
        print_json({"ok": False, "error": str(e), "meta_error": e.body.get("error")})
        return 1

    # Sort: recent spend first (if available), then lifetime spend, then name.
    def sort_key(a):
        recent = a.get("last_30d_spend", 0) or 0
        lifetime = a.get("amount_spent") or 0
        return (-recent, -lifetime, a.get("name") or "")

    accounts.sort(key=sort_key)

    hint_parts = []
    if not args.with_recent_spend:
        hint_parts.append(
            "Re-run with --with-recent-spend to see which accounts are currently active."
        )
    has_unsettled = any(a["status_code"] == 3 for a in accounts)
    if has_unsettled:
        hint_parts.append(
            "One or more accounts are UNSETTLED (unpaid balance). Reads still work; "
            "new campaigns blocked until billing is cleared in Ads Manager."
        )
    has_disabled = any(a["status_code"] == 2 for a in accounts)
    if has_disabled:
        hint_parts.append(
            "Some accounts are DISABLED - likely policy issues; insights may still read."
        )

    print_json(
        {
            "ok": True,
            "count": len(accounts),
            "filters": {"active_only": args.active_only, "currency": args.currency},
            "sort": "last_30d_spend desc, then amount_spent desc"
            if args.with_recent_spend
            else "amount_spent desc, then name",
            "hints": hint_parts,
            "accounts": accounts,
        }
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
