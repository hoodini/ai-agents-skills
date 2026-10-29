# Ground truth from the sales platform (Schooler MCP and similar)

Meta reports what it can attribute to an ad. The sales platform knows who actually paid. Always reconcile the two before judging a campaign, and use the platform's data to find the cheapest sales in the business: people who already know the seller.

This file uses **Schooler** (Israeli course platform, `my.schooler.biz`) as the worked example because it ships an official MCP server. The same logic applies to any checkout/LMS platform with an API or export (Teachable, Thinkific, Kajabi, Shopify, WooCommerce...).

## Connect (Claude Code)

```bash
claude mcp add --transport http --scope user schooler https://my.schooler.biz/mcp
```

Then the user authenticates once: run `claude`, type `/mcp`, pick `schooler`, **Authenticate**, log in to Schooler in the browser and approve. The server uses OAuth 2.1 with dynamic client registration and two scopes, `mcp:read` and `mcp:write`. In the Claude apps it can also be added as a custom connector with the same URL. `claude mcp get schooler` shows "Failed to connect" until the login is done; that's expected.

## What the tools give you

| Read (safe) | Purpose |
|---|---|
| `list_courses` | Standalone courses: id, name, **price**, type (paid / registration / free), status |
| `list_schools` | Multi-course schools and the courses inside them |
| `list_course_students(course_id)` | `students` = **enrolled** (for a paid course: paid or manually granted), with join date, last login and **lesson progress**; plus `interested_students` = **signed up but did not pay**. Report both |
| `list_school_students(school_id, course_id?)` | Same at school level |
| `search_student(email / phone / name / id)` | Everything one person has |
| `list_course_lessons`, `list_lesson_files` | Course structure (spot placeholder or "coming soon" lessons that hurt conversion) |

Write tools exist (`enroll_student_in_school_course`, `set_student_course_status`, `send_student_login_link`, `reset_student_password`, `create_lesson` / `update_lesson` / `delete_lesson`, ...). They change a real business: same rules as Meta writes (write-actions.md), one explicit confirmation per action. Reporting and segmentation never need them.

## Large results

A course with a few hundred students returns more than the conversation can hold; the client saves it to a file. Never page through personal data in chat. Analyse the file with a script and show the user **counts and names only when needed**:

```bash
python scripts/segment_students.py --out <project>/private/segments \
  --course "Course A=<saved_result_a.json>" --course "Course B=<saved_result_b.json>"
```

## The six questions this answers

1. **What really sold?** Count enrollments by join date around the campaign start. Compare with Meta's attributed purchases. The gap is sales from email, organic, word of mouth, other devices, or attribution Meta missed. Don't credit or blame the ads for sales that happened before launch, and don't call a campaign dead while the platform shows new paying students.
2. **Who signed up and didn't pay?** (`interested_students`) The hottest people in the business: they stopped at the payment step. A same-day personal message closes some of them.
3. **Who bought A but not B?** (cross-sell) Past buyers convert far better than cold traffic, at zero media cost. A cheaper course is an easy yes for buyers of an expensive one; an expensive course is the natural next step for buyers of a cheap one.
4. **Who paid and never started?** (0% progress) Refund and churn risk, and they never become testimonials or repeat buyers. Send an activation email ("start with lesson 1, it's 3 minutes").
5. **Is a course's sales curve flattening?** Enrollments by month show when a course needs a relaunch, new creative, or a new offer.
6. **Is the checkout page hurting?** `list_course_lessons` shows placeholder lessons and "coming soon" items that make a course look unfinished on the sales page.

## Turning segments into campaigns

The platform is the brain (who is where); the mailing tool sends. Typical pairing: Schooler + Rav Messer (רב מסר); the same applies to any ESP.

- **Two lists per course in the mailing tool,** filled automatically by the platform's integration: "signed up to X" on registration, "paid for X" on purchase. Check the integration is really connected: an existing "paid" list with 0 subscribers after known sales means it never was.
- **Signed up but didn't pay = "signed up" minus "paid".** A payer is in both lists. Either exclude the "paid" list at send time, or, better, set a rule on the "paid" list that **removes the subscriber from the "signed up" list** when they join; then "signed up" only ever holds non-payers and automations can run on it directly. Such rules apply to new joins only: clean up existing double members once.
- **Cross-sell sends need no import** when per-course "paid" lists exist: send to "paid for A", exclude "paid for B". Import a CSV from `segment_students.py` only for segments the mailing tool can't express (e.g. platform-side "interested" people from before the integration existed).
- **Automated reminder sequence** on "signed up to X": 1 hour (something got stuck? here's the link), 1 day (what you'll have built), 3 days (is it for me? + last reminder). It must stop when the person pays (the removal rule above, or a "stop if joins list" condition).
- **Bulk mail goes through the mailing tool, never a personal inbox:** deliverability, and anti-spam law (in Israel and most places) requires consent and an unsubscribe link, which the ESP adds. Personal 1:1 follow-ups to the handful of "interested" people can be drafted in the user's own mail for them to send.
- **Messaging apps:** WhatsApp/Instagram automation is bound by the platform's messaging windows (see ppc-operator-playbook.md). Personal messages from the user's own phone are fine.

## Daily report additions

Add to the morning check (monitoring.md): new enrollments yesterday per course, the current "interested" list (names, so the user can reach them that day), paid-but-not-started count, and enrollments since launch next to Meta's attributed purchases.

## Privacy

Student names, emails and phones are personal data:
- Keep exports and CSVs in a git-ignored private folder on the user's machine. Never commit, upload or paste them into shared artifacts.
- In reports, prefer counts. Show names only where the user must act on them (e.g. the few "interested" people to contact).
- Never send anyone's data to a third party the user didn't choose.
