# AI Image Models (2026) — Selection Guide

A film is never one image. It is hundreds of frames that must agree with each other: the same face, the same coat, the same light from one shot to the next. That single fact — **continuity** — is the lens through which a director must judge image models, and it is the opposite of the metric that goes viral on social media (one jaw-dropping hero shot). A model can be the most beautiful generator on earth and still be useless for filmmaking if it can't reproduce your protagonist twice. So this chapter ranks tools not by "which is prettiest" but by **the job**: hero cinematic still, legible text-in-image, precise structural control, and — the one that matters most for storyboards — character and world consistency.

> **Currency warning.** This space moves monthly. Everything here is dated to **mid-June 2026** and sourced. Treat version numbers, prices, and "newest model" claims as perishable. Where a fact is especially volatile I flag it inline. The decision *logic* (match the model to the job) outlives any specific version.

A note on a word you'll see throughout: a **reference image** is an input picture you give the model not to edit, but to *condition* the output — "make the new image look like / contain this." How many references a model accepts, and how faithfully it preserves them, is the single biggest differentiator in 2026. The frontier moved from "describe it in words" to "show me, and keep it consistent."

---

## The 2026 landscape in one breath

Three forces define the year. First, **Google's Gemini-family image models ("Nano Banana") collapsed the gap between speed and fidelity** and brought genuinely reliable multi-reference compositing plus real-world search grounding to the masses. Second, **Black Forest Labs' FLUX.2** made open-weights image generation a serious production tool with up-to-10-image multi-reference consistency. Third, **Midjourney shipped V8.1** as default (June 10, 2026), keeping its crown for raw aesthetic taste while finally exposing a proper reference stack (`--sref`, `--oref`; the older `--cref` is now V6/Niji 6 legacy). Everything else — Imagen, Ideogram, Recraft, Reve, Firefly, the SDXL/SD3.5 open stack — occupies a sharp niche.

---

## Midjourney — the aesthetic benchmark

**What it is and why it wins.** Midjourney has the strongest *default taste* of any model: lighting, color harmony, composition, and that intangible "this looks like a real cinematographer lit it" quality come out of the box without elaborate prompting. As of June 2026 the default is **V8.1** (released April 30, 2026; became default June 10, 2026), the fastest version yet, with native HD/2K output without a separate upscale step ([Midjourney docs](https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version), [PixVerse](https://pixverse.ai/en/blog/midjourney-ai-image-generator-review)).

**The reference stack (the part directors must know).** Midjourney's parameters are appended to a prompt with `--`:

| Parameter | Name | What it does |
|---|---|---|
| `--style raw` | Raw mode | Strips Midjourney's "house" beautification so the prompt is obeyed more literally — essential when you want *your* art direction, not MJ's defaults |
| `--sref <url/code>` | Style reference | "Make it look like this *aesthetic*" — color, grain, mood — without copying content |
| `--cref <url>` | Character reference *(legacy)* | "Keep this *character's* face/identity" across new scenes — **V6/Niji 6 only**; deprecated in V7+, superseded by `--oref` |
| `--oref <url>` | Omni-reference | V7+'s upgraded reference and the **current** consistency tool (use this on V8.1, not `--cref`): preserve a subject, object, or person with far higher fidelity than `--cref`; `--ow` controls strength |
| `--stylize` / `--s` | Stylize | How hard MJ pushes its aesthetic (low = literal, high = painterly) |

`--oref` (Omni-Reference, introduced in V7) is the headline consistency feature — it generalizes `--cref` from just faces to any subject or object and is the tool you reach for when a prop or a creature must recur ([AI Video Bootcamp guide](https://aivideobootcamp.com/blog/midjourney-complete-guide-2026/)).

**Weakness.** Two real ones. (1) **Text rendering is poor** — independent testing puts MJ near ~30% accuracy on short phrases versus ~90% for specialist models (that ~30% reflects older/longer-string tests; V8.1 did improve short-phrase legibility for single words and brief phrases inside quotes, but multi-word and precise typography remain unreliable); never use it for a poster, sign, or UI mockup that needs legible words ([pxz.ai](https://pxz.ai/blog/ideogram-ai-review-2026)). (2) **No API for most users and weaker programmatic control** — it lives in Discord/web, which makes it awkward inside an automated pipeline. Consistency via `--oref` is good but still loses to FLUX.2 / Nano Banana on hard multi-pose tests.

| Spec | Value |
|---|---|
| Max resolution | Native 2K HD (V8.1), upscalers beyond |
| Text quality | Weak (~30%) |
| Consistency | `--oref` (current; `--cref` is V6/Niji 6 legacy) — strong for faces, good for objects |
| Cost | $10 / $30 / $60 / $120 per month (Basic→Mega); 20% off annual ([Midjourney plans](https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans)) |
| Commercial | Included for all paid subscribers |
| Best job | **The hero cinematic still.** Mood, atmosphere, "movie poster" beauty. |

**→ AI APPLICATION.** Use Midjourney V8.1 to *establish your look* — generate the keyframe that defines your film's palette and lighting. Lock that frame's aesthetic with `--sref` for every subsequent shot, and carry the protagonist with `--oref --ow 100`. Pair `--style raw` with explicit cinematography language ("85mm, shallow depth of field, low-key Rembrandt lighting, anamorphic flare") to override MJ's defaults. Because MJ is weak on text and on rigid structure, hand those jobs to other models (below) — MJ is your *look-dev*, not your whole pipeline.

---

## Google "Nano Banana" 2 — the consistency + grounding workhorse

**What it is.** "Nano Banana" is the nickname for Google's Gemini-family image models. **Nano Banana 2 = Gemini 3.1 Flash Image** (API id `gemini-3.1-flash-image-preview`), released **February 26, 2026** — it fuses "Nano Banana Pro" capability with Flash speed and became the default across Gemini, Search, Lens, and Flow ([Google blog](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/), [TechCrunch](https://techcrunch.com/2026/02/26/google-launches-nano-banana-2-model-with-faster-image-generation/)).

**Why it matters for filmmakers.** Four things, in order of importance:

1. **Multi-image reference compositing at scale.** It maintains **up to 5 characters** and **up to 14 objects** consistent within one workflow — the strongest "keep my cast and props the same" feature shipping in mid-2026 ([Google blog](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/)).
2. **Conversational editing.** Because it's a Gemini model, you iterate in *dialogue* — "now make it night, keep her coat, move the camera lower" — across turns, instead of re-rolling a fresh prompt. This is the closest thing to directing an artist.
3. **Strong, legible text rendering** (and translation) — good enough for in-frame signage, titles, and mockups.
4. **Search grounding.** It can pull real-time info and *real reference images from web search* to render specific real-world subjects, landmarks, or current events accurately — unique among generators.

| Spec | Value |
|---|---|
| Model ID | `gemini-3.1-flash-image-preview` (a.k.a. Nano Banana 2; still a `-preview` build as of mid-2026) |
| Max resolution | 512px–4K |
| Text quality | Strong / precision text + translation |
| Consistency | Up to 5 characters, 14 objects per workflow; conversational edits |
| Cost | API per [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing); free via Flow; Nano Banana **Pro** ~$0.134/image for max factual accuracy |
| Best job | **Storyboard continuity + multi-element compositing + grounded reality** |

**Weakness.** Pure single-shot aesthetic taste still trails Midjourney for "movie-poster gorgeous." For absolute factual fidelity Google steers you to the heavier **Nano Banana Pro** rather than Flash.

**→ AI APPLICATION.** This is the model that makes AI *storyboarding* actually work. Build a reference sheet — your protagonist, the antagonist, the key prop, the location plate — and feed those as the multi-image reference set; then iterate every panel conversationally ("same characters, new beat: she enters the warehouse, dawn light"). When a scene must show a *real* place or product, lean on search grounding so the geometry and signage are correct. See **10-editing-theory.md** for why continuity across cuts is the thing the audience subconsciously polices, and the local **nano-banana-2** skill for exact API syntax.

---

## Google Imagen 4 — best value-per-pixel + best-in-class text

**What it is.** Imagen 4 (Fast / Standard / Ultra), GA February 2026, built on a Latent Diffusion Transformer, available via Gemini API, AI Studio, Vertex AI, and ImageFX ([Google Developers blog](https://developers.googleblog.com/announcing-imagen-4-fast-and-imagen-4-family-generally-available-in-the-gemini-api/)).

**Strength.** Widely cited as having **the strongest legible text rendering in the class**, at the **lowest price**: Fast ~$0.02, Standard ~$0.04, Ultra ~$0.06/image — cheaper than DALL·E 3 HD and far cheaper than Nano Banana Pro ([ThePlanetTools](https://theplanettools.ai/blog/google-imagen-4-models-fast-standard-ultra-guide-2026), [CloudPrice](https://cloudprice.net/models/google-imagen-4-ultra)). Imagen 4 Ultra outputs native 2K (2048×2048).

| Spec | Value |
|---|---|
| Max resolution | Native 2K (Ultra) |
| Text quality | Best-in-class legibility |
| Consistency | Weaker than Nano Banana / FLUX.2 (no rich multi-ref) |
| Cost | $0.02 / $0.04 / $0.06 per image |
| Best job | **High-volume, text-accurate, budget batch generation** |

**→ AI APPLICATION.** Imagen 4 is your *cost-efficient batch engine* — generating many establishing plates, title cards, or text-bearing frames where you don't need elaborate reference control. When the storyboard needs 200 quick variations, Imagen Fast at 2 cents each beats paying Midjourney GPU-hours. Promote to Nano Banana 2 the moment continuity across panels becomes the priority.

---

## FLUX family (Black Forest Labs) — the open-weights production tool

**What it is.** **FLUX.2** launched November 25, 2025, with three shipping tiers — Pro, Flex, and Dev — and a distilled **Klein** (Apache-2.0, 4B/9B) that followed on Jan 15/16, 2026 ([BFL](https://bfl.ai/models/flux-2)):

| Tier | Nature |
|---|---|
| **Pro** | Production API, frontier quality (~$0.03/megapixel) |
| **Flex** | Developer variant |
| **Dev** | **32B open weights** on Hugging Face; self-host commercial license $999/mo (incl. 100k images) |
| **Klein** | **Apache-2.0** distilled family (4B/9B, e.g. `FLUX.2-klein-4B`), runs anywhere free, sub-second on consumer GPUs — *not part of the Nov 25 launch; released Jan 15/16, 2026*; ~$0.014/MP on API |

*(Currency note: BFL's live models page has since added a **FLUX.2 [max]** tier above Pro for the highest editing consistency — the four-tier framing above was accurate at launch.)*

**Why it matters.** FLUX.2 references **up to 10 images simultaneously**, fusing them into one stable identity that survives across poses and lighting — community benchmarks score it ~92/100 on consistency, edging Midjourney on multi-pose tests ([the-decoder](https://the-decoder.com/black-forest-labs-launches-flux-2-with-a-new-multi-reference-feature/), [Together AI](https://www.together.ai/blog/flux-2-multi-reference-image-generation-now-available-on-together-ai)). **FLUX Kontext** is the editing-focused model: instruction-based edits ("change the jacket to red, keep everything else") on existing frames. And crucially, **open weights** mean you can run it locally, fine-tune it, and bolt it into ComfyUI with ControlNet/LoRA.

| Spec | Value |
|---|---|
| Max resolution | Up to 4MP (edit), high-res gen |
| Text quality | Good (much improved in FLUX.2) |
| Consistency | Up to 10 reference images; top-tier multi-pose |
| Cost | Klein free (Apache-2.0); Dev $999/mo commercial self-host; Pro ~$0.03/MP |
| Best job | **Self-hosted, reproducible, fine-tunable consistency pipeline** |

**→ AI APPLICATION.** FLUX.2 is the choice when you need **ownership and reproducibility** — a fixed seed + fixed weights + a LoRA of your character means the *exact same* generator next month, no silent model drift, no per-image cloud fee at volume. Use the 10-image multi-ref to lock your cast, FLUX Kontext for surgical frame edits between shots, and Klein for free local drafting. This is the backbone of a serious indie AI-film pipeline that can't depend on a closed API changing under it.

---

## Ideogram & Recraft — the typography and design specialists

**Ideogram (3.0).** The text-in-image champion: ~90% text accuracy via its Reliable Typography Engine, handling long strings, kerning, and multiple fonts without hallucinating letters; supports up to 3 style-reference images, plus Canvas with Magic Fill (inpainting) / Extend (outpainting). API ~$0.04 standard / $0.08 high-res ([pxz.ai](https://pxz.ai/blog/ideogram-ai-review-2026), [MindStudio](https://www.mindstudio.ai/blog/what-is-ideogram-v3)). **Best job: posters, title cards, signage, any frame where words must be perfect.**

**Recraft (V3/V4).** "Thinks in design language" — long the #1 on the Artificial Analysis benchmark; the standout is **editable vector/SVG output** (V4 Vector / Pro Vector) and the ability to place text at *specific positions*, plus brand-style training ([Recraft blog](https://www.recraft.ai/blog/recraft-introduces-a-revolutionary-ai-model-that-thinks-in-design-language)). **Best job: logos, UI, iconography, and any asset that must scale as vector** — title-sequence graphics, lower-thirds, motion-graphic source art.

**→ AI APPLICATION.** Filmmaking has text-bearing surfaces — newspaper inserts, neon signs, end-credit cards, a phone screen in a close-up. Generate the *scene* in your cinematic model, then composite a typographically perfect element from Ideogram, or build scalable title/credit graphics in Recraft's vector mode for crisp motion design downstream. Never ask a beauty model to spell.

---

## Reve & Adobe Firefly — prompt-adherence and the safe enterprise option

**Reve.** A newer entrant focused on tight **prompt adherence and accurate text** — when the literal contents of the frame must match a precise brief, it's a strong contender; verify current capabilities before committing *(verify — fast-moving; see open questions).*

**Adobe Firefly (2026).** The transformation of 2026 is that Firefly became a **multi-model studio**: 30+ models (Runway Gen-4.5, Nano Banana Pro, OpenAI image, FLUX.2 [pro]) alongside Adobe's own **commercially-safe, IP-indemnified** models, plus Custom Models (train on your own assets), Design Intelligence (brand Style IDs), and a conversational Firefly AI Assistant ([Adobe news](https://news.adobe.com/news/2026/04/adobe-new-creative-agent), [blog](https://blog.adobe.com/en/publish/2026/03/19/adobe-firefly-expands-video-image-creation-with-new-ai-capabilities-custom-models)). **Firefly's real selling point isn't the model — it's the legal cleanliness and Creative Cloud integration.**

**→ AI APPLICATION.** If your film is commercial work where a client demands indemnification against training-data lawsuits, generate with Firefly's native model — taste is a notch below Midjourney, but the legal coverage is the deliverable. Otherwise, treat Firefly as a *router/aggregator* to access many models inside Photoshop/Premiere with content credentials attached.

---

## The open controllable stack: SDXL / SD3.5 + ComfyUI + ControlNet + LoRA

This is not one model but the **maximum-control workbench**, and in 2026 it's run almost entirely through **ComfyUI** (the node-based interface, ~117k GitHub stars as of June 2026; most pros migrated off AUTOMATIC1111) ([tech-insider](https://tech-insider.org/comfyui-tutorial-sdxl-flux-workflow-13-steps-2026/), [ComfyUI Wiki](https://comfyui-wiki.com/en/tutorial/advanced/stable-diffusion-3-5-comfyui-workflow)). Three base families cover ~95% of work: **SDXL** (fast iteration), **Stable Diffusion 3.5 Large** (photoreal fidelity), and **FLUX.1 [dev]** (best prompt adherence).

Two control primitives are the reason this stack exists:

- **ControlNet** — conditions generation on *structure*: a pose skeleton, a depth map, Canny edges, a scribble. This is how you force a generated character into an *exact* pose or match a shot's composition precisely — impossible with prompt words alone. SD3.5 ships Blur/Canny/Depth ControlNets.
- **LoRA** (Low-Rank Adaptation) — small 50–300 MB weight files that teach a base model a *specific* face, style, or object. Train a LoRA of your protagonist once and summon them, on-model, forever. CivitAI hosts thousands; Hugging Face the official bases.

| Spec | Value |
|---|---|
| Max resolution | Model-dependent; tiled/upscale workflows push high |
| Text quality | Weak on SDXL; better on SD3.5/FLUX |
| Consistency | **Highest possible** via trained LoRA + ControlNet |
| Cost | Free (your own GPU) + electricity |
| Best job | **Frame-exact control + bespoke trained character consistency** |

**→ AI APPLICATION.** This is the **director's control booth**. When a shot must hit an exact pose, an exact camera composition, or reuse a character with zero drift, you draw/extract a pose or depth map, drive it through ControlNet, and overlay a character LoRA. It's the most labor-intensive option and demands a real GPU, but it converts AI image generation from "slot machine" into "instrument." Pair with **08-lenses-lighting-color.md** (if present) for matching virtual lens geometry to the ControlNet depth pass.

---

## Decision table — "if you need X, use Y"

| If you need… | Use | Why |
|---|---|---|
| The most beautiful single hero still | **Midjourney V8.1** (`--style raw` + cinematography prompt) | Best default aesthetic taste |
| Storyboard panels with a consistent cast/props | **Nano Banana 2** (multi-ref, conversational) | 5 chars / 14 objects, iterate in dialogue |
| A real place / product / current event rendered accurately | **Nano Banana 2** (search grounding) | Pulls real reference imagery |
| Legible words inside the frame (sign, poster, title) | **Ideogram 3.0** (or Imagen 4) | ~90% text accuracy |
| Scalable vector logo / UI / title graphic | **Recraft V4 Vector** | True editable SVG output |
| Hundreds of cheap frames, text-accurate, on a budget | **Imagen 4 Fast/Standard** | $0.02–0.04/image, best-value text |
| Self-hosted, reproducible, fine-tunable pipeline | **FLUX.2 [dev]/[klein]** | Open weights, 10-image multi-ref |
| Frame-EXACT pose / composition control | **ComfyUI + ControlNet + LoRA** | Structural conditioning + trained identity |
| Surgical edit to an existing frame | **FLUX Kontext** (or Nano Banana 2) | Instruction-based local edits |
| Legally indemnified commercial deliverable | **Adobe Firefly** (native model) | IP indemnification + content credentials |

---

## → AI APPLICATION: the recommended default stack for cinematic storyboard frames

No single model wins. A storyboard pipeline that actually holds continuity looks like this:

1. **Look-dev (taste):** Generate the defining keyframe in **Midjourney V8.1**, `--style raw` + explicit lens/lighting language. Capture its `--sref` style code — that code is now your film's "lookbook."
2. **Reference sheet (identity):** Lock each recurring character, prop, and location plate as clean reference images. Build a **character LoRA in the ComfyUI/FLUX stack** if you need zero-drift reuse and own-the-weights reproducibility.
3. **Panel generation (continuity):** Drive every storyboard panel through **Nano Banana 2** with the multi-image reference set, iterating *conversationally* beat by beat — same cast, new action, new light. This is where 5-character / 14-object consistency earns its keep.
4. **Structural overrides (control):** When a panel needs an exact pose or matched composition, route through **ComfyUI + ControlNet** (pose/depth) with the character LoRA.
5. **Text & graphics:** Composite any in-frame text from **Ideogram**, title/credit vector art from **Recraft**.
6. **Volume & budget fill:** Use **Imagen 4 Fast** for cheap throwaway variations and rough layout passes.

**Why this shape?** Because the four jobs — *beauty, identity, continuity, control* — are won by different models, and continuity (the filmmaker's true bottleneck) is won by reference-driven, conversational generation (Nano Banana 2) backed by a reproducible trained identity (FLUX/LoRA), not by the prettiest single-shot generator. Start one tier up (closed cloud) for speed; move down to the open stack the moment reproducibility or cost-at-scale dominates. See **10-editing-theory.md** for why an audience forgives a slightly-less-beautiful frame far more readily than a character whose face changed between cuts.

---

## Sources

- Midjourney: [Version docs](https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version) · [Plans](https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans) · [2026 guide](https://aivideobootcamp.com/blog/midjourney-complete-guide-2026/) · [PixVerse review](https://pixverse.ai/en/blog/midjourney-ai-image-generator-review)
- Nano Banana 2: [Google blog](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/) · [TechCrunch](https://techcrunch.com/2026/02/26/google-launches-nano-banana-2-model-with-faster-image-generation/) · [Gemini image docs](https://ai.google.dev/gemini-api/docs/image-generation)
- Imagen 4: [Google Developers blog](https://developers.googleblog.com/announcing-imagen-4-fast-and-imagen-4-family-generally-available-in-the-gemini-api/) · [ThePlanetTools pricing](https://theplanettools.ai/blog/google-imagen-4-models-fast-standard-ultra-guide-2026) · [CloudPrice Ultra](https://cloudprice.net/models/google-imagen-4-ultra)
- FLUX.2: [BFL model page](https://bfl.ai/models/flux-2) · [BFL pricing](https://bfl.ai/pricing) · [the-decoder](https://the-decoder.com/black-forest-labs-launches-flux-2-with-a-new-multi-reference-feature/) · [Together AI](https://www.together.ai/blog/flux-2-multi-reference-image-generation-now-available-on-together-ai) · [HF FLUX.2-dev](https://huggingface.co/black-forest-labs/FLUX.2-dev)
- Ideogram: [pxz.ai review](https://pxz.ai/blog/ideogram-ai-review-2026) · [MindStudio](https://www.mindstudio.ai/blog/what-is-ideogram-v3)
- Recraft: [Recraft blog](https://www.recraft.ai/blog/recraft-introduces-a-revolutionary-ai-model-that-thinks-in-design-language)
- Adobe Firefly: [Adobe news](https://news.adobe.com/news/2026/04/adobe-new-creative-agent) · [Adobe blog](https://blog.adobe.com/en/publish/2026/03/19/adobe-firefly-expands-video-image-creation-with-new-ai-capabilities-custom-models)
- Open stack: [ComfyUI tutorial](https://tech-insider.org/comfyui-tutorial-sdxl-flux-workflow-13-steps-2026/) · [ComfyUI Wiki SD3.5](https://comfyui-wiki.com/en/tutorial/advanced/stable-diffusion-3-5-comfyui-workflow)
