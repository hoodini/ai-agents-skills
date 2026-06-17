# AI Video Models (2026) — Selection Guide

A film director in 1925 chose a film stock, a lens set, and a lab. A director in 2026 chooses a **model**. The model is your stock, your lens, your camera operator, and — increasingly — your sound recordist all at once, and unlike celluloid it changes its capabilities every six to ten weeks. This chapter is the catalog and the decision logic: which generative video model to reach for, *why*, and how to wire them together into a controllable pipeline rather than a slot machine.

The single most important control surface in this entire chapter — the one Yuval should internalize before anything else — is the **keyframe**, specifically **first-frame and last-frame conditioning**. Text-to-video is a wish. Keyframed image-to-video is *direction*. Almost every craft principle in the sibling chapters (the precise camera move in `07-camera-angles-and-movement.md`, the composition you locked in `06-shots-framing-composition.md`, the look you graded in `08-lenses-lighting-color.md`) only becomes executable when you can pin the start and end of a shot to images you control. So this chapter foregrounds, for every model, the answer to one question: *can I give it a start frame, an end frame, or both?*

> **Currency warning.** This is the most perishable chapter in the bible. Every fact below was verified against live sources in **June 2026** and is marked **[verified Jun 2026]** or, where I'm extrapolating from a slightly older source, **[may have changed]**. Model versions, prices, and clip limits move fast. Re-verify pricing before you quote a client a budget. Sources are listed at the end.

---

## The mental model: three jobs, not one tool

Before the catalog, the framing that prevents 90% of wasted credits. A generative video model is really being asked to do up to three separable jobs, and no single model is best at all three:

1. **Synthesis** — invent pixels that look like a real (or stylized) world. This is the "photoreal vs. plastic" axis. Veo, Sora, Kling, Seedance lead here.
2. **Motion / physics** — make objects move with believable weight, momentum, and continuity across frames. This is where most models fail (the "morphing hands," the "spaghetti gait"). Kling and Hunyuan are physics-forward; many "pretty" models are motion-weak.
3. **Control** — obey *your* constraints: a start image, an end image, a camera path, a character's identity, a line of dialogue. This is the director's axis, and it's where Runway, Luma, Pika, and MiniMax differentiate.

A "hero shot" film is usually built by using a **strong-synthesis model for the look**, a **strong-control model for the precise motion**, and a **specialist** for lip-sync or upscaling. You are an assembler, not a button-presser.

---

## The big comparison table

All figures **[verified Jun 2026]** unless flagged. "FF/LF" = first-frame / last-frame conditioning. Prices are rough, per-second or per-clip, and vary by tier and reseller; treat them as order-of-magnitude.

| Model (version) | Max clip | Max res | Native audio | Img-to-video | First frame | Last frame / keyframes | Motion realism | Prompt adherence | Camera control | Rough cost | Best at |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Google Veo 3.1** | 8 s (extendable) | 4K | **Yes** (dialogue+SFX+ambient, 48 kHz) | Yes | **Yes** | **Yes** (first+last) | High | High | Cinematic, prompt-driven | ~$0.40/s (1080p), $0.60/s (4K); Fast ~$0.15/s | Audio-synced hero shots, 4K, realism |
| **OpenAI Sora 2 / 2 Pro** | 16 & 20 s (ext. to 120 s); Pro tier to 25 s | 1080p (Pro) | **Yes** (synced dialogue/SFX/music) | Yes (input ref frame) | **Yes** | No native last-frame; storyboard/extend instead | High | Very high | Storyboard, cameo | $0.10/s (Std 720p); $0.30–0.50/s (Pro) | Long coherent scenes, dialogue, world consistency |
| **Kuaishou Kling 3.0** (2.6 still common) | 15 s (2.6: 10 s) | 4K (2.6: 1080p) | **Yes** (native lip-sync, SFX, music) | Yes | **Yes** | **Yes** (start+end, chainable) | **Best-in-class** | High | Motion Control (mocap transfer) | ~$0.30–0.70/s equiv. via resellers | Motion, physics, dance/action, lip-sync |
| **Runway Gen-4 / Gen-4 Turbo** | ~10 s/gen (125 s/mo on entry) | 1080p (4K upscale) | Limited | Yes | **Yes** | Via References + Aleph editing | Med-high | High | Strong (camera + References) | 5 cr/s (Turbo), 12 cr/s (Gen-4) | Reference-driven control, in-video editing |
| **Luma Ray3 / Ray3.14** | ~10 s | 1080p native (4K via Hi-Fi) | No (model is visual) | Yes | **Yes** | **Yes — up to 16 keyframes**, start+end | Med-high | High | Excellent native camera | ~3x cheaper than Ray3 launch | Keyframe choreography, HDR, transitions |
| **MiniMax Hailuo 02 / 2.3** | 6–10 s | 1080p native | Partial (2.3+) | Yes | **Yes** | Start+end on some endpoints | High (physics) | High | Good | Very cheap (~$0.05–0.10/s tier) | Subject-reference identity, cost efficiency |
| **Pika 2.2 / 2.5** | up to 10 s (25 s chained) | 1080p | Partial (Pikaformances) | Yes | **Yes** | **Yes — Pikaframes**, chain up to 5 | Med | Med | Limited | Cheap, credit-based | Effects, transitions, playful keyframe morphs |
| **ByteDance Seedance 2.0** (1.0 Pro common) | 15 s (1.0: 10 s) | 1080p | Yes (2.0) | Yes | **Yes** | **Yes** (start+end frame on i2v/ref endpoints) | High | High | Multi-shot native | Low (cost-leader) | Multi-shot narrative in one gen |
| **Wan 2.2 (open source)** | ~5 s/gen | 720p–1080p | Audio sub-model | Yes | **Yes** | FF/LF via ControlNet-style | High (humans) | Med-high | Via control modules | Free (your GPU) | Local, photoreal humans, full control |
| **LTX-Video 13B (open)** | ~6–10 s | 768p–1080p | No | Yes | **Yes** | Keyframe conditioning | Med | Med | Programmatic | Free (fits 16 GB) | Fast local iteration, volume |
| **HunyuanVideo 1.5 (open)** | ~5 s/gen | 720p–1080p | Avatar variant | Yes | **Yes** | Limited | **Best physics (open)** | Med | Via modules | Free (24–60 GB VRAM) | Fluid/physics sims locally |
| **HeyGen / Hedra (specialist)** | minutes (avatar) | 1080p (4K upscale) | **Yes (the point)** | Avatar/photo | Photo as identity | n/a | n/a (talking head) | n/a | Static/locked | Sub-based | Lip-sync, talking avatars |
| **Topaz / Starlight (specialist)** | n/a (post) | up to 4K+ | Preserves | n/a — upscaler | n/a | n/a | Cleans motion | n/a | n/a | Per-min | Upscale & de-artifact AI footage |

---

## Model-by-model: the why behind the spec

### Google Veo 3.1 — the audio-native realism flagship

Veo's headline differentiator is **native, synchronized audio generated *with* the video** — dialogue lip-synced to the character, sound effects matched to on-screen action, and ambient soundscape, all at 48 kHz [verified Jun 2026]. Most competitors bolt audio on or leave it to you; Veo treats sound as part of the diffusion target. It outputs **8-second clips** at up to **4K** (the 4K tier rolled out January 2026), supports **portrait and landscape**, **image-to-video**, **up to three reference images**, **video extension**, and — critically for us — **explicit first-frame *and* last-frame** conditioning [verified Jun 2026].

The 8-second ceiling is the catch. Veo is a *shot* machine, not a *scene* machine; you build longer pieces by extending or by cutting between generated shots in an editor (see `10-editing-theory.md`). Pricing on the Gemini API runs roughly **$0.40/s at 1080p, $0.60/s at 4K**, with a **Fast** tier near $0.15/s and a cheaper **Lite** tier; consumer access is via Flow credits inside Google AI Pro ($19.99/mo) and Ultra ($249.99/mo) [verified Jun 2026].

> **→ AI APPLICATION.** Veo is your default when a shot needs *integrated diegetic sound* or *4K finish*. Generate a start frame and an end frame in an image model (Imagen/Nano Banana/Flux), feed both into Veo's first+last-frame mode, and write the camera move as plain cinematographer's language in the prompt ("slow 35mm dolly-in, shallow depth of field, the actress turns to camera on the last beat"). Because audio is native, put the line of dialogue and the SFX *in the same prompt* rather than scoring in post.

### OpenAI Sora 2 — the long-coherence storyteller

Sora 2's edge is **temporal coherence and world consistency over longer durations**. Access is **API-only** as of this writing — the consumer Sora web app and all ChatGPT consumer access to Sora were discontinued on **April 26, 2026**; only the developer API remains until the September 24, 2026 sunset [verified Jun 2026]. Per OpenAI's API docs, both **sora-2** and **sora-2-pro** generate **16- and 20-second** clips, and via the **extend** mechanism (up to six 20 s continuations) reach **120 seconds** while keeping a character and environment stable [verified Jun 2026]. Resellers report the selectable fixed durations as **4/8/12 s on standard Sora 2** and **10/15/25 s on Sora 2 Pro** — the 25-second option is a Pro-tier figure, not a standard Sora 2 one. Audio is generated **in sync** (dialogue, SFX, music). **Sora 2 Pro** unlocks true **1080p** (1920×1080 / 1080×1920); standard Sora 2 caps at 720p. You can supply an **input reference image as the opening frame**, and reuse uploaded **character assets** for consistency [verified Jun 2026].

The control gap: Sora has **no native last-frame** target the way Veo/Kling/Luma do. Its control philosophy is **storyboard + extend + cameo/character upload** rather than first+last interpolation. API pricing: **~$0.10/s** standard (720p), **$0.30–0.50/s** Pro depending on resolution, with a 50% batch discount [verified Jun 2026]. **Important:** the Sora 2 / 2 Pro API is scheduled to **sunset on September 24, 2026** [verified Jun 2026] — assume a Sora 3 transition is coming; **[may have changed]** by the time you read this.

> **→ AI APPLICATION.** Reach for Sora when you need a *continuous performance* — a character walking and talking through a space for 15–20 s without a cut, where Veo's 8-second wall would force an edit. Lock the opening frame with `input_reference`, upload a character asset for identity, then use the storyboard panel to steer beats. Because there's no last-frame pin, design the shot so the *ending pose is implied by the action*, not by a hard target.

### Kuaishou Kling 3.0 — the motion and lip-sync king

If a shot lives or dies on **motion realism** — a fight, a dance, a sprint, cloth and hair physics, a face that actually emotes — Kling is the strongest dedicated answer in 2026. **Kling 3.0** (launched Feb 4, 2026; Motion Control launch March 2026) generates **3–15 second** clips at up to **native 4K, 60 fps** (up from Kling 2.6's 48 fps), with **native audio** (dialogue, SFX, music) and **physics simulation** [verified Jun 2026]. The widely-used **Kling 2.6** (10 s, 1080p, 48 fps, native lip-sync) is still common because resellers lag [verified Jun 2026].

Two director-grade features: **start-frame and end-frame control that chains into longer continuous scenes**, and **Kling 3.0 Motion Control**, which **extracts a motion sequence from a reference video (3–30 s) and transfers it onto a static image or new clip** — full-body mocap, hand gestures, facial expressions, choreography [verified Jun 2026]. Note that the Motion Control mocap-transfer path outputs at up to **720p**, distinct from the 4K base text-to-video/image-to-video pipeline. That is the closest thing to *performance capture* in a consumer text-to-video tool.

> **→ AI APPLICATION.** For an action or dance hero shot: shoot (or generate) a *reference motion clip*, generate your stylized character as a still, then use Kling Motion Control to drive the still with the reference motion. For dialogue, Kling's native lip-sync means you can drive mouth shapes from a script line directly. Use start+end frames to chain two Kling clips into one continuous camera move across a cut point.

### Runway Gen-4 / Gen-4 Turbo — the control-and-edit workbench

Runway's bet is **post-generation control**, not just generation. **Gen-4** and the cheaper **Gen-4 Turbo** support image-to-video with **References** (feed character/style/location images for consistency), camera control, and character performance [verified Jun 2026]. The standout is **Aleph** — an *in-video editing* model: change weather, relight, remove or insert objects, restyle, all on already-generated footage. Pricing: **Gen-4 Turbo = 5 credits/s, Gen-4 = 12 credits/s**; plans run Standard ($12/mo, 625 cr) → Max ($76/mo, 9,500 cr) [verified Jun 2026]. Note: **Gen-4 Aleph (v1) is deprecated, sunsetting July 30, 2026; migrate to Aleph 2.0** [verified Jun 2026] — **[may have changed]**.

Runway's first-frame support is solid; its "last-frame" story is handled through References and Aleph editing rather than a pure interpolation slider — slightly less literal than Luma/Pika but more *editable* after the fact.

> **→ AI APPLICATION.** Use Runway when the workflow is iterative and *fixable*: generate a rough shot, then Aleph-edit it toward the storyboard (relight to match `08-lenses-lighting-color.md`, swap a prop, change the time of day) instead of re-rolling and praying. References is your character-consistency lever across a multi-shot sequence.

### Luma Ray3 / Ray3.14 — the keyframe choreographer

Luma is the **keyframe specialist** and the one most aligned with Yuval's first/last-frame priority. Ray3 accepts **start *and* end keyframes** and generates the transition between them; the **Multi-Keyframe** feature — which landed with **Ray3.2** — lets you set **up to 16 keyframes inside a single clip**, directing what changes, what holds, and how the shot resolves [verified Jun 2026]. Ray3 also delivers **native 16-bit HDR** (exportable as 16-bit EXR for pro grading pipelines) and **Ray3 Modify** brings start/end-frame control into a *video-to-video* workflow for performance editing. **Ray3.14** added native 1080p, 4x speed, better adherence, and ~3x lower cost — but traded away **character reference** (and native audio) for that speed/cost win, so reach back to an earlier Ray3 sub-version when you need identity locking [verified Jun 2026]. Audio is not the model's focus — treat Luma as a *picture* tool and score separately.

> **→ AI APPLICATION.** Luma is the precision tool for *exactly* the move you storyboarded. Generate 3–16 keyframe stills (opening composition, mid-beat, ending pose), drop them on Luma's timeline in order, and the model interpolates a single continuous shot that hits every mark. This is the cleanest way to get "a precise camera move that ends on a specific pose" — see the decision tree below.

### MiniMax Hailuo 02 / 2.3 — the cost-efficient identity-keeper

Hailuo's reputation is **best-in-class physics-per-dollar** and a strong **subject-reference** mode: feed a reference face/character image and it maintains that identity across the clip [verified Jun 2026]. It outputs **native 1080p** (Pro; standard offers 768p/512p), **6–10 second** clips, with image-to-video and first-frame support; newer **2.3** adds audio [verified Jun 2026]. The value proposition is volume: it's one of the cheapest credible models, which makes it ideal for *exploration* and *consistent-character* batch work.

> **→ AI APPLICATION.** When you need the *same character* across twenty shots on a budget, lock a reference image and run Hailuo for identity continuity, then promote your hero shots to Veo/Kling for the finish. Use it as the cheap "draft pass" of a two-tier pipeline.

### Pika 2.2 / 2.5 — the effects and transition playground

Pika is the **creative-effects** model. **Pikaframes** is its keyframe system: define a **start and end image** and it interpolates between them, **chaining up to 5 keyframes for up to ~25 seconds** [verified Jun 2026]. Its signature toys — **Pikaffects** (melt, explode, inflate, "cake-ify"), **Pikadditions** (insert an AI element into real footage), **Pikaswaps**, and **Pikaformances** (audio-driven performance) — make it the go-to for stylized transitions and viral effect shots rather than photoreal drama. Output is **1080p, up to 10 s** per base gen [verified Jun 2026].

> **→ AI APPLICATION.** Use Pikaframes for *transformation* shots — a product morphing, a face aging, an impossible match-cut between two stills you generated. Define both ends precisely and let Pika handle the impossible middle. For straight realism, prefer Veo/Kling.

### ByteDance Seedance 2.0 / 1.0 Pro — native multi-shot in one prompt

Seedance's unique trick is **native multi-shot generation**: a single prompt yields a clip with **2–3 shot changes** (long → medium → close-up) and natural transitions [verified Jun 2026]. **1.0 Pro** does **1080p, 10 s**; **2.0** extends to **15 s** with multi-shot storytelling and audio. Combined with ByteDance's scaling infra (the merged Pixeldance + Seaweed efforts), it's a cost-leader for *micro-scenes*.

> **→ AI APPLICATION.** When a beat needs internal coverage (establishing → reaction → detail) but you don't want to direct three separate generations, prompt Seedance for the whole mini-scene. Use it to rough out coverage, then re-shoot the keepers in a higher-control model.

### Open source — Wan 2.2, LTX-Video 13B, HunyuanVideo 1.5

For local, private, unlimited-iteration work on Yuval's own GPUs (relevant given the local-AI-stack memory): **Wan 2.2** is the first open-source **MoE** video model with sub-models for text-to-video, image-to-video, character animation, and audio — best open photoreal *humans* [verified Jun 2026]. **LTX-Video 13B** is the speed/accessibility champion and **the only one that fits comfortably on a 16 GB card** — ideal for volume iteration [verified Jun 2026]. **HunyuanVideo 1.5** has the **best open physics** (water, smoke, cloth) but is VRAM-hungry: 60 GB+ for full precision, ~24 GB quantized [verified Jun 2026]. All three support image-to-video and, via ControlNet-style conditioning, first-frame (and varying degrees of last-frame/keyframe) control. NVIDIA is the path of least pain; ROCm support was still unstable as of April 2026 **[may have changed]**.

> **→ AI APPLICATION.** On the 4090 in the local stack, **LTX-Video** is your fast draft loop and **Wan 2.2** your photoreal-human pass; reserve cloud Veo/Kling for finals. Open models also give you *programmatic* keyframe control (scripted batches, frame conditioning) that hosted UIs don't expose — the right tool when you're building a *skill*, not clicking a website.

### Specialists — lip-sync and upscaling

Two jobs the generalists do poorly. **Lip-sync / talking avatars:** **HeyGen** (Avatar IV) and **Hedra** turn a photo + audio into a synced talking head; independent tests rate **Hedra's lip-sync ~9/10**, though Hedra video export peaks at 720p (4K via its "Super Genius" upscaler) [verified Jun 2026]. **Upscaling / de-artifacting:** **Topaz** — and HeyGen's upscaler **powered by Topaz Starlight Precise 2.5** — is *purpose-tuned for generative footage*, reconstructing texture and fixing the softness/aliasing that naive upscalers amplify [verified Jun 2026].

> **→ AI APPLICATION.** Pipeline order matters: generate the picture (Veo/Kling), do any restyle/edit (Runway Aleph), *then* upscale last (Topaz/Starlight) so you're not amplifying artifacts you'll later edit. For a presenter saying exact lines, drive lip-sync in Hedra/HeyGen rather than fighting a text-to-video model's mouth.

---

## The decision tree

Read top-down; stop at the first match.

1. **Need a presenter speaking exact scripted lines (talking head)?** → **Hedra** (best sync) or **HeyGen** (avatar ecosystem). Upscale with **Topaz** after.
2. **Need integrated dialogue + SFX + a 4K hero shot?** → **Veo 3.1** (first+last frame, native 48 kHz audio, 4K).
3. **Need a precise camera move that *ends on a specific pose*?** → **Luma Ray3** multi-keyframe (up to 16), or **Veo 3.1** first+last, or **Pika Pikaframes** for stylized morphs. Pick Luma for realism, Pika for effects.
4. **Need heavy motion / action / dance / mocap transfer?** → **Kling 3.0** (Kling 3.0 Motion Control, best physics, native lip-sync).
5. **Need a single continuous 15–20 s performance, no cut?** → **Sora 2 Pro** (extend to 120 s, world coherence).
6. **Need internal coverage (multi-shot mini-scene) from one prompt?** → **Seedance 2.0**.
7. **Need to *fix* a shot after generating (relight, swap prop, restyle)?** → **Runway Gen-4 + Aleph 2.0**.
8. **Need the same character across many cheap shots?** → **MiniMax Hailuo** subject-reference.
9. **Need local / private / unlimited iteration?** → **LTX-Video** (16 GB, fast) → **Wan 2.2** (photoreal humans) → **HunyuanVideo** (physics, big VRAM).

---

## → AI APPLICATION (chapter-level): the keyframe-bridge pipeline

The recommended generation strategy — and the one this bible's skill should default to — is a **two-stage, keyframe-bridge pipeline** that separates *composition* from *motion*:

**Stage 1 — Author keyframes in an image model.** Use a high-control still-image model (Nano Banana 2 / Gemini image, Flux, Imagen, Midjourney) to generate your **first frame** (the opening composition, lit and graded to your `06`/`08` specs) and your **last frame** (the ending pose/framing). For complex moves, generate intermediate keyframes too. You now control composition, character identity, palette, and pose *deterministically* — none of it left to the video model's imagination.

**Stage 2 — Interpolate with a video model that accepts those keyframes.** Hand the frames to a model whose control surface matches the shot:

| You have | Use | Why |
|---|---|---|
| First + last frame, want realism + 4K + sound | **Veo 3.1** | native first+last, native audio, 4K |
| 3–16 ordered keyframes, want one continuous move | **Luma Ray3** | up to 16 keyframes in one clip |
| First + last, want stylized morph/effect | **Pika Pikaframes** | chains up to 5, effects-native |
| First + last + a reference *motion* | **Kling 3.0 Motion Control** | transfers mocap onto your stills |
| First + last, want editability after | **Runway Gen-4 + Aleph** | fix the result without re-rolling |
| First + last, fully local | **Wan 2.2 / LTX-Video** | frame conditioning on your GPU |

**Stage 3 — Finish.** Optional Aleph edits for continuity, lip-sync specialist for any to-camera dialogue, then **Topaz/Starlight upscale last**.

The reason this works is the same reason storyboards work in traditional film: **the expensive, uncontrollable step (motion synthesis) is bracketed by two cheap, fully-controllable steps (the still frames).** You are not asking the model to *invent* your shot; you are asking it to *connect two images you already approved*. That is the difference between directing and gambling — and as of mid-2026, Veo 3.1, Luma Ray3, Pika, Kling 3.0, Seedance 2.0, and the open Wan/LTX models all support it natively. Sora is the notable exception (no literal last-frame), which is precisely why you reach for it only when you want *continuity over a long take* rather than *a pinned ending*.

---

## Sources

- [Veo 3.1 — Google DeepMind](https://deepmind.google/models/veo/)
- [Generate videos with Veo 3.1 — Gemini API docs](https://ai.google.dev/gemini-api/docs/video)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Veo 3.1 Pricing Guide 2026 — AI Free API](https://www.aifreeapi.com/en/posts/veo-3-1-pricing)
- [Sora 2 — OpenAI](https://openai.com/index/sora-2/)
- [Video generation with Sora — OpenAI API docs](https://developers.openai.com/api/docs/guides/video-generation)
- [Sora 2 Model — OpenAI platform](https://platform.openai.com/docs/models/sora-2)
- [Sora 2 API Pricing & Sunset Guide — CostGoat](https://costgoat.com/pricing/sora)
- [Sora 2 release notes — OpenAI Help](https://help.openai.com/en/articles/12593142-sora-release-notes)
- [Kling 3.0 Motion Control Release — KlingAI](https://klingaio.com/blogs/kling-3-motion-control-release)
- [Kling 2.6 — Media.io](https://www.media.io/ai/image-to-video/kling-2-6)
- [Kling video models essentials — Scenario](https://help.scenario.com/en/articles/kling-video-models-the-essentials/)
- [Runway API pricing & costs](https://docs.dev.runwayml.com/guides/pricing/)
- [Runway pricing](https://runwayml.com/pricing)
- [Gen-4 Aleph pricing & specs — CloudPrice](https://cloudprice.net/models/runway-gen-4-aleph)
- [Ray3 — Luma](https://lumalabs.ai/ray3)
- [Ray3 Modify (start/end frame) — Luma](https://lumalabs.ai/news/ray3-modify)
- [Luma Ray3 HDR — CineD](https://www.cined.com/luma-ai-ray3-reasoning-video-model-with-10-12-and-16-bit-hdr-in-adobe-firefly/)
- [MiniMax Hailuo 02 — MiniMax](https://www.minimax.io/news/minimax-hailuo-02)
- [Hailuo 02 image-to-video — fal.ai](https://fal.ai/models/fal-ai/minimax/hailuo-02/pro/image-to-video)
- [Pika v2.2 Pikaframes — fal.ai](https://fal.ai/models/fal-ai/pika/v2.2/pikaframes)
- [Pika 2.2 release — AIbase](https://www.aibase.com/news/15808)
- [Seedance 1.0 — ByteDance Seed](https://seed.bytedance.com/en/seedance)
- [Seedance 2.0 — Artlist](https://artlist.io/ai/models/seedance-2-0)
- [Open-source AI video comparison 2026 — AI Magicx](https://www.aimagicx.com/blog/open-source-ai-video-models-comparison-2026)
- [Local AI video: Wan 2.2, LTX, Hunyuan — Local AI Master](https://localaimaster.com/blog/local-ai-video-generation)
- [HeyGen vs Hedra lip-sync 2026 — lipsync.com](https://lipsync.com/compare/heygen-vs-hedra)
- [HeyGen AI Upscaler (Topaz Starlight)](https://www.heygen.com/apps/ai-upscaler)
