# AI Storyboarding, Prompt Anatomy & First/Last-Frame Keyframing

Every previous chapter taught you what a good shot *is* — its size, its angle, its light, its place in the cut. This chapter is where you make the machine produce it on purpose instead of by luck. It is the hands-on prompt-engineering core of the bible, and it rests on one strategic reframing that separates amateurs from people who ship watchable films: **stop asking a video model to imagine your shot, and start handing it the answer.**

The central technique here — generate a precise first frame and a precise last frame as stills, then let a video model interpolate the motion between them — is the single highest-leverage quality move available in current AI filmmaking. It converts the unsolved, hallucinatory problem of "text → 5 seconds of correct cinema" into two solved problems ("text → one correct still," which image models are excellent at) plus one tractable problem ("morph between two known images," which video models are now genuinely good at). Most of this chapter builds toward executing that well. But first you have to know what a strong still prompt even looks like, so we start there.

A first principle to hold throughout: **the model is a sampler over its training distribution, not a director.** Anything you do not specify, it fills with the statistical average of its data — which is why unguided AI footage looks the same bland way (centered, eye-level, medium shot, soft daylight, slightly slow-motion drift). Prompting is the act of *narrowing the distribution* until only the shot you want is likely. Every term you add is a constraint. That intuition explains everything below.

---

## 1. Storyboarding With AI

A **storyboard** is a sequence of still frames — one per shot — that previsualizes the film before any motion exists. Its job is not to be pretty; it is to *commit decisions* (framing, blocking, eyeline, lighting key) so that the expensive step (video generation) executes a plan rather than improvises one. In traditional production the storyboard saves money on set. In AI production it saves you from burning 40 video generations discovering that your shot doesn't cut together. (Cross-ref `06-shots-framing-composition.md` for the spatial-continuity rules your board must respect, and `10-editing-theory.md` for why a board that ignores eyeline and the 180° line produces footage that won't edit.)

### From shot list to board

The pipeline is linear and worth doing in order:

1. **Shot list first.** Before any image, write the rows: shot number, size, angle, subject, action, the single emotional beat. This is the SHOTS-NOT-SCENES discipline from `06` — you never prompt "a scene of two men arguing in a bar"; you prompt *each shot* (WS bar establishing → MCU man A leaning in → CU man B's jaw tightening → insert: glass set down hard). A scene is an editorial illusion built from shots; the model can only render one shot at a time, so the shot is your atomic unit.
2. **Generate one board frame per shot row**, using the still-prompt anatomy in §2.
3. **Lock style across the board** (the hard part — see below).
4. **Assemble into an animatic** (timing + voice) to test the cut before committing to video.

### Style consistency across the board — the real problem

The defining failure of AI storyboards is that frame 3 looks like a different film than frame 7 — different color science, different rendering, a character whose face drifts. Consistency is not one knob; it is a stack:

| Lever | What it locks | Current tool syntax (verify — as of mid-2026) |
|---|---|---|
| **Style reference / code** | Color science, grain, rendering "look" | Midjourney `--sref <code or image URL>` (and `--sw` to weight its strength); a single shared `--sref` across the whole board is the strongest single move |
| **Character reference** | A specific person's identity across shots | Midjourney `--cref <url> --cw <0–100>` (cw 0 = face only, 100 = face+clothes+hair); Nano Banana 2 / Gemini image multi-reference (up to ~14 inputs) for compositing the same face into new shots |
| **Seed reuse** | Coarse layout/composition family | Reusing the same `--seed` holds the random starting point; useful for variations of one setup |
| **Single base plate** | Lighting + environment continuity | Generate one master location still, then *edit* it (inpaint/reframe) for each angle rather than re-generating from scratch |

The professional habit: pick ONE style reference image and ONE character reference, and pass them to **every** frame. The bland-mean problem (§intro) is also a friend here — because the model regresses to a stable look, a shared `--sref` makes that stability work *for* continuity instead of against you.

→ **AI APPLICATION.** Build the board in an image model with explicit reference locking, not a video model. Concretely: (a) generate or choose a 1-image style anchor; (b) generate your hero character as a clean, well-lit reference portrait; (c) for each shot-list row, prompt the still with the anatomy in §2 *plus* the shared `--sref` and `--cref`. For faces that must be identical across shots, Nano Banana 2 / Gemini-3.x image (multi-reference compositing, accurate in-image text) currently beats Midjourney for *exact* identity transfer; Midjourney currently wins on cinematic "look." A pragmatic split: design the look in Midjourney, then re-render identity-critical frames with Nano Banana 2 using the Midjourney frame as a reference. (Tools/versions verify — as of mid-2026.)

### Building an animatic from stills

An **animatic** is the storyboard set in motion at correct timing — stills held for their shot duration, with scratch voiceover and temp music — so you can *feel the edit* before generating a second of real video. This is the cheapest possible test of pacing and it catches dead beats that look fine as static frames.

The minimal AI animatic recipe:

- **Ken Burns moves** on each still — a slow push-in or pan across the frame. This is a 2-D crop animation, not real 3-D motion; it gives the eye something alive while the still does the storytelling. (It is also a preview of the camera move you'll later ask the video model to perform — see §4.)
- **TTS scratch track** for dialogue/VO so timing is real, not guessed. Generate lines with a voice model (ElevenLabs, etc.), drop them on the timeline, and cut the held-still durations to match the line lengths.
- **Hold-time discipline**: a still on screen should last roughly as long as the shot will in the final cut. If your board has a 1.5s reaction and a 6s establishing, build that asymmetry into the animatic — it is the rhythm test (cross-ref `10-editing-theory.md`).

→ **AI APPLICATION.** For a code-driven animatic, an HTML composition (HyperFrames) gives frame-accurate control of hold times, Ken Burns transforms, crossfades, and synced TTS — far more precise than slideshow apps, and the same project can later swap each still for its generated video clip. Generate TTS first, read its exact duration, then set each still's on-screen time to match the corresponding line. The animatic's per-shot durations become your *generation spec*: now you know each clip needs to be (say) 4s, which tells you how far apart your first and last frames should be.

---

## 2. Prompt Anatomy

A prompt is not a sentence; it is a *stack of constraints in priority order*. Both image and video models weight earlier tokens more heavily, so the order is load-bearing, not stylistic.

### The canonical IMAGE prompt (for a cinematic still)

Order matters. The reliable structure, front-to-back:

**[Shot size] + [subject + key visual detail] + [action/pose] + [camera angle] + [lens] + [lighting] + [color/mood] + [composition] + [style/quality anchors] + [technical tags/parameters]**

Annotated example:

> `Medium close-up of a tired detective, mid-40s, stubble, loosened tie [subject+detail], leaning back exhaling smoke [action], low-angle [angle], shot on 35mm anamorphic, shallow depth of field [lens], single hard key from a desk lamp, deep shadows, chiaroscuro [lighting], teal-and-amber, smoky haze, melancholy [color/mood], rule-of-thirds, negative space camera-left, neon sign bokeh background [composition], 1970s neo-noir, cinematic film still, Kodak Vision3, fine grain [style anchors] --ar 2.39:1 --style raw [tech tags]`

Why each block earns its place:

| Block | What it constrains | Failure if omitted |
|---|---|---|
| Shot size | How much of the human figure is in frame | Defaults to medium, eye-level |
| Subject + detail | The thing + the specifics that prevent generic faces | Stock-photo person |
| Action/pose | Implied energy; also the *motion seed* for video | Static mannequin |
| Camera angle | Power/psychology (low = dominant) — see `07` | Defaults to eye-level |
| Lens | DOF, compression, distortion character — see `08` | Flat, deep-focus "everything sharp" look |
| Lighting | The single biggest lever on "cinematic" — see `08` | Flat ambient daylight |
| Color/mood | Palette + emotional register | Muddy, unintentional grade |
| Composition | Where things sit in the rectangle — see `06` | Centered, balanced, dull |
| Style anchors | The "look" (era, stock, director) | Generic "AI render" sheen |
| Tech tags | Aspect ratio, rendering mode | Wrong delivery ratio |

The two most under-used blocks by beginners are **lens** and **lighting** — they are exactly what makes footage read as film rather than render, and they are the cheapest words to add.

### The canonical VIDEO prompt

Video adds the time dimension, so the structure changes. Lead with the *state*, then describe *change over time*, then *camera*, then *pacing*, then *audio*:

**[Start state / first frame description] + [motion/action that unfolds] + [camera move] + [timing/pacing] + [audio cue]**

Annotated example (Veo-style; Veo's own recommended order is cinematography → subject → action → context → style → ambiance):

> `A detective sits motionless at a desk in a dark office [start state]. He slowly turns his head toward the door as it creaks open [motion/action]. Camera pushes in slowly from medium to close-up [camera move]. Deliberate, tense pacing, no sudden cuts [timing]. Audio: distant rain, a single floorboard creak, low sustained drone [audio cue].`

Key differences from image prompts: you must describe **what changes**, not just what *is*; you must name the **camera move as a verb over time** ("pushes in," "cranes up," "whip-pans") not a static angle; and on audio-native models (Veo 3.1, Kling 3.0) the audio cue is part of the generation, not a separate pass.

### Negative prompts — what they actually do (and don't)

A **negative prompt** tells the model what to *avoid*. It is widely misunderstood. The honest version:

- In diffusion-style models, a negative prompt is a second conditioning vector that the sampler is pushed *away* from. It genuinely suppresses concepts — `--no people, text, watermark` reliably reduces those.
- It is **subtractive steering, not deletion.** It biases probability; it does not guarantee absence. "--no blur" does not force sharpness if the rest of your prompt implies motion blur.
- In Midjourney, `--no X` is mathematically equivalent to giving `X` a weight of `-0.5` (per Midjourney's own docs). So negatives and weights are the same mechanism.
- **Overstuffing negatives backfires.** A wall of "deformed, ugly, bad anatomy, extra fingers..." (the old Stable Diffusion ritual) wastes conditioning capacity and can drag the image toward an averaged, lifeless look. Modern models need few or no negatives. Use them surgically: exclude a *specific* recurring intruder, not a generic quality-spell.

### Weighting / emphasis syntax

Weighting lets you say "this part matters more." It is the precision tool for resolving prompt conflicts:

| System | Syntax | Notes (verify — as of mid-2026) |
|---|---|---|
| Midjourney multi-prompt | `concept::2 other::1 thing::0.5` | Number after `::` = relative weight; total must sum positive; **flagged as not fully compatible with V7** — on V7 steer via `--sref`/`--sw`/personalization instead |
| Midjourney image weight | `--iw 0.5–2` | How strongly an uploaded image vs the text prompt drives the result |
| Midjourney negative | `--no X` ≡ `X::-0.5` | Subtractive |
| Stable-Diffusion family | `(word:1.3)` / `(word:0.7)` | Parenthetical numeric weight; engine-dependent |

The practical lesson: when two terms fight ("rain" vs "golden hour"), don't add more words — *re-weight* the one you want to win, or remove the loser.

→ **AI APPLICATION.** Treat the prompt as an ordered constraint stack and **front-load what matters most** to that shot — if framing is the point, lead with shot size; if identity is the point, lead with the character reference. Keep negatives minimal and specific. When a model ignores a term, first try *moving it earlier* or *weighting it up* before rewriting the whole prompt. Note the V7 caveat: if you depend on `::` weights, either stay on Midjourney V6.x or switch your emphasis strategy to references and style weight on V7. (Syntax/versions verify — as of mid-2026.)

---

## 3. The First-Frame / Last-Frame Keyframe Technique

This is the core of Yuval's quality goal, so we go deep. (For which models expose this and at what price, cross-ref `15` — the model-capability chapter.)

### The intuition: don't let the model imagine — let it interpolate

Text-to-video asks the model to do three hard things at once: invent a *correct first frame*, invent a *correct trajectory of motion*, and invent a *correct ending* — all from a sentence, all without you seeing any of it until it's rendered. Each is a place for hallucination, and the errors compound. Resolution suffers too: a model spending capacity inventing composition has less left for fidelity.

The keyframe technique decomposes the problem:

1. Generate a **high-resolution FIRST frame** as a still — full §2 control over composition, character, lighting, framing. You *see* it and approve it.
2. Generate a **high-resolution LAST frame** as a still — the guaranteed end pose, end composition, end lighting.
3. Hand **both** to a video model and let it **interpolate** the motion in between.

Now the model is no longer guessing where to start or end. It is solving the much easier problem: "given these two known images, produce a plausible motion that connects them." This is why it yields:

- **Higher resolution / fidelity** — your endpoints are full-res stills made by an image model (which out-resolves video models), and the video model interpolates rather than inventing detail from nothing.
- **Composition control** — you compose both frames by hand; nothing is left to the model's bland mean.
- **A guaranteed ending** — the last frame *is* the last frame. This is enormous for editing: you can design the last frame of clip A to match the first frame of clip B, producing seamless cuts and continuity the model could never stumble into on its own (cross-ref `10-editing-theory.md`).

### Designing the two frames so interpolation *implies* the move

The magic is that the camera move and the action are not prompted as motion at all — they are **implied by the difference between the two stills.** The model reads the delta and fills it. So you design the delta deliberately:

| Desired result | First frame | Last frame |
|---|---|---|
| Push-in (dolly in) | Subject in MS, more environment | Same subject in CU, tighter, same axis |
| Pull-out / reveal | CU on a detail | WS showing the detail's surprising context |
| Pan left→right | Subject framed camera-right | Same world, subject now camera-left |
| Crane up | Eye-level on subject | High angle looking down on same subject |
| A character sits down | Standing, hand on chair | Seated, settled |
| Sunset / time passing | Daylight version of a locked composition | Golden/night version of the *same* composition |
| Object transformation | Closed flower | Bloomed flower (same plant, same frame) |

The discipline: **change exactly the variables that encode your intended motion, and hold everything else identical.** A push-in is *only* a change in framing scale — so lock subject, lighting, color, and background, and change only the crop. The more variables you hold constant, the cleaner the interpolation.

### The central pitfall: too-different frames cause morphing

The single biggest failure mode is endpoints that differ in *too many* dimensions at once. If the first and last frame have different lighting, different background, AND a different subject pose, the model has no clean trajectory and resolves the ambiguity by **morphing** — that liquid, melting, identity-warping artifact that screams "AI." The model is interpolating in latent space, and if the two points are far apart with no shared structure, the path between them goes through nonsense.

Mitigations (sourced from current Kling/Veo practice):

- **Share palette, tone, and setting** between the two frames. Generate them from the same reference/`--sref` so their color science matches.
- **Keep one anchor constant** — same character (use character reference on both), same key light direction, same background plate where possible.
- **Add continuity cues to the prompt**: "preserve shape," "maintain scale," "keep colors consistent" measurably reduce warping.
- **Increase duration** if the transition feels abrupt — more frames = more room for a smooth morph between distant endpoints.
- **Don't over-reach in one clip.** If you need a big change (day→night AND a 180° camera move AND a costume change), split it into two clips with an intermediate keyframe rather than forcing one impossible interpolation. Runway and Luma support an explicit *middle* keyframe for exactly this.

### Which models support it (verify — as of mid-2026)

| Model | Feature name | Notes |
|---|---|---|
| **Kling O1** | First-Frame → Last-Frame | Purpose-built endpoint interpolation; ~ $0.112/sec; excels at timelapse/morph/narrative transitions |
| **Runway Gen-4 / Gen-4.5** | Keyframe Control (First, Last, First+Last, **+ middle**) | API-exposed; strong creative control, motion brush, camera control |
| **Luma Ray 3** | Keyframes (first + last + intermediate) | HDR output; structured multi-shot narrative |
| **Veo 3.1** | Frames-to-Video / first+last frame conditioning + "Ingredients" reference images | Audio-native; 1080p/4K upscale; ingredients map a face/style across all frames to kill morphing |

Cross-ref `15` for the up-to-date capability and price matrix.

→ **AI APPLICATION.** Make first/last-frame keyframing your **default**, not your special-case. Workflow: (1) build both endpoint stills in your image model with shared `--sref`/`--cref` so they're already color- and identity-matched; (2) upscale both to max resolution (§5); (3) load both into Kling O1 / Runway Gen-4.5 / Veo 3.1 / Luma Ray 3 as start+end; (4) write the video prompt to *describe the motion you designed into the delta* ("slow dolly in, no other movement") plus continuity cues ("preserve face, maintain lighting"); (5) if it morphs, the diagnosis is almost always "endpoints too different" — pull them closer or add a middle keyframe. (Models/prices verify — as of mid-2026.)

---

## 4. Camera Moves by Endpoints

A corollary worth stating on its own: **you can author a specific camera move purely by how you frame the two stills**, with little or no reliance on the model's unreliable "camera move" prompt vocabulary. Text camera directions ("dolly in," "orbit left") are interpreted loosely; an endpoint pair is unambiguous geometry.

To get an orbit/arc, generate the first frame from one position and the last frame of the *same subject and lighting* from a position ~20–30° around it — the model interpolates the arc. To get a rack focus, keep the camera locked and shift which plane is sharp between frames. To get a reveal, the last frame simply shows what the first frame hid. The Ken Burns moves you built into your animatic (§1) are the 2-D rehearsal of these 3-D endpoint moves.

→ **AI APPLICATION.** When a model keeps refusing a camera move you prompt in text, stop prompting it in text — *bake it into the endpoints*. This is more reliable than motion-brush or camera-control sliders for clean, specific moves, and it composes with §3 perfectly. Reserve text camera prompts for moves you can't encode geometrically (handheld shake, organic drift). (Cross-ref `07-camera-angles-and-movement.md` for what each move *means* so your endpoint deltas are motivated, not gratuitous.)

---

## 5. Resolution & Quality Control

Resolution is won in the *order of operations*, not in one setting.

**The quality pipeline:** generate stills at **max native resolution** → **upscale the stills** → animate from the upscaled keyframes → (if needed) **upscale the video** → (if needed) **interpolate frames** for smoothness or slow-motion.

- **Stills carry the resolution.** Image models out-resolve video models, so a film whose keyframes are high-res, upscaled stills starts from a higher fidelity floor than any pure text-to-video clip. Upscale stills *before* animating (Midjourney upscale, Magnific, Topaz Photo, Gigapixel) — `--hd` / high-res modes where available.
- **Upscaling video** is a separate post step. Topaz Video AI (subscription as of late 2025, ~$299/yr) is the standard for AI-footage upscaling; some models (Veo 3.1) now offer native 1080p/4K upscale in-pipeline.
- **Frame interpolation for slow-motion and smoothness.** Interpolation synthesizes *new* in-between frames to raise frame rate — 24/30fps → 60/120fps, or up to ~16× slow-motion. Topaz Video AI's Apollo/Chronos/Aion models, or free open-source **Flowframes** (RIFE / DAIN / FLAVR backends). Use this to make AI footage feel smooth and to create slow-motion from normally-paced clips without the model having to generate slow-mo (which it does poorly and at low res).

A subtle but important point: frame interpolation is *also* the same family of math as the keyframe interpolation in §3 — RIFE interpolating two adjacent video frames and Kling O1 interpolating your two keyframes are cousins. The difference is that your keyframes are arbitrarily far apart and content-rich, which is why the video model (trained on motion) does it and a simple optical-flow tool cannot.

→ **AI APPLICATION.** Lock this order and never animate a low-res keyframe to "save a step." Generate keyframes large → upscale → animate → (Topaz) upscale the clip if the model output is soft → (Flowframes/Topaz) interpolate to 60fps for smoothness or for slow-motion beats. For a hero slow-motion shot, generate at normal speed and interpolate 4–8×; the result out-resolves any model's native slow-mo. (Tools/prices verify — as of mid-2026.)

---

## 6. Copy-Paste Template Library

Fill the brackets. Order is deliberate (§2). Replace `<SREF>`/`<CREF>` with your locked style/character references.

**A) Image keyframe (still) template**

```
[SHOT SIZE] of [SUBJECT + 2–3 specific visual details], [ACTION/POSE],
[CAMERA ANGLE], shot on [LENS / focal length], [DEPTH OF FIELD],
[LIGHTING: key direction + quality + contrast], [COLOR PALETTE + MOOD],
[COMPOSITION: placement + negative space], [STYLE ANCHOR: era / stock / look],
cinematic film still, fine grain --ar [RATIO] --sref <SREF> --cref <CREF> --cw [0-100] --style raw
```

**B) Video interpolation (first + last frame) template**

```
First frame: [link/desc of START still].
Last frame: [link/desc of END still].
Motion: [ONLY the change between them, stated as the action — e.g. "subject slowly turns head toward camera"].
Camera: [the move your endpoint delta implies — e.g. "slow dolly in, no other camera movement"].
Pacing: [deliberate / brisk / real-time]; no cuts.
Continuity: preserve [face / shape / scale], maintain lighting and color.
Audio: [ambient bed + 1–2 specific sounds].
```

**C) Camera-move-by-endpoints recipes**

```
PUSH-IN:    First = MS of subject (more room). Last = CU of SAME subject, same axis/light. Prompt: "slow dolly in, locked subject."
PULL-BACK:  First = CU on detail.            Last = WS revealing context.            Prompt: "smooth dolly out, reveal environment."
ORBIT:      First = subject from angle A.     Last = SAME subject from angle A+25°, same light. Prompt: "camera arcs around subject."
CRANE UP:   First = eye-level on subject.     Last = high angle on SAME subject.       Prompt: "crane up and over, looking down."
RACK FOCUS: First = foreground sharp/bg soft. Last = bg sharp/foreground soft, locked frame. Prompt: "rack focus, static camera."
TIME PASS:  First = day, locked composition.  Last = night, IDENTICAL composition.      Prompt: "time-lapse, sun sets, no camera move."
```

**D) Style-lock board header (prepend to every board frame)**

```
[shot-specific prompt] --sref <SREF> --sw 100 --cref <CREF> --cw 80 --ar 2.39:1 --style raw
```

The throughline of all four: you are never asking the machine to direct. You direct, in stills; the machine fills the gaps you deliberately left.

---

### Sources (verify — as of mid-2026)

- Kling O1 first/last-frame (fal.ai) — https://fal.ai/models/fal-ai/kling-video/o1/image-to-video
- Kling start/end frame consistency tips (Tona.AI, Atlabs, TheAIVideoCreator) — https://tonaai.io/blog/kling-3-start-end-frame-tutorial
- Runway Keyframe Control (Gen-3/Gen-4) — https://help.runwayml.com/hc/en-us/articles/34170748696595-Creating-with-Keyframes-on-Gen-3
- Luma Ray 3 keyframes/HDR — https://theplanettools.ai/tools/luma-ray-3
- Veo 3.1 frames-to-video + Ingredients (Google AI docs, CineD) — https://ai.google.dev/gemini-api/docs/video and https://www.cined.com/google-veo-3-1-ingredients-to-video-update-adds-native-vertical-format-4k-upscaling-and-enhanced-character-consistency/
- Best AI video models 2026 (Veo 3.1 / Kling 3.0 / Runway Gen-4.5 / Seedance) — https://www.teamday.ai/blog/best-ai-video-models-2026 and https://lushbinary.com/blog/ai-video-generation-sora-veo-kling-seedance-comparison/
- Midjourney multi-prompts, weights, --no, --iw — https://docs.midjourney.com/hc/en-us/articles/32658968492557-Multi-Prompts-Weights and https://www.whytryai.com/p/midjourney-negative-prompt
- Topaz Video AI frame interpolation (Apollo/Chronos/Aion) + Flowframes/RIFE — https://docs.topazlabs.com/video-ai/filters/frame-interpolation and https://unifab.ai/resource/ai-frame-interpolation-tools
