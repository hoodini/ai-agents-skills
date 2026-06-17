# AI Character & Wardrobe Consistency — The Hard Problem

This is the chapter that separates a one-off "wow" image from an actual *film*. A film is the same person, in the same clothes, lit and shot a dozen different ways, who the audience accepts as one continuous human being. Every other craft chapter in this bible — blocking (see `03-character-and-scene-craft.md`), shot grammar (`06-shots-framing-composition.md`), the 180-degree rule and continuity in the cut (`10-editing-theory.md`) — silently assumes you *can* put the same character in shot after shot. With AI, you can't, not for free. Identity is the thing the technology is structurally worst at, and it is the thing your audience is most ruthlessly tuned to police. We have a fusiform face area and decades of social evolution dedicated to noticing when a face is subtly *wrong*. So this is the hard problem. Here is why it's hard, and the full toolkit, lightest to heaviest.

## Why Identity Is Structurally Hard

Intuition first. A diffusion model does not store "your character." It stores a vast, smooth landscape — *latent space* — where every possible image is a coordinate, and nearby coordinates look similar. When you generate, the model starts from random noise (a random coordinate) and walks toward the region your prompt describes. "A 30-year-old woman with red hair" is not a point; it's a huge *neighborhood* containing billions of plausible red-haired women. Each generation lands on a different coordinate inside that neighborhood. There is no persistent variable holding "this exact face" between runs. The model has no memory and no identity — it has a probability distribution and a dice roll.

This is the core sentence to internalize: **every generation samples a new point in latent space, and the model has no persistent identity to anchor to.** A human painter holds a mental model of a character and re-projects it. The diffusion model re-rolls. Consistency techniques are therefore all variations on one idea: *shrink the neighborhood the dice can land in, or inject the actual coordinate of your character into the process.* Lightest methods just narrow the neighborhood with words; heaviest methods (LoRA/DreamBooth) literally teach the model a new coordinate and give it a name.

A second hardness, specific to *video*: temporal models must keep identity stable across frames *and* across separate clips. Within a single 5-8 second generation, modern models hold a face reasonably well. The break happens at clip boundaries — clip 2 is a fresh dice roll. That seam is where most AI "films" fall apart, and §7 is dedicated to it.

→ **AI APPLICATION:** Stop expecting prompt-only consistency to work and stop being surprised when it fails — it's not a skill issue, it's the architecture. Budget your effort: the more shots a character appears in, the further down this ladder you must climb. Treat "lock the identity" as a *production step* with its own deliverable (a locked reference image or a trained model), exactly like casting an actor before you shoot.

## 1. The Verbal Character ID Block (and Its Limits)

The cheapest tool: write a fixed, hyper-specific identity paragraph and paste it verbatim into every prompt. Not "a man with brown hair" but a *forensic* description:

> **MARCUS** — male, 34, Black, 6'1", lean athletic build. Short-cropped natural hair, faded sides. Square jaw, faint scar above left eyebrow, deep-set dark brown eyes, broad nose, full lips, light stubble. Warm medium-deep skin tone. Wears a charcoal wool overcoat over a white crew tee, dark indigo selvedge jeans, white leather sneakers. Silver ring, left index finger.

The mechanism: each precise attribute is a constraint that shrinks the latent neighborhood. "Brown hair" leaves a million faces; "scar above left eyebrow, broad nose, deep-set eyes" leaves far fewer. You are narrowing the dice.

**The honest limit:** words underdetermine a face. There are still thousands of distinct people matching even a long description, and the model will happily give you a different one each time. The ID block buys you *type* consistency (same vibe, same demographic, same outfit category) not *identity* consistency (same person). It is necessary but never sufficient for anything beyond a single shot. Anyone who tells you a clever enough text prompt gives stable character identity across many shots is wrong — language is too lossy a channel for a face. The ID block's real job is to be the *textual companion* to a reference image (§3), keeping wardrobe and proportions on-message while the image carries the face.

→ **AI APPLICATION:** Maintain one canonical ID block per character in a project file. Paste it identically every time — never paraphrase, because synonyms ("dark brown" vs "espresso") move you to a different latent region. Front-load the most identity-bearing features (face geometry, distinctive marks) since most models weight earlier tokens more heavily. In Veo/Sora natural-language prompts, the ID block reads as a sentence; in Midjourney, compress it and let `--oref` (§3) carry the face.

## 2. Seed Locking & Prompt Determinism

The *seed* is the specific random number that picks the starting noise — the dice roll itself. Fix the seed and fix the prompt, and (on the same model version and settings) you get a bit-identical image. So can't we just lock the seed for consistency? This is the most common beginner misconception, so be precise about it.

| Same seed, you change... | Result |
|---|---|
| Nothing | Identical image (useless for a film — one shot only) |
| One word in the prompt | A *related but different* image — face can shift completely |
| The pose / camera / action | Often a new person who happens to share palette/mood |

Seed locking gives you *reproducibility*, not *portability of identity*. Identity does not "ride along" the seed when you change the scene. The same seed with "standing" vs "running" can hand you two different faces, because the seed only fixes the starting noise — the prompt change steers the denoising elsewhere. Where seed locking genuinely helps: A/B testing one variable at a time (lock everything, change only lighting to compare), and re-rolling a near-miss with tiny prompt nudges to stay in the same family. It is a *control* tool, not a *consistency* tool.

→ **AI APPLICATION:** Use a fixed seed during the *exploration* phase to isolate variables, then once you've found a hero image, *discard the seed strategy* and switch to reference-image methods to carry that face into other shots. In Midjourney read the seed from the job (envelope react / `/show`); in ComfyUI and the SD ecosystem the seed is an explicit node — set the sampler to `fixed`, not `randomize`, while tuning. Don't market seed-locking to yourself as a consistency solution; it isn't one.

## 3. Reference-Image Methods (the workhorse tier)

Now we inject the actual character into the process instead of describing it. This is where 80% of practical work lives. You give the model a picture of the person and it conditions generation on that picture's identity features. The toolkit, by platform, as of mid-2026:

### Midjourney — `--cref` then `--oref` (mind the version split)

Midjourney's original **Character Reference (`--cref <url>`)** worked on V6, with `--cw 0-100` controlling how much it copied (low = face only; high = face + hair + clothes). **It does not work on V7+.** V7 replaced it with **Omni-Reference (`--oref <url>`)** plus **Omni-Weight (`--ow 0-1000`, default 100)** — a more general "put *this thing* into my image" system that handles characters, objects, and props, blending the reference into a fresh prompt. Critical, currency-sensitive fact: **`--oref` and `--ow` are V7-only and are *not* available in V8 / V8.1.** V8.0 alpha launched March 17 2026, V8.1 shipped April 30 2026 and became the *default* on June 10 2026 ([docs.midjourney.com/Version](https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version), [WaveSpeed](https://wavespeed.ai/blog/posts/what-is-midjourney-v8-features-pricing-how-to-use-2026/)). So in mid-2026 you face a real tradeoff: V8.1 gives faster, HD output but, at time of writing, you must **drop to V7 to use omni-reference** for character work. Raise `--ow` toward 400-1000 for a stubborn likeness; lower it (~50-100) when you want the face but freedom in styling.

### Nano Banana Pro (Gemini 3 Pro Image) — multi-image compositing

Google's **Nano Banana Pro** (the nickname for the Gemini 3 Pro image model) is arguably the strongest *practical* consistency tool in mid-2026 because of how it composes. You upload **up to 14 images** (up to 6 object references plus up to 5 human references) and it maintains the likeness of **up to 5 people** in one generation ([blog.google](https://blog.google/technology/ai/nano-banana-pro/), [AVB guide](https://aivideobootcamp.com/blog/nano-banana-pro-complete-guide-2026/)). Workflow: upload 3-5 shots of your character from different angles **plus** a target scene/pose image, and instruct "place *this person* into *this scene*." Its edge is **partial denoising** — instead of re-rolling from scratch, it selectively edits attributes (swap the shirt red→blue) while preserving the underlying *facial fingerprint*. That is conversational, iterative identity editing, the thing diffusion is normally worst at. Practical caps: ~5 unique characters in the Gemini app, 4 via the developer API.

### Video models — subject / ingredients reference

| Model (mid-2026) | Consistency mechanism |
|---|---|
| **Runway Gen-4.5** | Reference-driven character consistency + camera control; strong all-rounder for image-to-video with a locked subject ([aimagicx](https://www.aimagicx.com/blog/ai-video-generation-showdown-2026)) |
| **Kling 3.0 (Omni)** | Multi-shot sequences with subject consistency across angles; pick this for dialogue / storyboards |
| **MiniMax Hailuo 02** | Native **subject reference** input for consistent characters across scenes |
| **Veo 3.1** | **"Ingredients to Video"**: up to **3 reference images** to fix character/object, plus first-and-last-frame control ([genra.ai](https://genra.ai/blog/veo-3-1-complete-guide)) |
| **Sora 2** | More automated single-reference image-to-video; longer single clips (~25s) but no first/last-frame control |

### SD / ComfyUI stack — IP-Adapter, InstantID, PuLID, face-swap

In the open-source stack you get surgical control. All three identity adapters build on **InsightFace** (a face-analysis library that extracts a numeric face *embedding*) and inject that embedding into generation:

- **IP-Adapter (FaceID variants)** — earliest; treats the face as an image prompt. Flexible, lower fidelity.
- **InstantID** — best balance of likeness and control; ranks at or near the top on identity fidelity (FaceID can edge it on raw face-similarity in some tests), most resource-heavy; uses face embedding + keypoint control.
- **PuLID** — fast, clean, plays well with Flux; clearly lags both InstantID and FaceID on raw likeness in head-to-head ComfyUI tests.
- **Face-swap (ReActor / the older Roop)** — a *post-process*: generate freely, then paste the target identity onto the rendered face. Cheapest path to a recognizable face, but it can look "stuck on," fights extreme angles, and carries obvious deepfake-ethics weight.

Known gotcha: running **InstantID + IP-Adapter together degrades the face after ~3-4 runs** in recent ComfyUI builds ([GitHub issue #12989](https://github.com/Comfy-Org/ComfyUI/issues/12989)). A robust recipe people converge on is **SDXL base → InstantID for the swap → IP-Adapter for pose/lighting match → FaceDetailer to clean the face** ([MyAIForce](https://myaiforce.com/comfyui-instantid-ipadapter/)).

→ **AI APPLICATION:** Default to **Nano Banana Pro** for stills and shot-setup when you need fast, conversational identity + wardrobe edits across a scene — it's the lowest-friction strong option in mid-2026. Use **Midjourney V7 `--oref --ow 300+`** when you want its aesthetic and can live in V7. Reach for the **ComfyUI InstantID/PuLID** stack when you need free local iteration, exact reproducibility, or a pipeline you fully own. For video, generate the hero frame as a still first, then feed it as the **subject/ingredient reference** (Veo "Ingredients," Hailuo subject-ref, Runway reference) — never ask the video model to invent the identity from text.

## 4. Character Turnaround / Model Sheet (the cheat that compounds)

Animation studios draw a **model sheet** (a.k.a. *character turnaround*): the same character from front, 3/4, side, and back, plus expressions, on one sheet. Borrow it directly. Generate (or assemble) a **multi-view character sheet** of your AI character, then use *that* as your reference image everywhere downstream. Why it works: a single front photo gives the model no information about the side of the head, so when you ask for a profile shot it *invents* one and drifts. A turnaround supplies the geometry from multiple angles, so reference-based generation has real data to copy for any camera position.

The related **"character grid" trick**: prompt a single image containing a grid of the same character in varied poses/expressions ("character sheet, multiple poses, neutral background, consistent face"). Because they're generated *together in one pass*, they share one identity — the model is forced to keep them the same. Then crop the cell you need and use it as the reference for full shots.

→ **AI APPLICATION:** As step one of every recurring-character project, generate a clean turnaround (front / 3-4 / profile / back, neutral light, plain background) and a grid of 6-9 expressions. In Nano Banana, feed 3-5 of those views as the multi-image reference. In ComfyUI, the turnaround views become your InstantID reference pool. Keep the sheet in the project folder as the character's "headshot on file."

## 5. LoRA / DreamBooth — the Gold Standard

Everything above conditions a *frozen* model. Fine-tuning *changes the model* to actually learn your character and bind it to a trigger word. This is the only method that delivers near-total identity consistency from a simple text prompt, because you've literally added your character's coordinate to latent space and named it.

- **DreamBooth** retrains the model on your subject — highest fidelity, heavy VRAM/time, large files.
- **LoRA** (Low-Rank Adaptation) trains a tiny add-on layer instead of the full model — small file (typically tens to a couple hundred MB, depending on rank), fast, stackable. In 2026 LoRA is almost always the right call; with Flux the practical quality gap to DreamBooth is minimal ([Apatero](https://apatero.com/blog/flux-2-pro-lora-training-character-consistency-2026)).

**Dataset, the part everyone gets wrong:** not "more images." The rule is **consistency in what you're training, diversity in everything else.** Same face/body — different angles, lighting, expressions, backgrounds, distances. Flux character LoRAs train well on **~15-30 images** (often cited as a 20-image sweet spot); going to 140 images can fail to converge ([Civitai guide](https://civitai.com/articles/7777/detailed-flux-training-guide-dataset-preparation), [kohya-ss #1492](https://github.com/kohya-ss/sd-scripts/issues/1492)). Including a few stylized renders alongside photos actually *improves* cross-style robustness.

**When it's worth it:** the cost is real (curating a dataset, a training run, often $10-30 of GPU or a local 4090 hour). Worth it when the character recurs across **many** shots/projects — a brand mascot, a series lead, a virtual influencer. Not worth it for a one-shot ad.

The compounding move: use §3-§4 (reference + turnaround) to *generate* a consistent 20-image dataset of a character who never existed, then train a LoRA on it. You bootstrap a fully owned, infinitely reusable character from nothing.

→ **AI APPLICATION:** Decision rule — **recurring across a project/brand → train a Flux LoRA.** Build the dataset from a reference-locked turnaround (20-25 images, varied pose/light/background, tight crops on face). Train on Flux (Replicate/fal/Modal hosted, or local kohya/ComfyUI). Assign a rare trigger token (`mrcsx_man`, not "Marcus" which collides with priors). Then a plain text prompt yields the same person on demand — and you can stack a *wardrobe* LoRA on top (§6).

## 6. Wardrobe / Clothing Consistency Specifically

Faces get all the attention; clothing breaks just as visibly and is *harder*, because garments have logos, prints, seams, and drape that the model re-improvises every roll. A consistent face in a different jacket still reads as a continuity error in the cut. Layered toolkit:

1. **Forensic garment description in the ID block** — exact garment, color (with a named hue), material, cut, closures, distinctive details. "Charcoal wool overcoat, notch lapel, single-breasted, three buttons" beats "a coat."
2. **Reference crops** — crop *just the garment* and feed it as an additional reference image (Nano Banana multi-image, IP-Adapter on a clothing region). This carries texture/logo that words can't.
3. **"Outfit lock" prompt pattern** — repeat the wardrobe line verbatim and add "wearing the exact same outfit as the reference, identical clothing." With Nano Banana's partial denoising you can lock the outfit and change only pose/scene.
4. **Virtual try-on / garment transfer** — purpose-built models that warp a *specific* garment onto a person: **IDM-VTON** (GarmentNet preserves fine detail, higher realism), **CatVTON** (radically simple, runs ~35s at 1024×768 on <8GB VRAM), plus newer **OmniVTON++** and **JCo-MVTON** ([opencreator](https://opencreator.io/blog/ai-virtual-try-on-models), [arXiv OmniVTON++](https://arxiv.org/pdf/2602.14552)). Honest caveat: small-detail drift (prints, logos, fine texture) is still a real risk — don't ask one generation to solve pose + drape + identity + product fidelity at once.

→ **AI APPLICATION:** Treat the outfit as a second locked asset alongside the face. Best mid-2026 still pipeline: lock the face with Nano Banana / InstantID, then run **IDM-VTON or CatVTON** to stamp the exact garment, then composite. For a recurring costume, train a **garment LoRA** and stack it with the character LoRA. Always keep a clean front-on garment crop in the project folder as the wardrobe reference.

## 7. Cross-Clip Consistency in Video

The single biggest AI-film failure mode: clip 1 looks great, clip 2 is a slightly different person in slightly different clothes, and the cut screams "AI." The fix is **frame chaining**: the **last frame of clip N becomes the first frame (image-to-video seed) of clip N+1.** Because clip N+1 starts from an actual frame containing your locked character, identity carries across the seam. Veo 3.1's first-and-last-frame control is built for exactly this and lets you chain ~7s extensions to ~148s of continuous identity ([glbgpt](https://www.glbgpt.com/hub/veo-3-1-vs-sora-2/)); Sora 2 lacks a first/last-frame equivalent, which hurts multi-shot continuity despite longer single clips.

Companion technique: a **"same character bridge"** line repeated in every clip's prompt — "the same [ID block] as the previous shot, identical face and outfit, continuous scene" — plus feeding the *same subject reference image* to every clip so each generation re-anchors to one source of truth rather than to the previous clip's drift. For a true cut (new angle, not a continuation), don't chain frames — instead drive *all* clips from the *same hero still / character sheet* as the reference, so they converge on one identity independently.

→ **AI APPLICATION:** For continuous action, chain in Veo 3.1 (last-frame → next clip's first frame). For separate shots in a scene, generate every clip from the *same* locked hero still as subject reference + repeat the bridge line + reuse the ID block verbatim. Extract the last frame with `ffmpeg -sseof -0.1 -i clipN.mp4 -frames:v 1 lastframe.png` and feed it as the start image for the next generation. Match `10-editing-theory.md`'s continuity rules: a clean identity at the cut point is what makes the edit invisible.

## The Decision Ladder

| Scenario | Right tool |
|---|---|
| Single hero still / 1-shot ad | Strong text ID block + **one** reference image (Nano Banana or MJ V7 `--oref`) |
| A handful of shots, one scene | Character **turnaround** sheet → reference into every shot; outfit-lock prompt |
| Short video, continuous action | Hero still → image-to-video → **frame-chain** (Veo 3.1 first/last) |
| Short video, multiple cuts | Same hero still as subject ref for every clip + bridge line |
| Recurring brand character / series lead / virtual influencer | **Train a Flux LoRA** (gold standard) + optional garment LoRA |
| Exact clothing fidelity (logo/print) | Reference crop + **IDM-VTON / CatVTON** virtual try-on |
| Need local, free, reproducible iteration | ComfyUI **InstantID/PuLID** + FaceDetailer |

## AI APPLICATION — The Repeatable Consistency SOP

A standing operating procedure to run on *every* project:

1. **Write the canonical ID block** for each character (face geometry first, then marks, then wardrobe). Save to `characters/marcus.md`. Never paraphrase it later.
2. **Generate the hero portrait.** Iterate with a *fixed seed* to isolate variables; once you love a face, that image is "cast."
3. **Build the turnaround + expression grid** from the hero (front / 3-4 / profile / back; 6-9 expressions). Save to `characters/marcus_sheet/`. This is your reference pool.
4. **Lock wardrobe** as a separate clean garment crop in `characters/marcus_wardrobe/`.
5. **Decide scope on the ladder.** Few shots → reference + turnaround. Recurring → generate a 20-25 image dataset from the sheet and **train a LoRA** (rare trigger token); stack a garment LoRA if the costume recurs.
6. **For stills:** Nano Banana Pro multi-image (3-5 sheet views + scene) with partial-denoise edits; or MJ V7 `--oref --ow 300+`; or ComfyUI InstantID → FaceDetailer.
7. **For video:** generate each shot's start frame as a *still* using step 6 (never let the video model invent identity from text); image-to-video from that frame; **frame-chain** continuous action (Veo 3.1), or drive every cut from the same hero still + bridge line.
8. **QC every output against the hero portrait** before accepting — eye spacing, jaw, distinctive mark, exact garment. Reject drift; re-roll or re-anchor. Treat continuity errors as bugs, not "good enough."
9. **Version and archive** the locked assets (hero still, sheet, LoRA, garment) per character so the next project reuses the *same* identity instead of re-rolling the dice.

The mindset shift: in AI filmmaking, **casting is an asset-creation step you do once and protect forever** — a hero still, a sheet, a LoRA, a garment crop. Everything downstream conditions on those assets. Get identity locked before you shoot a single "frame," exactly as a live-action production locks its cast and costumes before principal photography.

## Sources

- [Midjourney — Character Reference (`--cref`)](https://docs.midjourney.com/hc/en-us/articles/32162917505293-Character-Reference)
- [Midjourney — Omni-Reference (`--oref`)](https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference)
- [Midjourney — Version docs (V8 timeline)](https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version)
- [WaveSpeed — What Is Midjourney V8 (2026)](https://wavespeed.ai/blog/posts/what-is-midjourney-v8-features-pricing-how-to-use-2026/)
- [Google — Introducing Nano Banana Pro](https://blog.google/technology/ai/nano-banana-pro/)
- [AVB — Nano Banana Pro Complete Guide 2026](https://aivideobootcamp.com/blog/nano-banana-pro-complete-guide-2026/)
- [Nano Banana 2 Subject Consistency (object/character caps)](https://www.glbgpt.com/hub/nano-banana-2-subject-consistency/)
- [AI Magicx — Kling v3 vs Hailuo 02 vs Runway Gen-4.5 vs Luma (2026)](https://www.aimagicx.com/blog/ai-video-generation-showdown-2026)
- [Genra — Veo 3.1 Complete Guide](https://genra.ai/blog/veo-3-1-complete-guide)
- [glbgpt — Veo 3.1 vs Sora 2 (consistency, frame control)](https://www.glbgpt.com/hub/veo-3-1-vs-sora-2/)
- [MyAIForce — PuLID vs InstantID vs FaceID](https://myaiforce.com/pulid-vs-instantid-vs-faceid/)
- [MyAIForce — InstantID + IP-Adapter + FaceDetailer workflow](https://myaiforce.com/comfyui-instantid-ipadapter/)
- [ComfyUI Issue #12989 — InstantID/IP-Adapter face degradation](https://github.com/Comfy-Org/ComfyUI/issues/12989)
- [Apatero — FLUX 2 Pro LoRA Character Consistency 2026](https://apatero.com/blog/flux-2-pro-lora-training-character-consistency-2026)
- [Civitai — Detailed Flux Training Guide: Dataset Preparation](https://civitai.com/articles/7777/detailed-flux-training-guide-dataset-preparation)
- [kohya-ss #1492 — large dataset non-convergence](https://github.com/kohya-ss/sd-scripts/issues/1492)
- [OpenCreator — AI Virtual Try-On Models (IDM-VTON, CatVTON, VITON-HD)](https://opencreator.io/blog/ai-virtual-try-on-models)
- [arXiv — OmniVTON++ (training-free universal try-on)](https://arxiv.org/pdf/2602.14552)
