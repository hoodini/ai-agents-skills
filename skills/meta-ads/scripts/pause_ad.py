#!/usr/bin/env python3
"""Pause or resume an ad, ad set, or campaign.

WRITE OPERATION. Read references/write-actions.md before invoking.
The skill is responsible for getting explicit user confirmation before
running this - the script will execute as soon as called (unless --dry-run).

Usage:
  python scripts/pause_ad.py --object-id 12345 --status PAUSED
  python scripts/pause_ad.py --object-id 12345 --status ACTIVE
  python scripts/pause_ad.py --object-id 12345 --status PAUSED --dry-run

Object can be a campaign, ad set, or ad ID - Meta's POST endpoint is
the same shape for all of them.
"""

from __future__ import annotations

import argparse
import sys

from meta_client import MetaAPIError, get, post, print_json


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object-id", required=True, help="Campaign / ad set / ad ID.")
    parser.add_argument(
        "--status",
        required=True,
        choices=["PAUSED", "ACTIVE"],
        help="New status. PAUSED stops delivery; ACTIVE resumes it.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would happen without calling the API.",
    )
    args = parser.parse_args()

    # Fetch current state so we can show before/after, and so the skill can
    # tell the user "it's already PAUSED" if relevant.
    try:
        current = get(args.object_id, params={"fields": "id,name,status,effective_status"})
    except MetaAPIError as e:
        print_json({"ok": False, "stage": "fetch_current", "error": str(e), "meta_error": e.body.get("error")})
        return 1

    if current.get("status") == args.status:
        print_json(
            {
                "ok": True,
                "no_op": True,
                "object_id": args.object_id,
                "name": current.get("name"),
                "status": current.get("status"),
                "message": f"Already {args.status}, no change made.",
            }
        )
        return 0

    if args.dry_run:
        print_json(
            {
                "ok": True,
                "dry_run": True,
                "object_id": args.object_id,
                "name": current.get("name"),
                "current_status": current.get("status"),
                "would_change_to": args.status,
            }
        )
        return 0

    try:
        result = post(args.object_id, data={"status": args.status})
    except MetaAPIError as e:
        print_json({"ok": False, "stage": "update_status", "error": str(e), "meta_error": e.body.get("error")})
        return 1

    # Confirm the change took.
    try:
        after = get(args.object_id, params={"fields": "id,name,status,effective_status"})
    except MetaAPIError:
        after = {}

    print_json(
        {
            "ok": True,
            "object_id": args.object_id,
            "name": current.get("name"),
            "status_before": current.get("status"),
            "status_after": after.get("status", args.status),
            "effective_status_after": after.get("effective_status"),
            "api_response": result,
        }
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
