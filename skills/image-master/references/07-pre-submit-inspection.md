# 07 — The Forensic Pre-Submit Inspection

Run twice: **PRE-FLIGHT** on the prompt (predict the likely artifact, pre-empt it in words) and **POST-FLIGHT** on the output (the judges will zoom in — so do you). The contest explicitly penalizes the 13 artifacts below; this checklist is built to catch each.

## PRE-FLIGHT (on the prompt, before generating)
- [ ] **Blacklist swept?** No `8k / ultra / hyperreal / masterpiece / octane / flawless / smooth / beautiful / glossy`.
- [ ] **One light only?** Direction + quality + resulting shadow direction named.
- [ ] **Anti-plastic present?** Pores / vellus / subsurface / texture-revealing light / film grain for any skin or fur.
- [ ] **Hands handled?** Hidden, posed simply, cropped, or on one solid object — never a complex free hand unless it's the hero (then plan to inpaint).
- [ ] **Faces sized?** Hero faces large in frame; gaze + catchlights specified; `slight asymmetry`; ≤2 faces or expect inpaint.
- [ ] **Text safe?** Quoted + short + ALL-CAPS for the hero string; background text left vague; Hebrew/exact text routed to post.
- [ ] **Negatives converted?** On Reve/GPT-image/Nano Banana, every "no X" rewritten as a positive.
- [ ] **Camera real?** Body + lens + aperture + shutter/ISO named.
- [ ] **Depth staged?** Fore/mid/background + atmospheric haze.
- [ ] **One impact lever locked?** A color recipe AND a composition/drama device.

## POST-FLIGHT (on the generated image — zoom to 100%)
Inspect in this order; the first failure usually hides the others.

| # | Penalized artifact | Where to look | Pass test |
|---|---|---|---|
| 1 | **Hands rendering** | every visible hand/paw | exactly 5 fingers, natural joints, no fusion/extra; thumbs correct |
| 2 | **Object & hand** | hand–object contact points | fingers wrap correctly; object geometry consistent, not melting into the hand |
| 3 | **Anatomical error** | limbs, joints, count, proportion | no extra/missing/floating limbs; natural posture; symmetric pairs match |
| 4 | **Facial rendering** | eyes, teeth, ears, symmetry | eyes aligned + focused, both catchlights match the key; no melted ear/teeth; *slight* (not dead) symmetry |
| 5 | **Artificial / plastic skin** | cheeks, forehead, nose | visible pores, real tonal variation; NOT waxy/airbrushed/uniform |
| 6 | **Unnatural material** | fabric, metal, fur, water, foliage | weave/grain/strands/wear visible; light behaves correctly on the surface |
| 7 | **Rendering issue (light/reflection)** | shadows, mirrors, glass, wet ground, eyes | all shadows agree on ONE light direction; reflections contain the actual scene |
| 8 | **Typography** | every glyph, foreground and background | hero text spelled right, clean kerning; no invented characters in background signage |
| 9 | **Image quality / artifacts** | edges, gradients, repeats, smears | no oversharpen halos, banding, duplicated patterns, smudge zones, warped backgrounds |
| 10 | **Composition sanity** | horizon, perspective, scale | horizon level; consistent vanishing point; subject scale plausible vs surroundings |
| 11 | **Species consistency** | every animal, esp. cubs/young/groups | each animal is unmistakably its correct species with the right markings (lion cubs ≠ cheetahs); no generic spotted "big-cat cub" |
| 12 | **Reflection accuracy** | eyes, wet ground, glass, water | every reflection contains the ACTUAL scene/light in the correct position and direction; catchlights match the key light |

## The PRECISION LOCK (bake into every prompt's tail)
Append this to any prompt, setting the species line per image:
> Every animal anatomically correct and true to its EXACT species and markings — **[species note, e.g. "lion cubs are tawny with rounded faces and only faint juvenile rosettes, never cheetah spots or tear-stripes"]**. Correct limb count, each paw/foot planted and clearly attached, five toes with natural pads and claws, no fused, extra or floating limbs. A single dominant light source with all shadows falling consistently away from it — no contradictory shadow directions. Accurate reflections: light sources and the scene mirror correctly in eyes, wet surfaces and glass, matching their real position. True materials, correct perspective and scale. Photoreal down to whiskers, individual fur/hair direction, pores and catchlights. No anatomical, material, typography or perspective errors.

## Triage when something fails
1. **One local element (a hand, a sign, an eye)** → on Reve, edit that node / inpaint that mask only (denoise 0.35–0.5) — do NOT re-roll the whole image and lose a good composition.
2. **Systemic (plastic skin everywhere, wrong light all over)** → it's a prompt problem; fix the words (add texture/one-light), regenerate.
3. **Text wrong** → fix BEFORE upscaling; if exact/brand/Hebrew, blank it and composite in post.
4. **Still failing after 2 inpaints** → change the pose/crop to hide the failure zone (back-turned, hands away, face larger) rather than fighting the model.

## The submit gate
An image ships only when: it passes all 10 post-flight rows at 100% zoom, it pulls at least one deliberate impact lever, and — for a SET — it adds *range* the other images don't already cover. If it only "looks fine at thumbnail size," it is not done; the judges zoom in.
