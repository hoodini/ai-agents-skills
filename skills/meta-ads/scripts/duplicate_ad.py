#!/usr/bin/env python3
"""Duplicate a campaign, ad set, or ad.

WRITE OPERATION. Read references/write-actions.md before invoking.

Useful pattern: when an ad is performing well but fatiguing, duplicate
it to start a fresh learning phase, then optionally edit the new copy
(swap creative, change audience). Default is to create the duplicate
PAUSED so it doesn't immediately start spending.

Meta exposes a `/copies` endpoint on every level. The behavior differs
slightly by object type - see references/write-actions.md.

Usage:
  # Duplicate a campaign (PAUSED by default)
  python scripts/duplicate_ad.py --object-id 12345 --type campaign

  # Duplicate and immediately enable
  python scripts/duplicate_ad.py --object-id 12345 --type campaign --status ACTIVE

  # Duplicate an ad set into a different campaign
  python scripts/duplicate_ad.py --object-id 67890 --type adset \\
    --target-parent-id 11111
"""

from __future__ import annotations

import argparse
import json
import sys

from meta_client import MetaAPIError, get, post, print_json


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object-id", required=True, help="ID of object to duplicate.")
    parser.add_argument(
        "--type",
        required=True,
        choices=["campaign", "adset", "ad"],
        help="Type of object. Must match the object-id.",
    )
    parser.add_argument(
        "--status",
        choices=["PAUSED", "ACTIVE"],
        default="PAUSED",
        help="Status of the new copy. Default PAUSED (safe).",
    )
    parser.add_argument(
        "--target-parent-id",
        help=(
            "For adset/ad duplications: target campaign ID (for adsets) or "
            "target adset ID (for ads). Omit to duplicate within the same parent."
        ),
    )
    parser.add_argument(
        "--rename",
        help="Rename the copy. Default is Meta's '<original> - Copy'.",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    # Verify the source exists and grab its name.
    try:
        source = get(args.object_id, params={"fields": "id,name,status"})
    except MetaAPIError as e:
        print_json({"ok": False, "stage": "fetch_source", "error": str(e), "meta_error": e.body.get("error")})
        return 1

    if args.dry_run:
        print_json(
            {
                "ok": True,
                "dry_run": True,
                "source": source,
                "would_duplicate_as": {
                    "name": args.rename or f"{source.get('name')} - Copy",
                    "status": args.status,
                    "type": args.type,
                    "target_parent_id": args.target_parent_id,
                },
            }
        )
        return 0

    # Build the copy params. Different levels accept slightly different fields.
    data: dict = {"status_option": args.status}

    if args.type == "campaign":
        # deep_copy=true also copies all ad sets and ads inside
        data["deep_copy"] = "true"
    elif args.type == "adset":
        if args.target_parent_id:
            data["campaign_id"] = args.target_parent_id
        # rename_options allows overriding the new ad set's name
        if args.rename:
            data["rename_options"] = json.dumps({"rename_strategy": "ONLY_TOP_LEVEL_RENAME", "rename_prefix": args.rename})
    elif args.type == "ad":
        if args.target_parent_id:
            data["adset_id"] = args.target_parent_id

    try:
        result = post(f"{args.object_id}/copies", data=data)
    except MetaAPIError as e:
        print_json({"ok": False, "stage": "duplicate", "error": str(e), "meta_error": e.body.get("error")})
        return 1

    new_id = result.get("copied_campaign_id") or result.get("copied_adset_id") or result.get("copied_ad_id") or result.get("id")

    # Apply rename if requested and not handled above.
    if args.rename and args.type in ("campaign", "ad") and new_id:
        try:
            post(new_id, data={"name": args.rename})
        except MetaAPIError as e:
            print_json(
                {
                    "ok": True,
                    "warning": "Duplicated but failed to rename",
                    "new_id": new_id,
                    "rename_error": str(e),
                    "raw": result,
                }
            )
            return 0

    print_json(
        {
            "ok": True,
            "source_id": args.object_id,
            "source_name": source.get("name"),
            "new_id": new_id,
            "new_status": args.status,
            "type": args.type,
            "raw": result,
        }
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
