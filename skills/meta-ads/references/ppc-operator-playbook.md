# The PPC operator playbook

How to run a live conversion campaign the way a good performance marketer would: launch it right, read it right, change it rarely and for a reason, and keep the user out of the noise.

This complements analysis-playbooks.md (patterns) with the operating loop (what to do on which day).

## The economics come first

Before launch, write down three numbers with the user:
- **Price** of the product (or average order value).
- **Break-even CPA** = the margin per sale (price minus platform/payment fees, minus delivery cost). Above it, every sale loses money.
- **Target CPA** = comfortably under break-even (for a digital product, often 30-50% of the price).

Every recommendation later is phrased against these numbers. "CTR is 5%" means nothing to the user; "a buyer costs 120 on a 400 product, so each sale leaves ~280 before fees" does.

## Launch checklist (Sales objective)

1. Pixel verified end to end, including a real Purchase (pixel-setup.md).
2. Ad account active with a payment method (Meta creates campaigns and ad sets without one, then rejects every ad).
3. Objective `OUTCOME_SALES`, optimization `OFFSITE_CONVERSIONS` with `promoted_object {pixel_id, custom_event_type}`.
4. **Optimization event by volume:** Meta needs roughly 50 events per week per ad set to exit learning. A new pixel has no Purchases, so start on `INITIATED_CHECKOUT` (or `ADD_TO_CART` if even that is rare) and move to `PURCHASE` once purchases reach ~30-50 a week.
5. **Placements: Facebook + Instagram, all positions** (`"placements": "fb_ig_all"` in the spec). Leave Audience Network out of conversion campaigns by default; see "Audience Network" below.
6. Campaign budget (CBO) with 3-5 creatives in one ad set, so Meta can shift spend to what works.
7. Budget big enough to learn: aim for at least ~3-5x the target CPA per day, or accept a slower learning phase.
8. UTM `url_tags` with `{{ad.name}}` so analytics and the CMS see which ad sold.
9. Everything created PAUSED, previewed (`preview_shareable_link` on each ad), then activated as a separate confirmed write.

## The operating loop

| When | Do | Don't |
|---|---|---|
| Day 0 (first hours) | Confirm ads are approved and delivering, pixel events arrive. Pull a **placement breakdown** after the first ~50 spend: this is when structural problems show | Judge performance |
| Days 1-3 | Daily read-only check. Fix only broken things (rejected ad, no delivery after 24h, pixel missing, spend with zero landing-page views, a structural leak like Audience Network) | Change budgets, audiences or creatives because of one bad day |
| Day 4+, or ~3x target CPA spent | Apply the decision table below | Change more than one thing at a time |
| Weekly | Scale what works in small steps, rotate in new creative, add remarketing once audiences are big enough | Restart campaigns that are working |

Every change resets learning. The cost of a reset grows with spend, so structural fixes go in early (day 0-1) and tactical fixes wait for data (day 4+).

**Keep a change log** (date, what, why, spend at the time) next to the campaign. Before/after comparisons are meaningless without it.

## Decision table (day 4+)

| Observed | Action |
|---|---|
| CPA well under target | Raise budget 20-30% every 2-3 days. Never more than ~50% in one step (it resets learning) |
| CPA between target and break-even | Keep budget. Switch off the weakest ad (spent ~1x break-even CPA with zero results), add a new angle, write dedicated ad copy for the winner |
| CPA above break-even, or zero purchases after ~2-3x break-even spent | Find the leaking stage (below), fix that, don't touch budget |
| Frequency above ~3 in prospecting | Creative fatigue: new creative, or broaden |

## Diagnose by funnel stage, not by "the campaign"

Use `funnel_report.py`; its `rates_pct` show stage-to-stage conversion.

| Leak | Typical numbers | Likely cause | Fix |
|---|---|---|---|
| Low CTR | under ~0.8-1% | Creative/hook | New first 3 seconds, new angle |
| Clicks but few landing views | click_to_landing under ~70% | Slow page, broken link, in-app browser issues, accidental clicks | Speed, check link, check placements |
| Landing views but few CTA clicks | landing_to_add_to_cart under ~5% | Offer/page: unclear promise, price shock, weak proof | Page work, not ads |
| CTA clicks but few checkouts | add_to_cart_to_checkout under ~20-30% | Checkout platform page: price placement, trust, mobile layout | Fix the checkout page; remarket to this stage |
| Checkouts but no purchases | checkout_to_purchase low | Payment friction, failed cards, missing payment methods | Test payment yourself, add methods |

Small numbers lie. Under ~20 events in a stage, call it a signal to watch, not a conclusion.

## Known traps (each one cost real money once)

**Audience Network.** With Advantage+ placements Meta can push most of a new campaign's budget into Audience Network (ads inside third-party apps and games). Signature: CTR of 20-30%, very cheap clicks, the 65+ age bracket suddenly taking a big share (accidental taps), and one creative "winning" only because it got that inventory. Those clicks rarely buy. Pull a placement breakdown on day 0; if Audience Network has the majority of spend, restrict placements to Facebook + Instagram (ad set `targeting.publisher_platforms = ["facebook","instagram"]`, keep everything else). Do it early, before the reset costs much.

**Advantage+ audience stretches age.** Age is a suggestion, not a limit, with Advantage+ audience on. Spend outside the set range is normal; a lot of it in one bracket with absurd CTR usually rides on a bad placement.

**Reporting lag.** Lifetime and daily totals lag by hours; the `hourly_stats_aggregated_by_advertiser_time_zone` breakdown for today is near-real-time. Before raising an alarm about "zero conversions today", check the hourly breakdown.

**Underspending during learning.** A CBO campaign in learning often spends well under its daily budget (e.g. 60% of it). Normal for a few days. Persistent underspend after learning means the audience or bid is too narrow.

**Existing Instagram posts become copies.** When an existing IG post is used as the creative but the ad account isn't connected to that Instagram account through a Business Portfolio, Meta creates an ad-only copy (`media_product_type: AD`, zero likes/comments) instead of running the original. Social proof is lost, and comment automations watching the original post won't see comments on the ad. Check `creative.effective_instagram_media_id` against the source ID right after creation and tell the user.

**Captions of existing posts can't be edited in the ad.** Edit them on Instagram first (stale offers, expired dates, "comment X" instructions that won't work on the ad).

**Boosted posts optimize for clicks.** Boosts from the Instagram app use link clicks or profile visits. For selling, a Sales campaign in Ads Manager is the right tool.

## Money-now levers (when the user needs revenue fast)

Paid prospecting is the slowest money: it learns for days. When cash is urgent, put these first, in this order, and say so plainly:
1. **Past buyers of anything** (email/WhatsApp): the warmest audience; an offer for them sells same day.
2. **People who raised a hand** (commented, DMed, signed up): reach them within the platform rules. Instagram allows automated DMs only within 24h of the person's last message, and one private reply per comment. A story asking them to comment again reopens the window legally. Manual DMs from the app are fine. Never blast promotional DMs through the API.
3. **Remarketing by funnel stage** (funnel-remarketing.md): cheap, but audiences need time to reach a deliverable size.
4. **A higher-ticket offer** for buyers (done-with-you setup, group coaching, team workshop). Three high-ticket sales can beat a month of low-ticket optimization.
5. Then scale paid prospecting on what the data says works.

Never invent discounts, scarcity, testimonials or numbers in ad copy. Ask the user what they will truly offer.

## How to report to the user

- Lead with one line: "working / learning, don't touch / broken, here's what".
- Then the money: spend, purchases, cost per purchase vs break-even, revenue, ROAS.
- Then the funnel by stage and the per-ad table.
- Then **one or two** actions, each with why, and any write needs an explicit confirmation naming the action.
- If the user gets confused, stop explaining options. Do the technical part yourself, then give them exactly one next step.
