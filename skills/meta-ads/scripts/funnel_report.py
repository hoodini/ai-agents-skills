#!/usr/bin/env python3
"""Read-only funnel report for one campaign: status, review issues and the pixel funnel.

This is the daily "how is it doing" call. It answers, in one JSON object:
  - is everything actually delivering (campaign / ad set / ad status, issues_info, review feedback)?
  - what did each stage of the funnel do (clicks -> landing page views -> view content ->
    add to cart -> initiate checkout -> purchase), lifetime and yesterday, campaign and per ad?
  - optionally, where the money went (--breakdowns placement,age,gender,hour,device)

Never writes to Meta.

Usage:
  python scripts/funnel_report.py --campaign-id 1202xxxxxxxxxxxx
  python scripts/funnel_report.py --campaign-id 1202xxxxxxxxxxxx --breakdowns placement,age,hour
  python scripts/funnel_report.py --campaign-id 1202xxxxxxxxxxxx --today --breakdowns hour

Why per-stage numbers matter: a campaign rarely "doesn't work" as a whole. One stage leaks.
references/ppc-operator-playbook.md maps each leak to its cause and fix.
"""
from __future__ import annotations

import argparse
import sys

from meta_client import MetaAPIError, get, paginate, print_json

# Pixel events as the Marketing API reports them in `actions` / `action_values`.
FUNNEL = [
    ("link_click", "link_clicks"),
    ("landing_page_view", "landing_page_views"),
    ("offsite_conversion.fb_pixel_view_content", "view_content"),
    ("offsite_conversion.fb_pixel_add_to_cart", "add_to_cart"),
    ("offsite_conversion.fb_pixel_initiate_checkout", "initiate_checkout"),
    ("offsite_conversion.fb_pixel_purchase", "purchases"),
]

BREAKDOWNS = {
    "placement": "publisher_platform,platform_position",
    "age": "age",
    "gender": "gender",
    "hour": "hourly_stats_aggregated_by_advertiser_time_zone",
    "device": "device_platform",
    "country": "country",
}

FIELDS = ("ad_name,spend,impressions,reach,frequency,inline_link_clicks,"
          "inline_link_click_ctr,cost_per_inline_link_click,actions,action_values")


def summarize(row: dict) -> dict:
    acts = {a["action_type"]: float(a["value"]) for a in row.get("actions", [])}
    vals = {a["action_type"]: float(a["value"]) for a in row.get("action_values", [])}
    spend = float(row.get("spend", 0))
    out = {
        "spend": spend,
        "impressions": int(row.get("impressions", 0)),
        "reach": int(row.get("reach", 0) or 0),
        "frequency": round(float(row.get("frequency", 0) or 0), 2),
        "ctr_pct": round(float(row.get("inline_link_click_ctr", 0) or 0), 2),
        "cpc": round(float(row.get("cost_per_inline_link_click", 0) or 0), 2),
    }
    for action, name in FUNNEL:
        out[name] = int(acts.get(action, 0))
    if not out["link_clicks"]:
        out["link_clicks"] = int(row.get("inline_link_clicks", 0) or 0)
    out["purchase_value"] = vals.get("offsite_conversion.fb_pixel_purchase", 0.0)
    out["cost_per_checkout"] = round(spend / out["initiate_checkout"], 2) if out["initiate_checkout"] else None
    out["cost_per_purchase"] = round(spend / out["purchases"], 2) if out["purchases"] else None
    out["roas"] = round(out["purchase_value"] / spend, 2) if spend else None
    # Stage-to-stage conversion rates: where the funnel leaks.
    def rate(a, b):
        return round(100 * out[b] / out[a], 1) if out[a] else None
    out["rates_pct"] = {
        "click_to_landing": rate("link_clicks", "landing_page_views"),
        "landing_to_add_to_cart": rate("landing_page_views", "add_to_cart"),
        "add_to_cart_to_checkout": rate("add_to_cart", "initiate_checkout"),
        "checkout_to_purchase": rate("initiate_checkout", "purchases"),
    }
    return out


def insights(object_id: str, level: str, preset: str, breakdowns: str | None = None) -> list[dict]:
    params = {"level": level, "date_preset": preset, "fields": FIELDS, "limit": 200}
    if breakdowns:
        params["breakdowns"] = breakdowns
    rows = list(paginate(f"{object_id}/insights", params))
    out = []
    for r in rows:
        label = r.get("ad_name") or "campaign"
        if breakdowns:
            label = " / ".join(str(r.get(b, "")) for b in breakdowns.split(","))
        out.append({"segment": label, **summarize(r)})
    return sorted(out, key=lambda x: -x["spend"])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--campaign-id", required=True)
    ap.add_argument("--breakdowns", default="", help=f"comma list of: {', '.join(BREAKDOWNS)}")
    ap.add_argument("--today", action="store_true",
                    help="breakdowns for today instead of lifetime (lifetime totals lag by hours; hourly does not)")
    args = ap.parse_args()

    cid = args.campaign_id
    status = "name,status,effective_status,issues_info"
    try:
        adsets = list(paginate(f"{cid}/adsets", {"fields": status + ",learning_stage_info,targeting", "limit": 50}))
        report = {
            "campaign": get(cid, {"fields": status + ",objective,daily_budget,lifetime_budget,start_time"}),
            "adsets": adsets,
            "ads": list(paginate(f"{cid}/ads", {"fields": status + ",ad_review_feedback", "limit": 100})),
            "lifetime": insights(cid, "campaign", "maximum"),
            "yesterday": insights(cid, "campaign", "yesterday"),
            "today": insights(cid, "campaign", "today"),
            "per_ad_lifetime": insights(cid, "ad", "maximum"),
            "breakdowns": {},
        }
        for b in [x.strip() for x in args.breakdowns.split(",") if x.strip()]:
            if b not in BREAKDOWNS:
                sys.exit(f"unknown breakdown '{b}'. Use: {', '.join(BREAKDOWNS)}")
            report["breakdowns"][b] = insights(cid, "campaign", "today" if args.today else "maximum", BREAKDOWNS[b])
    except MetaAPIError as e:
        print_json({"ok": False, "error": str(e), "body": e.body})
        sys.exit(1)
    print_json({"ok": True, **report})


if __name__ == "__main__":
    main()
