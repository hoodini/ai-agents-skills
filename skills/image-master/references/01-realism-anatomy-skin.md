# 01 — Anatomy, Hands, Faces, Skin, Bodies

The governing fact: diffusion models have **no 3D model of the world** — they predict 2D pixel statistics and default to the **mean of their training data** (retouched stock). Two corollaries drive every tactic:
1. Plastic skin and dead symmetry are not bugs — they are the *average*. Prompt actively *away* from it toward specific, messy, photographic reality.
2. **Negation is unreliable.** "No extra fingers" still activates *fingers*. Newer transformer models (GPT-image, Reve, Nano Banana) largely ignore negatives. **Describe the desired end state, don't forbid the failure.**

## 1. HANDS
Why they break: 27 bones, 34 muscles, usually small/blurry/occluded/foreshortened in training — the model can't reason about hidden geometry, so it guesses finger count and joint direction per pixel.

**Positive vocabulary (front-load — early tokens carry more weight):**
- `five fingers, fully articulated` · `naturally posed hand, accurate finger proportions` · `relaxed hand, fingers gently curved`
- Specify angle/pose/texture: `hand viewed from the side`, `open palm`, `calloused / smooth skin`
- Specificity beats vagueness: `fingers wrapped naturally around the handle` ≫ `holding a cup`

**Posing / hiding tricks (the single most effective lever):**
- `hands relaxed at sides` · `hands in pockets` · `hands clasped behind back`
- Hands resting on a surface, not occluded by other objects
- Holding one simple solid object (book, mug) — gives the model geometry to anchor to
- Crop the frame above the wrists when hands aren't the subject

**Negative terms (SD/SDXL/Flux/Leonardo only, weighted):**
`(bad hands, malformed hands, wrong number of fingers:1.4)`, `(fused/merged/webbed fingers:1.3)`, `(extra fingers, six fingers, four fingers:1.4)`, `missing thumbs`, `deformed hands`

**Strategy:** batch 4–8 and pick the best hand (variance is high); square 1:1 produces fewer body distortions in Midjourney. **Most reliable fix of all = inpaint just the hand** → `perfectly formed human hand, five fingers, realistic texture` at denoise 0.35–0.5; for SD, ControlNet OpenPose-Hand / MediaPipe feeds a literal skeleton.

## 2. FACES
Why they break: same averaging → over-symmetry; plus the "two-people/crowd-faces" failure where the model duplicates or melts faces it can't resolve at small scale (eyes/teeth/ears are high-frequency detail it interpolates badly).

**Positive vocabulary (toward humanity, away from sterile perfection):**
- `natural skin texture, freckles, slight facial asymmetry` · `subtle smile lines, authentic expression, unretouched`
- Eyes/gaze (be explicit — vagueness → dead/crossed eyes): `looking directly at camera` / `gazing off to the left`, `clear focused eyes`, `natural catchlights in the eyes`, `moist reflective eyes`
- Teeth: prefer `soft closed-mouth smile`; if open, `natural teeth, slight imperfection`
- Symmetry: explicitly request `slight natural asymmetry` — perfect symmetry is the uncanny tell

**Negative (SD/Flux):** `(deformed/distorted face:1.3)`, `(dead eyes, lifeless eyes, doll eyes:1.3)`, `crossed eyes`, `(bad/crooked teeth:1.2)`, `creepy smile`, `melted ears`, `cloned face`, `two faces`

**Portrait vs distance:** generate faces **large in frame** (head-and-shoulders) so the model allocates pixels. Distant faces and crowds are where eyes/teeth/ears melt — if a face must be distant, expect to inpaint it.

## 3. SKIN — the #1 realism tell
Why "plastic skin" happens: the model treats pores, fine lines, uneven tone, and subsurface scattering as noise/defects and smooths them to an airbrushed average; upscalers compound it.

**Words that CAUSE plastic skin — AVOID:**
`beautiful · flawless · perfect · smooth · airbrushed · glossy · glowing · radiant · porcelain · silky · model-like · glamour`

**Words that DEFEAT it — drop straight in:**
- Texture: `visible skin pores`, `open pores on nose and forehead`, `fine lines`, `vellus hair (peach fuzz)`, `subtle sebum / natural skin oil`, `skin micro-texture`, `uneven skin tone`, `subtle blemishes`, `slight redness around the nose`, `realistic subsurface scattering`
- Zone realism: `forehead skin different from cheek skin` (varying pore density reads as real)
- Texture-revealing light (critical — flat light hides pores): `directional window light raking across the face`, `hard side light`, `soft rim light`, `golden hour`, `single key at 45°`

**Camera / film vocabulary (signals "photo," not "render"):**
- Bodies/lenses: `Canon EOS R5, 85mm f/1.8` · `Sony A7 IV, 50mm f/1.4` · `Hasselblad X2D` · `Leica`
- Film stock: `Kodak Portra 400` (warm, fine grain, loved for skin), `CineStill 800T`, `Ilford HP5`, `Fujifilm Superia`
- Grain/ISO: `subtle film grain`, `ISO 400`, `analog photograph`, `35mm`

**Negative (SD/Flux):** `(plastic skin, waxy skin, smooth skin:1.2)`, `(poreless skin, no skin texture:1.3)`, `airbrushed`, `porcelain skin`, `3D render`, `CGI`

**Resolution:** you cannot get real pores at 512×512 — generate larger or upscale at denoise 0.35–0.45 so the model hallucinates true skin detail without changing structure.

## 4. BODIES / LIMBS
Why they break: no 3D body model → extra/missing limbs, fused joints, impossible poses, wrong proportions, especially in complex/contorted poses.
- Describe the pose explicitly and **simply**: `standing relaxed, arms at sides, weight on one leg` ≫ undefined dynamic pose
- `anatomically correct proportions`, `natural posture`
- **Cropping is the cheapest fix:** half-body or portrait framing removes feet/legs (a failure zone). Avoid extreme foreshortening.
- **Negative (SD/Flux):** `(bad/wrong anatomy:1.3)`, `(extra/missing/floating limbs:1.4)`, `fused joints`, `disconnected limbs`, `mutated`, `contorted pose`, `disproportionate body`

## 5. ANIMALS (wildlife realism)
- **Backs-turned, side-profile, and head-down poses** dodge facial-symmetry risk while often increasing drama — use deliberately.
- Fur: `individual backlit hair strands, directional anisotropic sheen, matted wet clumps near the nose/paws, dust caught in the coat`.
- Eyes: one sharp catchlight matching the key light; `wet reflective eye, sharp focus on the near eye`.
- **Never pose a raised, "hovering", or splayed paw/hand as a gesture** — it reads as a human wave and renders as a toy mitten with fused pads and wrong claws (proven in testing). Keep paws natural: planted on the ground, tucked under the body, or laid flat over the young. Convey a "dilemma/reaching" beat through the FACE and head-turn, not a lifted paw.
- **Match biology to the role:** a mother lion is a LIONESS — smooth tan head, **NO mane**. Always state "a lioness, smooth head, no mane" for a female; a maned "mother lion" is an instant anatomical-error flag the judges will catch. (Same logic for any species — never give a female a male's features, or a juvenile an adult's.)
- **Trace every limb in a pile:** a mother + cubs huddle is where extra/disconnected paws appear. Keep the group simple (one or two clearly-posed young), every paw attached to a visible body.
- **Lock the EXACT species + its markings for EVERY animal — especially cubs and groups.** The model defaults to a generic spotted "big-cat cub," so lion cubs render looking like cheetahs (proven). Specify the distinguishing marks: lion cub = tawny, rounded face, only faint juvenile brown rosettes that fade, **NO cheetah spots, NO black tear-stripes**; cheetah = black tear-stripes + round solid spots (not a leopard's rosettes); etc. Every animal in one frame must read as the same, correct species.
- Risk ranking for execution cleanliness: **primates (hands+expressive faces) are the hardest**; big cats in profile/back are among the safest.

## 6. Negative vs Positive — tool-by-tool
| Model | Negatives? | Do instead |
|---|---|---|
| SD 1.5 / SDXL | Yes, strong | weighted negs `(term:1.4)` |
| Flux | Yes | negatives + strong descriptive positives |
| Leonardo / ComfyUI | Yes | granular CLIP negatives |
| Midjourney v6/v7 | Partial | `--no term1, term2` or `term::-0.5` |
| GPT-image / 4o | Ignored | positive description only |
| Reve / Nano Banana | Ignored | positive description only |

**Core principle for no-negatives models:** replace every "no X" with the positive opposite. "no plastic skin" → `visible pores, vellus hair, subsurface scattering, raking window light`.

## 7. Drop-in blocks
**Realism positive stack (any model):**
`natural skin texture, visible pores, fine lines, vellus hair, subtle sebum highlights, uneven skin tone, slight facial asymmetry, freckles, subsurface scattering, raking directional window light, natural catchlights in the eyes, shot on Kodak Portra 400, 85mm f/1.8, subtle film grain, candid unretouched expression`

**Universal negative (SD/SDXL/Flux/Leonardo):**
`(plastic skin, waxy skin, poreless skin, airbrushed:1.3), (deformed face, asymmetrical face, dead eyes, doll eyes:1.3), (bad teeth, crooked teeth:1.2), (bad hands, fused fingers, extra fingers, six fingers:1.4), (bad anatomy, extra limbs, missing limbs:1.4), 3D render, CGI, illustration, oversaturated`

**AVOID-word blacklist:** `beautiful, flawless, perfect, smooth, airbrushed, glossy, glowing, radiant, porcelain, silky, glamour, model-like`

---
*Sources: trendsbyai; vertu 2025 hands reality-check; aiarty & multic (Midjourney hands); perfectcorp (inpaint); morphic, promptaa, promptimagelab, sider, alibaba (skin); pxz.ai, zsky, picassoia (faces); whytryai, promptingguide 4o, dev.to (negatives); venturebeat & curiousrefuge (Reve); artlist/z-image (Seedream); allaboutai (Imagen); shopmoment (Portra 400). Verified 2024–2026.*
