# 08 — Series Consistency: Cohesion + Recurring Characters

When the deliverable is a SET (contest entry, campaign, photo-essay), two problems appear that a single image never has: the set must read as ONE author (cohesion), and any recurring subject must stay the SAME subject (character consistency). Plus the hard rule that governs all output.

## 0. The full-prompt hard rule (non-negotiable)
Every prompt is 100% complete and copy-paste-ready. NEVER "the previous prompt plus…", "same as above but…", "[insert]", "(keep the rest)", or any abbreviation. If two prompts are 90% identical, write both out in full — repetition is correct; a reference-back is a defect. The user copies one self-contained block per image into the tool; a shortcut breaks the workflow.

## 1. Series cohesion — make 10 images read as one body of work
Lock a small visual DNA and weave it **verbatim into EVERY prompt** (the "Style Lock"):
- ONE film stock / capture signature (e.g. **CineStill 800T** for a night series — its warm halation around bright lights unifies the set and is on-theme).
- ONE grain / texture treatment.
- ONE lighting principle (e.g. a single motivated warm source against a cool night).
- ONE color logic / grade (teal-orange, deep protected blacks, muted editorial).
- ONE aspect-ratio family (vary within it for rhythm — 3:2 / 4:5 / 16:9 — not random).

**Cohesion lives in the Style Lock; range lives in the *treatment*** (lens, distance, time, energy). That separation is how a single-theme set scores Range without falling apart.

## 2. Character consistency — keep the SAME animal across images
Ranked by reliability:
1. **Reference image (strongest, tool-native).** Generate one "hero reference" of the character first, then feed it into every generation. Reve references are first-class and lossless across edits; Nano Banana takes up to 14 refs; Midjourney `--cref`; SD IP-Adapter.
2. **Reve layout-node reuse.** Reve is layout-first — build the character once and reuse/duplicate that node across compositions, editing pose/scene around it. Surest path within one tool.
3. **Verbatim Character ID block.** A fixed, fully-written description with 2–3 UNIQUE identifiers (a notched ear, a specific scar, exact eye color) pasted identically into every prompt. Unique marks stop "generic cheetah" drift. Most portable across tools; aligns with the full-prompt rule.
4. **Seed lock** (SD/MJ) for stylistic stability; **LoRA / fine-tune** (SD) for bulletproof consistency if you have training images.

Best practice: **reference image (1) + verbatim ID block (3)** together.

## 3. Worked series — "Through Their Eyes: Israel at War" (10 images)
Unified theme: life in Israel during war told through animals' helplessness — reflecting what people feel. **Honest Range bet:** a single-theme set risks the Range criterion; we win it by maximizing **treatment range** (discipline, lens, distance, time, energy) while the Style Lock holds cohesion. Recurring protagonists (HOPE, MARCUS) tie it to Yuval's Midbarium "Born to Run" characters.

### The Style Lock (paste into every prompt, verbatim)
> shot on CineStill 800T 35mm film, subtle film grain and faint halation glow around bright lights; a single motivated warm light source (Iron Dome airburst / emergency strobe / bare bulb) against a cool desaturated night; warm-cool teal-orange separation, deep protected blacks, muted editorial photojournalism grade; natural fur and skin texture with real micro-detail, one sharp catchlight per eye, no plastic sheen.

### Character ID blocks (paste verbatim wherever they appear)
> **HOPE** — an adult female cheetah, lean and athletic, tawny-gold coat with dense round black spots, the signature black tear-stripe lines running from the inner corners of her amber eyes down to her mouth, a small notch in the upper edge of her right ear, a faint old scar on her left foreleg.
>
> **MARCUS** — a mature male white lion, pale cream-white coat, heavy blond-white mane with faint amber tips, pale gold-green eyes, a thin old scar across the bridge of his broad muzzle.

### The ten (each anchored to a REAL, researched Israeli home-front pain — see `references/10`)
All 4:5 magazine-cover format; masthead "THROUGH THEIR EYES".
| # | Headline | Animal | The real pain it illustrates | Treatment | Risk |
|---|---|---|---|---|---|
| 1 | THE WITNESSES | Bengal tigers (one turns) | helpless watching the interception decide your fate | telephoto night silhouette, war-in-eye | low |
| 2 | THE WAKING | lioness over sleeping cubs | the dilemma: wake the just-asleep kids for the siren, or gamble? | intimate den interior | cub faces (closed eyes) |
| 3 | DON'T WAIT FOR ME | old greying lion | the elderly/disabled who can't reach shelter in time | environmental, aged subject | aged face large |
| 4 | A TIN OF SARDINES | mixed animals crammed | the public shelter — no privacy, no toilet, strangers at 3am | cramped group interior | multiple faces |
| 5 | NOWHERE TO GO | doe + two fawns at a bare wall | 56% of homes have no safe room | exposed-family medium | small faces |
| 6 | TOO LATE | HOPE + cub | the 15–90 second window to reach shelter | panning action blur | paws, open mouth |
| 7 | THE SHIELD | MARCUS over cubs, struck shelter | hit despite doing everything right; the body as last shelter | dust/aftermath protective | cubs, dust restraint |
| 8 | THE WATCH | exhausted mother, cubs asleep | bone-deep exhaustion; the parent who performs calm, never sleeps | low-light intimate | weary face large |
| 9 | THE SOUND | a hare frozen mid-flinch | the siren as trauma trigger; hypervigilance, phantom sirens | prey-freeze, ears straining | face/ears |
| 10 | DO YOU SEE ME? | street dog, direct gaze | the universal plea; pets paralyzed by terror | extreme close portrait | symmetry |

Emotional arc: helpless watching → the waking → the left-behind → the crush → the exposed → the race → the failed shelter → the sleepless watch → the trigger → the plea. Treatment still spreads across silhouette / interior / environmental / group / action / portrait for the Range criterion. **Benched alternates** (all pain-valid, swap in freely): baboon "caught in the open, cover your head"; lone oryx "one life beneath a war"; sunbird "her wings the only roof"; gazelle dawn "the morning after"; stork flock "exodus / displacement".

Full standalone prompts are produced from this bible using the Style Lock + Character ID blocks + the 8-block stack; each must pass `references/07` at 100% zoom before it joins the set.

## 4. Submit-set checklist
- [ ] All 10 carry the Style Lock verbatim (cohesion holds).
- [ ] Recurring characters use the same reference image + the verbatim ID block.
- [ ] Treatment ranges across discipline/lens/distance/time/energy (Range hedge).
- [ ] Each image individually passes the `references/07` forensic pass at 100%.
- [ ] No two images are near-duplicates; each earns its slot.
- [ ] Every prompt handed over is complete — zero shortcuts.
