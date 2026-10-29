# Remarketing by funnel stage

This is the implementation guide for the re-engage and close layers. The full ladder (including video-viewer and engaged-visitor rungs, lookalikes, testing and scaling rules) is in `full-funnel-system.md`.

People drop off at different stages for different reasons. Each stage gets its own audience and its own message. This is usually the cheapest revenue in an account, once the audiences are big enough to deliver.

## The stages

| Stage | Audience (pixel events) | Why they stopped | What the ad does | Link to |
|---|---|---|---|---|
| 0. Warm, never visited | Instagram/Facebook engagers (last 30-90 days) minus site visitors | Haven't seen the offer | Introduce the offer with proof they'd recognize | Landing page |
| 1. Visited, didn't click to buy | `PageView`/`ViewContent` (14 days) minus `AddToCart` | "Is this for me? Is it too technical? Is it real?" | Answer the main objection: who it's for, what you get, proof | Landing page |
| 2. Clicked to buy, didn't start paying | `AddToCart` (14 days) minus `InitiateCheckout` | Saw the price or the checkout page and hesitated | Outcome and value: what they'll have built / gained, price in context | **Checkout page directly** |
| 3. Started paying, didn't pay | `InitiateCheckout` (7 days) minus `Purchase` | Friction, doubt, interruption | Short reminder, reassurance, a real (approved) incentive if any | **Checkout page directly** |
| All stages | Exclude `Purchase` (180 days) | They bought | Separate upsell campaign instead | |

Each stage excludes the next one, so a person sees only the ad for the stage they're at.

## Sizing reality

- Meta needs roughly **100+ matched people** to deliver to a custom audience at all, and delivery is poor under ~1,000. Stages 2 and 3 are tiny early on (a few percent of visitors). Merge 2+3 until each is big enough; start with stages 0-1; turn on the hot stages as they grow.
- Audiences fill retroactively (pixel history within the retention window), so **create them on day one** even if they can't run yet.
- Check sizes: `GET /<audience_id>?fields=approximate_count_lower_bound,approximate_count_upper_bound`.

## Structure

- **A separate remarketing campaign with its own budget.** Inside a CBO prospecting campaign, Meta sends almost all spend to the large prospecting ad set and the remarketing ad sets starve.
- One ad set per stage, ad set budgets (or a small CBO across stages), placements Facebook + Instagram.
- Budget: small, typically 10-25% of prospecting. Frequency will be high by design (small audiences); cap the creative's life, rotate weekly.
- Optimization: the event of the *next* stage (stage 1 -> AddToCart or InitiateCheckout, stages 2-3 -> Purchase if volume allows, else InitiateCheckout).
- On the prospecting side, exclude past purchasers (and optionally recent visitors), so the two campaigns don't bid against each other for the same people.

## Creating website custom audiences through the API

`POST /act_<id>/customaudiences` with a `rule` (JSON) and `prefill=true`:

```json
{
  "name": "RMK 2 | AddToCart 14d | no checkout",
  "rule": {
    "inclusions": {"operator": "or", "rules": [{
      "event_sources": [{"id": "<PIXEL_ID>", "type": "pixel"}],
      "retention_seconds": 1209600,
      "filter": {"operator": "and", "filters": [{"field": "event", "operator": "eq", "value": "AddToCart"}]}
    }]},
    "exclusions": {"operator": "or", "rules": [{
      "event_sources": [{"id": "<PIXEL_ID>", "type": "pixel"}],
      "retention_seconds": 1209600,
      "filter": {"operator": "and", "filters": [{"field": "event", "operator": "eq", "value": "InitiateCheckout"}]}
    }]}
  },
  "prefill": true
}
```

- Retention: 7 days = 604800, 14 = 1209600, 30 = 2592000, 180 = 15552000.
- Creating an audience is a write: dry-run it in words to the user (name, include, exclude, window) and get an explicit confirmation, same as any other write (write-actions.md).
- **Engagement audiences** (Instagram account / Facebook page engagers) have a different rule shape; creating them in Ads Manager -> Audiences -> Create audience -> Custom audience -> Instagram account is simpler and less error-prone. Use the API only after testing the shape.
- Reference the audiences in ad sets via `targeting.custom_audiences` / `targeting.excluded_custom_audiences` (create_campaign.py supports both).

## Creative per stage

- Short vertical video (9:16, 15-25 seconds), one message per stage, the objection answered in the first 3 seconds.
- **Use real proof the product page already shows** (real screenshots, real press, real numbers). Never invent testimonials, counts or scarcity; ask the user for anything that isn't on the page.
- The creator's own voice beats synthetic narration for trust; on-screen text plus music is the fastest fallback.
- Stages 2-3 link straight to the checkout page; there's no reason to send someone who already saw the price back to the landing page.
