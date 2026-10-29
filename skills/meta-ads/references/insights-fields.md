# Insights Fields, Breakdowns & Gotchas

Read this when constructing a custom insights query (anything beyond the defaults in `fetch_insights.py`). It's a reference, not a tutorial - skim for what you need.

## Standard fields you'll use most

| Field | What it means | Notes |
|---|---|---|
| `spend` | Money spent in the account currency (major units, e.g., 12.34) | Already in major units, unlike budget fields elsewhere. |
| `impressions` | Times the ad was rendered | Includes auto-play video impressions. |
| `reach` | Unique people reached | Not always returned at the ad level for cross-placement deduplication reasons. |
| `frequency` | impressions / reach | Above ~3 is the rough fatigue zone. |
| `clicks` | All clicks (including profile clicks, like clicks). | Use `link_clicks` from `actions` array for outbound clicks only. |
| `ctr` | clicks / impressions, as a percentage. | Same caveat - this is "all clicks" CTR. For link CTR, divide `actions[link_click]` by impressions. |
| `cpc` | spend / clicks | All-clicks CPC. |
| `cpm` | (spend / impressions) × 1000 | Cost per 1000 impressions. |
| `cpp` | spend / reach × 1000 | Cost per 1000 unique reach. |
| `purchase_roas` | Purchase value / spend | Returned as an array of objects, one per attribution scope. See below. |
| `actions` | All conversion events for this row | Big array, see below. |
| `action_values` | Monetary value of those events (where applicable) | Parallel to `actions`. |
| `cost_per_action_type` | Cost per event, broken out by action type | Useful for CPA-by-event-type. |

## The `actions` array - the most important and most confusing field

`actions` is a list like:

```json
[
  {"action_type": "link_click", "value": "234"},
  {"action_type": "post_engagement", "value": "1240"},
  {"action_type": "onsite_conversion.messaging_conversation_started_7d", "value": "12"},
  {"action_type": "purchase", "value": "8"},
  {"action_type": "omni_purchase", "value": "8"}
]
```

Common `action_type` values you'll grep for:

- `link_click` - outbound link clicks (the meaningful CTR numerator for traffic objectives)
- `post_engagement` - likes/comments/shares/clicks combined
- `landing_page_view` - pixel fired LPV (more reliable signal than link_click, requires Pixel)
- `purchase` - conversion via Pixel/CAPI
- `omni_purchase` - purchase across all surfaces (web + app + offline) - usually what you want
- `lead` - lead form submission
- `complete_registration` - sign-up event
- `onsite_conversion.messaging_conversation_started_7d` - **this is your CTWA conversion**
- `onsite_conversion.messaging_first_reply` - first business reply in WhatsApp
- `view_content`, `add_to_cart`, `initiate_checkout` - funnel steps if Pixel is configured

**For Click-to-WhatsApp specifically**, look for action types prefixed with `onsite_conversion.messaging_*`. If they're missing, the campaign isn't a CTWA campaign or the pixel mapping isn't set up correctly.

## `purchase_roas` shape

```json
[
  {"action_type": "omni_purchase", "value": "3.42"},
  {"action_type": "purchase", "value": "3.18"}
]
```

Use `omni_purchase` as the headline ROAS unless you have a reason to scope to web-only.

## Breakdowns - what you can split data by

Pass to `--breakdowns` (one or more, but not all combinations are legal):

| Breakdown | Values | Compatible with |
|---|---|---|
| `publisher_platform` | facebook, instagram, audience_network, messenger | most others |
| `platform_position` | feed, instream_video, story, reels, search, etc. | publisher_platform |
| `device_platform` | mobile_app, mobile_web, desktop | most |
| `impression_device` | iphone, ipad, android_smartphone, ... | publisher_platform |
| `age` | 13-17, 18-24, 25-34, 35-44, 45-54, 55-64, 65+ | gender |
| `gender` | male, female, unknown | age |
| `country` | ISO country codes | most |
| `region` | sub-country region | country |
| `dma` | Designated Market Area (US only - being phased out for Comscore Markets in 2026 for autos) | - |
| `product_id` | for catalog ads | - |
| `hourly_stats_aggregated_by_advertiser_time_zone` | hour of day | limited combos |

**Action breakdowns** are different - they split the `actions` array, not the rows:

| Action breakdown | Splits actions by |
|---|---|
| `action_type` | (default - already in actions array) |
| `action_destination` | URL for link clicks |
| `action_target_id` | object the action was on |
| `action_device` | the device the conversion happened on |

## Date presets

Use these via `--date-preset`:

`today`, `yesterday`, `last_3d`, `last_7d`, `last_14d`, `last_28d`, `last_30d`, `last_90d`, `this_week_mon_today`, `this_week_sun_today`, `last_week_mon_sun`, `last_week_sun_sat`, `this_month`, `last_month`, `this_quarter`, `last_quarter`, `this_year`, `last_year`, `maximum`.

For custom ranges, use `--since YYYY-MM-DD --until YYYY-MM-DD`.

## Time series via `--time-increment`

- `1` = daily (one row per day per object)
- `7` = weekly (Mon-Sun)
- `monthly` = one row per calendar month
- omitted = single row covering the whole period

## Attribution windows - the confusion zone

By default, Meta returns numbers using your **account's default attribution setting** (usually 7-day click). To request specific windows, pass `--action-attribution-windows`:

- `1d_view` - viewed ad, converted within 1 day, no click
- `7d_view` - same but 7 days
- `1d_click` - clicked, converted within 1 day
- `7d_click` - clicked, converted within 7 days (most common default)
- `28d_click` - clicked, converted within 28 days (deprecated for some objectives)

**Important:** the `value` in each action object is bound to one window - if you request multiple windows, each row gets per-window subkeys. This trips up everyone the first time.

## Things Meta won't let you do (that you might try)

- **Combine `breakdowns: age` with `breakdowns: country` AND a third dimension** - usually fails with "Cannot have action breakdowns ... with the breakdowns".
- **Request `reach` at the ad level over a long period broken down by demographic** - Meta refuses on privacy grounds. Aggregate higher (campaign or account level) instead.
- **Get hourly data older than 35 days.**
- **Get per-day rows for ranges over 90 days synchronously** - falls back to async automatically in our `fetch_insights.py`, but be patient.
- **Mix `purchase_roas` with `breakdowns=product_id`** - known to silently return zeros. Use action_values + product_id breakdown instead.

## When numbers don't match Ads Manager

This happens *constantly*. Usual causes:
1. **Different attribution window.** Ads Manager defaults can differ from API defaults.
2. **Time zone.** Ad account uses one TZ; you might be querying in another.
3. **Currency conversion.** `spend` is in the account currency. If the account is multi-currency, the rate at query time may differ from when the ad ran.
4. **Late-arriving data.** The current day is incomplete; conversions can take 24-72 hours to fully attribute.
5. **Data freshness for "last 7d"** - Meta sometimes lags 1-2 hours on hot data.

If a number is more than 5% off from Ads Manager, check attribution window first. If still off, query at a more granular level and sum - sometimes Meta's aggregate roll-up has reporting discrepancies.

## Useful field combinations

**Link CTR (the one that actually matters):**
```
fields: impressions, actions[action_type=link_click]
formula: link_clicks / impressions
```

**True CPA for an event:**
```
fields: spend, actions[action_type=purchase]
formula: spend / purchase count
```
Or just request `cost_per_action_type` and read the right one from the array.

**CTWA cost per conversation:**
```
fields: spend, actions
filter actions for action_type = onsite_conversion.messaging_conversation_started_7d
formula: spend / count
```
