# The full-funnel system: signals, intent ladder, audiences, creative, testing, scaling

This is the doctrine behind every campaign the skill runs for someone selling a product online. Read it before designing audiences or campaigns, and come back to it every time you analyse results. The other references (pixel-setup, funnel-remarketing, ppc-operator-playbook, sales-platform-data) are parts of this system.

The idea in one line: **every action a person takes is a signal of intent; group people by the highest signal they gave, show each group the one message that answers why they stopped there, measure each layer separately, and move money toward what produces buyers.**

---

## 1. Signal inventory: everything Meta (and the stack) can know

Before building anything, list which of these signals exist for this business, and close the gaps.

| Where | Signal | How it's captured |
|---|---|---|
| The ad | Impression, reach, frequency | Automatic |
| The ad (video) | Watched 3 seconds, ThruPlay (15s or complete), 25% / 50% / 75% / 95% | Automatic, per video. Usable as **video engagement audiences** |
| The ad | Link click, landing page view | Automatic (landing page view needs the pixel) |
| The ad / profile | Like, comment, share, save, profile visit, DM | Automatic. **Instagram account / Facebook page engagement audiences** |
| Landing page | Visit (PageView), saw the offer (ViewContent) | Pixel base code + ViewContent |
| Landing page | **Engaged**: stayed N seconds, scrolled past the offer, played the page's video | **Custom events you add** (section 4). Without them, "stayed and left" and "bounced" look the same |
| Landing page | Time spent percentile (top 25% / 10% / 5%) | Website custom audience option, no code needed |
| Landing page | Clicked the buy CTA | `AddToCart` on the CTA (pixel-setup.md) |
| Checkout platform | Reached the course/product page | PageView with the platform's URL |
| Checkout platform | **Registered / left details** | Often no pixel event. Look for a **URL change** after registration (read the platform's JS bundle for its routes: e.g. a `/shoppingcart` route) and build URL-based audiences on it. Also the platform's "signed up" list in the mailing tool |
| Checkout platform | Clicked pay | `InitiateCheckout` (often fired by the platform) |
| Checkout platform | Paid | `Purchase` with value (platform) + "paid" list + platform enrollments |
| CRM / mailing tool | Signed up, paid, past buyers of other products, leads | Lists. Usable as **customer list audiences** (upload, hashed by Meta) for ads and as exclusions |
| Course platform | Progress, not started, completed | Platform data (sales-platform-data.md). Used for email, testimonials, upsell |

**Gap check, every time:** if two stages can't be told apart by any signal, either add a signal (custom event, URL rule, list) or merge the stages honestly.

---

## 2. The intent ladder

Each person belongs to the **highest** rung they reached. Rungs are mutually exclusive: every audience excludes all rungs above it and all buyers. That is what stops a person who reached the payment page from also getting the "is this for me?" ad.

| Rung | Who | Signal / audience | Window | Main objection | Reach by |
|---|---|---|---|---|---|
| L0 | Never interacted | Broad / interests / lookalikes | - | Doesn't know it exists | Prospecting ads |
| L1 | Glanced (3s to 25% of a video, or impression only) | Video 3s / 25% | 14-30d | Weak interest | **Usually not worth a separate budget**; it's mostly noise. Leave to prospecting |
| L2 | **Interested viewer**: watched 50%+ / ThruPlay / 75%+, or engaged (like, comment, save, share, profile visit), did not visit the site | Video 50%+ ∪ ThruPlay ∪ IG/FB engagers, minus website visitors | 30-60d | "Interesting, but not now / is it real?" | Proof ads, different angle |
| L3 | Visited the landing page and left fast | PageView/ViewContent, minus Engaged, minus AddToCart | 14-30d | Message-market mismatch or first impression | A different hook; test whether they're worth chasing at all |
| L4 | **Engaged visitor**: stayed / scrolled / played the video, didn't click buy | Engaged (custom event or time-spent top 25%), minus AddToCart | 14-30d | "Is it for me? Too technical? Worth it?" | Objection ads: who it's for, outcomes, proof |
| L5 | Clicked buy, reached the checkout platform, didn't register | AddToCart, minus registration URL, minus InitiateCheckout | 7-14d | Saw the price or the form | Value ads: what they'll have, price in context. Link straight to checkout |
| L6 | **Registered** (left details), didn't click pay | Registration URL (e.g. contains `shoppingcart`) or "signed up" list, minus InitiateCheckout | 7-14d | Hesitation at commitment | Email sequence first; ad: reassurance, "what's inside", a face |
| L7 | Clicked pay, didn't complete | InitiateCheckout, minus Purchase | 3-7d | Friction, card, distraction, last doubt | Email + short "one click left" ad; check payment works |
| L8 | Bought | Purchase ∪ "paid" list ∪ platform enrollments | 180d | - | **Excluded from all sales ads.** Email: activation, testimonial, upsell |

**Video depth matters, and it's how you read interest from the ad itself:**
- Hook rate = 3-second views ÷ impressions. Under ~25% = the first seconds don't stop the scroll.
- Hold rate = ThruPlays ÷ 3-second views. Low = the middle loses them; the promise isn't paid off.
- A person who watched 75% and didn't click is not "uninterested": the creative worked, the click didn't happen. Give them a different call to action or proof, not the same video again.
- Compare 50%/75% viewers' later conversion with 25% viewers' in the data before investing in a rung.

**Size rules:** an audience needs roughly 100+ matched people to deliver at all, and below ~1,000 delivery is weak and frequency climbs fast. Early on, merge adjacent rungs (L5+L6+L7 as "checkout abandoners"; L3+L4 as "visitors") and split them as they grow. Never leave a rung with no coverage just because it's small: email covers L6-L7 from the first person.

---

## 3. Campaign architecture

| Campaign | Audiences | Objective / event | Budget share (starting point) |
|---|---|---|---|
| **Prospecting (TOF)** | Broad with Advantage+ audience; lookalikes as a test | Sales, optimize for the deepest event with ~50/week (often InitiateCheckout early) | 65-75% |
| **Re-engage (MOF)** | L2 + L3 + L4 | Sales (AddToCart or InitiateCheckout) | 15-25% |
| **Close (BOF)** | L5 + L6 + L7 | Sales (Purchase if volume allows, else InitiateCheckout) | 5-15%, capped by audience size |
| Retention | L8 | Email and organic, rarely ads (upsell launches only) | - |

- MOF and BOF are separate campaigns with their own budgets; inside a prospecting CBO they starve.
- Prospecting excludes L4+ and buyers so it doesn't pay twice for people the closing campaigns already chase.
- BOF budget follows audience size: when frequency passes ~4-6 per week in a rung, the budget is too big for it.

---

## 4. Instrument the landing page for the ladder

Add these custom events next to the base pixel (values from config, not hard-coded):

```js
// engaged: 30 seconds on the page OR scrolled past ~60% (once per page view)
(function () {
  var sent = false;
  function engaged(reason) { if (sent || !window.fbq) return; sent = true; fbq('trackCustom', 'EngagedVisit', {reason: reason}); }
  setTimeout(function () { engaged('time30'); }, 30000);
  addEventListener('scroll', function () {
    var h = document.documentElement;
    if ((h.scrollTop + innerHeight) / h.scrollHeight > 0.6) engaged('scroll60');
  }, {passive: true});
})();
// the page's own video, if any
document.querySelectorAll('video').forEach(function (v) {
  v.addEventListener('play', function () { if (window.fbq) fbq('trackCustom', 'PageVideoPlay'); }, {once: true});
});
```

Verify each in Test events. Custom events can be used in audiences right away (rule field `event`, value `EngagedVisit`); to optimize on one, create a custom conversion.

---

## 5. Building the audiences

**Website audiences (API, tested shape):** `POST /act_<id>/customaudiences` with `rule` and `prefill=true`; see funnel-remarketing.md for the JSON. Variants:
- By event: `filter: {field: "event", operator: "eq", value: "AddToCart"}`
- By URL: `filter: {field: "url", operator: "i_contains", value: "shoppingcart"}`
- Exclusions in the same `rule` (`exclusions`), so the ladder is built into each audience.
- Time spent (top 25%) is easiest in the Ads Manager UI (Website source -> "Visitors by time spent").

**Engagement audiences (UI is the reliable path):** Ads Manager -> Audiences -> Create audience -> Custom audience ->
- **Video** -> choose the % (3s / ThruPlay / 25 / 50 / 75 / 95) and pick the videos (the reels used in ads, plus organic reels about the product) -> window.
- **Instagram account** -> "Everyone who engaged" or narrower (saved, messaged, visited profile) -> window.
Build L2 as one audience combining video 50%+ and engagers, then exclude website visitors in the ad set.

**Customer lists:** upload the mailing tool's lists (CSV with email/phone) as customer list audiences: "signed up", "paid", "all past buyers". The first upload needs the Custom Audience terms accepted in Ads Manager. Re-upload or sync weekly; lists don't update themselves.

**Lookalikes:**
- Seed quality beats size, but Meta needs at least 100 people in the seed country; 1,000+ is much better.
- Best seeds, in order: purchasers (all products, with value if available) -> InitiateCheckout+Purchase -> 75% video viewers + engagers.
- A young product has few buyers: use **past buyers of the seller's other products** (customer list) as the seed. They're the same kind of person.
- Start at 1% of the country; test 1-3% or 3-5% only as a separate ad set. Compare against broad Advantage+ audience; in many accounts broad wins, so lookalikes are a test, not a default.

---

## 6. Creative system: one message per rung

For each rung write down: the objection, the one message that answers it, the proof, the format, the CTA and the destination. Never reuse the prospecting video as the remarketing ad unchanged; the person already saw it.

| Rung | Message job | Proof | Format | Destination |
|---|---|---|---|---|
| L0 | Stop the scroll, show the outcome | The real product working | Video (hook in the first 1-2 seconds), the creator's face | Landing page |
| L2 | "It's real, and it's for someone like you" | Real result, press/authority, a student | Short video or carousel of proof | Landing page |
| L3 | A different angle than the one that failed | - | New hook / format | Landing page |
| L4 | Answer the top objection (who it's for, technical level, time) | Syllabus outcome, "no code" demo | Face-to-camera 15-20s, or static with one strong line | Landing page or checkout |
| L5-L6 | What they'll have built, price in context, reassurance | Concrete lesson outcome, testimonial | Screen recording of the result, a face | **Checkout directly** |
| L7 | One click left, help if something broke | - | Text or 10-15s face | **Checkout directly** |

Hooks to test (first line / first 2 seconds), one at a time: the outcome ("my bot answered 40 emails while I slept"), the objection ("not technical? good"), the authority ("they let me show this on national TV"), the number ("17 lessons, 4 hours"), the curiosity ("I didn't type a single line of code and..."). Claims must be true and provable; never invent testimonials, numbers, scarcity or discounts.

Where text is enough, the skill writes it. Where a face or a screen recording is needed, write a second-by-second recording brief (who, what's on screen, the exact sentence, length) for the user to film on a phone.

---

## 7. Testing: change one thing, read the right layer

Test in this order, because each layer caps the next: **hook -> angle/message -> format (video / static / carousel) -> offer -> audience.**

- **One variable per test.** Two hooks on the same video, or the same hook on two formats. Never both.
- **Method:** Meta A/B test (Experiments) when you need a clean answer; several ads in one ad set when you want Meta to find a winner fast (it allocates unevenly, so it's a race, not a fair test).
- **Read the metric of the layer you changed:** a hook test is judged on hook rate and CTR, not on purchases after 300 impressions. Purchases judge the whole ad once it has enough volume.
- **Minimum before a verdict:** about 1,000-2,000 impressions per variant for hook/CTR decisions; about 2-3x target CPA spent per variant for conversion decisions. Less than that, call it a lead, not a winner.
- Write every test in the change log: hypothesis, variable, dates, result, decision.

| Layer | Metric | Healthy (rough, varies by market) | If low |
|---|---|---|---|
| Hook | 3s views / impressions | 25-35%+ | New first 1-2 seconds |
| Hold | ThruPlay / 3s views | 15-30%+ | Tighten the middle, pay off the promise faster |
| Click | Link CTR | 1%+ (feed), varies by placement | Clearer CTA, stronger reason to click now |
| Landing | AddToCart / landing views | 5-15% | Page work (offer, proof, clarity) |
| Checkout | InitiateCheckout / AddToCart | 20-40% | Checkout page, form friction, price shock |
| Payment | Purchase / InitiateCheckout | 40-70% | Payment methods, errors, trust |

---

## 8. Decisions: keep, kill, iterate, scale, shift

| Situation | Decision |
|---|---|
| Ad spent ~1x break-even CPA with zero checkouts, and its hook rate / CTR are the account's worst | **Kill** it, replace with a new hook |
| Ad has good hook/CTR but no conversions | **Iterate** downstream: the page, the CTA, the destination, not the ad |
| Ad set CPA under target for 3+ days, frequency OK | **Scale vertically** 20-30% every 2-3 days |
| Winner is capping (CPA rising as budget rises, frequency up) | **Scale horizontally**: same creative to a new audience (lookalike, broader), or new creatives in the same angle |
| One campaign's marginal CPA (last added budget) is clearly better than another's | **Shift** budget toward it in steps, keep the weaker running small if it feeds a later rung |
| Metrics noisy, under the minimum data | **Let it run.** Changing now resets learning and teaches nothing |
| Frequency 3+ in prospecting / CTR decaying week over week | **Refresh creative** (fatigue) |
| A rung's audience is tiny and frequency explodes | Merge it with the next rung or move it to email |

Always compare against break-even and target CPA (ppc-operator-playbook.md), and against **real sales from the platform**, not only Meta's attribution (sales-platform-data.md).

---

## 9. Weekly rhythm

- **Daily (read-only report):** delivery, pixel health, spend vs results by campaign, new platform sign-ups/buyers, alerts.
- **Twice a week:** creative read (hook, hold, CTR per ad), kill/keep, queue the next test.
- **Weekly:** budget shifts between TOF/MOF/BOF by marginal CPA, audience sizes per rung (merge or split), customer list re-upload, new creative brief for the user to record, lookalike/seed refresh, written summary of what was learned.
