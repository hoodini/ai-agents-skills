# Proactive monitoring: a daily read-only check

Users who just launched a campaign want someone watching it. Set up a scheduled run (a Claude scheduled task, a cron job, or any scheduler the host offers) that checks the campaign every morning and reports in the user's language. Keep it **read-only**: it recommends, and every change goes through a normal confirmed write in a conversation.

## Before scheduling

1. **Credentials in a stable, private place** (e.g. `~/.config/<project>-ads/.env`, mode 600), not inside a temporary session folder that may be deleted.
2. **Run it once by hand** ("Run now") so the scheduler stores the tool permissions; otherwise the first scheduled run can hang waiting for an approval no one sees, and later runs pile up behind it.
3. Long-lived user tokens expire after ~60 days. Put the expiry in the prompt so the report warns a week ahead.

## The prompt template

A scheduled run starts with no memory, so the prompt carries everything. Fill in the brackets:

```
You check the Meta ads campaign for [product] and report to [name] in [language]. READ-ONLY:
never pause, activate, change budgets, create or delete anything; only recommend. Every change
must say: "reply 'approve' in a conversation and I'll do it".

Context:
- Product [name], price [P], break-even CPA [B], target CPA [T].
- Ad account [act_...], pixel [id], installed on [landing URL] and [checkout URL].
- Funnel events: [page] sends [events]; [checkout platform] sends [events].
- Campaign [id], objective, optimization event, budget, launch date [date].
- Change log: [date: what changed and why]. Count the learning phase from the last structural change.
- Known caveats: [e.g. ads are copies of IG posts; comment automation may not answer ad comments].

Steps:
1. python scripts/funnel_report.py --campaign-id [id] --breakdowns placement,age
   (from the skill folder, with the .env loaded). If it fails, report the error and stop.
2. python scripts/check_pixel.py --pixel-id [id] --ad-account-id [act_] [landing] [checkout]
   Any flag other than OK is the top alert.
3. If the sales platform is connected (e.g. Schooler MCP, see references/sales-platform-data.md):
   list_course_students for [course id]. Report new enrollments since yesterday, the current
   "interested" (signed up, didn't pay) names, paid-but-not-started count, and enrollments since
   launch next to Meta's attributed purchases. Counts in the report; names only for the people to contact.
4. Analyse with references/ppc-operator-playbook.md: learning phase (don't-touch days),
   decision table vs [B] and [T], stage leaks via rates_pct, placement/age anomalies,
   frequency > 3, remarketing readiness (references/funnel-remarketing.md).
5. Report: one-line status; money (spend, purchases, cost per purchase, revenue, ROAS);
   funnel by stage; per-ad table; one or two recommended actions with why.
6. Save to [project]/ads/reports/YYYY-MM-DD.md and send a one-line notification if available.
```

## What a good daily report looks like

- One line first: "learning, don't touch", "working, consider scaling Friday", or "broken: X".
- Numbers against break-even, never raw metrics alone.
- No more than two actions. Most days in the first week the right action is "nothing", and the report should say why.
