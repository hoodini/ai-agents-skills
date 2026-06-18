# 09 — Magazine / Editorial Cover Treatment

When a series should read as an editorial body of work (masthead + short headline captions), add a TYPE LAYER on top of the photography. This showcases legible-text craft (a judge-invited discipline — "graphic design") but courts the **double-penalized "typography artifact."** So the workflow decides everything.

## The cardinal rule: composite the type in post
Generate the clean photographic image first (reserve a text-safe negative-space zone), then set **real vector type** in a design tool — for Yuval, his **instagram-cover-studio** (`~/instagram-cover-studio`, Anton-based) or Figma/Photoshop. Real text = pixel-perfect kerning, zero garbled glyphs, full art direction, and it sidesteps the contest's most-penalized artifact entirely. This is exactly what Yuval's own `BRANDING_SYSTEM.md` prescribes: *"Generate one strong vertical image → use the app to place typography → export."* Only let the model render text to deliberately demonstrate its text engine, and then only a SHORT ALL-CAPS headline per `03`, inspected at 100%.

## Don't infringe (the contest requires original, non-infringing work)
Do NOT mimic a real magazine's trademarked identity — National Geographic's yellow border, TIME's red frame, any real masthead/logo. Borrow the *language* of covers (masthead, kicker, headline, dateline); invent an ORIGINAL wordmark.

## Caption craft — extreme brevity that explains the frame
- **Kicker** (small overline): one short line that gives the emotional read — 4–7 words.
- **Headline** (the big type): 1–4 words, ALL CAPS, condensed — *names* the image.
- Optional **dateline/footer**: a small consistent line for editorial realism (original, e.g. "ISRAEL — 2026").
Headline *names* the frame; kicker makes you *feel* it. Both must read at thumbnail/grid size.

## The design-system lock (cohesion across the set)
- **Type:** Anton (masthead + headline, condensed all-caps), Inter/Assistant for the small dateline. Same family every cover.
- **Palette / text colour:** never default to flat all-white (reads generic). Specify the colours: masthead in clean white/bone, the recurring tagline (or a key word) in **alarm RED** — it pops like a real magazine AND ties to the "Red Alert" (Tzeva Adom) siren. The single red accent is the grid's owned signature. Do NOT use a high-dopamine neon (the YUV.AI Reels look — tonally wrong here).
- **Placement grid (locked, EVERY page):** top — a masthead lockup: the title **THROUGH THEIR EYES** with the recurring tagline **LIFE IN ISRAEL AT WAR** beneath it; lower third — the per-image headline on a subtle dark gradient scrim; bottom-right corner — a small **YUVAL AVIDANI** credit. Fixed every page; only the photo and the headline change.
- **The recurring tagline IS the concept-explainer.** Without it a viewer sees a dramatic animal but may miss that this is *Israel-at-war seen through the animal's eyes*. Keep it SHORT so it never overflows; masthead + tagline + the animal in frame together make the concept legible in one glance. The brief is minimal-text: short, sharp, piercing — never wordy.
- **Signature / anti-theft:** the YUVAL AVIDANI credit goes on every page (provenance + theft-deterrent). Keep it ALL-CAPS and short for reliable in-model rendering; it is the single most likely string to need a re-roll.
- **Aspect — treat the set as ONE MAGAZINE FEATURE:** each image is a PAGE in one photo-essay, so a consistent **4:5 portrait** is correct and premium (cohesive grid, the lockup reads cleanly). Cinematic power comes from light, grade and composition — not from a wide ratio. Option: render the 1–2 most epic establishing frames as 16:9 "opening spreads" if you want a wide cinematic beat, but keep the spine 4:5 for cohesion.
- **Photo is sacred:** keep all type in the reserved negative space (clear top band, lower-third scrim, corner) — never occlude the animal. The photograph carries the craft score.

## Worked captions — the LOCKED text system (the animal-war feature)
Every page carries the SAME lockup, only the photo + headline change:
- **Masthead title (top):** `THROUGH THEIR EYES`
- **Recurring tagline (beneath, smaller — the concept-explainer):** `LIFE IN ISRAEL AT WAR`
- **Headline (lower third, large):** the per-image word(s) below
- **Credit (bottom-right, small):** `YUVAL AVIDANI`
| # | Image | KICKER | HEADLINE |
|---|---|---|---|
| 1 | tigers watching the interception | THE SKY DECIDES WHO LIVES | THE WITNESSES |
| 2 | mother over just-asleep cubs | WAKE THEM, OR LET THEM SLEEP | THE WAKING |
| 3 | old lion left behind | TOO SLOW TO REACH SHELTER | DON'T WAIT FOR ME |
| 4 | animals crammed in a shelter | NINETEEN STRANGERS, ONE ROOM | A TIN OF SARDINES |
| 5 | doe + fawns at a bare wall | NO SAFE ROOM, NOWHERE TO RUN | NOWHERE TO GO |
| 6 | Hope + cub racing the clock | FIFTEEN SECONDS | TOO LATE |
| 7 | Marcus over cubs, struck shelter | THEY DID EVERYTHING RIGHT | THE SHIELD |
| 8 | exhausted parent on watch | EVERYONE ASLEEP BUT ME | THE WATCH |
| 9 | a hare frozen at the siren | A WORLD FALLING APART | THE SOUND |
| 10 | street dog, direct gaze | WE FEEL IT TOO | DO YOU SEE ME? |

## In-model recipe (text rendered by the generator — Reve-only, no external editing)
When external tools are off the table, render the type inside the image. Reve runs a dedicated typography pass and is best-in-class at short legible text, so in-model covers are viable IF you respect the limits:
- **The magazine lockup = up to FOUR short strings:** masthead title + tagline (one top block), the headline (lower third), the small YUVAL AVIDANI credit (corner). This exceeds the safe minimum, so discipline matters MORE, not less.
- **Quote exact strings, keep them short, prefer ALL-CAPS.** Describe the font by style only: `bold condensed uppercase sans-serif`.
- **Reserve clean zones:** uncluttered top band for the masthead lockup; a subtle dark gradient scrim under the lower-third headline; a clean dark corner for the credit.
- **The small credit and the tagline are the highest-risk strings** — keep the credit `YUVAL AVIDANI` in caps. Fallback if text overflows or fights the image: drop the tagline first, then the credit, keeping masthead + headline.
- **No post-fix safety net (Reve-only):** render at 4K and inspect EVERY string at 100%. If any glyph is wrong, RE-ROLL (Reve is stochastic on text) or edit that text node. Text is the double-penalized artifact — never ship a garbled page.

## Prepping the photo prompt for type
Each series prompt reserves a clear top zone and a darker lower third as negative space, then names the masthead and headline as quoted ALL-CAPS strings inside the prompt.
