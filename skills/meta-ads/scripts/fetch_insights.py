#!/usr/bin/env python3
"""Fetch Meta ads insights with flexible date ranges, breakdowns, and levels.

This is the primary read-data script. It handles:
- Date presets (yesterday, last_7d, last_30d, etc.) AND custom ranges
- Aggregation level (account / campaign / adset / ad)
- Breakdowns (publisher_platform, age, gender, country, placement, ...)
- Custom field selection (defaults cover spend, impressions, clicks, CTR, CPC,
  CPM, frequency, reach, actions, action_values)
- Auto-async fallback for queries Meta refuses to do synchronously

Examples:
  # Last 7 days at the campaign level
  python scripts/fetch_insights.py --level campaign --date-preset last_7d

  # Custom date range, broken down by platform
  python scripts/fetch_insights.py --since 2026-04-01 --until 2026-04-15 \\
    --level campaign --breakdowns publisher_platform

  # Specific campaign, broken down by age & gender
  python scripts/fetch_insights.py --object-id 12345 --level ad \\
    --date-preset last_30d --breakdowns age gender

  # Daily time series for last 30 days
  python scripts/fetch_insights.py --level campaign --date-preset last_30d \\
    --time-increment 1
"""

from __future__ import annotations

import argparse
import json
import sys

from meta_client import (
    MetaAPIError,
    get,
    normalize_account_id,
    paginate,
    poll_async_job,
    post,
    print_json,
)

# Default fields that cover most performance questions.
# `actions` and `action_values` give conversion event counts/values.
DEFAULT_FIELDS = [
    "campaign_id",
    "campaign_name",
    "adset_id",
    "adset_name",
    "ad_id",
    "ad_name",
    "objective",
    "spend",
    "impressions",
    "reach",
    "frequency",
    "clicks",
    "ctr",
    "cpc",
    "cpm",
    "cpp",
    "actions",
    "action_values",
    "cost_per_action_type",
    "purchase_roas",
    "website_purchase_roas",
    "date_start",
    "date_stop",
]

VALID_DATE_PRESETS = {
    "today",
    "yesterday",
    "this_month",
    "last_month",
    "this_quarter",
    "maximum",
    "data_maximum",
    "last_3d",
    "last_7d",
    "last_14d",
    "last_28d",
    "last_30d",
    "last_90d",
    "last_week_mon_sun",
    "last_week_sun_sat",
    "last_quarter",
    "last_year",
    "this_week_mon_today",
    "this_week_sun_today",
    "this_year",
}

VALID_LEVELS = {"account", "campaign", "adset", "ad"}

# Common breakdowns. Meta supports many more - see references/insights-fields.md.
COMMON_BREAKDOWNS = {
    "age",
    "gender",
    "country",
    "region",
    "publisher_platform",  # facebook, instagram, audience_network, messenger
    "platform_position",  # feed, stories, reels, search, ...
    "device_platform",  # mobile, desktop
    "impression_device",
    "product_id",
}


def build_params(args) -> dict:
    fields = args.fields if args.fields else DEFAULT_FIELDS
    params: dict[str, str | int] = {
        "level": args.level,
        "fields": ",".join(fields),
        "limit": 100,
    }

    if args.date_preset:
        params["date_preset"] = args.date_preset
    elif args.since and args.until:
        params["time_range"] = json.dumps({"since": args.since, "until": args.until})
    else:
        # Sensible default rather than failing.
        params["date_preset"] = "last_7d"

    if args.breakdowns:
        params["breakdowns"] = ",".join(args.breakdowns)

    if args.action_breakdowns:
        params["action_breakdowns"] = ",".join(args.action_breakdowns)

    if args.time_increment:
        params["time_increment"] = args.time_increment

    if args.action_attribution_windows:
        params["action_attribution_windows"] = json.dumps(args.action_attribution_windows)

    if args.filtering:
        # filtering expects JSON like [{"field":"campaign.name","operator":"CONTAIN","value":"launch"}]
        params["filtering"] = args.filtering

    return params


def fetch_sync(path: str, params: dict, max_results: int) -> list:
    out = []
    for row in paginate(path, params):
        out.append(row)
        if len(out) >= max_results:
            break
    return out


def fetch_async(account_id: str, params: dict, max_results: int) -> list:
    """Submit an async insights job and fetch the result."""
    print(
        f"[fetch_insights] Falling back to async insights job for {account_id}",
        file=sys.stderr,
    )
    resp = post(f"{account_id}/insights", data=params)
    run_id = resp.get("report_run_id")
    if not run_id:
        raise RuntimeError(f"Async job did not return run_id: {resp}")
    poll_async_job(run_id)
    out = []
    for row in paginate(f"{run_id}/insights", {"limit": 100}):
        out.append(row)
        if len(out) >= max_results:
            break
    return out


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--object-id",
        help=(
            "Object to query insights on. Defaults to the env ad account. "
            "Can be a campaign ID, adset ID, or ad ID - the response will "
            "be scoped to that object."
        ),
    )
    parser.add_argument("--account-id", help="Ad account ID. Used if --object-id not given.")
    parser.add_argument(
        "--level",
        choices=sorted(VALID_LEVELS),
        default="campaign",
        help="Aggregation level. Default: campaign.",
    )
    parser.add_argument(
        "--date-preset",
        choices=sorted(VALID_DATE_PRESETS),
        help="A Meta date preset. Mutually exclusive with --since/--until.",
    )
    parser.add_argument("--since", help="Custom range start (YYYY-MM-DD).")
    parser.add_argument("--until", help="Custom range end (YYYY-MM-DD).")
    parser.add_argument(
        "--breakdowns",
        nargs="+",
        help=(
            f"One or more breakdowns. Common: {sorted(COMMON_BREAKDOWNS)}. "
            "See references/insights-fields.md for the full list. Some "
            "combinations are not allowed by Meta."
        ),
    )
    parser.add_argument(
        "--action-breakdowns",
        nargs="+",
        help="Breakdowns applied to the actions array (e.g. action_type, action_destination).",
    )
    parser.add_argument(
        "--time-increment",
        help="Daily=1, weekly=7, monthly='monthly'. Returns one row per period.",
    )
    parser.add_argument(
        "--action-attribution-windows",
        nargs="+",
        choices=["1d_view", "7d_view", "1d_click", "7d_click", "28d_click"],
        help=(
            "Attribution windows for actions. Default is Meta's account default "
            "(usually 7d_click). Check references/insights-fields.md for caveats."
        ),
    )
    parser.add_argument(
        "--fields",
        nargs="+",
        help="Override the default field list. Use 'all' to mean 'use defaults'.",
    )
    parser.add_argument(
        "--filtering",
        help='JSON filter array, e.g. \'[{"field":"spend","operator":"GREATER_THAN","value":10}]\'',
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=10_000,
        help="Hard cap on rows returned (safety). Default 10000.",
    )
    parser.add_argument(
        "--async",
        dest="force_async",
        action="store_true",
        help="Force async mode. Use for very large queries; otherwise sync is fine.",
    )
    args = parser.parse_args()

    # Resolve the object we're querying.
    if args.object_id:
        path_obj = args.object_id
    else:
        path_obj = normalize_account_id(args.account_id)

    params = build_params(args)
    insights_path = f"{path_obj}/insights"

    try:
        if args.force_async:
            # Async only makes sense at the account level.
            account_id = (
                normalize_account_id(args.account_id)
                if not args.object_id or args.object_id.startswith("act_")
                else path_obj
            )
            rows = fetch_async(account_id, params, args.max_results)
        else:
            try:
                rows = fetch_sync(insights_path, params, args.max_results)
            except MetaAPIError as e:
                # Codes 1, 2 and subcode 99 often signal "too big, try async".
                err = e.body.get("error", {})
                if err.get("code") in (1, 2) and path_obj.startswith("act_"):
                    rows = fetch_async(path_obj, params, args.max_results)
                else:
                    raise
    except MetaAPIError as e:
        print_json({"ok": False, "error": str(e), "meta_error": e.body.get("error")})
        return 1

    print_json(
        {
            "ok": True,
            "object": path_obj,
            "level": args.level,
            "row_count": len(rows),
            "date_range": {
                "preset": args.date_preset,
                "since": args.since,
                "until": args.until,
            },
            "breakdowns": args.breakdowns or [],
            "rows": rows,
        }
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
