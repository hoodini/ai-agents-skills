# The End-to-End Production Pipeline

A film is not made once. It is made four times — on paper, in pictures, on set, and at the editing desk — and each pass throws away most of what the previous pass produced. The pipeline is the discipline that turns an idea into a deliverable without the project collapsing under its own cost. Every stage exists because a specific category of expensive mistake can be caught *cheaply* if you catch it *early*, and ruinously if you catch it late. That single economic fact — **the cost of fixing a problem rises by roughly an order of magnitude at every stage you cross** — is the reason the whole apparatus is shaped the way it is. A bad idea costs nothing to fix in development; the same flaw discovered in the color grade costs a reshoot.

The other chapters in this bible teach the *craft* of each layer: story (`01-story-structure.md`), scene construction (`03-character-and-scene-craft.md`), framing (`06-shots-framing-composition.md`), camera (`07-camera-angles-and-movement.md`), the look (`08-lenses-lighting-color.md`), cutting (`10-editing-theory.md`). This chapter teaches the *order of operations* — what gets produced when, who hands what to whom, and crucially, **what the deliverable of each stage actually is**. The deliverable matters more than the activity, because a stage is "done" when its artifact exists and is approved, not when someone feels good about the work.

For AI filmmaking, the pipeline is not optional historical baggage you get to skip because you have a model that makes video. It is the opposite. The pipeline is the **scaffold that makes AI output coherent** instead of a pile of pretty, contradictory clips. Every professional stage maps cleanly onto an AI step, and the projects that look authored rather than auto-generated are precisely the ones that respected the order. The throughline of this chapter — and its single biggest lesson — is **animatic-first discipline**: build the whole film, badly and cheaply, before you build any of it well. Hold that thought; we earn it.

---

## The Three Acts of Production

The industry divides the work into three phases plus development:

| Phase | One-line definition | Governing question |
|---|---|---|
| **Development** | Turning a notion into a script the money will back | "Is this worth making?" |
| **Pre-production** | Planning every shot before a camera rolls | "Exactly how will we make it?" |
| **Production** | Capturing the raw material (the shoot) | "Did we get it?" |
| **Post-production** | Assembling raw material into the finished film | "Does it work, and is it deliverable?" |

The deeper structural truth: **planning is front-loaded on purpose.** A feature might spend a year in development, three months in pre-production, six weeks shooting, and a year in post. The shoot — the part everyone imagines when they think "making a movie" — is the shortest, most expensive, least reversible phase. Everything before it exists to make those six weeks deterministic. Everything after it exists to rescue, refine, and finish what the six weeks produced. AI inverts the *cost* profile (your "shoot" is cheap and infinitely re-runnable) but, as we'll see, **it does not invert the value of planning** — it raises it, because an AI model with no plan will happily generate a thousand confident, mutually inconsistent shots.

---

## DEVELOPMENT — From Notion to Greenlight

### Idea → Logline → Treatment → Screenplay → Table Read

Development is a funnel of escalating commitment, where each artifact is a more expensive bet than the last, and each must survive scrutiny before the next is written.

- **The idea / premise.** A "what if." *What if a hacker discovers reality is a simulation* (The Matrix). Cheap, abundant, worthless until pressure-tested.
- **The logline.** One or two sentences naming protagonist, goal, conflict, and stakes. *"A young FBI trainee must gain the trust of an imprisoned cannibal to catch a serial killer."* The logline is a **falsification test**: if you can't state the engine of the story in a sentence, the story doesn't have an engine yet. (See `01-story-structure.md` on why dramatic question precedes plot.)
- **The treatment.** A 1–10 page prose synopsis, present tense, beat by beat, no dialogue formatting — the whole film told as a story. The treatment is where structural failures surface for the price of prose: a saggy second act is obvious here and invisible in a one-line pitch.
- **The screenplay.** Industry format is load-bearing, not cosmetic: 12-point Courier, scene headings (sluglines like `INT. KITCHEN – NIGHT`), action in present tense, centered dialogue blocks. The convention that **one properly formatted page ≈ one minute of screen time** is the entire reason the format is rigid — it makes the script a *time-estimation instrument*. A 110-page script is a 110-minute film, roughly, and that lets every downstream department budget against the page count.
- **The table read.** Cast and crew read the script aloud around a table. Its deliverable is not a document — it's **diagnostic information**: which lines are unsayable, where the energy dies, which jokes don't land. It is the first time the script is *heard* rather than read, and hearing exposes what the eye forgives.

**The deliverable of development:** a locked, formatted screenplay plus a logline and treatment that survived being said out loud.

#### → AI APPLICATION
The LLM is your development department, and its highest-value mode is **adversarial, not generative**. Don't ask a model to "write me a logline" and accept the first output — that produces the statistical mean of all loglines, which is mush. Instead, *grill* it: feed your premise and prompt the model to attack it — "List the five ways this premise is generic. What is the obligatory scene this setup promises and am I delivering it? Give me the logline a producer would reject and explain why." Use the model to generate a treatment, then run a separate critique pass with a fresh context window ("You are a script consultant who hates this draft — find the structural break"). For the screenplay, LLMs reliably produce correct Fountain or Final Draft formatting on request; ask for Fountain (plain-text screenplay markup) so the output is diffable and version-controllable. The **table read maps to text-to-speech**: pipe each character's lines through distinct ElevenLabs voices and *listen*. Hearing AI-generated dialogue read aloud catches the on-the-nose, unsayable lines that look fine on screen — the same diagnostic value as the human table read, for the cost of a TTS call. This connects directly to the scratch-audio stage of the animatic below; the table read *is* your first scratch vocal track.

---

## PRE-PRODUCTION — Planning Every Shot

This is the densest phase and the one AI filmmakers most often skip — to their ruin. Pre-production converts the script (a *literary* object) into a set of *production* documents that tell everyone exactly what to make.

### Script Breakdown

The **breakdown** is the act of reading the script and tagging every physical element each scene requires: cast, extras, props, wardrobe, vehicles, locations, special effects, stunts, animals. Each scene becomes a row in a database. The deliverable is a **breakdown sheet** per scene, which feeds everything downstream — you cannot schedule or budget what you haven't enumerated. The classic color-coded system (props in one color, wardrobe in another) exists so a glance reveals a scene's complexity.

### The Shot List

Where the breakdown is *what's in the scene*, the **shot list** is *how the scene is captured* — every individual camera setup, in order, with shot size (wide/medium/close), angle, movement, and lens. It is the director and DP translating dramatic intent into a sequence of executable images. (The vocabulary lives in `06-shots-framing-composition.md` and `07-camera-angles-and-movement.md`.)

### Storyboard → Animatic — the highest-leverage step in filmmaking

The **storyboard** is the shot list drawn — a comic-strip of the film, one panel per shot, with arrows for movement. It externalizes the director's mental image so everyone aligns on the *same* picture. Hitchcock famously claimed to have made the film entirely in storyboards, so the shoot was mere execution.

The **animatic** is the storyboard *put in time*: the panels edited into a video at their intended durations, with **scratch audio** (temp voiceover, temp music, basic sound effects) laid underneath. This is the moment the static plan becomes a watchable, low-fidelity version of the finished film — you can sit and *feel* the pacing.

This is the single highest-leverage step in the entire pipeline, and it is worth being explicit about *why*. **An animatic is the first time anyone experiences the film as a temporal object rather than a spatial one.** A storyboard shows you *what* will be on screen; an animatic shows you *how it plays* — and "how it plays" is where almost every fixable failure lives: a scene that runs too long, a beat that lands flat, a transition that confuses, a joke whose timing is wrong, an emotional turn that hasn't been earned. None of these are visible in a script or a storyboard. All of them are obvious in an animatic. The industry adage is exact: **fixing a sequence at the animatic stage costs a day; fixing it after production costs a month.** Every major animation house — Pixar, Disney, DreamWorks, Laika, Ghibli — builds animatics ("story reels") as a non-negotiable core stage, iterating the reel dozens of times before a single final frame is rendered, precisely because rendered animation is the most expensive output in film and they refuse to render anything the reel hasn't already proven works.

The reason this matters *more*, not less, for AI: your final shots are expensive and slow to generate, frequently non-deterministic, and hard to revise once you've committed to them. The animatic is where you discover the film *should be 90 seconds, not 150* before you've spent the generation budget making the wrong 150.

### Mood Boards / Look Book

A **look book** is a curated collection of reference images — palette, lighting, texture, era, faces, locations — that defines the film's visual language without describing a single shot. It's the answer to "what does this *feel* like?" and it aligns every department on tone before money is spent (see `08-lenses-lighting-color.md` on palette as thesis).

### Floor Plan & Blocking Diagram

The **floor plan** is an overhead map of the set with furniture, walls, and — critically — **actor and camera positions and paths** marked. It's where the director plans **blocking** (where people move and stand) and where the camera goes, in advance, so the shoot doesn't dissolve into on-the-day improvisation. It also enforces the **180-degree rule** spatial logic (see `10-editing-theory.md`): you plot the axis of action on the diagram so coverage will cut together.

### Location Scouting, Casting, Schedule, Budget

- **Location scouting** finds and documents real places; the deliverable is photos, light conditions, logistics, permits.
- **Casting** matches faces and voices to roles; the deliverable is locked cast.
- **The schedule** orders the shoot for efficiency, *not* story order — all scenes at one location are shot together regardless of where they fall in the film. The daily distillation is the **call sheet**: who, where, when, what scenes, sunrise/sunset, contacts. The call sheet is the single most important operational document on any shoot.
- **The budget** is the constraint everything else negotiates against.

**The deliverable of pre-production:** a complete, approved plan — breakdown, shot list, storyboard, **animatic**, look book, floor plans, schedule, budget — such that production is execution, not invention.

#### → AI APPLICATION
This is where the AI pipeline most directly mirrors the human one, stage for stage:

- **Breakdown → structured extraction.** Feed the script to an LLM and ask for a JSON breakdown: per scene, list characters present, location, time of day, key props, and required visual continuity (what each character is wearing, lighting state). This becomes your continuity database — the thing that keeps shot 47 consistent with shot 3.
- **Shot list → LLM + craft vocabulary.** Have the LLM propose a shot list using the framing/angle taxonomy, then *you* edit it. The model is good at completeness, mediocre at taste.
- **Storyboard → image model.** Generate one keyframe per shot with an image model. As of mid-2026 the decisive criterion is **character consistency across panels**: Nano Banana 2 / Nano Banana Pro (Google's Gemini-based image model) leads here, maintaining facial identity across many generations via a multi-image reference engine (~14 reference images), whereas Midjourney v7's Omni Reference holds style well but drifts on identity by the third or fourth scene *(verify — fast-moving)*. Generate every panel from the **same locked character references** so your storyboard is already consistent. This *is* your look book's enforcement mechanism.
- **Animatic → stills + TTS + timing.** This is the keystone AI step and the cheapest it has ever been. Take your storyboard stills, add the ElevenLabs scratch voiceover from the table-read step, drop a temp music bed, and assemble them at intended durations in an NLE or, natively, in **HyperFrames** (HTML/GSAP compositions where you control exact per-shot timing, see the `hyperframes` skill). You now have a watchable cut of the entire film *made entirely of still images and temp audio* — for pennies and an afternoon. Watch it. Fix the pacing. Watch it again. Only then generate a single second of real video.
- **Look book → reference image set + palette.** Curate or generate reference frames and extract a palette; carry it forward as prompt language and (later) as a LUT.
- **Floor plan / blocking → text spatial spec.** Even without rendering, write the spatial logic down (camera left/right, who's on which side of the axis) so your generated shots cut together and don't flip the line.
- **Casting → locked character references.** "Casting" in AI is generating and *freezing* a reference image (or several angles) of each character. This locked set is the most important asset you own; everything consistent flows from it.

---

## PRODUCTION — Capturing the Material

On a real set, production is about getting *enough usable material* to cut a scene that works, while protecting the ability to assemble it later.

### Blocking, then Coverage

**Blocking** is rehearsed on the day — actors and camera find their final positions. Then the scene is shot multiple times from multiple setups. This is **coverage**, and understanding *why* you shoot coverage is essential:

> **A scene is not filmed; a scene is *covered* — shot from enough angles that it can be assembled, re-paced, and rescued in the edit.** You do not know in the edit room exactly which performance beat, on which line, from which angle, will work. So you protect yourself by capturing options.

The classic coverage pattern:

| Coverage element | What it is | Why you shoot it |
|---|---|---|
| **Master shot** | The whole scene, start to finish, wide enough to see everyone | The spatial backbone — establishes geography and is the safety net you can always cut back to |
| **Singles / OTS** | Each actor alone, or over-the-shoulder | The emotional close work — where performance actually reads |
| **Inserts / cutaways** | Hands, objects, a clock, a reaction | The connective tissue — lets the editor compress time, hide cuts, and redirect attention |

The reason for the master-then-singles ritual is **editorial freedom**: with a master plus matched singles, the editor can build the scene at any rhythm, fix a flubbed line by cutting away, and control exactly when we see each face. Shoot only one angle and you've made every editing decision on set, forever, with no recourse.

### Continuity / Script Supervision

The **script supervisor** tracks continuity (which hand held the glass, how full it was, where eyelines pointed, what's been covered) and logs every take. This is what makes shots from different setups — and different days — cut together without the audience seeing the seams. It is the unglamorous discipline that prevents the jump where a character's cigarette teleports between cuts.

### The Slate, and Multiple Takes

The **slate** (clapperboard) names the scene, shot, and take and provides the clap that syncs picture to separately-recorded sound. **Multiple takes** exist because performance is variable and you're buying options — take 1 might have the best first half, take 6 the best ending; the edit stitches the best of each.

**The deliverable of production:** logged, slated, covered footage — enough usable material, with continuity intact, to cut every scene.

#### → AI APPLICATION
The single most important conceptual transfer from production to AI is **coverage**. The amateur AI move is to generate one clip per beat and stitch them. The professional move is to **generate multiple shots per beat** — a wide "master," tighter "singles," and inserts — exactly as a set would cover the scene, giving your edit real options and the ability to cut for rhythm (see `10-editing-theory.md`). Concretely:

- **Generate coverage, not single clips.** For each storyboard beat, produce a wide establishing shot and 2–3 tighter angles. The current top video models — **Google Veo 3.1** (strongest all-rounder, best prompt adherence and native audio, 4K), **Kling 3.0** (cinematic motion, multi-shot storyboard mode with audio sync across cuts, cheapest premium tier ~$0.10/sec), **Runway Gen-4.5** (granular control: camera moves, motion brush, reference-driven consistency), and **Seedance 2.0** (native multi-shot with synchronized audio) — increasingly support multi-shot consistency natively, but you should still generate redundant angles and *select* in the edit *(model landscape verified June 2026; changes monthly — verify)*.
- **Multiple takes = multiple seeds.** Re-run each shot with several seeds/variations. Generation is non-deterministic; treat each generation as a "take" and pick the best, just as an editor selects among set takes.
- **Continuity = locked references + a tracked continuity sheet.** Carry the character/location reference images into every generation and maintain the breakdown's continuity database (wardrobe, time of day, lighting) as the prompt spec. This is your script supervisor.
- **Slate = disciplined file naming and metadata.** Name every generation `scene_shot_take_seed` and log the prompt. Your slate is your filename convention; without it, the "edit" stage drowns.
- **Note:** OpenAI's Sora consumer app and API were sunset in 2026 (app April, API September), so do not architect around it *(verify)*.

---

## POST-PRODUCTION — Assembling the Film

Post is where the film is actually *made* in the sense that matters — the same footage can become a masterpiece or a mess depending entirely on the edit.

### Ingest / Logging → Assembly → Rough Cut → Picture Lock

- **Ingest & logging** — all footage is imported, organized, transcoded, and tagged. You cannot edit what you can't find; logging is the boring foundation of speed.
- **The assembly** — every chosen take laid end to end in script order. Long, rough, complete. The deliverable is "all the pieces are here and in order."
- **The rough cut** — the assembly shaped: scenes trimmed, structure tested, pacing found. Most of the film's quality is decided here (see `10-editing-theory.md` on rhythm and the cut).
- **Picture lock** — the edit is frozen. This is a hard gate: **everything downstream (sound mix, music, color, VFX, titles) is timed to the locked edit**, so changing a single frame after lock means re-doing work in every department. Lock is the contract that lets the finishing crafts begin.

### Sound Design & Mix, Music, Color Grade, VFX/Titles

These run *after* lock, often in parallel:

- **Sound design & mix** — building and balancing dialogue, foley, ambience, and effects. Sound is half the experience and the half audiences don't consciously notice; it carries emotion and realism more than most realize.
- **Music** — score and/or licensed tracks, composed or placed to the locked timing.
- **Color grade** — the final color relationship across the film: matching shots, then authoring the look (see `08-lenses-lighting-color.md`). The grade is where disparate footage becomes one coherent world.
- **VFX & titles** — effects, cleanup, and the title/credit design.

### Mastering & Delivery Specs

The final stage is **mastering** to platform-specific **delivery specifications** — and these are exact, not approximate. Getting them wrong gets your file rejected or silently re-compressed into mush.

| Platform | Aspect / Resolution | Frame / bitrate guidance | Loudness target |
|---|---|---|---|
| **YouTube (long-form)** | 16:9, deliver 4K (3840×2160) even from 1080p source — the encoder allocates more bitrate to 4K-tagged uploads | ~30 Mbps for 1080p, ~80 Mbps for 4K; H.264/H.265 | ≈ −14 LUFS integrated |
| **YouTube Shorts** | 9:16, 1080×1920, ≤3 min | ≥8 Mbps for 1080p | ≈ −14 LUFS |
| **TikTok** | 9:16, 1080×1920, ≤10 min, file <150 MB | 8–15 Mbps (below 5 = quality flag, above 20 = flattened); H.264/H.265, AAC 44.1 kHz | −14 LUFS integrated, −1 dBTP true peak |
| **Instagram Reels** | 9:16, 1080×1920 | keep file <50 MB to avoid heavy re-compression; H.264 | ≈ −14 LUFS |

*(Specs verified June 2026; platforms change these — verify before final delivery.)* The recurring −14 LUFS target across platforms is not coincidence: it's the de-facto streaming loudness standard, and mastering louder just gets your audio turned down (and squashed) by the platform's normalizer. Master to spec, not to "loud."

**The deliverable of post:** a mastered file (or set of files) that meets each target platform's exact spec.

#### → AI APPLICATION
- **Ingest/logging → asset management.** Your "footage" is your generated clips, named by the slate convention. The logging discipline from production pays off here.
- **Assembly → rough cut → lock in HyperFrames / NLE.** Assemble the selected generations in script order, then shape. Because you built an **animatic first**, the rough cut is largely a matter of swapping each still for its finished video clip into a structure you already proved — this is the entire payoff of animatic-first work. HyperFrames gives you code-level control of timing and transitions; a traditional NLE (Resolve, Premiere) is the alternative.
- **Sound → ElevenLabs (voice/SFX) + Suno or ElevenLabs Music.** Replace scratch voiceover with final ElevenLabs vocals; generate the score with **Suno v5** (current quality leader for full songs with vocals) or **ElevenLabs Music v2** (built on licensed data, strongest vocal realism, mid-track genre switching and section inpainting) *(verify)*. Then *mix* — balance VO against music; don't let an AI music bed bury dialogue.
- **Grade → LUT or code.** Apply a consistent grade across all clips: a **LUT** (lookup table — a file that maps input colors to graded output) in your NLE, or color transforms in code/CSS if finishing in HyperFrames. Carry the look book's palette through to the grade so the film reads as one world.
- **Master → render per platform from one source.** Export each delivery spec from the single locked timeline — 16:9 master plus 9:16 reframe — normalizing to −14 LUFS. HyperFrames renders to MP4/WebM/MOV at arbitrary framerate; pair with the delivery table above.

---

## The Pipeline at a Glance — Human Stage → AI Step

| Phase | Human stage | Deliverable | AI-native step |
|---|---|---|---|
| Develop | Idea / premise | A "what if" | LLM ideation + **adversarial grilling** |
| Develop | Logline | One-sentence engine | LLM, then attack it for genericness |
| Develop | Treatment | Prose synopsis | LLM draft + fresh-context critique pass |
| Develop | Screenplay | Formatted script | LLM in Fountain (diffable) |
| Develop | Table read | Diagnostic of unsayable lines | TTS read-aloud (ElevenLabs voices) |
| Pre | Breakdown | Tagged elements per scene | LLM → JSON continuity database |
| Pre | Shot list | Every camera setup | LLM + craft vocab, human-edited |
| Pre | Storyboard | Panel per shot | Image model (Nano Banana Pro), locked refs |
| Pre | **Animatic** | **Timed boards + scratch audio** | **Stills + TTS + temp music in HyperFrames/NLE** |
| Pre | Look book | Visual language | Reference image set + palette |
| Pre | Floor plan / blocking | Spatial + axis logic | Text spatial spec (preserve the line) |
| Pre | Casting | Locked cast | Frozen character reference images |
| Pre | Schedule / call sheet | Shoot order | Generation queue / batch plan |
| Prod | Coverage | Master + singles + inserts | **Generate multiple shots per beat** |
| Prod | Multiple takes | Performance options | Multiple seeds per shot |
| Prod | Continuity / supervision | Seamless cuts | Locked refs + tracked continuity sheet |
| Prod | Slate | Sync + identification | Filename convention `scene_shot_take_seed` |
| Post | Ingest / logging | Findable footage | Named asset library |
| Post | Assembly → rough cut → lock | Frozen edit | Assemble generations; lock before finishing |
| Post | Sound design & mix | Balanced audio | ElevenLabs VO/SFX, then mix |
| Post | Music | Score | Suno v5 / ElevenLabs Music v2 |
| Post | Color grade | Coherent look | LUT or code transforms |
| Post | VFX / titles | Effects + credits | Image/video model + HyperFrames titles |
| Post | Master / delivery | Spec-compliant files | Per-platform render, −14 LUFS |

---

## The One Lesson: Animatic-First Discipline

If you internalize a single principle from this entire chapter, make it this: **build the whole film cheaply before you build any of it expensively.**

The professional pipeline is, at its heart, a machine for moving every consequential decision *upstream*, to the stage where changing your mind is free. The animatic is the apex of that machine — it is the first moment the film exists *in time*, and time is where stories live or die. Pixar will revise a story reel forty times before rendering one final frame, not because they're cautious, but because they understand that the reel answers the only question that matters — *does it play?* — at a thousandth of the cost of the answer you'd get from the finished film.

AI changes the economics of every stage except this one. Generation is cheap, fast, and re-runnable — which seduces the beginner into skipping straight to "make the video," generating a hundred gorgeous, contradictory, badly-paced clips and trying to rescue them in the edit. That is shooting without coverage, editing without an assembly, and finishing without a lock, all at once. The discipline that separates authored AI films from the generic slurry is unromantic: **write it, grill it, board it with locked references, cut a stills-and-TTS animatic, watch it, fix the pacing — and only then generate a single second of real footage.** Prove the film as a cheap thing before you commit to it as an expensive one. The model is your camera; the animatic is your mind made watchable. Respect the order, and the order will carry the work.

---

### Sources

- [Best AI Video Generators 2026: Sora 2 vs Veo 3.1 vs Kling 3.0 vs Runway — Get AI Perks](https://www.getaiperks.com/en/blogs/44-best-ai-video-generators-2026)
- [Text-to-Video AI Rankings May 2026 — Sora 2, Veo 3.1, Kling 3.0, Runway](https://freevideogenerator.io/text-to-video-leaderboard)
- [AI Video Generation 2026: Sora 2 vs Veo 3.1 vs Kling 3.0 — Lushbinary](https://lushbinary.com/blog/ai-video-generation-sora-veo-kling-seedance-comparison/)
- [Best AI Music Models 2026: Suno v5 vs ElevenLabs — TeamDay.ai](https://www.teamday.ai/blog/best-ai-music-models-2026)
- [ElevenLabs Music V2 vs Suno AI (2026) — MindStudio](https://www.mindstudio.ai/blog/elevenlabs-music-v2-vs-suno-ai-comparison-2)
- [Nano Banana 2 vs Flux 1.1 Pro vs Midjourney v7 — Starkie.ai](https://starkie.ai/articles/nano-banana-2-vs-flux-pro-vs-midjourney-v7-realistic-ai-portraits)
- [TikTok Video Specs 2026 — Xroad Studio](https://xroadstudio.com/platform-specs/tiktok)
- [Social Media Video Specs — Sendible](https://www.sendible.com/insights/social-media-video-specs)
- [Best DaVinci Export Settings for YouTube, Instagram, TikTok 2026 — Pixflow](https://pixflow.net/blog/davinci-resolve-export-settings/)
- [What is an Animatic? — Celtx Blog](https://blog.celtx.com/?p=13141)
- [How Previsualization Shapes Film & VFX Production — Hitem3D](https://www.hitem3d.ai/blog/What-is-Previsualization-Previs-in-Film-A-Complete-Guide/)
- [Pixar Animation Process (story idea → reel)](http://dreamco.com/pima/wp-content/uploads/2018/03/pixar-animation-process.pdf)
