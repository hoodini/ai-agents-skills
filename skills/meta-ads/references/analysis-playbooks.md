# Analysis Playbooks

Read this when the user wants *analysis*, not just data. Each playbook is a recipe: what to query, how to interpret it, what to recommend. Don't just dump numbers - synthesize.

## Universal rule: always ground recommendations in the user's actual numbers

Generic advice is worthless. Don't say "consider refreshing your creative" - say "ad `Summer_Launch_v3` has frequency 4.2 and CTR fell 38% in the second half of last 28d while CPM rose 22%. Pause it; the duplicate `Summer_Launch_v4` is already taking over delivery." Pull names, IDs, and exact numbers from the script outputs.

## Playbook 1: Time-range performance report

**Trigger:** "How are my ads doing this week?", "Give me a 30-day report", "What's my ROAS lately?"

**Query:**
```bash
python scripts/fetch_insights.py --level campaign --date-preset last_30d
python scripts/fetch_insights.py --level account --date-preset last_30d
python scripts/fetch_insights.py --level account --date-preset last_30d --time-increment 1
```

**Interpret:**
- Account-level totals → overall health
- Campaign-level rows → where the money went, sorted by spend
- Daily time series → trend (climbing, steady, or declining)

**Recommend:**
- If ROAS dropped vs. last period → run `anomaly_detect.py` to localize
- If one campaign eats 80% of budget but has worse ROAS than others → suggest reallocating
- If CPM climbed steadily → audience saturation or auction competition; suggest creative refresh + audience expansion

**Output format:** A clean prose summary with 3-5 numbered insights. Append a small table with per-campaign spend / ROAS / CPA for quick scanning. Match the user's working language, but keep metric names in English (`CTR`, `CPA`, `ROAS`, `CPM`) so they cross-reference cleanly with Ads Manager.

## Playbook 2: Creative fatigue diagnosis

**Trigger:** "Is my ad fatigued?", "Why is CTR dropping?", "Should I refresh creative?"

**Query:**
```bash
python scripts/creative_fatigue.py --date-preset last_28d
```

**Interpret the script's output:**
- `fatigued_ads[]` is sorted by severity. Top of list = most urgent.
- A single flag (frequency only, or CTR decay only) is mild.
- Two flags (frequency + CTR decay) is real fatigue.
- Three flags (frequency + CTR decay + CPM rising) is severe - Meta is now actively penalizing delivery.

**Recommend per ad:**
- **Mild fatigue, low spend:** monitor; don't act
- **Real fatigue, ad still profitable:** duplicate the ad (`duplicate_ad.py --type ad`), then pause the original after the duplicate enters learning. This buys you a fresh learning phase without losing the working setup.
- **Severe fatigue:** pause immediately. Meta's penalty (rising CPM) means you're paying more for less. Replace with new creative, not a duplicate.
- **Whole audience saturated** (multiple ads in the same ad set all fatigued): the audience is the problem, not the creative. Expand targeting or move to a lookalike.

## Playbook 3: Audience / placement breakdown

**Trigger:** "Where are my ads working?", "Which platform performs best?", "Should I split my budget by placement?"

**Query:**
```bash
# Platform breakdown
python scripts/fetch_insights.py --level campaign --date-preset last_30d \
  --breakdowns publisher_platform

# Placement detail (where on each platform)
python scripts/fetch_insights.py --level campaign --date-preset last_30d \
  --breakdowns publisher_platform platform_position

# Demographic
python scripts/fetch_insights.py --level campaign --date-preset last_30d \
  --breakdowns age gender

# Geographic
python scripts/fetch_insights.py --level campaign --date-preset last_30d \
  --breakdowns country
```

**Interpret:**
- Compute CPA or ROAS per breakdown row. Don't just look at CTR - high CTR can hide bad conversion rates downstream.
- Identify cells with sufficient volume to trust (≥30 conversions, or ≥$50 spend - fewer than that and you're staring at noise).
- Compare CPA across cells. A 2x difference in CPA between Instagram Reels and Facebook Feed is meaningful; a 20% difference probably isn't.

**Recommend:**
- If one placement has CPA <50% of the worst → consider isolating it in a new campaign with full budget
- If a demographic segment massively outperforms → tighten targeting (but warn: Meta's algorithm is usually better at finding people than we are at telling it where to look)
- For CTWA campaigns: Instagram Stories often dominates because it's a low-friction tap-to-message UI. If FB Feed is winning instead, that's unusual and worth investigating

## Playbook 4: Conversion funnel analysis (with CTWA support)

**Trigger:** "Where are people dropping off?", "Why aren't my course ads converting?", "Are people clicking but not buying?"

**Query for standard web conversion funnel (landing page → purchase / sign-up):**
```bash
python scripts/fetch_insights.py --level campaign --date-preset last_30d \
  --fields spend impressions actions action_values cost_per_action_type
```

Then in the response, count action types:
- `link_click` - they clicked
- `landing_page_view` - Pixel confirms page loaded (drop here = slow page or misconfigured Pixel)
- `view_content` - they engaged with content
- `add_to_cart` / `initiate_checkout` - moved toward purchase (if e-commerce)
- `purchase` / `complete_registration` - converted

**Compute drop-off ratios:**
- LPV / link_clicks → site speed / pixel issues if low (<70%)
- view_content / LPV → page quality
- purchase / view_content → offer / pricing / trust

**For CTWA funnel:**
- `link_click` (or omit - Meta uses different signals) → `onsite_conversion.messaging_conversation_started_7d` → `onsite_conversion.messaging_first_reply` → eventual sale (tracked outside Meta)

**Recommend:**
- Drop-off between click and LPV → landing page issue (speed, Pixel firing, broken link)
- Drop-off between LPV and view_content → page doesn't deliver on the ad's promise
- Drop-off between view_content and purchase → offer/pricing problem, not an ad problem. The skill should say so directly: "Your ads are working. The conversion problem is on your landing page."

## Playbook 5: Anomaly response

**Trigger:** "Something's off", "My CPA spiked", "Why did spend drop?", "Did something break overnight?"

**Query:**
```bash
python scripts/anomaly_detect.py --window-days 7
```

For shorter horizons:
```bash
python scripts/anomaly_detect.py --window-days 3 --pct-threshold 0.20
```

**Interpret the output:**
The script returns a sorted list of campaigns where metrics moved significantly. Look at:
- `status` field: `stopped_spending`, `started_spending`, or `active_change`
- `anomalies` array: which metric moved and by how much

**Common patterns and what they mean:**

| Pattern | Likely cause | Action |
|---|---|---|
| Spend dropped, impressions dropped, CTR steady | Budget exhausted, daily cap hit, or campaign paused | Check status; check budget vs. spend |
| CPM spiked, CTR steady | Auction competition (often around holidays, sales events, elections) | Wait or raise bid; not a creative issue |
| CTR dropped, CPM steady | Creative fatigue or audience burnout | Run fatigue playbook |
| Spend up, impressions up, ROAS down | Algorithm explored new audiences, found worse converters | Consider tightening targeting if it persists >5 days |
| Conversions dropped to zero, everything else normal | Pixel broken or website broken | Check Pixel via Events Manager **immediately** |
| Spend zero on a previously active campaign | Account issue (billing, policy, ad disapproval) | Check account status and ad-level disapproval reasons |

**Recommend cautiously:** anomalies have lots of false positives. Don't pause a campaign because one day looked weird - wait 2-3 days unless the issue is clearly catastrophic (like zero conversions for a converting campaign).

## Playbook 6: Click-to-WhatsApp specific analysis

**Trigger:** "How are my CTWA ads doing?", "Cost per WhatsApp conversation?", "Should I run more CTWA?"

**Why this needs its own playbook:** CTWA campaigns optimize for `messaging_conversations_started`, not website conversions. The funnel is different (ad → tap → WhatsApp opens → first business message → reply → eventual sale). Analyzing them with web-conversion frameworks gives garbage answers.

**Query:**
```bash
python scripts/fetch_insights.py --level adset --date-preset last_30d \
  --fields spend impressions actions cost_per_action_type \
  --filtering '[{"field":"adset.optimization_goal","operator":"EQUAL","value":"CONVERSATIONS"}]'
```

**Key metrics:**
- Cost per conversation started (`cost_per_action_type` where action_type = `onsite_conversion.messaging_conversation_started_7d`)
- Reply rate: `messaging_first_reply` / `messaging_conversation_started_7d` - high reply rate means real intent; low means accidental taps or low-quality leads
- Cost per reply (cost per conversation × inverse reply rate) - the "real" cost of a usable lead

**Recommend:**
- Compare cost per conversation across creatives and audiences - wide spread (>2x) means easy optimization
- Low reply rate (<40%) suggests the ad creative oversells; refine the hook
- If reply rate is good but no sales materialize, the bottleneck is your WhatsApp follow-up sequence, not the ads

## Cross-playbook: when to escalate

If the user wants ongoing monitoring (daily anomaly checks, weekly reports without asking), tell them this skill is on-demand only - scheduled runs belong in a cron job, a scheduled-tasks integration, or whatever automation layer the user already has. Don't try to fake persistence inside the skill.

If a third party (an agency client, a different team's account) wants this type of analysis, tell the user this skill assumes single-tenant credentials and the multi-tenant version is a different build. Don't run other people's analyses with personal credentials - each owner should set up their own app and token.
