# Creating campaigns from scratch

`scripts/create_campaign.py` builds an entire campaign tree (campaign → ad sets → creatives → ads) in one call from a spec JSON. This is a write operation - read `write-actions.md` first; the "Campaign creation" section at the bottom of that file is mandatory before you call `--confirm` for the first time in a session.

## The workflow

1. Write a spec JSON that describes the campaign you want.
2. Run `--dry-run`. This reads the spec, queries Meta for account currency, resolves interest names to IDs, and prints the plan - no writes.
3. Walk the plan back to the user. They name the change to confirm.
4. Run `--confirm`. The script creates everything PAUSED by default and writes a state JSON with every ID.
5. If the user wants to activate: they toggle ACTIVE in Ads Manager (or via the API). Never flip ACTIVE programmatically as part of creation - that removes the final checkpoint.

## Spec format (minimum viable)

```json
{
  "campaign_name": "My Campaign - Q2 Flight",
  "objective": "OUTCOME_TRAFFIC",
  "status": "PAUSED",
  "special_ad_categories": [],
  "identity": {
    "page_id": "1234567890",
    "instagram_user_id": "17841400000000000"
  },
  "landing_url": "https://example.com",
  "ad_sets": [
    {
      "name": "Angle A - Broad",
      "daily_budget": 50.00,
      "optimization_goal": "LINK_CLICKS",
      "billing_event": "LINK_CLICKS",
      "targeting": {
        "countries": ["IL"],
        "age_min": 25,
        "age_max": 45,
        "interests": ["Artificial intelligence", "Productivity"],
        "publisher_platforms": ["instagram"],
        "instagram_positions": ["stream", "story", "reels"]
      },
      "image_path": "./creative/angle_a.png",
      "ads": [
        {
          "name": "A1_Direct",
          "message": "Primary body copy - can be multi-line.",
          "headline": "Short punchy headline",
          "description": "Optional secondary line",
          "cta": "LEARN_MORE"
        }
      ]
    }
  ]
}
```

## Field reference

### Top level

| Field | Required | Notes |
|---|---|---|
| `campaign_name` | yes | Shows up in Ads Manager exactly as typed. Put identifiers (e.g. test name, date) in here for sanity later. |
| `objective` | yes | Meta's modern objectives: `OUTCOME_TRAFFIC`, `OUTCOME_AWARENESS`, `OUTCOME_ENGAGEMENT`, `OUTCOME_LEADS`, `OUTCOME_SALES`, `OUTCOME_APP_PROMOTION`. For courses/products without a pixel, use `OUTCOME_TRAFFIC`. For courses/products with a pixel firing Purchase, use `OUTCOME_SALES`. |
| `status` | no | Default `PAUSED`. Only override with `ACTIVE` if you're absolutely sure - you lose the review step. |
| `special_ad_categories` | no | Default `[]`. Required `["CREDIT"]`, `["EMPLOYMENT"]`, `["HOUSING"]`, `["ISSUES_ELECTIONS_POLITICS"]`, or `["FINANCIAL_PRODUCTS_SERVICES"]` for those regulated verticals. Wrong category here can get the whole campaign rejected. |
| `buying_type` | no | Default `AUCTION`. `RESERVED` is for Reach & Frequency (needs account eligibility). |
| `identity.page_id` | yes | The Facebook Page running the ads. Discover via `GET /me/accounts` or `GET /act_.../promote_pages`. |
| `identity.instagram_user_id` | no | The IG account running the ads (discover via the page's `instagram_business_account` field). Required if you want ads to show with your IG handle instead of a generic "Sponsored by Page Name". |
| `landing_url` | yes | Where clicks go. |
| `campaign_daily_budget` | no | Major units. Turns on Advantage+ campaign budget (CBO): the campaign owns the budget and bid strategy, ad sets must NOT set `daily_budget`/`lifetime_budget`. Recommended with 3-5 ads competing in one ad set. |
| `url_tags` | no | Appended to every ad's link, e.g. `utm_source=meta&utm_medium=paid&utm_campaign=x&utm_content={{ad.name}}`. |

### Ad set level

| Field | Required | Notes |
|---|---|---|
| `name` | yes | Descriptive. Good habits: include angle + audience descriptor, e.g. "Angle 1 - Broad IL 25-45 AI". |
| `daily_budget` | one of | Major units in account currency (50.00 for ₪50). Script queries the currency, converts to minor units (agorot/cents). |
| `lifetime_budget` + `end_time` | one of | Use when you want a total spend cap instead of daily pacing. `end_time` is ISO 8601. |
| `billing_event` | no | Default `LINK_CLICKS`. `IMPRESSIONS` if optimizing for reach. |
| `optimization_goal` | no | Default `LINK_CLICKS`. Common: `LANDING_PAGE_VIEWS`, `OFFSITE_CONVERSIONS` (needs pixel + `promoted_object`), `REACH`, `IMPRESSIONS`. With `OFFSITE_CONVERSIONS` use `billing_event: IMPRESSIONS`. |
| `promoted_object` | with OFFSITE_CONVERSIONS | `{"pixel_id": "...", "custom_event_type": "INITIATED_CHECKOUT"}`. Pick the event by volume: Purchase needs ~50/week; a new pixel starts on INITIATED_CHECKOUT or ADD_TO_CART (see ppc-operator-playbook.md). |
| `bid_strategy` | no | Default `LOWEST_COST_WITHOUT_CAP`. Use `COST_CAP` with `bid_amount` when you want to hold a CPA ceiling. |
| `bid_amount` | conditional | Major units. Required if `bid_strategy=COST_CAP` or `LOWEST_COST_WITH_BID_CAP`. |
| `status` | no | Default `PAUSED`. |
| `targeting.countries` | yes | ISO-2 list, e.g. `["IL"]`. Or use full `geo_locations` dict for regions/cities. |
| `targeting.age_min` / `age_max` | no | Defaults to Meta's (18-65). Narrow deliberately. |
| `targeting.genders` | no | `[1]` male, `[2]` female, omit for all. |
| `targeting.interests` | no | List of names - script resolves to IDs via `/search?type=adinterest`. Names with no match are dropped and warned. For stability across runs, use `interest_ids` instead. |
| `targeting.interest_ids` | no | Pre-resolved numeric IDs. Bypasses the search lookup. |
| `targeting.placements` | no | Shortcut. `"fb_ig_all"` = Facebook + Instagram, all positions, no Audience Network (recommended for conversion campaigns). `"advantage_plus"` = let Meta choose everything, including Audience Network. |
| `targeting.publisher_platforms` | no | Default `["instagram"]`. Add `"facebook"`, `"messenger"`, `"audience_network"`. Ignored when `placements` is set. |
| `targeting.instagram_positions` | no | Default `["stream", "story", "reels"]`. |
| `targeting.facebook_positions` | no | Default `["feed", "story", "video_feeds"]` when facebook is in publisher_platforms. |
| `targeting.advantage_audience` | no | Default `true`. Allows Meta to expand beyond your interests when it finds high-intent users outside them. Turn off with `false` for strict targeting tests. |
| `targeting.custom_audiences` | no | List of `{"id": "..."}`. |
| `targeting.excluded_custom_audiences` | no | Same shape. Useful for excluding existing customers. |
| `image_path` | one of | Path to image file, uploaded to `/act_.../adimages` once per ad set. Recommended: 4:5 or 1:1, PNG, under 4 MB. Not needed when every ad uses `source_instagram_media_id`. |
| `image_hash` | one of | Pre-uploaded image hash (skip upload). |

### Ad level

Each ad inside an ad set uses the ad set's image.

| Field | Required | Notes |
|---|---|---|
| `name` | yes | Ad is named `Ad_<name>` and its creative `Creative_<name>`. Keep short and unique within the campaign. |
| `source_instagram_media_id` | no | Run an existing Instagram post (feed or reel) as the ad. The post's caption is the ad text and **cannot be changed in the ad**: edit it on Instagram first. `message`/`headline` are then not needed. Requires `identity.instagram_user_id`. The dry-run reports `boost_eligibility` per post. After creation, check that `effective_instagram_media_id` equals the source; if Meta made an `AD` copy, the post's likes/comments don't carry over (see troubleshooting.md). |
| `message` | yes (image ads) | Primary body text. Multi-line allowed. No length limit enforced by the API, but Meta truncates in-feed around 125 characters before "See More". |
| `headline` | yes (image ads) | Bold headline below the image. Keep under 40 characters for mobile. |
| `description` | no | Small gray line below headline. Often cut by placements. |
| `cta` | no | Default `LEARN_MORE`. Others: `SIGN_UP`, `SHOP_NOW`, `DOWNLOAD`, `GET_OFFER`, `GET_QUOTE`, `SUBSCRIBE`, `CONTACT_US`, `APPLY_NOW`, `WATCH_MORE`, `INSTALL_MOBILE_APP`, `USE_APP`, `MESSAGE_PAGE`, `WHATSAPP_MESSAGE`, `NO_BUTTON`. |
| `standard_enhancements` | removed | Meta deprecated the bundled opt-out (v25 rejects it). The script sends nothing; review the Advantage+ creative toggles per ad in Ads Manager before activating. |
| `status` | no | Default `PAUSED`. |

## Currency handling

The script queries `/act_.../?fields=currency` once at the start and converts `daily_budget` / `lifetime_budget` / `bid_amount` from major units to whatever minor unit the account uses:

- ILS / USD / EUR / GBP etc. → × 100 (agorot, cents, pence)
- JPY / KRW / VND / ISK / TWD / XAF / XOF / CLP → × 1 (no minor unit)

Write budgets in major units only. Never try to pre-convert.

## Interest resolution

`targeting.interests` names are resolved via Meta's `/search?type=adinterest` endpoint. The script takes the top-ranked hit per name. This is convenient for readable specs but has two caveats:

1. The search ranking can change. A spec that resolved to "Productivity" today might resolve to "Productivity (software category)" tomorrow.
2. Search can return no match. Those names are dropped with a `[warn]` log.

For specs you'll re-run months later and want identical targeting, do one dry-run, copy the `resolved_interests` IDs into `interest_ids`, and delete `interests`. Now the targeting is frozen.

## Dry-run validation, payment guard and resume

- `--dry-run` resolves interests and budgets **and** asks Meta to validate the campaign and every creative with `execution_options=["validate_only"]` (nothing is created). Ad sets can't be validated before their campaign exists.
- `--confirm` first checks the ad account has a payment method. Without one Meta creates the campaign and ad sets but rejects every ad, leaving a half-built tree.
- If a run fails halfway, the state file keeps every object created so far (it is the rollback record).
- `--into-adset <adset_id>` adds the spec's ads to an existing ad set (exactly one ad set in the spec), skipping ads that already exist by name. Use it to resume a failed run instead of creating a second campaign.
- After creating: fetch each ad's `preview_shareable_link` and send those links to the user before anyone activates anything. Activation is its own confirmed write (`pause_ad.py --object-id <id> --status ACTIVE`, campaign, ad set and ads; validate with `execution_options=["validate_only"]` first).

## State file and rollback

Every `--confirm` run writes `<spec>_state_<timestamp>.json` with every object ID:

```json
{
  "ok": true,
  "campaign_id": "120...",
  "ad_sets": [
    {"adset_id": "120...", "image_hash": "...", "ads": [{"ad_id": "120...", "creative_id": "120..."}]}
  ],
  "objects": [{"type": "campaign", "id": "120...", "name": "..."}, ...]
}
```

`scripts/rollback_creation.py --state <file> --pause` pauses everything. `--delete` permanently deletes in reverse order (ads → creatives are orphaned → adsets → campaign). Prefer `--pause` unless you really want the objects gone from Ads Manager history.

## Common errors and how to handle them

**`error_subcode 1885036` - Ad account is unsettled.** The campaign objects get created fine but nothing will deliver until the account balance is paid. Don't block on this at creation time; surface it to the user and continue.

**`The ad creative spec is invalid`.** Usually missing `page_id` or a malformed `call_to_action` value. Double-check the `cta` is in `VALID_CTAS` and the landing URL is fully qualified (`https://...`).

**`Invalid parameter` on `flexible_spec`.** Means an interest ID is stale. Re-run the dry-run so search re-resolves names, or remove the offending interest.

**`special_ad_categories` mismatch.** If your ad is in a regulated vertical and you forgot to mark it, Meta rejects the whole ad set. Reviewable in the ad set's `delivery_info` in Ads Manager.

**Account not admin of page.** The ad account owner must have advertiser-or-higher role on the Facebook Page. Fix in Business Settings → Pages → assign.

**Instagram identity missing.** If `instagram_user_id` is omitted, ads still run on Instagram placements but show "Sponsored by <Page Name>" instead of your IG handle. Almost always you want to set it.

## When to NOT use this script

- **You only want to duplicate an existing ad.** Use `scripts/duplicate_ad.py` - it copies targeting, creative, and settings in one shot and is one API call instead of six.
- **You're iterating on creative for an existing ad set.** Creating a new campaign per iteration pollutes Ads Manager. Add new ads to the existing ad set via a partial spec or do it in the UI.
- **You want dynamic creative / catalog ads / collection ads.** Those have different creative shapes (`asset_feed_spec`, `product_set_id`, `template_data`). This script only handles single-image link ads. Extend it or build a sibling script.
